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
<img src="https://cdn4.telesco.pe/file/arvuIXHOnT2XDcLwFDYTz8STN5xnBOM_mccJS2aPwMGONRwUZJitEb63BGHXJ3ULkSNx9vSxSWiP8TQ8X-xDaquvu3rtZ1Dykk70lpvBDJ_XWzLa6M2u_XHmQ4V3zH8yX5RFgsjkM6VMatIx9E2gE-n2FQAf0vtLA8pr8EOKAfyIBMUONcIYgkZU87QJ7Pg711PA9gA40pslsQ8f6joaxR2nSQnxXhjyKXScJv2G5u1F1hmz00NJ1sx7qhRHQKD8DZ-nPHjuAswXZY_619IcUd__BqxsFa22iV2lFxphFN93FFWRlkLn6amU4AWTsPTM0GJO5yhd7aQGhOH8mc48_Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 02:24:45</div>
<hr>

<div class="tg-post" id="msg-452188">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5526e06d52.mp4?token=eGKjexKzHdeShfw_V1uFSabQgQ7jrNEDgRG2FiAVimLv_9oDE_1W4Fc_Ns0VME_sIUZrwohGUFEfuzxkaLN31Xz9kgWXnlFnsrjMTvFK-al_TLv0zu1xUxumF1mclV7C-GN7q5KVJJsOS1UVC0GSsSTLOE9VTjZ6MkQ02tQbmOoRCDg1bc7sq157V7kLiPpyu54ew0NEgbflemuEhFvVcoWKWyoZgFxmysK2YymjogVep96g1jVtvhoZatjzlwkxe5-QPhEBM3-6ndR-B1A8v1M2T4JlP3mxfEH8tgMVY0h77B-wbNnzXjGMV4_GNGXEUZohCZ5dfGRzbkYC5QHTnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5526e06d52.mp4?token=eGKjexKzHdeShfw_V1uFSabQgQ7jrNEDgRG2FiAVimLv_9oDE_1W4Fc_Ns0VME_sIUZrwohGUFEfuzxkaLN31Xz9kgWXnlFnsrjMTvFK-al_TLv0zu1xUxumF1mclV7C-GN7q5KVJJsOS1UVC0GSsSTLOE9VTjZ6MkQ02tQbmOoRCDg1bc7sq157V7kLiPpyu54ew0NEgbflemuEhFvVcoWKWyoZgFxmysK2YymjogVep96g1jVtvhoZatjzlwkxe5-QPhEBM3-6ndR-B1A8v1M2T4JlP3mxfEH8tgMVY0h77B-wbNnzXjGMV4_GNGXEUZohCZ5dfGRzbkYC5QHTnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تردد روان زائران امام حسین(ع) از مرز مهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/farsna/452188" target="_blank">📅 02:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452187">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d8c129d3.mp4?token=PW2ACRNgA_5q-fG_ZJYwyT6pn1xHw60sz1QYOKIVtmBizQBuci645dfPMteHFIqThhZr4idl6MTzWE5EzHFm7kUJ7tiiTi4Yw8s3Z4t_76rDdgFeMWoPepCSt5-4YEiqu-uPVnrYLU7w-gC5tQaQrOjh6eXXDncPYQK6yyzxv59NQSiRWio42N-d1Z2Jeu_uXv7fOQjDU2kxR51QnNW0wIbMSMgww_peBO4A63YT-ijvDy1NB_7DdHliDvsMhd4cgET9-_pD-67lm_gvJjOcHnYryCPnMj4AghLkGQsRSdCMDfiZZQSbySbUVkQepuHR3QW96YkKHT1QAuEQxSdU8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d8c129d3.mp4?token=PW2ACRNgA_5q-fG_ZJYwyT6pn1xHw60sz1QYOKIVtmBizQBuci645dfPMteHFIqThhZr4idl6MTzWE5EzHFm7kUJ7tiiTi4Yw8s3Z4t_76rDdgFeMWoPepCSt5-4YEiqu-uPVnrYLU7w-gC5tQaQrOjh6eXXDncPYQK6yyzxv59NQSiRWio42N-d1Z2Jeu_uXv7fOQjDU2kxR51QnNW0wIbMSMgww_peBO4A63YT-ijvDy1NB_7DdHliDvsMhd4cgET9-_pD-67lm_gvJjOcHnYryCPnMj4AghLkGQsRSdCMDfiZZQSbySbUVkQepuHR3QW96YkKHT1QAuEQxSdU8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عربی: گزارش‌های اولیه از سقوط یک هواگرد در آسمان جزیرۀ قشم حکایت دارد.  @Farsna</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/farsna/452187" target="_blank">📅 02:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452186">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
منابع عربی:
گزارش‌های اولیه از سقوط یک هواگرد در آسمان جزیرۀ قشم حکایت دارد.
@Farsna</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/452186" target="_blank">📅 01:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452185">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-LMzvXfPoXf5fQEMvy144UxQtzZ8Iub69gnRvp-i7oN0u5H4llmS7GuG9ixL5jm6PV13pQAKNbIG7t5pUxrfdbvY4ksmQAG00tnBguGuTKvcMBELstOdeKdrZs9CyJqb30mPdWgMo3EOqaMSFFumY8FV4Se0W0fezbiXyxgy6t5Yy3DELQNoUo9BQzK_gSl2yt_AdCnsTKniIeTrf-l_1bq7jR1tIF9Ven59W6PdA2895aiSaFo69SZ3iFlybvNYUTRLa8NMVZY29Z5DceqeaFUNRmMZ4eLCAs2ev7T8XeK8k2TlQaRwBdDfOydZ6YHq141DPPbZhAHInpXIqyKvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دوباره به لفاظی علیه ایران رو آورد
🔹
درحالی‌که مقام‌های آمریکایی بارها مدعی شده‌اند ایران هیچ تسلطی بر تنگۀ هرمز ندارد و آمریکا «کنترل کامل» این آبراه را در اختیار گرفته است، اکنون با تداوم تحولات میدانی و ناتوانی آمریکا در مقابل حملات ایران، رئیس‌جمهور…</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/452185" target="_blank">📅 01:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452184">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">مقر فرماندهی نیروی زمینی کویت هدف حمله قرار گرفت
🔹
المیادین به‌نقل از منابع امنیتی عربی گزارش داد که گروه‌های مقاومت روز گذشته ساختمان فرماندهی نیروهای زمینی در کویت را هدف حمله قرار داده‌اند.
🔹
گفته می‌شود نیروهای مستقر در این مقر،
گذرگاه مرزی شلمچه
را هدف قرار داده بودند.
🔹
به گفته منابع امنیتی مذکور، این حمله خسارت‌های سنگینی به ساختمان فرماندهی نیروهای زمینی وارد کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/452184" target="_blank">📅 01:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452183">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00627875b0.mp4?token=nzbN2bvJObkJxs2KlHJLKLm_dFohXP_zSowhcThRcK0U8m6GeK2_p_DL5YopbcCW4T1YKJj7HlfOCMzifp23reyKLHRdbC979SKm9-sA_ebZkxH4uvpobz_vmlA5TVCPmYqyrVdhV3uLOVi2E6VX5x8wbYonIPoencpq2xjqvvCs-Ro2uu6UDaqJcnojmAgpFWmDAj4veVTHbZYgUdxivWchTbmCaSLDWuqDL6HjB3fAGH3gJ9ZcjFA8N-wmjoUtLuqaHJHGa3Z-02cXrCARajJbH46dh9FX0UdAZFbMlg9TWPffnrWUDGN4JiNi4ZUX3hQhv4jgq9gfl80kF9GQ3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00627875b0.mp4?token=nzbN2bvJObkJxs2KlHJLKLm_dFohXP_zSowhcThRcK0U8m6GeK2_p_DL5YopbcCW4T1YKJj7HlfOCMzifp23reyKLHRdbC979SKm9-sA_ebZkxH4uvpobz_vmlA5TVCPmYqyrVdhV3uLOVi2E6VX5x8wbYonIPoencpq2xjqvvCs-Ro2uu6UDaqJcnojmAgpFWmDAj4veVTHbZYgUdxivWchTbmCaSLDWuqDL6HjB3fAGH3gJ9ZcjFA8N-wmjoUtLuqaHJHGa3Z-02cXrCARajJbH46dh9FX0UdAZFbMlg9TWPffnrWUDGN4JiNi4ZUX3hQhv4jgq9gfl80kF9GQ3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهید حاج قاسم سلیمانی: با وحدت باید دست همدیگر را بگیریم
🔹
ما امروز بیش از هر زمانی نیازمند وحدت‌نظر هستیم؛ ما در این پیچ خطرناک انقلاب، و در نزدیک این قلۀ بلندی که می‌خواهیم به آن دسترسی پیدا بکنیم که پرتگاه‌های عظیمی دارد، نیازمند این هستیم که دست همدیگر را بگیریم؛ نه اینکه در ستون‌های پراکنده حرکت بکنیم.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/452183" target="_blank">📅 01:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452182">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa389de510.mp4?token=kQeSVyZMfuAYEGiuhsZ8xPlGouvMuk0eWpy6TR2h5heppPLDWorKv3YjlWAWI4KBbuUai_a7rkREvtMSKUbKMomCrqKpKq4pW-irVaGhW-8KzZ_9DX-dUMfvaHOcuz65-D7x9vr9vrt0OTQq4uBkj-SNWxbFksvOcOAgs9dyWVqQ2R8eX6akaUHGzXZPsHfcMKA5lxkBUYQ0wypXgGF4TRsDKPNxz-dX-ooYy-xgS0xfQhBnDRI1z0_0IYy4yFyHtYVBpb_GFxs8M1-tUZVZn3ZWOZNIbYDtwjzKmJHjmiDxgtCclRGDDLrkiyl6LFTHfDHVFhyr5bUkCv6QBV6ypw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa389de510.mp4?token=kQeSVyZMfuAYEGiuhsZ8xPlGouvMuk0eWpy6TR2h5heppPLDWorKv3YjlWAWI4KBbuUai_a7rkREvtMSKUbKMomCrqKpKq4pW-irVaGhW-8KzZ_9DX-dUMfvaHOcuz65-D7x9vr9vrt0OTQq4uBkj-SNWxbFksvOcOAgs9dyWVqQ2R8eX6akaUHGzXZPsHfcMKA5lxkBUYQ0wypXgGF4TRsDKPNxz-dX-ooYy-xgS0xfQhBnDRI1z0_0IYy4yFyHtYVBpb_GFxs8M1-tUZVZn3ZWOZNIbYDtwjzKmJHjmiDxgtCclRGDDLrkiyl6LFTHfDHVFhyr5bUkCv6QBV6ypw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: نفت ونزوئلا حق مسلم ماست
🔹
ما به لطف ونزوئلا پول زیادی به‌دست می‌آوریم. حق مسلم ماست که این را داشته باشیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/452182" target="_blank">📅 01:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452181">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hw_0okxIySYqANsb420uSuNjDWlXMVCtuXdukUwsQdWPxfKI9YOODMvbwTmVRDMs9HCvX8E2-hwp-mryFAVDKosv3nkvDtcxTJ9gTu7HCvb7UCAzCJjrgdyn0CDAfBjDs3n1BtmxyzlR0jQ9FAvptOzsT9TYEbEZtdwcvSHI9eU0wE80d6un3DpXiKp5KrgbAuNyGXvOhjWgzbdsBuw_hwpbZLafYv8EZAGEZex_f0rNMiTrpDRuYyyt-PWPDoyR9s3fDJO_pGdDmVb61NEZj9bGPN8njT--mtiaHAxiSSzVhgTlWY1TgEFcwFsY7asVr5Lr46hC3VmOyAVJzegbvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انهدام موشک آمریکایی در آسمان کهنوج کرمان
🔹
فرماندۀ سپاه کهنوج: یک فروند موشک تاماهاک آمریکایی در آسمان این شهرستان رهگیری و منهدم شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/452181" target="_blank">📅 00:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452180">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62818e5d54.mp4?token=MfvwP5JAtFlZdJFYOPptBEJECJ0jgrwuq2t8qfTv_VFWLlAmy_H-vgNhewi3SFdU_hnahHQSyjF4wS5V0Yq7PlxnkMgfyOtEe5ezoQv7TQJ_DMW2gTof3tEB7_caMO0NRfwDL42sY-d8Gr3LmUSxXAzn1oy9fTp2tonPARbXFCjZPzJrEPY1hEtgDYKjeThDZzMJBtGuw7TKLR7iBoGZWWhdsLDfiJC1xYmUx02VhqcCJkOJkO7nE70I-YBI-1CBYt1fYtOfo9DKl5YGYA32fRou_x1cSv15tv9EmKhFnraFU6Ew3q2tuMVaNLZYb2_BQesAlPlwiGzh-dbj_wOXUjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62818e5d54.mp4?token=MfvwP5JAtFlZdJFYOPptBEJECJ0jgrwuq2t8qfTv_VFWLlAmy_H-vgNhewi3SFdU_hnahHQSyjF4wS5V0Yq7PlxnkMgfyOtEe5ezoQv7TQJ_DMW2gTof3tEB7_caMO0NRfwDL42sY-d8Gr3LmUSxXAzn1oy9fTp2tonPARbXFCjZPzJrEPY1hEtgDYKjeThDZzMJBtGuw7TKLR7iBoGZWWhdsLDfiJC1xYmUx02VhqcCJkOJkO7nE70I-YBI-1CBYt1fYtOfo9DKl5YGYA32fRou_x1cSv15tv9EmKhFnraFU6Ew3q2tuMVaNLZYb2_BQesAlPlwiGzh-dbj_wOXUjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پایان معطلی زائران در مرز خسروی با تردد یکسرۀ تهران-کربلا
🔹
با اجرایی‌شدن طرح تردد یکسره، اتوبوس‌های تهران-کربلا بدون نیاز به پیاده‌شدن مسافران از مرز عبور می‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/452180" target="_blank">📅 00:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452179">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">انتقال تروریست‌های زخمی آمریکایی به آلمان، در پی حملات پهپادی و موشکی ایران
🔹
یک مقام نظامی آمریکایی به نیویورک‌تایمز گفت: در این ماه نزدیک به دوازده نظامی در پی حملات موشکی و پهپادی ایران در اردن و سایر کشورها به شدت مجروح شده‌اند؛ به‌طوری که برای درمان با هواپیما به یک بیمارستان نظامی در آلمان منتقل شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/452179" target="_blank">📅 00:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452178">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
شنیده‌شدن صدای دو انفجار در محدودۀ روستای مسن قشم
🔹
دقایقی پیش دو انفجار در منطقۀ مسن جزیرۀ قشم شنیده شده است.
🔹
همچنین مردم قشم صدای انفجارهایی را از محدوده تنگۀ هرمز در جنوب جزیرۀ لارک و هنگام شنیده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/452178" target="_blank">📅 00:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452177">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
برخی منابع عربی از آتش‌سوزی در بزرگترین نیروگاه برق کویت در پی اصابت یک پرتابه خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/452177" target="_blank">📅 00:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452176">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b515e51b39.mp4?token=aCNRejehRUKuGyuiCB65Ab2_uckf-2LDQSjgsIaiNYVPQRhKC26YuNmENIZM4Kb9otDFEhIPoWEMxpN6H5yD7GOG-qLHPCsMgMkSt7-MnQCQFny15p-1GAAXhyT5_gOk7cyMz2asPK-wq9ZOD8Bqs1sr9VzfoRtQvY2F_RXNM4hK21iitszaDIHf81bZcIfGMuCbTd-FkPD8JEZ92wYbE8nrlraDTKgy0ggoozURg2cySlGRpIYpZbW2X8D--idbqtagHY8ja79rsKg7E03-UexsfUmECbO68H9GtDYtfIokCLdHrRMpwP6YpRVAMTQhj0pv20ertOoJAIvFGgzqvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b515e51b39.mp4?token=aCNRejehRUKuGyuiCB65Ab2_uckf-2LDQSjgsIaiNYVPQRhKC26YuNmENIZM4Kb9otDFEhIPoWEMxpN6H5yD7GOG-qLHPCsMgMkSt7-MnQCQFny15p-1GAAXhyT5_gOk7cyMz2asPK-wq9ZOD8Bqs1sr9VzfoRtQvY2F_RXNM4hK21iitszaDIHf81bZcIfGMuCbTd-FkPD8JEZ92wYbE8nrlraDTKgy0ggoozURg2cySlGRpIYpZbW2X8D--idbqtagHY8ja79rsKg7E03-UexsfUmECbO68H9GtDYtfIokCLdHrRMpwP6YpRVAMTQhj0pv20ertOoJAIvFGgzqvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایران دیروز به کدام اهداف آمریکایی حمله کرد؟
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/452176" target="_blank">📅 00:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452175">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5eeb7e5a47.mp4?token=ko2uqSPtk79LS7p76ld50PBoiDKK1jNPCofN6fm9BxsnYpqeqYg5RvWwghZVngiHuMMQ0Eu9lEUwSBwg1xX5OtsbvS8kCbSdjtG1dhOEGg7cCD3ovDEHQVIz5r_tFhAFaAZavuqTLYr1JBRFKY5N7jItIFAqINWRsWlzVXuA4hAy4BTEypyzLEcr3fwPPCdSu9vuSe3KiVGLRMTS5MQwJpDS4rpJR7TNzvy6QZJ61Zv6K7N8IWC7Gf3BHd30tj4ioTh8009ge_D5TtxUlDd_RW1Zl7dwKRtzxzqCU4EHVps8K24YR5OReXJqi3xzPiT3Ppd80aJCWUr8z0mncsS4BnkxmNRcc0gBf8doROECnIbKXMC0Rvp9H7BNSVl3pbVY9Lrjlqoov8CxYyovNeb5tk6R7OqATDr9y4z3TmsqCRI9--sbisa5MK9vdZDGopDkhmtuYFBpZob137uzBbwiuEaJPsEJbRc8ciGgf0Kx-nHuYo4LYQst7qCpdQfLXJpG-TZFv-36Yr8y4R3Ic4SadiYzw1WkW3DpY03fduvj4XwZlfZECurlawGWjJrM4NZ8JsAbq3R6DHQsAIsyJEVsTSk7kIQbv37y2YnEu_EYFIGPvvX_o53HU8dh0YueYQeYNGegMhsqUikuaahVxidxGDerQJIfNXCgN43cDfUGRKY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5eeb7e5a47.mp4?token=ko2uqSPtk79LS7p76ld50PBoiDKK1jNPCofN6fm9BxsnYpqeqYg5RvWwghZVngiHuMMQ0Eu9lEUwSBwg1xX5OtsbvS8kCbSdjtG1dhOEGg7cCD3ovDEHQVIz5r_tFhAFaAZavuqTLYr1JBRFKY5N7jItIFAqINWRsWlzVXuA4hAy4BTEypyzLEcr3fwPPCdSu9vuSe3KiVGLRMTS5MQwJpDS4rpJR7TNzvy6QZJ61Zv6K7N8IWC7Gf3BHd30tj4ioTh8009ge_D5TtxUlDd_RW1Zl7dwKRtzxzqCU4EHVps8K24YR5OReXJqi3xzPiT3Ppd80aJCWUr8z0mncsS4BnkxmNRcc0gBf8doROECnIbKXMC0Rvp9H7BNSVl3pbVY9Lrjlqoov8CxYyovNeb5tk6R7OqATDr9y4z3TmsqCRI9--sbisa5MK9vdZDGopDkhmtuYFBpZob137uzBbwiuEaJPsEJbRc8ciGgf0Kx-nHuYo4LYQst7qCpdQfLXJpG-TZFv-36Yr8y4R3Ic4SadiYzw1WkW3DpY03fduvj4XwZlfZECurlawGWjJrM4NZ8JsAbq3R6DHQsAIsyJEVsTSk7kIQbv37y2YnEu_EYFIGPvvX_o53HU8dh0YueYQeYNGegMhsqUikuaahVxidxGDerQJIfNXCgN43cDfUGRKY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عبدالله روا: ای کاش از اول به حرف رهبر گوش داده بودیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/452175" target="_blank">📅 23:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452171">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O-qTN1s4Iq6CPMm3YA9k-i6sjTLPKRIG1ve_JezVpYv1wy-opN3PbzdUjCuaTclKBqdPnLopPwZ3Q8w58XCPD2N-og3haQyovgFZ4Sfj8lPvZwpyRBnIoFPckqe8qztbGQE2WrOVUzzHjFWL2jiGCc2T-fJNLLu0loqQylAPjoD6goYoV8_NaHVwS2PCUGAi45__nzvlpeExz-OTwy8PZMWbUSAMLMzXTkfEhr0QxIwYZQmZ4xICqSkH_LxnJL_eokOLRLsj1lCKZW4eZzX4pLj-Qz7wAebFHiYbZ-P3Dg3J7bmb7R1BcHvP8muawlEeIIKUY7TpEcxq3hg5b4S6xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FCtk_5GGoE0o6rxbwd7yXvsyNVhYnMtLqIe6N4ySNkyo2tJ-rb7uv13cuhYr9IYKmQXLpFB7NR42GrQmrfgxwW1Mq7w1oFZwJLAomm6qc1YGcAAlc4WJmHekja-JTKv9BOBjlT95d15VMWaOes4EcM8yfiCjuwMiBWVR_lOOrwA_tfg_BInEM12ccTQ3i7xXSK1z_jDOVF96xLyB4INbddAfZ1wbms2aAdI3t_4TE8m7TohxFtFcS5322erTnTpzOMyKsURIKBUgDOxnJ7vEoVu4uhvR5Eq9dkSCbg3m_jGyE3gtzgusm9vv1Gkfle-a7nXOsR9pasGftrc2IOQxrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/noPTyAqAtdwMlg8WOelS6tk8fGBR12Qhx6zbS_ps5moqdIicic0OpgA4HTboQmhBh87VPxEhdZE9Ne9kH5Rqds1bmHhozCMYwukMKQQrTFstIotnK-pnjAuk8gvkIe0XQzCf_gvJsBCR1Uo5zcXd7_A44djSJuKcRTQjwgAtq2kq5Wy29Xt_03B4d6ESlkJz7BGNW1M7a9vSdtZNe94Mn5gwpQDkpbu-_rrdW73Jyr3_Fv2cV_8IrD_xJxq01FGnl-PupYyUl0HZm-wuvzoMw7tVWjQjylKMJ3_UYetRE-8FA8XEEblfzoAfZTSe1uzk1sbjxEopgDM3MVAgsgRxsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y3HIii8HicE46MsiWuPiVvzb_-Dd3sp-s_z_ucRKAnIAE6N9RyMGu5Ul7AaJFnQZ_fJrfQXYmk3NgJ9q71GcO66O604UEfd0M5gvFLGHrMxC6YRYGzJwQcjQfMbebRxKVljwDdUISaS3GHG6XbE6piRYFerRRNS87gdHYiSku3Zodn5SBEOwj5iiNcegQeNoXbk1G10Do1w89Tx60ynBhnRoDX9cAa4RRdJ1cGtWKAMrkpYKS3vy-6g--DvvupbkaavfPb6AS8Oa2HDssDfrur1rwsyD1gv8D4BqTLZ5Kv6zcbDVN5-0-tk2aQIuETl0Sg1OaYC8wtSPqStdYjUZoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
آیا نخست‌وزیر عراق حامل پیغامی از طرف آمریکایی است؟  @Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/452171" target="_blank">📅 23:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452170">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d25ecc3870.mp4?token=XSEds0_SJ15se9rkvWnRrFC7IiiwTXN1ON6aQRUEn5-x6-s-TrJTVDUIUvQKysmL4LeqPmIZqn_rgAZCCi3PFDgaTR0UAuQuhwdI8tgFbIJHQfUJ0J7-73oYgP_xJraq6X8v5grs0TqdupsNXYiGp9DzAv6J4N-RHLsmSbsEUPArkc_0ULeGUI9aG7S2ZcUkdB5RdvSlu9lY77Xc-XOcGHUpjGjyhWeVpxs1CouSBlszp34mv0gvYxPT7Te9ltoa4JPSikun_qbg3zgwXWoJ-HqdahmftFpgHywIEWRVFLvaFghxUm85uJ1DEbKZ-Pol9uqYisnLuSBrIHFdBFo8sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d25ecc3870.mp4?token=XSEds0_SJ15se9rkvWnRrFC7IiiwTXN1ON6aQRUEn5-x6-s-TrJTVDUIUvQKysmL4LeqPmIZqn_rgAZCCi3PFDgaTR0UAuQuhwdI8tgFbIJHQfUJ0J7-73oYgP_xJraq6X8v5grs0TqdupsNXYiGp9DzAv6J4N-RHLsmSbsEUPArkc_0ULeGUI9aG7S2ZcUkdB5RdvSlu9lY77Xc-XOcGHUpjGjyhWeVpxs1CouSBlszp34mv0gvYxPT7Te9ltoa4JPSikun_qbg3zgwXWoJ-HqdahmftFpgHywIEWRVFLvaFghxUm85uJ1DEbKZ-Pol9uqYisnLuSBrIHFdBFo8sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود خلبان محاصره‌شکن به فرودگاه امام
🔹
هواپیمای ایرانی که محاصره یمن را در میان بمباران فرودگاه الحدیده شکست، به تهران بازگشت و در فرودگاه امام به زمین نشست و خلبان و تیم پرواز آن وارد سالن فرودگاه شدند. @Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/452170" target="_blank">📅 23:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452169">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
انفجارهای شدید در کویت
🔹
منابع عربی از شنیده‌شدن صدای چندین انفجار شدید در کویت خبر می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/452169" target="_blank">📅 23:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452168">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
انفجارهای شدید در کویت
🔹
منابع عربی از شنیده‌شدن صدای چندین انفجار شدید در کویت خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/452168" target="_blank">📅 23:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452167">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27895f3cdb.mp4?token=m-7BBOQI1JTAzbka7AzpM1uOB4K7Whft8eg3oeN7u47yaDIQI38XPpTmsOLfiJdDrsdousviRxKWbZ-oggVUlgEvP6-i-3pBQEH-Qw2bfMAW7iMO3kCwohvt5UFMRO2EpUR29HohSln2-elgKlu3vrFDa5VpTahuGmBkETfJ7ahESWSv3DO1LK9kgys6O9_Kpcw7PkAnQFi6pZe6PJoqVpyOxOMPgYClhojt6nVrgeOu4FhWHafsmF3Ae5wD6q0ZR0PCDdHBSoZMyCy6niAUWQLU9dBtrGaLvyRaA89NVUZHVPvcSfxBiKtClSjI3LF5gudLJ9rOqdE4SXJzzTVIaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27895f3cdb.mp4?token=m-7BBOQI1JTAzbka7AzpM1uOB4K7Whft8eg3oeN7u47yaDIQI38XPpTmsOLfiJdDrsdousviRxKWbZ-oggVUlgEvP6-i-3pBQEH-Qw2bfMAW7iMO3kCwohvt5UFMRO2EpUR29HohSln2-elgKlu3vrFDa5VpTahuGmBkETfJ7ahESWSv3DO1LK9kgys6O9_Kpcw7PkAnQFi6pZe6PJoqVpyOxOMPgYClhojt6nVrgeOu4FhWHafsmF3Ae5wD6q0ZR0PCDdHBSoZMyCy6niAUWQLU9dBtrGaLvyRaA89NVUZHVPvcSfxBiKtClSjI3LF5gudLJ9rOqdE4SXJzzTVIaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ذوالفقار به میدان آزادی رفت!
🔹
موشک بالستیک ذوالفقار سپاه امشب در تجمع مردمی میدان آزادی تهران به‌نمایش درآمد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/452167" target="_blank">📅 22:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452166">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🎥
عملیات شکارِ ترامپ و نتانیاهو
🔹
انیمهٔ جدید از عملیات انتقام علیه وزیر جنگ آمریکا، نتانیاهو و ترامپ
@Farsna</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/452166" target="_blank">📅 22:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452165">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c40d7725da.mp4?token=kPCvm-Y392nKmt4fCklXLRgfgFOuRS12wYoMeY-eJYpgHGXKaGeE4lmAjijRkow-iwOKXYFzLlwkZ-xCvZns0vpGMWIMMCls9kL7tAD879Tmi0FYAZ1vmwt-JJM2zRE8jE0lt6Bz-QtMYBEk0YnoVPziXZbTTDHOt1JqjdcxjYKV42y9XckNcDZBHiKt5TP2TtNjZJzkhhdbsJymVs6vlNIYDjT6nVW89XTN-BtDnI6C4Yp_IyNOirDcM_mRepzP_xgLHYPy4Ydfiet0rM-MHP9FM6X_GfrAQ7ivPemZKgrm9CUyU5fTg165MRo2mI51SddXMxccENmMlZ5KM__qqIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c40d7725da.mp4?token=kPCvm-Y392nKmt4fCklXLRgfgFOuRS12wYoMeY-eJYpgHGXKaGeE4lmAjijRkow-iwOKXYFzLlwkZ-xCvZns0vpGMWIMMCls9kL7tAD879Tmi0FYAZ1vmwt-JJM2zRE8jE0lt6Bz-QtMYBEk0YnoVPziXZbTTDHOt1JqjdcxjYKV42y9XckNcDZBHiKt5TP2TtNjZJzkhhdbsJymVs6vlNIYDjT6nVW89XTN-BtDnI6C4Yp_IyNOirDcM_mRepzP_xgLHYPy4Ydfiet0rM-MHP9FM6X_GfrAQ7ivPemZKgrm9CUyU5fTg165MRo2mI51SddXMxccENmMlZ5KM__qqIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌بس ممنوع!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/452165" target="_blank">📅 22:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452164">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d132ac9d5.mp4?token=ajHVSEIErAiVCwjCsiHUQSc2XdvsnslafcW6kgCThZg_ZJeYzGFrnL3_zuFPNclsukTbSWyxFmP0x9qTppCUFd53Ze5l2Ha9jSCQm_M3I_pO2Nx2E2HQOq-NOB2tc2_zctuJEfEgUY7WVDM_HLyr2_INRkieAKRIQ5y0RQhY6QLW7RsvLWl8z72Sz5Lh5S08lfAGmDiLWjlo49h6PIkP6k0LNoU6ho05SP5e4PuKV_8JKXowS_XAmJU7QAOi0dm2LSZN1M0pdLdMA8QrpUTLTB6kmS7TYs6s1WPDIbv4gxEglFPTdrj6_tuZi_vZdPjaEYVLy3CduBLOT9jQwiuWSn4fKsrbK3P0zjxbZkfFC7vyr1F90p_R9fYxfnxzOcdUtB1IRD2XfxETwHP-Fjn52a-Bzcykahx-ioeJm9jX_yLO-kexRQBWdPgnEEd7OxaAtBBm0tqkgyxQSHx24YP0EmDbaPL88sNctemyXQKJD-4GD6eZKBaMosByJ4aJ9NRXR5scUDB0BJPwdUDsjGAJ4JGPe9qHEpwwkn7yp1bnceUDkFp8yMcaQsOhp6M5sktGR7zn_rTNECrGnFSlgzunkKTOh9Pe8K5IvGeW9HysyhJJRvkDVOaCNedGcmV4_Bz6Afuwl2s2YxEU0nUrWPmy-MOacLYU2h9bO-3mdA2DSrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d132ac9d5.mp4?token=ajHVSEIErAiVCwjCsiHUQSc2XdvsnslafcW6kgCThZg_ZJeYzGFrnL3_zuFPNclsukTbSWyxFmP0x9qTppCUFd53Ze5l2Ha9jSCQm_M3I_pO2Nx2E2HQOq-NOB2tc2_zctuJEfEgUY7WVDM_HLyr2_INRkieAKRIQ5y0RQhY6QLW7RsvLWl8z72Sz5Lh5S08lfAGmDiLWjlo49h6PIkP6k0LNoU6ho05SP5e4PuKV_8JKXowS_XAmJU7QAOi0dm2LSZN1M0pdLdMA8QrpUTLTB6kmS7TYs6s1WPDIbv4gxEglFPTdrj6_tuZi_vZdPjaEYVLy3CduBLOT9jQwiuWSn4fKsrbK3P0zjxbZkfFC7vyr1F90p_R9fYxfnxzOcdUtB1IRD2XfxETwHP-Fjn52a-Bzcykahx-ioeJm9jX_yLO-kexRQBWdPgnEEd7OxaAtBBm0tqkgyxQSHx24YP0EmDbaPL88sNctemyXQKJD-4GD6eZKBaMosByJ4aJ9NRXR5scUDB0BJPwdUDsjGAJ4JGPe9qHEpwwkn7yp1bnceUDkFp8yMcaQsOhp6M5sktGR7zn_rTNECrGnFSlgzunkKTOh9Pe8K5IvGeW9HysyhJJRvkDVOaCNedGcmV4_Bz6Afuwl2s2YxEU0nUrWPmy-MOacLYU2h9bO-3mdA2DSrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم امتداد مشت گره‌کردهٔ رهبرشان را هرشب در خیابان به‌نمایش می‌گذارند
@Farsna</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/452164" target="_blank">📅 22:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452163">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2dfb803e8.mp4?token=u68EK2NvOvQ76m9MzaGAssPi7ZCCLiM86HWkQ7esJdfppsbwG2PzcDbgMOmXsNK75MX7v12h5OHIvvNDRu59beGw-3iDO-ZgAijVYbsidiOtQPbrVgVQ8ZK0U21usayYC3yj59yZFYLCOgEN7NH5XC_KenfUrTLLgl80CS2q6H_FSNC8BFeB6CECyHbwIKux8V8n2ZR85JZIROpFualoVcfsMnEvUEWazZAt7M5gJVYOgBH_5gT0v-cv0DzRyQ9S6T40B6mbI1u1FI9vjEdEnq5nugIaau8O-PqZh4vVduCXtZSGyAXLCCPqtE3LEolPoQPKxxjHanMmu5z4tQWmOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2dfb803e8.mp4?token=u68EK2NvOvQ76m9MzaGAssPi7ZCCLiM86HWkQ7esJdfppsbwG2PzcDbgMOmXsNK75MX7v12h5OHIvvNDRu59beGw-3iDO-ZgAijVYbsidiOtQPbrVgVQ8ZK0U21usayYC3yj59yZFYLCOgEN7NH5XC_KenfUrTLLgl80CS2q6H_FSNC8BFeB6CECyHbwIKux8V8n2ZR85JZIROpFualoVcfsMnEvUEWazZAt7M5gJVYOgBH_5gT0v-cv0DzRyQ9S6T40B6mbI1u1FI9vjEdEnq5nugIaau8O-PqZh4vVduCXtZSGyAXLCCPqtE3LEolPoQPKxxjHanMmu5z4tQWmOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ سپاه: پاسخ حمله به مسیر زائران اباعبدالله را با حمله به پایگاه العدیری کویت دادیم
🔹
در ادامهٔ تنبیه متجاوز و پاسخ به جنایات ارتش کودک‌کش آمریکا که سحرگاه امروز با حمله به مسیر زائران امام‌حسین، ماهیت یزیدی خود را بیش از گذشته آشکار کرد، صبح امروز رزمندگان…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/452163" target="_blank">📅 21:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452161">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
زیرساخت مرکزی داده‌های شرکت آمریکایی آمازون در بحرین ویران شد
🔹
روابط عمومی سپاه: با توکل به خدای قادر متعال و در هم کوبنده ستمگران، رزمندگان هوافضای سپاه در ادامه موج ۲۴ عملیات نصر ۲ در پاسخ به تجاوز و تعرض روز گذشته ارتش کودک‌کش آمریکا به تاسیسات در دست…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farsna/452161" target="_blank">📅 21:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452160">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/642a887069.mp4?token=G5IHvJpdKbQnwgUyCqkONmfdEvfgf7HtScCiNvQzTCr79D_Qa7LDNoVaclClwuQxKONv8HBaVV7_i9yjL5ubv9BrRIZC-hF-Oph68p5ZKuNiwr540KxPMzamT1s8z1AhcgusfP7S0YYEzvcV3sazvIDnsia0sb_N-8eIXNLD_adS5iANugn0IIS8_GpZuvLoutUIH8XcylQiu6eLjcTR0S1G8cNchieAJXbWv-u5FKdLDhvTrqpahSyv9ug9VsC-mZdimKVkAE6-RfSQFfJxamqXZKWCkzTOEFuzZFXDwNF_8fgFniM2PaOk5NZJ7FH2TwF5S3RDkV9-J5QYxT9FCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/642a887069.mp4?token=G5IHvJpdKbQnwgUyCqkONmfdEvfgf7HtScCiNvQzTCr79D_Qa7LDNoVaclClwuQxKONv8HBaVV7_i9yjL5ubv9BrRIZC-hF-Oph68p5ZKuNiwr540KxPMzamT1s8z1AhcgusfP7S0YYEzvcV3sazvIDnsia0sb_N-8eIXNLD_adS5iANugn0IIS8_GpZuvLoutUIH8XcylQiu6eLjcTR0S1G8cNchieAJXbWv-u5FKdLDhvTrqpahSyv9ug9VsC-mZdimKVkAE6-RfSQFfJxamqXZKWCkzTOEFuzZFXDwNF_8fgFniM2PaOk5NZJ7FH2TwF5S3RDkV9-J5QYxT9FCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صف طولانی موکب‌داران در مرز مهران برای خدمت به زائران در عراق
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/452160" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452159">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdf0591852.mp4?token=X4JMIoDQZPBfMtURwpJl_C_F7HgvKWgNWXTjgngFYKRtuAj5rPqL18thrUUbumgFXX9RQ6IOVjJ0k-h0HM8CYe6MC3Ir-7HOIlXJ5i_ppxZuxzdDzoO9vHfoI-2t7MxUF8U3BHL_6FsOAYjQFMS3PPqudeC6a39vAgysOmXP3zD80AZMgd2v1HJt0OWK6PzgsXN9-x70NwUSedRGOqjZZiXcqW4wPsghF3wYh7rpRkAV8FpO6gOz8_MVRCtOz248-RtkgNJ7AiXNt2X4_ppX7crBcNbhGSqquI842Zv3qmL-UeDmgfnuATD2kgvOtqaL99bBAjqeAJledopP9RB65ESWzQb-0Wj9-OvreQaQibmjNrD4tWnL-hDkVjCUfZ0I1U28WckBcWWxZ7XiTZLQzSzm6N_Wob1J2fkKdIVReAkxnh6V_0Lxv3hlTdgVVtth9lXZSYjvVqKguBfyYEi8g_fitvV7RFsB2Z-WZ1HhqOXzjQIjDWkVhtTL6R7VNbsFueOo3dcwyTEqAcNfLOxaPan-TV1qaNsH2HrcAGqcQ5EPb8D7stkvcMLdg7IyMrEzx2dt7FshsKX6-rwcJf61esEfvKjjReT8eUYK21oLWsB9ytk8CnYqCnXPrJCCE6DNiVX6glxQjVbkozES-nLKpoF-8_IBywcU6udL_hQ0Ago" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdf0591852.mp4?token=X4JMIoDQZPBfMtURwpJl_C_F7HgvKWgNWXTjgngFYKRtuAj5rPqL18thrUUbumgFXX9RQ6IOVjJ0k-h0HM8CYe6MC3Ir-7HOIlXJ5i_ppxZuxzdDzoO9vHfoI-2t7MxUF8U3BHL_6FsOAYjQFMS3PPqudeC6a39vAgysOmXP3zD80AZMgd2v1HJt0OWK6PzgsXN9-x70NwUSedRGOqjZZiXcqW4wPsghF3wYh7rpRkAV8FpO6gOz8_MVRCtOz248-RtkgNJ7AiXNt2X4_ppX7crBcNbhGSqquI842Zv3qmL-UeDmgfnuATD2kgvOtqaL99bBAjqeAJledopP9RB65ESWzQb-0Wj9-OvreQaQibmjNrD4tWnL-hDkVjCUfZ0I1U28WckBcWWxZ7XiTZLQzSzm6N_Wob1J2fkKdIVReAkxnh6V_0Lxv3hlTdgVVtth9lXZSYjvVqKguBfyYEi8g_fitvV7RFsB2Z-WZ1HhqOXzjQIjDWkVhtTL6R7VNbsFueOo3dcwyTEqAcNfLOxaPan-TV1qaNsH2HrcAGqcQ5EPb8D7stkvcMLdg7IyMrEzx2dt7FshsKX6-rwcJf61esEfvKjjReT8eUYK21oLWsB9ytk8CnYqCnXPrJCCE6DNiVX6glxQjVbkozES-nLKpoF-8_IBywcU6udL_hQ0Ago" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تهران تا کربلا؛ ۱۴۰۰ عاشق در مسیر امام حسین(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/452159" target="_blank">📅 21:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452157">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gfJoVlTBta5cDP9HAIy6TmbTor_sQQosP5_W6kHnm_ASwlmaSDH_JMpVqs4kK_2hCxFRETGNXUZatjwMN3VeWMBoRhM3RSus-7Q19uuCgb5C3IbP51BjXjal5fkpL_JFZQ--pDtJIBBPaNmRwNwejZ5AYi4r3-OBpH9q9q0BtY8VQ__w1jBIqtQZujxNU7yM4aNSBMcXRiry11C2BycFXVQ9377RfOxj4PCxeHvR5US2ewufxXo14sLdnMnQl9fDAku9RRS1PVUF0ikaMHI1dpBCiiYyXLJbjGPPHOkpqn9IKRgGPx43J5MAe7e42YdQbCKc_Tlc9gN8h0lPNy7k5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dU0iDQ2qK5fxYWwdujrdbBz3bSfFSEJBLdm3E-8PTQKKaWjQgd-yzAQoJSQ83SrQQQqz6aWI6kNRumHsD5_YNtiLwZXPI1M3vQlJWtgvlzfGqNYJct6XFsKh-_D4LkxkaiL0_aNo-ewTd1P17WTD8SbJ_D9vCi8rQ6ulgSTvSP5XbPP5uaUQzxriS3T8umDXHaPDusatFBRMipkck_Umj67LhhWCGzNtxm9qlmt69DpJg-1xQ5zcv_g_J8WnP8Z0-QOd8M6IxlOeml8tmBeafEaMNUhNk6O-e0-7YB7Yi8sZrzIIVDVQYSuahrYxWasTMmxE3k7WeB7eAe7XfZ9Kkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قدردانی فرمانده هوافضا از هیئت بنی‌فاطمه و طباخیان
🔹
فرمانده نیروی هوافضای سپاه با تقدیر از هیئت بنی‌فاطمه و حجت‌الاسلام طباخیان برای حمایت از رزمندگان، تأکید کرد که «در میانه رویارویی ایران با دشمنان، مجالس حسینی باید به سنگری برای بصیرت‌افزایی، حفظ اتحاد و تقویت انسجام ملی تبدیل شوند».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/452157" target="_blank">📅 21:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452156">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXhGiU-cwHoTKEOpmLvdKx-6JBCcH64HRPMJmA3UKzSnvEewVobk5lSabYUUgdmLLQhf0zKRfF_auihOJKEgbsj4k24Nz9_KexIVFPbUjMiLE5DGCdlVs3v52Q7lwuvhG0jM8TyjXiwrgnxnzfy0_sD3gqCbnkXIUVswvCNo3O8J7jQha5kdgbOaefSzBfjtxiqxErnX-4DepWwy6CduQ8xCeETWNd1aovEvyWJ6rWsSIHMfI-2kbeY3LQhB8XlEC0_6fRNKYAP3y2yPf9F55Ciu_VdFVUrYpJewSxAAkjl8JxKvzRMh1bO83ho6z2RC3SM0ELb5FooPST7cLzrdgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتکش ایرانی از خط دزدی دریایی آمریکا عبور کرد
🔹
یک‌ نفتکش منتسب به ناوگان ایران دقایقی پیش با نادیده‌گرفتن محاصرهٔ ادعایی آمریکا از آب‌های آزاد وارد دریای عمان شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/452156" target="_blank">📅 20:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452155">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/389a429d6a.mp4?token=kMmS-H0mpA_KFa9BQwUoNK6O_PABBgVhgKjpiWs3VCLs_WkdYfnVSirCWeqnFwCfth9b9Nvj00ChEO5bO5tATMdFCRhKF_JHf1eN80tyiUE17i_avMKG6nkkU6gEIBbUPvSaaaIIiWuiocv2TquDIhsOyJar27ztXjsqGECxaFAIIOlN-FUhvEJdGxjfc0m1F1J5EH5SIQjR9vHjKWqFz97MbMJvuCq-vJmX64J_dyq3LJ-6kOPc-59M09-0gdhfo3pepHwQGRBuxcEJEMDJb1uSh_PJGAZTpllEqWeYkqp7P8IIjk8zCGpFh84QywBChmhzz5Dxm_FhVXYMr9-iHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/389a429d6a.mp4?token=kMmS-H0mpA_KFa9BQwUoNK6O_PABBgVhgKjpiWs3VCLs_WkdYfnVSirCWeqnFwCfth9b9Nvj00ChEO5bO5tATMdFCRhKF_JHf1eN80tyiUE17i_avMKG6nkkU6gEIBbUPvSaaaIIiWuiocv2TquDIhsOyJar27ztXjsqGECxaFAIIOlN-FUhvEJdGxjfc0m1F1J5EH5SIQjR9vHjKWqFz97MbMJvuCq-vJmX64J_dyq3LJ-6kOPc-59M09-0gdhfo3pepHwQGRBuxcEJEMDJb1uSh_PJGAZTpllEqWeYkqp7P8IIjk8zCGpFh84QywBChmhzz5Dxm_FhVXYMr9-iHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رأی مجلس نمایندگان آمریکا به پایان جنگ علیه ایران
🔹
مجلس نمایندگان آمریکا طرحی که خواستار توقف جنگ علیه ایران بدون مجوز کنگرهٔ این کشور است را با ۲۱۴ رأی موافق در برابر ۲۰۸ رأی مخالف تصویب کرد.
🔹
در این رأی‌گیری ۴ نفر از اعضای حزب جمهوری‌خواه با دموکرات‌ها…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/452155" target="_blank">📅 20:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452154">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f174f6ca73.mp4?token=NdjsvMYvzobv0LLwH2iO6BlBw79QOo1vk0mNeobeMp2lENtOb7MoqtDuHMNvZ_MsP4YJtHjbZwJpi9-o6UOlU4nK3HmvkAUUc_MHb3CkD4k7PrOLIFPJlY_L3tugxjBueEHm0PUPH3p7KZkRS9YMSAxOZo6nykigP8aju4U-0rOu5vvx1lAjuLbcKBcA73KsFulHwt6q3xsGX-MlwCK0s39wTHMmINNJxPMTVOn9GXaJG6WjPyVgjb_U-O2zW550Bl9ttb-hO0lQ--hW9rYwAQ5CjEgvIIXzK3Gy4dzUr1KYW2akiYARtsxHoBNkdcMLpts-A6F2i5DTLxrXc8eepZh1O7b-eGLo3-AYEVgINoW_JMOtjyY8ZjmTx3bJWFx9piD-RkNDYrCiTxuLPcc_cI15AAhsQdSgll0BWhaaw73VDs8C265KaX4niPKHhLOO-QldkWBlSDOtnNbzCSbTU_nH5O8ph6QKVKOamj-hrW5ZX7iKUBbgFwB_7LRdAV5Qqy1D76-qafbvz-c5KGBeJTMpr7p6zNS2BNDDxFU_CERF7ECMiWYGLebScJNUL-bzx0Rq4DwiTraFqxTMMAcfhCplajBgXI7ls8SvEpXXOUofZOL5L_jQtwGaUkoJ4hf8eOCPZCPIrOaBIbAo_sPhA_O57467vh92m6tsDafR2ws" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f174f6ca73.mp4?token=NdjsvMYvzobv0LLwH2iO6BlBw79QOo1vk0mNeobeMp2lENtOb7MoqtDuHMNvZ_MsP4YJtHjbZwJpi9-o6UOlU4nK3HmvkAUUc_MHb3CkD4k7PrOLIFPJlY_L3tugxjBueEHm0PUPH3p7KZkRS9YMSAxOZo6nykigP8aju4U-0rOu5vvx1lAjuLbcKBcA73KsFulHwt6q3xsGX-MlwCK0s39wTHMmINNJxPMTVOn9GXaJG6WjPyVgjb_U-O2zW550Bl9ttb-hO0lQ--hW9rYwAQ5CjEgvIIXzK3Gy4dzUr1KYW2akiYARtsxHoBNkdcMLpts-A6F2i5DTLxrXc8eepZh1O7b-eGLo3-AYEVgINoW_JMOtjyY8ZjmTx3bJWFx9piD-RkNDYrCiTxuLPcc_cI15AAhsQdSgll0BWhaaw73VDs8C265KaX4niPKHhLOO-QldkWBlSDOtnNbzCSbTU_nH5O8ph6QKVKOamj-hrW5ZX7iKUBbgFwB_7LRdAV5Qqy1D76-qafbvz-c5KGBeJTMpr7p6zNS2BNDDxFU_CERF7ECMiWYGLebScJNUL-bzx0Rq4DwiTraFqxTMMAcfhCplajBgXI7ls8SvEpXXOUofZOL5L_jQtwGaUkoJ4hf8eOCPZCPIrOaBIbAo_sPhA_O57467vh92m6tsDafR2ws" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کادر درمان اصفهان آمادهٔ جانفدایی در جنوب ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/452154" target="_blank">📅 20:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452153">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvcKvBttCrPmOWFiYmDAAsetbkgJAMb_KNJm3R4kQpn0v8AGfWq3bRv5UcabEdzXDoXVw2M0lvB4aHOcueBXygrgCnR2SEuBxL-TzyQzDzxFjNSEzjlgJsfA7fhMBbSDU4cxK3zfLLAaThlk2VrhUBImGoazbGDY3HobLUPnQi4EB1EN71Ho3aVbNxz_cdoGctwq5wu2uMSmN5nvJkP5X-bRzD1D36Wf1hT0xMrmJ7sEJJH8_9d-rHjl1SdjA4P1wmVuuAq9vWvGJutU99zGWSnzaGfkGumlwkprQ-lSE_SEUmi10XIAIgZ-ph-5f-3WcS8aHronFvIV2NL19HTxqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
وزارت دفاع کویت: پایانهٔ مرزی العبدلی هدف حملهٔ چندین پهپاد قرار گرفت.  @Farsna</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/452153" target="_blank">📅 20:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452152">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzJwxFHihWtK1TTDQTWbpUE3jlleg_I8qxL1lehkQ7Yz8o4UhIYTWYsdX1upTL0-FvB7aPf2c9h0YBcZS6UUPpVKI6vhCNVWCm926gg_qaIIy5kOtq5blcTpxelYNspphE22hOHki5UeqBsP8X4wJVhO-d8-c1ykeeKcIaHdU3ZumuCHnl4QGrvaL7zn9Ugpub7WMl7WU0Z42-Mp64Ci8ZWsHd3Dy794Ib02OHzpMQKAt-YLBSoAFm4lSgFTF6G_8aBjpddZbm6ROcAQf5bLXVkkUp-jSsXspQfZaW8r2DGHMG3eqUwWRhY-0Sbo58ksDIw-oeEfUL69pAFTPMxSDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
محسن رضایی: پاسخ ایران به حملات زیرساختی، تصاعدی و شدید خواهد بود.
🔹
حمله به زائران در شلمچه و تهدید به حملات زیرساختی چیزی جز استیصال و درماندگی نیست.
@Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/452152" target="_blank">📅 20:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452151">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🎥
منابع عربی تصاویری از بلندشدن دود پس‌از انفجار در منطقهٔ مرزی کویت و عراق منتشر کردند  @Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/452151" target="_blank">📅 20:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452150">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc396de329.mp4?token=eI0UecRJEdnPXXjXm7_SxXraGagIR5L_Ryh1UI6ugArJWXgGfi7hCcromFFq1nDfVm6uTe6alextFkD51CTXPN3IcY1Uvkfjlk-88cBviP0aht_Mp6VhxbM23EW3rF42uyEM8iz_7FvaF1ytgKJnU67uHX7PL8xr78yUSjZG4iPihhlMHf1GQrgc21QMwYhsbsGrfMkYz5sjX-PEdoKWhDgfEnMEiRq5Pnt7U3R6-_pswC_n-EXe0_AjVBMQ-tX1p07MjFXM5WC5um6W4aubkzG80Falr_3H3uovJkxuoZ4QqMWyIxdi4vVC_livdeskmmHG0AcfnKtIn2DZktGuMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc396de329.mp4?token=eI0UecRJEdnPXXjXm7_SxXraGagIR5L_Ryh1UI6ugArJWXgGfi7hCcromFFq1nDfVm6uTe6alextFkD51CTXPN3IcY1Uvkfjlk-88cBviP0aht_Mp6VhxbM23EW3rF42uyEM8iz_7FvaF1ytgKJnU67uHX7PL8xr78yUSjZG4iPihhlMHf1GQrgc21QMwYhsbsGrfMkYz5sjX-PEdoKWhDgfEnMEiRq5Pnt7U3R6-_pswC_n-EXe0_AjVBMQ-tX1p07MjFXM5WC5um6W4aubkzG80Falr_3H3uovJkxuoZ4QqMWyIxdi4vVC_livdeskmmHG0AcfnKtIn2DZktGuMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
منابع عربی تصاویری از بلندشدن دود پس‌از انفجار در منطقهٔ مرزی کویت و عراق منتشر کردند
@Farsna</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/452150" target="_blank">📅 20:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452149">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">صدای انفجار در حوالی قشم و لارک
🔹
دقایقی پیش صدای انفجار در جنوب جزیرهٔ قشم حوالی روستای سوزا شنیده شد.
🔹
همچنین در محدوده جزیره لارک هم صداهای انفجار از سمت دریا شنیده شده است.
📝
اخبار تکمیلی متعاقباً اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/452149" target="_blank">📅 19:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452148">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">باز نفت گران شد ترامپ یاد مذاکره با ایران افتاد
🔹
رئیس‌جمهور آمریکا در مصاحبه با آکسیوس بار دیگر مدعی شد که ایران می‌خواهد با او مذاکره کند.
🔹
وی در ادامه گفت: «ولی آنها الان آماده توافق نیستند و هنوز به اندازه کافی احساس درد نکرده‌اند.
🔹
ادعاهای ترامپ اندکی بعد از عبور قیمت نفت از 100 دلار مطرح شده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/452148" target="_blank">📅 19:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452144">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SAgvdfXD_L0-x_eAOca67fkdFQhjzKT-oFadRFQGVtMvpltV3E545aAJokFMZJRwHFk5-gPYlCwaOXLie5CsY72hn088DwODKigF-iAZHCsxaogfsSlo04vMa-0cVQuNNKeRcLWb1WpgBR4O3Va7cEWrW-EalWmUrJuCRWZb9qWiUBpWBQ07EhDGyP1K5lhO-ipVRyVRuWKcfJCFR7o8rEOO3Pt3ERftkvZ1tY9F1H1BULWda1IImdCEfoN5NBWdZpm8nAMtsRCjGzWqjkNxt46FgQbjtXonh_xN9rY5udU8HUN0EL5-zz9l9ZpfVf_ZOGKF9CYshM3qtFKZaLfM9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OFtSyerWiXCypv26q3fKGfRO_WxTKmwWhT0vq9JKCmwOFzZsx_zTT7f20-SzdgJi0V6hio_8s-dxHDRqVAVDo9IE14zVpeep49YTi582P-GrTZfo0ER9LSks2emtB5wwrqItFbqYVnPXw2wRDapa5yLl0l0D1Dmbq5gjR6qL_ccJ1j8CZOEPiOYTdxyTTXdmdcXay4_Qc_nfU96jaaL7NId-l2CI6za-JKGK8emAO-qQ-N5gTPBdZXpG-6svSaizwLxh02jYkiIOiiIN4eFvufvIQlCx4_SIWc3CrVRFYcB_3_c5cChDxTIgDCLxWxGD075J-HqWbA04lKPU094VsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VFppQqb4US31o4YU9laTTL5fUC34OPgko1K8oKJyz-Fqcp9d6IgwFIphisdTqLoBIVNUSNCNZKia2W9C84h7HK_CMyYgxr8tT2E1DXUI0d8FTczKr8GH4eWpw29itBDSRwbn_ZEIHatcCad3jiYl-yUX57SsrcBpCgqBLqfn3Q-2wFGnCpajGXdTQXw4xJf9RJ1_KU_a4gz12ao7Nvi_hekYtkkrMIgc9Vi2fuUKHtLyR0jhDUA0jq_TSjFDSgjlnzP36Swiimh8ut7oUzM8g2xyC9sujlxTPpA_93ymHG_-RzhVwHhy64HjmGDKbdll2ykY4aHX917zMWsronT_zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VWhkz5suAQXExr_Vibxy1o0z4pkPUYlS3lmDsXkxNbOCK9cnAa5UjapDLCsPEB_k2b2T8AL_1vtDkt3pU0sWAumU1lVtnF2yY8DzqO972x30qUMyGERvvlm_zt3w4TgDVExWPjgzpJNUBJYhq29rtZVKy8j0EdV7mG26PsXlIlyh3BqlvE9pRc6I84RAHgc6xBK-SRcADZFTJaYtYANCNG5TJDz7n_wUX4L3LmO77xU84by_1BIzN94f1Xvgdc8IIckJ0c316YDIh7d8Z3SyEkpk8fQoG2dbEw07jlV_kgEVyqqs0mgoL93ijUGR2iiCXpj3qDiEf3k3EB1Ns_MDAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آغاز برپایی موکب‌ها در مرز خسروی
عکس:
بهروز احمدی
@Farsna</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farsna/452144" target="_blank">📅 19:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452143">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y07xYZKvRQl85co4mqTwpCWpGV_Xt83Z2eG-wURJkddFu3efk1xhOUVYVoJot2amQx1FCcnRiYZZEo3mvPtSNlrcB4eUwIKnHzCuWglcu4xMpcQ7jot2blUwyJBDyUd8p2d2pWqAGsUyOyRrCGSR3IRO6iNTmjWt2UyYT2EmRkxmiy1XskDTvFw_7QoRPvT0YFkCUBa3BzJr1EthMSEnvDH8uqLeNmKN5jf9SKZUvSh-Yfry6m20Kvn10-7dyA1Z-S9HGMwF-PsYqvO-OLb9CBRYp3YoNeO5SD-UBbmrkCOos6k0DmdxnJZG_4gUrcoGs3jEyuJtxjbGtGZ40nACtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رأی مجلس نمایندگان آمریکا به پایان جنگ علیه ایران
🔹
مجلس نمایندگان آمریکا طرحی که خواستار توقف جنگ علیه ایران بدون مجوز کنگرهٔ این کشور است را با ۲۱۴ رأی موافق در برابر ۲۰۸ رأی مخالف تصویب کرد.
🔹
در این رأی‌گیری ۴ نفر از اعضای حزب جمهوری‌خواه با دموکرات‌ها همراه شدند و به این طرح رای مثبت دادند.
@Farsna</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/452143" target="_blank">📅 18:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452142">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvHlIJ6cLMtfDzwh-H5boLf-3UW8XjVv8AXZ-PcoMiREEK48nGX0zdE6P8uWfxSJYgn0OM7hya4TPvJvX8X87xkrUHHI8xDxjjrgySsuRizjygrNU2Fw_UKzXHCqJPDWWi8JzF-_5PEwymGr8rWReEJ_dx8RrjxWNtAXM4SFqCntLCvUHuSW8rgsgaWgRyIYHumSJ7tYntEReRrnxZZJ8wDFwAd5ezi43-GWT9KMkl5Haotak2r29Wv8ZLdNWC5CFBdXmlp7y844aoJcZAqN1wMBfzpBvHqu7n2hvJHD7FVydUfZyWjWZPPRi9JyOv2u-6rHwWz7CMYWz-hsvRp17A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نفت ۱۰۰ دلاری شد
🔹
قیمت نفت برنت که از چند روز قبل با اعمال کنترل بر تنگهٔ هرمز توسط ایران در پی نقض‌عهدهای آمریکا روند افزایشی گرفته، از ۱۰۰ دلار هم عبور کرد. @Farsna - Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/452142" target="_blank">📅 18:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452141">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‌ سپاه: دیگر اجازه نمی‌دهیم آمریکا با آتش‌بس‌های فریبنده، ذخایر نفت و مهمات خود را جایگزین و پس‌از آن مجدداً حملات را از سر بگیرد.
🔹
ارتش متجاوز آمریکا که در تجاوزات خود بعداز شروع رسمی مجدد جنگ، از پرتاب موشک‌های کروز از شناورهای خود در اقیانوس هند بهره…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/452141" target="_blank">📅 18:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452140">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‌ سپاه: پاسخ حمله به مسیر زائران اباعبدالله را با حمله به پایگاه العدیری کویت دادیم
🔹
در ادامهٔ تنبیه متجاوز و پاسخ به جنایات ارتش کودک‌کش آمریکا که سحرگاه امروز با حمله به مسیر زائران امام‌حسین، ماهیت یزیدی خود را بیش از گذشته آشکار کرد، صبح امروز رزمندگان…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/452140" target="_blank">📅 17:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452139">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">📷
تردد زائران اربعینی از مرز شلمچه  عکس: فرید حمودی @Farsna</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/452139" target="_blank">📅 17:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452138">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mu7mo3_6-oy5zXzSE89QUZdafmkPePnksl6W87pWgMq1EyzMwDq_vSIm3N_kKXuGT7xzc3fZotqgxJsdkjbdXykYj4tqGU6k3pCZqanP9Cz1H438rfJhe_QxxyQKgSlaE7ApfrgGmaKEhNllJZCqzLZog_cM5DMaX1g4CLJGVx8aWlQMr5U5QN_13zAl6WqbesF-zTE9kO_D8cGyXjvpYc5X8iPW2BlU5LyrUkEw3c8_zr0FqE3ge5KnxBGbC6F01pcf_3vM9B7UCZct7LI-KVq11BhYe2g7RBHZKzfwLOlB-2u7jFp6mzL9VnKCn3lLSHLAOLxWQRij1iIWjxaGRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پیام مهم سپاه به مردم کویت: آمریکاست که تمامیت ارضی و سیادت شما را هتک کرده نه ما
🔹
روابط عمومی سپاه پاسداران: مردم شریف و نجیب کویت؛ برادران رزمنده شما در سپاه پاسداران انقلاب اسلامی در تنبیه ارتش کودک کش آمریکا و دخالت های آن در تنگه هرمز، یک انبار بزرگ…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/452138" target="_blank">📅 17:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452137">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DuTqa1ErNSBen2QdMaHvToxA66b2H5kbCHlaZ60_ORWbBwexHDsi3LqmjX3Ar7Z9CMSE44Ee7C5ilrhG4047ERp5W-GYOGOfVUBr30fdTzk2dg30nVQhnO-33MrwOQ1uJS9SsYx9d7nERYn2dMKgMsiLjLKm0mbgOTC3AktM_WRPfcR9bOX-9u_t7Q--O9J1wn2AyEdR64l2495oIqw3kHpcUmfK86SdGWxJd7LSWZZE-RnLVCz5bhRWOA4r7ON2G2aNEOQzMjGlUmfscHXrka9oaTpsLErb-PBofRU-wkXK5EcAgzzVJklbxGoNzDH_p1uGpVu4-VayIqomv4-0QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی برای شرکت در نشست شورای وزیران خارجهٔ سازمان همکاری شانگهای راهی قرقیزستان شد.
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/452137" target="_blank">📅 17:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452133">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IYMI_0-bWoRALkXRkWFgK632WS31z3pZK03PNfTraZIdkNvwgbOSjS1MBsunQ1YboSudSH44dI3xVgaliYZRy292fFnP6gkF2OEnJaV3LTgxbtChmzCRQuLhwCy5c28VNSN_D-4-lV7XHJv5-abiND3ep_ZdG53u2JtFR8YI-FF8itNH0JnI0TFqCHxPHJ_qy-EJlQEtg7-mUV7lf0cCc6rO41iDSokOBtHVCpJ-Sa9bbLxAkWiaAKjUmOyZW8jeCIjf674oVnhfePBk4mw1eZd9GUnwWNfVu1QVxKrr9nz6SNIt4qxKbBm34CvlssA3G9p-wk75U5ynY_bIy1pFVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/obYrucInf5f0I0ZkVsle2-6ESOcQ69gHMFnDVYZFVc7_OElvfmQ3yokRyWvmxZZ9oR7O_ez9PkDObo98FI8GXHOPxOm0SLy1O-IYi_0ZYVWqtzMsa8H7kaK6Nbqo_BPNpH0kyKSOhTT4fK4v3NzISRO5jwhnkjp_TVVX-7poJjDfidiEZn6E-gIvwRvMOXQI9-A8Fq6TRGB5STtgBh3PNIGcklJXr57du--nem7X1F7Deo6sC9Dysw1my09pwbLESGzqX5v7PIdaFOZfRKXu7HYcJP2_hjUvIXPqQzASabqmCGqfeUK63hcZf4b3oOhaS5jkeuzEPZuk4kYX8Yz1QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DoXktJN5yNByp8pxCaJIm7brs7OGs7C6leKojujvaQBtSI-LmUz971g_1dy1k7D--FkztfI9PDdZzYcRVMnYeApPPL1KFNqHwQummHGDKy8pfupJcNF3qxVgAOSM4EzFj5Mem1k9awuVdFvBuAhMgU3biaZAMDz2kBud7G0lItONdmLPCLjWJ-WpMo8ORfl8O38HxO9QiL3YM4jQ4waUqWsYRhcXNppfpfkXGsmrw5mcIZR3n-DA50jJP7zXtskbOBN4H4E66btVpmnzfxqGLgUhbXnYL7ZyNoKwvXZXKWTpfgmchA2pg1WwjXBWqSNs-WVlwzYmYlLOo43Pzvvvcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GnBlyJsCv5JqKQNPHZhOBBnG0RSwORufGE6Xnh-1_S8hMvsrIJy2IXeBxR_tq2JTXo57lHffBxUERagszhRvI8DZjWHrh0VIz9PI8tqtXEw1v8X4TBdoIEh1ESMYxJIkJwSZw5D6Qhr-OiLP9Rjuw2_bVmV91qKekJMJJDNP4Onsw6-aufdTQsTDr712qZkBzsGV-dpvGP_0k-ZO_Yucib7jEyvZTa0gd91Kf0tZ0Qb-l516d1Mq9zFcmb4fA-ylzgSBvLFAf6rD5nw7vOc9r5q-zKouy3uEDWjlMwBDVtuyl25haytdRiHnukRRfqhC0B_2_LZ_SyH9GmVbsuDaMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‌
🔴
۲ شهید و ۱۱ مجروح در حملۀ موشکی آمریکا به مرز شلمچه
🔹
معاون استاندار خوزستان: در حملۀ موشکی دشمن تروریستی آمریکا به مرز شلمچه، ۲ نفر از هموطنانمان شهید و ۱۱ نفر مجروح شدند.   @Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/452133" target="_blank">📅 17:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452132">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bc04871c7.mp4?token=Mv9vEhGCaTTGIW3RL-IzAeTdHWAatM08VNhJ0UKTxu3-da2ofinhHtu2S6Rhf8xVct0JMZisbr8sdcDL_GVihRQL0l3bSKIT7Rwhd5ptA1Zv122jZCkuUKM7ja29RGqTLvqHe2vaOH_hjasltMKOIV9xxNj23hM3MQ0NoIWPiGXHpIo8I8dni_vqibHAg6LHBSQnHv9oPb1otGn1E8U_PXj-k8rK_KhORiK5bbrl2dainZcQdYx3wysv8qu0Hgbsohy-YN2OUlj-pnOlhw61LToOjDYuBvV6xABQ5wGTIm6RHW2sR_-FrCigTuEiAE8levtJMoE9nGAeydgVtdc2yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bc04871c7.mp4?token=Mv9vEhGCaTTGIW3RL-IzAeTdHWAatM08VNhJ0UKTxu3-da2ofinhHtu2S6Rhf8xVct0JMZisbr8sdcDL_GVihRQL0l3bSKIT7Rwhd5ptA1Zv122jZCkuUKM7ja29RGqTLvqHe2vaOH_hjasltMKOIV9xxNj23hM3MQ0NoIWPiGXHpIo8I8dni_vqibHAg6LHBSQnHv9oPb1otGn1E8U_PXj-k8rK_KhORiK5bbrl2dainZcQdYx3wysv8qu0Hgbsohy-YN2OUlj-pnOlhw61LToOjDYuBvV6xABQ5wGTIm6RHW2sR_-FrCigTuEiAE8levtJMoE9nGAeydgVtdc2yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر حملات موشکی-پهپادی سپاه با شلیک موشک‌های عماد، خیبرشکن، ذوالفقار، فتاح و پهپادهای شاهد در موج ۲۶ با رمز «یا اباعبدالله الحسین» تقدیم به زائران اربعین
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/452132" target="_blank">📅 17:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452131">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceeaf815f.mp4?token=SlbsWMyUkEZ-30PBJ0T4ydcoMTs4VUp8ZXW8p4xyEkLAVD7mZjY0STOtAGHLw91ytGp8CGu5n8IebSIdQfk-S_VyEToSzFJSH4koPZuW6cxeFcmezgMvs7uTSCjilENBjnCGY_7SDRwSnI-0LkKz1iGy_czsZcQ5bmnNDdrMggTciZbKibKy6i-15UzrOgAnN-sm0AndHn2cBZuIf4Zd7JXjAx7MzV0pXBf75NLfXOAq2m_WYtWfEA3qf3AsWn_vFPJfnOerWbj8yf06i6PNm6FWqs_RXW35unfgF2FS-Q8CplsmTMsHaXUvUOu5jGn0JdZTqmt1y2yiMWyJaIDhKIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceeaf815f.mp4?token=SlbsWMyUkEZ-30PBJ0T4ydcoMTs4VUp8ZXW8p4xyEkLAVD7mZjY0STOtAGHLw91ytGp8CGu5n8IebSIdQfk-S_VyEToSzFJSH4koPZuW6cxeFcmezgMvs7uTSCjilENBjnCGY_7SDRwSnI-0LkKz1iGy_czsZcQ5bmnNDdrMggTciZbKibKy6i-15UzrOgAnN-sm0AndHn2cBZuIf4Zd7JXjAx7MzV0pXBf75NLfXOAq2m_WYtWfEA3qf3AsWn_vFPJfnOerWbj8yf06i6PNm6FWqs_RXW35unfgF2FS-Q8CplsmTMsHaXUvUOu5jGn0JdZTqmt1y2yiMWyJaIDhKIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دعوت از همه مردم تهران، اتفاق ویژه در محر‌م‌شهر/ سر سفره خدا مهمان محرم شهر شد
🔹
از مردم تهران دعوت می‌شود جمعه ساعت ۲۰:۴۵ با حضور در میدان آزادی در برنامه سر سفره خدا که در حاشیه چهارمین سوگواره آئینی شهر تهران «محرم شهر» برگزار می‌شود، شرکت کنند.
@Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/452131" target="_blank">📅 17:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452130">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01ba910593.mp4?token=ao-LLTNWvaky50ixOC82O5PNSbel9uEvJx2LB7xGat08q9buaf8EDxMriNrQX0eDCEwZ_CqQ9wc4B8RdpDYTe9X6fK9Ua9BBNE8IgLbdHmF7AghBOUjClAvIRG02zHl1sLRb4CZx98TzMFROURQXMUHVu82TJR308RDrQcttAl0HklFOnrvqhsIAnngsAv7Oyg878pnGB2sEzlbD-OHKUTrda3OSm4bowTdsxfETBYdxdSEK4NFinjooChj6XnWzoMZeJORUu2lNidRjiRhz5BMBNiCsoLw9ZBfBJPDY7z_bdqyW6OVdCi_XrtpHi54vBKq8uru7w1IPWUsea677FzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01ba910593.mp4?token=ao-LLTNWvaky50ixOC82O5PNSbel9uEvJx2LB7xGat08q9buaf8EDxMriNrQX0eDCEwZ_CqQ9wc4B8RdpDYTe9X6fK9Ua9BBNE8IgLbdHmF7AghBOUjClAvIRG02zHl1sLRb4CZx98TzMFROURQXMUHVu82TJR308RDrQcttAl0HklFOnrvqhsIAnngsAv7Oyg878pnGB2sEzlbD-OHKUTrda3OSm4bowTdsxfETBYdxdSEK4NFinjooChj6XnWzoMZeJORUu2lNidRjiRhz5BMBNiCsoLw9ZBfBJPDY7z_bdqyW6OVdCi_XrtpHi54vBKq8uru7w1IPWUsea677FzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش ویدئویی از مراسم اهدای کلاه ایمنی رایگان توسط "بیمه دی" به راکبین موتورسیکلت قانون مدار در مازندران
🔸
این مراسم با حمایت بیمه دی و همکاری پلیس راهور مازندران برگزار شد .
#کانال
اطلاع رسانی شرکت بیمه‌دی
@dayins24
#دریافت
نظرات
@prday24
تلفن مرکز ارتباط( بدون پیش شماره) ۱۶۷۱</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/452130" target="_blank">📅 17:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452129">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/452129" target="_blank">📅 17:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452128">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbUCETaDFY9YVf2Vay51pgBS2dvls49B6a-JjfYbETbhpyUxE6tvYlMXAupYVilX20bCkEGPw4Yh7EHNTqr9XOvNOKF_xF8G30AdxZt7s21iq-8A9Kup15f6BVq9wmhKb6LmS5F_RIkhhDThJTrGcSW1rcCvrgHmK_hNI2ewOh6JYfICX8vyLYkjYbrHoFo4GrT3C7pnmXQqePo8thc6Bzb-iNx9GNM8YYovBvbLMRWhYAO5tt2jDrzXyI29xa0UGVxsIjrKfHo8NDdq-4dTFJdYPXKDAXuz5KpHiMdrXCnIAsqoxd3PSGfH4Ke-XPO4Dv5eWGJJA329pqma5W2xhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مخبر: نفت ۱۰۰ دلاری صرفاً نتیجۀ اختلال در روند حمل‌ونقل آن است نه تولید
🔹
آتشی که آمریکا در حال روشن کردن آن در میادین نفت و گاز منطقه است شعله‌هایش دامن همۀ جهان را خواهد گرفت.
🔹
نیروهای مسلح ما قطعا با ابتکار عمل و هوشمندی، میدان و سطح بازی را یک پله بالاتر…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/452128" target="_blank">📅 16:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452127">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMbNgRPp4VxSR0BKnVSD0y_vrqe_nQ7epcbls_0wVub6OZXBWbqU-0TGsHDXmspI1RSb8dZOP0jUKcltSey9bnokdJUxajmGb-Af-H_IIBOXLdM7DOJXhHoQbrbM7Yw0pTvnNqPoorTiv9EwWQ8rBFkvHEM3JFr3PqWn2QPRVJNYcHRqNa-LiDFZGjjGufHsNwGgFrdcriITihbWK3ErlzppPHxHIKX1BA8bFkpFwmJCjSfy72zAnjluJf_OX9hWpqG7AdujUrMKsiQf99ztUWnvADUbLoedBfnQG2LQityzMlMfxplHJD4G5Js7YNS3UIJlZdBnM-PZBrASs1o65A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قیمت نفت از ۹۷ دلار عبور کرد.   @Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/452127" target="_blank">📅 16:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452126">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
وقوع یک عملیات ضدصهیونیستی جدید در کرانه باختری
🔹
منابع صهیونیستی از حملهٔ یک فلسطینی به یک نظامی صهیونیست در نزدیکی شهر جنین و زخمی‌کردن او خبر دادند. نظامیان صهیونیست هم او را به شهادت رساندند.
🔸
ظهر امروز هم رسانه‌های صهیونیستی از حملهٔ یک فلسطینی به یک شهرک‌نشین خبر داده بودند.
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/452126" target="_blank">📅 16:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452122">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n8nQSpQ0a1WxGvgJUwkdLA-XAGsvCKqWz64xT7EXL11ZcZ5_zoZNNVex94drbbwF_JNIrFR4Q8OwOBp5rNcsoBAf32gJPBK-h3GkY4iFTP7OqqhRI1jvT604Xb6FsK6JSSbMKH1619ncIF4kPF50PVSKh4crq07JSyDOT8zkbqBz6sCuFjhDF4cse4KTiFgWw9nDPuyxqMsNiQTcQXRmlHMHa1ga9nlSL4CHLMYl2UpzK4U18c5zocM80LEllWCXmeUTT4KauEF5X6noiggH3u0NOw-kObI0fxW6Ifdxuk76zGMKiCAMZ1Pz9uJK-1s43gZveF57ce9vFRU9qgAP6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BLTxgQykd3I1hmsRHPX1HjP4Bw8Ub3dZ5eRo6bAeArR99sowvLcgD3pvgq9ILcRbJyMbl_8TehICzur_ymn_Uvg_Jw4nu60XCt7w4lN3wfObSwft9zILfhW2G_koMXxpvRGtgd2AO5vXW8-9bC4fNDMaGE6pxDQnfQ06Grm05ZaQK-T4I1XAn0e47MWy7TOvq_kZnWiSkN43_PibIgckusY6WLAt8krK78PJ8yK1qGuZJBG_hedjGbLSLYgcZNPLnZ6K9h0_x6cEsUwGiB8c3Aw15vWIgsWNgCyGshO1QSSaZvq3zrpEwcveMYTYGvQT7Vq7pkSnOFrEXn9FciqdLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KSpF2K08jYrTHcnVqbUczUD4iXfqrmFwIGu79Vmd-FFEdey5_DGWElGK1xfXCCeFqxCkqutvUwlpwpiMT_B5wBTSm7pt1qJBIaBUPR6Q7Ejf2xvQEI2UG8eVd5-nnpQqb1tp1aPPPX2p4Ar5B-YHAIXwWNzE5cAXS6LWisfSXjbITsIzfN8GWoJ7TPVeTW10wDDdIqJOYS8sLvonMGJExmWgNyR8LCjuiRVhABCwVzb7lqeusajJmdlNp9LYdHQ1B8lDTFPu4CKbj_Ll2vCqjQIBV8tgfjADs03Ua90gR0PJ2Ev4biBOpOeY_tHKRpO7qQAtuMUQfibr45I-u6q37g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UCB1_JY2oKAh0C-WgWxjoxItG1kxlhmKi7N8b9uqyg7XqzlaWnNybDKhlTpnjhtATboQn0hK9_Kn_e9-ECoeFiQotfxscf-XrgZ9XGnBpeTdD4QmQDEJNA2RCO2Xk-snZww5xk6WgQpIiiJfXvoRQdnGNpzIu5bo3vUEhoInIpu5q7uyFpVD8kqaFvRDweLv2lPhr3Rbe6AUpmKP4ZZ3G1hqcCk1KJi1bkfXSEEW9_I1BaWJN8gM3kx7KKHBXz1goWPDlBGhjhO_M4HIJ-GkS3AhyLDjdz6GahZXaDzuC4gNxqUFVLHpBmrvPELMtivrK0AJrPBrgTYqrCtSS9E4Tg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
فتاح، اولین مهمان اتاق گفت‌وگوی جدید خبرگزاری فارس
🔹
رئیس ستاد اجرایی فرمان امام (ره) امروز در خبرگزاری فارس حضور یافت و علاوه‌بر گفت‌وگو در جمع مدیران خبرگزاری، در استودیو و اتاق گفت‌وگوی جدید فارس خاطراتی از رهبر انقلاب گفت که به‌زودی منتشر می‌شود.  @Farsna…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/452122" target="_blank">📅 16:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452121">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqPW3EQ_nYSyKjHAO3QGuh7m6vlfD6On_wznW2i8qZ4qNtlK3PcDNTxVhUqkql0iUNLgRtAeuXt1uItiDYgKCb0COb-bffTVQmL0QkySu-ZZ5e4etJq5o1AV2-YYSIx4wIXOpbVyjmv2PMqe2MKuZLfxk_QwVs0EntOp3SBS__zqLOofLRhQ22Ic3JJdgM0MwNAqMHLWegR7tBb5AEeacCJC8W9LnNRMGdqdX4KWwEeN9e4lSv8mJjK9K_y6NI26Yc4--lijKBcRlkONG1Uota8hXF3p-AX29lrWNiBzt_AvJ6xjfUTBtukT9RPA-sfMYOmf__4bURTRrwLT_px-ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
وزارت خارجه صدور مجوز استفادۀ آمریکا از پایگاه‌های انگلیس علیه ایران را محکوم کرد
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/452121" target="_blank">📅 15:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452120">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AawuTHlY8T4zKTPUNMW18Pf7SLHZxS1Xz6ZB07obKJ3-LMcu948b66kmkAz5VvLjtijWeryzoKRwNyylE9UUb0M2wI5y2ZzU16gF08L0bFndtjolY4JvFsfaNsu_ia8q90xMhyoOjXYi5ZX4TpPUed8MUtcWCiMGG9mriJVLzedLi03DYhgYOy3SFV7tV30qTXw2iG9-ESWp5aPM7DU0IZWj3524U45kSxbefKXWvPTfzUo-B0iei1Ggwd2WMaf1GCXO9sDvHBRHzN0ljqUvHXZG7w2BRX2ZmclOgpOq0-zLU26esSxvm5TdbQjlHssSgT078-lUSNsBnh5hjoHH4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: توافق هسته‌ای با عربستان منوط به سازش با اسرائیل است
🔹
توافق هسته‌ای غیرنظامی که میان وزارت انرژی ایالات متحده و عربستان سعودی در دست تنظیم است (که به صراحت متضمن هیچ‌گونه غنی‌سازی مواد نخواهد بود) و تنها به مصارف غیرنظامی اختصاص دارد نظیر آنچه ایران، امارات و دیگران پیش‌تر از آن برخوردار بوده‌اند به تصویب خواهد رسید.
🔹
اما تحقق آن تماماً مشروط به پیوستن عربستان سعودی به «پیمان‌های بسیار محترم و موفق ابراهیم» است.
🔹
ایالات متحده مخالفتی با تاسیسات هسته‌ای غیرنظامی (بدون غنی‌سازی) ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/452120" target="_blank">📅 15:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452119">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">انگلیس هشدار سفر به کویت و بحرین صادر کرد
🔹
انگلیس به شهروندانش هشدار داد که با توجه به شرایط غیرقابل پیش‌بینی منطقه، از سفرهای غیرضروری به کویت و بحرین خودداری کنند.
🔹
هشدار جدید لندن کمی پس از آن صادر شده که دولت انگلیس اعلام کرد کارکنان خود را به‌طور موقت از ایران خارج کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/452119" target="_blank">📅 15:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452117">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5584145f6.mp4?token=g_nAjd5arKng_6HaPljsaQEoLQ6JlfzY8F0oLqVVWuVGhe2opC2FnveMY6cTlG3WygtjshRdiW6V-qelWxmZn_9GyX_AEwt4iit9SkhVtsKcxQtCHycPozFWzVfZHxnVomkWGM3yKApBA6iUsi3vVbNxlEaJg_DjC8KjwrQEWl8OqY8NgYucxj5cOFraGPb_gMo8smCdYKblDRHevWCKRfBDdeTSFNRzUXxbu36EP4uWVMoyqrxgaWqMl0HIvGB8vsSNxQqhkWohnoemIWG2mlGo-6k_LPjyQvRoZSe0ZLatMhormh8fksLsJje01xLQ1pW81I_REGYvLnI1BHRabmYQaUW6sh7k5YW8KKjCaY4KaV14Q8ziN7GeFyeRG24cVmNTQl0Hr-YLxZWbLaI5JOqfRiwGzkoBN-xMzdL-oixv_KwYif5TqnSxMWarrM0JW9fjHDaJDFy2T12q7H5q30WZoeYNfXj8Sc2AECCtigr_nk8K_FpbABqfxUYwqjpApSCIy3xvWftrDbiZ95gp7mSJ4xRSha-pRlzDbrt1UO2IQxGxBQSywX1vlWof69EuARUTDTg2MJjHqZtoz7I1avaeT-UEVrYyy2HK9xY4eIZTo21PHdtydOvwNWuY_g7GBAnGBF-6kq92cd5SfN6w2D8pgP8r9Xg6O_Wt3SX6GQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5584145f6.mp4?token=g_nAjd5arKng_6HaPljsaQEoLQ6JlfzY8F0oLqVVWuVGhe2opC2FnveMY6cTlG3WygtjshRdiW6V-qelWxmZn_9GyX_AEwt4iit9SkhVtsKcxQtCHycPozFWzVfZHxnVomkWGM3yKApBA6iUsi3vVbNxlEaJg_DjC8KjwrQEWl8OqY8NgYucxj5cOFraGPb_gMo8smCdYKblDRHevWCKRfBDdeTSFNRzUXxbu36EP4uWVMoyqrxgaWqMl0HIvGB8vsSNxQqhkWohnoemIWG2mlGo-6k_LPjyQvRoZSe0ZLatMhormh8fksLsJje01xLQ1pW81I_REGYvLnI1BHRabmYQaUW6sh7k5YW8KKjCaY4KaV14Q8ziN7GeFyeRG24cVmNTQl0Hr-YLxZWbLaI5JOqfRiwGzkoBN-xMzdL-oixv_KwYif5TqnSxMWarrM0JW9fjHDaJDFy2T12q7H5q30WZoeYNfXj8Sc2AECCtigr_nk8K_FpbABqfxUYwqjpApSCIy3xvWftrDbiZ95gp7mSJ4xRSha-pRlzDbrt1UO2IQxGxBQSywX1vlWof69EuARUTDTg2MJjHqZtoz7I1avaeT-UEVrYyy2HK9xY4eIZTo21PHdtydOvwNWuY_g7GBAnGBF-6kq92cd5SfN6w2D8pgP8r9Xg6O_Wt3SX6GQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فتاح، اولین مهمان اتاق گفت‌وگوی جدید خبرگزاری فارس
🔹
رئیس ستاد اجرایی فرمان امام (ره) امروز در خبرگزاری فارس حضور یافت و علاوه‌بر گفت‌وگو در جمع مدیران خبرگزاری، در استودیو و اتاق گفت‌وگوی جدید فارس خاطراتی از رهبر انقلاب گفت که به‌زودی منتشر می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/452117" target="_blank">📅 15:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452116">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🎥
انفجار و بلندشدن دود در گذرگاه مرزی العبدلی کویت  @Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/452116" target="_blank">📅 15:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452111">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTifrGrH1TQR5Yvhsn2Dp9Agnz1YMGs5kLaCmz8kGWR1ABo_KHM32cJcz5vK8HZCIlfP_cUA9ANt9iMZPiKODCF46yJNYbxGLhJjeAmvxDUpRLnaYv8CrteFRHIfH_s8MB8u0a7nH9S6eQPdzpiSPpuk7wMqSxQZi7JYD8wSy7JIob5Si4Ll7GSWfL80EXMcjJyBEIyZPq99APMWkm5r8R8nYPes3ssuHjah6iv1pe8Lixe-UTUelkacfMOtrK9SRIUKjqJI9zrcbhUJRMY8aWJvrZxlyt7KwXN9uCLWZYoAhG8YI9RIdcD5gwxNg0H71Ozmc1ydwAXysdcdsEq-OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3417c43d1e.mp4?token=GdUgu9ObM0AIWXJ8eIOHgooxi87QsEItF1pkzBcobrMrsQ1WnO5S_goBC9nNXBECD5VP9DybaYrE4eHWU0QNY4UUv7AAiOQax9_g7R1UJXLV9XDGWr8xrim3hW6GI_gi7PzAwSNbrh1VzQzsR1wSG6GNOWOhcUCkcqghajuSNjhtkm5Q4uV90Ekzz60JwPVPOk8YW5MYCizar0lM4bGxQuD0s2tlidZqdbH1rXdIoLEj2gXVx9_N-PnsirKFKLNRke3gQW6zA9DpCmZEqJYFjS2opoLS3BdxPfdV6WQ1slPgF3iewMnqB69jxCbKVnVoVhHESWHY1oBanyZb83YkdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3417c43d1e.mp4?token=GdUgu9ObM0AIWXJ8eIOHgooxi87QsEItF1pkzBcobrMrsQ1WnO5S_goBC9nNXBECD5VP9DybaYrE4eHWU0QNY4UUv7AAiOQax9_g7R1UJXLV9XDGWr8xrim3hW6GI_gi7PzAwSNbrh1VzQzsR1wSG6GNOWOhcUCkcqghajuSNjhtkm5Q4uV90Ekzz60JwPVPOk8YW5MYCizar0lM4bGxQuD0s2tlidZqdbH1rXdIoLEj2gXVx9_N-PnsirKFKLNRke3gQW6zA9DpCmZEqJYFjS2opoLS3BdxPfdV6WQ1slPgF3iewMnqB69jxCbKVnVoVhHESWHY1oBanyZb83YkdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
۲ شهید و ۱۱ مجروح در حملۀ موشکی آمریکا به مرز شلمچه
🔹
معاون استاندار خوزستان: در حملۀ موشکی دشمن تروریستی آمریکا به مرز شلمچه، ۲ نفر از هموطنانمان شهید و ۱۱ نفر مجروح شدند.   @Farsna</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/452111" target="_blank">📅 15:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452110">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51fa914cc2.mp4?token=r0nwL6Ou_Pym5eIE_PBO4yjUtbKRCoe4KqCzjQYj-p_SR6xY92ChgSv5Uc03-l-3ITwBo21lcP4bN174YcsRHiBi00Wm_rXA4IXaakGb9PS-l7HWnmwvfF1AaikZGRivi4471GlG-o_woyznV6ih9igLktAX0zXTOM0gwGLpKd9ktZTBmO2vux8v8a6a8UwwRYrkEfr-8Tzai2UAyWA7JZzyYmORNKThDLpiIJ0ZmC-3yc4vpvf3OjgktoQrqTDhOaOUZBXBozntKL97R60sHQwYAW9aqudbw3HI6q6ZXGzYGyJV2YVx5u548dBZ9oz-xV61GQAWDykZjIvRYxKwng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51fa914cc2.mp4?token=r0nwL6Ou_Pym5eIE_PBO4yjUtbKRCoe4KqCzjQYj-p_SR6xY92ChgSv5Uc03-l-3ITwBo21lcP4bN174YcsRHiBi00Wm_rXA4IXaakGb9PS-l7HWnmwvfF1AaikZGRivi4471GlG-o_woyznV6ih9igLktAX0zXTOM0gwGLpKd9ktZTBmO2vux8v8a6a8UwwRYrkEfr-8Tzai2UAyWA7JZzyYmORNKThDLpiIJ0ZmC-3yc4vpvf3OjgktoQrqTDhOaOUZBXBozntKL97R60sHQwYAW9aqudbw3HI6q6ZXGzYGyJV2YVx5u548dBZ9oz-xV61GQAWDykZjIvRYxKwng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
پیام سپاه به مردم اردن: حق قانونی و شرعی و منطقی ماست که پایگاه آمریکایی مبدا تجاوز به کشورمان را هدف قرار دهیم
🔹
روابط‌عمومی سپاه پاسدارانی: مردم شریف و نجیب و اردن؛ برادران مجاهد شما در سپاه پاسداران انقلاب اسلامی، در تنبیه ارتش کودک‌کش آمریکا و پاسخ…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/452110" target="_blank">📅 14:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452109">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6380e0c517.mp4?token=qybeIWlo664F2elWR9bCwrrJzdxN48-qkTJ04kzauDeEDtVxVB8okxpNtz5DIxubgseEiEX_gRnzyTLILWl_abm60dDSqoaaQTl3rQqPxlPpg11pe_PNZOxtrZERK49YOLj7AHB_VmmgPB2iozEHcWflEDzMarPn2rheMd7v_I5vNRTBkj7S36huxXzaGJtwo39jGU2j4dDbZJQeW13M7U3KjebeVUv2wWtLgjcTLVEdu5DSLaPrOEQvl4heFnuJWAK6b2ErMubuGGbPdgYDNNzI4dYdKeHoZvSnyyyUStJPJSqO9Dq4PLq6x13oNumz0SJyFuslg_hdri1Ikcqnxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6380e0c517.mp4?token=qybeIWlo664F2elWR9bCwrrJzdxN48-qkTJ04kzauDeEDtVxVB8okxpNtz5DIxubgseEiEX_gRnzyTLILWl_abm60dDSqoaaQTl3rQqPxlPpg11pe_PNZOxtrZERK49YOLj7AHB_VmmgPB2iozEHcWflEDzMarPn2rheMd7v_I5vNRTBkj7S36huxXzaGJtwo39jGU2j4dDbZJQeW13M7U3KjebeVUv2wWtLgjcTLVEdu5DSLaPrOEQvl4heFnuJWAK6b2ErMubuGGbPdgYDNNzI4dYdKeHoZvSnyyyUStJPJSqO9Dq4PLq6x13oNumz0SJyFuslg_hdri1Ikcqnxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار رادان: ایستایی یک زائر در شناسایی و مهر گذرنامه در مرز شلمچه فقط ۴ ثانیه طول می‌کشد
🔹
بیش از ۳۰۰ هزار نفر تا الان از مرزهای چندگانه وارد عراق شدند.
@Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/452109" target="_blank">📅 14:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452108">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcab2e787b.mp4?token=phBdzCikdLO9ukImB4HjzwoYgKqsIcW8cGvfzbBFwcjIlOCTDywaCFgyzS74j8aLyA5P-nVF9n4qsp5i6iFUNC3NvOZyiX4Hks_FWHVJwDbpy8c8uDjtJixGR97gO49hxeVWa8J5pZb_EyGnJeenR7oqk88bgmafSS16OAC7TMNyje1nmV-raa_1c9Me5l2VRfs-T06pRKX-nviYHK7iEg2FUuLfaPmt9nk3u4-NvgrBtMlp_rQDXHndO6n4MyQCpV2h4sm5s2or7X-HTHWbhsspivzK6FUf1vdhlveIrdwLRDnNW0KVUVcrnuUv5vq2p8HmfpXnAk47Qh5n7iUgZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcab2e787b.mp4?token=phBdzCikdLO9ukImB4HjzwoYgKqsIcW8cGvfzbBFwcjIlOCTDywaCFgyzS74j8aLyA5P-nVF9n4qsp5i6iFUNC3NvOZyiX4Hks_FWHVJwDbpy8c8uDjtJixGR97gO49hxeVWa8J5pZb_EyGnJeenR7oqk88bgmafSS16OAC7TMNyje1nmV-raa_1c9Me5l2VRfs-T06pRKX-nviYHK7iEg2FUuLfaPmt9nk3u4-NvgrBtMlp_rQDXHndO6n4MyQCpV2h4sm5s2or7X-HTHWbhsspivzK6FUf1vdhlveIrdwLRDnNW0KVUVcrnuUv5vq2p8HmfpXnAk47Qh5n7iUgZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نشست خصوصی پزشکیان با نخست‌وزیر عراق درحال برگزاری است  @Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/452108" target="_blank">📅 14:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452107">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383c67b5bc.mp4?token=XKWCXckVXl_VnBO-9TfLXttQQyDup1B1VtBjOqmPxMMhGO8-rOtY5JMt0E68qOuWn9qgSEEC-GsvkFEaWEjEYl5ojN61iwyspLaeiQyGynXA9Mv7futV2215fHIOmGObbTcEsGugVImElTNuaXFIqHCafuytRKYy8URdqiBrW_FKtRiG01Q-Hxb91vCd53lGV8f1jqhj3uAH5C0mVSI_bFEF7bl2g-4IaVU1YKa-ybvCEB-1oRopoLv3ckes_2vkUAJRfhAYe67V7ooGKTNDkBS4xInwHzc9LXkkLA3j3Vt1vclAlHwF5EUMIsuhmc_V5lrZ5ciQkelMjXjX2VxdCq_ndh1tUCPkq-K_SkrsQoB1I1MlFGpp8p6on8Hyv1xKy7vDKGlQt_R4K8g9qrv1hflZrAeqP-RViSaUn5FnhQEDXWAOH21fr1KwIPjlPzp5cEf8Jw89Hj6xd2DLrtUSwlH7vZBGon1Jc2qQcomn6DCFuOeSRJX45ntTax5WLJlWESllv3OTn2ksPTiJxkfl-Y_QZzbZM7i0ENEL5T9aZSifWAwqt_2qCtUJtCsEhYuYmfA6qBuDpymDS1LfPVSb8640vOSmvEMkQw_vM0MR6EK0aP6nB0-Y8fEgoNqKJRUyoLzIQb2P-0HdzULt2U-K1MfOmfIiyGJJHq0cGmKY1Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383c67b5bc.mp4?token=XKWCXckVXl_VnBO-9TfLXttQQyDup1B1VtBjOqmPxMMhGO8-rOtY5JMt0E68qOuWn9qgSEEC-GsvkFEaWEjEYl5ojN61iwyspLaeiQyGynXA9Mv7futV2215fHIOmGObbTcEsGugVImElTNuaXFIqHCafuytRKYy8URdqiBrW_FKtRiG01Q-Hxb91vCd53lGV8f1jqhj3uAH5C0mVSI_bFEF7bl2g-4IaVU1YKa-ybvCEB-1oRopoLv3ckes_2vkUAJRfhAYe67V7ooGKTNDkBS4xInwHzc9LXkkLA3j3Vt1vclAlHwF5EUMIsuhmc_V5lrZ5ciQkelMjXjX2VxdCq_ndh1tUCPkq-K_SkrsQoB1I1MlFGpp8p6on8Hyv1xKy7vDKGlQt_R4K8g9qrv1hflZrAeqP-RViSaUn5FnhQEDXWAOH21fr1KwIPjlPzp5cEf8Jw89Hj6xd2DLrtUSwlH7vZBGon1Jc2qQcomn6DCFuOeSRJX45ntTax5WLJlWESllv3OTn2ksPTiJxkfl-Y_QZzbZM7i0ENEL5T9aZSifWAwqt_2qCtUJtCsEhYuYmfA6qBuDpymDS1LfPVSb8640vOSmvEMkQw_vM0MR6EK0aP6nB0-Y8fEgoNqKJRUyoLzIQb2P-0HdzULt2U-K1MfOmfIiyGJJHq0cGmKY1Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استقبال پزشکیان از نخست‌وزیر عراق در کاخ سعدآباد  @Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/452107" target="_blank">📅 14:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452106">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35decde86f.mp4?token=MI1DLgVPr4XFK7TZFypTVJmdfpxR_VcoqY5ekwkCkwcMI9CNEKOt67arcpfL_eIfZhhkSmQPk8mSGUL19m6hFDjkq7-HksgGnJog-CgraNLt3jwtQ0ltsO9Q4gdZvAu-PkgSusgADpcPUwQxdHfoBdvIM6MTzHv1AkI1ff8Go53Bbz4Wx6MCSqVoKMFl2ihiNVAOECPJ1WdZF7j4ibAcXNrSyl-ZWKnT8wadp2ySqTOJeu-3P8vSYyfUlPIUD-QiKBrTzpp_zYjlatUjWoF5MIMviUD8xUqq0vNaAB_LlzSvPdKffSveGgurm8QVNwwyE5WfR7HHVwuASIskjmeApg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35decde86f.mp4?token=MI1DLgVPr4XFK7TZFypTVJmdfpxR_VcoqY5ekwkCkwcMI9CNEKOt67arcpfL_eIfZhhkSmQPk8mSGUL19m6hFDjkq7-HksgGnJog-CgraNLt3jwtQ0ltsO9Q4gdZvAu-PkgSusgADpcPUwQxdHfoBdvIM6MTzHv1AkI1ff8Go53Bbz4Wx6MCSqVoKMFl2ihiNVAOECPJ1WdZF7j4ibAcXNrSyl-ZWKnT8wadp2ySqTOJeu-3P8vSYyfUlPIUD-QiKBrTzpp_zYjlatUjWoF5MIMviUD8xUqq0vNaAB_LlzSvPdKffSveGgurm8QVNwwyE5WfR7HHVwuASIskjmeApg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین اژدهایی برای دفاع از ایران، در تنب بزرگ قناصه به‌دست شد
@Farsna</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/452106" target="_blank">📅 14:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452105">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b027328a6.mp4?token=cVtBnYPFJRVTH5TQpsE7-FUawfJU6Gk2umzbU_HuCYN29f_1Nx13MqAMO0epasmSdidnvpHv733qwaJyAeivlZ9-wHkzMSpXNmOB8dqva3rx_K4l73PkswP_sDHlV2ExFYkW4RolHdtAOsvmQ83qWbWdpWS0IRSb71LKz99MCUbonB_btQCbxR4-W1hbRYb0XY5vCMZseYWVBWVmjU9VeHhyGXr_e0vOlFzY6PPWYxVPtA9ctDAoKGVkosF11T2R09RmRff0drl5tpHBN2or5ISMImnI_Frgs8-zLvlSQXGn-akm1CNntwGll19QPneC6o4H1Rnhg3x9xr1QFuBdww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b027328a6.mp4?token=cVtBnYPFJRVTH5TQpsE7-FUawfJU6Gk2umzbU_HuCYN29f_1Nx13MqAMO0epasmSdidnvpHv733qwaJyAeivlZ9-wHkzMSpXNmOB8dqva3rx_K4l73PkswP_sDHlV2ExFYkW4RolHdtAOsvmQ83qWbWdpWS0IRSb71LKz99MCUbonB_btQCbxR4-W1hbRYb0XY5vCMZseYWVBWVmjU9VeHhyGXr_e0vOlFzY6PPWYxVPtA9ctDAoKGVkosF11T2R09RmRff0drl5tpHBN2or5ISMImnI_Frgs8-zLvlSQXGn-akm1CNntwGll19QPneC6o4H1Rnhg3x9xr1QFuBdww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سه پایگاه آمریکا در کویت هدف مجدد حملات پهپادی ارتش قرار گرفت
🔹
روابط‌عمومی ارتش: در پاسخ به ادامۀ گستاخی‌ها و تجاوزات دشمن خبیث به کشورمان، ارتش ایران  در مرحلۀ بیست‌وسوم عملیات صاعقه، ساعاتی قبل محل استقرار انبارهای مهمات و اقلام لجستیکی  ارتش کودک‌کش…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/452105" target="_blank">📅 14:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452104">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67e54c631b.mp4?token=aN_hfd8-4FUvg_29aPKgVgKUStVlp8Syjvq7lUVqIzkssKbGTmzSw2YtdKaMmtE151yeJBco70BipOJfckKvEmvE9OJJqnkGGLEvBzD4NHe0g-mE3Srr3vOLF2Q8gH_v2GHouwXUbkzpOeLitw_YRmNPVW7j2gyj8RQO1WCCUnkBy5Bn2jOGtNS-GwMohzrVZDP7OOWw6_as2Hhaz4BYabPfpNcXzi0IULsAzlY1By2nTi_t6mBmImxxVwF_UHh32XkJQERHaQ2d9WdVIbslFnTpcOqB2C0q1dkZf3sULj99mlvc4ze6zZKr1HC4hsRkAioTlPzA97XHtSUk69QzQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67e54c631b.mp4?token=aN_hfd8-4FUvg_29aPKgVgKUStVlp8Syjvq7lUVqIzkssKbGTmzSw2YtdKaMmtE151yeJBco70BipOJfckKvEmvE9OJJqnkGGLEvBzD4NHe0g-mE3Srr3vOLF2Q8gH_v2GHouwXUbkzpOeLitw_YRmNPVW7j2gyj8RQO1WCCUnkBy5Bn2jOGtNS-GwMohzrVZDP7OOWw6_as2Hhaz4BYabPfpNcXzi0IULsAzlY1By2nTi_t6mBmImxxVwF_UHh32XkJQERHaQ2d9WdVIbslFnTpcOqB2C0q1dkZf3sULj99mlvc4ze6zZKr1HC4hsRkAioTlPzA97XHtSUk69QzQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لفاظی‌ روبیو: پاسخ ترامپ به ایران «سر در برابر چشم» خواهد بود
🔹
وزیر خارجه آمریکا بر تهدید دیروز دونالد ترامپ به هدف قرار دادن زیرساخت‌های ایران که مصداق جنایت جنگی است، تأکید کرد و مدعی شد ایران در صورت ادامه روند کنونی «بهای سنگین‌تری» خواهد پرداخت.
🔹
مارکو…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/452104" target="_blank">📅 14:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452103">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9Qho1XyXef9NEzM_QJhO2Bv-tX0K8xa7kZuGu5ia5MqyTQVAVYj8S3V6zWHfD_sKeVrOv4kaJiXVleaq0kNCiXBypYCPoDY92-qlUYsDgOVVPFxQ7Yy_GN0A_wBDzPuAFnlcxsTZksjRfplw9onAU-0ZPOpQCgtGJdWBPdJ_x0ldaI9qYQDvudFgcUGe7TDayhpgWdIxApaaYpCF6B6Wgcn5Fom-ZAchbCaf7-lb9cOrtgQ9GGZWrrLObdddGm_8_y0KFdtlYsbjnYx_YNTEFlScZZQs3oAGR5wGC-KMA9YcZ5ItjNND9sAn6sDGYAeJfW79Cddk90lMCzGZ8uopA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مراسم بزرگداشت شهید زهرا حدادعادل از طرف خانوادهٔ ایشان
◾️
پنجشنبه ۱ مرداد، ساعت ۱۷ الی ۱۹
◾️
میدان فلسطین، مسجد امام صادق علیه‌السلام  @Farsna</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/452103" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452102">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a50e3811ea.mp4?token=LhXTZLrK1yPB6SGy4Zb6E-wyhEf0QMZ5H-Tmd5siSaRmwRZUSXXCwo4E9eLn3ziUopg3T85nCDaefwuIgjC1D7Rnju08CGhLpQrIE329FwoRyDxuH-j52V2UhbX5tRcncp0_A2HAWFWjp-5jJSTD-M1eKJDsf15m3tpUVzk278P9PAmAsuR_nhgLUFY_SfEoKb-haviqk9izPeAXcWiFzEjqHbnt6QRYqWTeo_33jrj83lr-YznIJL3COySsHSrpW3k-FpfMJFZYau0SXlSzGeWnBtoVNyHb3YZ9K0UEhvpaW4v8sn_QjxKT_6jYSZGsuKdV5TPaShV1lZdIGGcq5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a50e3811ea.mp4?token=LhXTZLrK1yPB6SGy4Zb6E-wyhEf0QMZ5H-Tmd5siSaRmwRZUSXXCwo4E9eLn3ziUopg3T85nCDaefwuIgjC1D7Rnju08CGhLpQrIE329FwoRyDxuH-j52V2UhbX5tRcncp0_A2HAWFWjp-5jJSTD-M1eKJDsf15m3tpUVzk278P9PAmAsuR_nhgLUFY_SfEoKb-haviqk9izPeAXcWiFzEjqHbnt6QRYqWTeo_33jrj83lr-YznIJL3COySsHSrpW3k-FpfMJFZYau0SXlSzGeWnBtoVNyHb3YZ9K0UEhvpaW4v8sn_QjxKT_6jYSZGsuKdV5TPaShV1lZdIGGcq5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصویر ماهواره‌ای از حملات امروز ایران به پایگاه ملک فیصل در اردن  @Farsna</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farsna/452102" target="_blank">📅 13:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452101">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/165b94d872.mp4?token=c7p15_HLeCMW7tRPqHluZhOThQhHIGTGmghs4NAVH_JDY7ajVTdqz_aO-7pM9i0-WvaRg2vs-qHr4_Q3fPV9CwbVm4sb5cfIg83iOXrUUNZAwT1s2Ve2jAZTtsPM5dFboWY4Bq9wso6AfT5f4rZ6qEdmvy3zUx6tZb1732yXwP9TQWIWAeWLaMWoJigNUMavMLw6QFP5fuS8vFvzKafGOZMjtwJD3of4bhEHrXguPJNI9TWGbYMimmX-zicAlYnf1J4sMZlwxgvaeC8l5SGZbXkit4-Ofm0GcJ_ejVFrxt2WANjnyPYXSEkGkYCHSGssInPIXWZnXGIG66L4xu0SLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/165b94d872.mp4?token=c7p15_HLeCMW7tRPqHluZhOThQhHIGTGmghs4NAVH_JDY7ajVTdqz_aO-7pM9i0-WvaRg2vs-qHr4_Q3fPV9CwbVm4sb5cfIg83iOXrUUNZAwT1s2Ve2jAZTtsPM5dFboWY4Bq9wso6AfT5f4rZ6qEdmvy3zUx6tZb1732yXwP9TQWIWAeWLaMWoJigNUMavMLw6QFP5fuS8vFvzKafGOZMjtwJD3of4bhEHrXguPJNI9TWGbYMimmX-zicAlYnf1J4sMZlwxgvaeC8l5SGZbXkit4-Ofm0GcJ_ejVFrxt2WANjnyPYXSEkGkYCHSGssInPIXWZnXGIG66L4xu0SLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روبوسیِ پزشکیان با نخست‌وزیر عراق  @Farsna</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/452101" target="_blank">📅 13:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452100">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be7716f95.mp4?token=hswwmAl7QMfqE2yDgNsBHq7D6HJb8uNIqpNG1fWFynfK3lt9v_mIUzOdrBaT6jDPgZ3B8R2Kcfq02h1GcfkY-GCqQ0sLorsrqfWiN_1bCY5oTsvgao6VELRHizUpB9tYUu-uJG5fLeHia9zI5NqAUpsgWGq7-gsrw5nYqqYIsjSCoG2AWDM7Ntfew33l72BTKYxayb1UoGM65zqAr8kMqhm70a7IECFrnelMkFjNLog3WSJWKU9iE5AEQpG6VNmZNmeMZuR8yBf6CK4QKGkBdgegpAd5JRpXpYW8qim-CUF0oZE5elbMqgTalc2xxUWUXjbBan2fEAz9zbHGqt4JXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be7716f95.mp4?token=hswwmAl7QMfqE2yDgNsBHq7D6HJb8uNIqpNG1fWFynfK3lt9v_mIUzOdrBaT6jDPgZ3B8R2Kcfq02h1GcfkY-GCqQ0sLorsrqfWiN_1bCY5oTsvgao6VELRHizUpB9tYUu-uJG5fLeHia9zI5NqAUpsgWGq7-gsrw5nYqqYIsjSCoG2AWDM7Ntfew33l72BTKYxayb1UoGM65zqAr8kMqhm70a7IECFrnelMkFjNLog3WSJWKU9iE5AEQpG6VNmZNmeMZuR8yBf6CK4QKGkBdgegpAd5JRpXpYW8qim-CUF0oZE5elbMqgTalc2xxUWUXjbBan2fEAz9zbHGqt4JXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نخست‌وزیر عراق به تهران رسید  @Farsna</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/452100" target="_blank">📅 13:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452099">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d19150166b.mp4?token=LfqsDYS4UkrPe6cMZhz48jUupOWh4mAsiDpm9YjpXvZyw6eOu1Kkf5nC3nsuhs3BIUM2F2GVu2Dv8DIxtlBIVo7HGw6IzGZA1e-pg4iaVUVr3aQhgF8ZdvW7_z8VXKCGx8mn9zdjwsIAjDpS8jKe0Hae2phpgl3ViZtB8SCQ-qYsYHXght7TTxXmm9-khADwxDzoxVAnYgQSHTXlaA3pUkE_udLspWyAbKLsbc6Zt04WirMAzIrqObs7U_RH4JAOoP8rm3mii9g9C7HSI76qEjgfXdPa6h2vBZXyoi-XaJGBBoLqXg2f-06lqw_YPpE2cSAql1i9lzdn-HpKd2n9PDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d19150166b.mp4?token=LfqsDYS4UkrPe6cMZhz48jUupOWh4mAsiDpm9YjpXvZyw6eOu1Kkf5nC3nsuhs3BIUM2F2GVu2Dv8DIxtlBIVo7HGw6IzGZA1e-pg4iaVUVr3aQhgF8ZdvW7_z8VXKCGx8mn9zdjwsIAjDpS8jKe0Hae2phpgl3ViZtB8SCQ-qYsYHXght7TTxXmm9-khADwxDzoxVAnYgQSHTXlaA3pUkE_udLspWyAbKLsbc6Zt04WirMAzIrqObs7U_RH4JAOoP8rm3mii9g9C7HSI76qEjgfXdPa6h2vBZXyoi-XaJGBBoLqXg2f-06lqw_YPpE2cSAql1i9lzdn-HpKd2n9PDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لفاظی‌ روبیو: پاسخ ترامپ به ایران «سر در برابر چشم» خواهد بود
🔹
وزیر خارجه آمریکا بر تهدید دیروز دونالد ترامپ به هدف قرار دادن زیرساخت‌های ایران که مصداق جنایت جنگی است، تأکید کرد و مدعی شد ایران در صورت ادامه روند کنونی «بهای سنگین‌تری» خواهد پرداخت.
🔹
مارکو روبیو در گفت‌وگو با خبرنگاران در حاشیه نشست آسه‌آن در مانیل توهمات دونالد ترامپ درباره درخواست ایران برای مذاکره را تکرار کرد و گفت «ایران مستقیم و غیرمستقیم، التماس می‌کند «بیایید توافق کنیم. بیایید گفت‌وگو کنیم».
🔹
وزیر خارجه آمریکا همچنین در اشاره به پیام اخیر وزیر خارجه ایران عباس عراقچی که دکترین دفاعی جمهوری اسلامی ایران را «چشم در برابر چشم» توصیف کرد و گفت «هرگونه تجاوز علیه ایران، از جمله علیه زیرساخت‌های ما، با پاسخی قاطع و قدرتمند مواجه خواهد شد»، با افتخار به ارتکاب جنایت جنگی گفت که «سیاست رئیس‌جمهور (ترامپ) یک سر در برابر یک چشم است، قرار است همین‌طور باشد».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farsna/452099" target="_blank">📅 12:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452098">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">هلاکت ۲ تروریست در درگیری با مرزبانان
🔹
فرمانده مرزبانی فراجا: در درگیری مسلحانۀ مرزبانان هنگ مرزی جکیگور با گروهک تروریستی، ۲ نفر از آنان به هلاکت رسیده و مقادیری سلاح و مهمات، فتیله و چاشنی انفجاری کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/452098" target="_blank">📅 12:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452097">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">هشدار حنظله درباره تداوم حملات سایبری به سامانه‌های کنترل صنعتی آمریکا
🔹
در پی حملۀ سایبری پیچیدۀ گروه هکری «حنظله» به زیرساخت‌های فناوری عملیاتی (OT) ایالت مریلند، این گروه با صدور یک بیانیه هشداردهنده، اعلام کرد که زیرساخت‌های حیاتی آمریکا در خط مقدم حملات آینده آنها قرار دارند.
🔹
حنظله تأکید کرده که دستکاری در کنترل‌کننده‌های منطقی برنامه‌پذیر (PLC) و سامانه‌های SCADA، تنها بخشی از توانمندی‌های تهاجمی این گروه است و تهدیدات گسترده‌تری متوجه شبکه‌های آب، برق و ترابری خواهد بود.
🔹
این هشدار در حالی منتشر می‌شود که اداره تحقیقات فدرال (FBI)، اخیرا با انتشار بیانیه‌ای امنیتی اذعان کرد که بازیگران سایبری، تجهیزات صنعتی شرکت‌های Rockwell Automation، Schneider Electric و Siemens را هدف قرار می‌دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/452097" target="_blank">📅 12:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452096">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
وزارت کشور بحرین: آژیرهای هشدار به صدا درآمده و از شهروندان و ساکنان می‌خواهیم که به نزدیک‌ترین مکان امن بروند.
@Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/452096" target="_blank">📅 12:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452092">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b4e206616.mp4?token=lIqBwe7B_yunAnpfmT-QpSTzTwdUoozD2hqrVVY1-fFq2GCaHTwX78QTzmLKMxa89fVz6px4Rj8hYmEg1nd_2YiAsOe-0SBLQlif-MkdImA_LJtKYVTnc_YCIo7xa-r9-VyGfd955dPaNQa5bX_0F6MpcRbx7LPG58EgDP1SRKuMtZDlrCDbnOIfe96dkhRoDyGpiPtxwn_TW8nbq0fXygjR3OgynatGsfLn_vHP7dakQjerDLVsjzOfM0t9IAtMreriYK1tz_jOx-eD8zE6PdqPZ8DruR_cblY5tLol0Qlr1buo8S0ltI6X250GCxh5z6q7eAdrWSd34pPxDIxaHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b4e206616.mp4?token=lIqBwe7B_yunAnpfmT-QpSTzTwdUoozD2hqrVVY1-fFq2GCaHTwX78QTzmLKMxa89fVz6px4Rj8hYmEg1nd_2YiAsOe-0SBLQlif-MkdImA_LJtKYVTnc_YCIo7xa-r9-VyGfd955dPaNQa5bX_0F6MpcRbx7LPG58EgDP1SRKuMtZDlrCDbnOIfe96dkhRoDyGpiPtxwn_TW8nbq0fXygjR3OgynatGsfLn_vHP7dakQjerDLVsjzOfM0t9IAtMreriYK1tz_jOx-eD8zE6PdqPZ8DruR_cblY5tLol0Qlr1buo8S0ltI6X250GCxh5z6q7eAdrWSd34pPxDIxaHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هتک حرمت مسجدالاقصی با یورش بیش از ۲۳۰۰ صهیونیست
🔹
هزاران صهیونیست از صبح امروز در دسته‌های ۱۵۰ نفری تحت حفاظت شدید نیروهای اشغالگر اسرائیل و با همراهی ایتمار بن گویر به مسجد الاقصی یورش بردند.
🔹
وزارت اوقاف اسلامی قدس اعلام کرد تا این لحظه بیش از ۲۳۰۰ شهرک‌نشین افراطی، همزمان با مناسبت ادعایی «سالروز ویرانی معبد»، به مسجد الاقصی تعرض کرده‌اند.
🔹
گروه‌های افراطی معبد هر ساله این مناسبت را به عنوان سنگ‌بنا و ایستگاهی اصلی در مسیر تشدید اقدامات علیه مسجدالاقصی قرار می‌دهند. این روزی است که این گروه‌ها تلاش می‌کنند به هر طریق ممکن حضور و قدرت خود را در میدان ثابت کنند و خواهان تغییرات گسترده در وضعیت موجود مسجد و شهر (قدس) شوند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/452092" target="_blank">📅 12:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452091">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">مرز استان‌های فارس و کهگیلویه لرزید
🔹
دقایقی پیش زمین‌لرزه‌ای به بزرگی ۴.۱ ریشتر در عمق ۱۰ کیلومتری، حوالی بابامنیر شهری از توابع بخش ماهورمیلاتی شهرستان ممسنی در استان فارس را لرزاند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/452091" target="_blank">📅 12:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452090">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8922578c34.mp4?token=Jgho7lMZBPEiyzg_MIG5pwmEs0_64XajWxqvzBQ67OHg2Hyz0FFiX5X8uLwtt7VxbSkCjw3pMYKkKxYxJKhVNjz1EMC9EuUj8ECh3hMYLW25wtFAauvan-jSLZfk7F1Dd3RbS0Cwbk7QV7xTGUx2ASjYFoLtL3BYv6gT_fc5Gs4pQ2ATF_vrbQ7dpar_ARwWa3CdL3uDn8i2FcE7gUTfjewybuZ29bQakodG107eLbahV17IQHOsVePo2gxRSUxzxTbuQ65MfmMmCh11wYWZ1MtvxU_MI2Ftg7-Y99fXyPYmcUOWfrGCj28vVvPXyYsdN5Kg1HIqW4zzzan9664PrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8922578c34.mp4?token=Jgho7lMZBPEiyzg_MIG5pwmEs0_64XajWxqvzBQ67OHg2Hyz0FFiX5X8uLwtt7VxbSkCjw3pMYKkKxYxJKhVNjz1EMC9EuUj8ECh3hMYLW25wtFAauvan-jSLZfk7F1Dd3RbS0Cwbk7QV7xTGUx2ASjYFoLtL3BYv6gT_fc5Gs4pQ2ATF_vrbQ7dpar_ARwWa3CdL3uDn8i2FcE7gUTfjewybuZ29bQakodG107eLbahV17IQHOsVePo2gxRSUxzxTbuQ65MfmMmCh11wYWZ1MtvxU_MI2Ftg7-Y99fXyPYmcUOWfrGCj28vVvPXyYsdN5Kg1HIqW4zzzan9664PrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نخست‌وزیر عراق به تهران رسید
@Farsna</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/452090" target="_blank">📅 11:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452089">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1328df24d9.mp4?token=U06jcYwCA8Exv5R_-E4prB0hlFzLLTWTAtiVNs0gIB-mY-kCjmeJMBiRf97ZiD2xT_43TwEtAdyo2qxtduJxry5a9DLabCVHk27kqvBJaOA0fo8GI-FHnythloLYabPulgjhMdTJE_SvO1Ay4qnlBlYc5-0QxjhaYJSL0a09wm6acuHh92DOnMu-yYyHSu6ntuYFXLoRTILQBa29UTi3apQNRxPSEfxU5qTdDNPrnTQAgYa6CJZ9cZUkxlLwIXmB2rd1apvrqJGUcgHIEDi7A0BskrgqfcQAmDVNhNWxdUFJQC6Mztcy1g9K3pj--dkVIa5VMINIw4wKlOrZB8S8VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1328df24d9.mp4?token=U06jcYwCA8Exv5R_-E4prB0hlFzLLTWTAtiVNs0gIB-mY-kCjmeJMBiRf97ZiD2xT_43TwEtAdyo2qxtduJxry5a9DLabCVHk27kqvBJaOA0fo8GI-FHnythloLYabPulgjhMdTJE_SvO1Ay4qnlBlYc5-0QxjhaYJSL0a09wm6acuHh92DOnMu-yYyHSu6ntuYFXLoRTILQBa29UTi3apQNRxPSEfxU5qTdDNPrnTQAgYa6CJZ9cZUkxlLwIXmB2rd1apvrqJGUcgHIEDi7A0BskrgqfcQAmDVNhNWxdUFJQC6Mztcy1g9K3pj--dkVIa5VMINIw4wKlOrZB8S8VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دقایقی پیش صدای چند انفجار در کنارک شنیده شد
.
@Farsna</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/452089" target="_blank">📅 11:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452088">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uA40rg22dc-yB9qQ1esuXy2w8l_eqWhljx8ar0d9LgM1t3__ODHuTHsxqW9mZoPPrgnf-yTMI9KrP46Xhgynkw0nuTFSBkoZYT6-fFg060AwmlaafZdAQbOsTALb6DbQgpW9zyAPLZa2aVDei0iRu0iraG2dxMZM_Od0VrV3c0Fcjt-GkivxZPUzKANZW_rXMuytPFvdkCU2iYWpXxqiWzC8qr9a_koiTmLxpP-cK5OKtFJdDfkRCCwLv8aVPUD87MGIqiTCTgp0d1q1FFrZKzNKiKnzMJtOuRryotFGA6cInGCkEzWKZa4KZSL2jI4_2oA-qQuvQxvKrCC6FIh9yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قیمت نفت از ۹۷ دلار عبور کرد
.
@Farsna</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farsna/452088" target="_blank">📅 11:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452087">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4r3GF-MpY6hmtra6m3sRHJ5EiUTFgqQfCCBJV5dgykh9DCWeEJhRId56Pv9MLBrK15niqNSoGiQEvHdLj_flX6ccTPvzvG5rR9Wy-bL0sGRljgMFRKkXpAsqVeA9Nq_vHuYJtHeCm7tCC7_xlXEEKu4P4y7ZjPQ_xkSWS1KbW3Fi_sJs5GnrLIEu9LXOoPcgQGH-ASTVb1iAr30rIfvxoI3V0P-R2R3JU8ERzv5pE-gyZwyDiE_td3BFxA74jyif2fRtdu6h7uj3MW-JeGCXi28cixUzT1OLH1_6QLmprZa1T59ckuXu3ZtuukRcdi9t1vX4XBR5-7UNRmiWcQsTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌گروهی امید‌های ایران با چین، امارات و کره‌شمالی
🔹
قرعه‌کشی مسابقات فوتبال مردان بازی‌های آسیایی ناگویا ۲۰۲۶ برگزار شد و تیم ملی امید ایران در گروه B با تیم‌های چین، امارات و کره‌شمالی هم‌گروه شد.
🔹
هدایت تیم ملی امید ایران برعهدۀ حسین عبدی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/452087" target="_blank">📅 10:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452086">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vxwAhAjvd6QzYCvTNGq8Dw7NOlHfe4CY8_6u3fKeRuH92BJNl-pgEiIGHtfraUdknFX4B9mB8ayl_SrPTGw7sWScHfSpTWILxi-vA5REHhC2tkMthzT58_JSEAYxgXfNb4bIpCzyn0UTxJRleG1NHwB7981MeAyg4kMuA3R3I_-hWsYgK8wxnNFLnTGZHYVW8060R0wiqbWZJW2QoNRp7YemPop6SFrRsYqhJpzsTSBZebHuJqtRqSRpHS0uVve8CQ1D-MIastn1Ap7HGemBTTDC_y1PxZawhh6pZ2IopNu2egKX1zzKleS6LA12j2rWt4lriyn1qf9nz8kvAz2i8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت فردوسی‌پور را باز کنید
🔹
«من را در صداوسیما ناجوانمردانه کنار گذاشتند. از چه می‌ترسید که اجازه نمی‌دهید کار کنم؟ من بله‌قربان‌گو نمی‌شوم، حتی اگر بخواهید مرا بازداشت کنید.» این جملات را عادل فردوسی‌پور پس از بسته‌شدن وبگاه «فوتبال ۳۶۰» در برنامهٔ ویژهٔ…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farsna/452086" target="_blank">📅 10:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452079">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qcJNYHOhLRw8Mb-IcBfSvzccdDyNOz6_PMJSnCHM9ZxDK5th42lywGs1msIMFjNS_RxxOzCotzVO1XzmCYDpp3bsEZrbBGjrnLxxQ2YXywV9dXWvpRoWnujFyuk3siAsKve3EF05kVSTs1zI7bXvRtQYe7X3KUlnhv9Ohqrug74KHuei3_YtbllCyRGd9kc5o0-EiWRbbD3yDG5xRLSO_f1yuOJRIp4OVs13FSY6Y1jsIK0HCt0gJXTWscn5t47kNWDGrEWofEdB1rtDsegtWjCrRHzUn9IiMZeV7ByR5KAPZqphNaogC1qTbXSPr3WRB2CKiOGt8i0_4i8bi0u42w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UMO4ChfE97vHh2WcZwx9ZW-GyEYSsVDeEV5vyUT68ON9sjJ1HscsCKG2B1VbY_LPiNMUd0f4DOzE1ECcMqGoHh2WaFe-ljy3ZTfW9C9a2mFaiV3RhlfqJYT8UXjM5h_egzsMaovY5RB7IskmA9amQsFlJCclGOKaIhalVDozLEu-mpnpemUEXn-HnKdlUl4Jrgz4CusfQ08UKxyb3xMtVEg4LWxfnmV85WZ5xY1uLqgt600qxA_w9jKKRcICtqXXx6EWxxF4bnXtQJK69K5aXOt6Fajd8VrKNTBNFgsxLYi3dK9BFIYgMNava1jD3RjIxcAUFbppavo-Br4ycqnzAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/wBtyBBqB87JQ5r5IjFmL2_MUxBOeME3vIn1KPDCfFVu4nabCGp8iGtSg823WyGgyFPwDATC4M7FMN6v-oEENQ1mo2mcJjj4qAHKT18k-QwuIhM6CEEzdua1VGWPB8XLpJEvbRBO3JSUo3ZPQSNndB_l_rrgKDa1VVDVDUASBj7UGANmYvYtJh5hCTDib7UNtfymQWAhbwLXEFaaX0fU4ckW29rrwN6F8WFD_NVykR3G1uCnqmZjUINHIA5xDndJD3p-g64EZjR-5ib3_N2plRl4WpZixRnsMSa1pROZjaJfXnnbTRPzKFcXs2n1clCrzCSLzjrJwbN_FlU41Owk3EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QyFL1f6Ka3EYfF4dt53Wj_cqYAfc-UGaOt9dv8c6UgADqQk8R5n5qDdsPQOk7TJvYg8zj5MOGjU1trHxVOKucHjPi1uCjfwL3iz0MMz83ykkriJNYIY7B-2sJwTaFnMWqbDKF3fVUIf662dkYrRbHZTfVpTQYmGqEMPj8--DBWenstsRyM6ho6B4ozT4rmE_5b99vkGMUGqpOQn-Pr4YChbmc7P65hnMtZKWc47RIEtPCdzf_1QYfxnR-OCz5xzWwQ0UBeSvbe-1vmcQHdAeSvj0YyxNFVxjpDg3LKKMDTlcc9pYiYy3xGvElvtjdQwzjhsev1iGZ-k6tzhuleueow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bmntHuANTfE7YEl9zfGCOIhIA6Tq56sPVV9c5KOJ8eNmSccQpNFSDedbbcdVFb-zQEafBTyZInpeBdytqzpewajWjFXk_QwZpYvoDU0P-Sn6iJd-F6SF9OvzmOvmNhZvSLZbwpHCfR1_qbyAWTzdHIKUIhBF1sF5_Agp3Tnh0ZE2qt_xUA1F1WA-teFTXYRrv9mrvl-PmvYkffJQq4y9ey6JgFaqErVBkNSvFnYr_uU-1rVjpd4yBttPD-V06wcATLBMFx46ZAyaSudxKo68JHNXlQWyNKHXfO3SclTt2vqcFCG10aY29tFW4Y8CmYEuYcc82vle7K_0Q5Z0Kus0Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WG7rgPk2pjTQhYP4sFKDPk_0gvsVJ1O0uTl07cQqxRKN3GTWzS73MmVPo_-2vDSJXjWaDSjwwz7gXwpA2OLQl7acIOv7boMy4g81ARQCOqh79OMlEhRAzjvUuIPlYc2Tvpz8zQb2wVBxp3DPWWJRnhnd46gf_AE5vU1VLG0_xHc2s8p9jwkTx_wQ-Foe5QBey1gpgIWnRCdUy0fwIG9NCYE3fPiq8lHiUd5TIAjVztKS01ya2hDaT_34zN4xLSRYJrguBhPgoM-seEVnI-gBG_f4ltV4JcQD6MiiDmEnBv_fL0TpzZDreJFsN6QjSNF21mVV-glyBjkOniTHRL_M_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mMK6JmvAOu5qk1VsjtwUIaE2prokalBGkhnci91iXDLEcajVWQSotAtE4Gq1i35KXjwOKO3bk5I05IjnkNi80GJWobIiZxJXG38ysraScm7ua_5wMMWeXLC7O3Pd4Hw5M_a9Y6t3U39A3uZvCfymg1_agtIgbo9t33nIzeGRhtH5kXxZwiYTvisOTlDh3YDr2PuC0SzsnE32Y_ytaOTrAgaulan37yHgVLyHbJ1P_X6zoqRcWDaQTFtKPw2op1hzULJp473tpLB2YzlvxzuHRytcA3va8vcUXZ9aGC_h8iVMc8FDxVR8XI6qWFOdpltOAkdkxaGnyEOsWuO9kSFW0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⬇️
با حضور اکثریت سهامداران رقم خورد
✅
تصویب صورت‌های مالی سال ۱۴۰۴ بانک صادرات ایران در مجمع عمومی
🔹
مجمع عمومی عادی سالانه بانک صادرات ایران با حضور اکثریت سهامداران برگزار شد و صورت‌های مالی منتهی به پایان اسفندماه ۱۴۰۴ به اتفاق آرا به تصویب رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/452079" target="_blank">📅 10:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452078">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bw5KQtrEuGL1afjPGrEu5-tXF_9mJK-KsKpJe2rRWfyPQLu63qSbODGjA4s_glPzKAfnIVaHmzgbjdz7bqvgU5t2ZCGMy0DV-C9azsS1g5YCifdFtHxIkNCfPYkpHKbAlsyRtXQQyQr0UwUYw6XgF8qeIWQvScqioBIlUAnKHqcDWzlDPuQtBGop26piIEJ4Bl-EpTSrTAJXTUdeS0W604_VcECD7V1Kt-BBA6YgR66hCs5a6De-aVcs16UeymZbpo7nGXLtAMm8--ARHFq5sdso6bNGK7Sn2Cv4tJAFzJo7uihZNvWPWsKSQ4yhFi0K4ATqoerEMFMSBFzt95WtPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
به مناسبت اربعین حسینی و ایام شهادت امام رضا (ع)، سدن پوش برگزار می‌کند:
طرح فردوس – نذر حجاب
✨
چادر حریر اسود با قیمت نذر (بهای تمام شده، بدون سود)
چاپ رایگان طرح‌های مفهومی روی تیشرت
✨
هر تیشرت با هر طرحی که دوست دارید، در محل چاپ می‌شود
محصولات ارائه‌شده در این رویداد:
▪️
چادر حریر اسود نذرحجاب
👕
تیشرت‌های مفهومی
🧕
انواع عبا (بزرگسال و نوجوان)
▪️
انواع شومیز مناسب اربعین
🧴
انواع محصولات ارگانیک و بهداشتی
📍
آدرس
: تهران، نازی‌آباد، خیابان بابایی، بعد از کوچه ترابی، پاساژ زمرد، طبقه همکف، پلاک ۱۴ و ۱۵
📅
تاریخ
: ۳۱ تیر تا ۲۲ مرداد
🕙
ساعت
: ۱۰ تا ۲۱
✅
ایران‌تن | واحد رویداد‌های سدن‌پوش
🆔
@irantan_roydad</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/452078" target="_blank">📅 10:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452077">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/452077" target="_blank">📅 10:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452076">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3u2t6jFgfj8PJgbwZaffkrwZNtQKvUwYtLsHmOX7EjTXJCWbD89WPFyk9fC_yibjqpNPvyYLgVn-O32mTPf1ywr1g7E1t9YZUv8NvizRDQD35Zi6uEy2XBF2jV_XbtVd1w0uQrOtcoOXcm8S5IpswWnA7VUu-JdS9BjoLyVJogK4N8pd_YkzFfIAAM5-XFNw_qwftL3vtOYSdhEvjtBJJMGWsboeu1cN1eCDrUuWo_FQ2GGd33I9PaqFIapsx1AETcs7eYrFcXECF4CoAvUXqpk5g4xf0b-TbFtU9eWmdMeUFtqWK_fvQZaBJOetHQzE5xrAi8lMbmb1Z8RfdCOtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد توکلی، عضو مجمع تشخیص مصلحت نظام درگذشت.  @Farsna - Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/452076" target="_blank">📅 10:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452075">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVj-tFTLrwxo3j4lOj5dXGcwK8mcV-VpQlq7zaa75GsmDRHZtjRtOoWREt1K1fW4Auh1tIFGnIvugnwqm04UzdKtRuVcD4o6aOno4r_UyUacoSJ_nWt0-IYqbOfbhzCPAotcW92K3TAXU8fKR1RjZF0peppcAJicIWy7HD5dwNdhpANcbxs9RqFnzx4JEWHjr36n9FIcBWsHzk0pcVFeNqk3AJxC0pxgFNV9QkuhfPHEYkXLHJu6xlSpYiwPEKYd0g5Q5Ur17XTTu3Ft4RCwp-L9I4CUsTOfjIGOrGpRmrnx-mshGAD7BKCRJJxdWZx_7U518ZEjU29qgOoler_vkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ سردار قاآنی: رژیم صهیونیستی باید بپذیرد که با وجود همۀ جنایت‌‌ها نتوانسته مقاومت را متوقف کند
🔹
پیام سردار قاآنی درپی انتخاب خلیل الحیه به‌عنوان رئیس دفتر سیاسی حماس: عرض تبریک انتخاب دکتر خلیل الحیه به عنوان رئیس دفتر سیاسی حماس، باید این انتخاب را به شخصیت‌های…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/452075" target="_blank">📅 09:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452074">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEnneJjOL2SMIOdhEzmS4pm9IdvlQefFLuiHpfrMdkHAZX2bzgSZzngDIr9DQnTuU5XTRD7ni6NClJ9OcMJ0yWfiVcaToJkZP7Fx78L3tGamaBKvP-TEJFSl6kr1PQUH2em8yPOgS-psf2ITrwGBwiRhoBDy7K1LITPopzVX9VCTYwLPonGtdeelyPZ5uvY59zws4bOQrYHFkuh36lJFPF9qyqHqrMbHB_ZBXuVsuAzC4SY2gr31FHLClEh1G4y3Opf0lCb908EqLE8X5KJCbgWoiIdByAavrYxD6bcoeneuUVViC41WzZyCrBtG5Pf8tdziYvcqUXpQ-6X810FSYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مخابرۀ کد اضطراری توسط آواکس در آسمان عربستان
🔹
یک فروند هواپیمای آواکس E-3 سنتری (سیستم هشدار و کنترل هوابرد) نیروی هوایی آمریکا پس از ساعت‌ها فعالیت بر فراز شرق عربستان و در نزدیکی قطر و بحرین، بامداد امروز کد اضطراری ۷۷۰۰ را مخابره کرد و مسیر خود را به‌سمت پایگاه شاهزاده سلطان در عربستان سعودی تغییر داد.
🔹
مخابرۀ کد اضطراری ۷۷۰۰ به معنای وجود یک وضعیت اضطراری و فوری است که نیاز به فرود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/452074" target="_blank">📅 09:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452073">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTTd4_R9t12ZqGT4FMUV1ebVDBeY2M86koIvCcFD8te0Sy6dMLaUJ_S9hiXCzUBFauBT3WKon9bjqkY8QsfpSivoCbXluV6RZCOtqt6ZiqdyMv46xlYiIqP1QVptwBc2n5_t-Q6G4uQ-APh5_7yJ2Q5zbdp-ddDtZjHlo9eeHAwdVMC5_5gYCU8ytfMCsMdBZXtvToa-402y9qSK_zq_s20LYVpt-IAqLdXYQZAfs5Lh4TA3CtaRXZSBbgF7iKvKaOr8_TXCW64iei0O-Vg_6rBjZ_vQoggmKYzNJGk-VwCPf4Ui0IcXQrsqHbzHrExcBXeuaAeszefomVkGwMG3zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازدید معاون اجرایی رئیس‌جمهور از پل B1
🔹
این پل که می‌توانست ۳۰ درصد از ترافیک تهران و کرج را کاهش دهد در جنگ رمضان مورد حملۀ دشمن آمریکایی قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/452073" target="_blank">📅 09:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452072">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
پیام مهم سپاه به مردم کویت: آمریکاست که تمامیت ارضی و سیادت شما را هتک کرده نه ما
🔹
روابط عمومی سپاه پاسداران: مردم شریف و نجیب کویت؛ برادران رزمنده شما در سپاه پاسداران انقلاب اسلامی در تنبیه ارتش کودک کش آمریکا و دخالت های آن در تنگه هرمز، یک انبار بزرگ…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/452072" target="_blank">📅 09:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452071">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">خطر سیلاب و طغیان رودخانه‌ها در ۴ استان
🔹
سازمان مدیریت بحران کشور: با توجه فعالیت سامانۀ بارشی از امروز تا شنبه هشدار سطح نارنجی در سیستان‌وبلوچستان، هرمزگان، کرمان و فارس صادر شده.
🔹
احتمال وقوع سیلاب، طغیان رودخانه‌های فصلی، سقوط سنگ از ارتفاعات، شکستن درختان کهنسال و آسیب به محصولات کشاورزی وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/452071" target="_blank">📅 08:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452070">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">حملۀ هوایی دشمن آمریکایی به شهرستان کیار
🔹
معاون امنیتی استاندار چهارمحال‌وبختیاری: بامداد امروز در پی حملۀ تجاوزکارانۀ دشمن آمریکایی، نقطه‌ای در شهرستان کیار هدف حملۀ هوایی قرار گرفت. حادثه خسارت جانی نداشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/452070" target="_blank">📅 08:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452069">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">احتمال صدای انفجارهای کنترل‌شده در دزفول
🔹
روابط‌عمومی فرمانداری شهرستان دزفول: از ساعت ۹ صبح تا ۱۱ امروز، انفجارات کنترل‌شدۀ ناشی از امحای مهمات توسط نیروهای مسلح در برخی از نقاط شهرستان انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/452069" target="_blank">📅 08:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452068">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24bffd69d7.mp4?token=gkUfFUqEe6kaBMmePgi703y4e5FJR2EnhneRgKboQ7fipz1BYzpYTI5fdmt9Mgy1Y6nggvTxkGSRb75tTdjQ3mAljobH894v-W3O7y-PnRYW7pPC3XtlqV0fCe9fYgLvvYv3-Yg1_yzzAKJt_Mvzie8so3Plh9zACPwCMYDbOejZq7zK6dkKMbejC_I4yT8E99YQbGxEAHdr-OMjtLTXEl71UaMoCr85PbsVcHjtS7ho-TB5p3onsrgUJGDN4nBXzCJdqtJDAc3wzvYrLp19VDbQABO1YCIDI8eNyhwYU60mrxl1H3oa3bc3evZ90UgfGAHrw-hBhypkZO0_0jGkZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24bffd69d7.mp4?token=gkUfFUqEe6kaBMmePgi703y4e5FJR2EnhneRgKboQ7fipz1BYzpYTI5fdmt9Mgy1Y6nggvTxkGSRb75tTdjQ3mAljobH894v-W3O7y-PnRYW7pPC3XtlqV0fCe9fYgLvvYv3-Yg1_yzzAKJt_Mvzie8so3Plh9zACPwCMYDbOejZq7zK6dkKMbejC_I4yT8E99YQbGxEAHdr-OMjtLTXEl71UaMoCr85PbsVcHjtS7ho-TB5p3onsrgUJGDN4nBXzCJdqtJDAc3wzvYrLp19VDbQABO1YCIDI8eNyhwYU60mrxl1H3oa3bc3evZ90UgfGAHrw-hBhypkZO0_0jGkZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خروش ۱۲۰ متری آبشار «کردیت» در دل زاگرس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/452068" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452067">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69a0fec006.mp4?token=Ab8Vyxf4YUWDTlBFPbiq52Iw800YFQPXsCDsw2mIHGn_xFWT_YjXbjPmOoD0HNfD5ks6P7U-37BlKFwRv9PyZMW0bu4ShEvL8dmQWyMJySK1_78eqb6VaQRfggJJ3Vx-vha6wCIXIep8SgX2SvrG4D6sj1zpYn9zxp3su8S0ITUI2sP5I8ufoN5xljyJE7oDiGuBQWZk229rNYxi3TfKPxZ-pJs1WpFyG2FMbSQTL4nO2GwsxjLA6EKluuv09jj3QTHzFqKVR_zrPsXy3oinPhAO0Fh-kE56PucqxxNB59syk8eMr7mRDl3Hkjrq6syTFvH-ZPzXpQzYR7Ci2bCeBjEfU3tj3_s_XzHUzhHnGd5qLQdE-XFeo-KGIXXOcZ5Tk3-NJyMnD9QXJpVlqNIdshzoDUDjJzNOxWNYaFvkdzJR2r0tccX-EeYXxYknSDbre7izjILS1mu8a6UJlTExk74J4XQNvdP5YJKFIv0CstHZrTR3P88M0r97nY18N6sY1omCsYkJMb0XNNyiZIKhH_nA0Ao2iX98t0JmfKS2PEzvO1abZgxot7P-LKZplaoVEgZisJX6lIu8DxP5cqBvTP_PlZXhlF8UjkJym93lDYBlJ557PEheMozDV_5MnyWv3fGjtWWrH7_o6H3pnXfSjgJvyaOWK0eH1sRf6FgXgb4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69a0fec006.mp4?token=Ab8Vyxf4YUWDTlBFPbiq52Iw800YFQPXsCDsw2mIHGn_xFWT_YjXbjPmOoD0HNfD5ks6P7U-37BlKFwRv9PyZMW0bu4ShEvL8dmQWyMJySK1_78eqb6VaQRfggJJ3Vx-vha6wCIXIep8SgX2SvrG4D6sj1zpYn9zxp3su8S0ITUI2sP5I8ufoN5xljyJE7oDiGuBQWZk229rNYxi3TfKPxZ-pJs1WpFyG2FMbSQTL4nO2GwsxjLA6EKluuv09jj3QTHzFqKVR_zrPsXy3oinPhAO0Fh-kE56PucqxxNB59syk8eMr7mRDl3Hkjrq6syTFvH-ZPzXpQzYR7Ci2bCeBjEfU3tj3_s_XzHUzhHnGd5qLQdE-XFeo-KGIXXOcZ5Tk3-NJyMnD9QXJpVlqNIdshzoDUDjJzNOxWNYaFvkdzJR2r0tccX-EeYXxYknSDbre7izjILS1mu8a6UJlTExk74J4XQNvdP5YJKFIv0CstHZrTR3P88M0r97nY18N6sY1omCsYkJMb0XNNyiZIKhH_nA0Ao2iX98t0JmfKS2PEzvO1abZgxot7P-LKZplaoVEgZisJX6lIu8DxP5cqBvTP_PlZXhlF8UjkJym93lDYBlJ557PEheMozDV_5MnyWv3fGjtWWrH7_o6H3pnXfSjgJvyaOWK0eH1sRf6FgXgb4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرکت زائران اربعین از جنوب عراق استان ذی‌قار شهر ناصریه به‌سمت کربلا
@Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/452067" target="_blank">📅 08:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452066">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5783ddb53.mp4?token=nudY5Z_02z_EZMcuDIzWrpH7FkIbpktT0lw6UGHjBjKOlZbaSGHlCPBjmaPNo4M2SQz-yfMyLUGYNiHMzrRapJEcKGTEPXOibtxuZy1w_7dSVgC5qtpSdnUxeirgRQRGzDthECSV81AOzsAzHfX2hYEERl_k9ByjmWQigHbCyMNMY1CMfh9KL0pSgoPOl0YG07P-q8Ds7mC_NT2aUKoskYORcfaXbdworUIiApMhV5FPvw311DQUxYD1Klpcj6WiBWAJ7JucQ8BuvPgh_Ft_gPqK_cm84-lP6k6MB_GVCRyxV8xwcFoTKmGet8AsuKe95Hv1xh0jrkzA4_LqYCl22A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5783ddb53.mp4?token=nudY5Z_02z_EZMcuDIzWrpH7FkIbpktT0lw6UGHjBjKOlZbaSGHlCPBjmaPNo4M2SQz-yfMyLUGYNiHMzrRapJEcKGTEPXOibtxuZy1w_7dSVgC5qtpSdnUxeirgRQRGzDthECSV81AOzsAzHfX2hYEERl_k9ByjmWQigHbCyMNMY1CMfh9KL0pSgoPOl0YG07P-q8Ds7mC_NT2aUKoskYORcfaXbdworUIiApMhV5FPvw311DQUxYD1Klpcj6WiBWAJ7JucQ8BuvPgh_Ft_gPqK_cm84-lP6k6MB_GVCRyxV8xwcFoTKmGet8AsuKe95Hv1xh0jrkzA4_LqYCl22A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سه پایگاه آمریکا در کویت هدف مجدد حملات پهپادی ارتش قرار گرفت
🔹
روابط‌عمومی ارتش: در پاسخ به ادامۀ گستاخی‌ها و تجاوزات دشمن خبیث به کشورمان، ارتش ایران  در مرحلۀ بیست‌وسوم عملیات صاعقه، ساعاتی قبل محل استقرار انبارهای مهمات و اقلام لجستیکی  ارتش کودک‌کش آمریکا در پایگاه الدوحه، مخازن سوخت در پایگاه علی‌السالم و انبار مهمات در اردوگاه عریفجان کویت را هدف حملات پرحجم پهپادهای انهدامی خود قرار داد.
🔹
ارتش ایران با تاکید بر عظمت و استواری ایران در مصاف با شقی‌ترین دشمن بشریت، تاکید کرد : لازمۀ حفظ این اقتدار، تقویت اتحاد و هم‌افزایی و پایبندی به شعار همۀ ایران برای ایران است.
@Farsna</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/452066" target="_blank">📅 08:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452064">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
پیام مهم سپاه به مردم کویت: آمریکاست که تمامیت ارضی و سیادت شما را هتک کرده نه ما
🔹
روابط عمومی سپاه پاسداران: مردم شریف و نجیب کویت؛ برادران رزمنده شما در سپاه پاسداران انقلاب اسلامی در تنبیه ارتش کودک کش آمریکا و دخالت های آن در تنگه هرمز، یک انبار بزرگ تجهیزات نظامی، یک سامانه پدآفندی پاتریوت و یک آشیانه پهپادهای MQ9 آمریکا در پایگاه هوایی علی السالم را مورد حمله پهپادی قرار داده و منهدم کردند.
🔹
برادران شما همچنین محل اسکان نیروهای آمریکایی، دو آشیانه بالگردها در پادگان العدیری را مورد تهاجم قرار داده و ضمن کشته و مجروح کردن تعدادی از نیروهای متجاوز، به چندین فروند بالگرد و پهپاد، خسارت سنگینی وارد آوردند.
🔹
رزمندگان همچنین در پاسخ به حملات آمریکا به دکل‌های مخابراتی در ایران، یک دکل مخابراتی را هدف قرار دادند.
🔹
گاهی گفته می‌شود ایران با حملات خود استقلال، تمامیت ارضی و سیادت کشورها را هتک کرده، درحالی که چنین قضاوتی کاملاً نادرست است. از نظر ما استقلال، تمامیت ارضی و سیادت دولت شما کاملاً محترم است.
🔹
پایگاه آمریکایی در کشورها چگونه جایی است؟، جایی که بدون کنترل مرزبانی شما آمریکایی‌ها و هر کسی که آنها بخواهند، گاهی زندانیانی از کشورهای دیگر به آنجا وارد میشوند و خارج میشوند، دژبان ارتش آمریکا انضباط آنجا را برقرار می کند نه دژبان ارتش شما، قاضی آمریکایی در مورد جنایاتی که آنجا رخ میدهد حکم می کند نه قاضی شما، قانون آمریکایی در آنجا حاکم است نه قانون شما، نه فقط نظامیان شما حتی وزیر دفاع شما بدون اجازه دژبان آمریکا حق ورود به آنجا را ندارد.
🔹
پس این آمریکاست که تمامیت ارضی و سیادت شما را هتک کرده است و نه ما. ما داریم به زمین هایی که توسط ارتش آمریکا اشغال شده حمله می کنیم. ارتشی که جز جنایت هیچ کاری بلد نیست.
🔹
در روز گذشته، مردم داغدار میناب باقی مانده قطعات اجساد فرزندان دانش آموز خودشان را که در جستجوی زیر آوارها کشف شده بود را، تشییع و به اجساد آنها در قبور ملحق کردند. آنها ۱۶۸ دانش آموز بودند که روز اول این جنگ در حمله ارتش کودک‌کش آمریکا به شهادت رسیدند و این جنایت ها ادامه دارد و بخشی از آن با استفاده از پایگاه های آمریکا در خاک کویت صورت می گیرد و این حق قانونی و شرعی و منطقی ماست که متجاوز به کشورمان و قاتل فرزندانمان را از هر جایی که حمله می‌کند هدف قرار دهیم.
@Farsna</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/452064" target="_blank">📅 08:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452063">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UthR7Xrp6hPKM2HdWS-hmG-mOCPPsiD8jtLmnwBEhmhpkBy5Gg5H5dCnQW9-3N14SZ1xZUJhnI414bKqOe644DGoYNxEZhbilyZsi2XtqPTgEIC5fojavIsIF_4vQ3g9oM5XGXpGjgUQvQ5H4KqglX_sLQboVihr40msTnBQ41x6Jp4EIlkuNUvkFqkSHsQtHgJaiMw7vyzrVUdAs58HEVEEVPw9Qa9YsoUap5V7ts0bHvM3-IpKvD1jrm1VRAXWkk5kqO3d19wy4e_1MHzeO4TxnAGZCphPyNz11KZpLLCeH8S5Ev2UZwegY6S1sSZuWU_xe8miqP7BHp8oTEBz0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت در چندقدمی ۳ رقمی شدن
🔹
به‌دنبال تنش‌ها در تنگۀ هرمز و باب‌المندب، نفت خام برنت به بالاترین سطح شش هفتۀ اخیر خود یعنی بالای ۹۶ دلار در هر بشکه رسید.
🔹
همزمان ذخایر نفت آمریکا طبق آمار هفتۀ قبل به کمتر از ۳۱۱ میلیون بشکه رسید که کمترین میزان در نیم قرن گذشته است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/452063" target="_blank">📅 07:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452062">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2NT5JyoLQY-DP1doWrAo1WC9hEI6MbGUiR5_s1xbAP55Qrb1wiOGmnDqUdGz1hXf_kexJsu_2tjcjOgfVptkcONVJYBOKnoZd8eS4xm7lzks9ITcqQ0MZVgPpBgU349F9TLINyH-hpKZ9x8Vvz_gGUtVZor3n1Yh9luxc7DxVJXZ2ZgHul_OAahXIYCeSBYwOx8zLYLLf3lYoKv6PV848OC9HC5q3D2v3EXNY-GavbAqbMhOhcR7V0hFTDw-V9cGxNinX2ckCYrDlrQfz3htbmoMNaUSjrAbIsyOaWQSUIhfZ4koIVL-R00S7BWQH_gSBS2-EGFNmUAeFTDUa8wTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنایع تا دوماه قطعی برق ندارند
🔹
با دستور رئیس‌جمهور و با هدف جلوگیری از توقف تولید و حفظ اشتغال، برق صنایع در مرداد و شهریور قطع نخواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/452062" target="_blank">📅 07:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452061">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
حملۀ دشمن به شناورهای نجات دریایی در آبهای هرمزگان
🔹
اداره‌کل بنادر و دریانوردی هرمزگان: بامداد امروز دو فروند شناور جست‌وجو و نجات دریایی «ناجی ۱۵» و «ناجی ۱۶» در اقدامی خصمانه از سوی دشمن آمریکایی-صهیونیستی مورد اصابت قرار گرفته و آسیب‌های جدی دیدند.
🔹
مأموریت این شناورها صرفاً امدادی و انسان‌دوستانه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/452061" target="_blank">📅 06:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452060">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‌
🔴
یمن: ۲ نفت‌کش عربستان را هدف قرار دادیم
🔹
سخنگوی نیروهای مسلح یمن: با اجرای یک عملیات نظامی ویژه، ۲ نفتکش سعودی به نام‌های «ENCELA» و «LAYLIA» را به‌دلیل نقض دستور ممنوعیت تردد کشتی‌های عربستان، هدف قرار دادیم. @Farsna</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/452060" target="_blank">📅 06:19 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

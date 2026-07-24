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
<img src="https://cdn4.telesco.pe/file/OuJoeLGFet0P6haMFctcBuZZ-hQTIiSkKDTBN1v-zrevIbgp3pKp84j35_OhKXTKt6E_Dq7tdejY-x08LV2MVg71f074NEuvLtUJbO-tNdsmH5p-qYQSOe9P8lAwT2ZHnQZWOcyB9TX0Z573ctIR4Gos0dULA-DL5zgGi4FJw1sOGV2Hnb5UM5jaxt56CaFLANMfcDghwQRACfVyfVuXuByugXBT7LVm2k0wlzRR9gHjALXeGTYc8N4BUo5wFNDg-pgfaMz9gDuKJm487-atZzcr1V7cBCbPqPFgNvftV2WgBxy-eDiP66Ju3RVVh4VTaIioKFTmNdPrEkP_rSxEUw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 15:28:59</div>
<hr>

<div class="tg-post" id="msg-452269">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e470892728.mp4?token=fMLETwWp-jy6LWmNctPmH36wpnstDrdOKgubdpyp2g74aTUnFQCJSnuBPbdZgCP_HDotTKkc3zFPdAB81BGXDSXshj1XmF5AaLEIaqVKbCbAmZzSkfjlTeqS2qJDntQz9Pg4lUaK_ltIWSEaICI5TqCYcmX47G4hoPapGh9jpQ0mhi71bnfLtLMUHvKqNlL03U8-tKx16ZgfWtCI-z9aBP1KtKmZUdwfWKa9OjmpddtHvag76zIfvv8MBHqDvUtpcmPhedvw37LK0ru0XuRAaHI8mxQhIXMfZ9tPrLsv_rceIKcR0sCNiQTAM6wAKs3jnuL3K4CFuSiOgMrFiPOdMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e470892728.mp4?token=fMLETwWp-jy6LWmNctPmH36wpnstDrdOKgubdpyp2g74aTUnFQCJSnuBPbdZgCP_HDotTKkc3zFPdAB81BGXDSXshj1XmF5AaLEIaqVKbCbAmZzSkfjlTeqS2qJDntQz9Pg4lUaK_ltIWSEaICI5TqCYcmX47G4hoPapGh9jpQ0mhi71bnfLtLMUHvKqNlL03U8-tKx16ZgfWtCI-z9aBP1KtKmZUdwfWKa9OjmpddtHvag76zIfvv8MBHqDvUtpcmPhedvw37LK0ru0XuRAaHI8mxQhIXMfZ9tPrLsv_rceIKcR0sCNiQTAM6wAKs3jnuL3K4CFuSiOgMrFiPOdMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین وضعیت تردد زائران اربعین امام حسین(ع) در مرز خسروی
@Farsna</div>
<div class="tg-footer">👁️ 709 · <a href="https://t.me/farsna/452269" target="_blank">📅 15:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452268">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a07644f999.mp4?token=DxOcBK8jPc3zfYvJ6bmSno4Q6E7dP_TvJOlDlB-xRPsQ6JRKQ4RfrZ92Lo7BYD2BvJk51aGBR8BVNadlSAYd58Io7dVUZSnsrSZngsLUhVGluMGKC1hTX3mPc7Mjr3-K2pwfZE7mkl-31UdioU5CNzmhZIwV1kvJydbBf4N9zIhwbynsykD0uHkyFGMLsCY9gofcBSFnHrRD_Y39fZnlSzlnrAoAQnm62ntfRo41tv6Q0cI66ou2ty78OdotE4yocJWmsbQ8zHNPquv-lOVzq_UV1W1B8e5H7M2zZMUGyKLlhCAw5UMoTZmKenBWYXxlk_w1S_OaQFkjg0Vw_F4KGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a07644f999.mp4?token=DxOcBK8jPc3zfYvJ6bmSno4Q6E7dP_TvJOlDlB-xRPsQ6JRKQ4RfrZ92Lo7BYD2BvJk51aGBR8BVNadlSAYd58Io7dVUZSnsrSZngsLUhVGluMGKC1hTX3mPc7Mjr3-K2pwfZE7mkl-31UdioU5CNzmhZIwV1kvJydbBf4N9zIhwbynsykD0uHkyFGMLsCY9gofcBSFnHrRD_Y39fZnlSzlnrAoAQnm62ntfRo41tv6Q0cI66ou2ty78OdotE4yocJWmsbQ8zHNPquv-lOVzq_UV1W1B8e5H7M2zZMUGyKLlhCAw5UMoTZmKenBWYXxlk_w1S_OaQFkjg0Vw_F4KGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نیروگاهی که رویای هوای پاک دارد
🔹
درحالی‌که شهرهای صنعتی کشور زیر دود مازوت‌سوزی نیروگاه‌ها قرار دارند، شمارش معکوس برای آغاز فعالیت نخستین نیروگاه زمین‌گرمایی ایران آغاز شده است.
🔹
مجری طرح‌های نیروگاه بخار شرکت برق اعلام کرد: نیروگاه مشگین‌شهر اردبیل که…</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/farsna/452268" target="_blank">📅 15:16 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452267">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImQ9WOekVQOm_mzjDGRDmtlg2ibNTr0kWNJASehFPtQNiKGMZLKl4jlblzu-gSm7gSd4IzKnnolCOAzqT4gaOF2-GVbi2JV5h2-SYLiMyGKH4QbW7FY1qzApSllIhOY5wPwPXmhAbL6yfErvujMeFA5jbU_29W6LNnl2S62Y097JKe0yvKQ1enO_OIWwddRFvgqhRi3NsmCqTFhCTWsDecPmeCflX6xT6yF4vadr8AL0U0gJvAE33ssE2brHHi8qs61KsSXFqw-pKl_FWFDRImwK-MDmxF6R3JG2o-yWwsTpdOdQW2BqNb8ZFngat72FRrf6oycAHbtIrmK_5rH3Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیاتزا روی نیمکت ایران ماندنی شد
🎙
میلاد تقوی، رئیس فدراسیون والیبال:
🗣️
پس از پایان لیگ ملت‌ها جلسات کارشناسی با پیاتزا برگزار کرده‌ایم و این جلسات همچنان ادامه دارد. عملکرد تیم، نقاط ضعف و برنامه‌های آینده به‌صورت دقیق بررسی می‌شود.
🗣️
حدود ۵۰ روز تا این رقابت‌ها باقی مانده و تیم ملی اکنون بیش از هر چیز به آرامش نیاز دارد. با قاطعیت می‌گویم که ایران با پیاتزا در قهرمانی آسیا حاضر خواهد شد.
🗣️
باید عملکرد فصل گذشته پیاتزا را در کنار امسال ببینیم. نمی‌شود به خاطر یک دوره نوسان، سرمربی را عوض کرد. ایرادهایی وجود دارد و تذکرهای لازم هم داده شده است. پیاتزا ظرفیت شنیدن انتقادها را دارد و خودش هم معتقد است تیم در مقطعی با بحران و چالش مواجه بوده، اما باور دارد با همکاری همه مجموعه والیبال می‌توان شرایط را بهتر کرد.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/farsna/452267" target="_blank">📅 15:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452266">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99e3dc7e56.mp4?token=j8bN9cHa2zcq1vDOEGrVQp3LrEGDIU4I7ZzsNRu-ygTPJ5b1lXNjoDRAFWdu1ndOjYtachHIeT-q_iNuVNhjhu2XR6Te5bU9E-EEQWRhlSb94aa6XQOjTtUPhthahRNnvFfNMaQZivNE8xVlsnKazbciXRH0ZVHs9FMkTyw_-lG20JN30hSBNf3A-v2ZT1N1JfoEEsh7cSGZ4MXOH_xkXIqPuco4t9C0Kf4fl0_WM813Jvfd38Jm7Vqcj5CyTJci3FV7zSMMeNULBJkg-dUDsOliW2U8u98tGWYOnWakPLSOb5rQMmQildcjed8gp59KvBND9Ghyb7KOvvDjCFp8UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99e3dc7e56.mp4?token=j8bN9cHa2zcq1vDOEGrVQp3LrEGDIU4I7ZzsNRu-ygTPJ5b1lXNjoDRAFWdu1ndOjYtachHIeT-q_iNuVNhjhu2XR6Te5bU9E-EEQWRhlSb94aa6XQOjTtUPhthahRNnvFfNMaQZivNE8xVlsnKazbciXRH0ZVHs9FMkTyw_-lG20JN30hSBNf3A-v2ZT1N1JfoEEsh7cSGZ4MXOH_xkXIqPuco4t9C0Kf4fl0_WM813Jvfd38Jm7Vqcj5CyTJci3FV7zSMMeNULBJkg-dUDsOliW2U8u98tGWYOnWakPLSOb5rQMmQildcjed8gp59KvBND9Ghyb7KOvvDjCFp8UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سعدالله زارعی، کارشناس مسائل منطقه: ایران با حمله به مراکز تمرکز و دپوی دشمن، از یک برگ جدید نظامی رونمایی کرد.
@Farsna</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/farsna/452266" target="_blank">📅 15:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452265">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3497f04ac9.mp4?token=XeCw7wKZLMTKitHcXGP8iF9CR-D7NbB2My_fLCXO8ZB3cDKFMNhvlmpE76id1_GNKQLACwdqkeTpV903HPw3HMpFvp15bXTTATwMnvssB6-0YzISK3t8cQzcJYcvCq2mrYWtnkoQYqJSIyqbapq8nEwxfEX9NzuaZJfN_6PYlYjOV2aRHp7yi-t4bYLYyer0LKdAzYTWis3mZbxRgaRawIShcQZ4L-kppIZBzGcSAl3VaAxnddj-fUWKIqwWClEAA8gwkob8jraFrVvqGItT3gC1QBg_L8lgxgBlQNTBnYvofxouQExLj6LVzObOUWmSjO3R6bp9lztICsmk4zXI0i7gDP2HVrbpwd1HoeOcpiSK4BvA4N93Slww1E3Gz2m2ny0pk1RZ25wJH45RYtOxJezxpY8HMFVnKz8u7-zW3v0HMSn1XGvaajTzUsIQXJQ5OZhbWNvn156W8uXta4nLzCMmH_QiZDIuRos3qJ2ZQm4wRG7PezjegEWbYHFff2hwZYz9Jd3eT4yjfAWs6Fy6VCwM_iINmHjul9pioVf1Qtjg-JVYHoVZT15JyArmcMdYMlbkKeIA-IUtLZWEMWkQbGoVTx6xKmDQz5LIOZ16EbsG0DiJXt65EMnBSB-aSMNT6dAvwHnnIJvrH1AwYROYxSy0u4vLxo57Z6-JnvN7fpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3497f04ac9.mp4?token=XeCw7wKZLMTKitHcXGP8iF9CR-D7NbB2My_fLCXO8ZB3cDKFMNhvlmpE76id1_GNKQLACwdqkeTpV903HPw3HMpFvp15bXTTATwMnvssB6-0YzISK3t8cQzcJYcvCq2mrYWtnkoQYqJSIyqbapq8nEwxfEX9NzuaZJfN_6PYlYjOV2aRHp7yi-t4bYLYyer0LKdAzYTWis3mZbxRgaRawIShcQZ4L-kppIZBzGcSAl3VaAxnddj-fUWKIqwWClEAA8gwkob8jraFrVvqGItT3gC1QBg_L8lgxgBlQNTBnYvofxouQExLj6LVzObOUWmSjO3R6bp9lztICsmk4zXI0i7gDP2HVrbpwd1HoeOcpiSK4BvA4N93Slww1E3Gz2m2ny0pk1RZ25wJH45RYtOxJezxpY8HMFVnKz8u7-zW3v0HMSn1XGvaajTzUsIQXJQ5OZhbWNvn156W8uXta4nLzCMmH_QiZDIuRos3qJ2ZQm4wRG7PezjegEWbYHFff2hwZYz9Jd3eT4yjfAWs6Fy6VCwM_iINmHjul9pioVf1Qtjg-JVYHoVZT15JyArmcMdYMlbkKeIA-IUtLZWEMWkQbGoVTx6xKmDQz5LIOZ16EbsG0DiJXt65EMnBSB-aSMNT6dAvwHnnIJvrH1AwYROYxSy0u4vLxo57Z6-JnvN7fpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر خارجهٔ دولت پیشین آمریکا: ترامپ نمی‌تواند از گرداب ایران خارج شود
🔹
بلینکن: به‌نظرم ترامپ می‌خواهد از گوشه‌ رینگ که در آن گرفتار شده، خارج شود. او به‌دنبال یک راه فرار است اما نمی‌تواند آن را پیدا کند. برخی آن را تلهٔ تشدید تنش نامیده‌اند.
🔹
او نمی‌تواند این گزاره را بپذیرد که خودش یک واقعیت کاملاً جدید ایجاد کرده که قبل از این جنگ وجود نداشت، و آن [کنترل ایران بر] تنگهٔ هرمز است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/farsna/452265" target="_blank">📅 14:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452264">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgcHcBJs-icaNbB5AifxWTyx36ULV1mAIjzRpPLJbHjW432hDuZcsivwIvTSZQK6iRkvjbQoNBTT67v1dysDcxPT3vLoDsyg-EMsdGVAEkd0Q8kv4b8pKO566sj79revagh7oURKnLUP4Uj5PEkVxGD1_sGhJX3130TPAqgvlQURCQCb8gNMSolGC-zzND6k_f1BFvsNbZ7-jd9vqMhAZlz2kp4648a6cw4Jznx4VDObSE-SYuaHMitpXNF7D0FLIZ-6z14bzhHs8mYoGrLo05v8azQ5b14n9wwg7TZ5WgA4g8xJ2rqnU6AXUx4kXOuyofB2nD4nGPKDxPmWPsqIIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامهٔ آزمون‌های نهایی پایهٔ یازدهم ۴ استان جنوبی اعلام شد
🔹
براساس ابلاغیهٔ رسمی وزارت آموزش‌وپرورش، امتحانات نهایی برگزارنشدهٔ پایهٔ یازدهم در استان‌های خوزستان، بوشهر، هرمزگان و سیستان‌وبلوچستان در روزهای ۷ مرداد، ۱۱ مرداد و ۱۴ مرداد برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/farsna/452264" target="_blank">📅 14:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452263">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اجرای محدودیت تردد در جاده‌های منتهی به مرز مهران از ۱۱ مرداد
🔹
پلیس‌راه ایلام: به‌منظور مدیریت ترافیک زائران اربعین، تردد تمامی خودروهای سنگین شامل تریلر، کامیون و کامیونت در جادهٔ ایلام–مهران و بالعکس از ساعت ۷ صبح ۱۱ مرداد تا ۷ صبح ۱۶ مرداد ممنوع خواهد بود.
🔹
خودروهای حامل سوخت، مواد فاسدشدنی، امدادی و پشتیبانی مواکب از این محدودیت مستثنی هستند.
🔹
درصورت لزوم، محدودیت‌های دیگری نیز متناسب با شرایط ترافیکی برای سایر وسایل نقلیه اعمال خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/farsna/452263" target="_blank">📅 14:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452262">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6aa13ec7b3.mp4?token=Bctd3UE285VoXETsIj--SIpPagNoulHJ7-KHbN9Jmhcb6YPNtL9ORtNjqUau6lmCUkElzk6z_iqALFKzYWiwvP3j2I3GPY76Ta7YiwR0vf0D03N51qlvzE2hNluAwnBTKsTv748fJsFfH0EXTNFbhbmkckF9621wYsT0PGS3o33J8mRRJbXbEa_L6h4CMyUfW8DB5Bc6fKqlJQCRM_6nCeu595pBX6073Jv1BHQia6GHHccz55QjOrXD1K8WL0LGrYtg8h_zTZ1dnSB4wODLwMgJacNj601v-zSnWXipFgh64Fq2sgCg9Ck51G-sqCcaIFK-bxpP2xOfa5jUR8dChA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6aa13ec7b3.mp4?token=Bctd3UE285VoXETsIj--SIpPagNoulHJ7-KHbN9Jmhcb6YPNtL9ORtNjqUau6lmCUkElzk6z_iqALFKzYWiwvP3j2I3GPY76Ta7YiwR0vf0D03N51qlvzE2hNluAwnBTKsTv748fJsFfH0EXTNFbhbmkckF9621wYsT0PGS3o33J8mRRJbXbEa_L6h4CMyUfW8DB5Bc6fKqlJQCRM_6nCeu595pBX6073Jv1BHQia6GHHccz55QjOrXD1K8WL0LGrYtg8h_zTZ1dnSB4wODLwMgJacNj601v-zSnWXipFgh64Fq2sgCg9Ck51G-sqCcaIFK-bxpP2xOfa5jUR8dChA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا تنب بزرگ، تنب کوچک و جزیرهٔ بوموسی جزایر راهبردی ایران هستند؟
@Farsna</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/farsna/452262" target="_blank">📅 14:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452261">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9f2ioG9KuYVdpBg6JAx5n_IphJY9jnuqRV2sUqZn0FNZ5kAay-DLe7kPvSu6r1OCmL7E-YzBykBLcHji70yIlHcrovYTh3tOrtIdi6wqdyaM9KnO6Sjv7qcnw3py9pSsPaVuEliCQpbwD8HdUhDmIi06R5TAzkNytmPxF--8v3rfn5dZJLaGUBf-zG_YBAqEBsi0lfZlMCek6JJAOvYWlaNh7y6zriscg9qb2bkaFaIcLNiwxOQ6wTGGMLD8Yhx2tz_9A8VPkCuJbdveYKfPt6yAfE2cLJ1I6tKz3cQAbswTd9gTb-4os3JrnjfHfSWtIWNKOsJSVFZZd85FfaJng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تردد بیش از ۸٠ هزار نفر از مرز مهران
🔹
راهداری ایلام: تردد ۸۰ هزار و ۹۶۷ نفر از مرز بین‌المللی مهران در ۲۴ ساعت گذشته ثبت شده است؛ بیش‌از ۷۴ هزار نفر از این تعداد از کشور خارج شده‌اند.
عکس: اصغر خمسه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/452261" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452260">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
۳ سولهٔ نگهداری مهمات و تجهیزات در پایگاه آمریکایی العدیری و برج مراقبت ناوگان پنجم دریایی آمریکا به آتش کشیده شد
🔹
سپاه: در موج ۲۷ عملیات نصر ۲ با رمز مبارک "یا اباصالح المهدی ادرکنی"، رزمندگان با هدف قرار دادن ۳ سوله نگهداری مهمات و تجهیزات در پایگاه آمریکایی واقع در العدیری کویت، این سوله‌ها را به آتش کشیده و از بین بردند.
🔹
رزمندگان همچنین به‌طور همزمان برج مراقبت ناوگان پنجم دریایی آمریکا را در بحرین هدف قرار داده و خسارات زیادی به آن وارد نمودند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/452260" target="_blank">📅 13:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452259">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8bfdf3f35.mp4?token=OBTgnrIiocg8NLv-umQUVM00LFp07YjP7jiwBx2ZL9UOD8aVbnwNJ2rkgddXKT4yFMu3ITBXaJTsHus6oYo62cTLhN2bZEVKh-1ibx7ev4zHUgIhNCbqR7kyBXtqGlbBNGgtZTqciI6Bva4OjnCmO60RCF0UjK254Ar3JaX6bg6SC-2STue5m7duuIzpfNra771GLJb8PDDdPjBcRXO_hj4T2DQv8UZbfOoffxKrjr7pNuxw-y8BoOy81uUR9SQmAxrPG8EtYGII6wgNUHYyDxxbvq1s29nNqbzpHqBSMeluTt9kNVbK3xbCke8Lo4X13f5uKn2CPQid2hK2SXVVuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8bfdf3f35.mp4?token=OBTgnrIiocg8NLv-umQUVM00LFp07YjP7jiwBx2ZL9UOD8aVbnwNJ2rkgddXKT4yFMu3ITBXaJTsHus6oYo62cTLhN2bZEVKh-1ibx7ev4zHUgIhNCbqR7kyBXtqGlbBNGgtZTqciI6Bva4OjnCmO60RCF0UjK254Ar3JaX6bg6SC-2STue5m7duuIzpfNra771GLJb8PDDdPjBcRXO_hj4T2DQv8UZbfOoffxKrjr7pNuxw-y8BoOy81uUR9SQmAxrPG8EtYGII6wgNUHYyDxxbvq1s29nNqbzpHqBSMeluTt9kNVbK3xbCke8Lo4X13f5uKn2CPQid2hK2SXVVuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
رسانه‌های اسرائیلی: یک اسرائیلی در محل تیراندازی نزدیک حفات جلعاد کشته شد.  @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/452259" target="_blank">📅 13:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452258">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpPzCzUF14z5sdInG9tcAUACs4ROoxX_n_I8uioxw_qeLwh9kFMBI0dXvWghGu5Si9gnsX_n15e8NAisjlmrNXVpeKx0qEnXcZHLALU4MxB4n1aYx4Xr1EMr48LQ1rUWTKXRnuqZIASyCBY3lhVMbQZJp5qYJq4WNADjeiqP9kddWS9nVMt4A92z6LG395xV1FYuGpkEFPmIS4i3QhTDL8mjvoM8Hc59AH8BLse4nEar2R2uWRwf-cowTHd4NWeiggsxYOz01kFzYR-YA_B7IuO_9QjNPuhiPY1KTdvUajVnXLx4hgT2GiCRGivzhyaqpwn7maAjmFNBWHn_lMiQJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دیدار عراقچی و لاوروف در قرقیزستان
🔹
وزرای خارجهٔ ایران و روسیه در حاشیهٔ نشست شورای وزیران سازمان همکاری شانگهای در قرقیزستان با یکدیگر دیدار کردند. @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/452258" target="_blank">📅 13:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452257">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCVst17KivDuvUgQZcucdgHmHXqR6mtypvxxRQ__HmejpDiw0dHFvqedVKn6LW7ZdiikeQz0b4IEaFIUiy4JE1ZfOq9wTXRhReiFlYap2suEUGTdTnL7VtNRrFirc3qXKECBUbWYGiOY5IMy5SaZA-MBpNlBq4QItLVZAnKj1b6o3GK8miUyAzXnsgTy1TwzDCa7DHqTWyG0XpvEwzJ7114PTjR2xVE_mp4ra5oPUIGE9A44MLUxm3J3aT2UGHCnaZPQ7YfkP85FN9nAlfyNlIszrvsOfVXaHX73pe-LKwjmlIe5dOeiLmgXHaeT57SbqkY5B8xXd1fFW_YvgjVvbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خاتمی: تنها راه دفاع شرافتمندانه است، نه تسلیم بی‌شرفانه
🔹
خطیب نماز جمعهٔ تهران: برخی از نهادهای حقوقی و بین‌المللی صحت سلب دارند؛ یعنی نه‌تنها از حقوق ملت‌ها دفاع نمی‌کنند، بلکه در برابر جنایات بزرگ سکوت کرده‌اند.
🔹
جنایتکاران در غزه دست به نسل‌کشی می‌زنند و مدعیان حقوق بشر سکوت کرده‌اند؛ در چنین شرایطی دیگر این نام را نباید بر خود بگذارند.
🔹
این چهارمین بار است که آمریکا در وسط مذاکره دست به حمله می‌زند. در چنین شرایطی راهی جز دفاع شرافتمندانه باقی نمانده است، نه تسلیم بی‌شرفانه.
🔹
خداوند در قرآن می‌فرماید «فَمَنِ اعْتَدَىٰ عَلَیْکُمْ فَاعْتَدُوا عَلَیْهِ بِمِثْلِ مَا اعْتَدَىٰ عَلَیْکُمْ» و همچنین می‌فرماید اگر مجازات کردید، به همان اندازه‌ای باشد که بر شما ستم شده است.
🔹
از زبان این مردم به رزمندگان عزیز می‌گویم دست شما درد نکند؛ پایگاه‌های دشمن آمریکایی را محکم بکوبید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/452257" target="_blank">📅 13:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452256">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
سپاه: با فوریت تا شعاع ۵۰۰ متر از اماکن محل‌های اقامت پوششی و مخفی نظامیان آمریکایی فاصله بگیرید
🔹
روابط عمومی سپاه پاسداران: مردم شریف کشورهای محل استقرار پایگاه‌های آمریکایی در منطقه؛ رژیم کودک‌کش آمریکا پنج ماه پیش بدون دلیل منطقی و توجیه قانونی با به شهادت رساندن برجسته‌ترین دانشمند دینی و رهبر سیاسی جهان و همزمان به شهادت رساندن ۱۶۸ کودک دانش آموز معصوم، جنگ تجاوزکارانه‌ای را علیه ما آغاز کرد.
🔹
ایران بعد از ۴۰ روز جنگ پیروزمندانه در حالی که می‌توانست جنگ را با قدرت ادامه دهد، برای بازگشت آرامش به منطقه حاضر شد با نهایت گذشت با چنین جنایتکارانی پشت میز مذاکره بنشیند و تفاهم‌نامه پایان جنگ را امضا کند.
🔹
اما ذات جنایتکار و درنده خویی ایالات متحده موجب شد از همان روزهای اول تفاهم، آمریکا درگیری‌ها را از سر گیرد و تعهدات را زیر پا بگذارد و نهایتاً از ۲۱ تیر ماه رسماً تفاهم را ملغی و جنگ را از سر گیرد.
🔹
با گذشت ۱۳ روز از ازسرگیری جنگ، آثار شکست مجدد آمریکا ظاهر شد و دشمن فهمید با عملیات جنگی نمی‌تواند بر نیروی مسلح ما غلبه کند. اما برای خروج از بن‌بست به جای عقب نشینی به ارتکاب جنایت جنگی متوسل شد و پل‌ها، اسکله‌های صیادی، قایق‌ها و لنج‌های مردم، خودروهای عبوری و راه آهن را هدف قرارداد و غیرنظامیان را به شهادت رساند تا جایی که در روز گذشته با کشته و مجروح کردن زائران اربعین حسینی در مرز عراق جنایت را به اوج رساند و ماهیت یزیدی خود را آشکارتر کرد.
🔹
از آنجا که در صورت استمرار چنین جنایاتی دستور کار ما قصاص جنایتکاران خواهد بود، بسیاری از افسران و نظامیان ارتش متجاوز آمریکا از ترس آتش رزمندگان اسلام پایگاه‌های خود را ترک کرده و ساختمان‌هایی در شهرها را محل هدایت جنایات خود قرار دادند، به عموم مردم کشورهایی که محل استقرار نظامیان آمریکایی هستند، هشدار می‌دهیم با فوریت تا شعاع ۵۰۰ متر از اماکن محل‌های اقامت پوششی و مخفی نظامیان آمریکایی فاصله بگیرند تا در امان باشند.
🔹
مردم همچنین می‌توانند محل‌های جدید جابجایی نظامیان اشغالگر آمریکایی را به حساب رسمی روابط عمومی سپاه پاسداران انقلاب اسلامی در تلگرام به نشانی
@sepahnewsiradmin
و یا بخش "تماس با ما" در پایگاه اطلاع رسانی
sepahnews.ir
اطلاع دهند.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/452256" target="_blank">📅 13:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452255">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
الجزیره: صدای انفجارهایی در اطراف فرودگاه اربیل و مناطق غربی شهر در اقلیم کردستان عراق شنیده شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/452255" target="_blank">📅 12:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452253">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PQbMv4BHBjdjftgy8077u-fcKGaz5nCRpnITTCSdOfur0_CdvySn3P0Ctc0Kmf7HzQqgpi4nRo55dDfUSobO8WWWNP7UqKW69fHiSrL1ZRRdzeeLfwd48_FSXvO2tjkl5_O4toA81lWWGWE_t1ksqDuocsj44n5smtmeh9JD51zOmTRjrQheF7SSD4eNl3zT-T8U0_s2BqTQ6F0fsoucQ_yP5YNJuwoByKsz1DxDrwl3nqlnyPkrnR9gfz6btu2yUqE8G6zUHWqa2YUZPK4aTzt_OOHTLFS8Pt728aCaN8IZIauaU_-et7yafMNCneitH6ZW4-TfYiF5yoOtn8uk7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ni3Ohn-Isbyf3RX0L2kS1oDaf79_d2FTtpuyib_d69P-O9iiVyK2EqXF10F8O_35ZSZGo-r5vFRQIx0aRhsFyBBINqknJz84hyQZFJqlUpIwRQ8Xzd2YkGkhRCScvpf9H4psE_w_l_SRGZTNRTTrd19Vj-Qo7miuNhqOY8HXHGDJlQpspsOZmKuFPKcyTjYBO8jQQJ8EEds8xt9NOsumF3vzgBkP_8UjNLujfZqq11rT5XfugjOXY51LnSsizqjJcKdFPqkI0QmC8XATrm8lmkd3b4yPbY5e8b_b2qm4x7oTJ2RBjz4KFcOA-MkvgiNPNosaR-qVzAXwDglyQUluwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">۲۵ سند در قالب ۹ تصمیم در پایان نشست وزیران خارجهٔ سازمان همکاری شانگهای به امضا رسید.   @Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/452253" target="_blank">📅 12:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452252">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRONw4fylMpQnTCx34Rsv6OcpP2EG74ezkn0-sdAk0edf95T0OIdSPc3O62xsfkjGoHnhrUCAno0tz_oYvHV3lwtghkSYEZbkdZ-Gpd7IxP40vYU7EDTKHyG3lFJRwLPRYSjgj9AG7LZPz5Xrb_TSIi2K5pzbDfT2L_W0oR54iYQxXRd2MK1SKjqvZPtAgNj1Q8XymWBcp2_eUsDStgjbfaCJPwYiEHDN_riRmglulaq78X2JHWKtcZgaVPOPQ6DWgM-Gi0uwioWyyUhk205bXHDRCu8eC5DggVqYeUFT7aZhOz4KUfZrTguJlmFIYiyc5X1WWyd82YHQrFzb09HLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درآمد دلاری نفت ایران ۱.۵ برابر شد
🔹
اطلاعات رسیده به فارس از وزارت نفت مشخص کرد، درآمد نفتی ایران از فروردین تا تیرماه امسال نسبت به مدت مشابه سال قبل ۱.۵ برابر شد؛ این درآمد علی‌رغم شرایط جنگی حاکم بر کشور به دست آمده است.
🔹
در ۴ماههٔ ابتدای امسال درآمد نفتی ۷.۵ میلیارددلاری وصول شد؛ رقمی که در ۴ ماههٔ ابتدای پارسال کمتر از ۵ میلیارد دلار بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/452252" target="_blank">📅 12:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452251">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ejsjuu9uW2r5A7z2r8is-rHMVct2GvPTue6NlQ7Mz4tJJvUZr14q6fR7sVTmgi_Y9G84aoyr8rRx4Ex2bKLV3_RejAxqgGmU3YtbCN0yTje0flmzJV0zVgQlg4E6y5X7HQ859y7Ulgbz1nfPgkwFKcwannwATU82J1ptDyNW8tLqF2paRzTbaWAQ17JbMBNziVImkUf3_HuGyG_w35kUSW3gbmRhJZRe5Mffl2mJ-3md7-N-2webZCR9X7fgjTN79Ws8gS8_S2hHuDDU4ZYYGF8WxotKC4gWzZRtLldRn8wczmdPPYL9qD-JrJdcN4Uwp0MElN9UcGlzRva3t_pJmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ تجاری جدید ترامپ با ۶۰ کشور جهان
🔹
رئیس‌جمهور آمریکا درحال نهایی‌کردن تعرفه‌های جدید ۱۰ تا ۱۲.۵ درصدی علیه حدود ۶۰ کشور است؛ اقدامی که با استناد به موضوع «کار اجباری» انجام می‌شود و می‌تواند شرکای بزرگی مانند اتحادیهٔ اروپا را نیز هدف قرار دهد.
🔹
این تعرفه‌ها…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/452251" target="_blank">📅 12:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452249">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d59a059df.mp4?token=Xlj-n82f0m751R_6zeIpjB3JglBZFzb1AmzxN-_n3i53u8Dwrx6gFMYDTIbK4t9W9wzER790cKOtntUmw3sEx65KUZtLHJz68KeOY1xNi-lni7gmAjJxT779BWNSQZsaM1vTNNLOqnVOV46H_4d8mqbrvWB_O-07-fsk_fs_oycp4FIVoojbPu2ZRaCFiDMmUwEEWrnQGYT_c11XgAOXTFmNWpn9MayzDdZRq_EBTiGai6QKmnzNMFn1fQBCK7FTdqOySGE7sH3HZsab-U76mfowDXRmwPZ1mNdKzz6UNEdaEE_S7xzts32TWeDJXpB5dkcL0rhsQ5KiEDigClYCZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d59a059df.mp4?token=Xlj-n82f0m751R_6zeIpjB3JglBZFzb1AmzxN-_n3i53u8Dwrx6gFMYDTIbK4t9W9wzER790cKOtntUmw3sEx65KUZtLHJz68KeOY1xNi-lni7gmAjJxT779BWNSQZsaM1vTNNLOqnVOV46H_4d8mqbrvWB_O-07-fsk_fs_oycp4FIVoojbPu2ZRaCFiDMmUwEEWrnQGYT_c11XgAOXTFmNWpn9MayzDdZRq_EBTiGai6QKmnzNMFn1fQBCK7FTdqOySGE7sH3HZsab-U76mfowDXRmwPZ1mNdKzz6UNEdaEE_S7xzts32TWeDJXpB5dkcL0rhsQ5KiEDigClYCZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعلام وضعیت اضطراری ملی در اسپانیا درپی گسترش آتش‌سوزی‌ها
🔹
دولت اسپانیا ساعاتی پیش درپی گسترش چندین آتش‌سوزی گسترده در نزدیکی پایتخت این کشور، مادرید، و استان همجوار آویلا، وضعیت اضطراری ملی اعلام کرد.
🔹
به‌گزارش خبرگزاری رویترز، این آتش‌سوزی‌ها تاکنون بیش از ۱۰ هزار نفر را ناچار به ترک خانه‌هایشان کرده و آتش‌نشانان همچنان برای مهار شعله‌ها تلاش می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/452249" target="_blank">📅 12:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452246">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
ساختمان باقی‌مانده از شرکت آمازون منهدم شد
🔹
سپاه: ملت قهرمان و به پاخاسته ایران اسلامی؛ حماسه قیام بی‌نظیر شما دنیا را بیدار کرده است و دعای خیر شما، پیروزی‌های درخشان رزمندگان اسلام را تضمین کرده است.
🔹
رزمندگان اسلام در موج ۲۷ عملیات نصر۲، در تکمیل عملیات قبلی خود علیه مرکز داده‌های اطلاعاتی شرکت آمریکایی آمازون که نقش اصلی در تکمیل اطلاعات ارتش کودک‌کش آمریکا را بر عهده دارد، ساختمان باقی مانده این مرکز را هدف قرار داده و منهدم کردند.
🔹
عملیات تنبیهی رزمندگان اسلام ادامه دارد.
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/452246" target="_blank">📅 11:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452245">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvZe-LQVNc4YTM9xjyR9i_WQIZcUtYmLDP4qn21y5EXw16Q7hVyIJ_Lvw-dWoyM_SsPnpVbI1-QGeaIl2Od1r7suruo5Dz7_bpl76UTfBiKDjYpGAcTIE6u2G-x9IDb-6Bel2-w4l_zti6SJAW6b2TssDdD8U6IUN1Ta19hEceW81opj1gB2BT0urlK9Gh1u4po0q7I-N3uDU-v9ls6c_1esrO_VB4icnAMlwZzLJPvMk4MyMapl9fZi2D_UNqkD8O8buQOS-Cy6ggl4cpSKxyFYONMNZRDjX29SeH-FNeF8YUjo9h0uGH1dbI414GLZR15xjW5WDF4S5EWZFm_qWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انهدام یک موشک کروز دشمن آمریکایی در آسمان کهنوج
🔹
سپاه کرمان: یک موشک کروز دشمن آمریکایی در آسمان کهنوج در شب گذشته توسط سامانهٔ نوین پدافند هوایی سپاه تحت مدیریت شبکهٔ یکپارچهٔ پدافند هوایی کشور منهدم گردید.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/452245" target="_blank">📅 11:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452244">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWvd4E4-LnHpGXEJjCjOXakBocLSNO8B6BdANJ1fVjOss4EhnUkgcVpq9RDeh5TyA3Oj0eEiwRMKcOOmYcYgJ7G9TIvFYLoYFM9Eeim3sadntfLmaYYdOLOdfk_xzUq1Y-jeObwD8Wd8sR-wJpzbTkDIMiooe25fW2OtYFYV9dUkCiA44slz0fGY6u7Oyo-cUKXLFhpVehw0RynyGRGPG_rUKZTgOkTmJHs3-tyQCoFjmAxAwy_dL3hpjG9uEDdxUu6fxYAnRWeiGfuX8sWNNJYas-b2KqFvqCzZPEXiWINyziUmrWVwSSwYE-pxAnMa2o6ffx9qh07BRvgfAKSnmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
رسانه‌های اسرائیلی: یک اسرائیلی در محل تیراندازی نزدیک حفات جلعاد کشته شد.  @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/452244" target="_blank">📅 11:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452243">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a85b786af9.mp4?token=iKwkU0j5Wlq4kFNwyRhnSgVbKXOAhJPYvlzkA69TRp6PNi3c96FsnlHCCgEhuB0Lw1lBpWGbt8CUHnpx-lEMiddSMGRQQcC3MywWqLxt9yVYesAACA3hsGGd10r2-XKpfMB_INUj1kHy70-s7bpgaWgJKfx0GbooaSEGmW4Wi81G4LYUDH0bxTadkPg7u1BOc7g8qoG751OM5XN_O7aB_8FDjrhduEzfqQxJXR0ctf6aV38Han9w-Z53xYpuEMvxNP_MGToStEyrcdXPvsKPoQxMhYe42Gu51o7o0joGOuUE0wfiVjiStlZln7NJ9XzxbMsZHveqE1NKTZQKhRym4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a85b786af9.mp4?token=iKwkU0j5Wlq4kFNwyRhnSgVbKXOAhJPYvlzkA69TRp6PNi3c96FsnlHCCgEhuB0Lw1lBpWGbt8CUHnpx-lEMiddSMGRQQcC3MywWqLxt9yVYesAACA3hsGGd10r2-XKpfMB_INUj1kHy70-s7bpgaWgJKfx0GbooaSEGmW4Wi81G4LYUDH0bxTadkPg7u1BOc7g8qoG751OM5XN_O7aB_8FDjrhduEzfqQxJXR0ctf6aV38Han9w-Z53xYpuEMvxNP_MGToStEyrcdXPvsKPoQxMhYe42Gu51o7o0joGOuUE0wfiVjiStlZln7NJ9XzxbMsZHveqE1NKTZQKhRym4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
یک زاغه مهمات بسیار بزرگ و سوله‌های محل اسکان نفرات در پایگاه علی‌السالم، به‌طور کامل متلاشی شدند
🔹
سپاه: ملت قهرمان بصیر و به پاخاسته ایران اسلامی؛ استمرار حضور شگفت انگیز شما مردم تاریخ ساز، عالم را به خیزش در مقابل ظالمان و زورگویان فرا می‌خواند و سوخت…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/452243" target="_blank">📅 11:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452242">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
یک زاغه مهمات بسیار بزرگ و سوله‌های محل اسکان نفرات در پایگاه علی‌السالم، به‌طور
کامل متلاشی شدند
🔹
سپاه: ملت قهرمان بصیر و به پاخاسته ایران اسلامی؛ استمرار حضور شگفت انگیز شما مردم تاریخ ساز، عالم را به خیزش در مقابل ظالمان و زورگویان فرا می‌خواند و سوخت موشک و پهپادهای رزمندگان برای سرکوب استکبار است.
🔹
رزمندگان اسلام در ادامه عملیات تنبیهی علیه ارتش کودک‌کش آمریکا و در پاسخ به جنایات شیطان بزرگ، ساعتی پیش در موج ۲۷ عملیات نصر ۲ با رمز مبارک "یا اباصالح المهدی ادرکنی" با پرتاب پهپادهای انهدامی فوق سنگین و پیشرفته، یک زاغه مهمات بسیار بزرگ را در پایگاه آمریکایی علی السالم هدف قرار داده و آن را با انفجارهای پی در پی به طور کامل متلاشی کردند.
🔹
همزمان سوله‌های محل اسکان نفرات این پایگاه مورد حمله قرار گرفت که ۶ سوله بزرگ به طور کامل نابود شد و به سه سوله دیگر خسارات اساسی وارد آمد و تعداد زیادی از عناصر دشمن کشته و زخمی شدند.
🔹
دشمن آمریکایی که در جنگ تحمیلی ۵ ماهه اخیر صدها کشته و بسیار بیشتر از این مجروح داده است و تخلیه روزانه انبوه زخمی‌های آن با هواپیمای آمبولانسی به بیمارستان آمریکایی در آلمان سند روشنی بر این تلفات بالا است، با دروغگویی به مردم خود مدعی است کمتر از ۲۰ کشته داده است.
🔹
این بر عهده رسانه‌های آمریکایی است که در مورد واقعیت‌های این جنگ و تلفات بالای ارتش آمریکا و خسارات سنگین آن و ارقام هزینه‌ها که همه از دید مردم پنهان نگاه داشته می‌شود، تحقیق کنند و آمار واقعی و شیوه‌های سانسور حکمرانان دروغگو را افشا کنند.
🔹
عملیات تنبیهی علیه متجاوزان ادامه دارد.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/452242" target="_blank">📅 11:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452241">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
وزارت کشور بحرین از به‌صدادرآمدن آژیرهای هشدار در این کشور خبر داد.  @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/452241" target="_blank">📅 11:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452240">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXMi3oLun7ing2u0ZvWfyK_VGgZUC4NKHnlXH0jGTTCWaFsz0Vk66M2SX8nCAbQuLLgXMQZXdCgX0ZoqHiw52ycl3upUqTZqVoE4PkojjiG_jD5AqKOwQ_DiNPTamntUvIqmCDA79On9lKTV7aSojeagDsKFFRm9gnWp-OfSecJ3v1lsMi1J5Qkg8qI7iZhFGcNbHzOQrs_SKIiJYPkpJdnK62cBGseNqQJ3rBtHVoejf3uDGwNOkkX8l7JXAW478K8lXhclx5-137PdQTdacgjHfw5ONAPeO7Y6pcnzPI0lbnavyraayLtYkQCLMD6gWpKicz2zkanKuW1v8X5p_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
نشان تعهد به مسئولیت اجتماعی سازمانی به ایرانسل اعطا شد
🔸
این نشان در اجلاس ملی جان‌فدای ایران با رویکرد تجلیل از اقدامات مسئولیت اجتماعی بنگاه‌های اقتصادی در دوران جنگ رمضان، به مهندس محمدحسین سلیمانیان، مدیرعامل ایرانسل اهدا شد.
🔸
در این اجلاس، مقامات کشوری از جمله نایب‌رئیسان کمیسیون برنامه و بودجه و اجتماعی مجلس، معاون قوه قضائیه، مشاور مجمع تشخیص مصلحت نظام و دیگر مدیران و فعالان اقتصادی حضور داشتند و بر نقش بخش خصوصی در افزایش تاب‌آوری ملی تأکید کردند.
🔸
اجلاس ملی جان‌فدای ایران با هدف تجلیل از نقش‌آفرینی شرکت‌ها در شرایط بحران، توجه به مسائل انسانی، زیرساخت‌ها و اتحاد ملی، سه‌شنبه ۳۰ تیر ۱۴۰۵ برگزار شد.
👈
جزئیات بیشتر
@irancellnews1</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/452240" target="_blank">📅 11:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452239">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUVMBUe8NVOfhaQaL6m9gabilC1v-Nf7Yxkw7j-Ic6CXuKOeLVMlza7N4rsrd6pm_EFY9_Fak3YfA281J2DGv5N0Qp09u7ec3q_iho-TtkTZ0FFCE3Wh_xcetvGKYpglPHz3_QJiQ05_mw0Xl1vU13m1aIqz3ufOB4IwsYcexPIvycSsoesRzQih7ltCyq0lyToiC8C4hodiK4dvB8Dm709jgao2HoZmwQQr8O5-1vst2b9157WBtJQQnTO04YNC6GqMO4-kI1jFEUxmFOb8JpKbyLDBEv8quSF0xxxHhWD5v0EsRyC_3nFNz-3MxUdHMXreftQNQvbSicevjEUyXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴
راهی اربعین هستی؟
🚐
دنبال وسیله نقلیه برای سفر هستی؟
👥
یا راننده‌ای و ظرفیت خالی داری؟
رحیل رانندگان و مسافران اربعین را به هم متصل می‌کند.
✅
ثبت رایگان درخواست سفر
✅
ثبت ظرفیت خالی خودرو
✅
جستجوی رانندگان و مسافران
✅
مناسب برای خودرو شخصی، ون، مینی‌بوس، اتوبوس و کاروان‌ها
📲
دانلود اپلیکیشن و عضویت در رحیل:
🌐
rahil-app.ir/download</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/farsna/452239" target="_blank">📅 11:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452238">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/452238" target="_blank">📅 11:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452237">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JshG94UmcfshT-KhQ2iQTzdbVx6Wvgxa3QY5nGCUC7yRGtf-J5NRVq2mLUQ4PBNJFs6YLbzziEgvXJr9kB6HeVJXkQmDR2p5dXUtMZpO9BUPQuc4hzpzQ-0ob7jBd1gR0URcugWZjuR7EHuxk8JYubLG_yf_BsKAQFh_egE8r6X7stOTsEwc4povDQO58D1IjKZBzBEmR8wuAb42OAZ55_Mt_m9jOzCObO5VhpGPBrIuOxEP-EiOT6bMcQpBBghy3Onqp3NgDqB7keCqOD0i4dlObeTm_QD0GrwyYMhoXN_Inji76FiWJ6jdMIb-4hlK_cLV8oG3cLFJKPdecUNQ2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه: منشا هرگونه تجاوز علیه ایران هدف مشروع خواهد بود
🔹
عراقچی در نشست شورای وزیران امور خارجهٔ سازمان همکاری شانگهای: آنچه جمهوری اسلامی ایران با آن مواجه شد، صرفاً یک تهدید علیه امنیت ملی یک کشور نبود؛ بلکه چالشی علیه اصول بنیادینی بود که نظم حقوقی…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/452237" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452236">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">شمار مجروحان حملات اخیر آمریکا به ۶۴۵ نفر رسید
🔹
سخنگوی وزارت بهداشت: تا ساعت ۶:۳۰ صبح امروز تعداد مجروحان به ۶۴۵ نفر و شهدا به ۵۵ نفر رسیده است.
🔹
خوزستان بیشترین تعداد مجروحان را به خود اختصاص داده و پس از آن استان‌های هرمزگان و سیستان‌وبلوچستان قرار دارند.
🔹
همچنین هرمزگان، سیستان‌وبلوچستان و خوزستان بیشترین تعداد جان‌باختگان را داشته‌اند.
🔹
تاکنون ۵۸۶ نفر از مجروحان پس‌از دریافت خدمات درمانی ترخیص شده‌اند؛ تعدادی از مصدومان نیز به‌صورت سرپایی درمان شدند و ۸ نفر همچنان در بیمارستان بستری هستند که برخی از آنان به انجام مراحل بعدی جراحی نیاز دارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/452236" target="_blank">📅 11:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452235">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
وزارت کشور بحرین از به‌صدادرآمدن آژیرهای هشدار در این کشور خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/452235" target="_blank">📅 11:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452234">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-E0gcyRy3dhh0G5rjaSanzwDFTB0Ba6Yw5aCDXEZWPzicXgPm3Z8WBEYxvrE3kxJCsRuQaRDFRwAGBEH6PC7AkWW5et5WatlHYDhn3RW-CMoi6aJqSzsC7fjCQI7HZsiSq92Jqyha8DKS2VfqgknxGamftKQ8l7Q-l40gtixPdqzWe-RD5zFHOTi8XmZYzP_T3bmwvuUTGot1DOq43kDwjrkaPJv3-52tB0awAtvrDLqvON6iKd52sRKWj8PtYLonZpa0NfaG1idKOvYyw9cNq9BJ3Z6h8rtImUpglTMbHSnT77Kp2ydyTD1yE1EJw17c7XrP-DixVGZvVX34yKOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
خطوط هوایی قطر پروازهای مسافری به بحرین، کویت و اربیل را تا پایان ماه ژوئیه جاری به‌حالت تعلیق درآورد.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/452234" target="_blank">📅 11:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452233">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
منابع عربی از وقوع انفجارهایی در انبارهای کنسولگری آمریکا در اربیل عراق خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/452233" target="_blank">📅 11:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452232">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/213477bb06.mp4?token=smNivpiyEQld8kCiuvjWINjUQwq6LH6Nx19LwsmKZoZwHFMzLUIy79hWVMxJPwBQB_9HfC4hoOJl9GE8XkEOynk6AmJ0iLVkw7KSvG0i0A7wjFgg2uFN6JriVP9D_ng8vh8fMJL9ZFSTd32cp3HIygvp7vzkYrTsS8DhEjR5LKLTECimBzPdwNA_UAA9SH1H8_BPT_mYcdzkO1rPH26eOLBZyeDJcSlYX4DqWbQDsJDYyjAKUpV9y-8YPRJDafvehM_Tjn4e-H9cKhVvQhHB7O6eZAlvy_zg-v8xCdEUAi_C3yeZH6pMNLXZAGp7dGjLfNCpBBUcyvOhllj0xbt9EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/213477bb06.mp4?token=smNivpiyEQld8kCiuvjWINjUQwq6LH6Nx19LwsmKZoZwHFMzLUIy79hWVMxJPwBQB_9HfC4hoOJl9GE8XkEOynk6AmJ0iLVkw7KSvG0i0A7wjFgg2uFN6JriVP9D_ng8vh8fMJL9ZFSTd32cp3HIygvp7vzkYrTsS8DhEjR5LKLTECimBzPdwNA_UAA9SH1H8_BPT_mYcdzkO1rPH26eOLBZyeDJcSlYX4DqWbQDsJDYyjAKUpV9y-8YPRJDafvehM_Tjn4e-H9cKhVvQhHB7O6eZAlvy_zg-v8xCdEUAi_C3yeZH6pMNLXZAGp7dGjLfNCpBBUcyvOhllj0xbt9EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایگاه‌های آمریکا در اردن و بحرین هدف حملات پهپادی ارتش
🔹
روابط عمومی ارتش: در ادامه حملات پهپادی ارتش جمهوری اسلامی ایران و در بیست‌و‌چهارمین مرحله عملیات صاعقه، بامداد امروز، «مخازن سوخت»، «انبار و سوله‌های بزرگ تجهیزاتی» و «محل اسکان» نیروهای ارتش تروریستی…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/452232" target="_blank">📅 10:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452231">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1df94d94be.mp4?token=t4iRuwerZgAdc5co8X3M3TmoeUJM7DIbKy0i-cffD8PtGPd2u2ps4Rx9ahnc8ojRPWz1QVpCiaP5vLsgaxV0-mqdwD35JhAsgqOLBY9OAw-A8m2JslnbG6R4Lv2RarTZ2NzZUN1u5_Gru0cTFqt3OKlgxuIXxWgGZv2eLd5QSntcYZH3M-ejp8MJ1QodG18NcyCmhuYYLwtjOe-SHUCMZlr3hmoPKNGP4O0gI-xOsPHGwK2bStjip8dLPQw_G9DzbOjRhDsIl3jDiliXY90KZ5b1HsUSYLm3dshXdk7K7mtfUu71JZQRom8mjCXO3pbE4wui2coeLJSqNmHD7rJa5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1df94d94be.mp4?token=t4iRuwerZgAdc5co8X3M3TmoeUJM7DIbKy0i-cffD8PtGPd2u2ps4Rx9ahnc8ojRPWz1QVpCiaP5vLsgaxV0-mqdwD35JhAsgqOLBY9OAw-A8m2JslnbG6R4Lv2RarTZ2NzZUN1u5_Gru0cTFqt3OKlgxuIXxWgGZv2eLd5QSntcYZH3M-ejp8MJ1QodG18NcyCmhuYYLwtjOe-SHUCMZlr3hmoPKNGP4O0gI-xOsPHGwK2bStjip8dLPQw_G9DzbOjRhDsIl3jDiliXY90KZ5b1HsUSYLm3dshXdk7K7mtfUu71JZQRom8mjCXO3pbE4wui2coeLJSqNmHD7rJa5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از محل برخورد پرتابه در نزدیکی فرودگاه اربیل عراق  @Fardna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/452231" target="_blank">📅 10:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452230">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">حملهٔ هوایی دشمن به پیرانشهر
🔹
مدیریت بحران آذربایجان‌غربی: حوالی ساعت ۹ صبح امروز یک نقطه در پیرانشهر مورد حملهٔ هوایی دشمن امریکایی قرار گرفت.
🔹
در این حمله چندین خودرو نیز آسیب دید؛ هنوز آمار احتمالی از تعداد شهدا و مجروحین این حملهٔ جنایت‌کارانه دشمن در دست نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/452230" target="_blank">📅 10:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452228">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c72562f143.mp4?token=dTj77c3SN8r3xgLpJcUqcMg6e3GVV9w_Fa0kXW-KgzM2L3l-XARnBh7exbXgfQiPMotMq6BpYQrAc6KXtHDXrlQNj-pfuMc7O2w-mDFlfaVAj6Fu-DcRr93JWOExU2fWD7y8Fz4AXIlKywO4fjE9RenVWc19eqhvNo3gQ4bo1VpgQYyTpUWn4vHAE21CSJWLU8QiVwTXOfj7hhu2OGlFzmcSndJj4575Xf3YsivZXY7by6tyqQRGB6xJxHNsLpVa5gPwRw2ZOMMiW48a70RQPwmppnHGo5gqOS1Kqnd-6tnrugXqW1mLuj_tE2G8f9hwstt_5l9JUz-qpFvIK-35ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c72562f143.mp4?token=dTj77c3SN8r3xgLpJcUqcMg6e3GVV9w_Fa0kXW-KgzM2L3l-XARnBh7exbXgfQiPMotMq6BpYQrAc6KXtHDXrlQNj-pfuMc7O2w-mDFlfaVAj6Fu-DcRr93JWOExU2fWD7y8Fz4AXIlKywO4fjE9RenVWc19eqhvNo3gQ4bo1VpgQYyTpUWn4vHAE21CSJWLU8QiVwTXOfj7hhu2OGlFzmcSndJj4575Xf3YsivZXY7by6tyqQRGB6xJxHNsLpVa5gPwRw2ZOMMiW48a70RQPwmppnHGo5gqOS1Kqnd-6tnrugXqW1mLuj_tE2G8f9hwstt_5l9JUz-qpFvIK-35ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عربی از وقوع ۲ انفجار در اربیل عراق خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/452228" target="_blank">📅 10:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452227">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/314e4b0791.mp4?token=A3WOwK_U_WCDCJLxyYTl2Sy6KKX3M62K7OciB2uuOy8rqXG9v3gd3Kb77IGAcd8oTMLNEwEsbpO-E5k04gPBr94XFwx6iXVq1Noydh-PERrVzWiSjlRgp9VjB822qOcfCaiL-Jjeg957KQykrOktcAJGMWMKEg44Uk0jSnr8haRw178lwKVtJHYnX7CRM0mlgx03q95MFXZ9S_nyhKknWFGxy-aqK1DGm8FgVkJ1YXcL3czGbbFgck9kGoOW64BLdq3NP0EeToCVVEvaMCV6_OtK4cIle7pLuF0bbqHwnRZyklHgbBzO2hUjuOjlD1g47Q__rFEs6yVgL-XTVzkwFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/314e4b0791.mp4?token=A3WOwK_U_WCDCJLxyYTl2Sy6KKX3M62K7OciB2uuOy8rqXG9v3gd3Kb77IGAcd8oTMLNEwEsbpO-E5k04gPBr94XFwx6iXVq1Noydh-PERrVzWiSjlRgp9VjB822qOcfCaiL-Jjeg957KQykrOktcAJGMWMKEg44Uk0jSnr8haRw178lwKVtJHYnX7CRM0mlgx03q95MFXZ9S_nyhKknWFGxy-aqK1DGm8FgVkJ1YXcL3czGbbFgck9kGoOW64BLdq3NP0EeToCVVEvaMCV6_OtK4cIle7pLuF0bbqHwnRZyklHgbBzO2hUjuOjlD1g47Q__rFEs6yVgL-XTVzkwFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عربی از وقوع ۲ انفجار در اربیل عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/452227" target="_blank">📅 10:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452226">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">۲۲ متهم پرونده‌های ارزی بازداشت شدند
🔹
دادستان تهران: تاکنون برای مدیران شرکت‌های تراستی ۵۹ پرونده تشکیل شده که در ۴۳ پرونده، قرار جلب دادرسی صادر شده است.
🔹
۲۲ نفر از متهمان این پرونده‌ها به زندان معرفی شده‌اند و برای ۱۵ نفر از آنان اعلان قرمز (اخطار بین‌المللی پلیس اینترپل) صادر و درحال پیگیری است.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/452226" target="_blank">📅 10:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452225">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">تجاوز دشمن آمریکایی به مقر سپاه در زیباکنار
🔹
استانداری گیلان: مقر حضرت سیدالشهدا(ع) نیروی دریایی سپاه در زیباکنار هدف حملهٔ دشمن آمریکایی قرار گرفت.
🔹
براساس بررسی‌های اولیه، تاکنون هیچ‌گونه گزارشی از خسارات انسانی دریافت نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/452225" target="_blank">📅 10:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452224">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🎥
تصاویری از محل تیراندازی در سرزمین اشغالی که درپی آن ۴ اسرائیلی زخمی شدند  @Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/452224" target="_blank">📅 09:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452221">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f19eb0e097.mp4?token=iO3EOOeYEdKHgEW1LLjJnPZHu2zSNkS_B_4PC9HJbQ-bahefv5tZ8MRx77-7a9Dxd-77xmLKnDuzN1abIMrBR3uUj7uz2vp6saP1WhPc18Bi5vJJLPZ4dKnURnCieMyObEGiy7P5KWXwa8fhsNrB3fBmn_3op5P5unmrnsFHgJn1-mHYZx4lHhQf59keNBkAt7EnaaAKMFXmcWPunPhOQH1OrrkLJ6HcVsYfcu80uQcZdKwoKv5WvYjKQhIsb-JSBagH_u5eSfezyXQxW8OtUOD2ywBnen9ovs5Kpy-BeeKvD0Un-9LlBs7Pi1YB3gTUBIJ3uvnI7upZjTsY5Js0Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f19eb0e097.mp4?token=iO3EOOeYEdKHgEW1LLjJnPZHu2zSNkS_B_4PC9HJbQ-bahefv5tZ8MRx77-7a9Dxd-77xmLKnDuzN1abIMrBR3uUj7uz2vp6saP1WhPc18Bi5vJJLPZ4dKnURnCieMyObEGiy7P5KWXwa8fhsNrB3fBmn_3op5P5unmrnsFHgJn1-mHYZx4lHhQf59keNBkAt7EnaaAKMFXmcWPunPhOQH1OrrkLJ6HcVsYfcu80uQcZdKwoKv5WvYjKQhIsb-JSBagH_u5eSfezyXQxW8OtUOD2ywBnen9ovs5Kpy-BeeKvD0Un-9LlBs7Pi1YB3gTUBIJ3uvnI7upZjTsY5Js0Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ پهپادی اوکراین به انبارهای لجستیک روسیه در سن‌پترزبورگ
🔹
اوکراین در ادامهٔ حملات پهپادی خود، مراکز لجستیکی شرکت «وایلدبریز» در سن‌پترزبورگ و استان لنینگراد را هدف قرار داده و همزمان یک کارخانه صنایع هوایی وابسته به شرکت «آلماز-آنتی» نیز هدف حمله موشکی قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/452221" target="_blank">📅 09:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452220">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed3a98b7f1.mp4?token=Q24LvS49tpSJVOiy4c_kBP-GMNq-mXSEcI-Bi_xLqZ5S8AMfajBGquASGvNRpcRfxbtRQ4yZFmqYjJuGDK6rz4TcZWog9awccRnJ6OKGvLRl_srukLd946T93yzXs0rHHqWoMSChzwOEC0hhdh_S6TtpsluOCFqmcNO-BrZWRFFoeWL5Ihck3JznHzfsaXPOzemXuir7gUXM4R1REEubdwp7PS13UHW6Q4GRUfzbQMdUqKdD4y96ejxmK2fMivf5XRMUQmlZMnDfBVIVLr4c-r65hKOBAw-zBLP4wrGp_RKgTASS1h58uqHpzg--PQlrpviu4IsZ04GpPz5OOtId5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed3a98b7f1.mp4?token=Q24LvS49tpSJVOiy4c_kBP-GMNq-mXSEcI-Bi_xLqZ5S8AMfajBGquASGvNRpcRfxbtRQ4yZFmqYjJuGDK6rz4TcZWog9awccRnJ6OKGvLRl_srukLd946T93yzXs0rHHqWoMSChzwOEC0hhdh_S6TtpsluOCFqmcNO-BrZWRFFoeWL5Ihck3JznHzfsaXPOzemXuir7gUXM4R1REEubdwp7PS13UHW6Q4GRUfzbQMdUqKdD4y96ejxmK2fMivf5XRMUQmlZMnDfBVIVLr4c-r65hKOBAw-zBLP4wrGp_RKgTASS1h58uqHpzg--PQlrpviu4IsZ04GpPz5OOtId5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اورژانس اسرائیل: ۴ اسرائیلی در حمله به شهرک حفات جلعاد زخمی شدند.  @Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/452220" target="_blank">📅 09:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452217">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef4e4007f7.mp4?token=BYBIarcTjpKSBszR3eUK28OgUCf60GwcCufd3zVbc_bOglGkgFEQYp88VGnvL5B7p8VtbwIn9aNr1s0KZSLtOBsQvsjpw4YlWXCb88-YX22J4kOoTn7gs-UelZtR7f5RbY0HTiiuoWGfBCgtbCTqUR4n9DuNNg1f3ymV9oQkvCvmTnEnbJ253rpqSuhye1Iwtt7F8csJCuHj_lUWCmnRzbBb_RacqPWb8NbSDX0FWWeAzoWRfWJA5RKfoCSAguLm8scb6Zbkt1Z0PT8o1DM6qmoD-yvoBHWsPDOr2qY4p7MELT7cpKD-HcyYKKScFcIWZqwSE9uMrKq5W1ZgcZaIKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef4e4007f7.mp4?token=BYBIarcTjpKSBszR3eUK28OgUCf60GwcCufd3zVbc_bOglGkgFEQYp88VGnvL5B7p8VtbwIn9aNr1s0KZSLtOBsQvsjpw4YlWXCb88-YX22J4kOoTn7gs-UelZtR7f5RbY0HTiiuoWGfBCgtbCTqUR4n9DuNNg1f3ymV9oQkvCvmTnEnbJ253rpqSuhye1Iwtt7F8csJCuHj_lUWCmnRzbBb_RacqPWb8NbSDX0FWWeAzoWRfWJA5RKfoCSAguLm8scb6Zbkt1Z0PT8o1DM6qmoD-yvoBHWsPDOr2qY4p7MELT7cpKD-HcyYKKScFcIWZqwSE9uMrKq5W1ZgcZaIKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیلاب مرگبار در آمریکا
🔹
مقام‌های ایالت ویرجینیای غربی اعلام کردند که درپی سیلاب‌های ناشی از بارش‌های شدید باران در روزهای اخیر، دست‌کم ۲ نفر جان باخته‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/452217" target="_blank">📅 09:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452216">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
اورژانس اسرائیل: ۴ اسرائیلی در حمله به شهرک حفات جلعاد زخمی شدند.
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/452216" target="_blank">📅 09:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452215">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5c1283765.mp4?token=kuEmQdxkdaeQrNVzKgJxHfapWgHtTzcEfQVizaBClGfYwt49H6-dn-bnRp88p5YC2TIruBXhu5Zkmq1RBq0OtVh0jViP2v3C-r1s4wnlAnDHtCPxr_JhduS-U4MfStBKTiSaRWBSLdLs3zYBz8Oy4rqetvpITK1MydWp11VWNCjv0QG0ERjS87c3ZKnEJzPhc1dSQJfEUn5U3J27BfLgZphqa6kdIEUbIxBW16bM8ifbeDuQBsn90lO928K26vHDpcN66Dlop90iS76i9UlxdH69w3qcR-P_pSIEL71FRWYyhB2S35JMFt8j5rCf0yZoQRDH7uUm_LZAsPT0t0Fazg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5c1283765.mp4?token=kuEmQdxkdaeQrNVzKgJxHfapWgHtTzcEfQVizaBClGfYwt49H6-dn-bnRp88p5YC2TIruBXhu5Zkmq1RBq0OtVh0jViP2v3C-r1s4wnlAnDHtCPxr_JhduS-U4MfStBKTiSaRWBSLdLs3zYBz8Oy4rqetvpITK1MydWp11VWNCjv0QG0ERjS87c3ZKnEJzPhc1dSQJfEUn5U3J27BfLgZphqa6kdIEUbIxBW16bM8ifbeDuQBsn90lO928K26vHDpcN66Dlop90iS76i9UlxdH69w3qcR-P_pSIEL71FRWYyhB2S35JMFt8j5rCf0yZoQRDH7uUm_LZAsPT0t0Fazg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
منابع عربی: ۴ انفجار، پایگاه هوایی شیخ عیسی در بحرین را لرزاند.  @Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/452215" target="_blank">📅 09:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452214">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fy-fFJnvDeaOx4mPe1NYZXFZxfFsvT3EK5PiKxWDnpzsqqgtdLhx0CLuMwApkfiXOPZRawnjc2igjtvCi3mJmjThaa2v1elc-zknDk6Nh-3YI64N6HP7Pix-J5F98XeE8fhd2LrRJBap7RmenCnVtMd1faohbdvlZ3z4XWntjxkKMivfZTBshQt6yv3QMnh6BEJDPNbgS9k5kh5mfFGiUcVWGUO1zwdEN8oKQPOHhBMTmv3KfBZPSyBGw9lVilEKFKml3F94TmIYUlPwis_IAclOiQue3fnCxT7X8nqfarRkv4YbVdY5WHCWk1S7mbvy-YjKQSGhf6uL_-ovT9meqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عکس یادگاری نشست وزرای امور خارجه سازمان همکاری شانگهای در قرقیزستان و حضور عراقچی در این نشست  @FarsNewsInt</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/452214" target="_blank">📅 09:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452212">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BR4LBftvbfCv03CtFaFcJFlanBoJ31kS0X1ZK9ctRE4n6hPIEYIqgjg5u43qYmL1ahL1ARUdny_-6BpQKdUira4uS69-RrQBvxrr10jbKmyvDVWIxdfK5Sd_1O6Ogs7Qx8QKiP42O2UeCHZRDzYbZYiVjqK8z7Vmp4P_8X2KQESloQr8k-iEggPRL8UmRC3d53xKITJr05JJ5v5-87StKIAXUzoaPtQ2EUQGzlnCCvonSXhIxJojXjRsNn5S9FWjfTRFc-TQ5L0ypWd94Uap2eWkCwWlDyzaiA34ANulMp949i5jrblrcYk9o22cKQvzXKCAlcItj4zNmyXhUdWArQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JHmIF6IVV7tnjUQMKh4K3MJHAWJeJnH5R9DazAxUhZ77BiZRH3sQcPxezb3J5SisnCQxxC6_ruIBvXpbycyaBM1XUCzCZSlaodxn0ZpxHArAYWGJYg-ScDDX4htJZ_g3BtXyKsBpzsUi5ngO7JUXhCYLwWZAD4lRh1acCzWqH5bIc7NS1Hw5d8XpGmzvlGASmcy1lOfZoTfzXmMf3LG2fmmu4pAx4DIWwi6-TlA95bB20Du1zQfVH85nHvZqWWVg_tPaZhH2nM1PAMywfXSEBtopsle3aotcimS9E0kEnJSuQVP_TAmjZ9RLYmEsHWfpljYMSUNbrjXwE4lNhtTbxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عکس یادگاری نشست وزرای امور خارجه سازمان همکاری شانگهای در قرقیزستان و حضور عراقچی در این نشست
@FarsNewsInt</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/452212" target="_blank">📅 08:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452211">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">تکذیب حملهٔ موشکی دشمن تروریستی آمریکا به خرمشهر
🔹
استانداری خوزستان: حملهٔ موشکی از سوی دشمن تروریستی آمریکا در شب گذشته به خرمشهر صورت نگرفته است؛ تاکنون شهرهای اهواز، اندیمشک و امیدیه مورد هجوم دشمن تروریستی قرار گرفته‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/452211" target="_blank">📅 08:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452210">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c755cc57a9.mp4?token=muzl4TH8H2e3vEGHGOxQzdcibM3_USI4eZKV0EHUjW4aiw2fqGxUNCI1OKodz5e8B8i5lkPyqa_yGsUKJEaLm_gnKim814S-_3pFzRT-v3sH6Q-hBoZnumnQysmkHyJJXTjET5bCDCjlmWFgL7_k7lj9PxwI8HKnRvH1B9Bs5CfjF0Q6Xxa41eiTgKHVnQyLCEC0E1FbBkin9yTyPiuPIl0Yo4En7kj-Iz4JsWFG8YNiaKfLbulcDPRFs_ZWQ0YofSSpWIyuRIJHM31VBs5tnX7jXrERSbLiWMfEAfF2G77n81kO1F8MMc8T-wyC_5zRjmHbPL5GMckZds9dYnMScg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c755cc57a9.mp4?token=muzl4TH8H2e3vEGHGOxQzdcibM3_USI4eZKV0EHUjW4aiw2fqGxUNCI1OKodz5e8B8i5lkPyqa_yGsUKJEaLm_gnKim814S-_3pFzRT-v3sH6Q-hBoZnumnQysmkHyJJXTjET5bCDCjlmWFgL7_k7lj9PxwI8HKnRvH1B9Bs5CfjF0Q6Xxa41eiTgKHVnQyLCEC0E1FbBkin9yTyPiuPIl0Yo4En7kj-Iz4JsWFG8YNiaKfLbulcDPRFs_ZWQ0YofSSpWIyuRIJHM31VBs5tnX7jXrERSbLiWMfEAfF2G77n81kO1F8MMc8T-wyC_5zRjmHbPL5GMckZds9dYnMScg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایگاه‌های آمریکا در اردن و بحرین هدف حملات پهپادی ارتش
🔹
روابط عمومی ارتش: در ادامه حملات پهپادی ارتش جمهوری اسلامی ایران و در بیست‌و‌چهارمین مرحله عملیات صاعقه، بامداد امروز، «مخازن سوخت»، «انبار و سوله‌های بزرگ تجهیزاتی» و «محل اسکان» نیروهای ارتش تروریستی آمریکا در پایگاه شیخ عیسی بحرین هدف پهپادهای انهدامی آرش قرار گرفت.
🔹
در ادامه این مرحله از عملیات صاعقه، «آشیانه هواپیماها»، «آشیانه تعمیر و نگهداری هواپیما» و «محل اسکان» مزدوران ارتش متجاوز آمریکا در پایگاه الازرق اردن نیز، هدف حملات پهپادی ارتش  قرار گرفت.
🔹
هر اقدامی در جهت مقابله با منافع مشروع و قانونی ملت و نظام مقدس جمهوری اسلامی ایران، موجبات سلب امنیت و منافع اقتصادی دیگر کشورهای منطقه را نیز، فراهم خواهد آورد.
@Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/452210" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452209">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای چند انفجار در بحرین خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/452209" target="_blank">📅 08:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452208">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای چند انفجار در بحرین خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/452208" target="_blank">📅 08:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452207">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای چند انفجار در بحرین خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/452207" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452206">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‌‌
🔴
قطعی برق در مناطقی از بندرعباس پس از حملۀ آمریکا
🔹
مدیریت بحران استانداری هرمزگان: درپی حملۀ ارتش تروریستی آمریکا به محلۀ تپه‌الله‌اکبر بندرعباس، یک تیر برق دچار شکستگی شده و پارگی سیم برق نیز در محل حادثه رخ داده است.
🔹
تیم‌های عملیاتی شرکت برق در محل…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/452206" target="_blank">📅 07:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452205">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
دقایقی پیش صدای یک انفجار در جنوب شهر خرم‌آباد به گوش رسید.  @Farsna</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/452205" target="_blank">📅 06:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452204">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68d31e61db.mp4?token=k9vK5GpZz11Bzpv7ptQYFH1yF_pXTRiCPeQEL3v2IjCvZwWTn9B0mFHLu0geBixE_YXhmRkKC9aljIebribyt5Ir-Tpp2P5Wkgfb8EY9_7IixKs8K7QgI8LQfEyLP_a__sgDJ6jjadNLB69fc_lVJm5KtY7R5XSPDwcucdRXiKJeg6RK1f8e1Gp0wXd6kKvbvykos2bPXjG3ZreDm6pBrnY27CWY3uVH9AoqE6rGkzlq0L4H5WILncPLjg4fi6Wy0pxxxcxkzqnNrlKFflQvT7KNEogzy0MgB-GfXUKfy4MXaN6gOj0abjwCk3WyT3Iv6vx3RzAlpnOGy6haShvdxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68d31e61db.mp4?token=k9vK5GpZz11Bzpv7ptQYFH1yF_pXTRiCPeQEL3v2IjCvZwWTn9B0mFHLu0geBixE_YXhmRkKC9aljIebribyt5Ir-Tpp2P5Wkgfb8EY9_7IixKs8K7QgI8LQfEyLP_a__sgDJ6jjadNLB69fc_lVJm5KtY7R5XSPDwcucdRXiKJeg6RK1f8e1Gp0wXd6kKvbvykos2bPXjG3ZreDm6pBrnY27CWY3uVH9AoqE6rGkzlq0L4H5WILncPLjg4fi6Wy0pxxxcxkzqnNrlKFflQvT7KNEogzy0MgB-GfXUKfy4MXaN6gOj0abjwCk3WyT3Iv6vx3RzAlpnOGy6haShvdxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود سید عباس عراقچی وزیر امور خارجه  به محل اجلاس وزیران امور خارجه شانگهای
🔹
سید عباس عراقچی، وزیر امور خارجۀ کشورمان صبح امروز وارد محل نشست شورای وزیران سازمان همکاری شانگهای شد و مورد استقبال دبیرکل این سازمان قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/452204" target="_blank">📅 06:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452203">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioXhsYNzI7KfzuGlKqdsHZmloLIhrW-0JUUwy-t9Ewoj21I4uEmXJ4M3H4c9aQqel4lc-UiQ70z7LmGQAkglOUwgAQFn4QnLWneBtDc5imrxJ-QG9hXzV8l0jBtgOzmlwnyUZKMkNsCJGUZqXC_nxNZ0nxraAbNsKn-cGEz26-CuK6Jjis_cQAUTM4djEcf2aEx-taIxZMkYu_eGeglvBjQQ6pk4D70WoZuX3zO9ytxagXWCUedaWjYx8ccA4z324xpcLMCAs-yiWDTLoXBvkeHlSb5pq8FIAAjvrF8A-GrFF37mEj4ipsD7trx-wwROQeAqlQuMxV3E73hMZW4O8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
هشدار عراقچی به توقیف دارایی های کشورمان؛ آشوب و بی‌ثباتیِ ناشی از چنین روندی، نه خوشایند خواهد بود و نه صلح‌آمیز
🔹
توقیف دارایی‌های یک کشور برای پرداخت مطالبات احتمالی و نامرتبط در آینده، ایجاد یک سابقه خطرناک و التهاب‌آفرین است.
🔹
کسانی که از چنین منابعی استقبال می‌کنند یا از آن سود می‌برند، باید به خاطر داشته باشند که وقتی دولت‌ها مصادره اموال دیگران را به یک رویه عادی تبدیل کنند، دیگر هیچ دارایی‌ای از امنیت و مصونیت برخوردار نخواهد بود. آشوب و بی‌ثباتیِ ناشی از چنین روندی، نه خوشایند خواهد بود و نه صلح‌آمیز.
@Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/452203" target="_blank">📅 06:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452202">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
تجاوز دشمن به منطقه‌ای در نایین
🔹
معاون استانداری اصفهان: ساعت سه بامداد امروز منطقه‌ای در شهرستان نایین مورد تجاوز دشمن متجاوز آمریکایی قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/452202" target="_blank">📅 05:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452201">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIjoa3yy9JTINfwty5yQ5SsybiDFsxSZ4JbuF9Nh-fpLLPNvdidP-LovWGnyR0iwaV-YJSfS6W1661SvNd7ay7Wb1AHwZNHx_RQj8ofZkUMvy1zKFLMcfGxhg0QheGlSIhMWvD2QOIeakpXvMM48tSxPiqumGFWtgo5B9Y_9wS7r7mm5Z778cyALWyhWYdQLrvuvU3rdLfYKHGlSWEBeuEn9ixcdFEZai5Z5I94kP_laxXgLoilCIfyomRh5t8ZlMSZApuL3-Z7NwY8beJH13y8Op7663C6H0Ow4fyUksFASxWfUQ61XJ1FLPmbPAvw050BXNSs4bzw7zBuWwIWd1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگرانی اسرائیل از سرعت ایران در بازسازی زیرساخت‌های آسیب‌دیده
🔹
روزنامه وال‌استریت‌ژورنال نوشت سرعتی که ایران زیرساخت‌های آسیب‌دیده را بازسازی کرده موجب نگرانی برخی از مقام‌های اسرائیل شده است.
🔹
این روزنامه نوشته اظهارات مقامات و تحلیل تصاویر ماهواره‌ای نشان می‌دهند ایران زیرساخت‌های آسیب‌دیده از بمباران‌های ماه‌های اخیر توسط آمریکا و اسرائیل را با سرعتی بالا بازسازی کرده است.
🔹
این زیرساخت‌ها از پایگاه‌های موشکی پنهان‌شده در دل کوه‌ها گرفته تا پل‌ها، بنادر و مراکز تولیدی را شامل می‌شوند.
🔹
در نزدیکی کنگاور در غرب ایران، تصاویر ماهواره‌ای شرکت «پلنت لبز» در ماه مارس آسیب‌دیدگی دو ورودی تونل و یک جادهٔ دسترسی را در اثر حملات هوایی نشان می‌داد که با هدف مسدود کردن دسترسی به یک پایگاه موشکی ایران انجام شده بود.
🔹
اما ظرف چند هفته، تصاویر شرکت «ایرباس» جاده‌ای تمیز و آسفالت‌شده را نشان داد که به ورودی‌های تازه خاک‌برداری‌شده منتهی می‌شد.
🔹
🔹
در موردی دیگر، یک مقام نظامی اسرائیل گفت ایران پُلی را که اسرائیل با سه بمب هدف قرار داده بود، ظرف چند روز ترمیم کرد؛ اقدامی که موجب غافلگیری مقامات اسرائیلی شد و آن‌ها را به تردید دربارهٔ اثرگذاری اهداف انتخابی خود وا داشت.
🔹
وال‌استریت‌ژورنال نوشته آواربرداری و جبران خسارات ناشی از حملات آمریکا و اسرائیل مستلزم صرف تلاشی عظیم، پرهزینه و زمان‌بر است اما سرعت بالای اقدامات ایران در سراسر کشور ادعاهای دونالد ترامپ و بنیامین نتانیاهو مبنی بر وارد کردن ضربه‌ای ویرانگر به ایران را زیر سؤال می‌برد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farsna/452201" target="_blank">📅 05:13 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452200">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‌ اخبار تکمیلی از حملۀ آمریکا به پل‌های جنوب؛ ۵ پل مورد اصابت قرار گرفتند
🔹
استانداری هرمزگان: در ادامۀ حملات تجاوزکارانۀ آمریکا به استان هرمزگان، متأسفانه علاوه بر پل کهورستان، پل‌های دیگر شهرستان خمیر هم مورد اصابت قرار گرفته است.  کدام پل‌ها مورد حمله قرار…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farsna/452200" target="_blank">📅 04:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452199">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
حملۀ هوایی دشمن آمریکایی به خنداب
🔹
معاون استاندار مرکزی: یک نقطه خارج از شهر خنداب هدف حملات موشکی دشمن آمریکایی قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farsna/452199" target="_blank">📅 04:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452198">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
دقایقی پیش صدای یک انفجار در جنوب شهر خرم‌آباد به گوش رسید.
@Farsna</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farsna/452198" target="_blank">📅 03:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452197">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
دقایقی پیش صدای چند انفجار در جاسک به گوش رسید.
@Farsna</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farsna/452197" target="_blank">📅 03:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452196">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‌ ۲ مجروح در حملۀ آمریکا به بندرعباس
🔹
معاون استاندار هرمزگان: تاکنون مجروحیت ۲ نفر در حملۀ دشمن آمریکایی به تپۀ الله‌اکبر بندرعباس گزارش شده است. @Farsna</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farsna/452196" target="_blank">📅 03:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452195">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
دقایقی پیش صدای چند انفجار در بندرعباس شنیده شد.
🔹
انفجارها از سمت غرب بندرعباس و تپه‌های الله‌اکبر است که تاکنون چندین بار مورد حمله قرار گرفته است.  @Farsna</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farsna/452195" target="_blank">📅 03:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452194">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
حملهٔ موشکی آمریکا به اطراف اندیمشک و امیدیه
🔹
معاون امنیتی استانداری خوزستان: نقاطی در اطراف شهرهای اندیمشک و امیدیه مورد حمله موشکی ارتش تروریستی آمریکا قرار گرفت.
🔹
این حملات تاکنون مجروح یا شهید درپی نداشته است.
@Farsna</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farsna/452194" target="_blank">📅 03:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452193">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
دقایقی پیش صدای چند انفجار در حوالی منطقه سوزا در قشم شنیده شد.
@Farsna</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farsna/452193" target="_blank">📅 03:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452192">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQ9Xxnj922bV9zFmeXaLnlYdF2H5do1uw_rxhuMOG_C4sZDSCqkQhPs0in7vd5TozuX2rSHQ8tLJB-w5j-u4jCpChOaoDGHzAR7DC8YZa4UPXPYDb5iL1xwa6QCU8NbeEOFgXYdF8JmAAY4pXtSitpFQ4hhWl64Wu0j3bBCmXB_LOapdo-g0LNRoYaWZZnPgGRL2wnZs9QzMLX-VaEtcpvvaZRDuXD-Vpr2B2-a6J9Xzgo-Ja3nQ8Xt_6w2x0JpCm7GdzGhP7JtFEClVf0t6jc8qVsBj84DW19lI5mNWxFxUsHT_ALA0eYYswKxJPfeOmRmRGEADz4ugyEZocLmQEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان تروریستی سنتکام: دور جدیدی از حملات علیه ایران را آغاز کردیم.
@Farsna</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farsna/452192" target="_blank">📅 02:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452191">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
دقایقی پیش صدای چند انفجار در بندرعباس شنیده شد.
🔹
انفجارها از سمت غرب بندرعباس و تپه‌های الله‌اکبر است که تاکنون چندین بار مورد حمله قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farsna/452191" target="_blank">📅 02:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452190">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در اهواز
🔹
معاون امنیتی استانداری خوزستان: دقایقی پیش نقاطی در اطراف شهر اهواز توسط ارتش تروریستی آمریکا هدف قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farsna/452190" target="_blank">📅 02:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452189">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8hKECOoT0uX31PcPtbMhKmTG4yxcw4s9WvXCYX37BjHLKp6rfwBUuS1NL8y1XJBlBrDYRO0IGbmcWrOVhgatOxviR1V6zz5Ri5xDRDyilwr7wnVXQTwP64wIhhukd3XRRmZjdHS8g-QsasF4IExvLlmB4hWpKNLD_IYTg2rO3dWLyMenOaycUhBhxGWGTngec0kZE8TQy7vH7UDLwlkzPl7ieNLVBOtZIP6xW5uegLDoLIAWul-diegVSUiwuV1KEe2WadG90-s_5rWX39VVkLUGpKRLYomkmhaYwcdbFVd6BDTJrnBCm9oe_UfF7PWVwXb8tyCQDGQFBJz9onVBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵۵ شهید و ۶۲۹ مصدوم در حملات دشمن آمریکایی به ایران
◾️
رئیس روابط‌عمومی وزارت بهداشت: از ۶ تیرماه تا ساعت ۹ صبح اول مرداد، ۶۲۹ نفر مصدوم و ۵۵ نفر به شهادت رسیده‌اند.
◾️
بین مصدومان ۴۶ زن و ۲۴ کودک‌ونوجوان زیر ۱۸ سال، و درمیان شهدا ۶ زن و ۳ کودک‌ونوجوان زیر ۱۸ سال دیده می‌شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farsna/452189" target="_blank">📅 02:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452188">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farsna/452188" target="_blank">📅 02:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452187">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d8c129d3.mp4?token=PW2ACRNgA_5q-fG_ZJYwyT6pn1xHw60sz1QYOKIVtmBizQBuci645dfPMteHFIqThhZr4idl6MTzWE5EzHFm7kUJ7tiiTi4Yw8s3Z4t_76rDdgFeMWoPepCSt5-4YEiqu-uPVnrYLU7w-gC5tQaQrOjh6eXXDncPYQK6yyzxv59NQSiRWio42N-d1Z2Jeu_uXv7fOQjDU2kxR51QnNW0wIbMSMgww_peBO4A63YT-ijvDy1NB_7DdHliDvsMhd4cgET9-_pD-67lm_gvJjOcHnYryCPnMj4AghLkGQsRSdCMDfiZZQSbySbUVkQepuHR3QW96YkKHT1QAuEQxSdU8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d8c129d3.mp4?token=PW2ACRNgA_5q-fG_ZJYwyT6pn1xHw60sz1QYOKIVtmBizQBuci645dfPMteHFIqThhZr4idl6MTzWE5EzHFm7kUJ7tiiTi4Yw8s3Z4t_76rDdgFeMWoPepCSt5-4YEiqu-uPVnrYLU7w-gC5tQaQrOjh6eXXDncPYQK6yyzxv59NQSiRWio42N-d1Z2Jeu_uXv7fOQjDU2kxR51QnNW0wIbMSMgww_peBO4A63YT-ijvDy1NB_7DdHliDvsMhd4cgET9-_pD-67lm_gvJjOcHnYryCPnMj4AghLkGQsRSdCMDfiZZQSbySbUVkQepuHR3QW96YkKHT1QAuEQxSdU8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عربی: گزارش‌های اولیه از سقوط یک هواگرد در آسمان جزیرۀ قشم حکایت دارد.  @Farsna</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farsna/452187" target="_blank">📅 02:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452186">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
منابع عربی:
گزارش‌های اولیه از سقوط یک هواگرد در آسمان جزیرۀ قشم حکایت دارد.
@Farsna</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farsna/452186" target="_blank">📅 01:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452185">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-LMzvXfPoXf5fQEMvy144UxQtzZ8Iub69gnRvp-i7oN0u5H4llmS7GuG9ixL5jm6PV13pQAKNbIG7t5pUxrfdbvY4ksmQAG00tnBguGuTKvcMBELstOdeKdrZs9CyJqb30mPdWgMo3EOqaMSFFumY8FV4Se0W0fezbiXyxgy6t5Yy3DELQNoUo9BQzK_gSl2yt_AdCnsTKniIeTrf-l_1bq7jR1tIF9Ven59W6PdA2895aiSaFo69SZ3iFlybvNYUTRLa8NMVZY29Z5DceqeaFUNRmMZ4eLCAs2ev7T8XeK8k2TlQaRwBdDfOydZ6YHq141DPPbZhAHInpXIqyKvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دوباره به لفاظی علیه ایران رو آورد
🔹
درحالی‌که مقام‌های آمریکایی بارها مدعی شده‌اند ایران هیچ تسلطی بر تنگۀ هرمز ندارد و آمریکا «کنترل کامل» این آبراه را در اختیار گرفته است، اکنون با تداوم تحولات میدانی و ناتوانی آمریکا در مقابل حملات ایران، رئیس‌جمهور…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farsna/452185" target="_blank">📅 01:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452184">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farsna/452184" target="_blank">📅 01:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452183">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farsna/452183" target="_blank">📅 01:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452182">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farsna/452182" target="_blank">📅 01:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452181">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hw_0okxIySYqANsb420uSuNjDWlXMVCtuXdukUwsQdWPxfKI9YOODMvbwTmVRDMs9HCvX8E2-hwp-mryFAVDKosv3nkvDtcxTJ9gTu7HCvb7UCAzCJjrgdyn0CDAfBjDs3n1BtmxyzlR0jQ9FAvptOzsT9TYEbEZtdwcvSHI9eU0wE80d6un3DpXiKp5KrgbAuNyGXvOhjWgzbdsBuw_hwpbZLafYv8EZAGEZex_f0rNMiTrpDRuYyyt-PWPDoyR9s3fDJO_pGdDmVb61NEZj9bGPN8njT--mtiaHAxiSSzVhgTlWY1TgEFcwFsY7asVr5Lr46hC3VmOyAVJzegbvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انهدام موشک آمریکایی در آسمان کهنوج کرمان
🔹
فرماندۀ سپاه کهنوج: یک فروند موشک تاماهاوک آمریکایی در آسمان این شهرستان رهگیری و منهدم شد.
@Farsna</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farsna/452181" target="_blank">📅 00:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452180">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farsna/452180" target="_blank">📅 00:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452179">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">انتقال تروریست‌های زخمی آمریکایی به آلمان، در پی حملات پهپادی و موشکی ایران
🔹
یک مقام نظامی آمریکایی به نیویورک‌تایمز گفت: در این ماه نزدیک به دوازده نظامی در پی حملات موشکی و پهپادی ایران در اردن و سایر کشورها به شدت مجروح شده‌اند؛ به‌طوری که برای درمان با هواپیما به یک بیمارستان نظامی در آلمان منتقل شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farsna/452179" target="_blank">📅 00:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452178">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
شنیده‌شدن صدای دو انفجار در محدودۀ روستای مسن قشم
🔹
دقایقی پیش دو انفجار در منطقۀ مسن جزیرۀ قشم شنیده شده است.
🔹
همچنین مردم قشم صدای انفجارهایی را از محدوده تنگۀ هرمز در جنوب جزیرۀ لارک و هنگام شنیده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farsna/452178" target="_blank">📅 00:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452177">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
برخی منابع عربی از آتش‌سوزی در بزرگترین نیروگاه برق کویت در پی اصابت یک پرتابه خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farsna/452177" target="_blank">📅 00:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452176">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farsna/452176" target="_blank">📅 00:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452175">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farsna/452175" target="_blank">📅 23:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452171">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O-qTN1s4Iq6CPMm3YA9k-i6sjTLPKRIG1ve_JezVpYv1wy-opN3PbzdUjCuaTclKBqdPnLopPwZ3Q8w58XCPD2N-og3haQyovgFZ4Sfj8lPvZwpyRBnIoFPckqe8qztbGQE2WrOVUzzHjFWL2jiGCc2T-fJNLLu0loqQylAPjoD6goYoV8_NaHVwS2PCUGAi45__nzvlpeExz-OTwy8PZMWbUSAMLMzXTkfEhr0QxIwYZQmZ4xICqSkH_LxnJL_eokOLRLsj1lCKZW4eZzX4pLj-Qz7wAebFHiYbZ-P3Dg3J7bmb7R1BcHvP8muawlEeIIKUY7TpEcxq3hg5b4S6xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FCtk_5GGoE0o6rxbwd7yXvsyNVhYnMtLqIe6N4ySNkyo2tJ-rb7uv13cuhYr9IYKmQXLpFB7NR42GrQmrfgxwW1Mq7w1oFZwJLAomm6qc1YGcAAlc4WJmHekja-JTKv9BOBjlT95d15VMWaOes4EcM8yfiCjuwMiBWVR_lOOrwA_tfg_BInEM12ccTQ3i7xXSK1z_jDOVF96xLyB4INbddAfZ1wbms2aAdI3t_4TE8m7TohxFtFcS5322erTnTpzOMyKsURIKBUgDOxnJ7vEoVu4uhvR5Eq9dkSCbg3m_jGyE3gtzgusm9vv1Gkfle-a7nXOsR9pasGftrc2IOQxrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/noPTyAqAtdwMlg8WOelS6tk8fGBR12Qhx6zbS_ps5moqdIicic0OpgA4HTboQmhBh87VPxEhdZE9Ne9kH5Rqds1bmHhozCMYwukMKQQrTFstIotnK-pnjAuk8gvkIe0XQzCf_gvJsBCR1Uo5zcXd7_A44djSJuKcRTQjwgAtq2kq5Wy29Xt_03B4d6ESlkJz7BGNW1M7a9vSdtZNe94Mn5gwpQDkpbu-_rrdW73Jyr3_Fv2cV_8IrD_xJxq01FGnl-PupYyUl0HZm-wuvzoMw7tVWjQjylKMJ3_UYetRE-8FA8XEEblfzoAfZTSe1uzk1sbjxEopgDM3MVAgsgRxsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y3HIii8HicE46MsiWuPiVvzb_-Dd3sp-s_z_ucRKAnIAE6N9RyMGu5Ul7AaJFnQZ_fJrfQXYmk3NgJ9q71GcO66O604UEfd0M5gvFLGHrMxC6YRYGzJwQcjQfMbebRxKVljwDdUISaS3GHG6XbE6piRYFerRRNS87gdHYiSku3Zodn5SBEOwj5iiNcegQeNoXbk1G10Do1w89Tx60ynBhnRoDX9cAa4RRdJ1cGtWKAMrkpYKS3vy-6g--DvvupbkaavfPb6AS8Oa2HDssDfrur1rwsyD1gv8D4BqTLZ5Kv6zcbDVN5-0-tk2aQIuETl0Sg1OaYC8wtSPqStdYjUZoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
آیا نخست‌وزیر عراق حامل پیغامی از طرف آمریکایی است؟  @Farsna</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farsna/452171" target="_blank">📅 23:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452170">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farsna/452170" target="_blank">📅 23:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452169">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
انفجارهای شدید در کویت
🔹
منابع عربی از شنیده‌شدن صدای چندین انفجار شدید در کویت خبر می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farsna/452169" target="_blank">📅 23:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452168">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
انفجارهای شدید در کویت
🔹
منابع عربی از شنیده‌شدن صدای چندین انفجار شدید در کویت خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farsna/452168" target="_blank">📅 23:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452167">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farsna/452167" target="_blank">📅 22:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452166">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🎥
عملیات شکارِ ترامپ و نتانیاهو
🔹
انیمهٔ جدید از عملیات انتقام علیه وزیر جنگ آمریکا، نتانیاهو و ترامپ
@Farsna</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farsna/452166" target="_blank">📅 22:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452165">
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farsna/452165" target="_blank">📅 22:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452164">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farsna/452164" target="_blank">📅 22:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452163">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farsna/452163" target="_blank">📅 21:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452161">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
زیرساخت مرکزی داده‌های شرکت آمریکایی آمازون در بحرین ویران شد
🔹
روابط عمومی سپاه: با توکل به خدای قادر متعال و در هم کوبنده ستمگران، رزمندگان هوافضای سپاه در ادامه موج ۲۴ عملیات نصر ۲ در پاسخ به تجاوز و تعرض روز گذشته ارتش کودک‌کش آمریکا به تاسیسات در دست…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farsna/452161" target="_blank">📅 21:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452160">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farsna/452160" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452159">
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farsna/452159" target="_blank">📅 21:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452157">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farsna/452157" target="_blank">📅 21:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452156">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXhGiU-cwHoTKEOpmLvdKx-6JBCcH64HRPMJmA3UKzSnvEewVobk5lSabYUUgdmLLQhf0zKRfF_auihOJKEgbsj4k24Nz9_KexIVFPbUjMiLE5DGCdlVs3v52Q7lwuvhG0jM8TyjXiwrgnxnzfy0_sD3gqCbnkXIUVswvCNo3O8J7jQha5kdgbOaefSzBfjtxiqxErnX-4DepWwy6CduQ8xCeETWNd1aovEvyWJ6rWsSIHMfI-2kbeY3LQhB8XlEC0_6fRNKYAP3y2yPf9F55Ciu_VdFVUrYpJewSxAAkjl8JxKvzRMh1bO83ho6z2RC3SM0ELb5FooPST7cLzrdgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتکش ایرانی از خط دزدی دریایی آمریکا عبور کرد
🔹
یک‌ نفتکش منتسب به ناوگان ایران دقایقی پیش با نادیده‌گرفتن محاصرهٔ ادعایی آمریکا از آب‌های آزاد وارد دریای عمان شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farsna/452156" target="_blank">📅 20:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452155">
<div class="tg-post-header">📌 پیام #1</div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farsna/452155" target="_blank">📅 20:47 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

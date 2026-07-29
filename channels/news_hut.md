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
<img src="https://cdn4.telesco.pe/file/tii12tyDIUX0tYNVbOdNprZNALc3QaI_S2unNAZ9L21VapsfkSipwbXxvhKrncfo_g2jQCGjqRjlS1jtsKijNKHsEBYdpaPdZTttcFwIJ_oRLzDDeZwxMvWrGTaQqpwbUVbA5O-zN9hXSwDgJx-hPmgWongNbmoDpKI-Tw2lfUSsxs7sJvovM_ZvQZQrRKmq429lKt9_mEmcGoGrfZc8BfFsWyTEhixEprGRegjrgyvvWZZRWDdGy_HGDyQOTz4vU2XFhGP58vWonSBrfvPwN9aakEUgBMjsaZg7q6M8ltyX8Qg3iw4AhNKN9zVoPv27jzMKxc_SKkxbcHMS1crInQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 142K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 21:31:29</div>
<hr>

<div class="tg-post" id="msg-69209">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AGR6AeZjiNVyVJerOMlz2SI9oY5DBDpw9UeLQftHeItb4yckBM4kKF6KY2xLnUYGhLuZE590f7zgGyCEfMbAxFePSC1_0T7K8aFLKKIIGhEfzuSbHNRWWfeE7PhOtWI_pq7QIikrNmEv8a26Ra9l8hJAwWlFPBZpD8ufluiRLt9fH3Q47c4rwFbIiG65K39DUtPA2BpI8VMW2CBvnsvcSvIovR-N6OB0tkTXWxjlbA7tgr_xo05DATN9-W3NbbZl9wqUo5M9ZFB9rGP_mjLQKa4AZEBV1r02WFSfQtOv7utkumL0Lvmd8hl3JM81wzVJH8Tw7L81zF6ZC3dWfejpMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حمله دیشب آمریکا به حشد شعبی عراق، ۵ تا از نیروهای سپاه قدس هم کشته شدن.
حالا حامیان حکومت میگن واسه اعدام اون جوونای اصفهانی خوشحالی کردیم، خدا چوبمون زد!
@News_Hut</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/news_hut/69209" target="_blank">📅 21:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69208">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3f736bc6e.mp4?token=ES4GHh2yS1MA5XLpD7YR4OFLLPyEfRdRbwop7zuJvmobXXQYMLPrLFcvtrXoek7uS00UQlipM8UOWPZwjMvyvOYVeFLGnCuFMIlXqf42jp5f8GO2qTaihXNMG83k9wDxZfG0IDjDHt6S-KmWCHrXNZncyv4BMKQsWewknD0WLCUIofCs54baUOr-VMMLdebTN-GMdio08gyKVfdt6mB5q4wUp9LZODftH7uwSmf1ip1DTtIGD7kQfSWIg7ZDHTO94VEs4eZ5Ybjz2bOmN05Jj2rB5yjP95zjoPXudqUcJIsF-mhxdaNbgOwOg0vWHDhLSgZ5nAw3tLM_kRNiIPT7KZfH2MXU79_zlzhUBYbATJbFcCKBwi2HUdkO_jhWR3cYsnWdm1v0-oX5pgtVAgSkZ3F-Iqus8XXJ1wb4EGRXOG8fGejfxSPQSz2UUpv1Q9lkQjPjo4SEa1vc3fvAtmiqeWU42l-ff9oAYifwo-e2gcrPVPYw0nAoJk844BXOL3zj1WWrvSOKYDrImv-EEh5jkIAcC1opSSheL5qpPRbMMgZSEXhFIgRaWR5DlxNKhrlOKocJHiEED_BZOHFS0oBMxitnWQQJnmey8I8zTlnDDpuJ1BcELc_mUb5x2IANoX-7u5K2jL3jr7xngHCCBvbj4eTgIFpXNiWYOroZmtHZiGY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3f736bc6e.mp4?token=ES4GHh2yS1MA5XLpD7YR4OFLLPyEfRdRbwop7zuJvmobXXQYMLPrLFcvtrXoek7uS00UQlipM8UOWPZwjMvyvOYVeFLGnCuFMIlXqf42jp5f8GO2qTaihXNMG83k9wDxZfG0IDjDHt6S-KmWCHrXNZncyv4BMKQsWewknD0WLCUIofCs54baUOr-VMMLdebTN-GMdio08gyKVfdt6mB5q4wUp9LZODftH7uwSmf1ip1DTtIGD7kQfSWIg7ZDHTO94VEs4eZ5Ybjz2bOmN05Jj2rB5yjP95zjoPXudqUcJIsF-mhxdaNbgOwOg0vWHDhLSgZ5nAw3tLM_kRNiIPT7KZfH2MXU79_zlzhUBYbATJbFcCKBwi2HUdkO_jhWR3cYsnWdm1v0-oX5pgtVAgSkZ3F-Iqus8XXJ1wb4EGRXOG8fGejfxSPQSz2UUpv1Q9lkQjPjo4SEa1vc3fvAtmiqeWU42l-ff9oAYifwo-e2gcrPVPYw0nAoJk844BXOL3zj1WWrvSOKYDrImv-EEh5jkIAcC1opSSheL5qpPRbMMgZSEXhFIgRaWR5DlxNKhrlOKocJHiEED_BZOHFS0oBMxitnWQQJnmey8I8zTlnDDpuJ1BcELc_mUb5x2IANoX-7u5K2jL3jr7xngHCCBvbj4eTgIFpXNiWYOroZmtHZiGY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
کشتی ترابری گاز آمریکا نزدیک بندر دمیاط مصر با پهپاد هدف قرار گرفت
.
@News_Hut</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/news_hut/69208" target="_blank">📅 20:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69207">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f541b0693c.mp4?token=n0zWTDoXekeC2lk2tAVi5qdJDv1fl2BywP08xBEZDQlzA8V1LlKYj-p3M2kx2Hmji_JgHOzcvB4z6vuuGRXw5cigONyKW9lLCq2pFdgdhPvN22KmKzJfJItmwzw4R3iYEKvPMnDBuR7mItMKBMjrx-p0wJKMxb6sHYGh6PKeDik798SjbT80ypOJsl_zDRTqyCeNSwRSefKFIHBxz_NC-n5ss6kX4ksoG1ej3xg4eQ9sEl91ujKre4uXz-coGG_d1Ws4ontG6-nVbfldUMDD8w1aKUxrhg_819PICXEXqi3BMg8MIoXeV-OGX7Xny_y-SX7KPRMw5yyJvDdccdnFMoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f541b0693c.mp4?token=n0zWTDoXekeC2lk2tAVi5qdJDv1fl2BywP08xBEZDQlzA8V1LlKYj-p3M2kx2Hmji_JgHOzcvB4z6vuuGRXw5cigONyKW9lLCq2pFdgdhPvN22KmKzJfJItmwzw4R3iYEKvPMnDBuR7mItMKBMjrx-p0wJKMxb6sHYGh6PKeDik798SjbT80ypOJsl_zDRTqyCeNSwRSefKFIHBxz_NC-n5ss6kX4ksoG1ej3xg4eQ9sEl91ujKre4uXz-coGG_d1Ws4ontG6-nVbfldUMDD8w1aKUxrhg_819PICXEXqi3BMg8MIoXeV-OGX7Xny_y-SX7KPRMw5yyJvDdccdnFMoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇱
نخست‌وزیر نتانیاهو:
«سفرم به آمریکا فوق‌العاده بود.
همیشه درباره موج نفرت از اسرائیل در آمریکا می‌شنوید، اما احتمالاً کسی از موج حمایت و علاقه‌ای که نسبت به اسرائیل وجود داره براتون نمیگه.
همین الان هم با وزیر دفاع آمریکا،
پیت هگست
، صحبت کردم.
اون یه حرف جالب بهم زد. گفت: "توی دنیا کشورهایی هستن که اراده دارن کنار آمریکا بجنگن، اما توانش رو ندارن.
از اون طرف، کشورهایی هم هستن که توانش رو دارن، ولی اراده‌ای برای این کار ندارن."
بعد گفت: "فقط در اسرائیل هر دو رو با هم می‌بینیم؛ هم اراده و هم توانایی."»
@News_Hut</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/news_hut/69207" target="_blank">📅 20:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69203">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eA2dEwq0WLoQ_8QFAaYMdGzLbmXI8PiQ9iuWeUFS3q0f9T50rpv8d0oaPhISJ-fmBtJK3TAg8MajvCsWBqDfasrZk77dbSN_JISlo1ueysptnKIDpJaR4lLcOBN7PuIzGBfokIW5WFWnXBfuIWnvEGBwo1Wv5knQtgJhyHxkOpMPWGFCtx952aqjtkjZ0Q2Wi3c6xEzdSwWxzm4-0tkP58tiuSBOe1Tq9F1StYUxV9uLmpidR5jBRWX5VbYiL4OvcTpSrwz--qEADxQa_AvAelLPUzfSqgLUa4WIPwdOl0kmKT_-H679yb3xcl9kw2tM5dZzYGxTOzAQaz1ari3_KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1f829b75e.mp4?token=dc0vCJ3XS4z3pRzzzl8Umrbcwgw8QQH5Szurizwbiroaz_ZjW3wTRNYPMceOhOocTbVMOq19bEdiUQkYVnPbNaLkw7ADyt_4k775o-VdLrdib7pB14Q6DvWldrSWdU4oDNVq8TQYcOMeCX9j6Jg8DphcAxX2SRtT3E7rynQOXAIiNLBPAagKdzj3MhW4dpjCEZI_Cyq-GwFkvhDaPgLxPk-kwFf3cWVnSAIvkJaWVGI6Qm7z1LHLUtpAZflYtVscVuIOSolHpTrB7wA02DTkES0fyffNeVLR6byjXlX7VC8fZBJ5yxSStM_4RT9oFZAIyzxx8B2z1F4y177DODV3_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1f829b75e.mp4?token=dc0vCJ3XS4z3pRzzzl8Umrbcwgw8QQH5Szurizwbiroaz_ZjW3wTRNYPMceOhOocTbVMOq19bEdiUQkYVnPbNaLkw7ADyt_4k775o-VdLrdib7pB14Q6DvWldrSWdU4oDNVq8TQYcOMeCX9j6Jg8DphcAxX2SRtT3E7rynQOXAIiNLBPAagKdzj3MhW4dpjCEZI_Cyq-GwFkvhDaPgLxPk-kwFf3cWVnSAIvkJaWVGI6Qm7z1LHLUtpAZflYtVscVuIOSolHpTrB7wA02DTkES0fyffNeVLR6byjXlX7VC8fZBJ5yxSStM_4RT9oFZAIyzxx8B2z1F4y177DODV3_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
اوکراین با حمله‌ای گسترده و پهپادی، منطقه ریازان روسیه را هدف قرار داد؛ در این حمله، یک مرکز لجستیکی بزرگ متعلق به شرکت «وایلدبریز» (Wildberries) آسیب دید و بنا بر گزارش‌ها، پالایشگاه نفت ریازان که تحت مدیریت شرکت «روس‌نفت» (Rosneft) قرار دارد نیز هدف قرار گرفت.
آشکارترین خسارت در انبار حدوداً ۱۸۰ هزار مترمربعی «وایلدبریز» در نزدیکی شهر «ریبنویه» (Rybnoye) رخ داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/69203" target="_blank">📅 19:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69202">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
⁉️
آمبری:
یک تأسیسات شناور ذخیره‌سازی گاز طبیعی مایع (LNG) با مالکیت آمریکایی و پرچم جزایر مارشال، در دمیاط مصر هدف اصابت دست‌کم یک پهپاد قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/69202" target="_blank">📅 19:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69201">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50c2f2b488.mp4?token=uJwZxi91e-S8nvioUP0RB16AC85GtHnDasgH60oqb_HDo8OX7X-GC8Rf6crko_7fEP6N5ERSOZNevM7P7Xw6aCeC_ukbbne5sUfwYFZwrXl5Fzb8iM-478u-MZov1qt70Z9CR0wAR_MRQ8kxQp0nybgDG_nmefq-4dliHqU66Bp72icFksSYuCLmlv4FN4DXrM7C5hQw9j35Okj1mVPEA0UDMSEkgCKD6WXCctqebmJFQX1ID9RLJ10i5925mQawHHxUirXvop8Dpr4dzRW5MgY9E9cAeMYbglRjIdDoZvgjE1FBcTZNQhA8pOFz5cIRcHjRD2xZzU20pt-7Dnrv8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50c2f2b488.mp4?token=uJwZxi91e-S8nvioUP0RB16AC85GtHnDasgH60oqb_HDo8OX7X-GC8Rf6crko_7fEP6N5ERSOZNevM7P7Xw6aCeC_ukbbne5sUfwYFZwrXl5Fzb8iM-478u-MZov1qt70Z9CR0wAR_MRQ8kxQp0nybgDG_nmefq-4dliHqU66Bp72icFksSYuCLmlv4FN4DXrM7C5hQw9j35Okj1mVPEA0UDMSEkgCKD6WXCctqebmJFQX1ID9RLJ10i5925mQawHHxUirXvop8Dpr4dzRW5MgY9E9cAeMYbglRjIdDoZvgjE1FBcTZNQhA8pOFz5cIRcHjRD2xZzU20pt-7Dnrv8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇺🇸
نخست‌وزیر اسرائیل، بنیامین نتانیاهو، با پیت هگست، وزیر جنگ آمریکا، در واشنگتن دیدار کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/69201" target="_blank">📅 19:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69200">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgRtorgWp9Ci8LaGTgdJtYeXlOEuDbcOA6IqKUe_ZOl-tcVaW8KR3DUYRDVoo7VKjQG1mu7h-6wKbo48XCg2tz4xw0d2w2tftc9XP5P43sKZrh6Lz_U3TbgjYk0VKDeKRiTD1g8QS5SWqKXomDEkzhYswL6zzRLUnRBar_j5Z-i_r7_IRRmtQ-oIf4fDte1xDueJyaPuRBmGn7gYqMrvA6KSKtqPMBF-uDB0a1t4H0bfveuURWegx-uk5lspP2D16rYRjQ69DeipOU5iabznGYOaZJ8LGwzrRHrREQqWGUYirlnRVXmX2iGWCrd04ddKDnL1Ra97uqYpofKYQ-upHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنت‌کام:
❌
ادعا: سپاه پاسداران انقلاب اسلامی ایران (IRGC) پس از تهدید و تلاش اخیر برای حمله به کشتی‌های تجاری و دریانوردان بی‌گناهی که از تنگه هرمز عبور می‌کردند، همچنان مدعی است که دریانوردان بین‌المللی باید تنها از مسیرهای مورد نظر سپاه استفاده کنند.
✔️
واقعیت: تنگه هرمز یک آبراه بین‌المللی است. سپاه پاسداران هیچ‌گونه اختیاری برای تعیین مسیر جهت تردد آزاد و باز ندارد. کشتی‌های تجاری همچنان با حمایت نظامی ایالات متحده از این تنگه استفاده می‌کنند. از اوایل ماه مه، نیروهای «سنتکام» (CENTCOM) به عبور حدود ۱۰۰۰ فروند کشتی و ۵۰۰ میلیون بشکه نفت خام از این آبراه باریک کمک کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/69200" target="_blank">📅 19:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69199">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🇮🇱
یک مقام ارشد اسرائیلی:
ایرانی‌ها سانتریفیوژها را به «پیک‌اکس» (Pickaxe) منتقل کرده‌اند، اما اسرائیل از انجام هرگونه غنی‌سازی اورانیوم در آنجا بی‌اطلاع است.
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/69199" target="_blank">📅 19:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69198">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNX_bokSQAccR6kVHVtR474LHqOT503rw5_BHNFmPDgh-9onXXhj4aWTaYYIJJLk4BkUNuNCAoi0ESrGTI_mbG5uYdXIYrkXoAp1m56DaK3aG1PmlwP2bbO_NU3EKuf4dfvjRnALafAdSojIP13HA6vouFLQojtPpJBZ2AAQ24ntS6WIZ3qD_e0008met0oMEqQ7lFkiPll4ydg8oqCOwMaGJXAwyLTnZtSc0Z-gnPFERsFsZu8X728rG1hnBNxmI5LD9rNVeE9x4L21LF54tyAxhtHqP9iTt23U4sQHYh7VFkg_fRCCgnMXgQqA6koJV6qwBnS8Bl6C_aCwdyXl0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باراک‌راوید:
معاون رئیس‌جمهور، ونس، روز سه‌شنبه با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار کرد. یک مقام اسرائیلی اعلام کرد که هگست، وزیر دفاع، امروز با نتانیاهو دیدار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/69198" target="_blank">📅 18:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69197">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MycRyAoWngXUzyWj0oKSRjEdj5Ia7IYP1qltZbNyVIOMuNAYJqcMe6smIG2tHabEUl8DjYhIyHs-uQ9C9y-Z0IO96hquwxW_mVdV8putds-RXuGe8UJQcRf6o8yfYwa2wqbnr4Rh4wpLwtu6h50IBrmfvbs623i0zqP8csCd29jsp2KHsf3XN_yCjT7LHKVM5eVtxGxJdBTTX3Mq88izNe0xZWpKpTDhKxbkU9qe6AFqX33erP-wh4PPp_IQu_PgTd7-nxjlkI3_x0Z0CZPRH6B_wJRcw50twa3whNPwQ1rpDF3IaKh45Efme3dPLmrzzfVXFDvar95UPql_Xg1NHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تلفات حمله مشترک آمریکا و عربستان به حشدالشعبیِ عراق تا اینجای کار؛
- 20 کشته
- 32 زخمی
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/69197" target="_blank">📅 18:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69196">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5BUkmqrRa0MpGi5ErXFKI-wILaVTYNDACrYEzty5lLiIfhJ28SgufF_b0M21RRnsrAM3lm5ZXFziEYt0wakRTbOyhjd3cHDZ8HtfB4VVndnDijytM9DZnpXjkfZ3UZczy3WeQsxDHah8z-20Gi61rDnKBVrjuPTNVqPgWDiWDdSrp8eam1SDkn9It56TYRWe2EhfpCuM_2Al4MMglpBMn5Mxp8lF9cm4dyuKza_KmPlZ8FhQMPLFP3X1hAoDIgJ-xwoAt1htOvI6FKgAQ0U_l0zmKyRjfEU3dHoauQkLoagCDLHW8Wg8U1qpwOS1njgQdxN6PqC0tLsQ7ZRWeNJ3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🇷🇺
پروفایل عجیب پاول دوروف مالک تلگرام در واکنش به تحت تعقیب قرار گرفتنش
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/69196" target="_blank">📅 17:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69195">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b07d2f0b1a.mp4?token=T-a4B4LICphF-fuepJ8qVXVMUJsDcimtEl20oCpu0wYxHEfO_B5GpefiCEx5Oawt18OS3wSgVhZTrpbZWfNtDH-1CxVQsX8nrPPG8TE5JwZaFgn9hs_RKIDvjVbI1_L97SBdKZpdTlwiK_N2YVXRRwCBku50IYWbutlbZDKXwnDvYUlOoadMLnwX7k9ZXrvQGBM_qnp_pr0_5h6iqVpfdXac-kXSk160W3B4a24QsrOmATIyskX-EjLHFK4-ExJedHOLKfy_hEBWFMX3gVv3jdk2-U3WnALVp52wFUBpN9MIbXnWy5N0IY1U9KSPiiI0apYQUAeywlDDsicnTUYkTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b07d2f0b1a.mp4?token=T-a4B4LICphF-fuepJ8qVXVMUJsDcimtEl20oCpu0wYxHEfO_B5GpefiCEx5Oawt18OS3wSgVhZTrpbZWfNtDH-1CxVQsX8nrPPG8TE5JwZaFgn9hs_RKIDvjVbI1_L97SBdKZpdTlwiK_N2YVXRRwCBku50IYWbutlbZDKXwnDvYUlOoadMLnwX7k9ZXrvQGBM_qnp_pr0_5h6iqVpfdXac-kXSk160W3B4a24QsrOmATIyskX-EjLHFK4-ExJedHOLKfy_hEBWFMX3gVv3jdk2-U3WnALVp52wFUBpN9MIbXnWy5N0IY1U9KSPiiI0apYQUAeywlDDsicnTUYkTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔞
ویدیوی وحشتناک از یه حرومزاده به اسم «نوید زیادخان قره‌داغی» داره همه‌جا پخش می‌شه، تو لایو اینستاگرامش چند تا خانم رو خیلی بد کتک می‌زنه و کلی بهشون فحش می‌ده.
هنوز دقیقاً مشخص نیست چرا این کار رو کرده و اطلاعات موثقی بیرون نیومده، بعضی‌ها می‌گن دخترا رو گول زده و برده خونه
⚠️
ویدویوی کاملش ده دقیقه‌ست اگه خواستین می‌زارم ربات ببنید
🔗
🔞
مشاهده ویدیوی کامل
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/69195" target="_blank">📅 17:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69194">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czrVqqFWjtdfPIgvGzUiYT2jcyD1s5TLFmmPkm42TnjfI3rs6JajebJzsPcpC-zVl_8vnxNqhhuUGTYZccnRuxDnuDRpqxNSm8DVj_Q0zS2IfnEJDTRDr8r1w74QTvxQ3s81LnAhO0EO_EYzbcwRjdDFzN7AeXJMEcyk3xbeHUspQYy7YJ664jEmAAluQxm7wl8hGLIcHVkZnfZFxjzjifkuIpQeXJZ_sjvEuCWbVV07cmxd9o-hO3djJz32czoa15uf0qq-kvbZu7lRjTP81GQY8KQD_9wsX-msG_pM13irT1zFJHpos57jbc6Spqr7Uw0ls5nn-VoDE3VFJdzL3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیروی هوایی ارتش جمهوری اسلامی   اعلام کرد بقایای پیکر امیر سرتیپ خلبان مجید کاظمی یکی  از  خلبانهای  2 جنگنده سرنگون شده Su-24MK که توسط F-15Q های قطری سرنگون شده بودند را در خلیج فارس پیدا کرده است و از سرنوشت ۳ خلبان دیگر اطلاعی در دست نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/69194" target="_blank">📅 16:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69193">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9f57d9f95.mp4?token=o0hf31UDR4vAvJi8fWk4DKLiOirMAlhmlS-Apq87P_6q_W6JatOfbv08I3i7d2l4wcq7l-jJ4iZ3nEJY5Ity_nQuNyv3lCzr7uDERsUS2LfaESZ4TxdV6Pt73pRKec4GCGpr84mr_Zj1BYO2PxvaupWGpGmkmXRVabUGWvCfXUf-3ri8xYPn2L_AGNWHsFCHsBrcR2Vtnfxqv14DeDQ3xBuJT6vMsesN8OCfOY5uelGpF16hC9DZ7FC2DS6Z-33JnRo2afu3cqhoWj3jycEv7eGQ6kEU-gqmydCtRVADugdrxA73dgfy5mYcklJLIuqFcHDw5mdXJHbCcBDFA19c_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9f57d9f95.mp4?token=o0hf31UDR4vAvJi8fWk4DKLiOirMAlhmlS-Apq87P_6q_W6JatOfbv08I3i7d2l4wcq7l-jJ4iZ3nEJY5Ity_nQuNyv3lCzr7uDERsUS2LfaESZ4TxdV6Pt73pRKec4GCGpr84mr_Zj1BYO2PxvaupWGpGmkmXRVabUGWvCfXUf-3ri8xYPn2L_AGNWHsFCHsBrcR2Vtnfxqv14DeDQ3xBuJT6vMsesN8OCfOY5uelGpF16hC9DZ7FC2DS6Z-33JnRo2afu3cqhoWj3jycEv7eGQ6kEU-gqmydCtRVADugdrxA73dgfy5mYcklJLIuqFcHDw5mdXJHbCcBDFA19c_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره حمله اخیر ایران به اردن:
این یک حمله غافلگیرانه بود. نیروهای آمریکایی تنها چند دقیقه فرصت داشتند تا موشک‌های ایرانی را رهگیری کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69193" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69192">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c969cbc6b9.mp4?token=axBO2XWuaCc8uJ1rkPCrz8s_6Yo1TVdnQWZofAQIpAv7PLv9-fzqKGda0HcQ2yyvzcd53FLDbe_RBbtu2gHO4j6Yz6y8gFLtuI13YddLgmxzwv5Ut5uENZ9fNEHtStj97aBz3pIX5EZCyOdWouPwbHinzvA3y-Fr62UQhCA7gJmGTQL6FiBUUs-_Ugl8iT9G3ehTKJGsvMp_yNEkXiQIQ-A-1JU0sfUWtf9gknRMh77DS6MzW3afgFbrb8LIKqFOccGYvy3xmDgOqG08qSl4u74JsZZEWQgvJeZ6jZaUqgvwkp0-1OF0_Tc1vSQXtyP3NiSHbRkmdwGF76nLaj49Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c969cbc6b9.mp4?token=axBO2XWuaCc8uJ1rkPCrz8s_6Yo1TVdnQWZofAQIpAv7PLv9-fzqKGda0HcQ2yyvzcd53FLDbe_RBbtu2gHO4j6Yz6y8gFLtuI13YddLgmxzwv5Ut5uENZ9fNEHtStj97aBz3pIX5EZCyOdWouPwbHinzvA3y-Fr62UQhCA7gJmGTQL6FiBUUs-_Ugl8iT9G3ehTKJGsvMp_yNEkXiQIQ-A-1JU0sfUWtf9gknRMh77DS6MzW3afgFbrb8LIKqFOccGYvy3xmDgOqG08qSl4u74JsZZEWQgvJeZ6jZaUqgvwkp0-1OF0_Tc1vSQXtyP3NiSHbRkmdwGF76nLaj49Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ به شبکه فاکس نیوز:
گروه‌های شبه‌نظامی مورد حمایت ایران در عراق، یک آفت جهانی هستند.
من در حال بررسی صدور هشدارهای بیشتری علیه عوامل نیابتی ایران هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69192" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69191">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
در پاسخ به حملاتی که اهداف آمریکایی در اردن را مورد هدف قرار داد، حملاتی علیه ایران انجام خواهد شد.
ما ایران را به شدت مجازات خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69191" target="_blank">📅 16:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69190">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZNIaNZz0Oy6Lm9J6RG6BdrpZiRj5dD1OBhv766NuxrZKYvBWbcR4Nn7TOZIXz5yusN3Wvr3s3rYY_al4h1kQtitZvIJ5vonjj24XYBBVKFSEOdOmJCJFmmG6TXVBRbeUqFW0w8CVTktKgmrYz6NBe7cLO4Zj7FAtaw_HFviIf7e9KM0M2VSmK8avbf061BeDV49m1j854gIw0ca1QTSoOgE_f1S-GBOu56YEExnqo-iGk7-4N_XUKxPV7UxSXV7mRjDoGACS2pbZsp-uooFFSijSa-SDgdAqIuCSWvzC4NxRKRHrYlmsDu6dbOVv98pkGsQlptRwmbz5nmxkUB-pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس تنش های دیشب، قراردادهای آتی نفت خام آمریکا ۴.۴ درصد افزایش یافت
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/69190" target="_blank">📅 16:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69189">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/640b7bb0a7.mp4?token=rWvjkMjZH_yH8hutcze4z4ihEwq0mTWfe87xGKHgpRpJYwmXD5bFK9iZT7fiP5pMmTqB5qdGK75YcP-W4_ha4ety-QQfTF_XQlj6yYLqI_gd__SLlt7y-1BiNVL-iNLihVAGRW744RpIDSVXfbVzhlKgw7IXCTUFYwUZVw77R_wrWzuPeFc_cDvgZCTUbpCck7Eqjw1ZCU9tf4qUwZWjIMNRsVJTsX4374Zm6r_B3ASkYTbK8zzU67llcoaYHyhSEwYTFnrb3sv6u7uSFMbj_4tPr2c7zUDR18fmhNdcw5rzvR5Sd_GiYrHGfyzJcJgDjqX1sc1ZdxDiQd-XmfZnBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/640b7bb0a7.mp4?token=rWvjkMjZH_yH8hutcze4z4ihEwq0mTWfe87xGKHgpRpJYwmXD5bFK9iZT7fiP5pMmTqB5qdGK75YcP-W4_ha4ety-QQfTF_XQlj6yYLqI_gd__SLlt7y-1BiNVL-iNLihVAGRW744RpIDSVXfbVzhlKgw7IXCTUFYwUZVw77R_wrWzuPeFc_cDvgZCTUbpCck7Eqjw1ZCU9tf4qUwZWjIMNRsVJTsX4374Zm6r_B3ASkYTbK8zzU67llcoaYHyhSEwYTFnrb3sv6u7uSFMbj_4tPr2c7zUDR18fmhNdcw5rzvR5Sd_GiYrHGfyzJcJgDjqX1sc1ZdxDiQd-XmfZnBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو مراسم ختم اکبر عبدی، مهوش وقاری وقتی داشت درباره مرحوم عبدی مصاحبه می‌کرد، یه پیرمرده تصمیم گرفت وسط مصاحبه باهاش یه سلفی بندازه
🌟
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69189" target="_blank">📅 15:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69188">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHaZ4pTdSy8L4GDtzgq4GnqLZhHPz0n8DygUwG-GZjHu90UeeXueUQf1FbK35nA2hz4WnU2e7MS9NPvbrPamhfVP8FBnsmSAjmqsFmejPSur9ROAz3ynT_T8O58XYYWelTFf3-OLRdvQSqDQALz40pq9XMRLOB5ErZUseDcQa97p0F_R-_LENZrL0VYP-1NlEZjbbjiyWP3WZObfwCcRtLJ9JNgsJDprDUJpT5q0S0BNALmi_cU55E6SSf3U_EPblMYThI2y_u0-IDXW0Q721w_aTjxipSy--jD9A-IW0QM5aVCunJ1z69KunBYP-PoQd0MNtbS1-odawd_NrXRVhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇨🇳
🇮🇷
رویترز:به گفته منابع، ایران ظرف چند هفته آینده سامانه‌های موشکی دوش‌پرتاب چینی دریافت خواهد کرد.
۲۹ ژوئیه (رویترز) - سه منبع آگاه از این قرارداد به رویترز گفتند که انتظار می‌رود ایران ظرف چند هفته آینده، نخستین محموله از مجموع ۴۰۰ دستگاه پرتابگر موشک پدافند هوایی دوش‌پرتاب ساخت چین را دریافت کند؛ اقدامی که در راستای بازسازی توان دفاعی این کشور در بحبوحه مناقشه با ایالات متحده صورت می‌گیرد.
این خرید که ارزشی بین ۶۰ تا ۷۰ میلیون دلار دارد، یکی از بزرگ‌ترین اقدامات شناخته‌شده تهران برای تقویت سامانه‌های پدافند هوایی کوتاه‌برد از زمان آغاز درگیری با ایالات متحده و اسرائیل محسوب می‌شود؛ درگیری‌هایی که کاستی‌های موجود در توانایی ایران برای حفاظت از تأسیسات نظامی و زیرساخت‌های راهبردی را آشکار ساخت.
به گفته این منابع، این قرارداد شامل خرید ۳۰۰ تا ۴۰۰ سامانه پدافند هوایی قابل‌حمل توسط نفر (MANPADS)، از جمله موشک‌های چینی QW-12 و FN-16 است.
این قرارداد با شرکت «ژونگ‌چینگ بائوشانگ اینترنشنال اینوستمنت» (Zhongqing Baoshang International Investment) امضا شد؛ شرکتی مستقر در هنگ‌کنگ که به گفته منابع، به عنوان واسطه میان طرف ایرانی و تأمین‌کننده چینی عمل می‌کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69188" target="_blank">📅 14:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69187">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9VMf0_B5gW-_LuUj9FhdqtXFWmoKIH2SaJy4acBNptYlPCDeh6MBD3Py_aR83uIR4syf8VExSXuE1MNyXPnAtLCRqEQQ3HZJyy3ved22CVPOzZL2Fj5GW_4BTWTsb3Ro8axKQA5Cg3vVJmYnyD19cT1yOetNjr5_SibTkr9mXT9nerKrr0HXIe1R38tUKy-eoior6LB9UnQYdzqUHQ2IBHtJCiKogv68QkLiYeZVmG4kKHHhS7scypVpt7yH_UKEee3LxGU_V4f30tHkUoWZAJHN5j2CoE8E_toUrqH-ZVQ0M5mgLqWELO7QsCEtR7h_I_TLhKUFYqPD5_kWiovnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عباس عراقچی:
وزیر خارجه اوکراین به من اطمینان داد که
حمله به کشتی ایرانی عمدی نبوده
و اوکراین هم
دنبال تشدید تنش نیست.
ایران هم قصد تشدید تنش نداره، اما
به‌صراحت اعلام کرد هرگونه حمله به شهروندان یا منافع ایران غیرقابل قبوله.
خسارت‌های واردشده هم باید جبران بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69187" target="_blank">📅 13:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69186">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78f023144.mp4?token=X2996PbZI241PaIn25W1YiTQPgIDmu2uJGDsM5ATid3YVhcTMxyFBBk9SpiAZ_iqMIQDOb6mLm5yMQyQpshqX0vpMWiUvR8Rf1MQmcXqIDg0gGwXL59Y0xJzMEHvWu9sAEeWXJoPa_DiJuZXG5j9qGFavj90O2Z4_B7ECM0wnenmK381cihqNm7mFHpJDxoigK03cfULKZC_gSM4ayOEv09_oC1kMZ_qebWDxk3ISeR09kV129BCao6fKABL4q398JM48RnGN6MuQ49oF_4KpqXIUsR47wIdke8r0oNfLCeMPvfR-DVd82qQWQ3hCw3DAeihZf6QO3nRDTAiDcCVxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78f023144.mp4?token=X2996PbZI241PaIn25W1YiTQPgIDmu2uJGDsM5ATid3YVhcTMxyFBBk9SpiAZ_iqMIQDOb6mLm5yMQyQpshqX0vpMWiUvR8Rf1MQmcXqIDg0gGwXL59Y0xJzMEHvWu9sAEeWXJoPa_DiJuZXG5j9qGFavj90O2Z4_B7ECM0wnenmK381cihqNm7mFHpJDxoigK03cfULKZC_gSM4ayOEv09_oC1kMZ_qebWDxk3ISeR09kV129BCao6fKABL4q398JM48RnGN6MuQ49oF_4KpqXIUsR47wIdke8r0oNfLCeMPvfR-DVd82qQWQ3hCw3DAeihZf6QO3nRDTAiDcCVxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بسیار کسان به این سرزمین روی آوردند ولی‌ همه آنان رفتند و ایران ماند؛
جاوید و پاینده ایران
🫡
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69186" target="_blank">📅 13:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69185">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuQfLyQa76fPWCwu5JFDBEu5ufsePzg4B0sWoEDceRPmUwECyevkcubRKElyU6SGU5BAHaDr5hmrB903DBXj59UMQ0C-1Efdra_bQrL6mY-MxxkGmIP7PTkLOfMWtDNdhbpcypfnnXvVndXtww5NtSHtc4Hwjjh5exkFNnATEB_N_NDZ5LEQvBKeS4idLsxZ67YE43o80pqGHzVU9YMLfWcAZPA-QjIWGJZv7qee55fu1OwkFgNK0ofZy6bt8DkdQsxlrgZRrQOMtMZdYR9PwVCSyPfSkrRx3xA4Y0253zKmp2mJ_sX7ZfFds1dmXiw8XlPldr6PO5lG121PJ40ySA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ایران پیشنهاد عمان برای مدیریت مشترک تنگۀ هرمز را رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69185" target="_blank">📅 12:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69184">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f04q5kr_inKjUkXA-fAxRCi0JXJ8pFOnyfaxpcUVLtAEaapfW6xO1J-ybL8cy7MV61pV1JjZYBX3_spztVUk4ry2-YukezZvrzcrmILosGPB30bOq99FFnpAbtWeB_FnibaePcLA8ou8LplY6mL6WE21iOUTs2c9XBmgM-dICtCsVKqOHhyElA7Iw2HWO3ljXLNOJa_hmLcZBtsghbWMwsl7kjL__FRCH_D-DFw27yZbJpe668F5RC59DMEFkxscUy2Z5PrKjkRH3aQBNPP3QhzrcObB4NuYt-ekpZfJQjsOQOR9SR9ruT6Y4R3kruCnCisqmYDap9SnsURVsSW1uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
نایا
:
موشک‌های ایران، همسر دوم رو لو دادن!
یه زن اردنی میگه موقع حمله موشکی به پایگاه موفق السلطي، متوجه خیانت شوهرش شده
😳
ماجرا از این قرار بوده که هشدارهای یه
گوشی دوم
که شوهرش داخل کمد قایم کرده بوده، موقع حمله شروع به زنگ خوردن کرده و همین باعث شده بفهمه اون گوشی رو برای ارتباط با
همسر دومش
استفاده می‌کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69184" target="_blank">📅 11:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69183">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8245e9f66a.mp4?token=nDyxe39lrg97YNMLWT-XY4i9OL0qdyr3HQPxFyBLWRxyA_aDZTHgDCyD-xs8FVw9JlNU8DbaWLBuFfnpqlVCwK0DLJFBTXQheGw6KhqokszQgWYtPebsw81arUbh6026juJHHP9aBrSodnfDn7qF39TfIBvTVLte5Zq0TOz0Vw1rxwNww_eFLCMqJjsrT-rFOO-z-JarDrs9RZbjABfS3gsT684JtRgh_42cicc2DteDs-mRYD2muRkc34BOEv30PnPhXJh0ICGcydeTBwXYm26pKz4hOE5h9IfWtlPv-7UQtbyVhDLWlYsOxK7WhWbrGPoNF_k2AdXsTFnk2jnV_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8245e9f66a.mp4?token=nDyxe39lrg97YNMLWT-XY4i9OL0qdyr3HQPxFyBLWRxyA_aDZTHgDCyD-xs8FVw9JlNU8DbaWLBuFfnpqlVCwK0DLJFBTXQheGw6KhqokszQgWYtPebsw81arUbh6026juJHHP9aBrSodnfDn7qF39TfIBvTVLte5Zq0TOz0Vw1rxwNww_eFLCMqJjsrT-rFOO-z-JarDrs9RZbjABfS3gsT684JtRgh_42cicc2DteDs-mRYD2muRkc34BOEv30PnPhXJh0ICGcydeTBwXYm26pKz4hOE5h9IfWtlPv-7UQtbyVhDLWlYsOxK7WhWbrGPoNF_k2AdXsTFnk2jnV_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، درباره ایران:
من نسبت به این توافق تردید دارم و این را آشکارا می‌گویم؛ اما تنها راه دستیابی به آن، درکِ درستِ ایران از این جناح‌های گوناگون است. به گمان من، تفاوت این جناح‌ها بیش از آنکه ایدئولوژیک باشد، ناشی از ارزیابی‌های متفاوت آن‌ها درباره میزان سرسختی ماست.
کسانی که رئیس‌جمهور ترامپ را بسیار سرسخت می‌دانند، معتقدند که «نباید با این فرد درگیر شد»؛ اما کسانی که تصور می‌کنند «نه، می‌توان آمریکا را بازی داد»، معمولاً خواسته‌های بیشتری دارند. با این حال، به باور من، در نهایت آنچه تعیین‌کننده است، عزم و اراده ماست.
عزم مشترک ما این است که اطمینان حاصل کنیم ایران به سلاح‌های هسته‌ای دست نمی‌یابد تا بتواند با آن، تک‌تک آمریکایی‌ها را تهدید کند.
به اعتقاد من، رئیس‌جمهور ترامپ در این زمینه کاملاً قاطع و صریح عمل می‌کند و من به همین دلیل، عمیقاً برای او احترام قائلم.
آنها باید بدانند که اگر به ما حمله شود، با نیرویی وحشتناک پاسخ خواهیم داد.
آنها به خاطر آنچه که من گفتم، در دورهای اخیر درگیری‌ها به ما حمله نکرده‌اند.
به عملکرد امروز این رژیم نگاه کنید. این رژیم به هر کسی که در دسترسش باشد حمله می‌کند؛ به عربستان سعودی، کویت، بحرین، امارات متحده عربی و دیگران حمله می‌کند.
این رژیم به هر چیزی که در برابرش باشد حمله می‌برد و ده‌ها هزار نفر از شهروندان خود را به قتل رسانده یا دچار نقص عضو کرده است. این کاری است که رژیم ایران امروز، بدون در اختیار داشتن سلاح هسته‌ای، انجام می‌دهد.
حال تصور کنید اگر آن‌ها سلاح هسته‌ای داشتند، با جهان چه می‌کردند. این همان چیزی است که باید اطمینان حاصل کنیم از وقوع آن جلوگیری می‌کنیم؛ و گمان می‌کنم ما در این باره کاملاً هم‌نظر و مصمم هستیم.
مایلم کسانی را که به دنبال ایجاد تفرقه میان ما هستند ناامید کنم، چرا که من و رئیس‌جمهور ترامپ در این مورد کاملاً با یکدیگر هم‌عقیده هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69183" target="_blank">📅 11:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69182">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be2265e1ef.mp4?token=s17UTf0uQ0KY4sxDJNQSgxbiUEAIpuo0lvc8AMLPihpfM2UiZGsPDExqZDPRayt7cTpzMQ997hDLMeX_qnQ6V7sh8s6DW4F6hzksKdhHXbgWHi1znbNyIIbEJlcGizCmvdRmB2nR3ynZNMdsO2Nwz9GP4gfwyXaPohADX5y67kBzWklbQMLMC0BbMoIe50qsrtojDfC8vn9OmcsA6QNi00iC9rjnj2qgi7BONQmmayDJ09Qvu6tr1xqrySbpldgis3n-tb4QWl5eFJH5Ie7mI6Qh5eb5uR-rF42i_TE1pM3DwNsmUEt5DO5x_jCnDZsNb0Vp9BMKlh5mwOaP4BNHSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be2265e1ef.mp4?token=s17UTf0uQ0KY4sxDJNQSgxbiUEAIpuo0lvc8AMLPihpfM2UiZGsPDExqZDPRayt7cTpzMQ997hDLMeX_qnQ6V7sh8s6DW4F6hzksKdhHXbgWHi1znbNyIIbEJlcGizCmvdRmB2nR3ynZNMdsO2Nwz9GP4gfwyXaPohADX5y67kBzWklbQMLMC0BbMoIe50qsrtojDfC8vn9OmcsA6QNi00iC9rjnj2qgi7BONQmmayDJ09Qvu6tr1xqrySbpldgis3n-tb4QWl5eFJH5Ie7mI6Qh5eb5uR-rF42i_TE1pM3DwNsmUEt5DO5x_jCnDZsNb0Vp9BMKlh5mwOaP4BNHSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این خانمِ باردار رفته بود سونوگرافی ولی به دکتر سپرده بود که جنسیت بچه رو لو ندن تا اینکه با این صحنه‌ مواجه شدن؛
شومبول آقا پسرشون انقد بزرگ بود که تا دوتا اتاق اون‌ طرف‌تر هم همه فهمیدن بچشون پسره.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69182" target="_blank">📅 10:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69181">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTGZyj8yLFc8tJ52ej5C2aIR8eLS-flrwkPArKO1nSj_64cv4J3N3ErQe_vXPXoCi4qRYRny3BtG1rKgaYy-76M_8tw1f5ltJctqAD93n6f25xJ4uMc2jaaN6kZN_U4qPRlUUVitfqqnKQ6uCAvOzmX1AHEQ10HT5PMCm1SYJ3G-eagNmpy40PUF8HCIzTslbcimV-RyVrpQj8WRdrVMme4ZelcwGu-rGXI1E9DPp-CxpyvSWwQk5tSibS53hWDN2iJjymLwfedb2dAVcKgxpJy3ypwHJY3DKva93lCd6rtxRHPLdKrpoyu80f89m3rLN4oj-ZpUdhWPUM1Uv33MfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
نیروی دریایی سپاه:
سه کشتی متخلف میخواستن از تنگه عبور کنن که مورد هدف قرار گرفتن.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69181" target="_blank">📅 10:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69179">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b39375dc32.mp4?token=p7sZ2a6b6ldc_K5tChMbhCXxY9AcxYQVPDpFg7DSSPWMuetoBqXhbxsEswZPYKqEisxr8qSOhQChbaoA_5_QIeqTs2pz9cWG3j1DIgZF1d4ZVKucaM8QE2aSdxkISjscTL0T8yMxhZu-nq7kP8FS8l99vvdO2vowWBllmHRudfHVMrITv9_owJfH0KcaUogXhJOOFgek6HH6607p5BwypkuOAUlIqcpL-dxMLKb8Q-MCVTLw5TDR_HM-yA5g5RZMYDQstrZnwT_onNst6twc2QdVCEV0UHc7nMX1SJ54-1RrD79DTkxYmFuCeB5G0Rnp3CNPwim5odrUecuBRvFmMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b39375dc32.mp4?token=p7sZ2a6b6ldc_K5tChMbhCXxY9AcxYQVPDpFg7DSSPWMuetoBqXhbxsEswZPYKqEisxr8qSOhQChbaoA_5_QIeqTs2pz9cWG3j1DIgZF1d4ZVKucaM8QE2aSdxkISjscTL0T8yMxhZu-nq7kP8FS8l99vvdO2vowWBllmHRudfHVMrITv9_owJfH0KcaUogXhJOOFgek6HH6607p5BwypkuOAUlIqcpL-dxMLKb8Q-MCVTLw5TDR_HM-yA5g5RZMYDQstrZnwT_onNst6twc2QdVCEV0UHc7nMX1SJ54-1RrD79DTkxYmFuCeB5G0Rnp3CNPwim5odrUecuBRvFmMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
کاخ سفید پست جدیدی از ترامپ با متن «کار این جنگ رو یه‌سره کن» منتشر کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69179" target="_blank">📅 09:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69178">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/305091e76a.mp4?token=H93O0JEj76MgxC0rxVjAOI0a1eLKb6_QMPmHLVu4rzShVlAbLmFmNrUANQ0LtYiQUnIWVG0Mhr3hqK7ibPBVdOCs1GnHqFisE716lYMbXn0Qw-ixyh7vtZQybb0ddx9P47UGnh2gzbsxdQzia-b4W9_He4qNAJ5EQLxqwaVbTpo_DmEHmBKAavVON8zOQKlx2SUUUqgXRli6GBZPlxUkxOS_K9v-bCURAL6xoHgaH0USZ7OuHGuMnuzizHuS4LrBi8J1xVdAez-o-j0kXvslX3ZyLVnb6d77F0RBmaqIVJbShZctf4XnHJE3rsNxiW14eE1fbbf0gKJT1YHMizD9TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/305091e76a.mp4?token=H93O0JEj76MgxC0rxVjAOI0a1eLKb6_QMPmHLVu4rzShVlAbLmFmNrUANQ0LtYiQUnIWVG0Mhr3hqK7ibPBVdOCs1GnHqFisE716lYMbXn0Qw-ixyh7vtZQybb0ddx9P47UGnh2gzbsxdQzia-b4W9_He4qNAJ5EQLxqwaVbTpo_DmEHmBKAavVON8zOQKlx2SUUUqgXRli6GBZPlxUkxOS_K9v-bCURAL6xoHgaH0USZ7OuHGuMnuzizHuS4LrBi8J1xVdAez-o-j0kXvslX3ZyLVnb6d77F0RBmaqIVJbShZctf4XnHJE3rsNxiW14eE1fbbf0gKJT1YHMizD9TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی از لحظه‌ی حملات عربستان و آمریکا به مواضع حشدالشعبی عراق تو استان واسط، که توسط دوربین مداربسته گرفته شده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69178" target="_blank">📅 09:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69177">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74196ace24.mp4?token=a88focWxGQYJePY4P9QOfWmSPsazUQahSzXEsUPuXnTrOTb5mTTAsuqvXq7iCJtwZwhY2ZGkXUYTwtVCd6QF9BIgWYgHloXndKbkbh2JcWauaglvAAJUvCvOLClqc6Zm87a5VOvzEgsFu9pcq0gX0jpc_EGzOECKw1WfNnH4m_0YsoH78oBvETKRuhoAhZeyRIOdjMNphBx_WChDLuCFpeOXzu2Pls6VTG6mSSx-APnfjQZmZqbMTqcigO9ILYribd72-GyJApjuospBxeY46ryVhdiMqaYAZWFPuQFCSwx969w4a8iFWbGYa50LLKe-E5wx-nnPgHGcU3oZ5ncbAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74196ace24.mp4?token=a88focWxGQYJePY4P9QOfWmSPsazUQahSzXEsUPuXnTrOTb5mTTAsuqvXq7iCJtwZwhY2ZGkXUYTwtVCd6QF9BIgWYgHloXndKbkbh2JcWauaglvAAJUvCvOLClqc6Zm87a5VOvzEgsFu9pcq0gX0jpc_EGzOECKw1WfNnH4m_0YsoH78oBvETKRuhoAhZeyRIOdjMNphBx_WChDLuCFpeOXzu2Pls6VTG6mSSx-APnfjQZmZqbMTqcigO9ILYribd72-GyJApjuospBxeY46ryVhdiMqaYAZWFPuQFCSwx969w4a8iFWbGYa50LLKe-E5wx-nnPgHGcU3oZ5ncbAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
خداییان، رئيس سازمان بازرسی : بعضی تراستی‌ها خیانت کردن و با پول رفتن!
یه تراستی (شخص یا شرکتی که حکومت بهش واسه نگهداری یا انتقال پول، اعتماد میکنه) فقط 200 میلیون دلار پول مملکت رو برداشته و از کشور خارج شده!
معادل38.1همت!
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69177" target="_blank">📅 09:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69176">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اگه فوتبال رو فقط نگاه نمی‌کنی و تحلیلش می‌کنی، این کانال برای توئه!
⚽
🔥
تو این کانال هر روز داریم: تحلیل تخصصی بازی‌ها بررسی فرم تیم‌ها آمار مهم قبل بازی پیش‌بینی مسابقات مهم نکات کاربردی برای فوتبال‌دوست‌های حرفه‌ای اگه دنبال تحلیل واقعی و بدون حاشیه‌ای،…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69176" target="_blank">📅 02:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69175">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=h7Oc7BG1vpaTqbWeLo4WC1ycyEmwKuWsICOYU_EwVolC_14XMzxC8h_6_nbakPaGu2y3Iz2oqOpeYtZTjAzgbhJ4lj2S2oMKe2ExIVBpeB6Of0egKDgAYOKATPqvuXRnSV-21yov36c51LxhTqRfZEtKRGHpxNKPFXOIQRCjVpEEteSffWA7pR4N02NbyhfV2HCyiVgvZz6VMqyzT1pKHVKDwJ1KZts9XcjQGnEICBK2BsG3vqxQGeCYGMjbGuLyE2mRqA7oW8GMp00ntsPbMUzPSKVZbooDJenxOcytdwMkZKil4YEeyJ7B3BFPFbJQmjcSkL-2-5yAmFEMzyAMeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=h7Oc7BG1vpaTqbWeLo4WC1ycyEmwKuWsICOYU_EwVolC_14XMzxC8h_6_nbakPaGu2y3Iz2oqOpeYtZTjAzgbhJ4lj2S2oMKe2ExIVBpeB6Of0egKDgAYOKATPqvuXRnSV-21yov36c51LxhTqRfZEtKRGHpxNKPFXOIQRCjVpEEteSffWA7pR4N02NbyhfV2HCyiVgvZz6VMqyzT1pKHVKDwJ1KZts9XcjQGnEICBK2BsG3vqxQGeCYGMjbGuLyE2mRqA7oW8GMp00ntsPbMUzPSKVZbooDJenxOcytdwMkZKil4YEeyJ7B3BFPFbJQmjcSkL-2-5yAmFEMzyAMeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه فوتبال رو فقط نگاه نمی‌کنی و تحلیلش می‌کنی، این کانال برای توئه!
⚽
🔥
تو این کانال هر روز داریم:
تحلیل تخصصی بازی‌ها
بررسی فرم تیم‌ها
آمار مهم قبل بازی
پیش‌بینی مسابقات مهم
نکات کاربردی برای فوتبال‌دوست‌های حرفه‌ای
اگه دنبال تحلیل واقعی و بدون حاشیه‌ای، همین الان عضو شو
👇
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69175" target="_blank">📅 02:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69172">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzFves7pYp5QH0vxfyCO4Y-S8mvAHT3HFMgh2eLQIHge-ha0l4ZY5BYALkdb-PHD753WVSG_QB4RNljJfjzeWR1EPlPALaWqmE94NP9-CA1D5ZciYd-68IWiHuINcMbsNlCNuhhX_deVGw_PZzJMWmLQROSRgEsD0dDQv_yqgk8mH18jstBOPibhyn4VyhMryGYgI9GZtpDVG-99zzAWnHiFZvxwEKgF607YIieuPhQxgKOFCm0I-RIY4iCN0ga2jr_ViHparYK4kkZ848HftvXPONqYDQKBZtem7zaw6c4yndqhcf3dLGiaGsiqkXnU6YTJMgh_Z37kHqDiUHl38A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
امروز ساعت ۵:۴۵ بعدازظهر به وقت شرقی، نیروهای سپاه پاسداران انقلاب اسلامی در تلاشی برای انجام یک حمله غافلگیرانه علیه نیروهای آمریکایی مستقر در خاورمیانه، چندین موشک بالستیک از خاک ایران شلیک کردند. تمامی موشک‌های ایران با موفقیت رهگیری شدند. نیروهای آمریکایی همچنان هوشیار و در وضعیت آمادگی بالایی قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69172" target="_blank">📅 02:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69171">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4px_G-eLizeSs8TH1BMHOpQjDLQtqFl35jfBcf6jZuG91gTRxs4cEI8K79Y8nWkc7lDx4sCTSnBs9SKaJIhocIDeW4CaWAGo-wIF6PIcF3yLAUSgRHMMaSaJID197PZbR6rp48u3kAqG7ZxRv4J9NVeb5qeTHyzbP0OcFlGWBT9fk4XnlaDS_5M0fz9o-Qt8CI1tULpnMNaeYu8I3Aw-NNbAlgPXWec5OhBkiukdnWfv9A4K5hf2ju6HEIdyjTgJhGJfY6u6SPvKMNqXLcEfFnzJmEp8k_olSMsUul8WWP2iou3lkZHD1tWUajIVwjAs2wYeb_9Fcd687Rk33uh7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران برای جنگ تمام‌عیار کاملاً آماده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69171" target="_blank">📅 01:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69170">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58608400cb.mp4?token=ahP-whn2zJ5kQkK_aw3Z_N4xfOLqXzoQlIKHySyLhG_CCGblTXuRPgJNf1xDwwsCnisfbWKmtPiAOf1K3r37-_N4K8dITWuLcS9OM8fBev7l-oa_jNkVLT07BJMSBaCIOwWXuqP65zdaWgN8ndPPUSNXfNWzoZ3Ah_nAGzPUd_TzoHeIhZPPdsN97MgTtQjWFQ1_xSNx8e_-KJSyORY2bpnXaD9FedEDH0x59UKuS_iNZrWMCnIh-A2N6lWyQ7Ir4GUdThYpw6XsyNeYS6kmtGQmipogJaC90Z81OPFp59mzYiZFtOJke8eWZ_kTKcM9nwTF1POUjkChI00uh1DtsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58608400cb.mp4?token=ahP-whn2zJ5kQkK_aw3Z_N4xfOLqXzoQlIKHySyLhG_CCGblTXuRPgJNf1xDwwsCnisfbWKmtPiAOf1K3r37-_N4K8dITWuLcS9OM8fBev7l-oa_jNkVLT07BJMSBaCIOwWXuqP65zdaWgN8ndPPUSNXfNWzoZ3Ah_nAGzPUd_TzoHeIhZPPdsN97MgTtQjWFQ1_xSNx8e_-KJSyORY2bpnXaD9FedEDH0x59UKuS_iNZrWMCnIh-A2N6lWyQ7Ir4GUdThYpw6XsyNeYS6kmtGQmipogJaC90Z81OPFp59mzYiZFtOJke8eWZ_kTKcM9nwTF1POUjkChI00uh1DtsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ خطاب به مجتبی:
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69170" target="_blank">📅 01:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69169">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXqwJdEvcREPpHgpEL-H8UU_fB5vrtQu5zEiIlpQL3VObbeUNEGuli6WgbXC4yOujZhvj6BRZMMHteAWuFBkCQgAH7Uzq3xCi0feEQCxW2oGyMLr8sNUndsKABC_gXs1KYs22LEKMXmwwCWlOemVf2CZEXZuCelUm8clks3UjbrBFqGR0CM7BYFOJzNALDbEXP8qtvoVqfsejtKURDf-L4IHhWZuBTaGwBYpRzZt_kQu2pmzr_1EUPSfD--SNy2JBXR5wj_Im7p2bmZNg50b6KU7Wsvsqil6Ucl81zzQjh1YVlrkUNDi3vOYaElpXumUcdU0UXjWAxQr4gnvMRZ_kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باراک راوید:
ایران چند موشک به سمت پایگاه آمریکا در اردن شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69169" target="_blank">📅 01:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69168">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
لحظه پرتاب چند موشک از خمین</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69168" target="_blank">📅 01:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69167">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRMiCboT9Z5gQ05FtjhYSBweJcxWDeCADso2euRD0CuqBxHzFvB5S42PWh_KD7DoXEWC5Gbl0AWcvvYsemDjbcoWAsqK1rhh_zX-ehtLppZRlVj6j9-7-9CJzeaWvnPeaGUrjSd9rihvZoK726lvzy_1ak8LV9kX5COIZP1MPT6vustDfSFFzHB47MOHyxul2EmZZ0QNJJYJfjKZeu3GYj1MjcMPxGUJnptvDXEDd65xBMKvZHk5hyUigmJGI6xiUp_DBcFfikzU6rx0w7TaG1SXmLdwVxXjIanfejHn1AQiWUyBe3RVsFDn7ffTgXjKWh4xrUF92ACq5rT64F2W_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای پهلوی در کنار یکی از طرفدارانش تو مراسم لیندزی گراهام
#hjAly
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69167" target="_blank">📅 01:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69163">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VYJ9NwMWYrLBCwmFg6Y2MOJoB7eyDDldBmPxNb3bi9bQsYjr1gT07maKPu5TPKRE7zSTPeIP2Y51bwsKsUszdNKqZ6BA-gMz7_hiXp6LufxNXJ6Hka38NLDMpajjBt3IxtproanepprwW4C67fA72DxVks0W-1P22QELDDJ1ydEgGiUgTwJkC8de3K4XTG0cMnRH7p8YkFrY68kJtAVBaxbPuwMZw5ly573yak5pNxo2Nh5UlPiJIjP06Vmymfzb2ioPdaEG-u5nB8g_MElv8GpSzbsUgv3k9Zo3Z-QfBD_eGZO-VY7L848NXw17pWuILOfIv9XND2bVPZD3BAluHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TSVKnySOb4iVOaaAK17Ng1SsRVk-iDZ_c1FZrIXFbmMtEq4AouOO2B7U_MMA_Ok35fyf7RL4LZaAfiap283uzuwvOi9eoSc43sFcj-bb7D_epbYfNUOGiG4QTEUfDCDsqk0dERRCTG06TccptUyDjRhK5zCHdAkojS0OQZuh75-VMCYq8g2t8ZhQSAfuSDhp3bNsXHjf9M2fPds3qZcXr-YOnMc_KuI4LqhO6aNfUyIW5I9_lbrljpyEYTP28PuXHL4jSt_2hFe3240caOwqQcBnDPcMq8o_ISI2JngZLasVDtRMNzSe28y69M7T2lrzP0lPzzw7WDAIKKnbloRk1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41f8819418.mp4?token=utjI-x_m-oAeLG5m0NV-VKzvbYYNNcOvsdp2fQxduutTJ7eYGB6YMfuSC72vSnbi-UlCys-qFzQBAwg-uhgFcHySZn2eBze8IfpEjwfeNI2ouJqqBkgRA0cr1irlEErW0-fiDDYPPu_-lWw8qNmWjW6pLpHDCBmxR2Df3HhHmmG-Dl4uBZVsyA0q9hu_cSyCxr675sK4ukP5nLvhSgqZz001SiUfBERJGaERC4QT5d6MbmgBBdUyQmZemG4gr7Nb6ZjcIWd734yq_C17MJavOV2a6a4-X97MG3M7JuR5w5JgLISA4J3L5FqIZrsLuZJ6iniCGAE_TMsucCAX8o_TTg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41f8819418.mp4?token=utjI-x_m-oAeLG5m0NV-VKzvbYYNNcOvsdp2fQxduutTJ7eYGB6YMfuSC72vSnbi-UlCys-qFzQBAwg-uhgFcHySZn2eBze8IfpEjwfeNI2ouJqqBkgRA0cr1irlEErW0-fiDDYPPu_-lWw8qNmWjW6pLpHDCBmxR2Df3HhHmmG-Dl4uBZVsyA0q9hu_cSyCxr675sK4ukP5nLvhSgqZz001SiUfBERJGaERC4QT5d6MbmgBBdUyQmZemG4gr7Nb6ZjcIWd734yq_C17MJavOV2a6a4-X97MG3M7JuR5w5JgLISA4J3L5FqIZrsLuZJ6iniCGAE_TMsucCAX8o_TTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
لحظه پرتاب چند موشک از خمین
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69163" target="_blank">📅 01:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69162">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qw5lIgEphp3wa3r3xwfk4W738nFer5bZnZM02Tzf0uk-pjhNnDOzGkzG7OHzWrpmQ0EI4dpl85JD6jIDAnF_Hvxa0EBsMsuIkgOY3HsjzAbq_hYGaQx-x4yFo-FZxxcJGrWcsAUczlbgIrWkdTZq7-eWuxR-QtimdXpRWVat0I5cRV-zmx2Lms16E79eFdkeYE0KVW9vcApAfFtRoXKq_JozK0usTQLUQPPoqkuoxeImwI79pZ0IhZThw6ortc7pO8kBsLpQO0v4L7KTq6tAbStCvPWEX2OLJoJnDskABT0MHxIQwPocZfNrCQ8bOjX_ZjdFHgq8L7POJSRYELqjlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سریع‌ترین مرگ رهبر و حاکمان دنیا در تاریخ پس از شروع جنگ:
1_ علی خامنه‌ای:
1 ثانیه پس از آغاز جنگ.
2_ هاردرادا پادشاه نروژ: 5 روز بعد از آغاز جنگ.
3_ جیمز چهارم پادشاه اسکاتلند: 19 روز پس از آغاز جنگ.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69162" target="_blank">📅 01:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69161">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03145bc392.mp4?token=C7oys07MNOhdmRvhlHcQhVbBsNLBX7vrEANMzvwK3pHEdd03jGShPpILlO6dv4xPXHv0CTDRmxL9yf8rE8jo_Q1pw0pAw-O-48XG6e_FBTm42_Qg_F_a6-li881nH1RgAQ5-sePXguJE8hicilcM9yNHDaihH66ckV7it3YXeSbtJ27Isbvk_iBOc5ictjVQxeufZJ2YPJRMepHEyL6z7xNwB1ocxw1yej6RPxTQOYv4ZYMLU2dIQYaNSsUMFfeZCnpDQXCc_YTdYrVDflMK1s2_zvKCjMTSr-GG_EHnbUg2NdodsMvW7NF3WDAL-IuP9TvVGwafL7TUz4Vmg4rDpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03145bc392.mp4?token=C7oys07MNOhdmRvhlHcQhVbBsNLBX7vrEANMzvwK3pHEdd03jGShPpILlO6dv4xPXHv0CTDRmxL9yf8rE8jo_Q1pw0pAw-O-48XG6e_FBTm42_Qg_F_a6-li881nH1RgAQ5-sePXguJE8hicilcM9yNHDaihH66ckV7it3YXeSbtJ27Isbvk_iBOc5ictjVQxeufZJ2YPJRMepHEyL6z7xNwB1ocxw1yej6RPxTQOYv4ZYMLU2dIQYaNSsUMFfeZCnpDQXCc_YTdYrVDflMK1s2_zvKCjMTSr-GG_EHnbUg2NdodsMvW7NF3WDAL-IuP9TvVGwafL7TUz4Vmg4rDpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69161" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69160">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
منابع عربی میگن سپاه به اردن حمله کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69160" target="_blank">📅 01:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69159">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YX7iN_O2dEDNIsdynC2qPOuIV4NVaFOTIjvhQ9vfSUaj4kYzTGkQ8QfwHgs2Tl8309mCUHr8VB3U6Pxng3BmC6-sRRaKcI1_LK9ANvmKD8_caeh7-YsOT22_Vb6ON6dz9UnHTPaWwncKsw3qSRQkiHk7WvdTU27IPrHl2FoOIXZTywtmPw2KWjjgYz32oV8xpdm0rhdyDX-sLdXol1qMmsg9JsyJx03S2flHB4AJMzszJ2owqGhQKFt_zU_A1vNGNUbobl53OD7wMOyQe2kEm6Ewx8iutfuEi6Zpz71G1gFVu-1ojOKp2dvcim7Eqfa_NwJbey-W9jdzM3Qfet7iKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سه موشک از خمین شلیک شده
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69159" target="_blank">📅 01:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69158">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJeLKotjcwGYjWIpmeCANvBq8-cjwjAQD8TCmw-bd0JWcF6eivkGTE3b1Urxt7wq6pyEtj1BN58V4grec-T2CPFi-6KhFu2gp38daalH-So512yZ8IopAr5Quj-nN-04LQcNp0_ejVRaQlFXHlhgdsvXdDbIg4kJ9R5_0LsXRgjZUqoTdVYrF1N4Uoe3WWkY7ZRyokq_hNhPawhOAxSUgBki1HmM1iPJegobfeEL_aJWfyiIafosg5o4_GtFCY001lcCjQ7-MbdvhTSeq-2lpO6S9jG8-8uvUwQ2zEFurjl0Lvua7LdYjynVPSSFeHso-At7xJ7eevfrdmBK6TcmrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
منتسب به خمین
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69158" target="_blank">📅 01:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69157">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های تایید نشده از پرتاب موشک از خمین استان مرکزی
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69157" target="_blank">📅 01:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69156">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/650687a011.mp4?token=VZgOLlN2mmM1rzUd6ZjuPdtWhsyl_4Kq7RIChfnJW-ZNBo6EKGu14TxuX0GvRp-pyhjbd3z-t20-NaL5HMundVLsxVA3gA8SfuZGKf4cV7X16CwowRxx9e0LytjiZnr8mnJKX-YxrLR8_xDzRQzfRHbXw5EDs8xA2WqV8INlZVInOVWWyRePMVtzfsMy59ocoXHsWtx23fW32OBerz66C0pVtADZxlE4wySnAmU7xyiAWAlmIkINAhN2W1vFQB4yWt2BgtgGheq4a_64q47FdDghe38ISWp4EUTi1kaWtt0wLyM3K-USL8YZxP9PNJoNfNmhkxop7njiMtk7VeKx6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/650687a011.mp4?token=VZgOLlN2mmM1rzUd6ZjuPdtWhsyl_4Kq7RIChfnJW-ZNBo6EKGu14TxuX0GvRp-pyhjbd3z-t20-NaL5HMundVLsxVA3gA8SfuZGKf4cV7X16CwowRxx9e0LytjiZnr8mnJKX-YxrLR8_xDzRQzfRHbXw5EDs8xA2WqV8INlZVInOVWWyRePMVtzfsMy59ocoXHsWtx23fW32OBerz66C0pVtADZxlE4wySnAmU7xyiAWAlmIkINAhN2W1vFQB4yWt2BgtgGheq4a_64q47FdDghe38ISWp4EUTi1kaWtt0wLyM3K-USL8YZxP9PNJoNfNmhkxop7njiMtk7VeKx6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
املاکیه دلقک در حال تلاش برای خوردن آب‌نبات در مراسم سناتور فقید لیندسی گراهام
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69156" target="_blank">📅 00:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69155">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‼️
علیرضا سپاهی، یک تن از زندانیان سیاسی که قرار بود سحرگاه دیروز همزمان با پسرعموی خود، ابوالفضل سپاهی و همچنین امیرحسین صفری در میدان علیخانی اعدام شود، اکنون در بیمارستان الزهرا اصفهان تحت تدابیر امنیتی بستری است.
او در جریان فرایند انتقال به محل اعدام دچار سکته قلبی شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69155" target="_blank">📅 00:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69154">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLSZjs3AnN-db-S8jJrHuM5S8O5yAsW_Hjbz3Z6Wojv7dsFyBOieCPKOh0tKrBcDGKwQKPG0GPBI5JfvHWDMdXnO6wQ_kEXcsyrUyw_iqWUXVQ1soDFI-MePkFqp79D_nV1VoNVep4ygyenXDYPx03GSnsEQwcGvIi8kktioQIjAaL81QRrxwKdu4684Q-vykmpTPMReoU1fmU5a8xlkmyLi5Wgp1oEF0VaP-jpv9q0qVVskg1CGDuEBK0RECkpio4DzehkUycpBSXnSuPQYFLvhUQDWzOtWrlGd9lItsLwkxyF7-K0jVuEejeLoPwR01HSfGc_xT8iOMqxkao1w0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حضور شاهزاده رضا پهلوی در مراسم لیندسی گراهام
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69154" target="_blank">📅 00:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69153">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c4805d382.mp4?token=Ngsat1DZhBLkmOn2oBDt2WZD9qGge_PT8xjcIzeNFiGgvviKrwC9QcaWfoPd1-_hPzvpA4rum8YRV99yjE4-pKuScSV2MUPmTQfLuqM7GS6OWYw2iSlCfiKXdoqldOodVhmjHWu4BHYBmLShnRr1p8cgXzQscPZdP7XjSxSR_eXpfv7acHiEZwvm7918St6QSy_CjcHiBW9WaxWa25FKaMsvDCKaJ92r1e5fymzU8OCGmiB7oO_xWP4bEuADyC3de9tYO7uFOViinGNxW3dA1efAVpaUI3NjR3VwlWmq3oSCsN0b72UDwZCFj9c8WSWuDg38V_TMMWL1XeIYsL_iFpfewuBpVnDuzq8GS0XUTU9NAlYWeBeVvqa4-IlsVI8mLRS2ernxKD4a56lNWUEcOBS03eQ4yhytFtjQnUFoQNDt2FmE2piHDqlF_Z16xDFvu6_Y9Lh7pQfVRup6CSS4n3rvGgh2vOvjkhjAHBSvyk_Ild3tqFFB8-OZv7-FtvGeRyPFNMJ9YyzbceffsVNfJMMwzToMczbXLaag8xZkeMUse6RCIY-Z6L9pBS-6ObSeHAAB9xpLm1bxDY67DgGaP20RjXnzYnpsQuL8qtx4Gbi2IXxheyWcv5d4vFX9n5V5VAefZBcgxC4INEnCiSd5rHkLn4JZy_SEBL8bkiNyXR4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c4805d382.mp4?token=Ngsat1DZhBLkmOn2oBDt2WZD9qGge_PT8xjcIzeNFiGgvviKrwC9QcaWfoPd1-_hPzvpA4rum8YRV99yjE4-pKuScSV2MUPmTQfLuqM7GS6OWYw2iSlCfiKXdoqldOodVhmjHWu4BHYBmLShnRr1p8cgXzQscPZdP7XjSxSR_eXpfv7acHiEZwvm7918St6QSy_CjcHiBW9WaxWa25FKaMsvDCKaJ92r1e5fymzU8OCGmiB7oO_xWP4bEuADyC3de9tYO7uFOViinGNxW3dA1efAVpaUI3NjR3VwlWmq3oSCsN0b72UDwZCFj9c8WSWuDg38V_TMMWL1XeIYsL_iFpfewuBpVnDuzq8GS0XUTU9NAlYWeBeVvqa4-IlsVI8mLRS2ernxKD4a56lNWUEcOBS03eQ4yhytFtjQnUFoQNDt2FmE2piHDqlF_Z16xDFvu6_Y9Lh7pQfVRup6CSS4n3rvGgh2vOvjkhjAHBSvyk_Ild3tqFFB8-OZv7-FtvGeRyPFNMJ9YyzbceffsVNfJMMwzToMczbXLaag8xZkeMUse6RCIY-Z6L9pBS-6ObSeHAAB9xpLm1bxDY67DgGaP20RjXnzYnpsQuL8qtx4Gbi2IXxheyWcv5d4vFX9n5V5VAefZBcgxC4INEnCiSd5rHkLn4JZy_SEBL8bkiNyXR4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش تند چند آخوند به حسن روحانی
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69153" target="_blank">📅 00:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69152">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7a509030f.mp4?token=amrmvVTTu-00SQ20wpGPpAWR3gG3DcMmyk3lqieIBgRUKT0mA150yEFqkRWbZpBQ9BirrHsrU_18AajPa4CCclkfo-N7P5VkZymDcTQUkkpOgCwvh-A4ceJRZnCbzeLfU2TXMQhtqPM0XzTTb1C_NjLQaADbUzdREWGyZOvjWT682dq5NcWbnhgsFBP5cWUBL3TQcd-d0AWGSAZx3c1L-9r-yugD6XFI4sS23NBWjyksRunZSWEy7n9aCMMxNu6XIJCNE5RVDXha3eCu2TT04UL8GBAz6lYXctDI0XLtr8lTwwxcBHxWWZg7GIC1OiI_X2qJPLoAV2s3JwwS4ry8pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7a509030f.mp4?token=amrmvVTTu-00SQ20wpGPpAWR3gG3DcMmyk3lqieIBgRUKT0mA150yEFqkRWbZpBQ9BirrHsrU_18AajPa4CCclkfo-N7P5VkZymDcTQUkkpOgCwvh-A4ceJRZnCbzeLfU2TXMQhtqPM0XzTTb1C_NjLQaADbUzdREWGyZOvjWT682dq5NcWbnhgsFBP5cWUBL3TQcd-d0AWGSAZx3c1L-9r-yugD6XFI4sS23NBWjyksRunZSWEy7n9aCMMxNu6XIJCNE5RVDXha3eCu2TT04UL8GBAz6lYXctDI0XLtr8lTwwxcBHxWWZg7GIC1OiI_X2qJPLoAV2s3JwwS4ry8pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز تو مرزداران، یه جرثقیل سقوط کرد و این بلا رو سر ماشین و خونه مردم آورد؛
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69152" target="_blank">📅 23:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69151">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCyFB6R8SNI3QLR6qCk_M4hYLNK5ZS7bxTc6w4zGNpKVKiCSzaRpbiFGSuDXjsDJMCqoo6RyIs1UtU-Bh6va6FBkUCOQa8VLBVJbbVhkS3mzR96IC2KepwNnGEv13PS0Wr-4UdZo3v5vhef4vjvOcqH9ta8ttuVuOAULU183e6qJRyh74MH-pU4oli-MAR3PbAUbW8T-yKbbiHHtXWOedBJqHm8s-ktSmTTgqi9iTy7B-mRazGkAHwtlwgpLcHJo9tLlWoiI10QoeEgUfFp35kd94IH28nWmuSso8qxVyK4HTrGg781YK0Fd729t1f9_Dl3Bo2ke9Z7ZqIBe3YJDJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
اکسیوس:
دونالد ترامپ، رئیس‌جمهور آمریکا، و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز سه‌شنبه در دفتر بیضی‌شکل کاخ سفید دیداری ۹۰ دقیقه‌ای و «سازنده» درباره موضوع ایران داشتند؛ دیداری که در آن هیچ‌گونه نشانه آشکاری از اختلاف دیده نمی‌شد.
- تزیپی هوتوولی، مدیر ارتباطات نتانیاهو، به خبرنگاران گفت: «این ادعا که اسرائیل در حال سوق دادن آمریکا به سمت‌وسویی خاص در مسئله ایران است، صحت ندارد. نخست‌وزیر به رئیس‌جمهور آمریکا نمی‌گوید که چه کاری انجام دهد و او را به هیچ جهتی سوق نمی‌دهد. هر دو طرف خواهان جلوگیری از دستیابی ایران به سلاح‌های هسته‌ای هستند و راه‌های بسیاری برای تحقق این هدف وجود دارد.»
- هوتوولی اظهار داشت که علاوه بر موضوع ایران، ترامپ و نتانیاهو درباره احتمال عادی‌سازی روابط عربستان سعودی با اسرائیل نیز گفتگو کردند؛ اقدامی که ترامپ خواستار آن شده و آن را بخشی از یک توافق هسته‌ای با عربستان دانسته است.
- به گفته هوتوولی، موضوع فروش جنگنده‌های اف-۳۵ آمریکا به ترکیه — که اسرائیل با آن مخالف است — در این دیدار مطرح نشد. همچنین ترامپ از اسرائیل نخواست که نیروهای خود را از مناطق تحت اشغال خارج کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69151" target="_blank">📅 23:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69150">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6524c67cb0.mp4?token=ZMykjtpC12Ny6RGI2bejmfxKlC4c9ZO6FrB9Fh6bY3--H2dqRmDf2R_hw3yhyq_clWFHXrvG7Gl_q9ETvP1qW2gjLkv3Y9fcgge8ZvkQnX6pLRJGTC-GHJYxVvb1YP42mOxVhVPA6l_AB5bcC61C02pRKBsq2wqwCqholJBjZosBYd3dF2imea227NhSxAL4VBsezJLU80TOYiDDfd0Q8KbOfBrQlthZUntOgLForivBPip5QrCzAwMhkdH3sf7EoUJw3Ckfnx56OXTu2jTLwOl1E4PyLQp2a-S--5EfkTpDQ0oMYam3jpu2PmtaJEXTS6ntn_1AE2ViP9nNd4D6ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6524c67cb0.mp4?token=ZMykjtpC12Ny6RGI2bejmfxKlC4c9ZO6FrB9Fh6bY3--H2dqRmDf2R_hw3yhyq_clWFHXrvG7Gl_q9ETvP1qW2gjLkv3Y9fcgge8ZvkQnX6pLRJGTC-GHJYxVvb1YP42mOxVhVPA6l_AB5bcC61C02pRKBsq2wqwCqholJBjZosBYd3dF2imea227NhSxAL4VBsezJLU80TOYiDDfd0Q8KbOfBrQlthZUntOgLForivBPip5QrCzAwMhkdH3sf7EoUJw3Ckfnx56OXTu2jTLwOl1E4PyLQp2a-S--5EfkTpDQ0oMYam3jpu2PmtaJEXTS6ntn_1AE2ViP9nNd4D6ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پژمان یکی از شرکت کننده های زگیل ابدی تو صداوسیما:
متاسفانه من اول که رفتم تو برنامه نه میدونستم قراره برم چه برنامه ای نه میدونستم چه برنامه ای هست
من اهل ماجراجویی هستم و دوستم اتیلا منو قرار بود دعوت کنه مسابقه ورزشی ولی ساخته نشد و منو دعوت کرد تو اون برنامه
ولی خب باید تاسف خورد چرا این برنامه رو تو ایران نمیسازن طوری که با قوانین جمهوری اسلامی سازگار باشه
اینطوری فرهنگسازی میشه برای مردم
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69150" target="_blank">📅 22:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69149">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/0050768259.mp4?token=eE8hw3r4V705030InC16cAocmS6nPj2F71z-QHyhXfoLhCSPWS7-1vcUKAI8NZxJyKKOhUd3e0UgY24o1avSTRmvcYKUovzlwyGyJFtdFw78pIpHyrqWK73I0TC7as7xWN3qzJ2uZ3D2VgHp_hEo4n3zBtokGPbRv8nkiXIErEtG6G6SG8jin85iwDZ9TdJpPA-D4OARPNbACOUtY5g3Hcd7m4gXesLTJ-vcJGq3DT1-E2LYrbjnIFTcUIssnzWUlXIFVDoJIHAtHKX4eehGrvFbbN4OIZ0eVtJruq4ethF0D2_oe1jLH0tovd7m_hV5PYBhSLma9Gc0BnvDD-DQ0A" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/0050768259.mp4?token=eE8hw3r4V705030InC16cAocmS6nPj2F71z-QHyhXfoLhCSPWS7-1vcUKAI8NZxJyKKOhUd3e0UgY24o1avSTRmvcYKUovzlwyGyJFtdFw78pIpHyrqWK73I0TC7as7xWN3qzJ2uZ3D2VgHp_hEo4n3zBtokGPbRv8nkiXIErEtG6G6SG8jin85iwDZ9TdJpPA-D4OARPNbACOUtY5g3Hcd7m4gXesLTJ-vcJGq3DT1-E2LYrbjnIFTcUIssnzWUlXIFVDoJIHAtHKX4eehGrvFbbN4OIZ0eVtJruq4ethF0D2_oe1jLH0tovd7m_hV5PYBhSLma9Gc0BnvDD-DQ0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
تصاویر بسیار نادری از به‌کارگیری پهپاد «گربرا-سیکر» (Gerbera-Siker) در نسخه انتحاری هدایت‌شونده آن منتشر شده که انبارهایی را در شهر کرولوتس (Krolevets) در استان سومی اوکراین هدف قرار می‌دهد.
پیش‌تر، پهپادهای «گربرا» عمدتاً به‌عنوان طعمه (Decoy) برای فریب سامانه‌های پدافندی استفاده می‌شدند، اما اکنون از آن‌ها به‌عنوان جایگزینی ارزان‌تر برای پهپادهای «گران» (Geran) نیز استفاده می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69149" target="_blank">📅 22:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69148">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnappPay | اسنپ‌پی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBLnLVJPmBiqZXz3v4uDhBCwTYPj1Pdj_im_NcIwygYPu2WFC-qaxR3m5cNvjvGn_cv16DQmdmqzfHW9pAIRFI3KdBuOm61B9k1INwsdb82ZdRPPp22liFXYkC1DpsK08K0uI3s4tTV71DU7e4PhwkLnPnDeS-p98SRNtrLd0G1RCbDbSCSyv_7NC1P6E4gRj3wIujCm03Y2CJvn39sAezecKIXf-bzbXly7H-G-5pjNen3R2RkLw0EGXJLkvFa2smo6s4fuZ06p7cvy2hVn1q3uyALP4t7yo18f_i60gQzAhGG7r2j3nZgCXDG4zUljbdIhu3R2EScuvTZ2v2OTPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
از برند‌های محبوبت،با تخفیف و ۴ قسطه خرید کن!
😍
🤔
می‌دونستی می‌تونی از فروشگاه‌های فعال در شبکه‌های اجتماعی مثل اینستاگرام و تلگرام و سایر شبکه‌های اجتماعی، با تخفیف خرید کنی و هزینه‌شو در ۴ قسط با اسنپ‌پی پرداخت کنی؟!
🤩
🤩
کد تخفیف ۳۰۰ هزار تومنی: PAY3SCP
⬅️
از طریق لینک زیر لیست فروشگاه‌های طرف قرارداد با اسنپ‌پی رو ببین:
👇🏻
https://l.snpy.ir/v06dj
https://l.snpy.ir/v06dj</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/69148" target="_blank">📅 22:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69147">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04ca836fdf.mp4?token=YWn_0gonszpiz-TaLsaLFd2puOsGmSZErzlQTRRPRRfzlImAmquo7MruHRU8ITH1Fc60NwLjHfCr8xNeUlKmX9RXJDQcFhRCKarviIYqaippIn5GYLzRKO0uTcTRWEiXTsoRharG2qXYdFZYhT34sv-iB5_FeLb4uKxfpyziakrhaPBVj_umTXDzUMUSlgthmJpGgI3-PloaAkT2-fr0q7CdM5SeGsGQv1zJFBGqJ5fcGZgt_kT3AiGI9fxySXH1bhIzL54OSwwFbO7f6jISXMBd0NSXla-rL9MklUs8TodJwwiPl6lE2qF3XX_iapP6Q1rC_uwzdeWMEx0MvO6JOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04ca836fdf.mp4?token=YWn_0gonszpiz-TaLsaLFd2puOsGmSZErzlQTRRPRRfzlImAmquo7MruHRU8ITH1Fc60NwLjHfCr8xNeUlKmX9RXJDQcFhRCKarviIYqaippIn5GYLzRKO0uTcTRWEiXTsoRharG2qXYdFZYhT34sv-iB5_FeLb4uKxfpyziakrhaPBVj_umTXDzUMUSlgthmJpGgI3-PloaAkT2-fr0q7CdM5SeGsGQv1zJFBGqJ5fcGZgt_kT3AiGI9fxySXH1bhIzL54OSwwFbO7f6jISXMBd0NSXla-rL9MklUs8TodJwwiPl6lE2qF3XX_iapP6Q1rC_uwzdeWMEx0MvO6JOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
من همین الان یک جلسه عالی با رئیس جمهور ترامپ را به پایان رساندم. وقتی می‌گویم عالی، این فقط یک تعریف ساده نیست.
گفتگویی با مشارکت کامل، با حمایت متقابل، با درک هدف مشترک اطمینان از اینکه ایران سلاح هسته‌ای و همچنین اهداف دیگر نخواهد داشت.
یکی از بهترین گفتگوهایی که تا به حال با رئیس جمهور ایالات متحده، دوستمان دونالد ترامپ، داشته‌ام.
تمام تیم ارشد او و همچنین تیم ارشد ما آنجا بودند و در اینجا نیز فرصتی برای تبادل نظر و همچنین هماهنگی مواردی که برای امنیت و آینده کشور اسرائیل مهم هستند، فراهم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69147" target="_blank">📅 21:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69146">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1hEYY01zLQYSCXaMrWXAcjY4ZyzaqXe_2sqbf0iXNpbOEN8WSp83CDZLd7k8VmRvJJMo31ql0l1udEkObueggYHBpnSerbFfGgUiBJO9Q7Wzm2vl6AgYPK016oPJJB5Eis8q14VOYLopwaOCXR5AVgbj4tOmvq2UBVvv7AI4kSUtfC9JB0vCQxWfu7GA2sOv6FMsW-vamfJxQWL2Bfnt-GMoY3o3F3dJp-XmmgEsJX-P0oGVf-CCN4Ge-TylEbVgqzdusk1qJEeErH8reKW8UIlobD7oPs2UWGNWrqgvUKPKKjMWnBEqupbcgvDbDWDK6SS3RSyKMt9F8d1YD_w2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
علی قلهکی: مراقب باشید پاسخِ احتمالی به اوکراین، کل اروپا را همراه با آمریکا علیه ایران بسیج نکند
به یاد داشته باشیم که ایران خبر اصابت کشتی خود را رسانه‌ای نکرد و این کی‌یف بود که خواست آن را منتشر کند! حال به چه علت؛ درگیر کردن اروپا در جنگ با ایران یا پیوند زدن پرونده «جنگ روسیه_اوکراین» با «جنگ ایران_آمریکا»؟ شرایط پیچیده‌ای است
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69146" target="_blank">📅 21:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69145">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🇮🇱
یک مقام اسرائیلی:
ترامپ در دیدار خود با نتانیاهو، خواستار خروج اسرائیل از هیچ یک از سرزمین‌های تصرف شده نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69145" target="_blank">📅 21:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69144">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6FogaGldPACdMPnnjpkfznLStLrxV_aQxDdmRF5yeJjB_L48ph1Hb7KRy4jSjYtJR-sYOfwdIfTcQFyHUYCVv8w6nb48LQL-uJPt08OPSE3NdDFn9RU1xBfY-U_ILUEj2DsxpgFJKzhTnFSd9-wmnOFBlZhCSO0wg-r7OKE2KuCYTnTa22QBhv0iSIEch1y80oKOvhMCzQwJbJL-mGkkglDteeAJXaxi9_IsIKWIP1lnKvpY-MfymhhdVatbmVddGexC5yl1OJaEWJ8WVvfOculljIjioQZlkyNsYFTm9VYDB38FVvtZxOh4o4ophax0Nwdkh1chke0YqYtP7pGBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یحیی سریع، سخنگوی نظامی حوثی‌ها:
نیروهای مسلح یمن نفتکش غزال متعلق به عربستان سعودی را به دلیل نقض ممنوعیت دریانوردی و نادیده گرفتن هشدارها با موشک‌های بالستیک هدف قرار دادند و این نفتکش مجبور به عقب‌نشینی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69144" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69143">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZNoWTwNBTxYX46ujwRotW8zsbNS-9r4saSgvEGmoebXbiP35BvAosK_plHmoIhQEmgHMpBIoeFCVPmiKUInXNyLj2FRrqN5MacMyClgeKwmgEX1X15y6bB4C5Gn64U456yjXiKwaRZ9pyTFwTakzRK4QNq8a3sh9jV4GTHFZsYrdqrOKrvQl6G_C2mU_8FD8PiVOghUEWwOJJm1CbppqdkgGvbgmxLLt2WzYI78VAQWtVpC7K5sfsTIRGYhvv1pZ-KKx-9aPt0gwPiUqFT8kmrQUap50T25TKBkipjuoMjr0H0GNqK8R__v-r9Upgj0ddUuAfpOPh8mG-ZuV5Lkqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
آمپول لاغری زیکورپا(
®️
ZCorpa)
؛ وقتی درست لاغر شدن مهم‌تر از کم شدن عدد ترازوئه
در لاغری با آمپول زیکورپای عبیدی، هدف
کاهش توده چربی بدنه، نه از دست دادن عضله
.
📊
مطالعات روی تیرزپاتاید (مولکول موجود در زیکورپا) نشون می‌ده:
✅
منجر به کاهش وزن بالای ۳۰٪ می‌شه
✅
عمده این کاهش وزن توده چربی بدنه و سهم کمتری مربوط به از دست دادن عضله‌س.
✨
برای
شروع لاغری با زیکورپا در کلینیک ویهان
، پزشکان ما به صورت رایگان شما را راهنمایی می‌کنند:
مشاوره پزشکی تزریق زیکورپا
کلینیک ویهان</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69143" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69142">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
⁉️
کانال 12 اسرائیل:
دیدار نتانیاهو و ترامپ با حضور تیم‌های گسترده‌ای از هر دو طرف، یک ساعت و پانزده دقیقه به طول انجامید.
یک مقام اسرائیلی مطلع از تدارکات نتانیاهو گفت: «ما در مقطع حساسی قرار داریم.
رئیس‌جمهور ترامپ به‌زودی تصمیم خواهد گرفت که در کدام طرف بایستد و چه مسیری را در پیش گیرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69142" target="_blank">📅 20:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69141">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukjpfXjWVFivSl_ZMr365LFziP9NXYAf42ZOuZsTc0EguzIUQT8vIrJX7kJd899desyW4ZqrA1LAXt-8M8sVzbi5Y3qbo-rSi_jsJJc6M5Si3ZLQqVnOwMnrVjxqmseEPJoN55u7MhTvnnyLWfHaiSxeU1BKpCFHM23k5-hUWkbiLa_QgLy3bG6c_kULdG3b8K-VnZkScLMf7IHLKHADLaMpA5DXy4LPdhmNt5SHPkDBiQS_HCKC9sSOVsLOhbLZBfvFIF554cKvot6l7pQxexuvVeHhUQ0y33h-fKMFybgpEDb08tCpc7LPeMSZGuKsmuRlTGkS4pjEnbNEglqRqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇦
آندری سیبیها، وزیر امور خارجه اوکراین:
من با عراقچی، وزیر امور خارجه ایران، برای گفتگویی صریح تماس گرفتم.
من تأکید کردم که هدف ما جلوگیری از تشدید غیرضروری تنش است.
من مجدداً تأکید کردم که تمام اقدامات اوکراین صرفاً با هدف دفاع از کشورمان در برابر تجاوز روسیه انجام می‌شود و هرگز قصد هدف قرار دادن کشتی‌های غیرنظامی یا مردم را نداشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69141" target="_blank">📅 20:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69140">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/001cd370db.mp4?token=uy_TdnWL_zb0ZIsxW-m_U-sBnZTIlLzzo-QKLgiFIAyVuLRguwxwaLk_vkes0M3nljfzzaJPfvVk93O9D6jKOlEU7-17acgrEj3VczYe1Ip27xfae04d5ZtxZM08CJs1HQd7zmhrjxbpDcelzxBbSm4G9Bkzg0J28U9bWja6yy66efrzf-dSfcKpHC-8WIFvX5jCXwI4bzkITYLCqHktV6Mv3MCmDKbDfFL0Jzml9EoMWW8g2u06mXJzkWn2JwbRL1Wupmn9rbLRXzd3CA8xQ1dEZb7aee3UAwfCKalmDq0_bU7cIPqu7n2aDTwAGQTRsmJvMezW6PFayWpUEr6qAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/001cd370db.mp4?token=uy_TdnWL_zb0ZIsxW-m_U-sBnZTIlLzzo-QKLgiFIAyVuLRguwxwaLk_vkes0M3nljfzzaJPfvVk93O9D6jKOlEU7-17acgrEj3VczYe1Ip27xfae04d5ZtxZM08CJs1HQd7zmhrjxbpDcelzxBbSm4G9Bkzg0J28U9bWja6yy66efrzf-dSfcKpHC-8WIFvX5jCXwI4bzkITYLCqHktV6Mv3MCmDKbDfFL0Jzml9EoMWW8g2u06mXJzkWn2JwbRL1Wupmn9rbLRXzd3CA8xQ1dEZb7aee3UAwfCKalmDq0_bU7cIPqu7n2aDTwAGQTRsmJvMezW6PFayWpUEr6qAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
غریب‌آبادی، معاون وزیر امور خارجه ایران:
ما در ۱۵ روز گذشته هیچ درخواستی برای مذاکره با ایالات متحده ارسال نکرده‌ایم.
برعکس، آمریکایی‌ها خواستار گفتگو با ما شده‌اند.
آن‌ها همچنین پیامی از طریق عمان برای ما فرستادند و اعلام کردند که هیچ‌گونه اقدام نظامی علیه ما انجام نخواهند داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69140" target="_blank">📅 20:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69139">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWTyvSWimmc9SWUUJ0olTndKl0-9XqcYbwcUh_ZtjqqCaNPXQiJRDVYsbkp9gAZRkBaWwfxtOcMWqIDueaPMrSM-Ug2NkRSBBJgC6nFM8MoXwky3sP-3sGs7uk0dggbvE6fVKrtIzoMzEGjRwwzyaAUNq7yBFPjpXLV8NcBkGD9ikV677zRxkvnCmEwag5t0BRZjYNJkvbzZysUAeblBb70xupmiY6DqP-vhrjWXHObtiTWWdmxI0zseZpzPqPHIiY30-OAnvuwpCksw4qVY096NKAQlegw11BzB5e_yTttk0gVeIOBlPq1qaXBq5hzqEpWqf8wlZ2Nl8G_km9TMAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سخنگوی کاخ سفید:
رئیس‌جمهور ترامپ دیدارهای خود در دفتر بیضی‌شکل با رئیس‌جمهور زلنسکی و نخست‌وزیر نتانیاهو را به پایان رساند. هر دو دیدار مثبت و سازنده بودند!
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69139" target="_blank">📅 20:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69138">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dcd737689.mp4?token=NPg6s7VWHXNzSF5qDWm3YHSa0zN5ZDg7h-k_g2Z2Dc6rehU812ub9oOn2nEzYyYNUiHelv6VuWK9QGsvn9hxlBaOP6MVQ9UOmDZBh8zVtCMiE_QNqD0FO44snAdte-rOYnFG7NlvcKEycro1VsutJDNKxdHhcIOAAUN3P84cHlwRWp_HhbtE4JH-6OoM9qhhiET8zB1ugcjvxBKWSD_scp00Mzk2noz8cQcqcDzM1LSD5qX-62_QODAhk9vVL4yjhs_CO7i3DI1OUr3N-Lg_UZTvk0uzfV3SHEoUlhqZbzCL_eeB4jZH5g3w_oR13Ppu_TdxEsbWxN3XFU3KexGr1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dcd737689.mp4?token=NPg6s7VWHXNzSF5qDWm3YHSa0zN5ZDg7h-k_g2Z2Dc6rehU812ub9oOn2nEzYyYNUiHelv6VuWK9QGsvn9hxlBaOP6MVQ9UOmDZBh8zVtCMiE_QNqD0FO44snAdte-rOYnFG7NlvcKEycro1VsutJDNKxdHhcIOAAUN3P84cHlwRWp_HhbtE4JH-6OoM9qhhiET8zB1ugcjvxBKWSD_scp00Mzk2noz8cQcqcDzM1LSD5qX-62_QODAhk9vVL4yjhs_CO7i3DI1OUr3N-Lg_UZTvk0uzfV3SHEoUlhqZbzCL_eeB4jZH5g3w_oR13Ppu_TdxEsbWxN3XFU3KexGr1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نایب‌رئیس مجلس:
نباید به ایالات متحده اجازه دهیم هر زمان که مایل است حمله کند و هرگاه با مشکلاتی مواجه شد، عقب‌نشینی نماید.
اصلا نباید با آمریکا وارد آتش‌بس شویم.
آتش‌بس با آمریکا معنایی ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69138" target="_blank">📅 19:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69133">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lRuPGa6pRewKCk2vzmXLdNW8EbGsHsIJ-LC9sJb7FiEihHNyBa6CMG1sNo69bUxvrZCwYmwdRJuUeJRgLfH9Ic_Zdis20DmL5wP-_5b4kEbS-4WWwqW1L0pX8SsXzJ8Aq7sMtmUFsZF7CCzMC3lqrMTxDuhlWQHjgDwxaEAiP81EPPJHEn9fTpQZgsJtKc9poM6G_wBZ1MW8_lwfseRYVAvvxoLCTtuK5OLQhFyr1Utqjfy9aw_ylw1nXQHnK3amjZQH0gn47Ea_eEokPLNdQvTJaXXDfJXrdrCtn8UYshjzHr3CeFbzsmjXtTAy00IbtKWYX3ldc6V_dZp6QeQUQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UAF-J5PwNmb0x5yq7DWnEVHq6Su8K9GxfAlbGTez6f0jAdkQ5q_N_T1HxL8Ejw_td1eSGyaBZvrhCSORYV5G1NgoGWs5fZtFzTg-6qH6yazdr7f4dSoonc5tMuQa7T6deLQ1MMAh4MlkQx6hZE7xCZgCrIVA-RXqlZpxOnUP15jt2BwP4uqO8nab8PmCmDGyTt60YlkY7CsXZh9acviAq5B1HwzDS9mM2QZ67srWqFQdgt1ktc8RJWzIAJ7CtriTxzUyRzrrd49hy2pfZo-5xrIFiW03xRKGRcx4Ub1-Xz2XIBF7zpQj_IHpzdhRaGHOkS9vvcvWhFUtodzbuqEIAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u5Ud9NWPTsLXe38j3F99DthsyBX-YhpX8tMygaq-202bCLRvDKPXvOC9ynXC4AHpc1ZrpLQVon2uhLTjjgZC9GifxfwxLJ2AAcRzOgOk4OOi7vswobVIqFu1gV_Q3ICo2l-U3YEw8eIwYzCe5hJVk1PAQgkSs8TOkAor0X27beGZQ6e0vl-EdPlom-qlktKpYnKvHsaFhtM6q6I8gL2bRa19hiEOsxD42y3imcft6P7OKQzEH8Fbz2HFov6kiV4AfUU7LFeGDLD1fVSWuIRit3MFTtn0r4owHlWIMKEuj6QtFH6PCJDp-lcsPK8_ckIO3vNth1eUNNBKWuRNl5_kkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vb3XrrlA8kzBjSoSBd5LgJAYmNwzISw3fIKUR1kQie2aKPY0bxyDtBQRk_6-iIlxWY_hLyHO9CsgxAndOAkR_K3k7mwDnozZ23xrefRtJtjyPAhwzYJXbCp8YWYjsJknwey7i7j-E4_ouMT3WogyaowdgU5vKUNsuQpQVcdsa3h7D1a2n8nLAMq6lIBTPbP0gVDXzn0FbLA5IdiV1sQ0fwNUV1e1FBhOqAfdIGs8yoCOIUbFKvKgkc4aMcM9QLf3rKZqyvm8Jp_vZKkJrYugJ51Db-TnYQO4rhx8bqCv1UKkeqAjJIMHeFYD812-oCfoKHP14vwNZ66t9nGUnJVodA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zs5OjdHmvsHa6j0x-NZz_YrPszC5QM0HvHA7j4d0TWlhDQO65EdiXgX6l0nhTAV_FsiVeqNfaO2_E8ZHCk4AUEk4S2-JR07tAHmVoabOt4Yb4HyDUg4-A3TcTzZP3hI-quyQhD_Jvqz1ulaGtLfQHRaK8JoHgn6SMjfDVN9P-wi6MlquFAb2rp8N0j3GHd-TgIil3-hQ0oiNH3RJFqHXrU8_Q6HG77nBz25B35dDK-wam4bLAUI3jaPu3XD6uYXLUozOgWfZzmKzQD3s6BJrlbcW-J3_71cWTw8k9wPJttMjakNt3LaA3XWNYVedUPbGOBfxxicROMBNCYYBXCmgBw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇮🇱
🇺🇸
تصاویری از دیدار تیم نتانیاهو و ترامپ در کاخ سفید:
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69133" target="_blank">📅 19:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69131">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QDKUJuOOvGkXEm1YEYQJrwBbxyjQZMPle-Hw28VdJ7Wh3ALYaYnyOM6Y48lH3_9Fzdw7mqozQrgJCKiP-T_GLm4SHViMonkPd3Yv6V4ywbfccisY0rKXCBoVgb2F9LhB1hbKxTa7BPnjsehnxrRkqmDQNtrukQJMXn0_X11pfJTZWB5SmEC8E7Kcr3F8gWblpzoaQJ1hGW0z8bevBZIsNb13X1k4T6UdoSxXszQIzvi99qGWvPRu5FJc3JHIzPVZzdWnMi0CXFSpbbr3xyu1JZEn0ndQ00_Og7-8LHHfzRcU9nK5hrg8mZb_kdrN-hg8uTi9Hb0iyxykVq7TXeUmxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iqhBz2u5c1fH-6GmOj9Ufmw1Ztfa9qHjqEq_yVx5mlcZyG9suZagXZFtEiW65nt5qaVH2E6mzSICFwppvavwrn7F8dunlIFXWj0fpER4xjhA7p_Jur5t4d_3sEvRrgq5fxVvac4NN55LOv-X4U3bfoHoAJThap0oC_HGiqXt1J2-x9QS9K-pswPMQ_7VjzJlo8vSUJymOPYc3s4FDLo88eEV3ydLbQKkZar8f7R8klMup8FwMvzrIZPOYrdr0ZmPTrKWcBf9jumoVFKAuhY2wPVhuj8oSQ9Ronq88lce39JRvBs-GnITdWaDt9DLEaQ4RLgfkHMxaTkYR43AuCJqSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
بنیامین نتانیاهو، نخست وزیر اسرائیل، پیش از دیدار با رئیس جمهور ترامپ در کاخ سفید، با مشاوران خود گفتگو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69131" target="_blank">📅 19:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69130">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6822c0ad1f.mp4?token=rJ9nhEPr8CAsM6aaLaAg_-uFDOLkM_xQe0tNaVDb1-ArV51SBTYvJKXFQrIInvxgPNjjIUlOh7Zbi2gwbS_wNH7g2HQO6NnlPKlgIAmh1fSSay_nEv7JpbBdOz67nxq85383RVX_NQamQMVt5vBcTjYcjMSzMxdPG3ZLKcKB-juaKnnTT88bFuhcPFlfmsVS9vaEV5i6A-jWf4eMtnY9yiZTb9pyXfgXb_4WmNmJ1KUPI7MBII_rf28EPXVOnX3jSI7LlbaLz3Pw-jpYUX3SJrZauF255bhw4kCoGtqLa6ILrxQZz4A2evm9oanz0WEgpLrxZassCAJIspO_jWYjOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6822c0ad1f.mp4?token=rJ9nhEPr8CAsM6aaLaAg_-uFDOLkM_xQe0tNaVDb1-ArV51SBTYvJKXFQrIInvxgPNjjIUlOh7Zbi2gwbS_wNH7g2HQO6NnlPKlgIAmh1fSSay_nEv7JpbBdOz67nxq85383RVX_NQamQMVt5vBcTjYcjMSzMxdPG3ZLKcKB-juaKnnTT88bFuhcPFlfmsVS9vaEV5i6A-jWf4eMtnY9yiZTb9pyXfgXb_4WmNmJ1KUPI7MBII_rf28EPXVOnX3jSI7LlbaLz3Pw-jpYUX3SJrZauF255bhw4kCoGtqLa6ILrxQZz4A2evm9oanz0WEgpLrxZassCAJIspO_jWYjOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مدیریت بحران تهران: این بلندگوها و سیستم های صوتی که نصب شده آژیر خطر نیست
اینارو نصب کردن برای پخش صدای اذان و ما برنامه ای برای اژیر خطر نداریم!
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69130" target="_blank">📅 18:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69129">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8q-kWiDTfoRDjkSoF4vwhJhlbD4PfAiMKElomVWhCk9d1irPAOyxNsa67fQscjigG8L6hC9RUmKVoUojzz3lxD7oKhvWGg-ka2YdMY_f8zG6YLDaRe628T-FKOVtOSflViZTsermtVpFG84lOW32G7svLU8qd-WmlZ700ma0Gnuz0Fcne7Pn1egbnDab_FzkoKcghXtkD9F-AYsNzte84NFd2vNrJjU5RsSzGIoNcI_aL39TlK9xiSEw0ck5XRgcMiIdBNJwuBCXrz9EieXtm6K7BB267jfF9-C_BmuoK7jUpwAZwlGXjp95XxznNoG65REKub4W6OjMnlzeNSfSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
تصویری از ورود نخست وزیر اسرائیل، بنیامین نتانیاهو به کاخ سفید
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69129" target="_blank">📅 18:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69128">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
کانال 12 اسرائیل:
دیدار ترامپ و نتانیاهو دور از دوربین‌ها برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69128" target="_blank">📅 18:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69127">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
دیدار ترامپ با زلنسکی پایان یافت؛ دیدار با نتانیاهو در نوبت بعدی است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69127" target="_blank">📅 18:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69126">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8339055d6f.mp4?token=K5sEiNQ46ACHPDT01AsnF_lasf9EqKaK4_Tb8SqYm_8S_SrmpUxkU3mdppOWssHcNI26r-lXdhEJdeuPM_qy6DMOBBJ_5Q9PYM1DKoIkbJTy6xkSCSOOU4oGys3fNF2_rb7ZwYi4NOgrF8oSXfaDLpRcvD1pp-Prl6PoYEqRZvwUksN2ykz96QH-8gBJcqigolqnUR6h06u_fyBlF9vxzeLX9cjJtQvkI5zEsPB4PKS-hfYI5Fcb2fhcrJl0_6J-7fZWO7KR2Z1B7er7f7tS-JpKjMMaaAPrG2qUddmB4uieWR0sMzwCS5UOairHP2aTZA5WA2Oa7lzoZ2tZCCvoPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8339055d6f.mp4?token=K5sEiNQ46ACHPDT01AsnF_lasf9EqKaK4_Tb8SqYm_8S_SrmpUxkU3mdppOWssHcNI26r-lXdhEJdeuPM_qy6DMOBBJ_5Q9PYM1DKoIkbJTy6xkSCSOOU4oGys3fNF2_rb7ZwYi4NOgrF8oSXfaDLpRcvD1pp-Prl6PoYEqRZvwUksN2ykz96QH-8gBJcqigolqnUR6h06u_fyBlF9vxzeLX9cjJtQvkI5zEsPB4PKS-hfYI5Fcb2fhcrJl0_6J-7fZWO7KR2Z1B7er7f7tS-JpKjMMaaAPrG2qUddmB4uieWR0sMzwCS5UOairHP2aTZA5WA2Oa7lzoZ2tZCCvoPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
🇺🇸
رئیس‌جمهور اوکراین، زلنسکی، امروز صبح به کاخ سفید رفت تا با رئیس‌جمهور ترامپ دیدار کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69126" target="_blank">📅 18:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69125">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/634ef5a127.mp4?token=ckuXTX25SVh4MYz2nfhszWBthdD-6ifr4smyB8IdapmyGX7fqZGo8VV8IFShpkepedmKOktYS1y-xBUUd_l8Ad0fFIWNd6_6AskDE_RIXlganrhTVcfVdstEppVEDxxWpLX6g09WHF_rj-uaBqXcI_GOyJIfP8sEKamwYs1ENxrL7sGAObrPJiPDs-nQTWzj04P0io9NSPwDSJrjJDG-5SZixGULtopELzxxTztM70haJyyaLc6XJoCjXYJPqeJEVpFmHf422dSU8YjGe67mW8oSSMPmTnSBq6K5VT-YLFZU28ub7052dx31LgRme88LrlJW_xAQ6S8vZhiQwAncxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/634ef5a127.mp4?token=ckuXTX25SVh4MYz2nfhszWBthdD-6ifr4smyB8IdapmyGX7fqZGo8VV8IFShpkepedmKOktYS1y-xBUUd_l8Ad0fFIWNd6_6AskDE_RIXlganrhTVcfVdstEppVEDxxWpLX6g09WHF_rj-uaBqXcI_GOyJIfP8sEKamwYs1ENxrL7sGAObrPJiPDs-nQTWzj04P0io9NSPwDSJrjJDG-5SZixGULtopELzxxTztM70haJyyaLc6XJoCjXYJPqeJEVpFmHf422dSU8YjGe67mW8oSSMPmTnSBq6K5VT-YLFZU28ub7052dx31LgRme88LrlJW_xAQ6S8vZhiQwAncxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سخنگوی قرارگاه خاتم :
هر شرکت یا کشوری که از دارایی‌های بلوکه‌شده ایران پولی دریافت کنه، دیگه اجازه عبور از تنگه هرمز رو نخواهد داشت.
همچنین به ترامپ هشدار میدیم که هر کشوری که از پیشنهاد آمریکا برای استفاده از دارایی‌های ایران استقبال کنه، شناورهاش از این به بعد اجازه تردد از تنگه هرمز رو نخواهند داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69125" target="_blank">📅 17:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69124">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9cd6b53c3.mp4?token=BvjeSIRqL1-zbGpS4JQjxQ3LWMrTsyRcYAw9lm7Lj4BRHpDPqsf8gLlC8d_zkggIKCD71h782vuxWHnqj4ZDsEXLa3GsEzDsYnCV-tghVtbSP9xI6FmbO-39llDlT4e6XKvHwpxWuwS3Sqw9BU_YUSKuAMqrt5VUJEz-iDZivCdQHkwJAIuUZTYDCNfkr7MVxoB2czkxJX6NnP_-dmkEXsH2cUXI7gQxmKRJsnYabpEvIiyNsbs2rB7VT0fUptOMcL4FlXgyMlr2O0k9NJGPdrXtEZLuRlw98Ti03HKWNUiodRO1F9lbUn_kZSgXUzeMZBWOYKcjRX8yU7EQB3jT2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9cd6b53c3.mp4?token=BvjeSIRqL1-zbGpS4JQjxQ3LWMrTsyRcYAw9lm7Lj4BRHpDPqsf8gLlC8d_zkggIKCD71h782vuxWHnqj4ZDsEXLa3GsEzDsYnCV-tghVtbSP9xI6FmbO-39llDlT4e6XKvHwpxWuwS3Sqw9BU_YUSKuAMqrt5VUJEz-iDZivCdQHkwJAIuUZTYDCNfkr7MVxoB2czkxJX6NnP_-dmkEXsH2cUXI7gQxmKRJsnYabpEvIiyNsbs2rB7VT0fUptOMcL4FlXgyMlr2O0k9NJGPdrXtEZLuRlw98Ti03HKWNUiodRO1F9lbUn_kZSgXUzeMZBWOYKcjRX8yU7EQB3jT2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ما محاصره رو برداشتیم، اما چون اونا توافق رو زیر پا گذاشتن، دوباره محاصره رو برقرار کردیم.
اونا مدام توافق رو نقض می‌کنن. دیگه نمی‌تونیم اجازه بدیم به شکستن توافق‌ها ادامه بدن.»
«ایران تنگه رو کنترل نمی‌کنه؛ ما کنترلش می‌کنیم.
اونا شاید بتونن چند تا مین دریایی بندازن و اوضاع رو به‌هم بریزن، اما کنترل تنگه دست ماست.
حتی یه کشتی هم بدون اینکه ایران جلوش رو بگیره از اونجا رد نشده.»
«وقتی قاسم سلیمانی رو از بین بردم، ضربه بزرگی بهشون وارد شد. به نظرم اگه اون هنوز زنده بود، ایران جور دیگه‌ای عمل می‌کرد. حتی ممکن بود به سلاح هسته‌ای هم رسیده باشن.»
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69124" target="_blank">📅 17:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69123">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/803209f6c9.mp4?token=q8ZbBE8PqE6alNygntarjHk5ZRsn02bsawi6NoUOgc0b_2F29-DetvRSCg2N0hLjAJR3wiNF-z0Sk9W_6r-vb8azlEGTWPpysFHbR0N4ZVQpZikGhuF7eO-KdfvsEqu61ogzG143zjHCuGneCgDvB-ctcfWxbHSPQPkue9j_OgzDUAaVr7di9hnBxM3FC5YuRUuyvwsoMfs5dLVKGqz2flHnslW9ji2uWzWxBYFwCle5dyJXl8Pl2SCMnBBz-OspVcyJ1Wsp4bU_Gs4cL4uf4GYCcpAQjIEgxUWXr1PVQwcS8MZ_jlFfPF92IDt9FCmmFUBL4GLveiqbWWgaA6PV8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/803209f6c9.mp4?token=q8ZbBE8PqE6alNygntarjHk5ZRsn02bsawi6NoUOgc0b_2F29-DetvRSCg2N0hLjAJR3wiNF-z0Sk9W_6r-vb8azlEGTWPpysFHbR0N4ZVQpZikGhuF7eO-KdfvsEqu61ogzG143zjHCuGneCgDvB-ctcfWxbHSPQPkue9j_OgzDUAaVr7di9hnBxM3FC5YuRUuyvwsoMfs5dLVKGqz2flHnslW9ji2uWzWxBYFwCle5dyJXl8Pl2SCMnBBz-OspVcyJ1Wsp4bU_Gs4cL4uf4GYCcpAQjIEgxUWXr1PVQwcS8MZ_jlFfPF92IDt9FCmmFUBL4GLveiqbWWgaA6PV8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«اگه من رئیس‌جمهور آمریکا نبودم، امروز دیگه اسرائیل وجود نداشت.»
«اوباما فکر می‌کرد می‌تونه با دادن امتیاز و پول، با ایران دوست بشه؛ اما بعدش رفتن دنبال توسعه برنامه موشکی و هسته‌ای. طی 50 سال گذشته، همه رؤسای جمهور آمریکا یا کشورهای دیگه باید یه کاری می‌کردن، ولی آخرش همیشه این آمریکاست که باید وارد عمل بشه.»
«اونا عملاً قبول کردن که سلاح هسته‌ای نداشته باشن. فقط مونده این توافق رو به‌صورت رسمی نهایی کنیم، اما با اصلش موافقت کردن. چرا نباید موافقت کنن؟»
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/69123" target="_blank">📅 17:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69122">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«اگه دوباره برگردم و بخوام کار رو تموم کنم، همون‌طور که بعضیا دوست دارن، خیلی راحت می‌تونم تو کمتر از یک ساعت بیشتر پل‌های مهم ایران رو نابود کنم.
ساختن یه پل حدود 10 سال طول می‌کشه. پل‌ها سخت‌ترین زیرساخت برای بازسازین و بعد از اون هم نیروگاه‌ها قرار دارن.
من می‌تونم ظرف یک روز همه نیروگاه‌های برق ایران رو از بین ببرم. اون وقت حدود 91 میلیون نفر بدون برق و بدون پل می‌مونن. برای همین این یه تصمیم خیلی حساسه.
اونا می‌دونن اگه به توافق نرسن، من این کار رو انجام میدم .
پل‌های اصلی واقعاً از بین میرن؛ فکر می‌کنم تو کمتر از دو ساعت بیشتر پل‌های مهم نابود میشن و نیروگاه‌ها هم ظرف یک روز.
ولی اگه بشه از انجام این کار جلوگیری کرد، ترجیح میدم این اتفاق نیفته.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/69122" target="_blank">📅 17:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69121">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a44e71f50a.mp4?token=DL5h9EQJPyEKJdZWF3Qv-VByX5yBWpfH5rGCkmgF6xThHL_A7qkeDjyjA82ZCQ-2HtL7iGhRAwYv8pcWJ0UmiM6VTQ-CxFwdo9EkvIJmZzni-bCBh447R5UFhWBUF27_vJHOR-0_2ITNp_dkTvQmZe8HL9CD2NnxGC-y9XcqCa47tpw9edERaGe9K2NL4taY9M9xIGKp9jDe86QY6nHqh_5NC40APVtQTjce2H__ImC2Lq5cg4wV_M4FIV8HT74GD8a2Omi-2ScO-NeJfVWKy4juV2ursnMPe4wPCRyyFBOhwcxaZSt_K19eqNPDYaFh2xPNWCtxaPVkGsfzD9HjpoNw1dUOEAa1gt2L5dwUtRK1ZqwLnklvD_oapAtVWVPp1MwRY303YWpXNmYeMOd3JzkN8652pC9oXLsGA8YPygvwRWMAOjSnN_5TQfx7PuMroEKnJ9xsHg86BqmE4X1-S_DrQcNCfv-aFMBxz6ZL8kytg5u584EmMGYBZm1Q0urIMc0a9doUl09oUuOGO6jmr4OlY-64O3S8yGaxZTbvD6O_lXYoocVrWzrtof_tYY_XpFGL7KCZeDI--lt22n6rdrdhS8lHpZXLHNvVcZIbTWrbxiAK24gaQLcZC30lf5NzG1iQKb-vRcdy0Y1FuLyt-NChh_LPMaJ5LcX_qAg7Cx4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a44e71f50a.mp4?token=DL5h9EQJPyEKJdZWF3Qv-VByX5yBWpfH5rGCkmgF6xThHL_A7qkeDjyjA82ZCQ-2HtL7iGhRAwYv8pcWJ0UmiM6VTQ-CxFwdo9EkvIJmZzni-bCBh447R5UFhWBUF27_vJHOR-0_2ITNp_dkTvQmZe8HL9CD2NnxGC-y9XcqCa47tpw9edERaGe9K2NL4taY9M9xIGKp9jDe86QY6nHqh_5NC40APVtQTjce2H__ImC2Lq5cg4wV_M4FIV8HT74GD8a2Omi-2ScO-NeJfVWKy4juV2ursnMPe4wPCRyyFBOhwcxaZSt_K19eqNPDYaFh2xPNWCtxaPVkGsfzD9HjpoNw1dUOEAa1gt2L5dwUtRK1ZqwLnklvD_oapAtVWVPp1MwRY303YWpXNmYeMOd3JzkN8652pC9oXLsGA8YPygvwRWMAOjSnN_5TQfx7PuMroEKnJ9xsHg86BqmE4X1-S_DrQcNCfv-aFMBxz6ZL8kytg5u584EmMGYBZm1Q0urIMc0a9doUl09oUuOGO6jmr4OlY-64O3S8yGaxZTbvD6O_lXYoocVrWzrtof_tYY_XpFGL7KCZeDI--lt22n6rdrdhS8lHpZXLHNvVcZIbTWrbxiAK24gaQLcZC30lf5NzG1iQKb-vRcdy0Y1FuLyt-NChh_LPMaJ5LcX_qAg7Cx4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ایران دیگه نیروی دریایی درست‌وحسابی نداره، نیروی هواییش هم نداره و ارتشش هم ضربه سنگینی خورده.
اگه توافق نکنن، دوباره اقدام نظامی رو از سر می‌گیرم و کار رو تموم می‌کنم.
می‌تونم تو کمتر از یک ساعت بیشتر پل‌های مهمشون رو نابود کنم و ظرف یک روز هم همه نیروگاه‌های برقشون رو از بین ببرم. این رو هم توی مذاکرات بهشون گفتم.»
بازسازی پل‌ها سال‌ها طول می‌کشه؛ خودم سال‌ها تو کار ساخت‌وساز بودم و خوب می‌دونم.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/69121" target="_blank">📅 17:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69120">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b8f908317.mp4?token=uOEIOJb0gS5nL8g4sYzXRIyfX6K_SgUCicXpmnicgzRwVsC7fd8dWpIocKJf7OcCT19qVlVsN1mywAbU-XAMkc3CGHgCC5ypeOUudSq7ci4z122SsIUfexs0H-9Dz6dS4BJSI6cMLlSqEEUX1AwXzVrTWB9VVjXt5aO9HC4MuIYgoXk2q-6hSay6V3RbUQ1sxJZJMH2Nx1kWUxvz71L7YfmW2HmObpFcnSCD4m20sMkc-bc9oMyshucP-Erna0YxycEZHjGoIiQcCOOrcrBymDKaxG186X71N1EUL3f5-H7uOP2-FaURVhz30hA-xuU6j0saiR4GD6TIC7GDJbIz97gofOsvQSf9_VxBrDe1IXRwg_yMRKnTej6hh0kA3A57r4I_fI6-EaHne_nqspcWoCVAHJ_yosf5nll38x3TAf5utKlJasW0CK-BbrNmlzMx5V9WVR8bmYZ23Em-HR0UU9VnHUu5cPL-rq2NoYSiPYwXJcS7ewOauOdcRN3bSGo9oALXtXF_AEW-KivGqbXMAb4xoSnXui7Dz3mifL-jxSEn3sTpUFYL2iv8ZE9qXUi_EQDjRuDe4n96hqb-Z1Hnn3KnJ1XbU2InxSUaS0Yitj98hWozH6IvzOI0T-43KYsYE6RmFJ9yCTUwPESPrW8W-MF7jAFQKyPsqVEVhiBJi5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b8f908317.mp4?token=uOEIOJb0gS5nL8g4sYzXRIyfX6K_SgUCicXpmnicgzRwVsC7fd8dWpIocKJf7OcCT19qVlVsN1mywAbU-XAMkc3CGHgCC5ypeOUudSq7ci4z122SsIUfexs0H-9Dz6dS4BJSI6cMLlSqEEUX1AwXzVrTWB9VVjXt5aO9HC4MuIYgoXk2q-6hSay6V3RbUQ1sxJZJMH2Nx1kWUxvz71L7YfmW2HmObpFcnSCD4m20sMkc-bc9oMyshucP-Erna0YxycEZHjGoIiQcCOOrcrBymDKaxG186X71N1EUL3f5-H7uOP2-FaURVhz30hA-xuU6j0saiR4GD6TIC7GDJbIz97gofOsvQSf9_VxBrDe1IXRwg_yMRKnTej6hh0kA3A57r4I_fI6-EaHne_nqspcWoCVAHJ_yosf5nll38x3TAf5utKlJasW0CK-BbrNmlzMx5V9WVR8bmYZ23Em-HR0UU9VnHUu5cPL-rq2NoYSiPYwXJcS7ewOauOdcRN3bSGo9oALXtXF_AEW-KivGqbXMAb4xoSnXui7Dz3mifL-jxSEn3sTpUFYL2iv8ZE9qXUi_EQDjRuDe4n96hqb-Z1Hnn3KnJ1XbU2InxSUaS0Yitj98hWozH6IvzOI0T-43KYsYE6RmFJ9yCTUwPESPrW8W-MF7jAFQKyPsqVEVhiBJi5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ما دقیقاً می‌دونیم تو تأسیسات هسته‌ای پیک‌اکس چه خبره؛ از حفاری‌ها، تونل‌ها و جاده‌های جدیدش هم خبر داریم.
این اصلاً مشکل بزرگی نیست. بی‌بی مدام این موضوع رو به من میگه، چون می‌خواد همچنان تو این قضیه نقش داشته باشه. اگه به توافق نرسیم، پیک‌اکس رو از بین می‌بریم؛ اونم خیلی راحت.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/69120" target="_blank">📅 17:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69119">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/825bd1594a.mp4?token=q1Kb5YzLSnD4hjtM9_5FYxtYgfdpB56en_lRyBpz5BeNg2GnST3j4h3YR-BFVbq_QWEEg3OwCcZEr5NRfx3N_Zd-YuM7A9w1wBSJrVhrNNAc-gk5DrIzzlFPC8OwkX35WvJDKQMvNEtVpJNs12tppy4Lj6Trhjon95KA_yOqqQaeWNwGy9jUwUnI2WiR3SEiphCWLzDO68z3hkDqQjeBGP6M-2dP_67Ln8zx_ffy1egUDsMGUinY38U7B340fuh1U9OC1zfayXBRSz_T90QWgHmyrDDN-oXdfHuypgCjoL4kr1hY0gRczzYiTxRijZQpyodCe1w5rqzDpjcds9ANEiasuxfw1fsmbXbZPvI2c6g6vjzIlN4Y96UEZ3LrRcJlnkOi1DPipQhcLIV-yWri7FQsSOmKmOTSjG3oGuJi931uv7hqlezZbnWR5QKBD7JQyw0eIE-Vnj8Ai2INNcTnyQcBlENGsF-VXw04PQOg4znYd6ZoG3DtTIEQCFOI6BIiaNyVXlufE37O4INP-0tLxrHJlkPd_b16Gt-s_BSC4Yfr7ANrhjee9iBMWy3zjHw931Lp8MLuC-tjN3PSYUS9vMpHdz_AjXXui4x7NQVWtLs6TLmAgbNZQCRVC7ZHBIoPDl04JE6BxVRhlZ9p3Js8zVOaM_g7G2UZtTKdsfcy7lk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/825bd1594a.mp4?token=q1Kb5YzLSnD4hjtM9_5FYxtYgfdpB56en_lRyBpz5BeNg2GnST3j4h3YR-BFVbq_QWEEg3OwCcZEr5NRfx3N_Zd-YuM7A9w1wBSJrVhrNNAc-gk5DrIzzlFPC8OwkX35WvJDKQMvNEtVpJNs12tppy4Lj6Trhjon95KA_yOqqQaeWNwGy9jUwUnI2WiR3SEiphCWLzDO68z3hkDqQjeBGP6M-2dP_67Ln8zx_ffy1egUDsMGUinY38U7B340fuh1U9OC1zfayXBRSz_T90QWgHmyrDDN-oXdfHuypgCjoL4kr1hY0gRczzYiTxRijZQpyodCe1w5rqzDpjcds9ANEiasuxfw1fsmbXbZPvI2c6g6vjzIlN4Y96UEZ3LrRcJlnkOi1DPipQhcLIV-yWri7FQsSOmKmOTSjG3oGuJi931uv7hqlezZbnWR5QKBD7JQyw0eIE-Vnj8Ai2INNcTnyQcBlENGsF-VXw04PQOg4znYd6ZoG3DtTIEQCFOI6BIiaNyVXlufE37O4INP-0tLxrHJlkPd_b16Gt-s_BSC4Yfr7ANrhjee9iBMWy3zjHw931Lp8MLuC-tjN3PSYUS9vMpHdz_AjXXui4x7NQVWtLs6TLmAgbNZQCRVC7ZHBIoPDl04JE6BxVRhlZ9p3Js8zVOaM_g7G2UZtTKdsfcy7lk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌐
هزار سال ایستادگی،
نامی در میراث جهان
قلعه الموت، افتخاری دیگر برای ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/69119" target="_blank">📅 16:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69117">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eoZNvK32BiGRYbd9N8IxbbCu-Q0cbX3XFjyvsOzmiJvz3gAf-WmJczk0ZhyrmiubysvT86pTEtTXjRXc9WBhv1SAjFiAfsW7tu5u7wCnlQsyyrz_iPZ2fLB08o3KmIAuYY_ByIT0NyNVnA8wbuuHjhJxnSpYVrVAZxBGFpI-mz8ISrxSU_EYdarYNt6SAN1s6GPiGMJdVLXsMcusgBbnm2AzaZrhxfThtoBB4u-x6TW7J4TtoQm0qqGO0KfOS0A6q9350Y8uJTiFeeZNWNo1i3XrfIiDbuxmMNhs0PsluuHWkbcJ-lsdo1wTcM7sADATmADFouG8Ptu-IwsTVxHSag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fUOxOvWUip8Q19bkLnDCt_Dy4AMdbaYQNcr2TIEec5_i4MCnBScc9MOjSaFpNCXsvFBC6yHCNExIHa0pg5B5dvIz332aMt_jlCy8-sMPjPsMABtNCucppi4mWXgTyEbFDz3f1Ngp4eyldHSR6zxewPTE1rNifeNBU_9j5s-7JPKZWxKVqGxCfwsIbQn1-qll4bFnNtC1FZxqQscdktb2UMAkdGcZqSc2-90B0LZOUNWKl2l8f7nG5G29TeYtj36t8NwrN7SSlWP0t8gbgJFMw-1SOL1gItBp4dhoVB2ZkKNh8aH1ci3bWuL4NoPI8RtWEX7GkGmO16clzJHaU_lKdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
🇺🇦
❌
🇷🇺
اوکراین بیش از ۳۹۰ پهپاد را در طول شب در منطقه مسکو به پرواز درآورد، که به نظر می‌رسد تلاش دیگری برای حمله به مراکز لجستیکی Wildberrys باشد، اما در واقع به جای دیگری اصابت کردند.
در Kaledino در نزدیکی Podolsk، یک پهپاد باعث آتش‌سوزی بزرگی در یک انبار لجستیک شخص ثالث به مساحت ۱۸۳۰۰ متر مربع شد که به Auchan، Magnit و سایر زنجیره‌ها خدمات ارائه می‌داد، درست در کنار یکی از بزرگترین مراکز Wildberrys که به گفته Wildberrys به طور عادی فعالیت می‌کند.
در Chekhov، یک پهپاد دیگر به طبقات بالای یک ساختمان مسکونی برخورد کرد و به بالکن‌ها و دو آپارتمان آسیب رساند، اما هیچ آسیبی گزارش نشده است. بقایای جداگانه باعث آتش‌سوزی تایر در یک کارخانه بازیافت لاستیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69117" target="_blank">📅 16:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69116">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0df10b659f.mp4?token=a_ov2qWDXjkR6T_cV-PBlESKPkMsppNBpPpQstQLX7bgq-H-DXamhoe5O0hs0MRvqNB8s1D9-bBXzym3zkoDnVAr473W2JUn8hSZdSeXbQKJnfHNW-bJpbYDnQKqa5Xc0IulklKfFEa46DwKlAntQ2nKp6CgZ3c6CDanICQA3dvi1FuuyBtBo0xuUdbUNcaF5wkYt_673v85BrZ91buA8Qcbn4EaF9eyNrc3fR9dKTRvldFn8-wtSLNmSZylMeiXQwPfLOoB0v5nbFdFau4Ab7k986kGOrPZIgK_2DRln77K6Um6NZq-RvtPAUaF6Tpyk0I_V5kawgiIdXuVEUYX_Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0df10b659f.mp4?token=a_ov2qWDXjkR6T_cV-PBlESKPkMsppNBpPpQstQLX7bgq-H-DXamhoe5O0hs0MRvqNB8s1D9-bBXzym3zkoDnVAr473W2JUn8hSZdSeXbQKJnfHNW-bJpbYDnQKqa5Xc0IulklKfFEa46DwKlAntQ2nKp6CgZ3c6CDanICQA3dvi1FuuyBtBo0xuUdbUNcaF5wkYt_673v85BrZ91buA8Qcbn4EaF9eyNrc3fR9dKTRvldFn8-wtSLNmSZylMeiXQwPfLOoB0v5nbFdFau4Ab7k986kGOrPZIgK_2DRln77K6Um6NZq-RvtPAUaF6Tpyk0I_V5kawgiIdXuVEUYX_Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
بخشی از صحبت های دیروز ترامپ در میشیگان به زیر‌نویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69116" target="_blank">📅 15:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69115">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/200b5b3122.mp4?token=QSYuo6Be38_y4XTm50hWgzgzbbXo5P86q_he86J3QWTPcDafarPkJrMkf8BS0nLOB2YqumhyJ09CJBlpVog6edOBKRj9Ud_gXm0p28sdAxYc3wMuAIC6ChUoXZkJZil-RbfNMJpnrvHErG9KkrD4V2MTNHqDNBC4UZzHuujcEC3rZyeR20Cj57GxQLzIZBUGMGiFiUvUKhzmBlSIWhuI18c1rdtHTlZ4ssPksvuuEjnCoZRB7AQIvt9yOyLcAVz8D6dJCY3IGmHXx4IsIemjparJkVsDv0DsGpdyU4PVwAkiiHlzGH6YufL0Q5YAmgLNObgwIM49ByZ6nFZ0pcwB7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/200b5b3122.mp4?token=QSYuo6Be38_y4XTm50hWgzgzbbXo5P86q_he86J3QWTPcDafarPkJrMkf8BS0nLOB2YqumhyJ09CJBlpVog6edOBKRj9Ud_gXm0p28sdAxYc3wMuAIC6ChUoXZkJZil-RbfNMJpnrvHErG9KkrD4V2MTNHqDNBC4UZzHuujcEC3rZyeR20Cj57GxQLzIZBUGMGiFiUvUKhzmBlSIWhuI18c1rdtHTlZ4ssPksvuuEjnCoZRB7AQIvt9yOyLcAVz8D6dJCY3IGmHXx4IsIemjparJkVsDv0DsGpdyU4PVwAkiiHlzGH6YufL0Q5YAmgLNObgwIM49ByZ6nFZ0pcwB7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی تحلیلگر ارشد اینترنشنال:
جمهوری اسلامی فهمیده که ممکنه آمریکا و اسرائیل یه حمله شدید انجام بدن و همه مقامات رو ترور کنن.
بعدش مردم بریزن توی خیابون و انقلاب کنن، برای همین از قصد داره معترضین رو توی ملأعام اعدام میکنه که باعث ایجاد ترس بین مردم بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69115" target="_blank">📅 14:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69114">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c00215915.mp4?token=pNuDzUjfSr6TwK4iLrQSDId_Hx70byDlTy67BRHGsh1zuCeL--u6j3RAY6_YOVCP7wtiXvFshVfxsFMTbmcE3V9HtHxL4riNdMoXTdGW6-8Pkspw-_E7U3QoQ1_cxAytk6lApYG0MWuoqipwDFBBvmqoXGUARaFEaJ5jaDcDypcmzs1Hz1emqhzAlcz4lz69zwHpUH1po2Es-jtgUs3lSc1ny9S-uNGVXs8LFYgEZ7GkD9NXLSgQl3H6TJm79-CmKgkpksJT_uqyCQMwnjYBu9qLwYOcKEd0yuLaaU_OvEj4VR-tQT-JA0kKUurB_8axgVUxLHk2YKLx4PfcsVT_JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c00215915.mp4?token=pNuDzUjfSr6TwK4iLrQSDId_Hx70byDlTy67BRHGsh1zuCeL--u6j3RAY6_YOVCP7wtiXvFshVfxsFMTbmcE3V9HtHxL4riNdMoXTdGW6-8Pkspw-_E7U3QoQ1_cxAytk6lApYG0MWuoqipwDFBBvmqoXGUARaFEaJ5jaDcDypcmzs1Hz1emqhzAlcz4lz69zwHpUH1po2Es-jtgUs3lSc1ny9S-uNGVXs8LFYgEZ7GkD9NXLSgQl3H6TJm79-CmKgkpksJT_uqyCQMwnjYBu9qLwYOcKEd0yuLaaU_OvEj4VR-tQT-JA0kKUurB_8axgVUxLHk2YKLx4PfcsVT_JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مهاجرانی، سخنگوی دولت:
تو بنزین سهمیه‌ای فعلا تغییر قیمت نداریم، ولی هر وقت تصمیمی بگیریم، شفاف به مردم اعلام میکنیم و اونا هم همراهی میکنن.
فقط مقدار سهمیه دوم بنزنین (3,000 تومنی) از 70 لیتر به 50 لیتر تبدیل شده که اونم بخاطر حمله دشمن به مخزن انبار نفت‌مونه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69114" target="_blank">📅 14:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69113">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd184b2451.mp4?token=m25FPkNurjzGVGgs5uW3kH8yaywCqsRJS2zbWXzaB6UPVhjomXQej_kr-YYQnIKCPJgpujFIGHpQnvtNprR--B5FFAD6noSzYJYXYgd8EPJC-QT7V5FDMXJNkoRzmpB98uw-Pnrk8xoOOomAQb0a_Cp5w6fGvqobgByoVO3EcBYOHD_z9tk0fcvQOhGABze6li-pSSQgH6qkV_tGhumvTykIu4mJWsBQgnQSQJ96OYDpY0afwXaJtANNaWQJnGQco_AdOAgRKFw66oP3qZzMjGunllD99Z1I6pzuNGsznr74_t-_32RiWGFEG2m09nC6vSn_j04jdep03SASxTRaHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd184b2451.mp4?token=m25FPkNurjzGVGgs5uW3kH8yaywCqsRJS2zbWXzaB6UPVhjomXQej_kr-YYQnIKCPJgpujFIGHpQnvtNprR--B5FFAD6noSzYJYXYgd8EPJC-QT7V5FDMXJNkoRzmpB98uw-Pnrk8xoOOomAQb0a_Cp5w6fGvqobgByoVO3EcBYOHD_z9tk0fcvQOhGABze6li-pSSQgH6qkV_tGhumvTykIu4mJWsBQgnQSQJ96OYDpY0afwXaJtANNaWQJnGQco_AdOAgRKFw66oP3qZzMjGunllD99Z1I6pzuNGsznr74_t-_32RiWGFEG2m09nC6vSn_j04jdep03SASxTRaHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:
نتانیاهو به دستاوردی رسید که چرچیل نتوانست به آن دست یابد.
او ترامپ را با ما همراه کرد تا به ایران حمله کنیم؛
بدین ترتیب، پیش از وقوع یک «پرل هاربر» دیگر، ایالات متحده را به اقدام نظامی واداشت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69113" target="_blank">📅 13:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69112">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/136b2d25c6.mp4?token=VWIDBFBET5F4SP_kbr4C9k5La92hBYOzlzJtdX5Y2-J_qBeChUIawrGocGOqwHPaL_f0mMRw18Yv_bgngxf0KgToeeDq-Z2xNdvkEM8o_v59exM1h5BVZ9npsmEaazV5gSmNkENLY7DAdQ7ZDanZsMXe1bRGWfGbZGeQLOu_k2PRuBAYLBHUgdMpYLmQ2Z8dHTd5CdcEE4wUWZIJt5FKl6sQTNrARyez3C2RFj5MwhTYW5cc9DSVy6CulGXVOskhN8GGtlEiwt3aDdsSKNWjXw-Q6H061gZCNz82U2wFONMQdL9vPMi1jr2490lXVpJWsdAoJGxyOrtI0eX-cMZ1nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/136b2d25c6.mp4?token=VWIDBFBET5F4SP_kbr4C9k5La92hBYOzlzJtdX5Y2-J_qBeChUIawrGocGOqwHPaL_f0mMRw18Yv_bgngxf0KgToeeDq-Z2xNdvkEM8o_v59exM1h5BVZ9npsmEaazV5gSmNkENLY7DAdQ7ZDanZsMXe1bRGWfGbZGeQLOu_k2PRuBAYLBHUgdMpYLmQ2Z8dHTd5CdcEE4wUWZIJt5FKl6sQTNrARyez3C2RFj5MwhTYW5cc9DSVy6CulGXVOskhN8GGtlEiwt3aDdsSKNWjXw-Q6H061gZCNz82U2wFONMQdL9vPMi1jr2490lXVpJWsdAoJGxyOrtI0eX-cMZ1nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:
ما بسیار مشتاقیم که به تأسیسات انرژی ایران حمله کنیم.
ایالات متحده در حال حاضر با این کار موافقت نمی‌کند، زیرا نگران است که ایران به کشورهای همسایه حمله کرده و موجب بروز بحران جهانی نفت شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69112" target="_blank">📅 13:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69111">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🇮🇱
کاتس، وزیر دفاع اسرائیل، به شبکه ۱۴:
جنگنده‌های آمریکایی برای انجام حملاتی در ایران از پایگاه‌هایی در اسرائیل به پرواز درمی‌آیند و ایران نیز از این موضوع آگاه است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69111" target="_blank">📅 13:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69110">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‼️
❌
آی‌24نیوز:
طی 48ساعت گذشته حدود ۲۰ پهپاد توسط شبه‌نظامیان مورد حمایت جمهوری اسلامی در عراق به سمت اسرائیل، اردن و عربستان سعودی شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69110" target="_blank">📅 12:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69109">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2c6cefb08.mp4?token=v0AntJtf7ztQb6nAm1WR3OuSKiUUFPDxVKT40ssc0w3CDH8ukpFYDN1lY-hr7QPlmEApGXL-KuIgBok-XvFABDrfNBwlUg3A8flUhJfgT7mj9ZsCWh5SvJcgYSOk4ZUm1hrBBazT5ufaphFYZUrQ6akNANg0tSgcF8ujw0AL2YPLOoOnhe8-EyiSvnb-M0WAZ6-cC3g_5p2TNRZY9BOo0XwNrFAMHi-8A272AhLl_LxzJikcGWoNb_njEhmP8MLDFsn7u-N8tlBidoSp_0XyUNuPAmU2UmXcK7djbpEz1EdEi6CFYzOwlsjCuVtAiqJ2Rfoy8vl7equ5lu85BOdZmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2c6cefb08.mp4?token=v0AntJtf7ztQb6nAm1WR3OuSKiUUFPDxVKT40ssc0w3CDH8ukpFYDN1lY-hr7QPlmEApGXL-KuIgBok-XvFABDrfNBwlUg3A8flUhJfgT7mj9ZsCWh5SvJcgYSOk4ZUm1hrBBazT5ufaphFYZUrQ6akNANg0tSgcF8ujw0AL2YPLOoOnhe8-EyiSvnb-M0WAZ6-cC3g_5p2TNRZY9BOo0XwNrFAMHi-8A272AhLl_LxzJikcGWoNb_njEhmP8MLDFsn7u-N8tlBidoSp_0XyUNuPAmU2UmXcK7djbpEz1EdEi6CFYzOwlsjCuVtAiqJ2Rfoy8vl7equ5lu85BOdZmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇦
گویا زلنسکی هم در آمریکا حضور داره و قراره با ترامپ دیدار داشته باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69109" target="_blank">📅 12:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69107">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hHJAxENHoG2GTaMyK7YIWt-fPYJWTJONNBIbFMnGpOddlwkwc1mbI4VpzjonCRGonVeAOawB-ScxiveItAsnnRyoMS-fcvojoUszz4QyQNnQRWs7rXmFaGb3KxppZRi-lgGh-5FGtsaRTrrjfJfTjvFwj6QPrKuznzCbAtdilk4eewx2AYWTW1kUfriHhbjJPxpeSntkaM-9uJEt9U0pszEBDbE8u68oCLecB98H6DPNr4LTGbcISopW88mXRnPkvsAdfAWBoUhfheafnGlp7U1jBeiOlsMcai3TkxKMGz6JybmrV8aDig9MW0es6QypaUNAIywoqstZzU1DkeN9kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KRAUeL3mS7OTm6T0MO0HWi5HJAUDHkGH_19YszgBLaS54ncb7izSPaj4HFUs0zlInN2T2vQYBiaE9B9JDWx6Q-kwpe4B1rYmP7Cdqz5et1tswaLEQIACFU1ZuDA7Z2qgV5kS4yRCZoIcZVKF6dVlt4lyT4nLO5Gr5pC6lpBAlQl9KBuF0bfD77U-GgaOHtnsuLuNA0y90P3MdWpH4OcJzABm-3yBpiRLre8GEeYMO0WPgJP2qruz0v-f3iFCx3hfiIc81n2DpTd5YnZovYaGWijc2lVKQJpJJn7GJsLfDDxe_rVTWpfA_f99sVvDA9sZz7O-3bmAWR39cGcClJRy0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تو‌ جلدی که مجله اکونومیست از سال 2026 منتشر کرده بود؛
زلنسکی
🇺🇦
درحالی که دوربین دستشه، داره به یه کشتی ایرانی نگاه میکنه!
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69107" target="_blank">📅 12:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69106">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f0b26c19f.mp4?token=Y5KYDk_QKaiLteCgGuTQPTFn7qGQCW-v7ByZKKATP_L8C1gaL2ObUCLGczNQEmeJZLSou1e-0Tl_BWq_QGOISknfak6BB8D3VfWZC5jawTYOLh59j7IYbstqmri5JqFYercNd89lnZBbMNzl2FlMHgETFJ7Z6uU07HeAYZqwt0drCajZ5G1lBgd-q4OmIf1hJQBKtoTP64LoSW1Rb_X_4vPJCiTYefYqG0bx6rl_NeY6TnDRJkvv2x0vEmddQefdO9mzJn9qqc1Gb7evsVRvHlQXcRJX5cQGzYtvW_kyAsUmYH653zB7IRUrDCYYF31EYsbD8kakBSIXIkYHZ-6b9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f0b26c19f.mp4?token=Y5KYDk_QKaiLteCgGuTQPTFn7qGQCW-v7ByZKKATP_L8C1gaL2ObUCLGczNQEmeJZLSou1e-0Tl_BWq_QGOISknfak6BB8D3VfWZC5jawTYOLh59j7IYbstqmri5JqFYercNd89lnZBbMNzl2FlMHgETFJ7Z6uU07HeAYZqwt0drCajZ5G1lBgd-q4OmIf1hJQBKtoTP64LoSW1Rb_X_4vPJCiTYefYqG0bx6rl_NeY6TnDRJkvv2x0vEmddQefdO9mzJn9qqc1Gb7evsVRvHlQXcRJX5cQGzYtvW_kyAsUmYH653zB7IRUrDCYYF31EYsbD8kakBSIXIkYHZ-6b9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
ساعاتی پیش بی‌بی‌نتانیاهو به واشنگتن رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69106" target="_blank">📅 11:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69105">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0eb0677cd.mp4?token=iRJcMlnRxYatdykcZNEjYZccrPj5LM9FO177BaP0-x7O6J14qccfuvN44dLcr9asQDuX1xFk84q6rwxpvZYLSxJKJLIBcHCGwOU8nrg-8wdF-h8TtSGJT3QM6txb2B-DRjk0_yZJDYHtLIYCvZFLDuDzykaF3oqAqUthqz7sXRB_ZpT2KA4KlAXoS-cvXY3jhX1-7F7SZelrFi0vzj1Aur2wHk3h8CtWlvUxWD_DXToPR57eHgmcK8U5Z_R9kJT0SFt3hvAtfWZKNN9bJxG5PrdapFYVljxG4KmWW9TRZwJHYLjlR-oqR-FS1BiALsx_zsxU0hW_po8LIiBgDAn5okW6eR-YmWZBVWse9Nhg2h9vwTeKv6VhkkgK2bXUIFIS7TQAAIQvKrMNOGwXvWr2IB8gZJtwO_FsxMPdg1IujYNx39UgzwI1tWS_DzfK3xo8tl0tlCPI51RBalGa89d0LlCp1QcuZjORjY_tK6YCr-5-V4m0LYcwq33GrnIC2GoNiLBK9-X1z2dXZgFEBIwllVlC3YICp-s9VZUGYu3HHg_GqLEycMx86oW8Si_VNDvbOQSs-pk_zQ6NoavE3ujYBgzQW-M1cbNGMPGuCATdX6IH6mVXNR_4cmigIQxvdTqQLoqDwK42cIZxl221M7FpesBw1bDIeryLGAaPwA7HwyY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0eb0677cd.mp4?token=iRJcMlnRxYatdykcZNEjYZccrPj5LM9FO177BaP0-x7O6J14qccfuvN44dLcr9asQDuX1xFk84q6rwxpvZYLSxJKJLIBcHCGwOU8nrg-8wdF-h8TtSGJT3QM6txb2B-DRjk0_yZJDYHtLIYCvZFLDuDzykaF3oqAqUthqz7sXRB_ZpT2KA4KlAXoS-cvXY3jhX1-7F7SZelrFi0vzj1Aur2wHk3h8CtWlvUxWD_DXToPR57eHgmcK8U5Z_R9kJT0SFt3hvAtfWZKNN9bJxG5PrdapFYVljxG4KmWW9TRZwJHYLjlR-oqR-FS1BiALsx_zsxU0hW_po8LIiBgDAn5okW6eR-YmWZBVWse9Nhg2h9vwTeKv6VhkkgK2bXUIFIS7TQAAIQvKrMNOGwXvWr2IB8gZJtwO_FsxMPdg1IujYNx39UgzwI1tWS_DzfK3xo8tl0tlCPI51RBalGa89d0LlCp1QcuZjORjY_tK6YCr-5-V4m0LYcwq33GrnIC2GoNiLBK9-X1z2dXZgFEBIwllVlC3YICp-s9VZUGYu3HHg_GqLEycMx86oW8Si_VNDvbOQSs-pk_zQ6NoavE3ujYBgzQW-M1cbNGMPGuCATdX6IH6mVXNR_4cmigIQxvdTqQLoqDwK42cIZxl221M7FpesBw1bDIeryLGAaPwA7HwyY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تسنیم این فیلمو راجب
ملانیا زن ترامپ
منتشر کرده تا اگه کسی قصد ترورش رو داشت از این اطلاعات استفاده کنه
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69105" target="_blank">📅 11:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69104">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76bcf42cd4.mp4?token=WY10LUARLoE-CkU_-LbkcqjkeCK7Ca6mR4cLmW5nqgQ-WwrZHyvfbfy8lSHB8J3_DVIMkpq5t3ww7Ydv7Na5bUKqueWd2KP5rf3tBTSKun337WQNgptSidD8aUkf_pqi8QkMvf2a9pWwozh7mK-6fDRWwddb1hd2Qy9pUexqmUcb7lbPas7cqk5W48d3xnAhK_htUuBziUaNJFzlOl3vvhZp5alh9e_dnM9f9QuajAW39d5S6v_fjlWyfluywi_YrtBEgX1zn7IpuQtSmjJF02swxSnQiA_TBgVOZCMSmhAiG9rFYJvw6j25YQuKqo7r6nx4w_yaOvgxQZ4FpD6UnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76bcf42cd4.mp4?token=WY10LUARLoE-CkU_-LbkcqjkeCK7Ca6mR4cLmW5nqgQ-WwrZHyvfbfy8lSHB8J3_DVIMkpq5t3ww7Ydv7Na5bUKqueWd2KP5rf3tBTSKun337WQNgptSidD8aUkf_pqi8QkMvf2a9pWwozh7mK-6fDRWwddb1hd2Qy9pUexqmUcb7lbPas7cqk5W48d3xnAhK_htUuBziUaNJFzlOl3vvhZp5alh9e_dnM9f9QuajAW39d5S6v_fjlWyfluywi_YrtBEgX1zn7IpuQtSmjJF02swxSnQiA_TBgVOZCMSmhAiG9rFYJvw6j25YQuKqo7r6nx4w_yaOvgxQZ4FpD6UnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری :
کراش فوتبالی تو دوران نوجوونی داشتی؟
⏺
غزاله اکرمی، بازیگر :
آره ، غلامرضا عنایتی
خیلی زیاد دوستش داشتم ، نمی‌دونم واقعا چرا به شدت روش کراش بودم!
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69104" target="_blank">📅 10:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69103">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TXnhHHBKCUdUWL9w-t8r0ESl4_5sjyOVvhi8NANbfYtfQS4LyJ9IYfd9u-kmkfh76nWT2ont87m-HnBQWJKkl-Vsh3TFCW1ixawzDaVni8hfvlqCaSEjV6fEWSSv3fE1lq9Cz58QhKAyn8gwh1AkP1asheEpmY1Q2Wc2MW64fl9206gmHPR4q9bfarCuclNo5y770eVsL7TD6h7WuYNE5NoRKtC9DAXmmZgLrYQtbF_1pO5f87Boty6eQAmdIx9YtxT8NPr29vHmCBmfUkp3Cw108hpp-ZI6_cHCX42B7OSOHIt6wZHUUw12IsQ_BBIBFXzpIg1S7VS58rtDcpAUrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به کشاورز زمین داد، چریک شد!
به زن‌ هویت داد، آنارشیست شد!
به کارگر سهام داد، کمونیست شد!
به هنرمند اعتبار داد، توده‌ای شد!
به مسلمان حرمت داد، تروریست شد!
به دانشجو بورسیه داد، مارکسیست شد!
به اقلیت حقوق برابر داد، جدایی‌طلب شد!
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69103" target="_blank">📅 10:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69102">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b88a652ec4.mp4?token=JNZrhWkMmprNg4y7P0t_zQABMXBDytNA-JR6R9ytesadvSawQgYfB0ientjPmYgnW6h52sc2DZYqU_RgUfssob6l0-MSouoMTQflFsk0Aj1ENz30DasQmzFwV3ZgWeD8V0_Uf6C_fJi9LcrC94GTJ0yBELjdEtbB8nZnZeYqMMe303KNCpz_I0sEBvOIsWlL6EqHgExD8L_SbZ7ZPOgnEe_1d867jv60_e0fhcaRrOVqoQJzp0yhgGezYmK3J4gTIGeyJW8HD1TxYc4vxhEFanR1kw6B6t5Bnn-ll0b8EpTF0zqvYyr4pE4xr72l3DfPcF2adNga29NIGVDJDaKhsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b88a652ec4.mp4?token=JNZrhWkMmprNg4y7P0t_zQABMXBDytNA-JR6R9ytesadvSawQgYfB0ientjPmYgnW6h52sc2DZYqU_RgUfssob6l0-MSouoMTQflFsk0Aj1ENz30DasQmzFwV3ZgWeD8V0_Uf6C_fJi9LcrC94GTJ0yBELjdEtbB8nZnZeYqMMe303KNCpz_I0sEBvOIsWlL6EqHgExD8L_SbZ7ZPOgnEe_1d867jv60_e0fhcaRrOVqoQJzp0yhgGezYmK3J4gTIGeyJW8HD1TxYc4vxhEFanR1kw6B6t5Bnn-ll0b8EpTF0zqvYyr4pE4xr72l3DfPcF2adNga29NIGVDJDaKhsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ارزیابی رابرت پپ از سناریوی ورود نیروهای تفنگدار دریایی (Marines) به سواحل جنوبی برای تصرف محدود نقاط بنادر و عواقب آن.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69102" target="_blank">📅 09:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69099">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JgmZNJm7T4Bt-bn-hQgDHGF4OqtsI_dMiQ_NCr99FaBkC4uTX2RUaBaRsR6-5TWRp1Qlu412qo-R1q5dT_rvSabhUrU7ZM_lYB_hG9kz4YKs9M8mGqBlMYo_n3_mFJpOc2ViHWlUb4xvLf0vgdG0mMKbXC1ROY91GgggtjksqVRAy5ZYmmD_5yA7rufgD1TGgL-xoqVLtxgKsLs0FkpyQoELT7LFKyXFJ7e5uLcMk7-AGFnTNWdAWQ6OnlI9u7IagnAMK-xFkOz53XxOWaPjLQdwPELf6CT1PBbvTV6WeWNC0nKcvh-LIFZSkdRNlsA_krdvzspnN4Z2aTt88Ol0XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HEq3JUezKwjUfadCj9wC2s9uxyYQS-X8KobUXI4qBbRtu4-Z4rxW-IW9KhFla-6LyfVSY3mX7VbhNjXokNxlvQjPrO3g0FXu3kEcFcX37Q1y_AvcnUWpZAZSEelwnWhAhjClu85nML6zCTp5RpNQxdOkd9bwCYUAylt_runoG9M7R3F1pPOlX3Dg6rOFXRJXVZhjAqI5PJOBb_UXFrxsJxdxRGEfvGtURVklDeQ_gdQBmWYIpKfFaIocPiOOZWpHdy2L9M4dlRJ0-q9p6fwirLkA4QD_QWku9MZxNXmroFMXUQyEG9el5RiLahWEa4_DgJuOoq6a66pfRtsriMhz5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادتان گرامی جانفدایان میهن
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/69099" target="_blank">📅 05:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69098">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">#رسمی؛ جمهوری اسلامی دقایقی پیش، پس از اذان صبح، ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری را اعدام کرد.  @HutNewsPlus</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69098" target="_blank">📅 05:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69097">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">#رسمی
؛ جمهوری اسلامی دقایقی پیش، پس از اذان صبح، ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری را اعدام کرد.
@HutNewsPlus</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/69097" target="_blank">📅 05:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69096">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">متاسفم برا یه عده که ذره‌ای شعور ندارن و چند ساعته مدام در حال پخش انواع فیک نیوز هستند، بهتون کاپ طلا می‌دن که خبریو زودتر منتشر کنید؟!
#hjAly‌</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69096" target="_blank">📅 05:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69095">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9f40f91b5.mp4?token=tZgtx_HVaHjVg2KbIrpvQWPdxw8FI1irz5h2WlgPCO5xFJIE3pEwADzFbUXa_uogpW-hyMmmEVVDX9R0k5jtDSUz4oQmSlW-ZJivQkQ0wL4MEMe_TD9qJuc_xFsBN3JyWhNGAdDXab5XhhlNMxvT0X9LsCySFaLo2DE0p_n_aAJmUcuoxVroSIkw0SLKUxsX8R7qDRMrNsNi2fea3LG2HMV7olPnt5jpkJeMeFtIWZiHaM0Sk7PrDHYoeI6r7i7-JZ2QPoW34sTmOa3B3552bsfyvA45lGwmJbPJG5D2PG9WVVceHXxfKvKdtXjc_9rU8bLuuLdOkZpEu7dZzvpMgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9f40f91b5.mp4?token=tZgtx_HVaHjVg2KbIrpvQWPdxw8FI1irz5h2WlgPCO5xFJIE3pEwADzFbUXa_uogpW-hyMmmEVVDX9R0k5jtDSUz4oQmSlW-ZJivQkQ0wL4MEMe_TD9qJuc_xFsBN3JyWhNGAdDXab5XhhlNMxvT0X9LsCySFaLo2DE0p_n_aAJmUcuoxVroSIkw0SLKUxsX8R7qDRMrNsNi2fea3LG2HMV7olPnt5jpkJeMeFtIWZiHaM0Sk7PrDHYoeI6r7i7-JZ2QPoW34sTmOa3B3552bsfyvA45lGwmJbPJG5D2PG9WVVceHXxfKvKdtXjc_9rU8bLuuLdOkZpEu7dZzvpMgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مردم دارن شعار سر میدن
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/69095" target="_blank">📅 04:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69094">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دفتر رضا پهلوی از جامعه جهانی خواسته هرچه زودتر برای جلوگیری از اعدام معترضان در اصفهان وارد عمل بشن!  @News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/69094" target="_blank">📅 04:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69093">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دفتر رضا پهلوی از جامعه جهانی خواسته هرچه زودتر برای جلوگیری از اعدام معترضان در اصفهان وارد عمل بشن!
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/69093" target="_blank">📅 04:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69092">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">لحظه‌ی اذان صبح و آماده‌سازیِ شرایط اعدام، در میدان علیخانی اصفهان</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69092" target="_blank">📅 04:06 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

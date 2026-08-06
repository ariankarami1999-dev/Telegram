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
<img src="https://cdn4.telesco.pe/file/GBIFt5_l3E5RvyyurTKJXJqGSAxjUXZ4GtnuSkx76JLzPmlA7xjEdc551rw_WB5mWZSBIliwPzZuql9725tHLiqDL1dMvC0W4d8VeOVZ3vtqym1J35OId01CDRp9odD1MZcqGe8GXK249aiEHnVIjcH8hbHgXxkP6ga1A05gxv2usVDQcsmJzuVmuGGHbJIRAe9dq3-bjscYe5KewdUkuelfl2NqiuwmJzV-JuJQ4WmYHTtUctm1mv9VulBt2R4GPAOosvH1SaSD3IPbFkUVbaR2UNOraSHeOyyfq1GzRHU1x0u4nFqYU3gw8Z8LTYlc2eDAWIUVkf4fVjw2-QjY4Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 636K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-15 13:59:38</div>
<hr>

<div class="tg-post" id="msg-27201">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97dd42f0c8.mp4?token=XWeIK-sOwb9H3FFDVN1n9ghLAOj_SJsQDQEo8Mgq526i0Sh_idqzjbPEf5qZtNNrsr6Gh7mnxaXUKunS_XWcKD7Hnkwb86A-m3mzXSNTs6Xny0AF0_s9lxmGB_rNacKaXdt0R8NJ0ygFY8irQThaC7Okc_t2KpFc2BO2vaQ_IyQ3pt0BrBvSInf6G0qc9iFr8cho34G2Q_lHes_UUkxlFcQutnaT-yanDXzCUwtxD-qP8dLqaFmsWAJputn8wDDK_QqVtUJ4UONE_eFhMLGiPhpdYvsNzyy2bh-a4qtrOoKEeBAt3QdvDY0-fbsjGn8Nw5opKEaEG2cwFTOcfzDICw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97dd42f0c8.mp4?token=XWeIK-sOwb9H3FFDVN1n9ghLAOj_SJsQDQEo8Mgq526i0Sh_idqzjbPEf5qZtNNrsr6Gh7mnxaXUKunS_XWcKD7Hnkwb86A-m3mzXSNTs6Xny0AF0_s9lxmGB_rNacKaXdt0R8NJ0ygFY8irQThaC7Okc_t2KpFc2BO2vaQ_IyQ3pt0BrBvSInf6G0qc9iFr8cho34G2Q_lHes_UUkxlFcQutnaT-yanDXzCUwtxD-qP8dLqaFmsWAJputn8wDDK_QqVtUJ4UONE_eFhMLGiPhpdYvsNzyy2bh-a4qtrOoKEeBAt3QdvDY0-fbsjGn8Nw5opKEaEG2cwFTOcfzDICw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش پادکستر هوادار محمد صلاح به انتقال او و پیوستن به ترابزون: این چه خبر مزخرفی بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/persiana_Soccer/27201" target="_blank">📅 13:47 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27200">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‼️
واکنش پادکستر هوادار محمد صلاح به انتقال او و پیوستن به ترابزون: این چه خبر مزخرفی بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/27200" target="_blank">📅 13:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27199">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dab647f68.mp4?token=aueVIhvA1IobEEs2f4KMcSdLZVrAMZbDECEEJZnJm_2h_cuM_sso6k0V-VUGmCjDO34FUK-WCyHertzuYSbyb9qJQXuj1mAzpgCYY5t0Iqv_VkW4zi52wOd-OoiLBLmG5uywSCJKvP82LvA8wblgrkRKhegWoTD29JiOvFYZEx2RzeBVI9cPaVRgNoRwgliCVzs4p8PtUIu9dXzGZozrQKntFYRwrIwNeQbRrMimkIRwfgUQzrZ2LNo0P4I-ueePMx2_rB4dBMsUGau8V-43ste8Rec8in9I4ztxQ4P37dZ5arj1oCNpoDLsbZ9y1RU5bBuGO29iTq-vsjyu6aVfFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dab647f68.mp4?token=aueVIhvA1IobEEs2f4KMcSdLZVrAMZbDECEEJZnJm_2h_cuM_sso6k0V-VUGmCjDO34FUK-WCyHertzuYSbyb9qJQXuj1mAzpgCYY5t0Iqv_VkW4zi52wOd-OoiLBLmG5uywSCJKvP82LvA8wblgrkRKhegWoTD29JiOvFYZEx2RzeBVI9cPaVRgNoRwgliCVzs4p8PtUIu9dXzGZozrQKntFYRwrIwNeQbRrMimkIRwfgUQzrZ2LNo0P4I-ueePMx2_rB4dBMsUGau8V-43ste8Rec8in9I4ztxQ4P37dZ5arj1oCNpoDLsbZ9y1RU5bBuGO29iTq-vsjyu6aVfFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های‌ تامل‌ برانگیز زنده‌یاد علی انصاریان ستاره فقید استقلال و پرسپولیس درباره حسادت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/persiana_Soccer/27199" target="_blank">📅 13:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27198">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvNjLfRyeImK5bzcYjtwxIxfqUsEV7rQZmN_t7Zhrz1pQ9ggw0ZDi6Oa9lDyhLy5SCXxR-LrEBA754g0C-ttfPh9cfRKoal0PeJtksidMtgpVnFZKIKqGPK-F-e8sN9QVJQwKZTwqe9mGpX2gGN_-s4AHgdIMBxJRynKaI3n8ASQqFzdy8vEASbaesw_DsbtJ6dkic6kyJs7Fja-f1aVNCuCqu7RLcayL3xqTNu8NdGUaNXXK1lAMfWU_YNSBKOHUc22mQH2O1NOOQVKWwhYpgivlcE6MR5yas9Ugz1R0X9Rz-Akm7um2pRMVv4PVWTIWbYCbFXDqy9oRpWTj-HLrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخبار دریافتی‌رسانه پرشیانا؛ بانک شهر بودجه‌لازم رو برای پرداخت رضایت نامه دانیال ایری دراختیارمدیریت باشگاه پرسپولیس گذاشته و انتطار میرود ظرف 72 ساعت‌آینده این انتقال انجام شود و ایری با قراردادی چهار ساله رسما پرسپولیسی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/persiana_Soccer/27198" target="_blank">📅 12:57 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27197">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bor17LPbqOR7edqSB4pHlFSty9vzknusLq-lRBVYZuQ2sWaZxDkGqmhutg3W2JZd8wJzHsWhMFBbdyLJWv3cK66JCjE9ehTdHMQnH2ab8F4iAFcGKYO82PPI7EhfVcOco_Ac7uxFHPJbuLyi44dj9Q4SNAP3foAuwzaOJjAxS0hx0bPvHu9Ngr7H5PUuY-iXXNft5qrmdFJ5JX-enP_UgxH-wmHf-WrDXvYZ2pyHnGUwMljdpCTjph-W0YNom2ix_dCkXEL8itscFXfdan_5j1y9tVscsR07d5pCTq-74djWp9RIqNHlcdM2D7sPdxXI-MvYbcZi9K8H2KKbrj5Uuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ فابریزیو رومانو: بعد از رئال مادرید، بارسلونا هم برای جذب رودری دست بکار شده و با مدیران باشگاه منچسترسیتی تماس‌گرفته و آمادگی خود را برای فعال‌کردن بند فسخ قرارداد این ستاره اعلام کرده‌اند. حالا همه چی به خودِ رودری بستگی داره که رئال مادرید رو…</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/27197" target="_blank">📅 12:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27196">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JHgJo16EW8CibtxmNos93kkeU2TTG4rjnqepXUBhJX15TLYy-X9rbZli1IVBSSFSZQTcGkgWjwlmX9R2BgMuj1WugYkz78kgiKJpVm0nr-AvGAj_ZzWm9pjgiF6fPMgj8V4-kYT7lkkgvsKEYBy2A_cMh-YLb7HYlBPRbjoU3QYmRZt-ScQhDbmuOfIs5YXhxMJuBHBhIPy8jssEs3OjWRGfZ3tQx-eqMbhDd6FbyDdQ51SVIjswtJj8VIf-kk-_jhhbZkXfVz69UTqaUGeSu75LqoYW0J-LeGbkTO7PXKQQl02Nv-gkxyAM44tlBOOc7NSgCPpjTNnK69NX_Ro-WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
رودری ستاره اسپانیایی 30 ساله باشگاه منچسترسیتی:من‌تمام‌پیشنهاداتم‌از تیم‌های بارسلونا، پاریسن‌ژرمن و منچسترسیتی ردکرده‌ام و تنها هدفم دراین‌تابستون پیوستن به باشگاه رئال‌مادرید است و مطمئن هستم که این انتقال‌بزودی انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/27196" target="_blank">📅 11:57 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27195">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17c93987d3.mp4?token=CZLT_WaDh2qTXF8gRXvOf0nfC5qFgmTaav-DFST65-1dAa1qZuitghKjuPsYsBGeTaXGif9ONl--x_9a505U628WuArBViyE8ggnhT765u_WkZ5n97oUp2xF7Yp7rTjWsrqtDdg9mLqnV0Cxdx52jGMR5TGFPmehDVh8RlisMjyw8MuZQEJjegBTtmtjHru2nDQIi_7LO6i8Hz0hvkos5Cr3-tKU_Nb08a182uTI-Ua6tIlM5-WkxYkjRdHX4ZXTTnjwF_b6QTMnlEjm8oMFnpfivJTBqYfousjUkNgVXeVVrBQjNnLiYi8eEsWcB91zLNiZOdshyG0m3Hr9uM7zWHHFWydoS9S7_kZ-lNA9ZHh-XvWAxFP_Yew2Lr91sPcJkc2Ly7sm2yCpzE8i35IUTvMrunvcd9iOZX-xA7KcBpvILrITcSM6O_07hzCOstxl_53YSxNt0Q292kC88jQI0GB75U4opR6Ye-KBR85dVTdIUo7tqgE5HZsJ8FzVK0FYnGMXiDbLHKL7zFOMnPVj7eXhv328vDfYhk6WbY3H1hI2VRzy1E2CkLu8aMKWcjkbCFUJk2RnHSDyA2_H5WGu8yp3_mqahhWlwuh-x0hN3_iVbxhW2kqqavlyRXX-JGJt76aaqStjXTaWTEwTMuGbWweslcQUKK4F1iZCmUKScoc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17c93987d3.mp4?token=CZLT_WaDh2qTXF8gRXvOf0nfC5qFgmTaav-DFST65-1dAa1qZuitghKjuPsYsBGeTaXGif9ONl--x_9a505U628WuArBViyE8ggnhT765u_WkZ5n97oUp2xF7Yp7rTjWsrqtDdg9mLqnV0Cxdx52jGMR5TGFPmehDVh8RlisMjyw8MuZQEJjegBTtmtjHru2nDQIi_7LO6i8Hz0hvkos5Cr3-tKU_Nb08a182uTI-Ua6tIlM5-WkxYkjRdHX4ZXTTnjwF_b6QTMnlEjm8oMFnpfivJTBqYfousjUkNgVXeVVrBQjNnLiYi8eEsWcB91zLNiZOdshyG0m3Hr9uM7zWHHFWydoS9S7_kZ-lNA9ZHh-XvWAxFP_Yew2Lr91sPcJkc2Ly7sm2yCpzE8i35IUTvMrunvcd9iOZX-xA7KcBpvILrITcSM6O_07hzCOstxl_53YSxNt0Q292kC88jQI0GB75U4opR6Ye-KBR85dVTdIUo7tqgE5HZsJ8FzVK0FYnGMXiDbLHKL7zFOMnPVj7eXhv328vDfYhk6WbY3H1hI2VRzy1E2CkLu8aMKWcjkbCFUJk2RnHSDyA2_H5WGu8yp3_mqahhWlwuh-x0hN3_iVbxhW2kqqavlyRXX-JGJt76aaqStjXTaWTEwTMuGbWweslcQUKK4F1iZCmUKScoc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اخیرا دانشجویان رشته علوم ورزشی دانشگاه سنندج به مناسب فارغ التحصیلی این ویدیو زیبا رو ساختن و درپیج‌دانشگاه‌منتشر شد امابلافاصله چنان فشاری به مسئولین دانشگاه از سوی نهادهای امنیتی وارد شد که مجبور به حذف این ویدیو زیبا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/27195" target="_blank">📅 11:47 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27193">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fi0TfOsQGekcSfHk94eDYkg_jGNCloHsEtLOnSwcG4hqZL0EDzJxWUu3owAD7yMA_yiRP-FIWrzGkvtXvOadQvYnHbqzTWfjEDbJc6MIPwElby43KiuYO8DTeM_fTg6lJajNsUtAqIGy_8uFCfEQFDWZ0-OXfBhSvLqiWRXPCDmrmJCCVzEtXIYdXLjjZ-IjsABqqUifYxtU1v7mG1pkZ-l-zo_7q-aMJUFcDhUqnOEc4JiDELEQMaBgmDfwCUFud26nDDi7pr1jsK872g8WWpFgALZhYM4kps5SVl-s5HcagJsvi_qPtGimqq-nWs_WLNNcFaNJYroUtADMtI_1ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wxq8u3bCHbZEvvNdo2XZ4Nty1h_f1KJtItVp56i84vuqk_IpZ7VMl-Z9Hg_h01-dbDq22iZeRMLwgqZxN21lS6WM9d7qwqwQOQsPWJWaLmi-NKKq0XBNKWur9HP4sqCLxSD3xAml82Qz2MLyMtph5C3eq3kquxTWMq-VArq6pUgn19uGsc5H5VnwIxaxTi4c_LL1Lj2qd3rDlv41f6iCMSJ4PBzNRy2xW-fsf_Ffj1yrM3OSScGIK2LEYUavpvRo790DwJMp9RxBcRTaAm0BJ5d2aAExd1IE_n0L4Mxt-o12K2kOje0jeE9UnxfjFHWwREbXbLl3uTLY4LGQbhdNbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
به جورجینا هم اومدن احساس بد بدن راجع به بدنش، در جوابشون گفته: واسه من موفقیت واقعی هیچوقت این نبوده که خودم رو توی یه قالبی جا بدم که معلوم نیست اصلاً کی و چرا ساخته‌تش. موفقیت واقعی یعنی با خیال راحت زندگی کنم. کنار آدم‌هایی باشم که دوستشون دارم. حواسم به خودم و سلامتیم باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/27193" target="_blank">📅 11:21 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27191">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/165da6fec7.mp4?token=P2T2THmIVcObx5NNIQiNuzzgkTaBWziVNZU-lrKbptTnVNumqpw0bAUg3b-erOR4-hcdqWe8Xmm97HEn_5_dn_5I44eiHUc6ixCnS-kcYLPkknTDI5cji9I0FvHQCO0bYa0-s3x7rBUMVZObrrPTjQjckKU1NpfXA3g4huOyGzcJwR-serSUzfFHXX_7Hm5A-r7qDqWIAfsIhxfWkWKEmj_bOay0ChWb2hGrWDS8dE8gstkDLTVrMyQftyYaGIF0tUbbAAet6C4WssMDVIZcAT5ZANniDrbmx6w-pAMmKqZLVLG5FRLYAsRaJfpMdISwqQ1gm-AG6Q806zt4wV0073ht0namwyTEvIUWzJiz_c5HO5oT2YkYd_ya_S8OZAFTL-vnrgrfTYDZaP8cQYKHejjKZXCExhUm9OsK7pIF06TMQQRtgtPEQXSV6ngj-eOBJqdcKTROnTus6Eqy2WAqNDpAhuZNYemAasuhKh-SVqlwXdr20GIdke99AEv58e9FeLhxD21VmD1c-hvmSiHRmiLv0d20MyOKimTgqDyP1-G-6vWzL2RkmJyeSGVTrI764s3qg1NjcdmM_PUKdLx3gB2FX-KNnRJrcnM_IluroKuXHPEslKHo1goxkEUk2dE0gbt4_aHiBR8lNAA-5A5t5FiFVFBW7vkWOY7oBfdKobQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/165da6fec7.mp4?token=P2T2THmIVcObx5NNIQiNuzzgkTaBWziVNZU-lrKbptTnVNumqpw0bAUg3b-erOR4-hcdqWe8Xmm97HEn_5_dn_5I44eiHUc6ixCnS-kcYLPkknTDI5cji9I0FvHQCO0bYa0-s3x7rBUMVZObrrPTjQjckKU1NpfXA3g4huOyGzcJwR-serSUzfFHXX_7Hm5A-r7qDqWIAfsIhxfWkWKEmj_bOay0ChWb2hGrWDS8dE8gstkDLTVrMyQftyYaGIF0tUbbAAet6C4WssMDVIZcAT5ZANniDrbmx6w-pAMmKqZLVLG5FRLYAsRaJfpMdISwqQ1gm-AG6Q806zt4wV0073ht0namwyTEvIUWzJiz_c5HO5oT2YkYd_ya_S8OZAFTL-vnrgrfTYDZaP8cQYKHejjKZXCExhUm9OsK7pIF06TMQQRtgtPEQXSV6ngj-eOBJqdcKTROnTus6Eqy2WAqNDpAhuZNYemAasuhKh-SVqlwXdr20GIdke99AEv58e9FeLhxD21VmD1c-hvmSiHRmiLv0d20MyOKimTgqDyP1-G-6vWzL2RkmJyeSGVTrI764s3qg1NjcdmM_PUKdLx3gB2FX-KNnRJrcnM_IluroKuXHPEslKHo1goxkEUk2dE0gbt4_aHiBR8lNAA-5A5t5FiFVFBW7vkWOY7oBfdKobQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فکت؛ محمد صلاح فوق ستاره مصری تبدیل به سومین بازیکن‌بزرگی‌شدکه‌به‌ترابزون اسپور پیوسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/27191" target="_blank">📅 10:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27190">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeYhb2jmQ6INLVbaXKEJrYf9NZ_YHpfWEJyHkNALJ1mu8V2Tex5XCMUW9EXIJMhcRFgA-YNcYFdaeyKtn7_-yKjp1BW1ezkhJYs7iS-7URtjkQBLuIA-lM3zz9o7-I4P6czWjeeaeTPn4sq5Smugo-QM4VMNDRJWhRFVvxcfT8NoTlBF3lG13QyB-W6MmsPVu9gTjS3oJdfukNq8ePCWNgS1AYppuIuWucDmKNygPx6Gp0FbBYE23ELLiS2__uCLDcEeS6RC4hozPYZC9c9KGYKi2sbgTuYhOAx4vr6ws1FdEQ2uuhM7vvGDwYd0Uof2_OhwioxdxhAqYoQqtNJHfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
عملکردخیره‌کننده لیونل مسی دربازی بامداد امروز اینترمیامی با به‌ثمررساندن دو گل و یک پاس؛ گل‌هاش رو در کانال دوم گذاشتیم برید ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/27190" target="_blank">📅 10:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27189">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a1ec418ed.mp4?token=po6VOI04kE1ZcndFRNZfGr71-zrg3KdVTsPj3y3VaFRbKUbr1-Du5r-yZAjHrlt0sRt9Df70M_sDL-zPs64GZpokDFxvWulOlnakiguWvc4rj4OGftecUSzyUFUj7GlnQtDaOyZk1O2GCR8XCvh2BMG_kPNNICk8vDsuGmd_LNPG2QoMwK2W9OEzJuE4zBI5s1Psd1SRi0saUsMm8HZsIg5iQZI4HH4N2KuPjHGC1FC_4oO5c_8ssRF6dNgelQlMksykY_5zl3Hk--ivLoZtyXUVaGeIJo3yb4bdB_NHnNocskmh6JGA0diRW8fThkT5X6sQ-T9BSzY52eNeKNClNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a1ec418ed.mp4?token=po6VOI04kE1ZcndFRNZfGr71-zrg3KdVTsPj3y3VaFRbKUbr1-Du5r-yZAjHrlt0sRt9Df70M_sDL-zPs64GZpokDFxvWulOlnakiguWvc4rj4OGftecUSzyUFUj7GlnQtDaOyZk1O2GCR8XCvh2BMG_kPNNICk8vDsuGmd_LNPG2QoMwK2W9OEzJuE4zBI5s1Psd1SRi0saUsMm8HZsIg5iQZI4HH4N2KuPjHGC1FC_4oO5c_8ssRF6dNgelQlMksykY_5zl3Hk--ivLoZtyXUVaGeIJo3yb4bdB_NHnNocskmh6JGA0diRW8fThkT5X6sQ-T9BSzY52eNeKNClNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه بغل کردن جواد عزتی توسط یک دختر در اگران عمومی و تذکر حراست سالن به این هوادار!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/27189" target="_blank">📅 10:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27188">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33a3912563.mp4?token=Qz5LSCP02F0Mvj_MppijvdyWBayp9nJDM8VoNs08_aZds9WXdVquhJMQdqHOabEYxjQBM3Dij8NxJR6JjH31MUP8oZiJV-rOIIeGW0ogP-c-LCUb0Bo09lDr6XruZckNQuq1HnrFu4n7BjBFHPDtV4weaIYEV3dKdcHBOTrEWStF3_b5FPPVcecy0_09PHlsMIAoKMsLXeGo5fZs9iiAGIOkClGTp1R1wN9Z5363AJPxgi1ecVbtGY7ANbDR_b6SVtCA_kEHeMazW_Jzaaybf00HXKmu6zyO2TLoW6-_pqCgCfPfRbFaHyQyBix7ZzNVLtlE7O_MdsIkLSqjJrPUww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33a3912563.mp4?token=Qz5LSCP02F0Mvj_MppijvdyWBayp9nJDM8VoNs08_aZds9WXdVquhJMQdqHOabEYxjQBM3Dij8NxJR6JjH31MUP8oZiJV-rOIIeGW0ogP-c-LCUb0Bo09lDr6XruZckNQuq1HnrFu4n7BjBFHPDtV4weaIYEV3dKdcHBOTrEWStF3_b5FPPVcecy0_09PHlsMIAoKMsLXeGo5fZs9iiAGIOkClGTp1R1wN9Z5363AJPxgi1ecVbtGY7ANbDR_b6SVtCA_kEHeMazW_Jzaaybf00HXKmu6zyO2TLoW6-_pqCgCfPfRbFaHyQyBix7ZzNVLtlE7O_MdsIkLSqjJrPUww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
پابلو گاوی؛
بازیکن‌اسپانیاکه‌قبل‌ازجام جهانی گفته بود اگر لاروخا قهرمان‌جهان شود موهای سرش راصورتی میکنه در روز تولدش به قولش عمل کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/27188" target="_blank">📅 10:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27187">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">چرا
3️⃣
2️⃣
1️⃣
انتخاب درستی برای شرطبندی هست؟
🔢
امنیت و اعتبار بالا
→ چون ایرانی نیست، مثل خیلی از سایت‌های داخلی آینده مبهمی نداره.
🔢
سقف برداشت
→ در ریتزوبت سقف برداشت معنی نداره و شما میتونید بدون محدودیت شرطبندی کنید.
🔢
بونوس‌های فوق‌العاده
→ اولین شارژت 100% بونوس داره، و یکشنبه‌ها هم هر مقدار شارژ کنی همونقدر جایزه می‌گیری!
🔢
فعالیت بین‌المللی
→ در کشورهای بزرگی مثل برزیل
🇧🇷
، هند
🇮🇳
ترکیه
🇹🇷
و بنگلادش
🇧🇩
فعال هست.
🔢
اپلیکیشن اختصاصی
→ با اپ اندروید سریع ‌تر شرط‌بندی کن بدون نیاز به فیلترشکن .
➖
➖
➖
➖
➖
➖
➖
➖
🚀
لینک و اپ رو همینجا براتون می‌ذارم . برای
جام جهانی
هوشمندانه انتخاب کنید
✅
⚡️
اپلیکیشن اندروید ریتزوبت
👇
🌐
RitzoBet App
⚡️
لینک سایت معتبر ریتزوبت
👇
🌐
RitzoBetLink</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/27187" target="_blank">📅 10:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27186">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WX7dUGvM5uErBXi84-fq8uVoJyh7166VCmhHrXFaSrwWuuezpEU4EqPk4ZgoOqHvjJfeKy3XwStUxvDPSBh76AzN-bzL3R1F9E2l7NM1vGU-tQo_Bf_K1xJYvR37-2gGGKn0-iXoYFiXa-f5oi1mXO17qSSTPpNQn9IlJQnVAW-rgDruXLjBxhAtjORYHm89pdDTxYQjVzMIqNxPrf2nHepxIwnlS-7Z-z66mikSUmZnlT68_vbrYI_l72iHhvUReDwVCDeMtE-rfcWYB-zmjsj4I2P-aDjLsGJybkdtmbYeOVQs5eWNoV8reJGyQ15Y9heuaKCO0Bfeu7p8Hoz2Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
نزدیکان دانیال ایری از توافق‌شخصی دانیال ایری باباشگاه‌پرسپولیس خبرمیدهند و بانک شهر این باربه‌مدیریت‌نساجی قول‌داده که بزودی رقم رضایت نامه این بازیکن رو به مازندرانی‌ها پرداخت میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/27186" target="_blank">📅 09:53 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27185">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jeR5mv4BHqSPZQ97stYlcrb9Y1Nq4lqkFUP8QQmV28ZucPPqY0HHDIgbb8Cf_hsoGFPOb_TlLD4O-SWT-5qk6KJZ2Cgg5FCul58eivrGK0eZjM7IfYG5DCkg5ur7vXRyJRlYIwXO-F5Wp-VKB1k1MCa0gbO6TvQytICyZS7vpuvseIyRoNJ2nSv5zS3nEbIgrqnOGnARcseS8qyUDQWCieRjeuPzVeKk5ADgyxv1B2nAqsmbHIsGtGG4jgm13AIPXaoDFt9aVm5kqX4k_wGBMGwwdWvjUzqLWy7xp4d9yuFLrbvTORg0eFVb7FrH1WpEHj77_F94Uy0iDvMSmlfoKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو آدان گلر سابق استقلال: هیییچ صحبتی با باشگاه برای بازگشت به استقلال نداشته ام. باشگاه استقلال به‌من‌بی‌احترامی کرد. دوبارنوتیس فرستادم اما مدیران‌باشگاه به من‌پاسخی ندادند. بر خلاف میل باطنی‌ام مجبورم از باشگاه استقلال شکایت کنم. اگر جنگ نمیشد استقلال…</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/27185" target="_blank">📅 09:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27184">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rT5VCI-SrcZGqpIy_yinBUHBztA79P0FbGuFGM2Gd1oOggfOv6tflbKaWZJZhFAxDUjlDRKIijYayYQgQw_SgfKxKRzRIqWnJzHFqE3wWRL5mmiEzHwrTSPiRee5afhgKuPQUrC_xOXpg1rbJGzi49uM79qFgPpcN_GFyNyC7cgNQwmdlejOYsbNdjUhjQTE5_C4zNWe15h31JwcUgmjcQmD99eRmAt5p6A4oYu4kId7hWfr1L9imHSZ_CRiHrMy-dwfa5q3H0ZdiMV9Gn3gT7yWKtTimE55wSQReqD7fEbo6vh9DBpmzK36XYLSbhFikzEg0s1KyiLAycvm1fdABg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبل لیونل مسی در اولین بازی‌ بعد از جام‌جهانی که از ابتدا در ترکیب اصلی قرار گرفته؛ همچنین لئو یه پاس گل هم از روی نقطه کرنر به ثبت رسوند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/27184" target="_blank">📅 09:33 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27183">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kN54es1U3C8dGcHeiUoxVMAa_5MhOi3mhGX9lAzX4ZVW6jgPjZhzaHk1HtuJX0JAC6tLmDymLnm3CCloe6A3aSaJpU1gKdri1YJ21Ddv2C45A53qJzZq0P63mPPr7ildObfb0Vth1gQcZb9DBBa1jywyzCkWfUt89FLUVQ1_PYt48hg9AGSweO4oh3qdQ9LJX6bsSWMrrgv8IoI0zgCx7ceMaEPw5cc3cNYrAj1On8yI8LQXlcO-v8DxJDuatDA9LakyCnfXrc7CWPEisD-IQY9OrQtlPP3q9MfC96RdurMi7D8cne5CRaO704dR5uWAUM64smD7YBlB-y90F6BZyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ آفر مالی رئال‌مادرید پایین‌تر از ارسنال بود اما وینیسیوس بعد از مشورت با نزدیکان خود از جمله نیمار تصمیم به موندن در رئال مادرید گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/27183" target="_blank">📅 09:26 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27181">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBzcqlvXJuNnhvFb3QNAyTAnuXZ9uUqWFZEJLLiJi8Ei4TAaC1Y87XKyCRDSDCaxZhm0U7mzuSba_mFPHxUBQqz3MhUxCei7QnHIyOat-oToHqPYBu9erL7OWygrzgaXKLtOM0UrugaG0PnC_s976Wej0Zt2rdyoLhwXN_2ehoWyhEgUH8p0eRdEDVJfYvH3BpCzLqtN-VrJV7vvYSofA6AocpuDRf0JGVXmfyohysWvAQU_yRRf0l9iaJz8OiqSKsvHlzfnI9LK9JbCM94b43Z4ulCnVxTtYaB1LjkvWWpGpBLayn7vzoQwzv0gJFgI7b4pv5-eeK71pCkJAJMYmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4684a0276e.mp4?token=Nm3rLF8TW4dK1HubfFlbVOSkX4QW6ULqo9ed3meHwHRnOs-bTb64clHvtz9QxzrD4QymVyFKv1NTKL02S1y96CwY97YbUsIEQ2_KN8xP5x9CVUg3QXI7UfjR57kJgxh37wh5UzTv92MvsfIob8vj2dEhV3k8RRakXOHWQaZIfNw2Nw2lXJ_pI0S-3rmWmeZUMZ2FZbZkf9euohgUEBUGll3Bnzj7F2dnTNxdyjsDeRP_gS-HchlRoZtxPA2o2eO55uQOUjJQCcVu7wrKmxrrq-w5cL0fD-bjEDoGkUy1-lAZx5775XM26golY9vhOCR8kq3JbOX3AK9q2ClCCBsvIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4684a0276e.mp4?token=Nm3rLF8TW4dK1HubfFlbVOSkX4QW6ULqo9ed3meHwHRnOs-bTb64clHvtz9QxzrD4QymVyFKv1NTKL02S1y96CwY97YbUsIEQ2_KN8xP5x9CVUg3QXI7UfjR57kJgxh37wh5UzTv92MvsfIob8vj2dEhV3k8RRakXOHWQaZIfNw2Nw2lXJ_pI0S-3rmWmeZUMZ2FZbZkf9euohgUEBUGll3Bnzj7F2dnTNxdyjsDeRP_gS-HchlRoZtxPA2o2eO55uQOUjJQCcVu7wrKmxrrq-w5cL0fD-bjEDoGkUy1-lAZx5775XM26golY9vhOCR8kq3JbOX3AK9q2ClCCBsvIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
محسن بنگر کاپیتان سابق پرسپولیس در کنار دخترخانمش؛ دخترخانوم بنگر دانشجوی رشته دندان پزشکی دانشگاه روسیه هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/27181" target="_blank">📅 02:45 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27179">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhEheoWubFcQAnkzUCH0O6iKO-dwRBi1UUZFJtK0BTK-5ZM2eOd6E_Y1wonQdCvMPgBkqvxTEpgDllq0yZtsRuFATEh47A8KgRhTSYhMzTwFmfHXAIuYq-JxBkicznn_4YAMO4eAu81nL15PWGyXVoLgu5EpFT36sgVHiU3R0c88GeNzvA6iqiY7PLFZRbANr7RuPPxQxPkZDnovsaFv-ESvqvQPza3d3fjBziVMEQw-KKZvHC_rTSxh47d4EAA-XKIsAhMbolSofFFdf-vX_V0Kdq5wTWd1QMx_NeHNe0SVSoRcgbGMdVOPWbzHnrEL-cUeJR09poCLVuY1GGUSaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ با اصرار زیاد مهدی تارتار؛ مدیریت باشگاه پرسپولیس بار دیگر بامدیریت باشگاه نساجی بر سر انتقال دانیییال ایری به جمع سرخپوشان وارد مذاکره‌‌شده‌اندوقرار شده که این بار پرسپولیس 120 میلیارد تومان پرداخت کند و این انتقال نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/27179" target="_blank">📅 01:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27178">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e55341bcb2.mp4?token=NQo3howdD0hTf_dIJBZ7J6Gpg9TDAaUDMOf2NnZ8KaZECJP0FuHt5gkXyfO7E5x0zFH5DjyivBmlw4zPfeDHWMkPGzKM_WlDogc146w1HqJN7BKpIXdk_elMWlDXkE53NeaGcrY5TqsJirKQXiFxUCM3O55fzKkd17elFa6uO-MnMFyzTV1xn6uSlS0wSYWkSbCNrHockOGPohHnCSrog_mCstyxMDWL_oUalg0hFqEKH6PPlumsRjBFD9T8sPvSMcaCJ_ndhIxrK7MWEv3tuDUoeSoDIrqpA05-O9I1tLIRqBQJ2qt_oWcpfK3mvG7A0KKOLlLXSUVCRb2rLkP24qZasyKEOUJfw06Sfn0Tgyq_CZkQEi6rmjAIUVD2YqbBsY1yg6viP6-gWLLKJ8UfqWTPMqAEGb4g3bNA1ZCYe3CBXst_JxFuwinTWbxnJr8iekHxptWMZA3mp4gCwKxzmv4idh0AFVEQ7nOmBVKTIPsZJWWjnSjdJADhZK3ooBCToB_VzF3Z7iq7U_qqsSI-gSDSQa-OFYm21VFrRbj5mqvLsnxnYqdPWdSFIRacIFs8URbkR2aLhRAUYgjpJpjRV_eAalzsz8-KROezWq_KvdcTy6N6z1nw_9rMj3TMB8rBaROG3eeIZzgfC8BHWK5psA2pwDSluq5Ek5NX63M6VXo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e55341bcb2.mp4?token=NQo3howdD0hTf_dIJBZ7J6Gpg9TDAaUDMOf2NnZ8KaZECJP0FuHt5gkXyfO7E5x0zFH5DjyivBmlw4zPfeDHWMkPGzKM_WlDogc146w1HqJN7BKpIXdk_elMWlDXkE53NeaGcrY5TqsJirKQXiFxUCM3O55fzKkd17elFa6uO-MnMFyzTV1xn6uSlS0wSYWkSbCNrHockOGPohHnCSrog_mCstyxMDWL_oUalg0hFqEKH6PPlumsRjBFD9T8sPvSMcaCJ_ndhIxrK7MWEv3tuDUoeSoDIrqpA05-O9I1tLIRqBQJ2qt_oWcpfK3mvG7A0KKOLlLXSUVCRb2rLkP24qZasyKEOUJfw06Sfn0Tgyq_CZkQEi6rmjAIUVD2YqbBsY1yg6viP6-gWLLKJ8UfqWTPMqAEGb4g3bNA1ZCYe3CBXst_JxFuwinTWbxnJr8iekHxptWMZA3mp4gCwKxzmv4idh0AFVEQ7nOmBVKTIPsZJWWjnSjdJADhZK3ooBCToB_VzF3Z7iq7U_qqsSI-gSDSQa-OFYm21VFrRbj5mqvLsnxnYqdPWdSFIRacIFs8URbkR2aLhRAUYgjpJpjRV_eAalzsz8-KROezWq_KvdcTy6N6z1nw_9rMj3TMB8rBaROG3eeIZzgfC8BHWK5psA2pwDSluq5Ek5NX63M6VXo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
تعدادی از گل‌ های دیدنی در مستطیل سبز روی شوت‌های فوق‌سنگین‌بازیکنان؛ عالی‌بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/27178" target="_blank">📅 01:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27176">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729a2d9732.mp4?token=b-1b_kyTDrljKGGdfyVn0fzJ-SAe1wqGQHsPVDH3Sb7eU7rgv6txO2zqhT9cv7XAFUEgwLza4RdS6btYQfnQVSLueZeLfbi-sRmLigGBO2NTlsBWbjgyJtqIHDY5nTSqvR_6P4__xXUPawf1Jx5aUFBW-x4no0oiM9bMeoeVASHHzk2dJ-GNBbdnZ3c94o8RiQCa-06QfvSFoZZaGmxZ_ELCuqu7NwI-cA8bBd66I4Auxo2zhzJ16Q-8avD0--lP3PHPbKZWa1V6l_BP5KiBtm7Cuom_WeSLg14rRj1aHOx_ki4BV-pbT4u7aAhwYEWowvudeXRP-rj5S9V4g4R-Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729a2d9732.mp4?token=b-1b_kyTDrljKGGdfyVn0fzJ-SAe1wqGQHsPVDH3Sb7eU7rgv6txO2zqhT9cv7XAFUEgwLza4RdS6btYQfnQVSLueZeLfbi-sRmLigGBO2NTlsBWbjgyJtqIHDY5nTSqvR_6P4__xXUPawf1Jx5aUFBW-x4no0oiM9bMeoeVASHHzk2dJ-GNBbdnZ3c94o8RiQCa-06QfvSFoZZaGmxZ_ELCuqu7NwI-cA8bBd66I4Auxo2zhzJ16Q-8avD0--lP3PHPbKZWa1V6l_BP5KiBtm7Cuom_WeSLg14rRj1aHOx_ki4BV-pbT4u7aAhwYEWowvudeXRP-rj5S9V4g4R-Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛مدیر ورزشی ماخاچ‌قلعه به‌مدیربرنامه‌های محمد جواد حسین نژاد اعلام کرده که تصمیم این باشگاه برای فروش حسین نژاد قطعیه. هر باشگاهی دومیلیون‌یورو بدهد و خودِ حسین نژاد هم راضی باشه این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/27176" target="_blank">📅 00:56 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27175">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1mkK8TGGTTgMDa2ngVskWUmw2ND8k9j28PI-pkiomUpV2BzgYFw0-kJ4OopuNvCzIL5wWF63bslLufhV2MnYmTf43Scm3i6qHSJvePOZXVV-KLKkV5BzxYyVoehrzgaHX0-a301wzxZGAAa0xlCYIGLPCUWqZwCyQaQAXEu6dThdsdEM48AR10L3QML-m9F-QBfHtkZfllsfEA3tL-G2n-YdoDbjlqxTSWRXieav9ATf_OkFinzVyOq3-rUDt2g8Jd2pxXsXGhmpen1jv2cbGOFTFtxxnIzvZfJWWkuL97r5JU0jbom6oetAv4FL0SkPqbn4TEKyZCoBCUB3y0bow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه ‌‌‌‌دیدار ها‌ی ‌‌‌امروز؛
بازی یاران اللهیار صیاد منش در دور سوم پلی‌اف فصل آینده لیگ اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27175" target="_blank">📅 00:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27174">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cp44nDugGDQN7WGqw1eCesFdZwcPf26-d5ZOoofuF7CUyNLmSZ4Qdb5ue_4_RYTd7t7Od9IPugKxJWTZslrXZeN8fMNNlb9rnpjtfEKBUmqNv_xsTq9tV4FcPLq-QV3_LsFGtrtK6ty-2nFMkMGTqJri9SXf9mzeTRNqQA3ukXfMbyMBPABHoZUYA__cn99_LyS8OoMTbhhP_VnhnNdV4wcquKGA_VmcK91tUDXoSw_UrOXf1sJbYxGZ1hZPMrlOZR50ZM-I908dqh2JwBnPFNfIzRT1xP4AlTATwGH9EWf3Sjmw91rXzYkqOPT54uHPCmP1CR2VBHTsBrlGWz7S9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای‌ دیروز؛
تساوی در دربی میلان و برتری شاگردان اسپالتی در جدال دوستانه با چلسی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27174" target="_blank">📅 00:52 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27173">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gd26SkgujW-vnz6cab2PZGloAXjQC-87oozRL31oJwQ9LLOPn8Q7y2N6nG-Eo0QwYpa4f_sAdFianBeV2tSGpLxX4jAmOoxxUFEKgsgWV7P1-82ZHnG_PTlJ9wU5Q5H0NFyg2IBy8-4KNDcleRcHrG-4xpatlPEn-SPcFVOHTgoTQ6nXGlyp77ewVyt_NCdisP22yMyIDpXq3LaF1kQa4ufGtSp_te4uHpWw42QoJBBzbvPxhPpO5fDj7RTa0NdtED5nzh2-bsHW_qyMXB_Vd825x7N9mB57WA-9wJewOhCNSp15kQkSJDOBJdn9x_KhunHV9E-uTrQriE3RORC0Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛بیانیه‌جدید باشگاه استقلال: تموم کارهای‌اداری‌مربوط‌به‌بازگشت داکنز نازون انجام داده ایم و منتظر بازگشت این بازیکن به ایران هستیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/persiana_Soccer/27173" target="_blank">📅 00:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27172">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QeJHsvkdfHZtnWZ5F4eBzLxtk8DdKa4eG5a-yhB26NW1jr8ltRkkPPOJzoHban9zFc8WV81FdNE6fzoK2fngSqyFE9T2LVsKS4jqO9QGAOtHpa5JleSATLMdnonM8wSIK5NWe9phxHvSu_ijiXTVOoAIg7ZfcLdE_Uwa4rllC37RamHlDlgL6QQc2cRMKJ_keeurUoELNDb5QRPKvIlKwM3Kgjz-lz2_vBuLQjera9HJX6FYmpT4T8A8YjR4todUqltBucl0rlqNkij3WIgCtE_xs-c2XtVoYjI5sRTkdFzJqRzrUwNt6t2fn9CWnmLFbPKL5KanV20SWnQmz7rRqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ با اصرار زیاد مهدی تارتار؛ مدیریت باشگاه پرسپولیس بار دیگر بامدیریت باشگاه نساجی بر سر انتقال دانیییال ایری به جمع سرخپوشان وارد مذاکره‌‌شده‌اندوقرار شده که این بار پرسپولیس 120 میلیارد تومان پرداخت کند و این انتقال نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/persiana_Soccer/27172" target="_blank">📅 00:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27171">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4oXaCtkdQ9_f6towDPJTJBiopjDybnplYAd1tmKTTOkuM9ZGo8EdoG0kUNnnKCBGM5Lao40RVe1-U9qaaqely8UjQ0cy0G3DVwPfNwouhMnlK4y-nuDRBnYgRhDLtS46Tjk8_H0Q-SrgrbySeDG3yWQNwr563OApB_GkYQcZVRJit1khbEKF0UDb559u1ESoFJ82pQcWW2H4ywbhs8G-A7AHZ3E_8mp4qXzMriwrBoP3FZf1TgLAVNmYgueMDhxORSshEV5eP19MBfpo1y_syJ3g6f2tg--qB6EiXH9R8a-rhADKTLS6T3w-LCKGk4_b4maVHduJDYXxsgKVeSBfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیرو خبرچند روزپیشی‌که دادیم؛ باشگاه نساجی به احتمال زیاد به‌وعده‌اش عمل خواهد کرد و دانیال ایری رو پیش از شروع فصل خواهد فروخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/persiana_Soccer/27171" target="_blank">📅 00:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27170">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPJEHP84WYf4xSs3RKYyI6DZ-mNkq6k_71yiOnM05yFpEdtBLsG81NxkrdkNCjf-GhCqfXD7MkPHBMIsfOuWvwKTeY5pwMiOsmyp--dIKzthSpk6FVYA6e77_BvW4w6zxD78x3LBN_3OfHP3ofOqBUjPHYmfTiC8VzDbEIx4T_At8gqUIVMPk5J5P781bwWNx1IUQihDJGZHkVTQuL3Ddzkl1Bvv7B6yqKwc3IM9w6h6bZonAqVIpvpEG8A2DpDsEd-CEH5X4yjUltKa7IHgOanqatepludIj3hVF881wiTPffQCYcHUH5vrEqPIKpFnDiatuZ67D1WSr8haF5ynNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
وقتیCR7 از اسباب‌بازی‌هاش رونمایی کرد؛ كريستيانو رونالدو با انتشار پستی در اینستاگرام از ماشین های لوکسش نوشت؛ اسباب بازی های من.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/persiana_Soccer/27170" target="_blank">📅 23:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27169">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2pO6GPux1Hf9Wc9nIgR6LItBJrQ166HxsmPb7e9g91hx5sMH4xFLc_DX-eXeLah5EqVHjqIgRZqrUD9_H8LuO17r_LvDKgg1LykDt3W_ePpNslJK50XcdNlZw3Lg9eM5n5TMHRvjn1SEJkzwAGZ8zLxt5FbVRvIttANGesaQaOvkDfJmL5adCYriVmV5hKoFYgZoo9vNOisyr7UWX10AzeWx3QyrasocYRg0iGE6ph3OBVoI2Bt1QgJVLzKzorkX9ZI4Fkyn9VzOytPogcwIZXwlirymOzkPDZhXoMrRepRoGteNtwUhdhVmnfoc8sqBW1fIlB37ZdFCbhiZq7FMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
توییت‌جدید علی تاجرنیا رئیس هیات مدیره استقلال که غیرمستقیم‌اعلام‌کرد که رای دادگاه عالی ورزش اعلام شد و پنجره تا نیم فصل باز نمیشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/persiana_Soccer/27169" target="_blank">📅 23:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27168">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqaqFZb5FULcpD_WcQkzkAQaksXERYmh7tzVNuBVPfIdMr3kJ3KzWyvvNl6AfLjzS7hFWMMYKWHKpG_emVE3sZTvVdwzZOSaynf7mW52tbUibnzSRV3HDQIOs6xSg6ei83nkigUEVxdPTTukI2p_Q-R7v_ofF7UzFN-wK66Nk8LbyIEhXL-vRICqetNQYUYROhfg47kdUlh3iRvgGlpaH76g4l5xVBRMGFc09QDBpxqkOtDnQ317deFyH30D0MBm_19PX3JUMnHg9yksx-6EhW16EhZHXAh0RtvUoxP6QAfWGW2Hfbqny94e57NkwxdBMSGHAbZBImv3sy71Pe3sXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
👤
ساعتی‌قبل کارت‌بازی محمد مهدی زارع و محمدمهدی محبی دوخریدجدید پرسپولیس از اخمت گروژنی روسیه و اتحادکلبا امارات صادر شد و این دو بازیکن جوان مشکلی برای همراهی سرخ‌ها ندارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/27168" target="_blank">📅 23:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27167">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b58266add9.mp4?token=PEhNQz_u9jq9A4MG62rdntNmiWOBgsWFQpNX7XnAnEZXUQTrjWAYY0aom5LYwvb-m3tzLaqhCHUPoJ4NUr_rI111ss2NuGZ44qqbRYNUywlZTjCkvzGWVCPeZIWZ6_-ayFCkvU8bG37-R_0WUPF4S-DfFdVOubfs2QG8fhKz7gUmQEfPHqIwKm07CG8Hz1NGd3VOLVzvI-9FiPsEoZxX_jfERRQ7eRF93GL2Hx7WdEjRFNECyL6ccLnFKEWI8nFiuPSMrlILN3tLI5rYItjXoFtitRpbgX1FWFXMNkX6wFYM-xCtePFMCpHroDpDdze9KRulZpl40EIKaOzFY_YJDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b58266add9.mp4?token=PEhNQz_u9jq9A4MG62rdntNmiWOBgsWFQpNX7XnAnEZXUQTrjWAYY0aom5LYwvb-m3tzLaqhCHUPoJ4NUr_rI111ss2NuGZ44qqbRYNUywlZTjCkvzGWVCPeZIWZ6_-ayFCkvU8bG37-R_0WUPF4S-DfFdVOubfs2QG8fhKz7gUmQEfPHqIwKm07CG8Hz1NGd3VOLVzvI-9FiPsEoZxX_jfERRQ7eRF93GL2Hx7WdEjRFNECyL6ccLnFKEWI8nFiuPSMrlILN3tLI5rYItjXoFtitRpbgX1FWFXMNkX6wFYM-xCtePFMCpHroDpDdze9KRulZpl40EIKaOzFY_YJDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل فردوسی‌پور:
🔴
اگه قرار بود که من چاپلوس و دست‌ بوس باشم الان‌صداوسیمابودم‌و نود روداشتم. چراباید دست یه مسئول رو درمقابل‌جمعیت ببوسم؟ چراچنین چیزی روباید باور کنید؟ دست کسی رو نمیبوسم. هجمه عجیبی علیه اومده. همیشه کنار مردم هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27167" target="_blank">📅 22:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27166">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbd4624448.mp4?token=XALrzUtA5m_-bMOZwX7GADJr1EzSQM-VwIzzg7MFMT42gZtbnVNjO28QxqIs8sGCYFG0z20f3RAOQmP2yRWUCERXleH4t-MH3RtlC__1Yyn_wz7GjJFKhNRq1BzEscZU3iNPzyysi_yq3iBZbGpAHtsfbYFLAiPh_qi3cPbboz2LpqMC2YISzI006BY5_FktAx1_WyjBHZ6cOlkKr5kAEN_mhXyedn72GI79g3-5r5pZP-Co-hUuGkAkrLz8Eck53D_MPNZZAePOkf1ryFLxSSbnyG1HZ-xZpPvXmIh9I0kM_2FUhHEYE1irLeXB1SCu3J_UUpKWorKKvNcwdNdWtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbd4624448.mp4?token=XALrzUtA5m_-bMOZwX7GADJr1EzSQM-VwIzzg7MFMT42gZtbnVNjO28QxqIs8sGCYFG0z20f3RAOQmP2yRWUCERXleH4t-MH3RtlC__1Yyn_wz7GjJFKhNRq1BzEscZU3iNPzyysi_yq3iBZbGpAHtsfbYFLAiPh_qi3cPbboz2LpqMC2YISzI006BY5_FktAx1_WyjBHZ6cOlkKr5kAEN_mhXyedn72GI79g3-5r5pZP-Co-hUuGkAkrLz8Eck53D_MPNZZAePOkf1ryFLxSSbnyG1HZ-xZpPvXmIh9I0kM_2FUhHEYE1irLeXB1SCu3J_UUpKWorKKvNcwdNdWtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
باشگاه‌فجرسپاسی‌رقم رضایت‌نامه یادگار رستمی وینگر 22 ساله خود را 50 میلیارد تومان اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/27166" target="_blank">📅 22:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27165">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAAK_qC1tKOj0092CNCwlbkhnMKNtmeWDubr-n_Z90gQn-WwsNwkDFEqauEuFRRTXV5gnhqn5KLTtD-eyx8vGWqqJu59i-N8Yg1J4sh2-s_RD1Y9znV_G8OgdWBf15p5bFxqG2-UqHZTm4wBvSrjyWF10bBMYYirRDXOxVRLdGkQ3A2QD9nEmegIzkgT5VRsK_zRMgCILBDsWlVNNSrZLGzqIv8w776fwS78PPGmus4vdPNVlT21gZDvoy1hWSiHlLUFTk3TkXWnEwdAX2J02D0LKW6hz7Ladk8_fYbrgGhy6qMYqhfGIlVnlhK0D3ycmFTocw4kj8Mc-kf5d3n_WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
🔴
مدیریت باشگاه نساجی به دانیال ایری قول داده هر کدوم از دو تیم استقلال یا پرسپولیس رقم مدنظرمدیریت‌نساجی رو پرداخت کنند رضایت نامه این‌بازیکن رو برای آن‌ها صادر خواهد کرد. ایری در شرایطی به نساجی اومده بود که از مدیریت این تیم‌قول گرفته بود که او رو در…</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/27165" target="_blank">📅 22:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27164">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/neDrS1C3c18Kjly-0oRjQ29fP16IvJSSgxq3HSfY3BcCPtWPv79qCcsyicB8KFVQ_jiJvljW6n0dgbjhKItaTflWvwqJKePqlD7sMyHkpRFK1537IZU91wlQjhsVL6RkDUGv8IE2wo0-CoWrKISZU9JfgmjrT1zdftOAC8vSDGVEM2j8OFEXqPNUGi_BwQEqo1M4yQ7t83rVGHCtvJPNXi27ZqSWFSRi9fesoJf_-1Kw2Pdv1mvgcWI2ubySCOmynRFMVhgn9OhJh_V4BM-ihhf5w3Jt1DhJXvx3132RE7GLxTehg4PHj7J2amUpDK_jnsOViusZ6m7XrsB7y9uAeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
🎙
محسن تنابنده:
وقتی‌حال‌مردم کشورم خوب نیست سریال‌ساختن‌ارزشی نداره. دوست داریم فصل جدید مجموعه پایتخت رو بسازیم اما شرایط جامعه به شکلی ست که هیشکی حوصله سریال دیدن نداره. هر زمانی که حال همه خوب بود میسازیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/27164" target="_blank">📅 21:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27163">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vR8SaDeMmnWeGgR9o41eqZ1DorBPgo07-YhSs8nYgScDH-CAMkd-5g_DucUGVbsMnW_jXV410vKG5-DzO5shgAODX3xfK4qp5eqxAQbrTI-I-AIuXWaE-d0H4Udg70ZG4szWSpBuQjIM1p4RyqJmeD_l6MUaniVAxq2dxRmhpIul7e9nGdcQq5tbzgozBCkPHoDIpsoXw7nAHHiJy__XQwY1uVeJwUiho8aNWVdplU_wWCs6VMNuJPXEj3bUMSJz6sndOp1hm7TwxEJ014UfXeZ8LGL9zoC8j-3PN6u_dQJ76BfO8pQnbDPZGxlXpi0FZFaAlE3WDtktfntBO8-PhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
اگه‌اتفاق عجیبی رخ نده؛ تموم خبرنگاران و رسانه‌های‌معتبردنیاخبراز موندن وینیسیوس جونیور در باشگاه رئال مادرید میدهند‌. گویا فلورنتینو پرز با رقم درخواستی این فوق‌ستاره موافقت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/persiana_Soccer/27163" target="_blank">📅 21:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27162">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_BgRkJfEGcYG9Ax3MVXEihMWBShcZMW3mr_B0X-kdlKOxKf5KOUZ8-7jp9fF5pkgP9ScBhC2LZcv7oel9CIxGIdDYuuML11fSDKh7K4j8RWSJFObkksPngEhr0S1_5P_05NzejLK5fUg3xJz2NUoi2TczqF9sKwbprINwArcpG59swfsGObGcQJPqC6pnGqKtG3LSjpG0WBehxKyr7vuA6-sSKwkIFpFWgXM1F_OkMkAPhus2Yzle2rattXsuEZ6waJFkQMOidJQRierACEz4JaYFFxMvDtiXrNInqLPesfFEHPlEvQjHpqsYEbiJ1krqS2UuitBUDQXwjIqSr7KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق ادعای جدید مدیریت باشگاه استقلال؛ فردا تاظهردادگاه‌عالی‌ورزش"CAS" رای‌نهایی خود را درباره‌پنجره‌آبی‌ها صادر خواهدکرد و به صورت ایمیل به باشگاه استقلال‌ارسال‌خواهدکرد و باشگاه در بیانیه ای اعلام خواهد کرد که پنجره آبی‌ها باز شده یا نه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/27162" target="_blank">📅 20:40 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27161">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIpOLT2ahILg9rSSXbipqE1bwwn0WvujzZJzJeKFZocIw2q-IpwsqRmPk8Q72ETRaYCUfeqHj6v5ktZ_sKF1AOKp-nELxgHrrVo1tgPklEs_FLeAI_t6gzPyDcfXDMsVK6N5bADcicZ0PvoB6B_ICR1fZ1T1DqctTfpXfg1bJAOTQuhL9RBLO57FvYT_pyFZhYy1OoETIyOtPWvm8bvE3cOZTO0yfRxQOHuhFsxYCMnITY-g2EyRoW_LbKfUKqorSZdxy-MGhay4PYa5hcHsLnrIb88pw_EeXagjN2_oXbcX6MLvhEcGw1kq70HbSdUDNQ9Ad2tQPQPSjwe5iAidXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
ادعای اسکای اسپورت: وینیسیوس پس از مذاکرات با سران رئال مادرید دراین‌تیم ماندنی شده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/27161" target="_blank">📅 20:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27160">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVnIJAE7q69t9BnV-dkLcEzlaG2-fa3AuIFRAr85d7S2Y4EK7pPhd18Rsj43nK_7fazXZxwmqwQRNDL15shExSTY61Wfo7eB2mvDfrCnq48ybNd3js2YPMdLo7QG5RzF5NB2JJuj_57CytgdoFJBV-_4I83Pr3PsAFQBkTZOlOI95okCMvna4PFHuMUhrIWeeInenOPJTD1UvoVd2HykRrgX7G_V2_os7a1noxv84X8dM1-lpwO5VCyE6D--04fjbsaCLs_JrF7zddG3a2B5AW2v1pjHdRR3ggNpoVLYAIRZtHhYa5F81oozrDIoXJ2K5hg7oEhsugch6udV_-N42Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
باشگاه تزابزون اسپور ترکیه با انتشار این ویدیو از محمد صلاح خریدجدید خود رسما رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/27160" target="_blank">📅 19:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27159">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALR-zXRd-jImnhoRyur_-cfzyl-E3E1HPSKbLsSwrIl-lZVTLucqR3lR_JcpUrKfKRnvhrDQz9LgvlPloezpL2vXG8so2eZarga8sv3rj4wr-u_cfm1JzCWrICVoR9UivHJuYZgFxX8RwDAJNQP0Z8bRiTq-NNZ2B2wSGn1tOjIJQy1SO1IZrMLERav-A3FSiuwg2CrZMrApBDSQGNgUoGtFwXYmmavBtCMB1YDNqIHy_Lcp_kOyKed9CTiEBIwZdf00WfOd-JXYEpGTQXRbLId1DNFQC65CDvCSqhIOMOIdcuD_8KzDjdCCPdKJW4V9om-ZqSpVxYBJwnfle-9hWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بااعلام باشگاه استقلال؛ رامین رضاییان ستاره 36 ساله آبی‌ ها بعد از 1.5 فصل حضور در این تیم جداشد. مقصدبعدی او بزودی مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/27159" target="_blank">📅 19:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27158">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mylT040P_f6prCXpJX3P99zTYiQCT3klEDgQwV4akUhnxaluWuXrsj85-bQ8Cn14mX1IFR3YdbNn4Lb49Aq9au-USERRIgRSFLqIzdsjbPy0Jisnz3n5ZfxnFs6MNS022IPIJ8K-SakLpjiB5ooCIawL5weV_ggHiOvb3jzP6UOtiX1WqiLQr-IaUgsbhSiEAlN1tPQMswpNgScKCFCx7vGo-Csy77ma6T9CRnuzbrIqSDylWOunvtcHBVdLxS_9yN-i-fUNhYD9W6jbhWRVEOaYA4Pk9VMh5xnZV4fE1XhSryZzls9S_D5UcexwPNneXkZK1N9KrFoQfm1jJQKMfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ امید عالیشاه کاپیتان سابق پرسپولیس باعقدقراردادی 1+1 ساله رسما به تیم گلگهر سیرجان پیوست و شاگرد سید مهدی رحمتی در این تیم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/persiana_Soccer/27158" target="_blank">📅 18:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27157">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ToFP031Ikh_m7KSQGopUT0FBO68R-tDwBXK9Dfo6tB913h6zX78zuaq_iF7OBSjjIgcbFfovE-4audo22XxrGc6mKsJYJvfVviY887gtWgpMyDsY4cknJX6vC95RVaE7KQN8rIIxUCnyyyIDW38JQyz7NDIXQukFEOfYGh3jSEdjfTzzyx0zfozQzI4LE1pF_tSwtAqIKheflS-MvwnK6EJKGRt6hrq2eKoWI2GsdHB14qz9AVkX5agPLnFBFs2xJJrchhIQeSTmtWN9Iu0cOCimRKCOoQ7TLi-POtJN1OGuAuHf6beGJxbVT-x1RjtWUvSSFIMzM2MwmXG-C1B90A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
خوزه فلیکس دیاز: مدیر ورزشی آرسنال به اعضای این تیم قول داده کارهای انتقال وینیسیوس جونیور به این تیم در حال نهایی شدن است و این بازیکن فصل بعد قطعا در آرسنال خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/27157" target="_blank">📅 18:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27156">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BT9RLvw1mF5so-ypUsbGHFP5GmDz5GlI8b6TmLVYDbDH2mNyWN7aoxWXz1XLHMsxGdnHVMx4E86CvBfc0A-hk-Q3sbcVIECQcScdpfKoSUj0g03aVoWJVgDVptPrGf1IAPD5XwWuLOP5tKTeuqAgX1qeluO0hbdOszRRG8aEQV6vF24iujXDX_lJ60RYKaWlIS35IUtROCgQ0jSyY5JPUwH2rWAztg4yRCrYlc880GLq6bBs1sV4LKOrXGSJEZLJdDDomvaYNbthRVMX1MTMtnISeCtdf7Cq_76Cw3xMnq3GZrTaj4bQMKhiyDk5kh5XBYk9B73culuVAgH9sffc5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بعد از کش‌وقوس‌های فراوان؛ امید عالیشاه برای عقد قراردادی دو ساله با تیم گل گهر سیرجان با مدیریت این باشگاه به توافق نهایی رسید و بزودی از او رونمایی خواهندکرد. بعد از اخباری و گودرزی این سومین خرید گل‌گهری‌ها بود که سید مهدی رحمتی شخصا با بازیکن مدنظرش…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/27156" target="_blank">📅 17:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27155">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjtrkbjHiciB0WutUEfG2g6F_5M-no_Tp7W9Xd7bSiM-mw0ocu5yviDu5Sr0Zkm8xu7ElQ1fmmU_1KT092do_v3HAsZvizaD4EpXFGvwxB3AlenNkviMoJlt2tbycZ2c9BwY_KPrd-vP7kCmIKRI552RYZbKZQXM8Gwftwzh0zRqYogNvBs_vHth8yQ8k3eRqeF50eA_1iU1MkPp0OAB78Uj_5bGu33BUs1B2wwbcEXQyzgXAmZr2IqEInm4NNEAlWp9jONRYavhBOrxyZ0fxTcce6TzEhQsaP8rXFtaTyE1ZHqN2hEBZ7kctvH-UtuoFYGFaEIE8Fw8_Ci6uiBkpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های رسانه پرشیانا؛ امیر هوشنگ سعادتی مدیربرنامه‌های رامین‌رضاییان این بازیکن رو به مدیریت باشگاه سپاهان پیشنهاد داده و مدیرعامل طلایی پوشان اعلام کرده در صورت موافقت محرم نوید کیا آماده عقد قرارداد با این بازیکن هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27155" target="_blank">📅 17:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27154">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4LFu_JNrj-L4auhMasA-YKIS6XROGekPkT5vuetmUua-X6qqXPA798MhSykBoA4qgfrsQGrkJDuvOnRac8NkqmEP_7hOfAXr3kTHn9dLnMuKhYV6-ryQCcOYd95xpLGA2LdanGZYez2CzPqUbmOBkpy63qMJW-EAioJF0A1R0xLItyeEEurIODzxiRF9uQ7VkQuyGTVveog_EQPMAz2KDdoy5gVL5k8k6YosOfQtfEuK40A7oYjmfVEUxcpAHoegs-O7ca5yIdNyvnNcVulLjHcrJZP0QfDj-rFZKNEHqUuLAOujb0B9kuRr3S4HEm0aFtw2QzUumvbgVTXOh7vsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مدیررسانه‌ای‌باشگاه‌ماخاچ‌قلعه: ایرانی‌ها با کامنت‌های پرشماری‌که در اینستاگرام برامون داشتند حقیقتا دهنمون رو سرویس کردند‌. هر باشگاهی که با ما به توافق‌مالی برسد و حسین نژاد نیز راضی به این انتقال شود این بازیکن رو به اون باشگاه میفروشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27154" target="_blank">📅 17:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27153">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b7185f121.mp4?token=TekEibfDyy1EjDWYFmQxBdGuXxUhr6NTeHPolkA-dRapIG9mtodWKJ3DbyrlPkwpuQNTS-wtXi-HfcIix8zTm4uchToXuf47eAv08IXq9m1eKzThMFVtbowbroD-CTC5Lx9n9ZKE8KDEzClte3XLMPzy9aTuQgG-xKESz14RCIzIJGt_9EMUXN246KsMv4IL7GRagBtO8NUV5CXYLPSlrHJ2_Jjh5z4eHTkVepCW-mNx3W-NqVmweKjEEYiiOA0A-VcdMQi7tMEwgIEs2Cnmn4HmICPhp5FEudK7I-DWk4Yg4h0jvqykRZ-Fnkx8ZD9MQ7KiqSVJpfdnZapAhAl-Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b7185f121.mp4?token=TekEibfDyy1EjDWYFmQxBdGuXxUhr6NTeHPolkA-dRapIG9mtodWKJ3DbyrlPkwpuQNTS-wtXi-HfcIix8zTm4uchToXuf47eAv08IXq9m1eKzThMFVtbowbroD-CTC5Lx9n9ZKE8KDEzClte3XLMPzy9aTuQgG-xKESz14RCIzIJGt_9EMUXN246KsMv4IL7GRagBtO8NUV5CXYLPSlrHJ2_Jjh5z4eHTkVepCW-mNx3W-NqVmweKjEEYiiOA0A-VcdMQi7tMEwgIEs2Cnmn4HmICPhp5FEudK7I-DWk4Yg4h0jvqykRZ-Fnkx8ZD9MQ7KiqSVJpfdnZapAhAl-Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتیجه‌دو دیداردوستانه‌امروز درتور پیش فصل؛ توقف شاگردان‌آموریم مقابل‌افعی‌ها و پیروزی راحت سیتیزن‌هامقابل‌کره‌ای‌ها در دوران پسا پپ گواردیولا!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/27153" target="_blank">📅 17:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27152">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9McQlQrnf4GmEpJTQnDFzLgE6EyJj5oI6iBGU0v7jV-xxssRckOtTD7G6E7uZ5vSQL2g8RwQqm4FZcYqU_29UAzJCr5BaDbUw6LVF-PkmcQAdWFYvirHmwJyAaEUzUpAgOJjyS-O-7mTCBcGLhELbKPqMLYU7rdPlFgqzcuHiu4bp_Bi9Jfems57hNXMc9M2nXCbEFAXVJu4Gf2RwViBiI2zxo9pAKvcZpf4LAGbZM6IsCIFUjIm3okeV4UPEOkC_kT9kKASIfdqryRZZrWRQHGZy54mVkkM0FaTfL7_v8Y5t8KGGnhC1E2RFJ_UPRnzHoAac9r_B6z4c3aH2bAxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛ازدربی‌دوستانه دلامادونینا تا دوئل شاگردان ژابی و اسپالتی در کشور هنگ کنگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/27152" target="_blank">📅 16:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27151">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6UYbGC5aYcIgfjwGZA1078-Vs_gqioUcWfchMaugKRP69ziWnYPks-HieWuoxAHm9CDgSI8mTbmVKcD5kWEbc-YyxcEnCwUu8xh2iiCwMiLnrG_JrQfOAL71nA_gbkSLYCYbVxtwdE4PdmJxe-D_StSbTDsypQjsfkc-GLUp0QDuYEk4UoCiTn4MaUmBY06fj6hGMbscXFaZrJYRS6LOxTkqnzjD_vb_SaQDUMqgQEthRDkCNHXjjwTQ4db1CFoHczQh6tLXeUEPPv8liEW_Zy1cAZQFnEx2xx9Y3JeQ7WBJs2LvhLxhlcQzYmrdp6QJWUst13g23AhQFjc9HAlWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
#تکمیلی؛ امروز سرنوشت وینیسیوس جونیور در رئال‌مادرید و پرونده انتقال خولیان آلوارز به‌بارسلونا تاحدود خیلی زیادی مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27151" target="_blank">📅 16:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27150">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0d917f67b.mp4?token=ljy8SyfYtmJPRdChlGYI7-lnPAAlAG2916xFQkPe5V5kVbcn-VojPoWE9b0z2VTZwTj5R6TE0ODw_qCOwRc-H3Q8k8_vzmmD8M-jbt-3bZyuO0SyskO1J5fFiVhSxUU-wEIwIOKugPKGbMAOhAUv7iCLCUvOwSO57j8hq1EnxS1th1J6DHHjVxjXR67vCDrXWpJbmbzvzMqjUEt_-I2_iCSYCqs_uTy3Hzw8gMcKMkZ_aKYRJMS7XNWCCDxTEpDQIe1d9MMDURv3AIBLTUexZVxiwYp8nob-tKnYyfIGNoX7SLvfIOHyth_XHztgPdn5Tv-LnRmslxy8iJGiT9umcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0d917f67b.mp4?token=ljy8SyfYtmJPRdChlGYI7-lnPAAlAG2916xFQkPe5V5kVbcn-VojPoWE9b0z2VTZwTj5R6TE0ODw_qCOwRc-H3Q8k8_vzmmD8M-jbt-3bZyuO0SyskO1J5fFiVhSxUU-wEIwIOKugPKGbMAOhAUv7iCLCUvOwSO57j8hq1EnxS1th1J6DHHjVxjXR67vCDrXWpJbmbzvzMqjUEt_-I2_iCSYCqs_uTy3Hzw8gMcKMkZ_aKYRJMS7XNWCCDxTEpDQIe1d9MMDURv3AIBLTUexZVxiwYp8nob-tKnYyfIGNoX7SLvfIOHyth_XHztgPdn5Tv-LnRmslxy8iJGiT9umcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
🔥
فقط و فقط ۱۱ روز تا شروع بهترین لیگ دنیا و رقابت‌جذاب تارتتا و سهرابیولا مونده؛ برنامه دیدارهای هفته اول رقابتای لیگ برتر خلیج فارس!
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/27150" target="_blank">📅 16:29 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27149">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sve9nRhjqYllKCS8UK_QQnDviBqYnDR2mQmDAiMeDKBS9VsQsucLfa24w-2FbrGZjOAFJ_6KyKF9wu6UZsr9Lc4mcBCk3pNDbY05KMGAA5681Da4oDtdqr-J0gv4p9zooMkNd0qQjKN9CGTMYfcKfCv5-nHszZqS9JirG99GclZLFU36SKMi-iZfcuPZxRDIQhTuHWT9C-DaE5TrkVyxemupKhbYWI9iko__45e5ANBN6bAaoGeMOVFsrE5psKqQ9OtuQNXf6uV786uVJfbcr1L7nqOF2B7YRR_qpuLcgZ5SYEp6rBAeQjXkme91C5TUPVk33w1wFV0OOitFrCEt8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
چه خبرهه زیر این پست محمد جواد حسین نژاد؛ استقلالی‌ها میگن بیا استقلال، پرسپولیسی‌ ها میگن بیا باشگاه‌ پرسپولیس... اون‌ ویدیو هم فن پیج‌هاش ساختند. انصافا شاه ماهی نقل و انتقالاته. هر تیمی بگیردش برد بزرگی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/27149" target="_blank">📅 16:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27148">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/315f795088.mp4?token=hI8zyUU4n5gJdL2C_omeiFPEd4Lv7MYzM8t1CdElvh-9l7rML3chsR7kt3QGUaamWffZWWQyubXA1hdvuwp-ls_aeKpWt31g28bfqy-KutH3iRjh1nnSvXdJaJEIQn_r9d2sFLiYHbrAHgNGXi3j18C4emaDLS0jQNsg0MFR_H72ospN1WCocF8YyWugBFdMCWiW9kyR8LNA_A2CG3_sFMmkqXRv8yjyAVjU1RtFhqZbhzyzNxahqSxLKYxXAONcbotf1t4h3NZWswuyffew_Eq9HIXLGWGkigtpasLVJMjfz_v6ShBZTH_jeL7NyEZFM6jmwjvorrlL3_n4ASMxSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/315f795088.mp4?token=hI8zyUU4n5gJdL2C_omeiFPEd4Lv7MYzM8t1CdElvh-9l7rML3chsR7kt3QGUaamWffZWWQyubXA1hdvuwp-ls_aeKpWt31g28bfqy-KutH3iRjh1nnSvXdJaJEIQn_r9d2sFLiYHbrAHgNGXi3j18C4emaDLS0jQNsg0MFR_H72ospN1WCocF8YyWugBFdMCWiW9kyR8LNA_A2CG3_sFMmkqXRv8yjyAVjU1RtFhqZbhzyzNxahqSxLKYxXAONcbotf1t4h3NZWswuyffew_Eq9HIXLGWGkigtpasLVJMjfz_v6ShBZTH_jeL7NyEZFM6jmwjvorrlL3_n4ASMxSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
امید عالیشاه کاپیتان سابق پرسپولیس بعد از یه‌ دور مذاکره با سپاهان، فولاد و ذوب آهن حالا با مدیران صنعت‌نفت آبادان نیز درحال مذاکره هست و هر تیمی‌ رقم بالاتری پیشنهاد بدهد قرارداد میبنده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/27148" target="_blank">📅 16:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27147">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aee60bdfdc.mp4?token=Eb9cVMtGeBIWbhuQCFe1aGdsBp_JjFHcYhJSP27eSjX9xF3YWd9enmGPS3Za_oEgG_5qy-5Z0kclU3vqX_U2Aph8HPGh21M-fJy2nISfAOekwiMOVeXRYQqy50_0YrtiJoGSq-f8kOco52GATALyZhTb5j-xUbEDAP3LWlBp1Y4HxKS8d_l54G_JQjlgrQwSRWSED5r4QSp-DP5QsuNHnbym-A1jJsG_-aPXFUw2H0RoCf9KeTsYm8w206rvxrqYojVWMhWuBxUr38Y9VcEE3ksw_e3wiC9EvpKFnZKmbsRQsUOf0SnzTZZ7NrU7w1wXKQL7QwzxwhlUHNLE2teUCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aee60bdfdc.mp4?token=Eb9cVMtGeBIWbhuQCFe1aGdsBp_JjFHcYhJSP27eSjX9xF3YWd9enmGPS3Za_oEgG_5qy-5Z0kclU3vqX_U2Aph8HPGh21M-fJy2nISfAOekwiMOVeXRYQqy50_0YrtiJoGSq-f8kOco52GATALyZhTb5j-xUbEDAP3LWlBp1Y4HxKS8d_l54G_JQjlgrQwSRWSED5r4QSp-DP5QsuNHnbym-A1jJsG_-aPXFUw2H0RoCf9KeTsYm8w206rvxrqYojVWMhWuBxUr38Y9VcEE3ksw_e3wiC9EvpKFnZKmbsRQsUOf0SnzTZZ7NrU7w1wXKQL7QwzxwhlUHNLE2teUCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
توضیحاتی‌جالب‌درباره‌پست‌جدید کریستیانو رونالدو در کنار ماشین های لوکس و گرانقیمت خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27147" target="_blank">📅 15:46 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27146">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vNmVo_oRs_KHI6SB-PVHuFe_9eCg5VdzXE8ZzRZHXYrfAf6lRuo64lJn3zb-dBgrga8z8mudSyFxZSwRkQ1sK29TVvT5-D7KIPt82-Jt0jYtISqTMRFY3WdHqPHkpz22NPsCsvULGBMqmVCoyxFEmYIFncuhW2rstjIR95g0j7IkQYCp9fT9L4Ip9Mr2HvwBEizVyBsJ-N2ex8Vc_B5zYZn5sSHjIbRUwcuHRJqAk0ummUWATQZn-oWUocTWQNIpdssDnwKHEH8F4GGHdW-Fyz24ADLTpPXlsvqXv1-VyP5YhGXxa9uGJFFaVnkSE2rm-5GOlW5WGdGXqFWQUL1RrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
فرشیدباقری بادریافت14میلیاردتومان از پیکان قرار دادش رو با خودروسازان یه ساله تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/27146" target="_blank">📅 14:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27145">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlMztFcH3ZRQwDcNzV1SjK14K8LkIsSEYsItQp_XhnQXSzW21W3O0ubiYSEarbbYU-eGb-rtvxtvntFQlH_HOg3FFrXsHD1f196do75MujI730qxE2ub8ubnbu0K1jrtYpqV7M5dn_xAq4GpqQGcDITtf2td3bnxMzeGEBISIQKe4O5VqO9VSemdxtjeCddQrs2y5dakBV1aUPcjqlz0TNRR_H_AP9UbrSTIjf0vll9BMAD1ILB-9_MSuTDp1DUNClA2Dfibuy0L62OsJeACgw1aWjAp5Rl9iED_45Gw8ZeGNWBFWU6DwErsMZ-YCJAaX8o9XaSA1NBJWB9kUBxWSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های رسانه پرشیانا؛
امیر هوشنگ سعادتی مدیربرنامه‌های رامین‌رضاییان این بازیکن رو به مدیریت باشگاه سپاهان پیشنهاد داده و مدیرعامل طلایی پوشان اعلام کرده در صورت موافقت محرم نوید کیا آماده عقد قرارداد با این بازیکن هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27145" target="_blank">📅 14:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27144">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09ea3c3b07.mp4?token=k4AMYJqc7qjn1jUPJgeWZEqmSEhtWBwySd1s2fV8T9LzKylHFhGgXlypFKTMa1pwqdr7PQnXKYCPrtWf1knF_f4pofp4SY5uRh6s5VAeFmIjFAPA_9moiZcH8vP3pKqdKlD8HcJYGoL034RG2Yjh0OS2n4ibIZSonmKCMQ9lVTBDim9yTh7Mh8pi0E06Xo0VL38fSk7DSP2i198ChJgbo9OggEmzF9TdNZcmFbgh7E_YYttpbEWmyyVS81GTbPWVZo5ioJjvixQjShME8xI90uztymxtw4WqjIbBBxEwiwoshfKV9sCFBLyMstEG_OSPSOrlgSfbDpMpW-Ul43lkp4XEu4dhJQ_Vkgb9hP-3JU-nU6jTZC7N6c654OpQvQwDmDYzWA0A4ojuzqJcBy1qlU9GJB0tmTdS8TsnOA5n2lVRMvA5XFATs5RRaaVxEU_bG-SSxXFApVs60vPKSPR5gSyZebEd5Brwid2YESjo9cwy4lifJCjHWeC1kqGx9V0glbR5kTeq22WilLaxaCnjV7jPTs_JttHOxGphkavwly5-TxcSYwueXlIj1zVSt0UCbUgqIPP9GFXhO9mCHQfVd5jJ_ppBQ_lTz749JYYLAhbRh-4qemmQnbVcReJ0AXKaOJ91uUr2kebd7G0CGhUvQXMQS45klbrXAj2ERLyZfLI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09ea3c3b07.mp4?token=k4AMYJqc7qjn1jUPJgeWZEqmSEhtWBwySd1s2fV8T9LzKylHFhGgXlypFKTMa1pwqdr7PQnXKYCPrtWf1knF_f4pofp4SY5uRh6s5VAeFmIjFAPA_9moiZcH8vP3pKqdKlD8HcJYGoL034RG2Yjh0OS2n4ibIZSonmKCMQ9lVTBDim9yTh7Mh8pi0E06Xo0VL38fSk7DSP2i198ChJgbo9OggEmzF9TdNZcmFbgh7E_YYttpbEWmyyVS81GTbPWVZo5ioJjvixQjShME8xI90uztymxtw4WqjIbBBxEwiwoshfKV9sCFBLyMstEG_OSPSOrlgSfbDpMpW-Ul43lkp4XEu4dhJQ_Vkgb9hP-3JU-nU6jTZC7N6c654OpQvQwDmDYzWA0A4ojuzqJcBy1qlU9GJB0tmTdS8TsnOA5n2lVRMvA5XFATs5RRaaVxEU_bG-SSxXFApVs60vPKSPR5gSyZebEd5Brwid2YESjo9cwy4lifJCjHWeC1kqGx9V0glbR5kTeq22WilLaxaCnjV7jPTs_JttHOxGphkavwly5-TxcSYwueXlIj1zVSt0UCbUgqIPP9GFXhO9mCHQfVd5jJ_ppBQ_lTz749JYYLAhbRh-4qemmQnbVcReJ0AXKaOJ91uUr2kebd7G0CGhUvQXMQS45klbrXAj2ERLyZfLI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
به‌بهانه جدایی رامین رضاییان از استقلال نگاهی بیندازیم به لحظاتی‌که این بازیکن در این تیم داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/27144" target="_blank">📅 14:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27143">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ek2W8YMiWYOMOWLRRlQX0VYaA6F5m2QDVm_LV00cGh3HfR5DmiXZzD1PhgxwKO85axC_x5-7E1as9Dfv-HCqGyw3xYP7zZS0mebfuRsAl9ai5_k5J5fbpIwlArQWWtMxFQKkXpTAM00yNpdFwtvM74VatbMATaF6aYYZAjwcFasg5dX5AXKKXA5Ce2JjF8VnFK5uSmZWfB0hHMC2jCLhfvFV1fVHhtcMyuegjXlBrH3tB_O6lQwSqimVfUy0kr_kxHNNb43fuLSrmqH-YHoaLEoWJ-JoN2BxBzRITPoDINUw7BR5TBqWTS9x_P6ryl2As_UgQfdveSXQ-W3dX4PoKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بعدازجذب دنی ولبک؛ چلسی ساعتی قبل جردن هندرسون کاپیتان36ساله‌سابق لیورپول رو به خدمت گرفت. حالاجالبه‌بدونیدکه هدف ژابی آلونسو از خرید ولبک و هندرسون‌بحث‌فنی نیست فقط‌وفقط میخواد تجربه تیمش رو بالا ببره چیزی که توی تیم خیلی کم وجود داره و رختکن تیمش یه رهبر…</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/27143" target="_blank">📅 14:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27142">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‼️
اولش یه لحظه فکر کردم وحید امیری رو برده اون بالا؛ لامصب ته چهرش کپی وحید امیریه:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27142" target="_blank">📅 13:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27141">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/590b770d9f.mp4?token=qJ1wlcbhP3kN7QGWg9k30wOvjMVLWJCoX9Awzvk8dd0GLqm8sh83fGtrtGUhgVD-DgB-TAGiG5HHtjiIn-q_kYLc0CpfgzZP4HMj_-6KfTo6S-B5j3KfA5xHJQktgMPSKlB8qT9kO0Dm_pvPdLHQFum85Bpe5xBYfTL4NZUoWeTfXD6tC79cmHOU_sUJ8tAsoKrmgxUti4UsLznt4ESSgUrMumqgfAsDjZimxk-JPjhg-jPhX8lhmSNpDv5RnJH7cbAxaKegXR94QdEmzp7r4xNnmxpRUb2IBLN0fGBhqcbW-8xmUmRrsPvYIlr1-G4t4roN_aoiSydTX63Ms6UGsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/590b770d9f.mp4?token=qJ1wlcbhP3kN7QGWg9k30wOvjMVLWJCoX9Awzvk8dd0GLqm8sh83fGtrtGUhgVD-DgB-TAGiG5HHtjiIn-q_kYLc0CpfgzZP4HMj_-6KfTo6S-B5j3KfA5xHJQktgMPSKlB8qT9kO0Dm_pvPdLHQFum85Bpe5xBYfTL4NZUoWeTfXD6tC79cmHOU_sUJ8tAsoKrmgxUti4UsLznt4ESSgUrMumqgfAsDjZimxk-JPjhg-jPhX8lhmSNpDv5RnJH7cbAxaKegXR94QdEmzp7r4xNnmxpRUb2IBLN0fGBhqcbW-8xmUmRrsPvYIlr1-G4t4roN_aoiSydTX63Ms6UGsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
ویدیویی‌زیبا بمناسبت درگذشت فرانکو بارسی اسطوره تاریخی باشگاه آث میلان و فوتبال جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/27141" target="_blank">📅 13:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27140">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇪🇸
🇨🇮
ویدیویی‌جالب‌ازگذشته سخت و درد ناک یان دیومانده ستاره 19 ساله و جدید باشگاه رئال‌مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/27140" target="_blank">📅 12:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27139">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0jXHtuNUE9RkeAj1y_CFyHazo39rNx2hFfiaMwMqOoVroNOcDYKBt3ojXqPaLy7ydILZqLSJ3A7byr7XWwBUF8r5ulVBKU28qInq1iZXJoNEBs5T59PCIB7b1XBAGbUQEuDExf87JCypl1aVyMiNzvo4GxF3nlOCuXWoI4-6-fOTEkSQrgtMPWPi58XPV2LMpPBRH4J2EevIt-zLaYXdZMzN8fktDqsoCGeC_fgjShBK92YEhVvzweJ9lX0Akao19le3LJIkDm6kCxkRFYjPhPKRJl84z0CGyUqJwFbK1WB5nIbwHHz2CjdzN6AtLQFQWX_Q1719u01E25-01Lp6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌وانتقالات|فابریزیو رومانو: با صلاح دید کادرفنی رئال مادرید؛ فرانکو ماسانتوئونو ستاره آرژانتینی رئالی‌ها در ژانویه قرضی جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27139" target="_blank">📅 12:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27138">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WksYICKVpLgDxr2g5HceLoXbZVeac-F9E4ZdWrZ_awQFGxNMJXNPwvJXfy_zD3fva_Xkffu-Tc9SBSJeYzCh9zLK8vvwrcCDKH3VCkgvbI3DTNQAXuD56V2-gnbF9kqqmOWgjtVgZnQevDKT5AnzcP3q-dhkHomSQRA7tZaWb6OVu6CAcGjJV9N_W8EqTvG9DdmmQLxaZNaYmmUBMHTf6xkNCHB94npnk5MvpYfuunIW8FZ8RI0MRlcdzLgKS41NdgAuJCCNoA99ko_Vi9Iw5lNuwMIKLB2PZK9BkLTuiXE5ecHlIVHkLvCRptD6trYSNxV_LJ6bRLM7VQiQzVKcGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/27138" target="_blank">📅 12:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27137">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNZDbmqwamgUyGnCJ2nVBZtnTtKMbI6WjbHN4YShOZmvc4JzDzabQx6yCmSDfxo7MhDSVwSzGHFNzzs_FaLzMfrJQpj83nS3Pslk5OYMGUpWpNmvnfyUMDvFg9eHCBKelNSQPHZHc5QYE1czJ_tQevIzml3-tkkBYEngt3wktT0aVO6fMnTqRHHRQpY589_fJ8mZZFvzTcszSrYMa2OPrsSSnk7t3wz1XB0THI2crhiXOZlqLUGEjA6c63wPlo3awQdKpqPOUmQV533Jgja-xBaAyNqz7K6oLA8puRzb2uny1p5bKRhYxnfVdsU4v2eklV0zEavhNMsuuxbneceJVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛مدیر ورزشی ماخاچ‌قلعه به‌مدیربرنامه‌های محمد جواد حسین نژاد اعلام کرده که تصمیم این باشگاه برای فروش حسین نژاد قطعیه. هر باشگاهی دومیلیون‌یورو بدهد و خودِ حسین نژاد هم راضی باشه این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/27137" target="_blank">📅 11:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27136">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca19ec3ee1.mp4?token=Pnnuwk3yg4q6OMgFsJeaHbKvcJMd7E6aygMFvzlmJNZRPZg0nbVItxUDe_XYg3ckiK_48_uM9a5T_CJQgn0rJ4bCDmF4DqGf54z7mX4nT17mLfNwm7Tx6CRKf0nSiLmY1IvOmVuLym2k43BwaEYQuZkpYta1x7lsZd-5hW2SZ7Z-h7z4X6N7hxMygoIe3eP88KjnBODYU4bTxUK8ELF8L-eVT-RXEH0D-B1-axbqZr1XyzKb_-LcE67Whop1tGoOpOQEnsZ6mQunnTutRtdO38vrwDGIc-tW0czuuxOXVw6BD7xWXcdvW0jzHnJ-1WN60tGQBUuw07oIQeFCDZkvQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca19ec3ee1.mp4?token=Pnnuwk3yg4q6OMgFsJeaHbKvcJMd7E6aygMFvzlmJNZRPZg0nbVItxUDe_XYg3ckiK_48_uM9a5T_CJQgn0rJ4bCDmF4DqGf54z7mX4nT17mLfNwm7Tx6CRKf0nSiLmY1IvOmVuLym2k43BwaEYQuZkpYta1x7lsZd-5hW2SZ7Z-h7z4X6N7hxMygoIe3eP88KjnBODYU4bTxUK8ELF8L-eVT-RXEH0D-B1-axbqZr1XyzKb_-LcE67Whop1tGoOpOQEnsZ6mQunnTutRtdO38vrwDGIc-tW0czuuxOXVw6BD7xWXcdvW0jzHnJ-1WN60tGQBUuw07oIQeFCDZkvQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تموم‌ شد؛ صلاح رفت سوپرلیگ ترکیه! با اعلام فابریزیو رومانو؛ محمد صلاح فوق‌ستاره مصری 34 ساله سابق لیورپول به ترابزون اسپور پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/27136" target="_blank">📅 11:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27135">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1ef6701e2.mp4?token=b-EYra0nhX7fulwuYkrTE3EMqkfZOg1KzXC8K9nK3tWodIfHSbHzUqEvAhzWhrD6yIcXK2uff2vyRyzpgLzbTBgqPhz7LYq31CZDTcxnBUX9TdnS1hrGRhCuaSsAkii5N32f2Fy6luq9z-qsa36kI901vij2YHDX5xyPTbhEMhE4UrwECZFkiA4Bg16PWveFTfbaurMfdl6JqPkMtPeMGenLslWzNv9vYIlTTInfksfvRRqJ-AF-ItxgN2SvmJBFQHcX9ZD669hxbZ7WUKBrB-qK05DuX16RfB2cabpdSmOLnRpV85y2rnymp0vec6Ry5alOmP8qQFiTSaJy6DxTyoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1ef6701e2.mp4?token=b-EYra0nhX7fulwuYkrTE3EMqkfZOg1KzXC8K9nK3tWodIfHSbHzUqEvAhzWhrD6yIcXK2uff2vyRyzpgLzbTBgqPhz7LYq31CZDTcxnBUX9TdnS1hrGRhCuaSsAkii5N32f2Fy6luq9z-qsa36kI901vij2YHDX5xyPTbhEMhE4UrwECZFkiA4Bg16PWveFTfbaurMfdl6JqPkMtPeMGenLslWzNv9vYIlTTInfksfvRRqJ-AF-ItxgN2SvmJBFQHcX9ZD669hxbZ7WUKBrB-qK05DuX16RfB2cabpdSmOLnRpV85y2rnymp0vec6Ry5alOmP8qQFiTSaJy6DxTyoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش‌تند رئیس باشگاه رمو پس از رفتار نیمار و حذف تیمش توسط سانتوس در جام حذفی برزیل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/27135" target="_blank">📅 11:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27134">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0nnWTzpfuxdONd4dcEcxmB3WFlApCCh2BrlwCKh5AZW4QRrlW6MWEQj5rdlYgtNPSCathw6ID8gdv8emZa5SH6RB4CTi-TmirYmOjyPKK5KTmL4lFcYfz9U4OoJXA17qaLmt_foDlT6JLsKBqyg7ioqILg5YhztQmlhuOJlpfb3wiERxfC9k22W7vaZzixxsvsYsXixdrYrcKZWDEwW2hTEBKoogkW-TbWvTr67wHQLW0QgJzk5QnRv8_l5RcO1TjklUlNq-U33a38KaaeC6K5V0eyvAMq-FSj4tMjQEjN053W-o3wbuMu5bSYclNqI2ZHdrRwAsR3V2ixDKU0CNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
🔴
🇧🇷
باشگاه نیوکاسل پیوستن برونو گیمارش ستاره برزیلی خود به آرسنال در ازای دریافت 93 میلیون یورو ناقابل از توپچی ها رو تایید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/27134" target="_blank">📅 10:59 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27133">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c293e9daff.mp4?token=ePh22_-Cpt3PT1cpRvfisY80BbJgA08ZiB2aF982VEpkgSchJwtj6LHwpo7m7O51XT-Quv2pvcsClQ5tToAIV3T4ZFywH74sHOf0mwUmpPAUyuxO_94I96h8Ne9gdhpYhgS3wiEg2n0jwpFPqhJYytXlIjOasw7zL-0WmfRg6Ocd_26h_VJ7U-nmwT1RyEX9xIJe7AJ3OGdJWSp--p4nWLnt6WUDaHvy0ZkgEpqB03z_0iLBqS_bAKYc0_K9O3GRhkh2myo-py9wi3JBhgRLsv8T0-eWwz2EAk4QOBZIXLLWTBWlBO66TJ2e4T-PDWtRNKX8Onowj_oggRZMh3gWLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c293e9daff.mp4?token=ePh22_-Cpt3PT1cpRvfisY80BbJgA08ZiB2aF982VEpkgSchJwtj6LHwpo7m7O51XT-Quv2pvcsClQ5tToAIV3T4ZFywH74sHOf0mwUmpPAUyuxO_94I96h8Ne9gdhpYhgS3wiEg2n0jwpFPqhJYytXlIjOasw7zL-0WmfRg6Ocd_26h_VJ7U-nmwT1RyEX9xIJe7AJ3OGdJWSp--p4nWLnt6WUDaHvy0ZkgEpqB03z_0iLBqS_bAKYc0_K9O3GRhkh2myo-py9wi3JBhgRLsv8T0-eWwz2EAk4QOBZIXLLWTBWlBO66TJ2e4T-PDWtRNKX8Onowj_oggRZMh3gWLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش‌تند رئیس باشگاه رمو پس از رفتار نیمار و حذف تیمش توسط سانتوس در جام حذفی برزیل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27133" target="_blank">📅 10:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27132">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJ3cdzjV0sP9CfHJCewPnrUVHSmzuMj-JoYZgbJasmUAh9WWLWhKmiTKxxum0mk4VUnQKnrGic_UuEPobaNIwE1AA28dUKfJBS9aH5TulbV1ASaCvTKQzSWyvZLHpFLdVcZoV7sVLNOG40IutAFvcT7HVWy8BAhCa8qlwe9ql5TyrS7sq4YQKRyv-_2bDtCK_sxjaSwpT6mK6zHioUQRtYqXw35Lg17T8eekNay5u_sDUbkfN0g1vk7Xbe1cW9oQwMIEJixWdAog7Tq5lNd-11Y-I_3ObDAdnYgIXZFF8n7LEoWni-_d7C1tANYCp0l1aG-Rb7gfMiI7_lkwS_i5-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🤩
با اعلام جرارد رومرو؛ دکو مدیرورزشی بارسلونا هم‌اکنون‌درمادرید بسر میبره و قصد داره که فردا بامدیربرنامه‌های‌ خولیان‌آلوارز جلسه مهمی بزاره تاراهی‌برای پیوستن‌این‌بازیکن به بارسا پیدا کنند. چند روز پیش مدیران باشگاه اتلتیکو گفتن آلوارز خودش رو هم بکشه…</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/27132" target="_blank">📅 10:29 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27131">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qsvc9RnI-OfJ-XEU-QBD_B7aOFqck1FnZgsiIgmy3CwewKQfO8-PDBOHkfdOdqMcjEdYufDAaJF_qvc0WhIJBIeIBnssW4wdvVFKMzdVeC6vAnCWWF72gETsHS9w2AE9MR6aOgwwhpYEowjF1AqCbuFNuhfMxBKde3Aqds0G3WOarvJQPiRwcVEwr_c_eK5tAWq83DqdnxbpS4TBW1FNlKgEB6nENXEqtWflLNpqrXAJffuBjgkJqojeiceALAbtkrrEjZtAARLmByti3grogAs11Trh0KQz36NumG7_QlWVuHYb-aWhujYmozf7jUFXFyZ8VTqeFpeS-3CvqQnzpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ بعد از باشگاه‌‌تراکتورتبریز؛مدیریت‌باشگاه‌ پرسپولیس نیز با ایجنت ایرانی یاسر آسانی ستاره سابق تیم استقلال تماس گرفته و از او خواسته که یاسر آسانی رو برای پیوستن به پرسپولیس راضی کند. حدادی به ایجنت آسانی اعلام کرده حاضره اون رقمی…</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/27131" target="_blank">📅 10:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27130">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDVn9OW9ElUs_KE-Q_QWL2wfOWoxrhUrgiRw0FUG1EvCmYTmo1kCvqwOpz1--csWVLroKpaf8YTLgEipmM0KZiCCnUTGF5goearUUtycTa_hKK17UtRnqMVQBmgpH4weYkTeXIAZv7K0XpgrLrKzeIYsODoEg4NQOUQC1whw6NlVDZUj1TnpUR1X7UQhwoG_95zcNISUPseEfzEv1eUHPBrk6J6tGgCv4JS4OPX2g6rSvNJnx-6Q0LMRKqxxHeorf23_3czWZ1-WQHXro1MN26TulpNgaKQhxlqVRuG8SJiJK6PnzaXFhuTsUoKHS4IhlDT2cqflbWb-WzoWydff5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
درحالی‌تموم‌اخبار این روزهای نقل و انتقالات شده انتقال وینیسیوس به آرسنال؛ ستاره برزیلی رئال مادرید بی توجه به این اخبار با دوست دخترش در تعطیلات به سر میبرد و در حال عشق و حاله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/27130" target="_blank">📅 02:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27129">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aeUB-ugf4wqN9juZSI5vBygwwiKRYJp0jwIn9wYOMPxCWH3ly9F3FScJPHpzD_nNUyFpvJFSSMF9mXGrIkupDZ3fX24h6xjI922LutICUXq-cq6QIuofHcZpbMYgsoUZYxlMwjYk6ON2YtBcsCdNfzdBA7C3zjzwy1g9f0XPhxU7LKW0jF8XqyTcIKsGamxHiROFi0oQD0trq-qRKCAiX77erly-M8pzRXSxVJKl4kbX54ew2fVwZzjPKDdOV7HVXB640RnHcdu7mlMvMlqjA-SXzr_lTV1nafYwuSV0pTPXkpzJoAQgT6TMEeZWIgje9FowAPKeY7DaKB-bHxI82g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ بهترین‌و‌باکیفیت ترین ابزارهای هوش مصنوعی که از همه آن‌ها رایگان میشه استفاده کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/27129" target="_blank">📅 01:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27127">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dm8OigP_GpvHARBotLG3XlgiyOOcRccgHzrMA31vTT3FC53SQELuRbEUNLXmJ112qyL-4CMcbRDKX3nv6t1wXx0qUaknq8nOYamOigUb2QNyRJ0Ou5o9DPRN_9gh_7DkTwSHw4cyvqZ1M-atDPZvnOQZMGt1OnTJzPhviRh1o3Db7aKU4SQ25x1FqtqJGaElVd6y5XWmYax-SAqGjYaVUBz0AOgV7jEuTjah_XH-b25-EfQbRgPJYgZkdBjPf11T7SDNRTNhFflqdZY4aqWSDJgvvpduIgWVoAVC4_d48RqsA-958iFrzWcTx8zy855UQ7we-5NCKeYbUydxDtUgog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛
ازدربی‌دوستانه دلامادونینا تا دوئل شاگردان ژابی و اسپالتی در کشور هنگ کنگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/27127" target="_blank">📅 01:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27126">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pK5Aq4OKb0zHYnWMAKMMQvglJW77n7XzKUcbU4GGncqZyeWCEi7Iksw2bwrFZx-i5ibmsXG5nZVdZkLmyOGmWZZBFfCh8SGfg0SIcoDeISG0AUtrdhfBgPf1dTGHmDq3y9A7-CZPQb80A686uX0pywvbUi6gZdQIHabxIRtxpG5x48X3aqN06s-LLwL8MEeOypxPVSUA_p36-Tl7bWyNLKbU_mbbFsEKyqXFusVYHJY9iKF_4nIbNdG3yB06GEkUslZRv-aGyIo_YccesrX51q94yhRm-oHsAWxTc7mB1lXpMgexboO1DUIZ4qMESt7EpH-RzNio6QdF04J_EwURgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
از باخت ماخاچ‌ قلعه با حسین‌ نژاد تا برتری بایرن و رم در بازی‌های دوستانه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27126" target="_blank">📅 01:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27124">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNGyaKwO69c9MOk4vAfemE7FLiaCg0qFqLTSI-37JDjBZpOJ0WDJpzGtGJ191KOlPzeZ4u8aDALmKodop6B53MTMsk7vRgucmpePktWV6XqOHA7K8acaH4p-5FT_Fd_plY_Tmj9ydM5Mj7_09bPfx0rdfNdNvV9AZydFWm_dVn918nTSX3Iw0Ql8-Y5n9O1iqDBh7n9R4ING8fr8R9T6n57_8I5OnO7U2Tzc600E3pRBXXCFSpOGumvSNq9UvclSt2NQi3bg27NqollxLtl1x5o0TGVRsMTJQu3BZ-W6imaSwSYoXLU9u4UL3bbphu3KYe3ZMvFB0eOGrP_AerAt7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تموم‌ شد؛ صلاح رفت سوپرلیگ ترکیه! با اعلام فابریزیو رومانو؛ محمد صلاح فوق‌ستاره مصری 34 ساله سابق لیورپول به ترابزون اسپور پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/27124" target="_blank">📅 01:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27123">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Px-My9d0jJ89Jo3LBuZYhD98rEnxxXJFPzSlRgpsDNvwB887k_MZgIa4_v-p0teOHAfuU1MEfLjQ6aoWSMgd5SbcenfbUVvKZoLJLMhHUCQH4Io0Z6DFKoDVI0_yKD0FpRpswKt3Bq0efYdkI2StyHQQLytUzS_hgQ089eUnErCA6Os7pIslkEL4wPJ1SCvLyWLMQSy4dw5hcJEsCmOXNXgkwqsp-p9xwbvvPjQNWSGCe2J21yfW8oTlir5GRISaBZwD23SUQ4KGrSylA7MMhU0P0vsM29ogmao3DYNp5Uo2haNEopQbNXhqCWEz0XI8dVT603BRUGwB_uvXAycfJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال: مسی؟ فوق‌العاده‌ست. من به نصف دستاورد هایی که او رسیده بتونم برسم بسمه. یامال برای رسیدن به نصف دستاوردهایِ لئو‌ مسی فقط به 455 گل، 205 پاس‌گل،660 تاثیر مستقیم روی گل، 22 جام، 4 توپ طلا، 3 کفش طلا، 4 پیچپیچی، 6 قهرمانی لیگ، 2 لیگ‌قهرمانان،1…</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27123" target="_blank">📅 00:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27122">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmtVz_X-r79yzXQ0PfWwK-iyOxIB-Q4Zzx8C_sh8EzJhcadZ1R2GzV0VaT9wpdaQotW6WhPtK9AlQe72Q2lh1BX0Lwi-aWego1kzHehsZdRwaYZ35HOU_JBtpLyej-OMTHuC8iOu1RNimtj4xPTD_lKw4ITOzr524ePGFRf0rBtu48gs9H341_SvEKm9zE609i9-dSyNNS-VPvs330K5pGtQSm8FMjGcBBARR_1YLYNE3oNniWz7FUgNCkh0VR1ueKTdD7UfiBl1lUSKgRdU9xRy-eIUf6UrM_XCfH8UA_hb3jYsOD2y2FwKvPLWXE-s2weASQV_8c6Vu-yaoausQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
سعیدفتاحی معاون‌ورزشی‌باشگاه استقلال: قرار شده بود امروز عصر آقای رامین رضاییان همراه‌ با مدیر برنامه‌هایش به ساختمان باشگاه مراجعه کنند تا ‌اقدامات مربوط به بازگشت او به این تیم رو انجام بدهیم اما برخلاف قولی که داده بودند عمل کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/27122" target="_blank">📅 00:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27121">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwB_aNi8gTZVEG3NHM1iqolpVp60Bw-G0iW-bEg3nBF1neN-Dclwp7aVITuFoou7M-lJwZgb8kNw6JJKTqvzBY4sos5dIWCm98EEn9s0yKKESutdQ9ghtgC2m4Iuin0-kwVpxwSB-fUbjAWuZDO52ukA1XbvBFSLfMImdTFNDrc6qE6K70pxa_QEnD9_A3SeRaffctbET6fDnS-8p4Tz3rVrs-2PSCDxfipr-tGq4asi2Mq_S9f8m0Si6ooKv9_XzIqWh9eehLi2nUIJPbNy_Tb7tMWbHc94daG7S-W7-frT6GE8ciluQWFCy5164yFsBASXi0F8NlGGT47r4P1_9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
طبق‌اعلام‌رسانه‌های ترکیه‌ای، محمد صلاح فردا ساعت 12 ظهر به‌استانبول خواهد رسید تا کار های نهایی برای عقد قرارداد نهایی با ترابزون‌اسپور انجام شود. ازطرفی‌هم رسانه های عربستانی میگن الاتحاد میخواد بارقم بالاتری هایجک کنه صلاح رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/27121" target="_blank">📅 00:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27120">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NoWo_WSuAph15LcrJ9gNP47cW4cUCJQT_rsLFCX4EIMEVmQaX-yjyOqBnxEXuAP2ADLcfZXuH0nGBYz6FU819CTmc-CO6OMWtaC_pebwT150IJ_w5wfkedA0MmsQF9x_Q1ktnnbfVGxpYFJ_sWbxKhigg7cKcYbU0H56yA4HYDTkk2ELQOcyTJ5Fqbg_Jcqi-wjoHGhFeDLMnsYQ9BUbNh_75U457ZgBfRutXJt9WnZGg9gxzkoTSig5rRq_SJSLatl9tc48GLqiseM51JQxeivQgPv6LrZgSH-CcHdIepap9ogthLUwX6Suyk1w9CoSgna-kbyg9MZH0DuXjpmdxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال:
مسی؟ فوق‌العاده‌ست. من به نصف دستاورد هایی که او رسیده بتونم برسم بسمه. یامال برای رسیدن به نصف دستاوردهایِ لئو‌ مسی فقط به 455 گل، 205 پاس‌گل،660 تاثیر مستقیم روی گل، 22 جام، 4 توپ طلا، 3 کفش طلا، 4 پیچپیچی، 6 قهرمانی لیگ، 2 لیگ‌قهرمانان،1 لاریوس نیاز داره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/27120" target="_blank">📅 00:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27118">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8a21ccb63.mp4?token=Yvx0ec98VqBEIYKRQ81pzXFMvu9tC5dNhq7oh-por5RZ9iPG_TfXtsTX7rEff5D4nZSEQeuT8xoBGiqfpgKSemwpFddfgNz4snQr-BKVwQXL1w4UxCtXMzIDC3gEmI6pMOnJK97EH3WDK2yPsVhiyFtXNLnrYyrHeFvELuFa8TmB9udbLSgrWbBQF3-kbVgEWRtJeiM6HM0Lig6qBFuBHlYFvDW2VeWifhPr0E0J0UEvH-PwS1PkKXxh8FMo2qh3nQS6T14_QD9T3yQ8cymrCiDFcClpRlSjfoPyOthbla0Rg0HwbWZqcQ5sVa9r-i-rIuF-Nb8PCwBIEMME7Asi122cDvADn6-NAW1VJtsr2RelR2DT0e0SA24jd8LKlFy0DsvOPlTw67apE_ehrZ8lRLcbSL5J_PH_d6ad1tUiPG1LiTrUNbWg68wR6moNtbDRVFn__e-t_xnsJml3pgex9TQ1xRxa0Yq_3BjHPjYsorin8GGydB8S-pGah5x1ALWZifVFgVi7uCDbrEdjtTGop4-hFNzKbIiOUJc05oHIn8NoytslVio9WIhwgDdfJ-yrRjApYXogS9xQHoavZuYnF7iUxcQaJuNmcVST_ITJ8N8D-bN0BdpAb0U3j8vyh_fl-K-Xp5rGzBS-c4oyRVqzlUPa7OUhvpP6LpOi4bYvj0E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8a21ccb63.mp4?token=Yvx0ec98VqBEIYKRQ81pzXFMvu9tC5dNhq7oh-por5RZ9iPG_TfXtsTX7rEff5D4nZSEQeuT8xoBGiqfpgKSemwpFddfgNz4snQr-BKVwQXL1w4UxCtXMzIDC3gEmI6pMOnJK97EH3WDK2yPsVhiyFtXNLnrYyrHeFvELuFa8TmB9udbLSgrWbBQF3-kbVgEWRtJeiM6HM0Lig6qBFuBHlYFvDW2VeWifhPr0E0J0UEvH-PwS1PkKXxh8FMo2qh3nQS6T14_QD9T3yQ8cymrCiDFcClpRlSjfoPyOthbla0Rg0HwbWZqcQ5sVa9r-i-rIuF-Nb8PCwBIEMME7Asi122cDvADn6-NAW1VJtsr2RelR2DT0e0SA24jd8LKlFy0DsvOPlTw67apE_ehrZ8lRLcbSL5J_PH_d6ad1tUiPG1LiTrUNbWg68wR6moNtbDRVFn__e-t_xnsJml3pgex9TQ1xRxa0Yq_3BjHPjYsorin8GGydB8S-pGah5x1ALWZifVFgVi7uCDbrEdjtTGop4-hFNzKbIiOUJc05oHIn8NoytslVio9WIhwgDdfJ-yrRjApYXogS9xQHoavZuYnF7iUxcQaJuNmcVST_ITJ8N8D-bN0BdpAb0U3j8vyh_fl-K-Xp5rGzBS-c4oyRVqzlUPa7OUhvpP6LpOi4bYvj0E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
فدراسیون‌ والیبال‌ ترکیه‌ به‌ این‌ شکل از زهرا گونش و خانواده‌اش بعداز قهرمانی در لیگ ملت‌ ها تجلیل کرد. گونش با درخشش در لیگ ملت‌ها یک تنه تیم ملی ترکیه رو قهرمان رقابت‌ها کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/27118" target="_blank">📅 23:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27117">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EeHL0bj7xvJABMdwpKw1kYQIJisinH0Eb5LT7b2z5fp3L5ctQNQhUOpwlWOgrK2ERPSsaGne12FZhhm5lm1XaZQ8Nfrhs4Aeg1PBNQ5qomJeBESFPifgUanJqQJhh3w_5topegzW61bsUs-JXb-PEsOJeu-6Hk8pC9VDc6X-sPVPOTGQD4Nmzrvy-mWDFwoCQNyn5isFkf3ehQmBSbpy1oiXebl8s4RFCM_KtjxSozrSrdbBN0EqslYKa259vQ_nu79L3PADj0vL8kPjZYEayT6mwwkl4kDaImQplHBadF7xGaVEhitoWcmoTGIQzkrvU5dzAITbRIHBTcuxGp-F4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
رئیس باشگاه اتلتیکو مادرید به زبان عامیانه گفته؛ خولیان آلوارز خودشم‌بکشه نمیزاریم از اتلتیکو جدا بشه. 100 میلیون یورو که هیچی 200 میلیون یورو هم بارسا بهمون بده آلوارز رو بهشون نمیدیم. مصاحبه های آلوارز اهمیت نداره. او موندنیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/27117" target="_blank">📅 23:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27116">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnjxM-hhvKmlauS7Q3yFJ23LN8_tKb_6npdaFB2GMKljq8G1C-YHk53nPBxyRIGvKqDTF4kfADdfHRkaq0dJcswJWkbxdss10VE8vGOmWGjGFrBqv9iI_TRXXYM30cmm1Btl2td4mBD7f5UejKbJxlIDeb_ZlWg1Kjwayw3rRDyeeoGNw4I7Tz3Um-c11iNN4cQcMN7SN-8OimS48aXAvGH2htoa5z4YEZuOYhqkTpwcmvfph0wMcXUKPIlVbaRu7AOn91AB9aJhaenUwjRY5t5B94gEw2Rg3TIiarYpZLKknBoztzGXAiiG37KFaQT7tmjV-Y60yFYSzaZ_99zWlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ مدیربرنامه‌ های رامین رضاییان امروز با مدیریت باشگاه استقلال مذاکرات مثبتی بر سر رقم قرارداد این بازیکن داشته و قرارشده‌ که رامین رضاییان عصر امروز برای انجام مذاکرات نهایی و عقدقراردادجدید با باشگاه استقلال وارد ساختمان این…</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/27116" target="_blank">📅 22:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27115">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52510ee628.mp4?token=tNocQxbTVXInfcc74DabTIN43bS_5XjADuDQSf_BvIdzksGdypqq6l8XOLFvpBqI6ZxF-iv8wwtrzbNfJcvBUZd6mAxehXMaRj_ggGVy1qncUU0rmkPEmvJXaQS46H6DZYjeEU4F5gtxUybut5m_sogfTbvEQzFRTLVb6QV37_3itP6bCDizHCoCpQmWEtstpBOI5txgNg2ZbWF35HgB9JbW2zZSCljrLmIchUe1Z3FREG8cQrzhSY1F20I7qFKeUu5TnP-skbLGkR53ydmvCkWNsve5CJ2bdTWcq9XHt7RiCG1qJkTb5aUWu7BUki70-u1ckGw5a_QF_h7Il0Qxvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52510ee628.mp4?token=tNocQxbTVXInfcc74DabTIN43bS_5XjADuDQSf_BvIdzksGdypqq6l8XOLFvpBqI6ZxF-iv8wwtrzbNfJcvBUZd6mAxehXMaRj_ggGVy1qncUU0rmkPEmvJXaQS46H6DZYjeEU4F5gtxUybut5m_sogfTbvEQzFRTLVb6QV37_3itP6bCDizHCoCpQmWEtstpBOI5txgNg2ZbWF35HgB9JbW2zZSCljrLmIchUe1Z3FREG8cQrzhSY1F20I7qFKeUu5TnP-skbLGkR53ydmvCkWNsve5CJ2bdTWcq9XHt7RiCG1qJkTb5aUWu7BUki70-u1ckGw5a_QF_h7Il0Qxvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
درمصاحبه‌جدیدخانواده‌نیمار؛همسر نیمار از قلب بزرگ او گفت؛ ازکمک‌هایی‌که حتی دور از چشم همه برای اطرافیان و گاهی حتی غریبه‌ها انجام می‌دهد.
‼️
البته ستاره واقعی این مصاحبه شیرین، شیطنت‌ های بامزه دخترکوچولوی فوق ستاره سابق بارسلونا بود که تمام مدت توجه‌ها را به خودش جلب کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/27115" target="_blank">📅 22:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27114">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0LnBibsmUN_xfP68Bm_E_-LgRVG3x6Jb-8jZIhMFdz5xY85ceLFpm_djiRAXjkAyM1Pi2a72MpYrtmH0x6HOEnMrW-Rqjnz0pXF8avSok2ubRQIfxd9ul1hzr9JOI0EHzNtBCDjIQ40dMEyMIddlis33wtIf2l134qimSExJgiPo6Ja_MWOC3JItRKqRpJAtK7VrRSt4KKo7JjQz9CwsQk-k_0oVdQbYa_cMxXbl_IaFD7i3FYhbzcNOiXWAX6Iri31kTIE8a43aHyESDMkHzPY0ZrPcpTnY8G6KZzT2VtlEFMTZedKtxdcyG92b0Lns2rHWXoDPsKBSSu8z_I10g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌انتقالات|نشریه‌ سان: سران آرسنال به درخواست میکل آرتتا به‌دنبال جذب یان کوتو مدافع راست 23 ساله دورتموند در پنجره ژانویه هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/27114" target="_blank">📅 21:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27113">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JAAra195LbG1-3oNtBBlonCNINZLb4no4tibiFHLItQIA1CLLy3zuYEfv8yLQXxWOAAgfea-eS9vWgsnASV36vBfy9a6AdFlD_YDRS5nVIra5AKde4A6MrRIgvMq7s6QSnE598d7mg9j7bUkyHGPFl22AdMIzMEcxIxijTddeC8EakTCSLVkcN2ppe5XUvFNIpAYOTXBNF1FX_h2_wDMtVa8TcbQd2whmhePOlga-rorkLHs-2JoSSOOeCLT3chF_-P_hAbaURFgm5FiHav_Rvo_y8mGBlWXMbdMrWH7JtetYuOEHtiohUEGJp1P1aDJrFKXvwRKpMscImq8ygROkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس اسپی مهاجم رئال مادرید:
الگوی من در رئال‌مادرید کریم بنزماست. میخوام با گل‌هایی که میزنم همچون او در مادرید محبوب بشم. برای دیدار مقابل بارسلونا در الکلاسیکو لحظه شماری میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/27113" target="_blank">📅 21:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27112">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClIYwsGR4XMTYBmFSVAJjyYa1Q4gjTu6XaEFwEXpnD6CcplTTGPbhmlqEnVeYsCMERmTXAnxTrk1f8A015dGMYj763_5g3m4T8wjKGI8IQR8aTqa_aGrpaT6w0zv5Qw5Jy-S6WYZozZyC6c2KM_vG6PjFMMaFTWFZ8TixYiH3arkPjgeKnyXKDh2YtLNCtGi5v5_1kaH9WKmJJQT6ZtUGT7ERZ-XYgpAxCGyboa_Si1GCJ1oRUSdymN5nU7O7mersahJZ3--hBTZyimD3ZSXWIe_EfGsjt1ITHB09ZD9CI9Q2Giz417YIQKZ2x21f2N2rs88EvjQ23Fo6mZLgZBrhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ مدیربرنامه‌ های رامین رضاییان امروز با مدیریت باشگاه استقلال مذاکرات مثبتی بر سر رقم قرارداد این بازیکن داشته و قرارشده‌ که رامین رضاییان عصر امروز برای انجام مذاکرات نهایی و عقدقراردادجدید با باشگاه استقلال وارد ساختمان این…</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/persiana_Soccer/27112" target="_blank">📅 20:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27111">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftvaSKbzHM5E9kbFbggkSPz5AGUf7nbueqnnZmH2uopmYz-0vKw2oObTLtGZpYKjIdp2ZEcHqR8lxEN86p5tWaEuxjkI0re6-PXEyiDK-OIKOTFTEQj6JnpafQuaJMyGTjj0TMP1IRekXwnEn-n3DDejELNtBmxG7YBPQGpya4N1J_ae41-gASb05tOpg9ep1m9TZcTB_xIAxG5RT2IEutLpN5-tTTVW3aL8es26_NMra55NrBDx7pObViZuumK0Lrp7YAcWN_QSWkztA14rrVNs-HXf6nI1PPPsPxt_GtXx6xfBbSciIabcAc3Aky0jrzSS6EdDejF7EUvZ3gl3fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فابریزیو رومانو: باشگاه ترابزون اسپور ساعاتی قبل‌پیشنهادی دوساله به محمد صلاح ستاره مصری سابق لیورپول داده و منتظر پاسخ این بازیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/27111" target="_blank">📅 20:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27110">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UR_P_6FbbiHhW8jE0PCbdvv43XLSHBz8SUUsTsRpOeCk7wA8sIOTVEaCVbvzrLLk6Uo_-uKd1y-VQUj74s55ZyvraxqlTU5xUxneI4pxJJSD47oi82jFoapLzSOIJ9x6PIfozegNI81fc2VtHq_UsjMacgNKxb_1wschsU5CnABxrmRSv8YO4Ccy4h2RZFB9-D8M1w_V9ONEXexwifiQ-Y6-Kzfh2K3Arvf4PTgP7gJOrRqq4Wrxdl4N9UXrxU7W8ZhWfmDmhSBzSkipZ6iy-q1lNO0j9t-M2fCv-VJc0DnoAcfmExRF4YHsP-zLOPsM0BCbnzDnnQ8xu5EYXDWTrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
استوری جدید آلن هلیلوویچ هافبک تهاجمی کروات سابق تیم بارسا و مدنظر باشگاه پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/27110" target="_blank">📅 20:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27109">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/baBeeuxhXPrW8qaoMPmSFL9Q1QzOpeh_fbh6hPAxa6WJjPLK4121zryrz04rKXNjSMxRN3iZG_GR0Gm-yJtDhQ4B3cKws8BKDIk8uYNoO2mSub14J_GgOExVumQ7_OCEcZ0iI4GKKV98n4HuIuaqdcTS5iHjTRmlUC-huOnA6i3plblLkHwSZb8R8VhbiwMIj58q8McMjE8MmACJfVknGR9Bjb_mV4s2-aTifgOWPsk9jwHylEbIeo-Py_JNiXvkP-KES7O6y1Qn8QNdHcm2VTR8TFOaSDrur35FyufBlaWYwWRNMqe7T7q2m_G73U2CnK7Gn_VWUnVzaDoBB6sivg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
نشریه‌مارکا: انتقال رودری و یان دیومانده به باشگاه رئال مادرید نهایی شده است. بعد از رونمایی از این دو بازیکن پرز پیگیر باستونی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/27109" target="_blank">📅 20:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27108">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EuEJF0vK1U6DV_YGNM1hBWJv4NmsPaPc2g1rRrn1WrM8QVV9vqy6tY5wuutGMcEhs7AaN96egk1m0QsxltmM-rnZFJYw5P6n-VM1RmqmDCmpVXihJgbTqBhvz-x2RGSC2l2maWfKzIuJGc75_sDFhUdaQdtxT7b1b3k9P6U9VToDbyj4VsrH0ANzUI7qVwxqXAJ7dQvxx1IUrCjF22n-pwqx9Soh6nvh-e_Cm-ij4TCMQtqnnAK-RfxZEAdZBB_qQ67rdornROta361wbmx8V5v_dsVTzQHAuEVebjeevSU7sm3ZKO3PR4obNVUP2fiOYS_J2hjSPDa0LK3weOSdRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
پاسخ‌نهایی باشگاه‌فولادخوزستان به پیشنهاد باشگاه‌پرسپولیس‌برای‌خریدابوالفضل رزاق‌پور مدافع چپ‌فولادی‌‌ها: 200 میلیاردتومان نقدبدهید تا ما هم رضایت نامه رزاق پور رو براتون صادر خواهیم کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/27108" target="_blank">📅 20:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27107">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMUONfIkrm2m6DDv_Z_Q8pjhbJ2G-Wj84cEhOQFXYh2hI8U3u-IvT1qVC0KMkrsapVaTZUO5mGtBBm9SIDHTtW23qR8LiYCKGhJvPV3YVkWpgz2kNOTrYC2RsA1ihYAFNj5YljdHqd0eSWKnmPIK1XT1DVpq2FjxAP9VTLzbrgRoSTJbn2nqM2cOgD3JF0I7s4rGrU4rL9Oz3b4WcbnncR_ljgEN3QlGEGmWmd44mHnPESQm-dtlClQcmgW4ZnANshNZcnZYSUnpUhsIY03pFuZYpKn28tFeeDxsLwMdSs6EsGbXqoZfQSSJszK2MwuLFF4dthosDBFOKlnik0Qn0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مدیربرنامه‌های علی نعمتی؛ این مدافع ملی‌پوش باباشگاه‌لوسیل‌قطر درحال انجام مذاکرات نهایی است تادرصورت‌توافق با این باشگاه قراردادی دو ساله به ارزش 850 هزار دلار امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/27107" target="_blank">📅 19:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27106">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd6169d08e.mp4?token=BU0wDLxfSp_r8x0x-Y4MTFxu3HNjOBefCGQ1ncM3zbionp7g8KcnOWMkQsLYGzNAE2nvWguNRIiA-Ioz8DuhaOw9Vf87IDZWoMnHD2sJgnmFnCxPwSxt9gZBz9vOSzqc5ufhGOW14a-kTA10kytatkB9YXBD129UEy385vl76RzZgXJ72QfmrWXxHWQlL0OmWBztndgG-9rOcGcb-ia_2I8LKcJG6IHShtmUe1z-WPOdfI8hGETVHbac7jftMfOsAGNEBeS-BvhWdIQwt0QfhxPuJPTv7OZ3h8TkOUcbGin5nPql_V1gdd07tbfg90ecPQyPuDbmUMHKH1ODbO0R4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd6169d08e.mp4?token=BU0wDLxfSp_r8x0x-Y4MTFxu3HNjOBefCGQ1ncM3zbionp7g8KcnOWMkQsLYGzNAE2nvWguNRIiA-Ioz8DuhaOw9Vf87IDZWoMnHD2sJgnmFnCxPwSxt9gZBz9vOSzqc5ufhGOW14a-kTA10kytatkB9YXBD129UEy385vl76RzZgXJ72QfmrWXxHWQlL0OmWBztndgG-9rOcGcb-ia_2I8LKcJG6IHShtmUe1z-WPOdfI8hGETVHbac7jftMfOsAGNEBeS-BvhWdIQwt0QfhxPuJPTv7OZ3h8TkOUcbGin5nPql_V1gdd07tbfg90ecPQyPuDbmUMHKH1ODbO0R4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیش‌بینی عجیب احسان علیخانی که چند سال بعد به واقعیت‌تبدیل‌شد! حدود ۱۰ سال پیش، زمانی‌ که عادل‌فردوسی‌پور و محمدحسین‌میثاقی هنوز در کناریکدیگر در برنامه«نود»فعالیت میکردند، احسان علیخانی با لحنی شوخی گفت: «میثاقی رو آوردن که‌بشوننش جای فردوسی‌پور!»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/27106" target="_blank">📅 19:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27105">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phTsaxsW12miKw4QANibZaLjtwFdp3etDZ5WTtGfJDI3WX7bcf1qA0-vvOWnA1NldNWs3UvOakYjcWw8k3HdtuGfLSgkn6m-pEDEmv5eDXdW0JB8ifpiYCbQ3PvleRz64_lzTShrXHJO3ajn758bKUOWwyD0Fp3hShfrXvCRg-t0EDSjRoRY6oMC8ehQh5kZuAud7rtq8cu54ywTH4HtvvpIdd3Rd2gzt3FXzrHv2vuBWUtIDoshqic8m8VxOUHRFTJMSnhOO1mDFCYsRizv3z2lTj96qRQiBLjBu_N-pIZgjPQcUBGvkF9LPLEolywRat6BmI2RpXFv2Nv-BaHXFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
سانتی‌آئونا: محمد صلاح ستاره‌مصری سابق تیم لیورپول برای‌عقدقراردادی یک‌ساله به ارزش 12 میلیون‌یورو بامدیران تیم بشیکتاش به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/27105" target="_blank">📅 19:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27104">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe05053c48.mp4?token=S1EyFqbw_XMkrk9miahGkwZThbBk_IY1GQiSF4Rz_c-fblLbHoC2M5Yqs1vUxDSj78iAjAmcGo_U883u4HlPrzx8rWg5zURcM6wxtiYbQssk_lfxSd1v1eL8yCxoPi_fljCb3eTpi0yLF72m6KTWXAOPkTBhOBuG9z7l4ZvrQxi6gg96GsJ4Yx_wpEm3dlf4_dmw3T1bucx_RerKW4CFMIC1_lhb2z6mmcDa2agDC3PcdKYfsswkOD5_f3yN6it4rF4QMNKPKXFa1hOeBGAe8rHw01r2DIy3d7nPR_Jc8pgHszcHbvOtC-XzltQryJU-EvvNN3H_OktacuxhtXqqTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe05053c48.mp4?token=S1EyFqbw_XMkrk9miahGkwZThbBk_IY1GQiSF4Rz_c-fblLbHoC2M5Yqs1vUxDSj78iAjAmcGo_U883u4HlPrzx8rWg5zURcM6wxtiYbQssk_lfxSd1v1eL8yCxoPi_fljCb3eTpi0yLF72m6KTWXAOPkTBhOBuG9z7l4ZvrQxi6gg96GsJ4Yx_wpEm3dlf4_dmw3T1bucx_RerKW4CFMIC1_lhb2z6mmcDa2agDC3PcdKYfsswkOD5_f3yN6it4rF4QMNKPKXFa1hOeBGAe8rHw01r2DIy3d7nPR_Jc8pgHszcHbvOtC-XzltQryJU-EvvNN3H_OktacuxhtXqqTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترِکپی برابر اصل نیمار جونیور!
ماوی، دختر سه‌ساله نیمار باشیطنت‌های بامزه‌اش وسط مصاحبه اجازه نداد پدرش‌راحت‌صحبت کند؛ همچنین حرکات شیرین و بازیگوشی‌های او دیشب بازتاب های زیادی در فضای مجازی داشت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/27104" target="_blank">📅 17:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27103">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/835360d02b.mp4?token=TjJiOAQ1OA47a8xpNXPcBv_MHzrPahg_Dy30bPf34mtXt3OvPKOr2hGUR9A8nk8ueVAd_OeRiLYzrL6Jf09eS-fpmzi4ycWIBrqiX2cIfjdJofFF--COlA64XG6z9fgtAtjHKZJ-bdSCVxYYKi9KIWHQRxcKHW9K9oVtfsLUsb-WnLWdpiQpUmMpUDKpWOBnG6C7utG0PztQN3gIajG9NDilxLUCT8KfJlJUy-A1Szwd4H6DtFF2Xt-8ixlrBUgn6R-6efhYwqkaW86ZyFWNRf6Wq0S_qE-LNO2Q8LI4ESn73GMTamVAEf5fEE9-7WRG7bRsEUpUVBVQmvTz0OGb4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/835360d02b.mp4?token=TjJiOAQ1OA47a8xpNXPcBv_MHzrPahg_Dy30bPf34mtXt3OvPKOr2hGUR9A8nk8ueVAd_OeRiLYzrL6Jf09eS-fpmzi4ycWIBrqiX2cIfjdJofFF--COlA64XG6z9fgtAtjHKZJ-bdSCVxYYKi9KIWHQRxcKHW9K9oVtfsLUsb-WnLWdpiQpUmMpUDKpWOBnG6C7utG0PztQN3gIajG9NDilxLUCT8KfJlJUy-A1Szwd4H6DtFF2Xt-8ixlrBUgn6R-6efhYwqkaW86ZyFWNRf6Wq0S_qE-LNO2Q8LI4ESn73GMTamVAEf5fEE9-7WRG7bRsEUpUVBVQmvTz0OGb4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بنظرم‌جذابتر از گزارشگران ماگزارش کرد در حد همین چندثانیه؛ گزارش فوق‌العاده گزارشگر زن لیگ MLS روی‌اولین‌گل‌لواندوفسکی برای شیکاگو فایر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/27103" target="_blank">📅 16:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27102">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUKQNZUzsiviQxincCYcqnuCBfqVG-G5oeN0rP7RIxkmUMv5UTV0w0E0ajQm0sfWd-Rfcje--d4JiosmbrqD1eaqCwCLLjG0b65APJ4xViV4Eia2WJGDltRgzJSQVJQZd2eLCNwNd3j0yBUhqucAwy_k6Qny4DSBMO2KhINoQNTz-67e_jtrDWV2g6TF44sD65wyTHi3enXgLwjgtkDJr6zB5sfuBxMC2nLdZTuURDUHQx7QBdn3EwEblw7TpP3wCadZz3FI-CPUbANh1JW8aT8ZTyDIPeaEIRltKTp6vr_VrreP7mCM7HF_xOoXa_-Ij3nKPawLSqT-cfFFXJAQDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
رتبه‌بندی با سابقه‌ترین سرمربیان حاضر در لیگ برتر انگلیس براساس‌تعدادروزهای‌حضور مداوم روی نیمکت باشگاه فعلی‌؛ میکل آرتتا با بیش از ۲۴۰۰ روز هدایت آرسنال، با فاصله‌ای چشمگیر در صدر جدول تکیه زده است. اونا امری در رتبه دوم قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/27102" target="_blank">📅 16:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27101">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40f136b3eb.mp4?token=lTTRXKjvUaewRiS6BpWynWoLUgUi37SrPvoG4sYTzdhZxk8qwXx6LPSDlxNsYU6udCx9jjehetdrM6BwKRG14aj641GqjhlwL-3-JgWNmPv86ofVSMwa9eY9Q_oZiPrv_0h51VKqFCseF2HgNcGfjUAj48_f2Q6MNaA15YLyZRfb3POcFHjlTuQmjLr5rl_KUVTAinuW798DQXa5fw43qm6PFUKbkOKw5mDb0lHGph0D9oubHx8I3aHnNDzBzW1A1TapsZhs6EWMnn6TpncUb3pZvfpcdK7n_VDG6PhANXgBK99H-yJmx5IEKxQ41KTxvT896HQFe-xIrMYUYczDvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40f136b3eb.mp4?token=lTTRXKjvUaewRiS6BpWynWoLUgUi37SrPvoG4sYTzdhZxk8qwXx6LPSDlxNsYU6udCx9jjehetdrM6BwKRG14aj641GqjhlwL-3-JgWNmPv86ofVSMwa9eY9Q_oZiPrv_0h51VKqFCseF2HgNcGfjUAj48_f2Q6MNaA15YLyZRfb3POcFHjlTuQmjLr5rl_KUVTAinuW798DQXa5fw43qm6PFUKbkOKw5mDb0lHGph0D9oubHx8I3aHnNDzBzW1A1TapsZhs6EWMnn6TpncUb3pZvfpcdK7n_VDG6PhANXgBK99H-yJmx5IEKxQ41KTxvT896HQFe-xIrMYUYczDvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو تو چند روز اخیر بیشتر از 12میلیون ویو خورده؛ رونالدو بفهمه تو ایران دارن باهاش چه تبلیغ‌هایی میسازن میاد از همه‌مون شکایت میکنه. طبق گفته رسانه های معتبر، کریستیانو رونالدو و جورجینا قراره بزودی بالاخره باهم ازدواج کنن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/27101" target="_blank">📅 15:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27100">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_amwroRMSIqwGflQntltPlaXD8mwubNysQBK1UfLo4ROGQ0wlmy6Xo24Si3oFWKJK1Zeoq4I09NeD27POvMz1vKqNkOdu9myD1vIIcC_ALlvUDFfmSVqK1Qvggofi5EVpwFsKRqU64wWxT9hX4EGmXz-L5Nb2svGvQ4jEjqY2uezkk7FM85QxIjLJ8Ry6o4WChz6rNFHb2TunCaXOv5ggOJpZcrMnecJ4okK4RqufH3Cy-R-KBuYVWkPw54r8hLOVpw20BUVSSzh7vrQ7UFYvFd5z2rYOnOatS0Phe9X6dPB3exy9cMrJh8Bucrx5gl-yfXDb7W9atV49wWxfoMlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنایی که بهترین بودن ولی از تیم ملی شانس نداشتن و از داشتن یه تیم ملی خوب محروم بودن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/27100" target="_blank">📅 15:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27099">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">قیمت محصولات ایران خودرو و سایپا 13مرداد
🆔
@Persiana_Newss</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/27099" target="_blank">📅 15:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27098">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jktz0RvdOWplO81YkUJC8uQMlgQz_CkRxHRxxkk4d40tHSM9-g-_zAex9TD3CwO6Ywo6fLdt92RXbWyRTr8JWXeQ2IaloPHGqxbLOQJW9YiVtssO005S5mylzTusTKB2cjVyA1k-PGjPG0yXqYrEKXo7FxDp8DuOB6x2bO0nXf0aUqGN1t9D44TNHFcM9RLz_gqUnSjX6O748HHFL3sHcmd_LYFFrFRBXi9HRx7L-H728STfiifE0WYVcQF2Yl5WB1cNaw7IUiaf4_z5eF-V6PFzoBDi2EUvR0GFlvH6kjX7wc9zF7D5SxFy5sEd8YUZntrFCOK4kefVXVITTo09YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کاپیتان‌ های پرسپولیس در فصل جدید:
حسین کنعانی زادگان، علی علیپور و اوستون اورونوف.
🔵
کاپیتان‌های‌استقلال‌درفصل‌جدید:
روزبه چشمی، صالح حردانی و امیر محمد رزاقی نیا. البته درصورت تمدید قرارداد رسمی رامین رضاییان با آبی‌ها، رامین کاپیتان دوم آبی‌پوشان در فصل جدید میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/persiana_Soccer/27098" target="_blank">📅 15:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27097">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VeqH5_2FB3Kgh7956Pna8oegWB428pR8CLOIMmpQeSPDQHjst8YDjuG7fxUFPtvbibjEsLegJmUwpHcfBgc21M0s9s9zm9mhkVa82gja3v6lCpGfoiHiru1T_2sxNgEZyapWeeIxSoXB10cT9GFW5GHJ81bvWm1GYS0QeaWZ1bmxD5RL3DvpAqx7j4nGcIxr3lIUjxdKRDfrqfInNN0l1rZcdNpN2cPN56Bwlo1cyD3BRr3lhjmqwKufxxkTeQoKPC09-ggS-TBTvF-uBbttpKrrdlt2E259dA0pw6YFcd4oizeKL54zn1bbtkx4BTS3mseHBbqZdeVO4gk7CTvQJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
👤
عبدالله‌ویسی سرمربی‌ذوب‌آهن: دوست دارم کاری که‌سال 95 بااستقلال خوزستان کردم رو با ذوب‌آهن تکرارکنم. بسیارسخته‌امانشدنی نیست. امید عالیشاه مذاکراتی‌بامدیریت‌باشگاه‌داشت اما درجریان مذاکرات نیستم. امیدوارم که قرار داد منعقد بشه و این بازیکن با تجربه رو…</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/27097" target="_blank">📅 15:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27096">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2BYtaKA4Tw8xi0ABM5tRA6KOk1ssWC-ZhOd4Sbm_H9tSxQCRedYB3V4mlSdFxQ2NnO3QVgeJCk-O4QyLn1ZFE6M0_1kjGwsvLgw_SniWJX63YaswQ8UKwVbEFZGRtNJUWI-ju9ScwlwoTNPWxuk7Z-F1GLzQyesAjkBjOlv6IBQql92mOYwzySRJbFst8O05BRiPoNybqcD1bhC6QroX6wuJ1HBu_VUTv77Nro-MVEv0SDHKRZk5zbkINROzHzVxr8T4G-mhTeGObTFY-i897ot_6aK94KkbYp7SPjyR-jh9NfMs9JZJrly1dDvZNL6nYX31luEgrq1WACyNNPTkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛مدیرعامل‌ تیم پرسپولیس امروز به حمیدرضا گرشاسبی مدیرعامل فولاد خوزستان اعلام کرده حاضر است برای خرید ابوالفضل رزاق پور 120 میلیاردتومان‌پرداخت کند. گرشاسبی به حدادی اعلام کرده تلاش خواهدکردکه مطهری رو راضی کنه تا این انتفال انجام بشه. مدیریت پرسپولیس…</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/27096" target="_blank">📅 14:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27095">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAre9YGUcGOl3iIvp1CL44QvXOk0s-E3LPNxTzi7eEvhdgk2QK-DppJtGf3u3ygwD8dGwk_P3-WV1NysfztrMcyOnRUtehXJaBFoS9qlgZMVpVoyPSDgVkyRDFAxoDHNy13-0QDmV2fo5GZOrljRcIdEg54OpGXtI70CYMDmpWjcbpCLNsfIe3pefxgXfSxBMehCJ6JHJ3SaNaaewe3m2aIS2D8wv-HW-T8Rc1jHE9zbgNOQzmz3-jRANMp27Wyp5sUas23Jd-1miWx4tC4XQgIkXh6iCB5fqx97mH0Dz93uigwHIR7Gi2iz2Eu07mrp4g_Fw0wRvJuu3OO5w7gnfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌_پرشیانا؛ آفر جدید استقلال به رامین رضاییان برای یک فصل حضور در این‌تیم 150 میلیاردتومان + 50 میلیاردتومان آپشن گل و پاس گل و قهرمانیه. رضاییان قراره ظرف 48 ساعت آینده پاسخ نهایی خود را به این آفر بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/persiana_Soccer/27095" target="_blank">📅 14:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27094">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ru94-Fw50llyhuYv5m3SuTNqhuDmu3A_5wsDMC7-gIk3SG5h1uHHgA0wvpSeD97nod5IJ3G8q-9IVheAczL9bSAeJ37co5IgK9Zotxmd0yVRocSbYpWQoK4o9TMrZ2rgQqVTfwU0EgNdzm8bYan52v6vD8qrtXvzDv8xr-h-Oemb8u4MLZgC2-PT2-s66swVJlOqkvXK3-TTWFryxRfGu2p150qkIoukBcJEqj19GLGhzX-jY7nAqUI-vGxkgsdQbcbNEoBj3Du92f6V0DUIOqpMrZvUUyyaJtUNsITKyAYgOUHMnRNMo2OvSRdHtakFRCUqrXP27P7FTGwOsMLtFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
عملکرد نیمار جونیور فوق ستاره سابق بارسا و PSG در کل دوران حرفه ایش در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/persiana_Soccer/27094" target="_blank">📅 13:43 · 13 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/jqRLReb-Sf6T5r-cVPeX-o4MqvxanT6ox0uT7__ptx-MBmPzLmQJYZYVdbH251QaI-DInTg_DnxERcYOyWyRm9lw-8_8gR8PJB0mW0N6KqspXiXYdVbEQnzIjnnMndO9qqFJn0EG0ae1SWv6s6w-sAhLuvLHX5VaYTTbAHjKYUO9YnyKSuAfJRQO3puFWrWOpNvphXwlDFez9eCuLQi4URgANsPmEKsbDA3VX-LA1lZ6dtBzwEuKeoKlLPVwRaoxh5rxBzH-NXgTDIX8yqegHaIkoocn56cG0IbDQTRKD8NjOrJ5SCnq4scN7f2twXHnitmAnerJfoT2JIqWw3q79A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.18M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-24 11:19:51</div>
<hr>

<div class="tg-post" id="msg-681343">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDjT9f9BM--hnyKdJpUx8jRw0JoOMcaLDM1LpYHjohBV6aF17oF_TwIZEXtY6wrx216h8Dwm9-2OKUwFcl0hKiNj6TzW71lEnUC2-NKxsSn442y14VcPjr1j5-4t1-_RvQ_-PEg_oaq3AIlpmLd2mnocg22mRsRWGLEMv9WumQnmnIQDSgx0AOdwKOk7MFxUVIZ04E0IuTXat7Afl_wdS0peEVCFBFcIAnXaFTtBYnvpBpRSXdi72p0mUUtuiHSeq2ta9DVMKilcwUthFfGHU5LYZKrBc_YOkSqqAmmainNs_kHZKr2UlPm5JbPb1PKHsUhZwNUQoA6kp-wt5VqXyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از هلیا و ۵ توله‌اش چه خبر؟
🔹
«هلیا»، یوزپلنگ ماده توران، پس از ماه‌ها جابه‌جایی به همراه پنج توله‌اش در محدوده توران و میاندشت، حالا وارد مرحله تازه‌ای شده است؛ آنطور که معاون محیط‌زیست طبیعی و تنوع‌زیستی سازمان حفاظت محیط‌زیست، گفته دو توله از مادر جدا شده و مستقل شده‌اند و هلیا همچنان با سه توله دیگر در این محدوده در رفت‌وآمد است./ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7 · <a href="https://t.me/akhbarefori/681343" target="_blank">📅 11:19 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681342">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61f8e5d284.mp4?token=AGi3GOVzLVS2mog3YeNXw9SdxbGw1kowl6PndabEEuXXF2q0jUFFWMe6IWv4m_KRryfdV0HXpG-Z_9QICFUS2gC_OeC8LO6geGZW6hCA6efDhnfe6rE2J9EwUvC_skdITVZr6mMm-bF16mUaXNmfy8MzH4PANGE3_z7HaIsGc_4rdNH0yrohMq7m-_MVIj2j6J3qVpPD9-1QPxtYoAVKnKi9bSiN5oohcIedj2kzPYVzs2j3r1i-MCvcF6XlvuZcyAGTcjdqRbffdeA2Vn4TQ1VmtHzLpAOVveNZX4qW4HgZk6b2eJ52POwwapA6lMvbkdHuea1XsT64uikog2qeNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61f8e5d284.mp4?token=AGi3GOVzLVS2mog3YeNXw9SdxbGw1kowl6PndabEEuXXF2q0jUFFWMe6IWv4m_KRryfdV0HXpG-Z_9QICFUS2gC_OeC8LO6geGZW6hCA6efDhnfe6rE2J9EwUvC_skdITVZr6mMm-bF16mUaXNmfy8MzH4PANGE3_z7HaIsGc_4rdNH0yrohMq7m-_MVIj2j6J3qVpPD9-1QPxtYoAVKnKi9bSiN5oohcIedj2kzPYVzs2j3r1i-MCvcF6XlvuZcyAGTcjdqRbffdeA2Vn4TQ1VmtHzLpAOVveNZX4qW4HgZk6b2eJ52POwwapA6lMvbkdHuea1XsT64uikog2qeNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی یک بوئینگ ۷۴۷ با سرعت ۹۰۰ کیلومتر بر ساعت از کنار هواپیمای شما عبور می‌کند
✈️
🔹
جالب اینکه با وجود سرعت سرسام‌آور هر دو هواپیما، به‌دلیل حرکت نسبی، هواپیمای مقابل از پنجره تقریباً آرام و شناور به نظر می‌رسد!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/akhbarefori/681342" target="_blank">📅 11:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681341">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
سقف انتقال وجه بانکی برای حساب‌های تجاری اعلام شد
🔹
بانک مرکزی در اطلاعیه‌ای سقف برخی تراکنش‌های بانکی را برای دارندگان حساب‌های تجاری اعلام کرد؛ بر این اساس، انتقال وجه حضوری از حساب تجاری بدون ارائه اسناد تا سقف دو میلیارد تومان امکان‌پذیر است و سقف انتقال وجه غیرحضوری و خرید کارتی نیز برای این حساب‌ها تعیین شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/akhbarefori/681341" target="_blank">📅 11:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681334">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aZcC7uF0OTF6vtuoTouAFgO99jD0ypM27jOZ0zEGxdPjBprkJbuS7JJutvqNGysEDzN1RVMpKKoHt9mxm7JyPH5DTpcpjcWaS4ngYp32eL0DdbLCkzAOur6T3107-G6kmFIUxHZJ4gU-5oT8qgR1PsTbRs8wIdWWaUMmcDRBHvyDk-MOg5WlZiONa3i3urJ0Ute7ZfbN90WaLSsHQQTpk74rZr_J19e_ZN6WO8j7mTd-8glY6Gq8PSkFmRkYiUs67WQxTdPKjqULbwT55yNRS40lEFkQXYPNYs0fwJ6mhjlS_NKyEnD-yfUlahmX9OP2-Eydaj4sntJPphs8_BVwAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f7dVV_KZwsmFZebBt_OsuhBI_Qd_OnL3xGArwUqcbn8O6i6CAcZ2R-czXdbYT5hwIbsLc7fhab2cNazDnAIb_E0TmhMrs9E9-t3m8gbxdWM-MLT3Voi_Jn_8T8vFIPo1hLVbzWOnLcG72Vzec08oGFMjiqPTkJEgazGWUQWTjNz7NBs1yl32idJueq_eu2rH-oxOqTPHfvvSRd2yt0Zl4qsaarTLE7zUp7K13weUj6TfxO1hQYgrOMfw1NHzFJn8HvMMQzuuCvq9EjwM0D7x3HSUo8sZPf3UJ78KusTDqNB9t12tuTCLdV8J_HipzRBvbjWsywkhThulyWP9vjO_ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BQIvmZgd-BT-jxU-Jgpbx7NStsnQj5hI2bDAvqM4nXo1nv8OoWgNvaOeeSjWuJK0NAkQT1o0uLv7Mrr_IexDnRTAd9TWFsKsgTFnUqFj9Ks7qCBMhe7GV4WYk1GerqBBf3eOhP5T58j0fWUpMxrjCqBD6kVTEUZB_e-fkcmnhbhaVvPDkhlVat9nzYWYRrwEKiY-oHeAn085NBPajjHoADv-Ibv5iwQjWH58RdtZHrjqahVY4w8UFM5538AO8_bT2EBaCvIncGJ5lKlQ-DDqKQ2BBVJqzF8KRO5ruN7dxAaI5Hx_4JHeLT4tJYg4JQW9XSsfRkxexOhPAqBLXfe6RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GD-w2vzJQW5nXKFOk9NW0wQVLGrbo3HOj6zn99n6jq2EHkjdmeSPN8lqJv4WOFn8qamerzXQLBUD7CNv6Ts4tcCoTm8i8-LmwqwqyMKeJgt8tUZLJ_kaA0dfKGFfHK502tx9AHRwByHAb3VYM-3NRnWn0sxnnPMVLipxFoBYAioCT9rKI8ONBHsbOO3T45YDTdMbzGuP1YFCFWkhCUgTcKq_cMKndbjLv6MvcUMkeqOJnk7uYNhxJOjOBF5fMrkQi14_qUuSqs9a9fRsc22ZauwvaSQN3MO5eiN1GyNvT1ybnd5MjkHr3eM8orav22a9c0lcxQ8LyWMOatk6xxaGFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k3f6s-CGOeZgPz9pSoGOH5qgoflmgzeNEmjbhmbprN7m6dVjp121pJ6Xg6UtJN4F0V8cAzhCIVX8QJ1wcVbhgpFjTPVBsbs0zOqDFr2ejXsf0GEcY-iruDa3M6vhCiSfuWNdZTYJfM8rkpYtmCJ-MLPXPQsq_x1imL3Iq0Dj0bGUlFrghlrbV67pogMKWyDcJ9z_4l43ZQsqZvOHOurLTGq1lZtYAOEG1rhlHoj9ROMtX3sC8Fd0rLivpIrXIDt5E41ALm9V0IDRZPTZnvQcp28rlpHvrLSZIe_hc5LupcGrWZcZQ8WL49Mle6zeH1j5CjbduNZjqJ4SQvSUEMzbZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bTd1w1FaVfwLx3rs546EXNuUuF__4lpCGE_QfBaUKezlCVmwKHOz-OminyAuvc3Tb7LlkyKccv-sw21LZzM7R1hjjLRmMMkPA9jb6lDKb8gBgivwB0CF5m6c0NbOOVH6bp8VAk-X5lFb1ynHYF0K4wQ0sALjwwjroisQBRxKtOycRyVkclLXkZ3PyQX54itOwNnWyxBxJHB0u6A8tu6usgSvXvALr-WyjDJU0CLkGJKDblq3DyUyH7HrcfcEwMEzeal1dp3K9-iZe3vWGITygNDf9YtYGICshtjSWr-_LnKXiys_rTe5qbiW6A6NIVqqp0o1u2G4YBAQ-wHuHxj6qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AVcP5nXkny5pVqFwqAdkvqDXMuju9Nu19FFp0v-p598UpqIY-c7V_zo1FPe5RP5Z7NQewzOZpi61pqjanRAH4UmTAsjPfRdyNXQgkyrnkVrm0rJdjZCBd1NX0bRLC9EoYEq48Vy1UAIlrlv5CJTTO65kvPFbptAVtx4oFWR2qubjtyukXOMqGC5WaejoIgxC_t8lAot-3mGS58jwdV4QbPzi7Fs54y3vj1Ld7FKWV9_le1C4L7JVpm8JDAYQAsv_nxTZKmCpknKLXfzXcva0aiV1ToyK2iy8fvZAUogEp6MwwGDGj3GGixwV-1DI3awbQeUK5CXGbI63pPgUr6FlOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شناخت رنگ‌ها با الهام از گل‌های طبیعی
🔹
در این مجموعه، طیف‌های مختلف رنگ‌ها با استفاده از گل‌های طبیعی نمایش داده شده تا تفاوت تناژها و ترکیب رنگ‌ها راحت‌تر قابل تشخیص باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/akhbarefori/681334" target="_blank">📅 11:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681326">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SR8AvE6TZA6pn20stcGTND5S24UJyAdNmhqDLh340vXwBIs4QkZ3Npq18saocyKGIUCJV-hkYsUfWJsEM7rB0C6C6rx0sBBwYzRGelM66txWp4Je1UlaHvwFIIIkg1jiIV9PozYKmgBlL95aiNYavYtFdSbHuRTPH07tWHuWoXRT45mKc8gv6Htx76YI_khzzSppHyG4X-Kb6PYR_enp2-mS6jfX3z_FCTGYm8cO9wJ5_a0vbY5bIvy6LB0VwLmThK_zBi4LrY63cpY65pftDagoeDqO0Qc_pKMnoJk0GYJz7quSkMeGNcjXuuG4rwTpT7x358g4XKzdM4KFdmvk4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایرانی‌ها جزو ۱۰ کشور پرکار جهان
🔹
مقایسه آمارهای سال ۲۰۲۴ نشان می‌دهد ایرانی‌ها به طور متوسط هفته‌ای ۴۶.۳ ساعت کار می‌کنند؛ رقمی که ایران را در میان ۱۷۰ کشور جهان در رتبه دهم قرار داده و افسانه کم‌کاری ایرانی‌ها را رد می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/akhbarefori/681326" target="_blank">📅 10:59 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681325">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2576faf18.mp4?token=fnTpceOCLSMt1kPLDFxGgO3yETXcTpMZNtnCUFuE4SdYv-lwPH4RzM_D9d61ASpT6ArhJa-l3C_DEYt2S1UK8gRZF5XMVvo4v7c7VvUng4PS8Xb2E_-nRPc6DK96m1y3sTnX8N_WOU26vuyqhlcTgrTuTMRH3Xz-TJbDe0ncdNO4vTCtYge-2_g6ntzV7ToSa_n7a2zynl07GEIRSZjBGCEeDlCa4fdsgMM_diRXxhs6TugGgfnWrUe9JAeOrCC8I7UcYcy9wttLWrqMMOlmr71T5-7hIEmsSPnKX7lBlMfdBwzHJblxD0lktt7F0LZ6p2g4foi8OvaypH-pmdbghg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2576faf18.mp4?token=fnTpceOCLSMt1kPLDFxGgO3yETXcTpMZNtnCUFuE4SdYv-lwPH4RzM_D9d61ASpT6ArhJa-l3C_DEYt2S1UK8gRZF5XMVvo4v7c7VvUng4PS8Xb2E_-nRPc6DK96m1y3sTnX8N_WOU26vuyqhlcTgrTuTMRH3Xz-TJbDe0ncdNO4vTCtYge-2_g6ntzV7ToSa_n7a2zynl07GEIRSZjBGCEeDlCa4fdsgMM_diRXxhs6TugGgfnWrUe9JAeOrCC8I7UcYcy9wttLWrqMMOlmr71T5-7hIEmsSPnKX7lBlMfdBwzHJblxD0lktt7F0LZ6p2g4foi8OvaypH-pmdbghg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری که می‌بینید از دوربینِ لباس پلیس ثبت شده؛ سریع‌ترین عملیات نجات گروگان‌ در تاریخ!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/akhbarefori/681325" target="_blank">📅 10:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681324">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_ErEPuEuvklWRlvWn_LNmEXuoN7i3SmOPz2ZIGqLPjFA0Gqsi6FLgFrWaPgILZafFm44SJZazN7nZTz_ij6g-8Eerlkdqu_9kiuUKwTmzW3QsHW4uDu8pqLGtNogie2esYllhB30WzykTtr4x0gGcH35gPZIYtYTassJrtrkzRTSJa0lXdTED8-CrkWLdJ3cDhoEFm-lEnZPWARAJ1LWhichJcWVDTHY7WH0J2DAGNJV3JhMcrK-K2l8LxLn0Uz6pYcl-q6fHIzfccb_sZpkfHDRW2dfpu3OUx6TmkgX14P3sKa0evRwIkJqkEu2YSHiccsto6UXeaRgmWZZWXSZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بی‌بی‌سی به‌دنبال احضار فرزندان ترامپ به دادگاه
🔹
بی‌بی‌سی از دادگاه فدرال آمریکا خواسته دونالد ترامپ جونیور، ایوانکا ترامپ و جرد کوشنر برای ارائه شهادت و اسناد درباره حوادث ۶ ژانویه احضار شوند.
🔹
این درخواست در پرونده شکایت ۱۰ میلیارد دلاری ترامپ علیه بی‌بی‌سی مطرح شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/681324" target="_blank">📅 10:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681323">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cm7jm8LZvhNI72CBfETl-ytxffgGytiiOWSGYa2NF39EiawFdoVpwNns2HZT4COgMbX4pnMzDtEv74R06J2ZrWQ-9dz0-1ct4XViiCbg-knfLvztoC6b2X1kD4ecJtEOD-fH3CokORCpqQaZw5eob2sbngtKViavURTF24mXk7S8VR4QlIP5tGBLxDtg3NtYEyA88pSEsqlsLZFhw8JhprSBqS2uSSEOF_QUlf7swEzN-pWhtQn5RHq6iOaiVFYWQvtGHHByiVqK9L_QbfjsdV558YPyy1vEbt2XQ97JzNIWrUQwnqv6iMrLjyAFFwwEhH02HV1qKfX5rMTU2trwRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقائی: سیاست خارجی آمریکا دچار دروغ-محوری افراطی است
🔹
اسماعیل بقائی، سخنگوی وزارت امور خارجه، امروز در پیامی در شبکه ایکس، با استناد به رمان «برادران کارامازوف» داستایوسکی، سیاست آمریکا در قبال ایران و منطقه را به‌دلیل «اتکای افراطی بر دروغ» مورد انتقاد قرار داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/681323" target="_blank">📅 10:38 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681322">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
رئیس اقلیم کردستان عراق: اقلیم کردستان نباید به منبع تهدیدی برای ایران تبدیل شود؛ ما مانع ایجاد هرگونه مشکل برای ایران از مرزهای اقلیم شده‌ایم
.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/681322" target="_blank">📅 10:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681321">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1490ef01bf.mp4?token=TQVy1CHEDoaggdgTzP78jMnssG7XzQ0RRmGOCXhZUre4iPEGhIvAwiWydtyu4hRK36vmRikexb0SPV8fVrb1DSJ8O4f6xurpQzHd15uPnz2HVtVCNLWYba1sSpjd3iKQW_ZJU7ften0h-cgmcWpaf4PyrqhQvA-wE9eyDyrthe3ZkeQX14BAAfTsN_S8PW8quCjdBeZ1eqfmwuy6DInaTmqOk7cWbYoBizuCLWr17311zVxtLUGZCctJIqZrNYlecaQaKIJcibHrh3i-GyFnX52MYJWPGVYp9ymEI-YoiIHuXae8kKGxZYW8cEEEdQ99Kfq84ne_pR7-gvnkPfKWgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1490ef01bf.mp4?token=TQVy1CHEDoaggdgTzP78jMnssG7XzQ0RRmGOCXhZUre4iPEGhIvAwiWydtyu4hRK36vmRikexb0SPV8fVrb1DSJ8O4f6xurpQzHd15uPnz2HVtVCNLWYba1sSpjd3iKQW_ZJU7ften0h-cgmcWpaf4PyrqhQvA-wE9eyDyrthe3ZkeQX14BAAfTsN_S8PW8quCjdBeZ1eqfmwuy6DInaTmqOk7cWbYoBizuCLWr17311zVxtLUGZCctJIqZrNYlecaQaKIJcibHrh3i-GyFnX52MYJWPGVYp9ymEI-YoiIHuXae8kKGxZYW8cEEEdQ99Kfq84ne_pR7-gvnkPfKWgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
قطعی برق؟ تاریکی دیگه دردسر نیست!
🔦
چراغ شارژی خورشیدی تاشو با طراحی کاربردی، مناسب برای خانه، سفر، کمپینگ و مواقع اضطراری.
✨
ویژگی‌ها:
✅
شارژ با نور خورشید و USB
✅
طراحی تاشو و کم‌جا
✅
نوردهی قوی
✅
مناسب برای قطعی برق، خودرو، ویلا و طبیعت‌گردی
🔥
قیمت قبلی: 1,598,000 تومان
❌
💰
قیمت ویژه: 1,098,000 تومان
✅
⏳
این تخفیف برای مدت محدود فعال است.
🛒
برای مشاهده مشخصات و ثبت سفارش، روی لینک زیر کلیک کنید:
👇
👇
👇
https://memarket24.ir/product/brief/47540/180124/</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/681321" target="_blank">📅 10:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681320">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f52aac7c16.mp4?token=dfuhlz3c0nGgH624BEL1z01alGsknDFdGt9dfMTzEmdt_lIvwIu6pt_-C_86GBZrEd7HWMvIrMSyFZKsgH3M0GGhfo_pkJwreYcTc2ZVRmzAFdl05-BqaDCIIW_G8HTI4r-Z8G63l3--Yr6Je88xGe6Nca0wxVZlof7TXeye2C1EPj0eWBRFPuF-BM77R8idft9x4FEXiKZZYtcm_WTpWtznY3Ofa76_BHLVlMpOvsQN4gaiiozPUw0ZcuFlOoOC1EsyxMw9_-zwaBa15HELBCp0HuePmIfZ06gqKdj_uI59Gln-OWUbNeD-xyvQ5RgEy2p1OC9NjuCuR-tQsHsfFCdH6uEA_57H-HAc_jVFZUZeW1sTRU_4154j2T199ACgTAMq68mDvUKbAO7WA8FfD5rqze0-_rUbkfi8Eukx9BrE2v7ojqywtdoXL9VHYzedM1cUyTFazySuzCn5CK-2R83IOw5j3elrVIONGE1IHpQ2SNw-GJWfTFEOyghJKwQj70TdMiM_vJVgnIBZHf6oRhj73f-fzTnxmaseAKniCRGKRgv5vHdns4l5yyz1t5o6W00Vp8a7eZmoZMhXGt0PlV089HfN5Ru673MzP5dK6UbJSEQNi4M0FLkIPgQ8ESpJklF6WOhItHD4ZmsDACu7mLLEMSpv9tpUBeDAaULL6lY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f52aac7c16.mp4?token=dfuhlz3c0nGgH624BEL1z01alGsknDFdGt9dfMTzEmdt_lIvwIu6pt_-C_86GBZrEd7HWMvIrMSyFZKsgH3M0GGhfo_pkJwreYcTc2ZVRmzAFdl05-BqaDCIIW_G8HTI4r-Z8G63l3--Yr6Je88xGe6Nca0wxVZlof7TXeye2C1EPj0eWBRFPuF-BM77R8idft9x4FEXiKZZYtcm_WTpWtznY3Ofa76_BHLVlMpOvsQN4gaiiozPUw0ZcuFlOoOC1EsyxMw9_-zwaBa15HELBCp0HuePmIfZ06gqKdj_uI59Gln-OWUbNeD-xyvQ5RgEy2p1OC9NjuCuR-tQsHsfFCdH6uEA_57H-HAc_jVFZUZeW1sTRU_4154j2T199ACgTAMq68mDvUKbAO7WA8FfD5rqze0-_rUbkfi8Eukx9BrE2v7ojqywtdoXL9VHYzedM1cUyTFazySuzCn5CK-2R83IOw5j3elrVIONGE1IHpQ2SNw-GJWfTFEOyghJKwQj70TdMiM_vJVgnIBZHf6oRhj73f-fzTnxmaseAKniCRGKRgv5vHdns4l5yyz1t5o6W00Vp8a7eZmoZMhXGt0PlV089HfN5Ru673MzP5dK6UbJSEQNi4M0FLkIPgQ8ESpJklF6WOhItHD4ZmsDACu7mLLEMSpv9tpUBeDAaULL6lY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش تند آماندا رز، نویسنده استرالیایی به توصیف «دیکتاتوری» برای نظام ایران: دیکتاتور کسی است که ۱۶۰ کودک را به کام مرگ می‌فرستد
!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/681320" target="_blank">📅 10:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681319">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d09a61bf62.mp4?token=CCy5AGRx4sS1ZN_eIQpfKZtSecp7F68vX4lVLWkBHRsoM7g9GQi3c9BWiUsD1EHVwaudJDZD4ie6ZwwwauwcQOfvM9ZhrAgaMuf_U2KMveN0b2_BwDZvUl2i2WatslANvjKki4AD7KTGT47F7WFezagebSENun3myjPe70VCWWEuquzl7hyyjC34jJpzOSsllZFARHoiTEtbt6HiACcUuhu2YcvBX8Ax-hoEfJh_R05UxQMj9E5IGEwumXcvGShfTwuY_4VBdXZNhDhkFwukc5c2ixarc-0uHJHTJ1jAm9NvEk5rWzEOtgH62dU_l3j9blc7aTknx_juB1TnuixaCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d09a61bf62.mp4?token=CCy5AGRx4sS1ZN_eIQpfKZtSecp7F68vX4lVLWkBHRsoM7g9GQi3c9BWiUsD1EHVwaudJDZD4ie6ZwwwauwcQOfvM9ZhrAgaMuf_U2KMveN0b2_BwDZvUl2i2WatslANvjKki4AD7KTGT47F7WFezagebSENun3myjPe70VCWWEuquzl7hyyjC34jJpzOSsllZFARHoiTEtbt6HiACcUuhu2YcvBX8Ax-hoEfJh_R05UxQMj9E5IGEwumXcvGShfTwuY_4VBdXZNhDhkFwukc5c2ixarc-0uHJHTJ1jAm9NvEk5rWzEOtgH62dU_l3j9blc7aTknx_juB1TnuixaCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیوی عجیب از یک دندانپزشک با کلکسیون ۲۰۰۰ دندانی در شبکه‌های اجتماعی
🔹
این فرد طی ۸ سال فعالیت حرفه‌ای، نزدیک به ۲۰۰۰ دندان کشیده‌شده را جمع‌آوری کرده است که هر بار دندان‌ها را شسته و آنها را سرجایشان می‌گذارد؛ رفتاری که ظاهراً برایش لذت‌بخش است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/681319" target="_blank">📅 10:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681318">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/932e334a2e.mp4?token=YeCmthXY2a4hufU70iNqpxPyI6_AsL9KkWbC3MeI_Rv7GZGgDCZCNZHsh5JXYS38T-pk2Wh5mmBHBoutxHjRgA-ciucjBLu9NgLdvbr9QIjH-nuvYTber-KVgvyxQO-h4zXPfxiat8nKFe2e1h3ctLolbGJL--M0UMxHYVFMgG5BxFv_WoiChdUf7Ub4ISbEDQACiG4e-Jha-DLtAaG7Ks3riD_uDwW9lTWYj1PPLvlcT9bfzDP6UDA6OLSVB2kaVIPdh77ri1K-stKm3BxHAyDV8yvYrdGZ8penEoVJxGVPrl17XMZ0Cb8GkNTXV8E_lL4d-Iu9L-Lh8sZCo8cxIoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/932e334a2e.mp4?token=YeCmthXY2a4hufU70iNqpxPyI6_AsL9KkWbC3MeI_Rv7GZGgDCZCNZHsh5JXYS38T-pk2Wh5mmBHBoutxHjRgA-ciucjBLu9NgLdvbr9QIjH-nuvYTber-KVgvyxQO-h4zXPfxiat8nKFe2e1h3ctLolbGJL--M0UMxHYVFMgG5BxFv_WoiChdUf7Ub4ISbEDQACiG4e-Jha-DLtAaG7Ks3riD_uDwW9lTWYj1PPLvlcT9bfzDP6UDA6OLSVB2kaVIPdh77ri1K-stKm3BxHAyDV8yvYrdGZ8penEoVJxGVPrl17XMZ0Cb8GkNTXV8E_lL4d-Iu9L-Lh8sZCo8cxIoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرگزاری فرانسه: تعداد کشته‌های زلزلهٔ ۷.۷ ریشتری اندونزی به ۲۰ نفر افزایش یافته است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/681318" target="_blank">📅 10:19 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681317">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
حاجی‌بابایی: مجلس می‌تواند با رعایت پروتکل‌ها حضوری شود.
🔹
هواشناسی: اهواز با دمای ۵۱ درجه سانتیگراد طی دو روز آینده گرم‌ترین مرکز استان کشور خواهد بود.
🔹
سپاه اصفهان: احتمال شنیده‌شدن صدای انفجار کنترل‌شده در صفه، بهارستان و اطراف آن تا ساعت ۱۴ امروز وجود دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/681317" target="_blank">📅 10:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681316">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8789f7e651.mp4?token=J_biXwAlhBO0Fg_xl2CwTCgoJUmC68QkmGCGFYItGvKKX7k00TlJciIoNWOOUCdy-cj5xBFBQRG4whe8oSjCd0dLsLCudjhLLqYkmQ-bO7hZliHJnwtZlFpMRI1hF3TPDfyWsFDoeO9_oMjk_3OIj5yfi08P67MD9CboOcGgbT2pazfSv-Qp5waX7ekfABIYmd9PqT-cnw8t0x_0PlPXmASIWLY0RPWulUIc4F6wKbOyeLaZPXBGHfvN7WKXls-HtloF2snEGJDeoEPnS78a_ddL_iCwI2YAZDhtwH0OjJBflM-gZESVGoKopy3XewgEXq9l23R8KoIHNBvTRVezbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8789f7e651.mp4?token=J_biXwAlhBO0Fg_xl2CwTCgoJUmC68QkmGCGFYItGvKKX7k00TlJciIoNWOOUCdy-cj5xBFBQRG4whe8oSjCd0dLsLCudjhLLqYkmQ-bO7hZliHJnwtZlFpMRI1hF3TPDfyWsFDoeO9_oMjk_3OIj5yfi08P67MD9CboOcGgbT2pazfSv-Qp5waX7ekfABIYmd9PqT-cnw8t0x_0PlPXmASIWLY0RPWulUIc4F6wKbOyeLaZPXBGHfvN7WKXls-HtloF2snEGJDeoEPnS78a_ddL_iCwI2YAZDhtwH0OjJBflM-gZESVGoKopy3XewgEXq9l23R8KoIHNBvTRVezbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: در آخرین حمله به ضاحیه مذاکرات را متوقف کردم
رئیس مجلس:
🔹
در آخرین حمله‌ای که به ضاحیه شد، مذاکرات را متوقف کردم و اعلام کردم امشب رژیم را خواهیم زد و اگر رژیم پاسخ دهد، کل منطقه را می‌زنیم. نتیجه این شد که همان شب محاصره را برداشتند؛ در حالی که قرار بود طبق تفاهم، ۳۰ روزه باز شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/681316" target="_blank">📅 10:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681315">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
پیامدهای مصرف «گل»؛ از اختلال حافظه تا وابستگی شدید
وزارت بهداشت
:
🔹
مصرف گل نه تنها از منظر علمی اعتیادزا قلمداد می‌شود، بلکه می‌تواند آسیب‌های جدی برای تمرکز و حافظه مصرف‌کنندگان به ارمغان بیاورد.
🔹
مصرف موادمخدر می‌تواند از نظر فکری و جسمی وابستگی ایجاد کند؛ به نحوی که وابستگی آزاردهنده‌ای به مصرف یک ماده مخدر پیدا کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/681315" target="_blank">📅 10:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681314">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9677aba05.mp4?token=SQEy6pJvtsdNoYLfjXmmi7sLtsJAWY-jQ-AqJB5YmTSyLkovWM9mxwEyJCRiRXrBP-08MHRcvM1Cs446h3YBw4_FOEi67F7JSzl4ggPh7ijwIeOTCTHX4C_8NRwwtfPqBwOh3COoPW94RUfrcHmQlXCjj_YSKYSzJnOVpgAS4jYGCyiP0Fa3RKU3jpSWlplwH50Wv1XKaVIw_I2NR5y0AMSTnjP4XLSpyxcmUCepRRYZGgsF9ht3IFYq081yoSVd5STyXehfoTvJUQoJeDE_ZEXFhInjkHjp7UshzG52KqGge21y_1xMlmkLBcgjg-bcrn1vQyoX1zD8eNQSMzBsHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9677aba05.mp4?token=SQEy6pJvtsdNoYLfjXmmi7sLtsJAWY-jQ-AqJB5YmTSyLkovWM9mxwEyJCRiRXrBP-08MHRcvM1Cs446h3YBw4_FOEi67F7JSzl4ggPh7ijwIeOTCTHX4C_8NRwwtfPqBwOh3COoPW94RUfrcHmQlXCjj_YSKYSzJnOVpgAS4jYGCyiP0Fa3RKU3jpSWlplwH50Wv1XKaVIw_I2NR5y0AMSTnjP4XLSpyxcmUCepRRYZGgsF9ht3IFYq081yoSVd5STyXehfoTvJUQoJeDE_ZEXFhInjkHjp7UshzG52KqGge21y_1xMlmkLBcgjg-bcrn1vQyoX1zD8eNQSMzBsHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این رسپی یک شام ترد و خوشمزه اما اقتصادی درست کن
😋
مواد لازم:
🔹
سیب‌زمینی نیم کیلو
🔹
پیاز ۱۵۰ گرم
🔹
پودر سوخاری ۱ لیوان
🔹
سیر
🔹
ادویه: نمک و فلفل و زردچوبه و پودر سیر #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/681314" target="_blank">📅 10:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681313">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d26c33deac.mp4?token=RLNRDcRdRYqhxvcwo-cbS-QALgaCFG5FVu9uYZ_i8YU2SEDZa0VlxYfSLDX-iCqg1gZV07LAfFu8uPkdzKXrQ-ohdggC59xGOKMXUcouYqJGnh7C9bf6j6NpgKe_UXHl4xwRpVA1CSwuJH2Cquq7dMWBDCbZ3VAaZrgm0p5FgKLH1jY611TlOCt7WD9pDQ2eYC-4hhyVZcBA6nN9FKdPJuA1J2Ywya7xhlTpKPrz5eiZu6lNBv7fAvk_baNx0W0pD494QcC18QGeLJEav9yazsJG7QprFf-OMhJDrEmxHTaCG1DAzFJuK73ADo6x8A_gMnU16TjzXiu3xH5hlA8O9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d26c33deac.mp4?token=RLNRDcRdRYqhxvcwo-cbS-QALgaCFG5FVu9uYZ_i8YU2SEDZa0VlxYfSLDX-iCqg1gZV07LAfFu8uPkdzKXrQ-ohdggC59xGOKMXUcouYqJGnh7C9bf6j6NpgKe_UXHl4xwRpVA1CSwuJH2Cquq7dMWBDCbZ3VAaZrgm0p5FgKLH1jY611TlOCt7WD9pDQ2eYC-4hhyVZcBA6nN9FKdPJuA1J2Ywya7xhlTpKPrz5eiZu6lNBv7fAvk_baNx0W0pD494QcC18QGeLJEav9yazsJG7QprFf-OMhJDrEmxHTaCG1DAzFJuK73ADo6x8A_gMnU16TjzXiu3xH5hlA8O9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دریاچهٔ ارومیه از قاب آسمان
#اخبار_آذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharb</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/681313" target="_blank">📅 09:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681312">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fbo7BKolEROsf9imTVuWUNp82OKpXIM6Xl09KcGcdEVIuNH5UoS5fELUCO4BQdyfXKpEkHlQ7xRVz49XEGMee6JU9FMGZZsomnl212CkFOUUGmas6Z_23lPjpWA3SH6bVvZgwzpg-918Ed7_-wcnLBHL62c-WtHNK2l0uokosrvQiDvLHi3uyKDT5jre3ZEVLNiaiMT-CV5aj0R64i0iY6OxHQT390YUWuXR9L-U6Z29Pb6X3bKFxSeGnrycnPwCeVTPlMMZSjAgx_jAdDaJOYgc-Al5Jg4FXlEsAYpEJr4euR1YzDFXrJZRb5Mo55x4gzLXiqqP65tZLQvifgiaqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی کاخ سفید برکنار شد
🔹
دونالد ترامپ، رئیس دولت تروریستی آمریکا در اطلاعیه‌ای رسمی از برکنار کردن «کارولین لِویت»، سخنگوی کاخ سفید، در پایان ماه اوت میلادی خبر داد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/681312" target="_blank">📅 09:50 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681311">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ARgKc0V7QuSserxJKBjZ9a-Kb467TRGStI0q4au2MBn7_EqmNA11OaEAyv95qkWtiC8BpWacEkoY5VZly9RSddagMYrZzKC8977jodGj4m9CZgGhB5i6qhWVvFR6bgIJwAjleA5jTuau2uwH9J7pLAXAUXSKLHv54nyELVUyOnky-wXldylM9I_hPn1PLHBVlB4AphQYJR4LzKQUU2Q39BYBQJ_tmaS679krd5iJm_pNK48lqPJm8yigkTJZfYRYyibxVuh7ONNsRZuKauvYjoE-ma3gEhk6eREkogG0egPvZb4Rr6nFVs1-Rfpt1zdGDXUDfdgfN1c6Rk_2bqaIrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کنایه مجری آمریکایی به ترامپ: بنزین آن‌قدر ارزان می‌شود که پمپ‌بنزین‌ها به مردم پول هم می‌دهند!
مجری طنز‌پرداز آمریکایی:
🔹
منابع داخلی کاخ سفید فاش کرده‌اند که پس از شکست دادن ایران برای ۴۴۳مین بار، ترامپ قرار است قیمت بنزین را آن‌قدر پایین اعلام کند که پمپ‌بنزین‌ها واقعاً به شما پول بدهند تا بنزین را از دستشان بردارید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/681311" target="_blank">📅 09:46 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681310">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
حادثه دریایی در نزدیکی تنگه هرمز
🔹
گزارش‌های رسانه‌ای از وقوع حادثه دریایی در نزدیکی تنگه هرمز خبر می‌دهند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/681310" target="_blank">📅 09:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681309">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فرماندار کنارک از انجام عملیات خنثی‌سازی مهمات عمل‌نشده در محدوده نظامی کنارک خبر داد.
🔹
رئیس انجمن غلات کشور: گندم مورد نیاز نانوایی‌ها تا پایان سال تأمین است.
🔹
طالبان: همه افغان‌ها می‌توانند به افغانستان بازگردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/681309" target="_blank">📅 09:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681308">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/077593b529.mp4?token=vgtBfJNvFrVr96bIvpkIVoGdrOJgZD3mXZq8BZMrZbZTxyD2AxCb4xlPKmhz7cWbWEC8wXpROkp39amz-I542vnVloLfQ2w_4V76zPMqmIzVdcp_l7nGOXAF1IjNYp8YiYOxDmHCRL7bcohgc1v2AHboD4HJXy1jvM13E9xNfCcpNqiNmoHQPaK494R-S2obE8rvSbHUlsP8g7Eg3uYPC85tsihTtITKPSTjycT3cTLBi8pYyH6QQj7jO9oKMpz4axtFV-l2VEADt1hj9P5qVVLFYoFipJM9dBhPcqqabYbsiBX7RFKiZLHIhiW2vHk11SSE2ZI3KlANAz-_FI8VyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/077593b529.mp4?token=vgtBfJNvFrVr96bIvpkIVoGdrOJgZD3mXZq8BZMrZbZTxyD2AxCb4xlPKmhz7cWbWEC8wXpROkp39amz-I542vnVloLfQ2w_4V76zPMqmIzVdcp_l7nGOXAF1IjNYp8YiYOxDmHCRL7bcohgc1v2AHboD4HJXy1jvM13E9xNfCcpNqiNmoHQPaK494R-S2obE8rvSbHUlsP8g7Eg3uYPC85tsihTtITKPSTjycT3cTLBi8pYyH6QQj7jO9oKMpz4axtFV-l2VEADt1hj9P5qVVLFYoFipJM9dBhPcqqabYbsiBX7RFKiZLHIhiW2vHk11SSE2ZI3KlANAz-_FI8VyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر تکان‌دهنده از نجات‌یافتگان زلزله کلمبیا
🔹
تصاویر منتشرشده، افرادی را نشان می‌دهد که پس از زلزله شدید ۷.۴ ریشتری کلمبیا، زیر آوار ساختمان‌های چندطبقه گرفتار شده بودند و زنده بیرون آمدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/681308" target="_blank">📅 09:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681307">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
حادثه دریایی در نزدیکی تنگه هرمز
🔹
گزارش‌های رسانه‌ای از وقوع حادثه دریایی در نزدیکی تنگه هرمز خبر می‌دهند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/681307" target="_blank">📅 09:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681306">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJV0JWVaWIhG82YfpLWfmk8fOzY8pKyqR4gnbzJIgIrKzd6h_vO00uZkXeJ7qhWlNTMdNXFW_uD2DfwrnnXwlnjsNPxEhBJgFcn9uO0qLnTVPy2sS1BmBA5_OdO_LEeyjvg2KjprO98w8Iq0hmtcmHRz16ckeymciMwsKbF4ygspcnlePvlADdfqygc54ny2W4kQg48MUknzTNNp086TJq5i2gOB8N4WEZGgsHBFvSUiafbvPEQBzQWGtXtrQgRGx2TYi0V2JYPFhsq1BVRPzzSw_I5bfdnThkgCPJjX0aNFbiYWkAUHTCysAc9h-1carOuDieuPDbmAm6X8Ad7HqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اگر ترامپ کاپیتان تایتانیک بود...
ران فیلیپکوفسکی، دادستان سابق ایالتی و فدرال و تحلیل‌گر سیاسی آمریکایی:
🔹
اگر ترامپ کاپیتان تایتانیک بود، نه‌تنها خودش اولین نفری بود که سوار قایق نجات می‌شد، بلکه درست قبل از ترک کشتی به مسافران اعلام می‌کرد که همه‌چیز کاملاً روبه‌راهه! “همه‌چیز خوبه، دوستان. من بهترین کاپیتان تاریخم. دقیقا می‌دونم دارم چه کار می‌کنم.”
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/681306" target="_blank">📅 09:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681305">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
۲۴ میلیون زائر در اربعین؛ رکوردی از حضور میلیونی مردم  معاون مراسم و استانهای شورای هماهنگی تبلیغات اسلامی:
🔹
در پیاده روی امام رضا ۴ میلیون و در پیاده روی اربعن بیش از ۲۴ میلیون نفر و راهپیمایی جاماندگان حدود ۷.۵ میلیون نفر شرکت کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/681305" target="_blank">📅 09:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681304">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6592e5d285.mp4?token=vZ68af11fS2UUZeRSUFAFcQh96mU020E_emllfIork7zBmr9EY7bvZVMV138Kqohc6V4MfFAJPhdQePkZwdZJm_qhrIMFx8yOwXiq3no2t5FXvS1WU6aQ7Tmv9Z5CjSUt5JlxJn3Tmqa0fSk-XRwv68z5J746czp0l683kiXGJu9zXUZ-rtdwO_4C74jHnwIwcq0zyN9rAEj36Y07qoA9zDll8ExAce7U5edVGTN5PYfOtKOQ0DQ4PfuccEH4-rRB7qjvZZMIpKGME37yoZI8eIhgjF34qvHRxvcNOkgPECeDcfYy58IpyMVob8AAnkO8i-LEQKwhrijaN-FcliDow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6592e5d285.mp4?token=vZ68af11fS2UUZeRSUFAFcQh96mU020E_emllfIork7zBmr9EY7bvZVMV138Kqohc6V4MfFAJPhdQePkZwdZJm_qhrIMFx8yOwXiq3no2t5FXvS1WU6aQ7Tmv9Z5CjSUt5JlxJn3Tmqa0fSk-XRwv68z5J746czp0l683kiXGJu9zXUZ-rtdwO_4C74jHnwIwcq0zyN9rAEj36Y07qoA9zDll8ExAce7U5edVGTN5PYfOtKOQ0DQ4PfuccEH4-rRB7qjvZZMIpKGME37yoZI8eIhgjF34qvHRxvcNOkgPECeDcfYy58IpyMVob8AAnkO8i-LEQKwhrijaN-FcliDow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی قطار از میان آب‌های سد سپیدرود عبور می‌کند؛ یکی از تماشایی‌ترین مسیرهای ریلی شمال
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/681304" target="_blank">📅 09:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681303">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c81e014932.mp4?token=bpY2x-2h_TCXdCirLtTxKuVtQzu2awKV6f_4y3jXPhf65gfaxd4aoCWtUXDgrDMa9jlagoRtgqgaJqMfKSMRDAK4KcsohQKFK24rkgM9-xEBzE-lvhb8FNa0kwgmCzjn2LCb6fFAsgYi3f5TewzRhogCC78rIGBrp4m3menWsx3zYeTulGq7k49pwQytaFPQvsO0kwoK9OPJfzdDQmHhbvpVpk2Idl7BZKfhEYCW-voBVNthToQGDnA3VdJmE5o03woV0xiBGAG_xbISusMKOGrQb1ceeNfXrzFzJyIuEGb69YpY0Qcoo3tdX6eOn1WqlCTo4whRIG0c0demqr4HUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c81e014932.mp4?token=bpY2x-2h_TCXdCirLtTxKuVtQzu2awKV6f_4y3jXPhf65gfaxd4aoCWtUXDgrDMa9jlagoRtgqgaJqMfKSMRDAK4KcsohQKFK24rkgM9-xEBzE-lvhb8FNa0kwgmCzjn2LCb6fFAsgYi3f5TewzRhogCC78rIGBrp4m3menWsx3zYeTulGq7k49pwQytaFPQvsO0kwoK9OPJfzdDQmHhbvpVpk2Idl7BZKfhEYCW-voBVNthToQGDnA3VdJmE5o03woV0xiBGAG_xbISusMKOGrQb1ceeNfXrzFzJyIuEGb69YpY0Qcoo3tdX6eOn1WqlCTo4whRIG0c0demqr4HUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خیانت، مثل سوختگیِ دست است؛ زخم خوب می‌شود، اما جای آن همیشه می‌ماند و هر بار که می‌بینی‌اش، گذشته را یادت می‌آورد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/681303" target="_blank">📅 09:09 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681302">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JetnSbm5A-vMpSUxAnkprDOgBc4Y3nU-bQbF9H-xtZvm5h9CtZoboyQYQKl0vP5nXFhLe32scfRsFUNXINiCXxA6oLq7P5Vz9OfPx3qYCNRikjf_cRLj3dP1ylEWbZfD9pZKh1kmNLJR5VWaB3N8V9ibsBoZkPVHa7gEX92ljlYfWwqqAUf4w7hVNLA1cQGJ5d3TNiHHPisCEqX779hRI4GeCONTF2ndELNAc5xJJw8dBp5MftpQsfclRYBiuUMiGVHB6aHr450SYyQsin2HQaUQbr5gjheSK9t7wf2q6l0pVFUKxF3NWk5LjRR0dxlhbGzTA_i-MNG5BwhqKLf2zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرلشکر وحیدی: رزمندگان اسلام مسلح ترین ارتش تاریخ جهان را به زانو در آوردند
سرلشکر وحیدی در پیامی با قدردانی از ۶ ماه جهاد رزمندگان اسلام:
🔹
شما با عملیات موفق آفندی و پدافندی زیر آتش سنگین، مسلح‌ترین ارتش تاریخ جهان را به زانو در آوردید.
🔹
صحنه نبرد با مدیریت مبتکرانه و تحت فرماندهی حکیمانه آیت‌الله سیدمجتبی خامنه‌ای، دروازه‌های قیام را بر روی مستضعفان جهان گشود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/681302" target="_blank">📅 09:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681300">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
۲۴ میلیون زائر در اربعین؛ رکوردی از حضور میلیونی مردم
معاون مراسم و استانهای شورای هماهنگی تبلیغات اسلامی:
🔹
در پیاده روی امام رضا ۴ میلیون و در پیاده روی اربعن بیش از ۲۴ میلیون نفر و راهپیمایی جاماندگان حدود ۷.۵ میلیون نفر شرکت کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/681300" target="_blank">📅 08:50 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681299">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyypkCTWgwxBwFBytHahSLHcdUs-Nt7q1KQ9u4nf2R8Z-5XdWlCYRlGkKDx7RYxTZeLcQS2ddpAyt14oZ7qw--RtxO9Isial5QbGDZGrzJB73a4PeNuT34CYkwwwLR0jkB9ZLorf5ZbqdMjLWXXo5qBJPhjQaC504MvyAalJM_-Mr8kXMvzGtOtLyjpL37rvRn8MdPn1tIThK5CRhJWnFlEP00tQsQOtNxjbebh4rQ9sjL_7Bphmky14x_k64S9i1G6h_mZCmJgmy8o1oXbtQ-2FxHqV1QqtwA3xGToVmpjNRnCM9LLG_rzUbOYeUvmBiO3nKSRygMLjIpoBg198LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قهوه؛ نوشیدنی محبوبی که می‌تواند پیری مغز را تا ۶ سال عقب بیندازد!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/681299" target="_blank">📅 08:48 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681298">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0rk8UFyUe1zqzPd32DI6tKVEbytwg4i1eDRmwOXvpxNt8hRObJRbaAE9w9SU3zt7WZ9dqU9r9ANMQr8BePvlDikIwV2YhZ7cyPTyRFq6b6LshNHmowMc0kWzz0ZGaq8U-0_DEQgVyqutvsk2WfiuzA41YvxpHhhjjCe-6aSB3AlJ_uAuUFjac9vxW1pSoDHkMt2FlY9qOxGjLrLjxx3KumSP4PDpVss1pVC19tRFRVCSyy0p1CT7AJWRQpnFd5Ah-NWkxbf4Xk6S9DqTxAHxOpnDHOa9DyqjtdmQvOX6BttlCfKFV5sRW_AhvIKLdsyjOdJ6c5xqF3FmtCzS-s-nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز انتخاب واحد نیمسال اول سال تحصیلی ۱۴۰۶- ۱۴۰۵ دانشگاه آزاد اسلامی از امروز
🔹
براساس برنامه زمان‌بندی شده، دانشجویان برای انتخاب واحد از امروز تا ۲ شهریور به سامانه آموزشیار مراجعه کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/681298" target="_blank">📅 08:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681297">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
هواشناسی: موج گرما در بیشتر استان‌ها حاکم است و تا اواسط هفته ادامه دارد/ دمای ۴۸ تا ۵۰ درجه و بالاتر در شهرهایی مثل اهواز، مهران، برازجان و فراشبند دور از انتظار نیست
🔹
دمای ۳۹ درجه برای تهران پیش بینی می شود که برای پایتخت رکورد محسوب خواهد شد.
🔹
امروز بعدازظهر در شمال هرمزگان و جنوب کرمان رگبارهای سیل آسا داریم. عشایر و کوهنوردان از صعود به ارتفاعات خودداری کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/681297" target="_blank">📅 08:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681296">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
مقام کاخ سفید: می‌دانیم که برای مؤثر بودن توافق، باید موافقت همگان را در ایران جلب کنیم
ادعای پولیتیکو به نقل از یک مقام کاخ سفید:
🔹
جناح‌های درون ایران گاهی اوقات تفاوت اساسی با یکدیگر دارند و توافق با یکی از آن‌ها به معنای موافقت بقیه نیست.
🔹
ایرانی‌ها موضع ما را می‌دانند اما ما گاهی موضع آن‌ها را نمی‌دانیم و آن‌ها همچنان شرایط را تغییر می‌دهند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/681296" target="_blank">📅 08:20 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681295">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nEio40zQgSRazJzR7GjMVEPOUpuFl0dNtW8RKFGAvDCt0oM7zhWBU4hYazS3X1rvxMl0jnX5-m3LMU9LFEthLKD0T407tqp0yurVu-nPYhgbWrue86YlAnHQfHxUNweLnD2Y6ErCX5e7AuOLhSM3yfQAKTwNE6pzAk6vb8fyj7g96FRAsxjyx7w5ShfSS619C2-F64DtW-WnOxntmeFR_mAnOpKy3286e-TN5ufLZYSRLt-9yCiqV9waL4nDKAxs9vf6a2ckbR7TWt7oWLLUXU99C-6ISkTDMhPCj_rbiiNChRnWK441H41J6ReQ4b7O4Ztv6-oWWZK4k0Jr3pGqVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کابوس اپستین ترامپ و دارودسته‌اش را رها نمی‌کند
🔹
قاضی فدرال، وزارت دادگستری آمریکا را ملزم به توضیح درباره حذف و سانسور بخش‌هایی از اسناد پرونده جفری اپستین کرد؛ به‌ویژه بخش‌هایی که به ادعاهای علیه دونالد ترامپ مربوط می‌شود. این پرونده همچنان به کابوسی…</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/681295" target="_blank">📅 08:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681293">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b4hAlXWR8qvw9UgXyx_KvxQ-nb4tyV2VC0Szv2XnNbrfcFG7jOvj0SGMV0OWJ5OBlssU1De_ccHmvVQDOA1smiYnzUIbsAUz_JG0LbcVVgMo2IrlJqQH_zxT-NiQufpMo11BYkbizrwOL41R1zhbqbwa4Yd-T6lukjnf9nLIw6kIKBbLZsa-ASoKcMqWp4Gyj9T1zGxM5sJPCceZj8lZHPQhDcuZnRoy_WJS60zA4ObZofcdTm8LgCusgIXy1cfBTz6USlrfeUBOasP38ttTDCjwGrosoywI2qi5eE33e2oSvx_xl5d5ZfXN17kxr7klcvv4MrHNLjWwhz86zwju7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cDphE7fO9AT4xk6c4wx7KQt5ber3Xqp0nj9I956nd8PzijDlus6t-OcR8-zavT3zC4qqBByJFomnEgD1LXI-jRsvBIgl7OZ2CY2U44VU7P0XWDk_v0ftJdyfwp6Ev14_esqiycnqVdQsbj6LAybVKkxeitSjliZtLTzt8dWyTJfUiVQAlIYx-VBVssdKZqDoM6AwGehjxU-QqoJ3uQvME3N16kqgNfg5fvCL42-EZ1ylDtCeKL1EsT8JvQd1VECo8ZBlq7awMrDKbVFCtJs_OXQswvyVjhVC1Ui_v5QkPIW9hwnI2_gCc-t6Ck3o1SwYOQyVy3AEuwLQY_eAXzDjAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
عکس عجیبی که ۱۱ سال قبل از آشنایی، آینده یک زوج را لو داد!
🔹
این زوج چینی بعد از سال‌ها فهمیدند در سال ۲۰۰۰، بدون اینکه همدیگر را بشناسند، به‌طور اتفاقی در یک عکس کنار هم افتاده‌اند؛ ۱۱ سال پیش از آشنایی‌شان!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/681293" target="_blank">📅 08:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681292">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c0010c262.mp4?token=uUA26tGz71etCmDhzFJdkMsM0B6LJIOWKmZVbqp_vb_u78l_JTDcBCSs4EZvwReHpKAmNfx9RfY67T-6yTvp5ltxPjE8f9FVAhyOvsWxKcUybrD922ZQLBxdO7B9GbDBkcNhvRqulcYDxQR8R1xlkJZ63GMh2iuGRtgA517DstOhYJBmwq6XMepXB_k3vuFapsQsEhdVbPNCkW7H39ZaZe77vRFUp6hon5vMM3DZJknbiIQW12Qy771op97d2w7qAI0ITB6s2J88hvNEo-p-YtRueL3R5nRZesnTekPSrXkAN24t4BYOxSWTvGAB-u_zC8RBJepV3OdO4lVuJ3clojzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c0010c262.mp4?token=uUA26tGz71etCmDhzFJdkMsM0B6LJIOWKmZVbqp_vb_u78l_JTDcBCSs4EZvwReHpKAmNfx9RfY67T-6yTvp5ltxPjE8f9FVAhyOvsWxKcUybrD922ZQLBxdO7B9GbDBkcNhvRqulcYDxQR8R1xlkJZ63GMh2iuGRtgA517DstOhYJBmwq6XMepXB_k3vuFapsQsEhdVbPNCkW7H39ZaZe77vRFUp6hon5vMM3DZJknbiIQW12Qy771op97d2w7qAI0ITB6s2J88hvNEo-p-YtRueL3R5nRZesnTekPSrXkAN24t4BYOxSWTvGAB-u_zC8RBJepV3OdO4lVuJ3clojzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر زانو درد دارید، این ویدیو رو ببینید
👌
🔹
این حرکت رو روزی ۳ ست ۱۰ تایی انجام بدید تا درد زانوتون رفع بشه #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/681292" target="_blank">📅 08:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681289">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e3fc8b242.mp4?token=Hm2PsIl8_yw6Gz2M0XQTSFBmIuWcCPf4czmodByS-CsWKuSb8dWdvlN8Vs4OwQEHgR9_jsua_p21mMe3PutFRT8vxsLVH-Fw24Mt1EKh02NKtQsLRyDsbTlXCWZz2OWbvUY4XTSHkDVSgTPDTUcgQNFcb10aXt8jzof9r5aICsWKqc0fwFn2JaV2eDxak_DGyco7H3ILCTj-h8s1--ft0snWrU2FqfO0hjw8q1vtVbksD1p1DOh2z3UT08HJ1piIz3x-8Gf9iKKfye_1FpwRNMmAHchQ1jao0a6ICYTiNaptDiH1HfXOtkvlsdTbEzjI7Vd7Hr4PPoG1fbcFPbZFaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e3fc8b242.mp4?token=Hm2PsIl8_yw6Gz2M0XQTSFBmIuWcCPf4czmodByS-CsWKuSb8dWdvlN8Vs4OwQEHgR9_jsua_p21mMe3PutFRT8vxsLVH-Fw24Mt1EKh02NKtQsLRyDsbTlXCWZz2OWbvUY4XTSHkDVSgTPDTUcgQNFcb10aXt8jzof9r5aICsWKqc0fwFn2JaV2eDxak_DGyco7H3ILCTj-h8s1--ft0snWrU2FqfO0hjw8q1vtVbksD1p1DOh2z3UT08HJ1piIz3x-8Gf9iKKfye_1FpwRNMmAHchQ1jao0a6ICYTiNaptDiH1HfXOtkvlsdTbEzjI7Vd7Hr4PPoG1fbcFPbZFaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی دیگر از زلزله مهیب اندونزی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/681289" target="_blank">📅 07:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681288">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc655e94fc.mp4?token=pReXmvClc9wwgoJ5fatC1a7WeqUrVTjhch2XOrFnhq2tXMYlmqIzbEkV8j-oy6VnztvqxUU_HkaeCRNFiBR0wcMp5pGU6-PzTjxz-LoeskP1YSdxJVx8L-EQS5mgoLIms_1OnEWazmRZqrsCnqsDZCipXX39gUfE9f_xWQkAkHCvXiWuPpFQDI4n39gwuW6dx2zq000pciQFN0aHyvEfz1o7sVymksfbOjovrt4jmhCj9_H-pMR1Be9FciwzHX-sWQfwaLHQQ1DdAW1yI43cAGJqvyptmi4XSFjfbe4xTcA58jay9AJzQq4nPFUkPjt01M9SViJdO7341gTPQjg8gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc655e94fc.mp4?token=pReXmvClc9wwgoJ5fatC1a7WeqUrVTjhch2XOrFnhq2tXMYlmqIzbEkV8j-oy6VnztvqxUU_HkaeCRNFiBR0wcMp5pGU6-PzTjxz-LoeskP1YSdxJVx8L-EQS5mgoLIms_1OnEWazmRZqrsCnqsDZCipXX39gUfE9f_xWQkAkHCvXiWuPpFQDI4n39gwuW6dx2zq000pciQFN0aHyvEfz1o7sVymksfbOjovrt4jmhCj9_H-pMR1Be9FciwzHX-sWQfwaLHQQ1DdAW1yI43cAGJqvyptmi4XSFjfbe4xTcA58jay9AJzQq4nPFUkPjt01M9SViJdO7341gTPQjg8gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فواره پاریس خونین شد
🔹
حامیان فلسطین در پاریس با رنگ‌آمیزی یک فواره به رنگ قرمز، نمادین‌ترین اعتراض خود را علیه جنایات رژیم صهیونیستی در غزه به نمایش گذاشتند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/681288" target="_blank">📅 07:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681287">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
مردی که همسرش را در مشهد کشته بود، در زاهدان به دام افتاد
🔹
متهم گفت به‌دلیل سوءظن با همسرش وارد مشاجره شد، اما در جریان جروبحث ناگهان خشمگین شد و با چاقو به شکم همسرش ضربه زد و گلوی او را فشار داد تا بی‌حرکت شد.
🔹
متهم پس از ۹ ماه زندگی مخفیانه و تغییر چهره، سرانجام توسط کارآگاهان در زاهدان دستگیر شد./ خراسان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/681287" target="_blank">📅 07:53 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681282">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1286888a36.mp4?token=SnFqLMI2GcjD0VKdu-osRqRuY9tJ_tEe_4ptwgkmSjlzPgx1Syv18vMQiXTpPBFUNqnJO2mNrva_JGRmJcwCoG9D6JHWcUm9i_mgYxAByeQk6vHPBVVSv--Wpum0nXhzZ_bxkLyNAUKuxDg9_hkjmU8ktw9o_90DvwmxrsiSUhnzTHL85uMRYahrmoljS2D9IheTBLwmKAbDcz1OYCmfdfY5BVsWNMmY1DXeUcIWguW3jLg-OPoHivzUvSx_et0UlhYDLFzjtaw0O-rrEwHqbUEMxGNCUFKQ8JbLJ7cs9qq7esjX1-P7cuBPjGhIBWezEd5yMm94uY1SdzK_7m4mQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1286888a36.mp4?token=SnFqLMI2GcjD0VKdu-osRqRuY9tJ_tEe_4ptwgkmSjlzPgx1Syv18vMQiXTpPBFUNqnJO2mNrva_JGRmJcwCoG9D6JHWcUm9i_mgYxAByeQk6vHPBVVSv--Wpum0nXhzZ_bxkLyNAUKuxDg9_hkjmU8ktw9o_90DvwmxrsiSUhnzTHL85uMRYahrmoljS2D9IheTBLwmKAbDcz1OYCmfdfY5BVsWNMmY1DXeUcIWguW3jLg-OPoHivzUvSx_et0UlhYDLFzjtaw0O-rrEwHqbUEMxGNCUFKQ8JbLJ7cs9qq7esjX1-P7cuBPjGhIBWezEd5yMm94uY1SdzK_7m4mQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ متوهم باز هم به مردم ایران توهین کرد!
🔹
«نمی‌توان اجازه داد کشوری که توسط مردم دیوانه اداره می‌شود، سلاح هسته‌ای داشته باشد.»
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/681282" target="_blank">📅 07:39 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681278">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-lI95t_O4_wB9d_1tBDg_l8yV_-qkDuJNkEqRyQOXCdqvlDmaojrgU7lZ434JT8CuvfU0SfMMwMgqv99OmCYWFNl3XNw_cYQUs9YQXWiK3chNgl2iK9_yOxJtCq5wY6hYMgQ8z6DDPJ7f_dE0u1esFFn62jvIvghBzW-MxqlYl4u2v7jZyRdngth4II74Zq8zErtjQlF18frkQmRy97NhvVhc6Y90cH1_HcBwMzcRM8rud5ujQrqkL7-f7pBGI2SHk2ozbI3MuLH3ridvJVif07BRn4Y6p5jJOYQUHVHjbdgNWlUXQB0d8Jnqa9UpFarMKx8OPVbgL5_8qBQON5XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز شنبه
۲۴ مرداد ماه
۲ ربیع‌الأول ‌۱۴۴۸
۱۵ آگوست ۲۰۲۶
شنبه‌ها
#دعای_عهد
بخوانیم
⬅️
متن و صوت دعای عهد
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/681278" target="_blank">📅 07:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681277">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
امارات: یک کشتی ما هنگام عبور از تنگۀ هرمز هدف قرار گرفت
🔹
منابع خبری اماراتی به نقل از شرکت ادنوک این کشور، از هدف قرار گرفتن یک کشتی در تنگۀ هرمز خبر دادند.
🔹
سازمان عملیات دریایی انگلیس روز جمعه از دریافت گزارش‌هایی دربارۀ حادثۀ امنیتی برای یک نفتکش در نزدیکی سواحل عمان خبر داده بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/681277" target="_blank">📅 02:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681276">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
پرواز هواپیماهای جاسوسی ارتش تروریست آمریکا در آسمان بغداد پایتخت عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/681276" target="_blank">📅 01:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681275">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromربات هوشمند اطلس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cjcd4o0xt_z_Y_NRoa6HPMNsly0pCjwQTrqMVfVSFew61zUiB-bXRTa-lJ0i0dZ8keoG4ZSo_C_XYtDqd8KM3hzqBAF3urAZqC_GLpIR6wZzni7dZFsQJvPGR8ms84mbWN66yKrojhI0OXpgystc2is_bCYlNd4Ct8nKDPczBSlbYjG5zwQybXCbaVnQCGK0mVwgrSETz-Dr6A66uXxeRmCykdomxEh8UNMx7gAUallBZZWVYut_eCBXkTaKTfgpwWMls5-k6W7Jch9Eg3Vyq65-dHF-N4PIBGfyfRZz3wV09N8O27R_LzUO0_Jzrgh9ywayqF0XStQodERDSAXmYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
📈
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/681275" target="_blank">📅 01:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681274">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
ترامپ جنایتکار وضعیت وخیم در ناو آمریکا را رد کرد
🔹
خبرنگار: اعضای خانواده سربازان نگران شرایط ناو یو اس اس لینکلن هستند.
🔹
ترامپ: نه، نگران نیستند.
🔹
خبرنگار: آیا استقرار نیروها خیلی طولانی شده است؟
🔹
ترامپ: نه. نه. نه. به اندازه کافی طولانی نیست. #Devil…</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/681274" target="_blank">📅 01:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681267">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0f993d653.mp4?token=aflRCIQ5xMDA5s_6ACNh-jkr8Ll_OP0eFpVudRk8senaBN_JynO5O_2BLCBgfW4uxluj46sTXavxcGwNh1L4mRFwZ8YQ-lVbeacMyXEIfi2Tv_GS_sLnXtDZfM7GloZNnCcMgj5EZYKYiGr---w56-d9CAZid47r2Xbj-aFIRB2GWaQD_b62fra9dhW3Z9WPc_VoZTt3ozDERek5Te0SK20zRd3_0HDAw4obNVpfv3NCbPyhkWtPIYy_OED-hCcalFvCk-4VeB-fbXXfttylu3FxFPgV3KHB3doKalTlL9jlWYbycYr2ewm95zScKgtS0DwIyCdDIUeEAjnekoOYjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0f993d653.mp4?token=aflRCIQ5xMDA5s_6ACNh-jkr8Ll_OP0eFpVudRk8senaBN_JynO5O_2BLCBgfW4uxluj46sTXavxcGwNh1L4mRFwZ8YQ-lVbeacMyXEIfi2Tv_GS_sLnXtDZfM7GloZNnCcMgj5EZYKYiGr---w56-d9CAZid47r2Xbj-aFIRB2GWaQD_b62fra9dhW3Z9WPc_VoZTt3ozDERek5Te0SK20zRd3_0HDAw4obNVpfv3NCbPyhkWtPIYy_OED-hCcalFvCk-4VeB-fbXXfttylu3FxFPgV3KHB3doKalTlL9jlWYbycYr2ewm95zScKgtS0DwIyCdDIUeEAjnekoOYjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ متوهم مدعی شد: به زودی تنگه هرمز را قلمرو آمریکا اعلام خواهم کرد! #Devil
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/681267" target="_blank">📅 00:42 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681266">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
ترامپ متوهم مدعی شد: به زودی تنگه هرمز را قلمرو آمریکا اعلام خواهم کرد! #Devil
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/681266" target="_blank">📅 00:38 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681265">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
عراقچی: هنوز تصمیمی برای ازسرگیری مذاکرات با آمریکا گرفته نشده است  وزیر امور خارجه:
🔹
آنچه در یادداشت تفاهم اسلام‌آباد آمده «خاتمه جنگ» بوده و نه آتش‌بس.
🔹
آمریکا این یادداشت تفاهم را نقض کرد و درگیری‌ها مجدداً آغاز شد؛ بنابراین چیزی به عنوان آتش‌بس ۶۰ روزه…</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/681265" target="_blank">📅 00:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681264">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
افتخار ترامپ جنایتکار به فرمان اجرایی برای مجازت اعدام قاتلان پلیس آمریکا  ترامپ:
🔹
مدت کوتاهی پس از آغاز به کارم، یک فرمان اجرایی تاریخی امضا کردم که بر اساس آن، هر کسی که به جرم کشتن یک افسر پلیس محکوم شود باید با مجازات اعدام روبه‌رو شود؛ و سال گذشته،…</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/681264" target="_blank">📅 00:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681263">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
عراقچی: هنوز تصمیمی برای ازسرگیری مذاکرات با آمریکا گرفته نشده است
وزیر امور خارجه:
🔹
آنچه در یادداشت تفاهم اسلام‌آباد آمده «خاتمه جنگ» بوده و نه آتش‌بس.
🔹
آمریکا این یادداشت تفاهم را نقض کرد و درگیری‌ها مجدداً آغاز شد؛ بنابراین چیزی به عنوان آتش‌بس ۶۰ روزه که نیازمند تمدید باشد وجود نداشته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/681263" target="_blank">📅 00:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681261">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b3f9bb132.mp4?token=XkrWj_FjnxFfKT6L3LrsurdZtRULiugknUppRucKoEuNrV-LeBliGoG1Im-mxigtpmwcj93MTek7TGbSC5kEr5fbm19VySrydx9S1OKLS4HVqQnC_HSX_Uaa5hebL9Ag7_TjJZGIBuA4FuG79-UhX2VYHh5m98-zBJiow8fEDOfwbeXjV151sOPu-8WBG0ZpIulwtOZEHlkS5l0zVv0YxtZUqhwOKS_vLPzLpGk6U0QP_3Ne0-uTt-GPqM09rkQgc7kkyGWqKI28lai7iyzOm5gt07ZAPAHx3vyZXDpuI6EDd5iIL9t28koYaLa4X823Y_TXoVoOrkZX-if8Hij4Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b3f9bb132.mp4?token=XkrWj_FjnxFfKT6L3LrsurdZtRULiugknUppRucKoEuNrV-LeBliGoG1Im-mxigtpmwcj93MTek7TGbSC5kEr5fbm19VySrydx9S1OKLS4HVqQnC_HSX_Uaa5hebL9Ag7_TjJZGIBuA4FuG79-UhX2VYHh5m98-zBJiow8fEDOfwbeXjV151sOPu-8WBG0ZpIulwtOZEHlkS5l0zVv0YxtZUqhwOKS_vLPzLpGk6U0QP_3Ne0-uTt-GPqM09rkQgc7kkyGWqKI28lai7iyzOm5gt07ZAPAHx3vyZXDpuI6EDd5iIL9t28koYaLa4X823Y_TXoVoOrkZX-if8Hij4Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افتخار ترامپ جنایتکار به فرمان اجرایی برای مجازت اعدام قاتلان پلیس آمریکا
ترامپ:
🔹
مدت کوتاهی پس از آغاز به کارم، یک فرمان اجرایی تاریخی امضا کردم که بر اساس آن، هر کسی که به جرم کشتن یک افسر پلیس محکوم شود باید با مجازات اعدام روبه‌رو شود؛ و سال گذشته، شمار جان‌باختگان نیروهای مجری قانون در حین انجام وظیفه به پایین‌ترین سطح در ۸٠ سال گذشته رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/681261" target="_blank">📅 00:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681259">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
رونمایی از تیتراژ جذاب برنامه محفل ستاره ها با نام "سوره به سوره" با صدای محمد اسداللهی
🔹
جهت شرکت در پویش حفظ جزء سی عدد ۳ را به شماره ۳۰۰۰۱۱۴۵ ارسال کنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/681259" target="_blank">📅 00:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681258">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9ct513eM5L-9I2qkibIPQE2vPtHj7m17EEVCeUcpn2OGWtsqTK5Stss3I55axILqAj_miL-6e4hzFWsPq4PULFfcWPCL9eozi9_xvHukWY5CVdnTwKxfD2_ddwNEdBcsQSNtv6skyE7RYWgKZfe-SwX05GkXKiXYohwvFdu7TRVV8BdM8TbEo-CzB7E6H9u-2rye9rE7CAIy0JICbQ7rllRR2B8HFq5obVVgXa5r1hYC31IOJog8zzhZ2UoPW2qBFWxRRBgrpP3ejsnuOUwSXYuKxLA7GT5v3SYY1KdHkw59XCQ7-Xa_ZtQCfns7hqORPogvn3Uw8_Ux_CKb1x6Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/681258" target="_blank">📅 00:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681257">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔹
اگر فرصت مرور همه خبرهای امروز را نداشته‌اید، جذاب‌ترین‌ها در دسترس شماست
🔹
🔹
نقشه نگران‌کننده ریاض برای ضربه زدن به تنگه هرمز
👇
khabarfoori.com/fa/tiny/news-3237668
🔹
محاصره دریایی اگر شدید شود، بیش از ۳ ماه توان مقابله نداریم
👇
khabarfoori.com/fa/tiny/news-3237665
🔹
سخنان عروس معصومه ابتکار از بازداشتگاهی در آمریکا/ نظر شما چیست؟
👇
khabarfoori.com/fa/tiny/news-3237660
🔹
دلیل استعفای کارولین لیویت؛ تماس‌های مکرر ترامپ در دوران بارداری!
👇
khabarfoori.com/fa/tiny/news-3237666ا
🔹
تغییر چهره عجیب رونالدو پس از ازدواج
👇
khabarfoori.com/fa/tiny/news-3237628
🔹
همه خبرهای جنگ و مذاکره را اینجا مرور کنید
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/681257" target="_blank">📅 23:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681255">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqb7rsJDsilMmZKKHSC8Zl15CS0sRj8JrqzSAqlFUCww-6RXRw3k33zh15cxa1pD1OrXUKLBIBkTOoVmzxxtdGzAX6iEBvOqh0DMCdDzJ41wM_Rk5B_j8z6hsvPMyDCgPayw-n_-258ZLaIymGNePzmLaZgu-qtEs6UfZWn2fg3xOCmoebvW4OORa3ZgxktXVmOlb62Vh-OENd3tU_nT0FGmVJaPA13SRnsSWUz6tj9ddqE2AzGOmIdnD1z8D3D6I4IxHPr_vboO1SGfXLId6jCRlPZOtz_xORNyB9O3jsB7u8GA1Pem89ySAEwfzEhzNxIRYBUQsUN7JAy0q3S-yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خارج کردن سوزن از روده کودک ۱۰ ساله در رشت
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/681255" target="_blank">📅 23:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681254">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LnJmBvcIwK5NS-QnC9HXjRpJFZvzS7Lge9w2q0MkQ8g7VSQ3X-VhxumMCOZbI_0ltOuPdUtOE6BiskQKc1aoBb9ksKre17gAKHi3DTYeOs7y_XjAQPIWCErQ7Ys7IxC1vV0S9WlkH-yx98GNSQnRMyMT9avGMfmS1CkXVX9ZbD_7bca522eznbA3SoprkrE0ujrtYJ__1aQCeBe9P1FN2XUcbubAFKNXIrV6G16b0O_ybCHJWHGVeErKH0bmcmAqjYMhG7tHoDknt4w4yxq6TKEmkptJ63ILyS3YhkjCe3qejtSrQroSpm4mymBG76gRtvvYqhOodO1_KPEKh5FuWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیلگر اطلاعاتی و نظامی osint: متأسفانه این اتحاد مکه برای دفاع از غزه تشکیل نشد
🔹
چنین سه‌گانه‌ای اگر کاملاً مستقل و متحد با ایران باشد اسرائیل را به زانو درمی‌آورد و هر تحریمی از سوی ایالات متحده را بی‌اثر می‌کند.
🔹
برعکس، این اتحاد به رهبری عربستان سعودی پس از ناتوانی امریکا علیه ایران تشکیل شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/681254" target="_blank">📅 23:43 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681253">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIYB3UwHH9NxB2O5GyPjVhhebc9Yc5dQwoVr_8gGKXSB9y2vdqACpAEic2HSeqgV9wFY_ynq-C8YF_CmLT2F8zUH6nGDjazC5V2cdMBazhik_XelY7njHrmzvMDbYPYczu1uApEQemWjBI_VybYxLb4LCCpg3PRKBo4p0Pn5CZ2Ia1wbo9h6zQNWCljCAZb8Pz8hPOpkxnfZ41e6bT2HD2CjBV3zxOIcfgHuxmKIpyMV4HeIdOoAl1XwSjhupHbvz9rrJIhFA6ZcfTXSU9L0o2p5sirCw7jqPIwU0yem4UnKjXTWiaT9PI5oNvSjcqYT0RtrbuHpY612YW1I1JvzhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه چینی: در طول ۲۶ سال، این چهار مرد به بیش از ۱۰ کشور مسلمان حمله کردند و ۱۱ میلیون مسلمان را کشتند، اما هرگز تروریست نامیده نمی‌شوند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/681253" target="_blank">📅 23:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681252">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcSHH2l3REfqFWwnWos7EsueDVq7ft_EtH4E6zQ8gkGbqW5CVrpm5mWf0Fe9UGvpIIq4HqBG3N8bKcj5eQ6qvTIDSZ54wCAgRnP7xkcCjgw6edsbyvKAiha0SSkYCoK6jDeNXYmeIrH8AV-kIULHMRYBRztUJdRFJsedNacgno3brS9l_hG5zHTEHBnpWZQRvzASFIjZ0LnL0NH6KwF1iKzhlSjtrU-RCBIwMwZKlkll6Ka88GEAbkY_MtYM4xNNTh48a_4C1UktOX7jgL19H7YEuTnynnS4Qv4Gx6oilVvaXwIYFonlfBb7fj1j6vRGjDyQNZE82s1tGmEFAouKDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک منبع ارشد ایرانی: ایران برای نخستین بار در این جنگ، در حمله به دو نفتکش امارات در تنگه هرمز از پهپادهای زیرآبی استفاده کرده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/681252" target="_blank">📅 23:36 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681251">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/462cf267ae.mp4?token=NF1tlrU9XEhyyyqOsm1pYuzmZSr1pvrWY380eCxgJaGKP3FnrSbEDDeg-lRkSQWCjgLFZaYgx1bVWi1BHfe5X6mPdasahDaMHknY2fEa8qiOFSCf5Arx7ct-VWoha73dHduZpSHeloHeZgtikI55XZ10ncJHW6VA4OtD2aketOnL4KcYAGqIHyRDM7zzlR8HcxdAepaaA1yiwaABysykS0nCQ2hbBHLhRM_RbzGjnzARPeT5JhgUQQ-qeetPNRS-q3reZ7us2M9t8Gw_Dl7KfMHLE1NiUcQHWHE2GZZyyX8TT_MMjB8L6Q7EWZeFoZ06fKWKI7s8u-RtKM1MWHg6dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/462cf267ae.mp4?token=NF1tlrU9XEhyyyqOsm1pYuzmZSr1pvrWY380eCxgJaGKP3FnrSbEDDeg-lRkSQWCjgLFZaYgx1bVWi1BHfe5X6mPdasahDaMHknY2fEa8qiOFSCf5Arx7ct-VWoha73dHduZpSHeloHeZgtikI55XZ10ncJHW6VA4OtD2aketOnL4KcYAGqIHyRDM7zzlR8HcxdAepaaA1yiwaABysykS0nCQ2hbBHLhRM_RbzGjnzARPeT5JhgUQQ-qeetPNRS-q3reZ7us2M9t8Gw_Dl7KfMHLE1NiUcQHWHE2GZZyyX8TT_MMjB8L6Q7EWZeFoZ06fKWKI7s8u-RtKM1MWHg6dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اتاق ده متری مناسب مرد مجرد در تهران!
/تلویزیون اینترنتی مدار
پوف‌نیوز را در یوتیوب تماشا کنید
👇
▫️
https://youtu.be/KXxqKDxq9TA
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/akhbarefori/681251" target="_blank">📅 23:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681250">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7ba875d8a.mp4?token=fszNkE-dbqS5A0LSpNaYpYG0z1tkqeKBgMvbl_VwE1syKswm1PRNdhNXAKs3hH72wjf64vjA3BMDckmgZEvnKmEw21T0zZXEquCSSCuLfXYPy47XfqsBzzE2RnEdNDVCs4XaI_Ja1K3d7u_N4Ga3hfyti_tg73MRAb5JmiBUJU1XJVZyTathIsrIUn5hcHVEr8xRrLEzJHXwDTZzd6rhOd6mN9eiAM68Loh-Es957KASeuttnV3o5mPt__OfxAkmNV40ovuMqa5DAt8q5nH02WH_-XTcC0EvE4gCW6A3ORxktndypJznCS4mwAdkXdnm-se7EY9fVJY3KyitSBje0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7ba875d8a.mp4?token=fszNkE-dbqS5A0LSpNaYpYG0z1tkqeKBgMvbl_VwE1syKswm1PRNdhNXAKs3hH72wjf64vjA3BMDckmgZEvnKmEw21T0zZXEquCSSCuLfXYPy47XfqsBzzE2RnEdNDVCs4XaI_Ja1K3d7u_N4Ga3hfyti_tg73MRAb5JmiBUJU1XJVZyTathIsrIUn5hcHVEr8xRrLEzJHXwDTZzd6rhOd6mN9eiAM68Loh-Es957KASeuttnV3o5mPt__OfxAkmNV40ovuMqa5DAt8q5nH02WH_-XTcC0EvE4gCW6A3ORxktndypJznCS4mwAdkXdnm-se7EY9fVJY3KyitSBje0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای مضحک ترامپ جنایتکار به فاکس نیوز: به‌ایران از لحاظ اقتصادی ضربه شدید خواهیم زد #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/681250" target="_blank">📅 23:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681249">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9OKmynr0_wUOIuO_SF02ofNoxdyMTR7YUfF4qWtwSYsKFeHiaDCeX_YxVb7g8-qdeQlQUc4cnUIU5e5fbN_DSrlRCrj7gGyJ1YHnvb5tq5Xew22-oSEAO8bfJm7nLokJD6KNBDqFypmIPmVMLEiDHFlh7cmOiZePHgO5gMeJKnwBKws9lkNYF19uekl5LH3PEv_YfMgNc-NRK9Xd4HWlb15kdtI4mJIIMUbuA9N9cFGUtib6QYWZyCwgQ-9O-LK-BsP3cqtbDBfxIqb9voDd2peWSgrZy2cWb9xMgbH1gjngtxjhkuKD4nHoZGDTZSRf-AYX2nMTj4wLxlSZVepUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تلگرام ۱۳ ساله شد؛ بیش از ۴۹ میلیون کاربر ایرانی
🔹
تلگرام ۱۳ ساله شد و اکنون بیش از ۴۹ میلیون کاربر ایرانی دارد؛ ایرانی‌ها بیش از ۲.۸ میلیون کانال دارند که سالانه بیش از ۹۰۰ میلیون پست با بیش از ۱۷۰ میلیارد نمایش یونیک منتشر می‌کنند.
🇮🇷
✊
@AkhbareFori |…</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/681249" target="_blank">📅 23:24 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681248">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/500ce1a0a8.mp4?token=Vkuib_uXT7EvudmDlcLO9Aox5G797VHpeojnvE1-Ad33HsvEAsnTcj6ZgxALO2fcm5ZLOMx1mwtVMcmxsBw3nSPmXDO-IOSwDcV4y0RkNLFiT7nthhYTaVZYv6Ta5S0KFIT_J3wtq2lg5dOkhi_T21RXy8tT2WjvXzpzDdQmOQA-fnnPHlcg0opJbymmUq__ntxdLIsU_AKYcFfDGzXQrr1M0rh5n4jlyLmdQeznQYx0zZ5fKfq6g-fxlZshYvWsIm1W3BWFHAtC99SvUv-9anqbBbooy_SHfKIt2PgkbdhNIJTF39MeiwTwjPN1f4UIDnFVk3EYslCC10sL4XgV0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/500ce1a0a8.mp4?token=Vkuib_uXT7EvudmDlcLO9Aox5G797VHpeojnvE1-Ad33HsvEAsnTcj6ZgxALO2fcm5ZLOMx1mwtVMcmxsBw3nSPmXDO-IOSwDcV4y0RkNLFiT7nthhYTaVZYv6Ta5S0KFIT_J3wtq2lg5dOkhi_T21RXy8tT2WjvXzpzDdQmOQA-fnnPHlcg0opJbymmUq__ntxdLIsU_AKYcFfDGzXQrr1M0rh5n4jlyLmdQeznQYx0zZ5fKfq6g-fxlZshYvWsIm1W3BWFHAtC99SvUv-9anqbBbooy_SHfKIt2PgkbdhNIJTF39MeiwTwjPN1f4UIDnFVk3EYslCC10sL4XgV0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جدول زمان‌بندی خشک کردن میوه‌ها با سرخ‌کن #چرخ_زندگی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/681248" target="_blank">📅 23:21 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681246">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bjSZvkzwPFQcyLTkNk6_t2C3RGYY56uHYiu84pyVugwGTcqPjQCljDImK-MTq_S5mkmcSBrlukj5HfegrW0oc2XehnuAlqqgCgcz9I0umPKtDKLYW4pjy50kmPcgYudk147n0skB5v7FngCVCZAuLkCzWSdDKCuFWfL9u64vc9PmFwOZVltO3kzYiMsmytMAkRDsdV65_N1gJrjZb5HXxzDEhbb3nBJ41t3rLSgNeqVmDpuQVgjLU_VglJDIiwKoDsuLYLN7rdNoIsR7tQe6bxDGUje8eFvUuvnKHqfDL5357GK3_x4p_xE8rEUViXfmiIpHCEW0RZgAsP2eAjrIaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری زیبا از جاده هراز
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/akhbarefori/681246" target="_blank">📅 23:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681245">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
ادعای مضحک ترامپ جنایتکار به فاکس نیوز: به‌ایران از لحاظ اقتصادی ضربه شدید خواهیم زد
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/681245" target="_blank">📅 23:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681243">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a8759ff1d.mp4?token=Nla7Ud6FJQTp7ACBvO_ZSHQI41v-GRiSYKiM6tUIzyaddkmJPLNLdulFq0OPyv7JV0NyabEupfzS17UB6_fxeV45KPEag5ouAoDbvGTFqLB0veJYlp3eGsF1ULI7gmcEu40EYd4T0v3QotIKuOtOc3wwfCz5nd8LIyLo6P6hHYlx9jqFYRjop1zobCCEgYNOtsBZ10e-5GXqTUtzQySdk8T70QSKpdlI3ym_YFWQj_CSfu5aLY2eJzILJzBZbf05qR4sT-wPg-BMpbXtbCXReLDVhqEUTFpxd-gRpclCeKAlmSFch-9P-c42MlqK7lRu-zWOj51e8iQHm7EU7xrHWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a8759ff1d.mp4?token=Nla7Ud6FJQTp7ACBvO_ZSHQI41v-GRiSYKiM6tUIzyaddkmJPLNLdulFq0OPyv7JV0NyabEupfzS17UB6_fxeV45KPEag5ouAoDbvGTFqLB0veJYlp3eGsF1ULI7gmcEu40EYd4T0v3QotIKuOtOc3wwfCz5nd8LIyLo6P6hHYlx9jqFYRjop1zobCCEgYNOtsBZ10e-5GXqTUtzQySdk8T70QSKpdlI3ym_YFWQj_CSfu5aLY2eJzILJzBZbf05qR4sT-wPg-BMpbXtbCXReLDVhqEUTFpxd-gRpclCeKAlmSFch-9P-c42MlqK7lRu-zWOj51e8iQHm7EU7xrHWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توضیح دکتر پزشکیان درباره گرانی‌های اخیر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/681243" target="_blank">📅 22:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681241">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/812f3d2ee5.mp4?token=KtLyfj7FtBLvl35yZQDhwBZXVL1cdkLNfgoG0L4rsMpoJV0oYBttFCcQVlZIOqBxpGY3_QCVArkeWu9XjnbTPTojVmIKXLH3wRLNHOkqpPUWy4faehlb98z_nlN6UsyaRjuHLmCUuT1DWFyesiU3iZF6htCVQX_ZO_wuX_dpdZYVv1UwoHBkUdQLC2XVOqEVJrvLI4TwJPMOVMPSf6-_nfixhUmm4uAiboY6S_JZomPbPxgcWafVH34EJuwyFzgOULk-rkvzm0YoDhMhVvxQzSdsYX6PaxXmrYQA-DSxWB2TUVFQlGixc4g2nclN7mowvqVpdY6swC1WoQ080Nzzag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/812f3d2ee5.mp4?token=KtLyfj7FtBLvl35yZQDhwBZXVL1cdkLNfgoG0L4rsMpoJV0oYBttFCcQVlZIOqBxpGY3_QCVArkeWu9XjnbTPTojVmIKXLH3wRLNHOkqpPUWy4faehlb98z_nlN6UsyaRjuHLmCUuT1DWFyesiU3iZF6htCVQX_ZO_wuX_dpdZYVv1UwoHBkUdQLC2XVOqEVJrvLI4TwJPMOVMPSf6-_nfixhUmm4uAiboY6S_JZomPbPxgcWafVH34EJuwyFzgOULk-rkvzm0YoDhMhVvxQzSdsYX6PaxXmrYQA-DSxWB2TUVFQlGixc4g2nclN7mowvqVpdY6swC1WoQ080Nzzag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توضیح دکتر پزشکیان درباره گرانی‌های اخیر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/681241" target="_blank">📅 22:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681240">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOaY8gOwDL2jWzb_mNDTmlsURjhzwdE3EHR3mq8bgPJGv0i1Nvj02sDZKYxPDkuNabIpErrD1aq6YXSp3orG5Yvob729F6cgm33UUaxBEQ0V-Plb-PVF7YelA8Sg1E8AhUYFB3Ov4DbvnNY47XCcHg0XtAK2HitwceirPV7wHnWhPx6eVLrtB3PVxuH6qjHla_2FG2vs-IY_1uDYxf_85XjCaakOlAY8882Y_7yvtIYRMVJIJN2gFBUy80W6qjEhQ_Nb2kOE5CGRHRM8BKsYazyv-TKhlZgCdrcRLYnNqfYE0ZDweevKiJKEKinsUmaowaouu8PLxKpySJzCMfV6AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خورشیدگرفتگی ۱۲ اوت ۲۰۲۶ در اروپا موجب جزر سریع و شدید اقیانوس شد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/681240" target="_blank">📅 22:47 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681237">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ddfa3587d.mp4?token=VX1oTkCWz-THWwF1NDFl-0me6pqhc-0FKp_3EC5Omy0YsLQESh7QV5zwcFp90mNH-osKMJ3SsEpmjgYJxcuxf5liT5kXrAgcR2Ha3hCZIMNUjm19-GCdmbj0V-1h91Ifm9nVlBhCA0WbxMQAQ3N-8Y1F5RnZDkmqa3qv0ryWTPuRtwc1Qit_Rpuwx4GSICFwhDwrDIhHNRfepTrk4qc1dLp7YANPZKSp30VTeoiJ5aSLwcADwk1Z8eD-mB4DM0xxC2AUp8ev2tLgOr51oEKNCpfgRiVNQ6SXBHXyzZMZCeYj1xtl1X1q6mfc_VDaSh1TbRUiIZN0ws5rhLD8zlONWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ddfa3587d.mp4?token=VX1oTkCWz-THWwF1NDFl-0me6pqhc-0FKp_3EC5Omy0YsLQESh7QV5zwcFp90mNH-osKMJ3SsEpmjgYJxcuxf5liT5kXrAgcR2Ha3hCZIMNUjm19-GCdmbj0V-1h91Ifm9nVlBhCA0WbxMQAQ3N-8Y1F5RnZDkmqa3qv0ryWTPuRtwc1Qit_Rpuwx4GSICFwhDwrDIhHNRfepTrk4qc1dLp7YANPZKSp30VTeoiJ5aSLwcADwk1Z8eD-mB4DM0xxC2AUp8ev2tLgOr51oEKNCpfgRiVNQ6SXBHXyzZMZCeYj1xtl1X1q6mfc_VDaSh1TbRUiIZN0ws5rhLD8zlONWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: تفاهم‌نامه آتش‌بس با رضایت نیروهای مسلح انجام شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/681237" target="_blank">📅 22:37 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681235">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aec64a1c85.mp4?token=MzUTNDnQ3GWyRGr9FWdKbdMDpsGMTaNSYtkG3gyjDNT1tTP-gTPVVqTRD45b5xzDlNfROoskgSDKgjIq6EJIxaEo4qizL0oReXwD--rFzn_kJB26F2iZ5g2hrLCfQu1nSUSF2E_L5pIwfU3krq0BptPwMf4AVD-bFvre-6dBD_fhudARyXidJ50gmuKqpDfvGQ-yHWOAKDf289oVvYDusuMX2uZ2O4cDg6G_BE3qETe8mebrcLt14j8qjgvddMohpBZg4yCfMoDyER6VtqmCE6YN4G7sI91DkF20oZKxwAaJ4qskkWXtjTJIDoZw7tMgsKe3GWs3-vK73gfiG72ECg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aec64a1c85.mp4?token=MzUTNDnQ3GWyRGr9FWdKbdMDpsGMTaNSYtkG3gyjDNT1tTP-gTPVVqTRD45b5xzDlNfROoskgSDKgjIq6EJIxaEo4qizL0oReXwD--rFzn_kJB26F2iZ5g2hrLCfQu1nSUSF2E_L5pIwfU3krq0BptPwMf4AVD-bFvre-6dBD_fhudARyXidJ50gmuKqpDfvGQ-yHWOAKDf289oVvYDusuMX2uZ2O4cDg6G_BE3qETe8mebrcLt14j8qjgvddMohpBZg4yCfMoDyER6VtqmCE6YN4G7sI91DkF20oZKxwAaJ4qskkWXtjTJIDoZw7tMgsKe3GWs3-vK73gfiG72ECg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خورشیدگرفتگی ۱۲ اوت ۲۰۲۶ در اروپا موجب جزر سریع و شدید اقیانوس شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/681235" target="_blank">📅 22:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681233">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdOgzx8UTP0QNoCfYweErOPnAsVo_tm_4pKXx2Cl5oVMx7WGMkwASG_b9Q76Q8Zg970fOw8sJSCBI1FaAjHzlNS7h-ajNA4RwMnBoWsQEwP9Z20Z1yesZn6uiNpa2LN4R72n8tEMG0ioWyDD2_7OZqhWnklCTCjJywJIq21rL5CTpqr1bsHNeG_1Sm3iDZ86AZMNHsRouPJsuqFuq9P3e7Gjc6VLfM-dFhrJxMeKXZ-SidZvhiKKG_w1HL31a9Cv_zNvONQwUSDt19CQ3zfr7p6oZpNaXKI7oY9OAx53JsY6pOao12KWkUqPrRoejxyufzgVTNJYNOoYKqQv6Orafw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
طلا؛ یکی از پربازده‌ترین دارایی‌های یک سال اخیر
افزایش قیمت طلا در یک سال گذشته باعث شده این بازار بار دیگر مورد توجه سرمایه‌گذاران قرار بگیرد. بازاری که علاوه بر رشد قیمت طلای جهانی، از تحولات نرخ ارز و شرایط اقتصادی داخل کشور نیز تأثیر می‌پذیرد.
در این میان، صندوق‌های سرمایه‌گذاری طلا نیز توانسته‌اند بازدهی قابل‌توجهی ثبت کنند و در برخی موارد، عملکردی بالاتر از انواع سکه و ارز داشته باشند.
این صندوق‌ها امکان سرمایه‌گذاری غیرمستقیم در بازار طلا را فراهم می‌کنند و برخلاف خرید طلای فیزیکی، دغدغه‌هایی مانند نگهداری، سرقت یا اصالت طلا را به همراه ندارند.
صندوق «جام طلا»
نیز یکی از صندوق‌های فعال این حوزه است که با سرمایه‌گذاری در ابزارهای مبتنی بر طلا، امکان حضور در این بازار را از طریق بورس فراهم کرده است. مسیری شفاف‌تر و کم‌دردسرتر برای افرادی که تمایلی به نگهداری طلای فیزیکی ندارند.
📊
تصویر بالا، بازدهی یک‌سال اخیر صندوق‌های طلا، انواع سکه و ارز را در کنار یکدیگر نشان می‌دهد. (
بررسی بیشتر : کلیک کنید
)
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/681233" target="_blank">📅 22:27 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681231">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
آکسیوس: کاخ سفید بدون اطلاع نتانیاهو در حال برقراری ارتباط با اپوزیسیون اسرائیل است
🔹
آکسیوس به نقل از منابع آگاه گزارش داد، در بحبوحه کاهش محبوبیت نتانیاهو، دولت ترامپ برای جلوگیری از به خطر افتادن ابتکارات خاورمیانه‎ای خود، شروع به برقراری تماس‌های مخفیانه با رهبران اپوزیسیون اسرائیلی کرده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/681231" target="_blank">📅 22:07 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681230">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
کانال ۱۳ اسرائیل: آمریکا چند هفته پیش درخواست اسرائیل برای بمباران اهداف ترکیه در سوریه را رد کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/akhbarefori/681230" target="_blank">📅 22:01 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681229">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca4d9eb2a5.mp4?token=WRDpKZ0IX3V0_s1KyJwzXif5FhgwLLg6yUC4BklKxfxOuVFrN6WT_CwyKhwmGMobF_DpqHuu0C_2W9e5bhvGuC0nlg_gMB1c6YZG7O8LBp2MlYBaulHtc7EWENS_352EQmG0zH1db8wTX3EmTpKEJs2GLqwX6g9-SnbyGMsjU8KigohzFMvjYU7dpqIoUdsakVRDH6apzUCXietJXxfWUDPSPAbMxD5QKroweln_YWwRSDBfmR7iZAPWu78CpfAyf07EzOYcycGW0s9DpDHLJ3sbpPNqKfaYbzSj8JNtqfhVTDgAHpMYlnWtNkm03tiYntaf2GsZzGPJLBk5AiKDjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca4d9eb2a5.mp4?token=WRDpKZ0IX3V0_s1KyJwzXif5FhgwLLg6yUC4BklKxfxOuVFrN6WT_CwyKhwmGMobF_DpqHuu0C_2W9e5bhvGuC0nlg_gMB1c6YZG7O8LBp2MlYBaulHtc7EWENS_352EQmG0zH1db8wTX3EmTpKEJs2GLqwX6g9-SnbyGMsjU8KigohzFMvjYU7dpqIoUdsakVRDH6apzUCXietJXxfWUDPSPAbMxD5QKroweln_YWwRSDBfmR7iZAPWu78CpfAyf07EzOYcycGW0s9DpDHLJ3sbpPNqKfaYbzSj8JNtqfhVTDgAHpMYlnWtNkm03tiYntaf2GsZzGPJLBk5AiKDjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ربات پینگ‌پنگ باز هم از راه رسید
🤖
🏓
🔹
واکنش زیر ۲۰۰ میلی‌ثانیه؛ هوش مصنوعی حالا پشت میز پینگ‌پنگ هم حریف می‌طلبد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/681229" target="_blank">📅 21:55 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681228">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjCrF04ymYYTufSC7_n8MbVVJ2J9WbeXSEkeUTneoG7s_qqo2euKjBtg9cYjwVZ-_RFxT7aVHkY5HJgddErl_KLTTcalkIUYHcH8Dc0ABlq4YuLUXDu1cms5GnPbIHpMWoOM20wLNudqVbIJMaediGVVG5-zT5ZF1Vz_oWv2nxaXEAIb0DUlcfmFP_CGV6ZHpAu6m5WoGBEsuFCCzaadCWmWufmm0CsJ-vQfn1ijDmSKKTwY4iedioGhAkc-AR_1yeg3HjCta3hz5ua-JcLE5BTE_XF5tA24oNVwRSPdrV1cqAxF3rsDGDT9Fu_gDattXM9pRWcODN1Q3UCPfJFdmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمایی تماشایی از ورزشگاه ترومسو؛ ورزشگاهی در شمال نروژ
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/681228" target="_blank">📅 21:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681227">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/693cd8d045.mp4?token=Ik5wOS71hjdOKuVLLbgzRS_kNWb7N4-TgynEcbZg0KJDmwPbMmiczZQidfS69U4KiDSFH-cBdJoiBllAJSZYH9jV5TbQiJs0-rjyy3-j6OzDd7bTIH4q8eeH1-S9paaxaPEpA16VZ8uCsGCR-MLQ5euKdvWv8d6BAIT-V6VZMKGzSOjuAA6wZu3AfDN6hQUsiDS5gT92jXOI3i1FeYFIP6l4c1YxJJJycIFb2I3fwJQvPPiL8rh3Yogq-m1xjQjUm1oPY77JkYCbrarT8BmSktjZF1evcQDkYXZmo7q0xDZwt5boxWKwvlpF1KonS1HcPztyTeSEIqVVsrZSshWnPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693cd8d045.mp4?token=Ik5wOS71hjdOKuVLLbgzRS_kNWb7N4-TgynEcbZg0KJDmwPbMmiczZQidfS69U4KiDSFH-cBdJoiBllAJSZYH9jV5TbQiJs0-rjyy3-j6OzDd7bTIH4q8eeH1-S9paaxaPEpA16VZ8uCsGCR-MLQ5euKdvWv8d6BAIT-V6VZMKGzSOjuAA6wZu3AfDN6hQUsiDS5gT92jXOI3i1FeYFIP6l4c1YxJJJycIFb2I3fwJQvPPiL8rh3Yogq-m1xjQjUm1oPY77JkYCbrarT8BmSktjZF1evcQDkYXZmo7q0xDZwt5boxWKwvlpF1KonS1HcPztyTeSEIqVVsrZSshWnPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی عظیم در هتل۱۳ طبقه در ومبلی در لندن
🔹
گفته می‌شود این هتل محل اسکان
پناهجویان
بوده و فقط چند قدم دورتر از ورزشگاه ومبلی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/681227" target="_blank">📅 21:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681226">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/935af1a1b9.mp4?token=M0nhpCfst1eSeP-UF-IvCYvH10bPCO-cXSg_qKoQAYOHk71PGnr_OkkBdrg3uqyt3JIoWd1UYhkMLhmypKESs64YQ_Qy6zMNEPbcAxp9zGOkk2uVL0moag1FzczH2h1oULvYSE3g6d_w1eou6nEA_rjhC2nadJM61hoHOu1udGAgbqsMII1lKcWmy9HSV5qI5deGnz5EdGyQOrEoyM5q_MYiD8qhP8zOb7BVEnQiD6w-VwxQxHjYhHWd0djS7TnvYJHvy9IDLnpc6Oz1uV_xWXiV5zL8w_8w1RI4NlMobkCi4OO3fJZg06vUW2OelUtmLw6F2mOaF3U-sWEcnKyh3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/935af1a1b9.mp4?token=M0nhpCfst1eSeP-UF-IvCYvH10bPCO-cXSg_qKoQAYOHk71PGnr_OkkBdrg3uqyt3JIoWd1UYhkMLhmypKESs64YQ_Qy6zMNEPbcAxp9zGOkk2uVL0moag1FzczH2h1oULvYSE3g6d_w1eou6nEA_rjhC2nadJM61hoHOu1udGAgbqsMII1lKcWmy9HSV5qI5deGnz5EdGyQOrEoyM5q_MYiD8qhP8zOb7BVEnQiD6w-VwxQxHjYhHWd0djS7TnvYJHvy9IDLnpc6Oz1uV_xWXiV5zL8w_8w1RI4NlMobkCi4OO3fJZg06vUW2OelUtmLw6F2mOaF3U-sWEcnKyh3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارگر ایرانی در عسلویه، تکه‌ای یخ را به سر و صورت خود می‌مالد تا با گرمای طاقت‌فرسا ۵۰درجه مقابله کند و چرخ تولید انرژی کشور را بچرخاند و سهم خود را در آبادانی وطن ادا کند
🇮🇷
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/681226" target="_blank">📅 21:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681215">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Opq4Ogmru1FZNUWX0Jw5cW295D19caJPk7KN-A7bhN9k-DCFqYGIUU4aF2qEx-ZiVQ5EQm1gNn0BKS7pEjZ-PBN1Gc3Y6uj2Ujx0UWZun94R5zUocLykFtu1_cm2p-D4L-iePxqKcVZtf13MQ8py6eNdkBqSQlfPJPHcdF3-zsMAJDaPJlVkAFUITHIIMpwVzPJD5P-rv5BPKXZWOiTSJOz0B-ifv-bJRanOZN4AkIuKAbsi0-rrRwu1WHtZnaMeQa7xR0V0Hd4r93hKb3p0E4H6pUK2LJ-yn-9frYwtmYyJjqvFLPmfKbnleKxQF_wSRJVAMIKgn8wGnHdSRonc3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UyCTCf80ebHpQyQ1eTAoXpxVVeIwCSZzCrhMaPnOQiFKiTR-6MFQHdaqaN7dRvYU4oAaod7_D0I_qBDZRS6TpPaxkwkg6IeVfM4fue9QfLmLtS-WGf5RqotcKuGd1wOHAB-T7X45ghv6vXEra9VlFPsSuDdWGIDM4NQ1iOcJZk6cT1sVQ5XRDZqVV0vbmd2al3-fhrjbVlG_3pnF2_YHAGGy8UXGhpsqxNDR3_xLSu_QTd85J46zYdWSywsl_UlHhJ_ydI9tJzesmmieqxG_dMYdYoJzH8Y-HmKbzQPnf7AKmHNNjWYEXUih2e_gcAvayaagXv2cKhuIlDUwHaZVaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tmSfRRc8PeNHuddS3R1K4f8wzSaDU1PIMtBRrUPoJjxs_HMDEvYdACAhe7J0m5fOuRowW_BJI9meDPjGIWlE1qArDUBcQIE_yVmNwsea-oeUSs-rfp6znR5e2QezcpXK9g1iQmBrDLSD-FmgUyuiZvcm852pjNNgdG9fbbrYjYOsha_eLjnONjVPxxJzBeUrsgPN-Vl2HZHSL29U8EbGD4HawTLg8LQuw18pAoMVE5aTsPdHAVwN71QdPgj2z9F6h2zX11yPA6NTFODFD4TuTWM4bjcxPTd3nK2HT7ohkI0Y3o_hi3NWyu-VDmX1fniOcATqcD4wD3HHReEtYVMI2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/faL5b03DUnnClor_Pj575lJ6cuKKbBGuGndIG17p6GxqaCDuuHe8q0fPKun1OCmoHKZSP2dH-rMaiwVDwv5XRanQwLqDXTje88qBuTYoviji_w4SNzHRp_HZToeIio1LMJOOW6CLUhQ-qe2TvNDlHGCL9YVsANXQfrPzPALqHQZGBXoaukcno1J_BoV4E7BwrQDFkJgJBp3hkkoEsf_V96UO9jJaeC557z6BwN4ZFLg9NXaUoppf-xOHC1yBIAmfj_y8U7ChDZy5iCdw-LRmFUhMM8HSG3xz8ZdntX5DKvcSvA6L6kW9NwJ_f-HaeXjvID_NGCg9u_RK_chfXot5CA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اشتباهات رایج در مصرف دانه‌ها که ممکن است تمام خواص آن‌ها را از بین ببرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/681215" target="_blank">📅 21:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681214">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cafdd78c9b.mp4?token=NWM6gPE97ZzQ6LpubHxyZ_HqLRnHgmwZgWZtyWnZ-wTt_PgyxTUJTfwPo5sMWyaZcnLw7XukJMQMkFGKjxInbnYtih_69Igc0Pdx0lSYZpM4Oz88KKyyF4MhTky7E-HYpJUquoGt9IESrXskgg6QITCpPkSiAjwk0sGhf95biRYiBXhb6Z8PVMPsWbxutEs9qLM4TIm2VbI-CxJCXL8K4R_zstSY0zNp-wBfc-4UbhJIY-gyG3uWVJJI4Sh82tC1bRcsBdn_yi4O8dB9PDP1hjW5IXY7svX6_-IYm7wDGIx3dO_DSkw11FLSrCsSSAN9VG3VYOPrOaJUbO7GYZntHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cafdd78c9b.mp4?token=NWM6gPE97ZzQ6LpubHxyZ_HqLRnHgmwZgWZtyWnZ-wTt_PgyxTUJTfwPo5sMWyaZcnLw7XukJMQMkFGKjxInbnYtih_69Igc0Pdx0lSYZpM4Oz88KKyyF4MhTky7E-HYpJUquoGt9IESrXskgg6QITCpPkSiAjwk0sGhf95biRYiBXhb6Z8PVMPsWbxutEs9qLM4TIm2VbI-CxJCXL8K4R_zstSY0zNp-wBfc-4UbhJIY-gyG3uWVJJI4Sh82tC1bRcsBdn_yi4O8dB9PDP1hjW5IXY7svX6_-IYm7wDGIx3dO_DSkw11FLSrCsSSAN9VG3VYOPrOaJUbO7GYZntHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دو پدیده فضایی در هفته اخیر
🔹
تصاویر دیدنی از خورشیدگرفتگی از دید ساکنان زمین و تصاویر از ایستگاه فضایی و تصویر دیگر از بارش شهابی که از داخل یک هواپیما ثبت شده‌است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/681214" target="_blank">📅 21:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681213">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
سی‌ان‌ان: نشانه‌ها می‌گوید دولت ترامپ از جنگ با ایران خسته شده و دنبال خروج است
سی‌ان‌ان:
🔹
نشانه‌های زیادی از خستگی دولت ترامپ و متحدانش نسبت به ادامه جنگ با ایران دیده می‌شود؛ جنگی که ترامپ تصور می‌کرد تنها ۴ تا ۶ هفته طول بکشد.
🔹
کین فرمانده ارتش امریکا به طور خصوصی به مشاوران ارشد ترامپ اعلام کرده که دولت باید راه فراری از جنگ پیدا کند زیرا گزینه‌های نظامی روی میز برای تشدید درگیری می‌تواند نتیجه معکوس داشته باشد و بعید است که قدرت هوایی به تنهایی به اهداف ترامپ دست یابد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/681213" target="_blank">📅 21:07 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681212">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uq1HczK848c7g6LH8BDqXcnSS_t-JkZps0gTXUqUB7FoqOSuS8oyFXXNXVJQFQJltgRafCie0DtQ_Xt1C3ZWHjWb_jojMB60yIxuEPPmxXKaxjwae0mJjxRnwuGUAGh3FJhO9iTCfTtdHH8wM3m5zZuLcmRchTLZaEH4S0kbALVlWuBXbibcMB7oKI99lx1cAbhfi1HR0uG2VmVFEG3KSXj2LIfdECvTDHurYGnbNx2sP_JQ1uHMfwZmGX_CmwuIj_bY82uWcFGbdKe2IKiVqmylivx237-XxetwPgR76ImAhtk3dFQcEt7pdV6Oa0pRo5wtK3Fi7ngxgniqXaAXjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش مهارت‌های ورود به بازار کار؛ مهم‌ترین مهارت مغفول‌مانده در سیستم آموزشی کشور!
🔸
در این نظرسنجی بیش از ۱۷ هزار نفر شرکت کردند که سهم روبیکا ۵۵، بله ۲۸ و تلگرام ۱۷ درصد بوده است.
🔸
بعد از مهارت‌های ورود به بازار کار،
حل مسئله، مهارت‌های ارتباطی، سواد مالی و خلاقیت به یک اندازه از نظر شرکت‌کنندگان در سیستم آموزشی کشور اهمیت داشتند.
🔸
این مسئله بیش از هر چیز، نشان‌دهنده اهمیت مسائل اقتصادی در آینده کودکان ایران از نظر مردم است.
@amarfact</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/681212" target="_blank">📅 21:04 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681211">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12961fee27.mp4?token=hN4SIlsnS5E3SFcD273efGmQoQTt3NT_QChAswv7B7ximFACwPRT3-YWiJ37NR1yHuhDfKc7erT5szGjlf6RllPi3pc0Cw_0mBV3pOI_8qpP-KMrtJPGyZaIn7mDEwzS3US033K1uG5jOvmJ8-GLPrOW4qElwF_MZC-fV3kdC5uE7Z4ZtMqbLondkL8sfDXGteq7I1ejhWP1Q0FwT7pTpYsa4FofQuRjUhis-H767iSaN_IrvBzzmx1Guoe3y5_N_RVZvp_Ki_QXa8ZbnQrE-eK9klUgM2YCBKSCsYA6sOXhLez_zgzeEvbb-osiTHJ79iybHhjy9G7wPPmHRyRQqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12961fee27.mp4?token=hN4SIlsnS5E3SFcD273efGmQoQTt3NT_QChAswv7B7ximFACwPRT3-YWiJ37NR1yHuhDfKc7erT5szGjlf6RllPi3pc0Cw_0mBV3pOI_8qpP-KMrtJPGyZaIn7mDEwzS3US033K1uG5jOvmJ8-GLPrOW4qElwF_MZC-fV3kdC5uE7Z4ZtMqbLondkL8sfDXGteq7I1ejhWP1Q0FwT7pTpYsa4FofQuRjUhis-H767iSaN_IrvBzzmx1Guoe3y5_N_RVZvp_Ki_QXa8ZbnQrE-eK9klUgM2YCBKSCsYA6sOXhLez_zgzeEvbb-osiTHJ79iybHhjy9G7wPPmHRyRQqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ جنایتکار وضعیت وخیم در ناو آمریکا را رد کرد
🔹
خبرنگار: اعضای خانواده سربازان نگران شرایط ناو یو اس اس لینکلن هستند.
🔹
ترامپ: نه، نگران نیستند.
🔹
خبرنگار: آیا استقرار نیروها خیلی طولانی شده است؟
🔹
ترامپ: نه. نه. نه. به اندازه کافی طولانی نیست.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/681211" target="_blank">📅 20:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681203">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjzoU3kQIO2sMX4f9Ma9UdlE1o53uqqgaCCda55aHO5FWTl0SrEPbwxQWSZYstIdn9VSKEiyGXDKxgmNUOraM2w3CFuAGVDd4ZF3UC6q9ra3dpJk1of9HvlhOsq5zt-I-oM3h-N9rQSD_j3uYigPXiqSL2X4de1RLJlPHOBQ8JIMlSW9m93op7bEHKYnGvINX7n-_7OJN3mz3DXpGALgqnFNJscQ0yu7rUGSh1UHLpupdrP0sWu0cQ68ivdrxvBnTfdASvNu0OCfUEzXkZ856PjwuplqDhoe97fKKnCyBG4EdEMC7qJ0zZ-VAouzgQfSOmrcGnVYpd3a_AV2632Skg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چگونه فیلیمو «بدنام» را پرمخاطب ترین سریال تاریخ شبکه نمایش خانگی کرد؟
🔹
پس از مدت‌ها گزارشی بر اساس اعداد و محاسباتی رسمی از تعداد مخاطبین پلتفرم فیلیمو بر اساس دیتاهای مدیران فیلیمو و سازندگان «بدنام» منتشر شد که نشان می‌دهد پشت پرده این پر مخاطب‌ترین بودن چگونه است. این گزارش منتقدانه، تحلیلی رسانه آخرین خبر را بخوانید؛
https://akharinkhabar.ir/cinema/10970209
@AkhbareFori</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/681203" target="_blank">📅 20:36 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681200">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
روایتی هولناک از جهنم؛ وقتی هر گناه، عذابی متفاوت داشت
🔹
00:12:30 در پرتو نور امام حسین (ع)، رنج طبقات جهنم قابل درک نبود
🔹
00:16:25 خودکشی پایان رنج نیست؛ آغاز سخت‌ترین عاقبت است
🔹
00:24:40 پاسخ به همسر خانمی که به او نگاه بد کرده بودم در طبقه پنجم جهنم
🔹
00:32:30 آنچه در انتظار آزاردهندگان حیوانات و درختان است
🔹
00:40:30 دستی که بر پدر بلند شد، اجازه ورود به بهشت را نداشت
🔹
00:55:00 سنگینی حقوق همسر در ترازوی عدالت الهی
🔹
01:03:45 راز انسان کامل بودن در جمله‌ای از فرزندم در برزخ
🔹
قسمت سی‌ام (فراز و فرود (۳))، فصل پنجم
🔹
#تجربه‌گر
: سید محمد موسوی
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/681200" target="_blank">📅 20:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681199">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
هزاران عضو قابل اهدا، به‌دلیل تأخیر در رضایت، از دست می‌روند
امید قبادی، نایب‌رئیس هیئت‌مدیره انجمن اهدای عضو ایران در
#گفتگو
با خبرفوری:
🔹
ایران سالانه ۳ هزار مرگ مغزی قابل اهدا دارد اما تنها هزار مورد به اهدای عضو منجر می‌شود و دو سوم مرگ‌مغزی‌ها با ۷ تا ۸ هزار عضو قابل اهدا، به خاک سپرده می‌شوند.
🔹
به‌طور میانگین ۲۸ درصد افراد در ایران مرگ مغزی را مصادف با مرگ می‌دانند و در فاصله تقریبا ۳۰ ساعته رضایت می‌دهند که در این فاصله، اکثر ریه و بخش زیادی از قلب را از دست می‌دهیم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/681199" target="_blank">📅 20:26 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681191">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/micLE1iJq3RMmh1Ndg8zaUXZ0XT3etp3d_YCbKpcmiw9oRU9-qLtagviBd6qGXSZ6Pn4-NzcSfrN6z1BU23JEQYIRBXoJS07e4dIjjRaAJVihE0Klf0D0PRekFE3-SM0mrpLQkWHr1vOBeFdYP5BWa11_Iz7Bc0bvh6nSWR415-MuoISthYyqItooe92UI-GPVb_8oKGF_I3EjYBIntpAzgm4S8uOKdVxqlQ7w28DsIDYzOSBUIC2yK_JD6JyaUKzK6ISqkX30ErVrdt75IBsDV8hhh1gFoIvfeOXkwqxL9qkY6Zj_L2oT_Plm4AvrLfT_eHaxL9fzKnsEl96z0FKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WBiH-f_HV9B4uKpDLTJ30apSp_RNaMDX9SY4cBcXiyMgjMe8D0W3Leh6NKPFS2QtfsrSomzF3s0Gl2yPw3KTzns8X0KeYQr4GVqvlyNC0gr214BRcxEQygRhtyaD_GP_O78B4Z2H3s0G8TLisMdPAqKRQit7rmkxCskit9-zdUGru5NDQAYvx2VPsyt6gPh3UyNfWub2ef2diEK1ga0ZOYnO1NnmIriBghSe_jCDSJYy4u2ENDafsdpOzrfEKPODnxJ0UwYXkAjQANT_U_9kTCQCGAZocJoplNOmSkjCLU6IkS6N9jgOzokuX2TByb0URyckfOL3gwXZZAwI3U6p2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ckqvm700yX2887HCRR7cDSUxqSqRq4pUgK0fZzJdRd92kB5Rjhfs7soW1AGgt7zBFctXJiAkes4PbLI9eYBxHfJPCjxJ3XzgIrkAfz3Cm0XNn-mqB2zop1FV4ujFnh-G08GjCGkmrKr2S7SwzLqqLifhQkGX6wbNfqbxgV_gJ-lmHhxbg-jMvYUTnEvNhEik2OPtzNmQgMEP6DR4cO9Ycqhx6mmXJRpbBxnPwEXtc7a41MZ_nbCAI85XLwatBI61utOc0XeRlYBm9s7SYpCFLE3zPpqAkLOoMYPi2yqjywLLoHk28Rv5xIemcq9LuS2QH9TcWEX3ie2dyqNcPTAs4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rxW1_XtyVJEzYbscPRyIht8wO-Mllhnr9780kbpdPk-8EFc2Qr4CUt4K81CjrpwLmWsLWbHF2yN2e55yp_3EEqa8tGebI66UV_Gvf5vQQ5cFDJRK_N0kStcVrpsNI9CVfzsI8EqRv5MacwKpsAog_9B4U6-rlsUErT1F_jVbmKMlJm8A3pcG2BTVWe4Yy5C5GoRdyNFMDmcQVPEY5XGvOEEamAg5R76pFvoxz3R08CR1QopYL1og0wXL9Y6tKI19OCi-z24Vwn7izqD2x-VddNEMWPaRTRxYjj3ZI-xJSz-Yr9eFQwUIaUM1yyjOqzq3ncP0q_L7nwoiLuoluPExmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
قبل از شستن لباس‌ها این راهنما را ببینید؛ هر برنامه برای چه کاری است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/681191" target="_blank">📅 20:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681187">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/024cddc0ca.mp4?token=Qxw3aZeeh2bqEAfd0d9exfX6fVVSBBVAQtZGZ6hjJ4O4nOIMMoUfExnr-SU294UXyGYIOeTsDHMIcHZMRL5E406I3DwGBOyb_XllrrghXhBzSU_ODh-T2Il8JCp5hA5IV4IutALYJYL4uVKqOaHSMCFe1bYMj__0IKH1blaVFa_csjjI_jq0AIsAOZHdFLbW2qcGHqsB7d914BWd23kpVIrLbpWvmCeAxlOuMqWKHR8wUBSqj3P2EGQNoxdMFt2RvTf1eboFxNBUjRCQc90_1QRtgiGTbalZrjavZ6p25_-cwJNSyvjFSX-NBJG3U5oJyxUEx6Ep4yvqUW8uoCm7lxGVcf8CCnWUIFB6rCyQmj_-Gdwtj4kqnfn3bcMI2Ah8AIxsHleymrCvTho0PI_bnD1yWetQHzrBPYrz-LHXPaBh1MUDLjz2AJ5nXSLZ7Wd9BEXDe5YVDnFfmualrAhNaQctZXRhrRHLKD2Mrm4Rc2eyqNmviYDH-k8v3d-vU673Q1J3Xy4BSH84GV16m5Oj8z3x_K5OpCapqHc0M08K-ibR0p4qQrOXN-UxYVefOvIXO2YTsjj4sfvG7jdA16yiGGE5EoAcTdzjPIR829xcfG6HIQdkBB5UttWRiJvAZ1fxW6AZ58WQQXJefP3835bDgPcDgS2lDRZVpBcxMGrf7gM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/024cddc0ca.mp4?token=Qxw3aZeeh2bqEAfd0d9exfX6fVVSBBVAQtZGZ6hjJ4O4nOIMMoUfExnr-SU294UXyGYIOeTsDHMIcHZMRL5E406I3DwGBOyb_XllrrghXhBzSU_ODh-T2Il8JCp5hA5IV4IutALYJYL4uVKqOaHSMCFe1bYMj__0IKH1blaVFa_csjjI_jq0AIsAOZHdFLbW2qcGHqsB7d914BWd23kpVIrLbpWvmCeAxlOuMqWKHR8wUBSqj3P2EGQNoxdMFt2RvTf1eboFxNBUjRCQc90_1QRtgiGTbalZrjavZ6p25_-cwJNSyvjFSX-NBJG3U5oJyxUEx6Ep4yvqUW8uoCm7lxGVcf8CCnWUIFB6rCyQmj_-Gdwtj4kqnfn3bcMI2Ah8AIxsHleymrCvTho0PI_bnD1yWetQHzrBPYrz-LHXPaBh1MUDLjz2AJ5nXSLZ7Wd9BEXDe5YVDnFfmualrAhNaQctZXRhrRHLKD2Mrm4Rc2eyqNmviYDH-k8v3d-vU673Q1J3Xy4BSH84GV16m5Oj8z3x_K5OpCapqHc0M08K-ibR0p4qQrOXN-UxYVefOvIXO2YTsjj4sfvG7jdA16yiGGE5EoAcTdzjPIR829xcfG6HIQdkBB5UttWRiJvAZ1fxW6AZ58WQQXJefP3835bDgPcDgS2lDRZVpBcxMGrf7gM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایتِ فصلی تازه از پیوند، هم‌افزایی و نقش‌آفرینی همه سلائق مردم
🔹
بسیج، سال‌هاست میدان حضور اقشار و گروه‌های مختلف مردم در دفاع، خدمت، سازندگی، فرهنگ و پیشرفت بوده است.
🔹
امروز سخن از یک گام فراتر است؛ گشودن میدان‌های بیشتر برای مشارکت بیشتر، پیوند ظرفیت‌ها و به میدان آمدن انسان‌های بیشتر.
نه تغییر آنچه بوده؛
بلکه کامل‌تر کردن آنچه هست.
https://basijnews.ir/00f1KP
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/681187" target="_blank">📅 19:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681184">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0rV50ubk4BCUqBMaDySIUoNPV0SgI73QqXf5N12G_EBAEG9iTNgCRYC4b936Vid-E8UiMuVYyqh8LKLKUrxK9Jdqehil0Fe2CElGGoHp4K41e7fRi3om8x_32ajDd7k_MRnnb7oTcc1GgVVmtcWj4cbqXtwZykZNTv-Wy8_1qRWNMM-NHI103s5eg0hGkix2hjD7FRQn6pUyE7haF7eiu6YE8sNCx1cXJjwutbmHVdjglJavKNzKVhGviRVfvkEwJfaIxKPsndL3yFWlEv4Iebrx1j5L6GY222yB7Z4xePSRxalbh9T5nHBTI2AEOPvjQaTyIDTirSqTjNp3YK1Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اینترنت در آستانه تسخیر توسط AI؛ موجی که می‌تواند انسان‌ها را پشت سر بگذارد
🔹
کلادفلیر هشدار داده اگر روند فعلی ادامه پیدا کند، طی پنج سال آینده ترافیک بات‌ها می‌تواند تا ۱۰۰۰ برابر ترافیک انسانی شود.
🔹
رشد انفجاری سیستم‌هایی که می‌توانند به‌ جای انسان در وب جست‌وجو کنند، قیمت‌ها را مقایسه کنند، اطلاعات جمع‌آوری کنند و حتی کارهای مختلف را انجام دهند، می‌تواند چهره اینترنت را برای همیشه تغییر دهد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/681184" target="_blank">📅 19:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681180">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
هر پیراهن، فقط یک پیراهن نیست؛
روایتِ یک سرزمین است، یادِ یک نسل و افتخارِ یک ملت
🔹
کیت جدید استقلال خوزستان با الهام از
خلیج همیشه فارس
و ادای احترام به
شهدای میناب
طراحی و رونمایی شد؛
تا نام و یاد کسانی که برای این خاک ایستادند، در میدان هم زنده بماند.
🔹
برای پیراهنی که فقط رنگ آبی ندارد، رنگِ ایران دارد.
بانک ملی ایران، هوادار استقلال خوزستان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/681180" target="_blank">📅 19:32 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681177">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJ1M9klfWQoRc2TA9P2JzVK_pMJiynC-7Z3Z4aa09H-BCcpz-J20t3qrOs_p81XrKJJ2HGDwEBKJKHZlVSd23UmKTA111IFXFcFefvTGXhiant0MUbGBAeCc0ijS-7YN3ECh4a5_zU_1Tat1HJMOEru6zXrReB_iq_A26TQFM-v8xR-Z0PExMN-QRC-kEz5Y0FPcZC9IKGeuT7VNvJjGPaSiQj22TcF7LISYrqOflnrw_ryf-sCiz_aEDzqwN9SZL4_polDffVX-mTtTpWtJ93H948EFV35-VXPSi4TvYKfOwKPR1dsoHCMMXZiSBVT1A_CgPuY6c-SepFAED8IHGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنوع اقلیمی در کشورهای جهان
🔸
بیش از ۸۰ درصد از پهناوری ایران را اقلیم خشک و بیابانی تشکیل داده و مابقی آن شامل نواحی معتدل و سرد است.
🔸
در مقابل، کشورهایی مثل آمریکا و چین تقریباً تمامی اقلیم‌های پنج‌گانه جهان از استوایی تا قطبی را در خود جای داده‌اند.
🔸
همچنین کشورهایی مانند اندونزی با اقلیم ۱۰۰ درصد استوایی و امارات با اقلیم ۱۰۰ درد خشک، از یک‌دست‌ترین پهنه‌های آب‌وهوایی محسوب می‌شوند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/681177" target="_blank">📅 19:17 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681175">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be8a99796.mp4?token=d23khuuGxpgov9qOm415qSP3A-GYKjf8L7Oc6C9l_zn8_mT9hdl9haFnQag6FCxBxNTq5MRZLev_SiFgrNq45NFDbPvJVmbW52ZSH0PumphRfA9tQ3pmskg7wMK8ZvJ-yW0cI37lBj01l0HJLzQnzc5XUcVFXeZu9hk6cHXuQxE8ViYe57SZcsQ-eQ6faDVx6QTa7oFHDXkRzq6Ign6JsbTBMB1lDe0gusjn4ogakQOJ9A126YgruHdv8BOgnbbw5V07Sel_S-iHSlP3URRiDLRuEG4YV4F4ADQwZ5GWmTfcf5tU2OTbXArefLMxLhfeOOC5xPjl82jISfLUEP30HG8XhXWJimPe-ph0X-WTLqi5OiRpabpSHN2Bk_EpqQ9fVyIEOIS48Uavz3OYp773F6_rUD8ldyjhxwUfDZSMoIvMCk4zDFyqow3Bo3vANgnxFDpBdJf7mnP4emCsFJGYw8gcIsLBUn3N3Rs2atGHq3nug1rXwshchFmPzhiwWBIj_x4MK_RO5GRVFUwDeDYcZe8KJ6V9NEUhv2XejmxcaRtut7kiDNi2HxIzL_2BLmUH5OGorR-1Tj7jW7nKmxwsm2utxtsBSqJU5GAxFoin2xECN78IPlSuvAfx0rETNssMK-wiapuWQiaDumtFU2F74B5b0VH2xobEsXNsKRncp1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be8a99796.mp4?token=d23khuuGxpgov9qOm415qSP3A-GYKjf8L7Oc6C9l_zn8_mT9hdl9haFnQag6FCxBxNTq5MRZLev_SiFgrNq45NFDbPvJVmbW52ZSH0PumphRfA9tQ3pmskg7wMK8ZvJ-yW0cI37lBj01l0HJLzQnzc5XUcVFXeZu9hk6cHXuQxE8ViYe57SZcsQ-eQ6faDVx6QTa7oFHDXkRzq6Ign6JsbTBMB1lDe0gusjn4ogakQOJ9A126YgruHdv8BOgnbbw5V07Sel_S-iHSlP3URRiDLRuEG4YV4F4ADQwZ5GWmTfcf5tU2OTbXArefLMxLhfeOOC5xPjl82jISfLUEP30HG8XhXWJimPe-ph0X-WTLqi5OiRpabpSHN2Bk_EpqQ9fVyIEOIS48Uavz3OYp773F6_rUD8ldyjhxwUfDZSMoIvMCk4zDFyqow3Bo3vANgnxFDpBdJf7mnP4emCsFJGYw8gcIsLBUn3N3Rs2atGHq3nug1rXwshchFmPzhiwWBIj_x4MK_RO5GRVFUwDeDYcZe8KJ6V9NEUhv2XejmxcaRtut7kiDNi2HxIzL_2BLmUH5OGorR-1Tj7jW7nKmxwsm2utxtsBSqJU5GAxFoin2xECN78IPlSuvAfx0rETNssMK-wiapuWQiaDumtFU2F74B5b0VH2xobEsXNsKRncp1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیر همستر ۵ ساله؛ تقریباً دو برابر عمر معمول همسترها!
🐹
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/681175" target="_blank">📅 19:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681174">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
فرمانده کل ارتش: تا آخرین قطره خون از ایران دفاع می‌کنیم
🔹
امیر سرلشکر حاتمی: این قدرت ایمان است که می‌تواند یک جنگنده اف-۵ را به فراز مواضع نیروهای آمریکایی در کویت برساند، در حالی که آن‌ها از پیشرفته‌ترین سامانه‌های پدافندی زمین‌پایه و هوایی برخوردارند،…</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/681174" target="_blank">📅 19:09 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681173">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
چرا هنوز حساب‌های بانک آینده تعیین‌تکلیف نشده‌اند؟
هادی محمدپور، دبیر کمیسیون اقتصادی مجلس در
#گفتگو
با خبرفوری:
🔹
پس از انحلال بانک آینده و ادغام آن در بانک ملی، روند تعیین‌تکلیف حساب‌ها، بدهی‌ها و کارمندان این بانک به دلیل محدودیت‌های ناشی از جنگ و مشکلات سامانه‌ای بانک‌ها، با تأخیر مواجه شده است.
🔹
مسئولیت اصلی پاسخگویی و تسریع در این فرآیند بر عهده بانک ملی و کمیته ویژه مشترک با بانک مرکزی است که باید هرچه سریعتر نسبت به انتقال حساب‌ها و تعیین‌تکلیف بدهکاران اقدام کنند.
🔹
تأکید می‌شود با وجود زمان‌بر بودن فرآیند بانک ملی باید با اولویت‌بندی، هرچه سریعتر نسبت به تعیین‌تکلیف مشتریان و نیروهای منتقل‌شده اقدام کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/681173" target="_blank">📅 19:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681171">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzUFFqePNaUL8ztrvIDCRAVfJ3KpF0zuO0vi5aPHaclxKq7gfwEklKf5-xAW3SwDGH_FpGhJ7r0q5zkXhPuUCvqMrQ96wGZu_SV_eENEstRsnNciD8G_PWUd4xwe4iqvOwmqHRknzbQ6hEnqQxglUC1_4fEyPIRcxTmKO1qS5fUcBXc-kblrxCPxHPLsD-mSRps0em5NkuhqcufjcxZVg6IHb76_6dVHNRCgO-AZME3PYynLtbwJGKu0TE6R_de1n6YUyqobygyxBgrX28LDZCyR2YTYlIaBllA9I52NIvslMAOhRg6Ufp2CTN4Q97XlWC6mha6GvCJsk0YZAtX9Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی کاخ سفید برکنار شد
🔹
دونالد ترامپ، رئیس دولت تروریستی آمریکا در اطلاعیه‌ای رسمی از برکنار کردن «کارولین لِویت»، سخنگوی کاخ سفید، در پایان ماه اوت میلادی خبر داد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/akhbarefori/681171" target="_blank">📅 18:39 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681170">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z07TzBOPw3gi6YCAbBsLrH-ZcFa3afA0I_X2rta_J9dxPSOpa9mxO1LOvghX2TK4JW-35qbsVafEGNH36mVGJenTnMtK5P6s6tep_pGY7EEzrATXcqh1KsyBfEqR2TQ4W0k-kIfpo3C2OSEvS0xsDQ2vAc2qpaBp2cs13A4CktgAAO2ETK5tqwqOpoBPZyWuvOrudnAia-L4n7kIDmQVuIZEv227PzpchNmssiytMFmCP5IZr1BgPAc_87HvTv_otzp8i0C5nY7njf0YXONZyWxxlHIm3BMAE_NaSuus6q1-cm5iByXpI-8lrn_ynGHrp1uPGrvEAqy1gKanYCagoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گوجه را ببوس! | نمایش آشپزی با ملکه پاستا | نادیا کاترینا مونو کیست؟
🔹
نادیا کاترینا مونو، که با نام مستعار «ملکه پاستا» شناخته می‌شود، یک سرآشپز ایتالیایی، نویسنده، کارآفرین و شخصیت رسانه‌ای ایتالیایی است.
#چرخ_زندگی
تجربه میلیاردر شدن با آشپزی
👇
khabarfoori.com/fa/tiny/news-3143141</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/akhbarefori/681170" target="_blank">📅 18:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681166">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d719e28752.mp4?token=GnPM5TuN1MfRughp_RKTumYPrBIJ0ZncHrM5QxDvNH1dALYi_brbj3DgsZMvR3nGAJHPWLxKt1gSpFzLER8ectZqRf5a9GzApSbk_q76rsoBhVDAN2AeL017xFslxk4x7Dfx9OIkNxwooIccn9TocF8HXB1WNCLhLyuCIKVD5D8WuKcsT51Ly9zAcr5dtnksCxo5fJu68mlLiGQbKPOkpIeeyTXko6AXj0lzPGSpmSszZvnPoxImckkbd89POYDFq9F7GKCLKCtG-W2yODcCaqsXfHbltFixT8n-t6tb8Wy6sJh24NDWFcpj0opIgVNGAeSIE3QhapD-8jiyMZmbZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d719e28752.mp4?token=GnPM5TuN1MfRughp_RKTumYPrBIJ0ZncHrM5QxDvNH1dALYi_brbj3DgsZMvR3nGAJHPWLxKt1gSpFzLER8ectZqRf5a9GzApSbk_q76rsoBhVDAN2AeL017xFslxk4x7Dfx9OIkNxwooIccn9TocF8HXB1WNCLhLyuCIKVD5D8WuKcsT51Ly9zAcr5dtnksCxo5fJu68mlLiGQbKPOkpIeeyTXko6AXj0lzPGSpmSszZvnPoxImckkbd89POYDFq9F7GKCLKCtG-W2yODcCaqsXfHbltFixT8n-t6tb8Wy6sJh24NDWFcpj0opIgVNGAeSIE3QhapD-8jiyMZmbZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علیرضا دبیر، تیم ملی کشتی را آبیاری کرد
🔹
علیرضا دبیر برای کم کردن گرمای تابستان، ملی پوشان کشتی آزاد را با آب پاشی خنک کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/akhbarefori/681166" target="_blank">📅 18:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681164">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4c58a8ae1.mp4?token=UMslw3NQ7SGQeCAnSt7lZbOn_MJnpiuSdBNYmoWkw-nAMfYnYj8CInouLkKDYnrfgZOvQQZTHVRe6k_yuLgH81oDpqQVfCx7CaRBod_Y9wwjLgPSJd9aqQ-4TFJNHCfN2etsx55COSYN_i9ZvVTdCXaP5uvYhQpiscuyhXftvsQlUPGwovJ6u-nRgTn2us6d6d3jWFJ_dbs6pTirlCXV5R9NsC8Fvi1kO-jRCd6NPDUtJMn_EVLj8H-oN98tI_35jUjEsaRs898fKnIAUhY8B9kyOCvCnj1RWyblCDt-f5yX9LtzmucDmrcRJ6-i_UzmA-BLnOAEbbHVKop5AKP7kZYxYMwBkLJqY_hJSW-TCAOXhHyuqpW65LcCuXV8kwlifhCTJKsmakXXNsNzbrC7NaFn81yGoxlFbdslygNQX0cj4nVCmMp5vJjEGfGec1FKo4gC0joRxcI7OpGaZzPJsBdLdX67IxQQXegiAncI7c0-dwLDkGAsS9r33TGfgX17HFKqo83I5ampZTYemQNoFBJp7Hxk3poT5J3rhPviVT7RV1TAeD--Nqt2UC4AybJOzRLOW2fxJHa2s9hBKjSrDluO1GCJIFlzG7ipmgq_HOoenTRo3hw0t5WJPUCbQ9HuberYrVu0nVINS_qtlF9ha3WT2w7rctLtJpvXbwojzOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4c58a8ae1.mp4?token=UMslw3NQ7SGQeCAnSt7lZbOn_MJnpiuSdBNYmoWkw-nAMfYnYj8CInouLkKDYnrfgZOvQQZTHVRe6k_yuLgH81oDpqQVfCx7CaRBod_Y9wwjLgPSJd9aqQ-4TFJNHCfN2etsx55COSYN_i9ZvVTdCXaP5uvYhQpiscuyhXftvsQlUPGwovJ6u-nRgTn2us6d6d3jWFJ_dbs6pTirlCXV5R9NsC8Fvi1kO-jRCd6NPDUtJMn_EVLj8H-oN98tI_35jUjEsaRs898fKnIAUhY8B9kyOCvCnj1RWyblCDt-f5yX9LtzmucDmrcRJ6-i_UzmA-BLnOAEbbHVKop5AKP7kZYxYMwBkLJqY_hJSW-TCAOXhHyuqpW65LcCuXV8kwlifhCTJKsmakXXNsNzbrC7NaFn81yGoxlFbdslygNQX0cj4nVCmMp5vJjEGfGec1FKo4gC0joRxcI7OpGaZzPJsBdLdX67IxQQXegiAncI7c0-dwLDkGAsS9r33TGfgX17HFKqo83I5ampZTYemQNoFBJp7Hxk3poT5J3rhPviVT7RV1TAeD--Nqt2UC4AybJOzRLOW2fxJHa2s9hBKjSrDluO1GCJIFlzG7ipmgq_HOoenTRo3hw0t5WJPUCbQ9HuberYrVu0nVINS_qtlF9ha3WT2w7rctLtJpvXbwojzOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با جان خودتان بازی نکنید؛ هنگام شعله‌وری سیلندر، با بستن شیر فلکه از گسترش آتش جلوگیری کنید
🔥
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/akhbarefori/681164" target="_blank">📅 18:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681162">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
پرداخت وام ۴۰۰ میلیونی برای اسقاط خودروهای فرسوده
🔹
رئیس هیئت عامل سازمان گسترش و نوسازی صنایع ایران با اعلام آغاز اجرای آیین نامه جدید نوسازی خودروهای فرسوده از هفته آینده، از پیش‌بینی وام ۴۰۰ میلیون تومانی برای دارندگان این خودروها خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/akhbarefori/681162" target="_blank">📅 18:07 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681160">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPsHvI2CkkxKO8PAo8xQono2nyUfFZYgxNvuBAJgSgM6c3TFJvBPE6my4O43h0Gi6ishdd_Dpit-CNYksLBOZuJ_I7aDM3nDafwY_rZarI2b1wzzsQcL8w2jsmyuzltpy_eajl0pZP-Y_hF9ovJsY0nKFklcznErrAe5JL5RiiJRtS1x8e__Wz_MlE7wueglZhp9Gvcb3ZeV95dlrE3agdkA_VViF0dQwCVcqKRkwiiuEoiKlsZ5u2D2d_ibKeK3wN84ky_T9bAHETjyIeJmuoRtWP_PmKvU46RQ9BG3q7NshmaMNGRFSKmylDaKCnVsofDsjg3MvUcRSuWKekT6Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لگوها این‌بار وضعیت بحرانی سربازان تروریست آمریکایی در ناو آبراهام لینکلن را به تصویر کشیدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/akhbarefori/681160" target="_blank">📅 18:01 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681159">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
ورود خودروهای فرسوده به کلان‌شهرها ممنوع می‌شود
معاون وزیر صمت:
🔹
خودروهای فرسوده از تردد در کلان‌شهرها منع می‌شوند و نقل‌وانتقال، تعویض پلاک و جریمه هوشمند آنها نیز ممنوع و اعمال خواهد شد.
🔹
این قانون شامل خودروهای شخصی، تاکسی‌های اینترنتی، ناوگان حمل‌ونقل عمومی و خودروهای خدماتی و باربری است.
🔹
گفته می‌شود که برای اسقاط خودروهای فرسوده به دارندگان آنها وام ۴۰۰ میلیون تومانی پرداخت خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/681159" target="_blank">📅 17:58 · 23 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

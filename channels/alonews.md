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
<img src="https://cdn4.telesco.pe/file/KtAzV1Pmir1gkKl-4ODKdWdhVbBys6Zs0Fa6yJjg1Q8I8_DPN_DckRlefO0UVj8OC2Rvg6A-jvr72vxqLaADOFrL983gXtm4_IjZNpAATG5gaTNaTHWgmUN21zwxMKLOh8AAUWnXHBE9bBm-UdPgqg5PEEhOCIFRcg8iqFhgP0J2Kpm-_1dQ9rjEmw4_Rfyw2wlweQLPIq-dYVRxu_0AOxxj0dwq56WVIvz2QqtgcaUW5Ug0sOS5C73qgq2QKsyOuUJZYAg73KbQZ8wVDqhNm9bPJF-m1YsYuSw_rcbhUCusZurhd9lRv_B_8ISBc-hTnlzGpd1WQXOcH4w17tZrmA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 954K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-26 16:31:47</div>
<hr>

<div class="tg-post" id="msg-120384">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
منابع رسمی پاکستانی به الحدث: اسلام‌آباد به دنبال قانع کردن تهران و واشنگتن به «انعطاف» در مذاکره است.
🔴
اسلام‌آباد به دنبال ادامه روند میانجی‌گری با تمام «جدیّت» است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/alonews/120384" target="_blank">📅 16:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120383">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mx4rUCO777iVtD5akuXwdJfS12WR0U7e1Zyf7WVXoxXM_vUww_M21c0JXHbTseNyAWeYVkJeajeDsCNN9PnvbFkDAlv5J_q9Z9G9VOcvgiUmeWO9-9OEY2yniuxmDb827oJFCtfPhKVeb7Oyz0n6iZxL6rDR39nD57cDpHCgI4UWJggzWiNc68zoT41LT1qlz1meskwFptng8zTMfXk7asGXJXgx8_Mz1IUilKGnfPFpPvRBjQPUG739ifmpFkd6a65zOogd9-MU5ZKLYtAma_YTXsh4ACE3NNjlt_3KDsj89j0mV6ZbJGRjf5Cv4vn9u0OqKLZGKH5_02hf5E4R-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قطعی اینترنت وارد روز ۷۸ام شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/alonews/120383" target="_blank">📅 16:20 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120382">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb5b602b82.mp4?token=PWinXQMQ2KuQ-JrCgRfOOCXCWwJ_Dh0FXJ5eRO4GAaGNWz59dGaLC3a8ntMCt-Zh3Ka3-QHdWBeNHlNKFgR4pvwbbhl714czaWWJabWii2qkKBMxLjFOsDI2h0jlOtknMBa8sD45KOM_6ncRye5-xAAe2v9NyZ2wVlWePepXJQO607hRaGclbTZCGM055izOeWe_kIx2etCV1reYQqMSQj5KAr2aAABsPfItOyZJ3aXT324_oBdVeGeRn61cnyeGDC2oaa1fEY-2lYPcKvMXChVBlYc9OffkGrtxJodVjxHdxG0-D9x0d4ALhUovoKS8kc2txvCX3muWAaUlRAQZbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb5b602b82.mp4?token=PWinXQMQ2KuQ-JrCgRfOOCXCWwJ_Dh0FXJ5eRO4GAaGNWz59dGaLC3a8ntMCt-Zh3Ka3-QHdWBeNHlNKFgR4pvwbbhl714czaWWJabWii2qkKBMxLjFOsDI2h0jlOtknMBa8sD45KOM_6ncRye5-xAAe2v9NyZ2wVlWePepXJQO607hRaGclbTZCGM055izOeWe_kIx2etCV1reYQqMSQj5KAr2aAABsPfItOyZJ3aXT324_oBdVeGeRn61cnyeGDC2oaa1fEY-2lYPcKvMXChVBlYc9OffkGrtxJodVjxHdxG0-D9x0d4ALhUovoKS8kc2txvCX3muWAaUlRAQZbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو منتشرشده توسط ارتش آمریکا از عملیات کشتن ابوبلال المینوکی، نفر دوم داعش در نیجریه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/alonews/120382" target="_blank">📅 16:09 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120381">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04afd7993a.mp4?token=DAMti7uvu3QHDDFD4Uu1S5s2EmitkKaqB8G1e51LxMlEYE5TVFpdQY-JZhS1bZsIFleG89WqEnnHwtjc4haecJP9atA98N1X78RLeCDhoOEBOwZTnJLEoYmtYoC66Sh-EfVfxGeE7fgvbkFTSpf0gAhFyc7KwQ-RC-ymtedB-FK4-PcqdCA9SQpbFMfl0PoPUgAm8X84z3sknUoPqyQk8JigZLHRXHXVSK4Zqej3cTMm8_XPI3e_QzHtLfuRiMLdpxfeWRO8cYP2N9VWlKiBLgp_mRfpaoFqY8yfptR2vCQkQZTcCJNmng0A7rosgtXj_odwKshJsL7ZoOnyL0n3xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04afd7993a.mp4?token=DAMti7uvu3QHDDFD4Uu1S5s2EmitkKaqB8G1e51LxMlEYE5TVFpdQY-JZhS1bZsIFleG89WqEnnHwtjc4haecJP9atA98N1X78RLeCDhoOEBOwZTnJLEoYmtYoC66Sh-EfVfxGeE7fgvbkFTSpf0gAhFyc7KwQ-RC-ymtedB-FK4-PcqdCA9SQpbFMfl0PoPUgAm8X84z3sknUoPqyQk8JigZLHRXHXVSK4Zqej3cTMm8_XPI3e_QzHtLfuRiMLdpxfeWRO8cYP2N9VWlKiBLgp_mRfpaoFqY8yfptR2vCQkQZTcCJNmng0A7rosgtXj_odwKshJsL7ZoOnyL0n3xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
از عجایب روزگار اینه تو مراسم بزرگداشت فردوسی نوحه پخش کردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/alonews/120381" target="_blank">📅 16:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120380">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256a5b96d9.mp4?token=nFA61o59H7UYQbX2XeRhCQQWwGOZIrbLGmwMhMsTTl-KXulwFhbxbO33nDosw-lJL87JQ_OhVBczm6GQx9hwgGr7PdGehrjaY1WpmYQwYXYxUR9BhxRLWIeJgrki47MLrZfjQiVrmex3FFc1U1DecgQzKOUCcOQIoombvJDgN1fHDQwP6iHUex-TyQfJSQmr_iWzwfJpZJTPaPPRy6XO0anYoIRjnC81cuM4SdS7GsKw2H_C99JLfNQQEofXpIXPRiw7eXZQiB_f_wBJB1JMF_nuVKETe6kCLtFrytg33onaCq_T1UbE-ItFQMmWj9YtcVXrX7CLMbWjWC2zK5o3SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256a5b96d9.mp4?token=nFA61o59H7UYQbX2XeRhCQQWwGOZIrbLGmwMhMsTTl-KXulwFhbxbO33nDosw-lJL87JQ_OhVBczm6GQx9hwgGr7PdGehrjaY1WpmYQwYXYxUR9BhxRLWIeJgrki47MLrZfjQiVrmex3FFc1U1DecgQzKOUCcOQIoombvJDgN1fHDQwP6iHUex-TyQfJSQmr_iWzwfJpZJTPaPPRy6XO0anYoIRjnC81cuM4SdS7GsKw2H_C99JLfNQQEofXpIXPRiw7eXZQiB_f_wBJB1JMF_nuVKETe6kCLtFrytg33onaCq_T1UbE-ItFQMmWj9YtcVXrX7CLMbWjWC2zK5o3SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شلیک رگباری در پخش مستقیم صداسیما
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/alonews/120380" target="_blank">📅 15:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120379">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dsMnvoBljQPIWfG3zp54CXziMUiup46vJXuZqMJyDaRsw-1ldUcwSSNsZN1GjGg35p50rjIw6sROXrRGTxRJY6-TfxUrqUtkpPuXyyeimwT14StycbVrN_KSdP-eOQYN5aaLuX6nKEb_kuq8iJAI70CEfWPguj5S2YHIwhpLS5SKB8tQ6ky2bnkOv4bg1NKnCXxG4Uyaz063Ako1Fi6_Ct9sy4Pwba8C4U1stamiZA_lAPU0hSmWsJ-_ATaaNZu8bwlg8PrxNo5dHEJROR_s7J49zVMygtyWbfATUyRD9y68OJxmApJ1sj3Gbk4wQNATvT9AZRhzJrGJsEBOmfZcyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اردوغان:
مطالبات ما روشن است. ما اف-۳۵ ها را می‌خواهیم
🔴
همکاران ما به تماس‌های خود با همتایان آمریکایی‌شان ادامه می‌دهند و امیدواریم نتیجه مثبتی به دست آوریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/alonews/120379" target="_blank">📅 15:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120378">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OnocWhzMiJoZfZ9kyfuEveNWO8aA5xHkJGNPW8wrTObWfVXAlP9n1bQKdl-32KJIlRmrWTuQROhSSxEFpvrPOsXc8rrFgQ3LITVjNQ6TazFeAF8S4xEt67tJusyQq72K3gWAQGCP-ZLCO7UJ0rE9OY4f37ncOPTv_GUH2xzmPJsK-ftpdqAZEdSDesw1CaeLJgFV1BkevZ5ZUA3Q-CEiumm1ENnaCOWgn3GKA7s4Hwwo1vIVslemLEwgmPh-Jk-wk1J6FGWXhSzAonrWrhwPJhbEl8nQS1VJT6A_TTIrt5f0xBg5I_2INATxiMiL9z_18jukSMXsomk1Xv5_YXM7xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۱۰۹.۲۶ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/120378" target="_blank">📅 15:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120377">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
فوری/شبکه ۱۲ اسرائیل :
اسرائیل در حال آماده شدن برای یک جنگ چند روزه یا چند هفته‌ای با ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/alonews/120377" target="_blank">📅 15:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120376">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">⚠️
توجه
⚠️
بچه ها فیلترینگ خیلیی شدید شده همین الان که اینترنت دارین حتما جوین بشید و از کانفینگاش استفاده کنید که موقع قطعی خیلی به کارتون میاد
⏬
https://t.me/+WgqzouUHJ1U3OTY0
https://t.me/+WgqzouUHJ1U3OTY0
https://t.me/+WgqzouUHJ1U3OTY0</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/alonews/120376" target="_blank">📅 15:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120375">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
جاده چالوس از فردا به مدت ۴روز مسدود می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/alonews/120375" target="_blank">📅 15:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120374">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
دقایقی پیش وزیر کشور پاکستان برای دیدار با مقامات ایرانی، در سفری از پیش اعلام نشده وارد تهران شد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/alonews/120374" target="_blank">📅 15:23 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120373">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2GBFJN0ytOepQBeSgIR1fCnrERTQ-V1WMevbomIIOuM2XYlYysqOiOxesRHQSZ6lmpmPuBN4iT8wnX1MgocDQrf-tL48Vl4autfVwLFZpwksP4Zt7D6NjDP8F7-PGmlN7fqjZ2LPqEClN4sXfIB9Ac8hta4hobG8sBO4KcJSDE9yLUvpTdCA-K8kh8AuBJc6kUdqP9QporxCBNHouTbH1XrAcVFtZ2eLnElhvJpGNnhq7TsaDrpl6R0KmjK_L_UpPIecFqB7E06mlKfKMt8e7gSRwQV4Oy0x_3h0d-7dM6L3SBuLLbdEB316R2lDrpBDnNkqf8DiNYRcED4v7I7IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مخبر: این خویشتنداری همیشگی نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/alonews/120373" target="_blank">📅 15:11 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120372">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
ارتش دفاعی اسرائیل اعلام کرده است که حملات به سایت‌های زیرساختی حزب‌الله در چندین منطقه در جنوب لبنان را آغاز کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/alonews/120372" target="_blank">📅 15:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120371">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
دقایقی پیش وزیر کشور پاکستان برای دیدار با مقامات ایرانی، در سفری از پیش اعلام نشده وارد تهران شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/120371" target="_blank">📅 15:00 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120370">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی مجلس :
یه سیستم طراحی کردیم که رفت‌وآمد کشتی‌ها تو تنگه هرمز رو با یه مسیر مشخص کنترل کنیم و به‌زودی هم اعلامش می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/120370" target="_blank">📅 14:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120369">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
به گزارش کانال ۱۲ اسرائیل : ترامپ بزودی با اعضای کابینه خود جلسه اضطراری برای پایان دادن به اوضاع ایران برگزار میکند ، حمله و تقابل سوم قریب الوقوع و بسیار نزدیک است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/120369" target="_blank">📅 14:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120368">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
الجزیره: وزیر انرژی امارات می‌گوید خروج از اوپک یک «انتخاب استراتژیک مستقل» است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/alonews/120368" target="_blank">📅 14:41 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120367">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
از دقایقی قبل سوپراپلیکیشن بله با اختلال مواجه شده و کار نمی کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/alonews/120367" target="_blank">📅 14:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120366">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdMXzPeXP7c-9wgefCABkwnw2Vso4_h9BL3_i3ZiisM-TMhWX_uOCSFcvgU7rawsgbfVinZvSUEl63oDYhsv132ygsOnDrLYYBeXjYseOgdK3nVrVpOQHkWNGPl3sUo031cDR85QiCku_PI5BHc6Sboq9JfiutsiAFyHa5FI2VIyTWlSjaOG7dZfept_DY6MYoaWkIHowqTBMbn8QQYH7qfoSaXFjj9GchwJf6pY4pxDgtVE-DqphDpUitt0mUB6RT1t2HuIpyctwpQxNaNDQh7urbLXYFMnIXy014KmV7D2VvtpDfrVqXRqFY7vHzXxkCwEOtU8BGWNPKgwBWvsPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فارس مدعی شد: یک نفتکش غول‌پیکر چینی که از تنگهٔ هرمز عبور کرده بود، خارج از خط محاصرهٔ آمریکا رویت شد.
🔴
این نفتکش پیش از آغاز مذاکرات رئیس‌جمهور چین و ترامپ درحال عبور از مسیر تعیین‌شدهٔ ایران در تنگهٔ هرمز در کنار جزیرهٔ لارک دیده شده بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/alonews/120366" target="_blank">📅 14:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120365">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOwH0iuGkgXCwiYSx5BWLvn4bVKL7MHY1AypwAHP387lWCeASEW24H6e9pfQIixxr0bmr46Y6pqYaNw_FgICv6UX28r-XdZ09wamP9U7yxGL2XZL4kb0kidjvU6OaLHOiF9iyyPBIScVPbank_-C0I7qtyS3NSvlhdqMrZjVumbYXDHVPkM54nIh51fv94dbMDCBMG2OuPHP1V0BujkIk87CMB0zGkCUpEYR5nRkQ70xAVJZLy5x2FgHz4AQWfwyr6jl2Bp-5E_3pKtRTvGP_z434oyV8eUjvT_Bu-xF-IgbzuI9Za5HzafTbnvqUvTaocXKU64FXKxvGkCa7SZTOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ناو شارل دوگل فرانسه، خروجی خلیج عدن - ورودی دریای عرب دیده شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/120365" target="_blank">📅 14:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120364">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
فرماندهی کل نیروی دفاعی بحرین : برای حمله احتمالی جمهوری اسلامی، تو آماده‌باش سطح بالا قرار داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/120364" target="_blank">📅 14:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120362">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
فوری / شبکه فاکس نیوز: ارتش آمریکا درحال آماده شدن برای دور جدیدی از درگیری های نظامی در ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/120362" target="_blank">📅 14:23 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120361">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
امارات مدعی شد: خروج از اوپک و اوپک‌پلاس نشانه اختلاف با شرکا نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/120361" target="_blank">📅 14:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120360">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
یک مقام مطلع نظامی به نورنیوز: در صورت وقوع جنگ، اهدافی که قبلاً مصون ماندند این‌بار در تیررس‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/120360" target="_blank">📅 14:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120359">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
سی‌ان‌ان: مشاوران ترامپ خواهان پایان فوری جنگ هستند؛ فشار اقتصادی رای‌دهندگان را نگران کرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/120359" target="_blank">📅 13:51 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120358">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
مهاجرانی: نگاه دولت به اینترنت دسترسی برابر برای همه شهروندان است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/120358" target="_blank">📅 13:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120357">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
وزارت دفاع اسرائیل می‌خواد برد جنگنده‌های F-35I رو بیشتر کنه - DefNews
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/120357" target="_blank">📅 13:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120356">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c1198d606.mp4?token=DJkwlSBVW9hjWcs9Dv2WGky4D_9kjqFcsXI3Ikw73wPehaN_XIhOpDds7nSlr1M3Vg_f813cgaluwyJf4rfn2Nu2_Ct2oqbr7WjtheUdOM0JHEKyVcSidxRxka_pWiy2tUjGl7_yfeKanuRi8o28rMJDuWPOneBVHPO90T17hoenteiXLOJBMqIDiSBbuBQtuDrcyUK_gcYXJ3uQFK7Hs7hYanmIAXj0x-K8tGtTFGzQNBjUCYklJoRI_uQlqC3u5Y8ugVBpjCatjYDyV7vJXoXEdsfk5uO8hzd0vQgqepmT_LDp7BjdK128DJ2JfmkLsFV5CFJq0nFYXR8prySwzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c1198d606.mp4?token=DJkwlSBVW9hjWcs9Dv2WGky4D_9kjqFcsXI3Ikw73wPehaN_XIhOpDds7nSlr1M3Vg_f813cgaluwyJf4rfn2Nu2_Ct2oqbr7WjtheUdOM0JHEKyVcSidxRxka_pWiy2tUjGl7_yfeKanuRi8o28rMJDuWPOneBVHPO90T17hoenteiXLOJBMqIDiSBbuBQtuDrcyUK_gcYXJ3uQFK7Hs7hYanmIAXj0x-K8tGtTFGzQNBjUCYklJoRI_uQlqC3u5Y8ugVBpjCatjYDyV7vJXoXEdsfk5uO8hzd0vQgqepmT_LDp7BjdK128DJ2JfmkLsFV5CFJq0nFYXR8prySwzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده‌های جدید "MiG-29" سوریه رسماً رفتن تو عملیات و دارن برای دفاع از حریم هوایی سوریه پرواز می‌کنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/120356" target="_blank">📅 13:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120355">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
یک مقام ارشد اسرائیلی در گفتگو با کانال ۱۲ اسرائیل: تل‌آویو در حال آماده شدن برای یک جنگ چند روزه یا چند هفته‌ای با ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/120355" target="_blank">📅 13:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120354">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
ترامپ: ۵ بار با ایران نزدیک توافق شدم، ولی روز بعدش زدن زیرش
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/120354" target="_blank">📅 13:24 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120353">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
حدادی، عضو کمیسیون صنایع: گران شدن خودرو توجیه فنی ندارد/قیمت‌ها باید به قبل از جنگ بازگردد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/120353" target="_blank">📅 13:19 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120351">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/alonews/120351" target="_blank">📅 13:00 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120350">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVarzesh+plus | ورزش پلاس(K_B9)</strong></div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/alonews/120350" target="_blank">📅 13:00 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120349">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
فوری / ارتش اسرائیل : عزالدین الحداد فرمانده گردان‌های القسام، همراه با محافظ‌هاش ترور شد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/120349" target="_blank">📅 12:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120348">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
وزیر جدید نفت عراق، باسم محمد، اعلام کرد که عراق در ماه آوریل/نیمان ۱۰ میلیون بشکه نفت خود را از طریق تنگه هرمز صادر کرده است.
🔴
وی توضیح داد که عراق قصد دارد با سازمان اوپک همکاری کند تا تولید و ظرفیت صادرات کشور را افزایش دهد و افزود که بغداد هدف دارد به ظرفیت تولید روزانه ۵ میلیون بشکه دست یابد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/alonews/120348" target="_blank">📅 12:34 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120347">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
سنتکام به نیویورک تایمز : کشتی‌های ایرانی رو با ماهواره و چند روش دیگه ردیابی می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/alonews/120347" target="_blank">📅 12:30 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120346">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
منابع پاکستانی: سومین کشتی گاز مایع قطر با عبور از تنگه هرمز در کراچی پهلو گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/alonews/120346" target="_blank">📅 12:17 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120345">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
قطارهای چین به ایران سه برابر شد
🔴
با وجود محاصره دریایی آمریکا، قطارهای باری چین به ایران از هفته‌ای یک بار به هر سه تا چهار روز یکبار رسیده‌ است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/alonews/120345" target="_blank">📅 12:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120344">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
سخنگوی وزارت کشور: از نمایندگان مجلس توقع داریم در اظهارنظرهای خود در موضوعات مختلف بیشتر دقت کنند؛ انسجام ملی باید حفظ شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/120344" target="_blank">📅 12:06 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120343">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e175bcbc6c.mp4?token=mhrpRBS8HulmpY4YvfDVhnzBf7f25r8q-whK0jk4jqzFLlp6jw2jzmnUmKuSNNW90zu-azM-PqN7HFCE-T8lXKvyS0oCnbHRzZyg9bBTXOBmQHO5mXu5VPSk9Psw6AkfKU2y0WolXv4b45L3x4gQcM7fy5oS4sJgbbJjyBx5DNQ16lYlbxDbUhL6X27yENUThEx8HDxbmN8yQTN2VoJKTwQJz3c54kXowSihtMx1-Ev2cCHxD9026Y55zxw_HsN6BIFaK2B0r3zhWa-tc2qX3nPA2WplHEeNARiPnXrwMZv7SxonbvGkC4PTZPzqMConJ3bsFnyiQKrSZBPeK-CnVg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e175bcbc6c.mp4?token=mhrpRBS8HulmpY4YvfDVhnzBf7f25r8q-whK0jk4jqzFLlp6jw2jzmnUmKuSNNW90zu-azM-PqN7HFCE-T8lXKvyS0oCnbHRzZyg9bBTXOBmQHO5mXu5VPSk9Psw6AkfKU2y0WolXv4b45L3x4gQcM7fy5oS4sJgbbJjyBx5DNQ16lYlbxDbUhL6X27yENUThEx8HDxbmN8yQTN2VoJKTwQJz3c54kXowSihtMx1-Ev2cCHxD9026Y55zxw_HsN6BIFaK2B0r3zhWa-tc2qX3nPA2WplHEeNARiPnXrwMZv7SxonbvGkC4PTZPzqMConJ3bsFnyiQKrSZBPeK-CnVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: نام افرادی را که در نزدیکی اورانیوم های غنی‌شده ایران هستند، می‌دانیم. پنجاه درصدشان اسمشان محمد است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/alonews/120343" target="_blank">📅 12:00 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120342">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQPFfMyRnlpLOS1j4Wrwct1KtUIs5si9waQcyif0X7izPLuNfbjtXNyLYXDX51JbNcyaOOGmSQ-egrX6f_8oN9PkKKCtLd_6pr7k8EySTznZXZbfLSDTStOfj_fCpcxqKWhHSbhSvVTs3ReqEI_hSD7oRFES-ilSRu2YyckXnUsN2IojyVtn1RqhLaxjA46tIHT2ciuSmQyzcy84yW9_tphEMSW5c6SXO6sHhPNmmD_GNIi0kxb5Gw9-FwBVZ2DuU8EXeuqZydM5vGFMo202WQexejYWPV0MxpsMLjIUUYxnjIVsVl1z-aOYYhqDsILR8l1We-jxTOgbP7Sho8d8GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پراید هم رویا شد ...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/120342" target="_blank">📅 11:54 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120340">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rren5iiHYOJYbtp7jtTkeIbVavWYri2_BMfq0VSG26vrC5_V5k1aBQ_zBpwvzx8OWha50R0Q2PHv_h8LWGdawuU_vMFeqhum2ph5QggMVnnfuN_F_e34IELhQgEoAP5dn5KupjCG_eyzJRdSeSvJuKp4NtOOND57LguYuXJH64VxPaWUfZsj3SoMNTeAIJ6bASFzIRMdAsAMF2Oa_UDodin9o-4VjheBogHYuIS3st1jjgewgNEH9GuiRFTIZODD4xBqSL6-mYAEB4M-fmjwyse_SQvC0qN765kx430cQ-S7ruoYvSgc_HJFA0Jw403B3xzOKJ6NLziJxfXhdfnexg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cvN9LQx38hFP9rg2BojBw72HWkLpr1ZtN0ol8WZIXM-1nnu9uCJ5rpaz0EmzezV2N7di3GTusbSNJv-17WfGiCSxeqNcEytvKd_W5FUt6TRFQAgVP9EDK3Tibf5j7BKzDN5853JvnzvSireIlso5x4HYypbE7iYV7m2LHbmh9x851b_L22a27IGTYcyuO2zXqbaAUYRxVznaddIq6V8TtR5DpBgNzn8POdI2B3rfnNfOQQNdHxuc6lPsLVKuyGoHcWgcOgFwpG64GqbDnEg8VY6JypjX3aMU3Hw6wqzv_H0oU2OVj2G8RvHk4Xr2EncF9l7Zm9MrDYVmICx8vZCYdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ارتش اوکراین بامداد امروز با استفاده از پهپاد های خود حمله‌ای به یک کارخانه شیمیایی در منطقه نوینومیسک انجام داد که این کارخانه به طور فعال مواد منفجره را برای صنایع نظامی روسیه تولید می‌کرد و همچنین کارخانه صنایع فلزی متالیست پلاس در نابورژنیه چلنی روسیه نیز مورد حمله قرار گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/120340" target="_blank">📅 11:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120339">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O20O1L1WsWwfF3Mjc3dtPTMVvqDSBHBP7EtwiAP1DkMV6Ps_hpmo4IGBUpxESfOLzFc2qsnFXf_K517ZkZIZA98OjveZiDtsf4J-ZtEw26HeRWMSIWab4qalExO8siefUrGbUJlbcOaC_dSZl89g6n3m2onhjRT5hXcmJAgGZnwrr8Fk0kcGWD3Z_tEcjMkBRJQP22v0PHaa30OPl5MZMe4wn0VcXxscyRzOw1jQB2bTzJCg9SAbGo3aoA3AtaMZI7gf2d-2Q7fCmhmu_dt-NSFy4EF7nv-l31VXELDjb3R8ybXF4zfAi6u5ccWKYtoQlaeoHTJDTS_fnMDmoOF0iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تایوان به ترامپ و چین پاسخ داد: ما تابع پکن نیستیم
🔴
پس از آنکه ترامپ بعد از دیدار با شی جین پینگ گفت دنبال استقلال تایوان نیست، تایپه پاسخ داد: «تایوان یک کشور دموکراتیک، مستقل و دارای حاکمیت است و تابع جمهوری خلق چین نیست.»
🔴
این پاسخ نشان میدهد تایوان نمیخواهد در معامله بزرگ واشنگتن و پکن، فقط به یک کارت مذاکره تبدیل شود. ترامپ با احتیاط حرف میزند تا با چین وارد درگیری تازه نشود، اما تایپه هم میخواهد روشن کند که هویتش را با سکوت دیپلماتیک دیگران تعریف نمیکند.
🔴
برای پکن، این جمله تحریک‌آمیز است. برای واشنگتن، یادآوری دردسرساز است. چون هرچه ترامپ بخواهد پرونده تایوان را آرام نگه دارد، خود تایوان نشان میدهد حاضر نیست استقلال عملی‌اش زیر سایه توافق‌های پشت پرده کم‌رنگ شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/120339" target="_blank">📅 11:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120338">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">قیمت استثنایی گیگی
2️⃣
2️⃣
2️⃣
تحویل زیر یک دقیقه
✅
دارای لینک سابسکریشن جهت دیدن حجم و کنترل مصرف
✅
بدون قطعی
✅
بدون محدودیت کاربر و زمان
✅
جمینایو چت جی بی تی و... کامل اوکیه با سرورامون
✅
🏪
پشتیبانی کامل
✅
شروع فعالیت از سال 2022
✅
پرداخت ریالی
✅
ضریب و این چیزا…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/alonews/120338" target="_blank">📅 11:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120337">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/120337" target="_blank">📅 11:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120336">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ls958bHLXTVKGAaBhohke8KDEPSfFTzQRzipA6iFAlZVc-RKwRN27Gl3L-HUGhDdBDvzabZwO7_fGDIK1_lSJ24Fq68BixkSZeUj1o2BOLf6a4Opmxj7upkt-xlFb1A1BsgM5789oBLz02NSNYK39mphRuYK2n2UEXO-7jSOBKbQxqHGggIUWQ4ecWpPIYaV0xy31ywWT02sSoFYvhFn5cbxIQnK6l8gpZl2HWQIqTmFv7gBH0CwyPd9eHWhNjPN9lpcdUavZ9J0eiLwtLrKi-rAgUJaPaDC46n1CrrBrDma30tSVXVu6M-tfdag7BrH1bHnOS2wNojWQ-U-gR4meQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دوستان این تبلیغاتی که پائین کانال نمایش داده میشه کلاهبرداری هست و توسط خود تلگرام انجام میشه و از دست ما خارجه
🔴
به هیچ عنوان اعتماد نکنید چون سرمایتون میره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/120336" target="_blank">📅 11:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120335">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
انفجار ناشی از امحای مهمات در دزفول
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/120335" target="_blank">📅 11:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120334">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2mhTc-JUgbIrorzKoMYvfhtP_N6rGJOO85-7610FcCNN81iJZhDVKHltUF3pNtj0YTShts9Rn5usmfvF3UdyCY6lX6gyU8fnszZJ6nVZSC-5nfI2VcWEL8KL20kRVPTDBVxCWJ2ctzfpcSf7CGvUPwCki9I5Um_Qtyf4ITKRs59mheWmEl3pwfbT4WEYYj1csGZiyuPGt-1Jq7GlCJP5DsHFosNNLk697jz0tG-aveb6B2MMET4dzCGtbbzOAHsf0krmFlq8JuJ-8cpdbjULJ-jSMnh_3QS0_EZbKc-YJVCufC0gPHlg299e3ZKog8uHsPBcVczwGlnV9rdZTu_GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استثنایی گیگی
2️⃣
2️⃣
2️⃣
تحویل زیر یک دقیقه
✅
دارای لینک سابسکریشن جهت دیدن حجم و کنترل مصرف
✅
بدون قطعی
✅
بدون محدودیت کاربر و زمان
✅
جمینایو چت جی بی تی و... کامل اوکیه با سرورامون
✅
🏪
پشتیبانی کامل
✅
شروع فعالیت از سال 2022
✅
پرداخت ریالی
✅
ضریب و این چیزا ندارن و تا آخرین مگابایت برای پشتیبانیش درختمتیم
🥂
⭐️
@Napsternetiran_bot
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🔶
@Napsternetvirani</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/120334" target="_blank">📅 11:19 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120333">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ارگان رسانه ای وابسته به سپاه نوشت: وزارت اقتصاد طرح مدیریت تنگه هرمز از طریق بیمه را پیگیری می‌کند تا امکان مدیریت بر تنگه در پساجنگ مطابق حقوق بین‌الملل فراهم شود و برای ایران آورده اقتصادی نیز داشته باش
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/120333" target="_blank">📅 11:16 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120332">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
الجزیره: برق کوبا پس از خاموشی گسترده دوباره وصل شد، اما بحران انرژی همچنان ادامه دارد
🔴
برق در سراسر کوبا روز جمعه پس از خاموشی‌های گسترده دوباره برقرار شد، اما بحران انرژی این کشور با کاهش شدید ذخایر نفتی همچنان ادامه دارد.
🔴
شرکت ملی برق کوبا اعلام کرد که پس از قطعی برق در ۷ استان از ۱۵ استان، «سیستم برق ملی دوباره برقرار شده است»، با این حال قطعی‌های برنامه‌ریزی‌شده ادامه دارد و نیروگاه‌های قدیمی هنوز در دست تعمیر هستند.
🔴
وزیر انرژی، روز چهارشنبه اعلام کرد که ذخایر نفت کشور «تمام شده است». کمبود انرژی خشم عمومی را برانگیخته و شهروندان هاوانا با کوبیدن قابلمه و ماهیتابه اعتراض خود را نشان دادند.
🔴
کوبا کاهش انرژی را ناشی از تحریم‌های آمریکا می‌داند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/120332" target="_blank">📅 11:13 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120331">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
آسوشیتدپرس: بازگشت ناو هواپیمابر جرالد فورد به پایگاه پس از ۱۱ ماه مأموریت
🔴
وزارت جنگ آمریکا اعلام کرد پیت هگست، وزیر جنگ، روز شنبه در پایگاه دریایی نورفولک در ویرجینیا از ناو هواپیمابر جرالد فورد و ۴۵۰۰ ملوان آن پس از ۱۱ ماه مأموریت استقبال می‌کند.
🔴
این ناو ۳۲۶ روز در دریا بوده که طولانی‌ترین استقرار یک ناو هواپیمابر آمریکایی در ۵۰ سال گذشته و سومین رکورد از زمان جنگ ویتنام است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/120331" target="_blank">📅 11:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120330">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
کپیتال اکونومیست: قیمت نفت به ۱۵۰ دلار در هر بشکه خواهد رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/120330" target="_blank">📅 11:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120329">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
نیروی هوایی اوکراین اعلام کرد: 269 پهپاد از 294 پهپاد پرتاب شده توسط ارتش روسیه را شب گذشته سرنگون کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/120329" target="_blank">📅 11:04 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120328">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
نیویورک تایمز گزارش می‌دهد که نیروهای نظامی آمریکا "در حال آماده‌سازی برای دور دیگری از حملات هستند... این بار با شدت بیشتر. این حملات ممکن است از روز دوشنبه آغاز شود. اهداف نظامی بیشتری از ایران در نظر گرفته شده است که شامل زیرساخت‌ها نیز می‌شود."
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/120328" target="_blank">📅 11:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120325">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HAFG02CbZxF8lKCt8mtm6MKo4gMgyN-24FH8Q4hmroDooKiKLwFQT7n465oCLKrqxi9bintqMaKgrMKAIj3Cshq9hxNoE8UDKo4ItWbBWw1U_TbxJgyBzcAPUgnSUoDXgwvscui4MNveXa9V8GG-fpvYULEwCMC9xS3NL9uXvpxm0yUJ8QnLHustJFEeb1I8xIXWR8rM1HVM4MksyRS7SjESQhAa44J_b-g6RN7Es5gBarkFv0mckdf9aBoGjAPBAXHFeBTN2h6HAhG7qwFbw1595kmY8XEKhPQCu1XtAwhR8mucUFk3WYLMy_Iz8hiqzb7yIxSBd06fubn3pnSw8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o-THk5kZSDcyfINTrEtr161BcA1vXe9OQRqvRHYMRou7aqAcsIEumI0kG3CmtQDUce8TuF75-j2rm2Eu-VZzgZ1Q5wD2LRky1oz4_rP8vZucbL8LdHcFhiVONVz7afvJsC6wUubCvyFWjKRJXKGelguQhAYFSh9pGNWM477-3eKY2ypIa-vfIa_QgFxoGsm4PdxQhT0HlGqzEMzGdCpCWXcMxvOsoqmIPGRMua6qbKq1Q61j--RzBx4TByapBUc_uMAnAa1L566-z7UlMIaLD11-IcVHfH2f2sKUnYXleJl1G6S_Z_AS66Vce9VS6HaLXDhr-g2wRAAdoElKSQ6hXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dTDXgbAB9kFi6WqCdK0-wMU6wKq0Dku2DmI_ZI1hpt2WeVcBuYXmS41smvEm7JOhpj3o8UPe7VRiQsP8wqa7_TW3Hw4_YQoszcsZbaOrgMBeOgr0wkaKzIl-VsIt3jniIqfkdiMO50vtRTiqug7g48xJTz-hOifHbTRTSTIdCsao8fLzKO9cwf8q-4BOKiUFiXDTlqg0gqaVRAJPjkVsoA2cRUTSX7A6pnN7oDeTDXTscWfeeRbOweylbb2kWgu4SfUewZ7y4jNHJEk_rtK02mIHbWCBH8sSlmYeFPKZ3Qu2TtS8nzxS1iYJjTCQna7uK6gS6qHXQZgDCiBg3CIqbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
شب گذشته در بسیاری از برنامه های صداوسیما، مجریان با تفنگ حاضر شدند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/120325" target="_blank">📅 10:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120324">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a78a5c4a5a.mp4?token=uml108V9Um0ehOcVz2ukgSRV3usIyq5a6e4tyKUpVQZMsF9JH7a8DBQWvksGwBYhniQ1hICSPfBDBqSrIJFgR4MioIzvJRKipeILCpE-7K9C_ZomboKe6kVum_9to8di4PQuFl116ukNXQKGAGm1Q5cvZExOH4mnSol5QnZaAgtYdK43fJCm6NNQLnv3_UV8VviolseXEO_tIgwt-UbDHAba-qYA2I5HfAD6SJ8ln4L6hBz2jqJrIT7huR0WKX1hZiMp6umppI3cPgRLpqUnkW_InKxYJOWB0z1gZX1euSMN-gSsAvVKrRNo0CAMAG959Z0VyDPHmLz3Q5M2HxwwwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a78a5c4a5a.mp4?token=uml108V9Um0ehOcVz2ukgSRV3usIyq5a6e4tyKUpVQZMsF9JH7a8DBQWvksGwBYhniQ1hICSPfBDBqSrIJFgR4MioIzvJRKipeILCpE-7K9C_ZomboKe6kVum_9to8di4PQuFl116ukNXQKGAGm1Q5cvZExOH4mnSol5QnZaAgtYdK43fJCm6NNQLnv3_UV8VviolseXEO_tIgwt-UbDHAba-qYA2I5HfAD6SJ8ln4L6hBz2jqJrIT7huR0WKX1hZiMp6umppI3cPgRLpqUnkW_InKxYJOWB0z1gZX1euSMN-gSsAvVKrRNo0CAMAG959Z0VyDPHmLz3Q5M2HxwwwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو: چین کاری را انجام می‌دهد که من اگر رهبر چینی بودم انجام می‌دادم. آن‌ها تلاش می‌کنند در تمام این صنایع کلیدی آینده بر جهان مسلط شوند.
🔴
شاید ما از آن خوشمان نیاید، اما این همان کاری است که آن‌ها انجام خواهند داد زیرا به نفع بهترین منافع خود عمل می‌کنند. ما نیز باید به نفع بهترین منافع خود عمل کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/120324" target="_blank">📅 10:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120323">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e012e3f1b5.mp4?token=vkJkBCQRS9YpZ8NXVzfOQ7HZdLjMXY7FSqsNlqqdvW3_7AYxbq8vCWWl7-pB0TVeKjox6fV3LMYXuAPUl25vIJTVpoCo5vyKsqI4UKVTm-n9yciRbA5Bu5yxAclkyDxYfx__pCYqerwRLkCj1REku_gHJuOnm_n0qdWRQdkJW7eQ283lcEqUL3KiHBCXAUb6Lh10aDWnR5TvQEJbjwYDs-pXDFVjT6qDdY8cvxTQqVNyipCb94fZN6mYRYgzRJpgGhS7PzDN9kO0qmPX1OyGqwjReGKBkjFJN-pzdvg3oVjV5_Yl6R4AxVb_YFumYrFD8bmx2j1s6ES5uMU_xk6Rag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e012e3f1b5.mp4?token=vkJkBCQRS9YpZ8NXVzfOQ7HZdLjMXY7FSqsNlqqdvW3_7AYxbq8vCWWl7-pB0TVeKjox6fV3LMYXuAPUl25vIJTVpoCo5vyKsqI4UKVTm-n9yciRbA5Bu5yxAclkyDxYfx__pCYqerwRLkCj1REku_gHJuOnm_n0qdWRQdkJW7eQ283lcEqUL3KiHBCXAUb6Lh10aDWnR5TvQEJbjwYDs-pXDFVjT6qDdY8cvxTQqVNyipCb94fZN6mYRYgzRJpgGhS7PzDN9kO0qmPX1OyGqwjReGKBkjFJN-pzdvg3oVjV5_Yl6R4AxVb_YFumYrFD8bmx2j1s6ES5uMU_xk6Rag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روبیو: اگر جی دی ونس کاندیدای ریاست جمهوری شود، اولین نفری هستم که از او حمایت می کنم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/120323" target="_blank">📅 10:30 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120322">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
روزنامه عبری هاآرتص: چهار ماه از ایجاد «شورای صلح» برای نوار غزه می‌گذرد؛ تاکنون طرح ترامپ اجرا نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/120322" target="_blank">📅 10:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120321">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
ترامپ: نفت ونزوئلا ما را ثروتمند کرد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/120321" target="_blank">📅 10:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120320">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEoJr2epALS8dnvzsVzDQ-_LLbL4DsESy-YQ7Zgb3dw1Y1KU5WkqtH0QQ4xoKlbsY70ukmkiihcz0XZGEN_hHNISBmEf1TEL18pG725G65dLZfU4NkKa60UFlrfUtdbz3yf_w8p-34T7kphfNH4WQ4B4YyY3szvkCJmoqcmbMGw6HlsApSg7x7VgYk9LE8RfBD-xbQO-CFvyoAQhOjOhADKkxYKrKew71K8GPAfl2bKXF8T6HkmRiB5IA61-tCpr7ASQ7QB3ny2ych0zPjfStzeP4h6kBA7bYowz7FxtUiDXFLs_guw-ygxlramsPQ9rbWs9_zxKY45Do7iXZa8lcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری مشاور قالیباف در اینستاگرام
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/120320" target="_blank">📅 10:24 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120319">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
وزارت دادگستری آمریکا با صدور بیانیه‌ای، مدعی شد «محمد باقر سعد داوود السعدی»، شهروند عراقی و از اعضای شاخص کتائب حزب‌الله دستگیر شده و به ایالات متحده منتقل شده است.
🔴
وزارت دادگستری آمریکا افزود كه این شهروند عراقی در برابر «سارا نتبورن»، قاضی دادگاه فدرال در منطقه منهتن شهر نیویورک حاضر شده و او دستور بازداشت را تا زمان محاکمه صادر کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/120319" target="_blank">📅 10:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120318">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
سی‌ان‌بی‌سی: ترامپ چند هفته قبل از آنکه به طور علنی سهام شرکت هوش مصنوعی Palantir Technologies را در شبکه Truth Social تحسین کند، سهام این شرکت را خریداری کرد.
🔴
سوابق نشان می‌دهد که ترامپ در اوایل سال ۲۰۲۶ بین حدود ۲۴۷,۰۰۰ تا ۶۳۰,۰۰۰ دلار سهام Palantir خریداری کرده است، از جمله چند خرید در ماه مارس. او بعداً این شرکت را در یک پست در Truth Social در آوریل، در زمانی که سهام فناوری به شدت کاهش یافته بود، تبلیغ کرد.
🔴
اسناد همچنین نشان می‌دهد که ترامپ در فوریه تا ۵ میلیون دلار سهام Palantir فروخته و سرمایه‌گذاری‌های بزرگ دیگری در حوزه فناوری انجام داده است، از جمله در Nvidia، Apple، Amazon، Microsoft و Oracle.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/120318" target="_blank">📅 10:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120317">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
کرملین: پوتین در تاریخ ۱۹ و ۲۰ مه به چین سفر خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/120317" target="_blank">📅 10:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120316">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
رسانه‌های عراقی از شنیده‌شدن صدای انفجار در منطقه الکراده بغداد خبر دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/120316" target="_blank">📅 10:04 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120315">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
پیام پزشکیان به رهبر کاتولیک‌های جهان: از موضع اخلاقی و منطقی شما در قبال تجاوزات نظامی اخیر به ایران قدردانی می‌کنم
🔴
حملات آمریکا و اسرائیل صرفاً علیه ایران نیست، بلکه علیه حاکمیت قانون و ارزش‌های انسانی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/alonews/120315" target="_blank">📅 09:54 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120314">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
فوووری / منابع روسی: یک جنگنده سوخو-35 نیروی هوایی روسیه، یک جنگنده F-16 فایتینگ فالکون ناتو را سرنگون کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/120314" target="_blank">📅 09:41 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120313">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
هشدار نارنجی هواشناسی: بارش‌های شدید و وزش باد در شمال کشور
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/120313" target="_blank">📅 09:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120312">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
کوبا: آماده دفاع از خود در مقابل تهاجم احتمالی آمریکا هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/alonews/120312" target="_blank">📅 09:16 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120311">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
مدیرکل مدیریت بحران استانداری اصفهان گفت: در ساعات بعدازظهر امروز تا روز دوشنبه وزش باد شدید و تندبادهای لحظه‌ای همراه با گردوغبار در استان پیش‌بینی می‌شود و سرعت باد به ۹۰ کیلومتر می‌رسد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/alonews/120311" target="_blank">📅 09:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120310">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
انفجار کنترل‌شده بمب‌های عمل‌نکرده در شیراز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/alonews/120310" target="_blank">📅 09:09 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120309">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
رویترز: ایالات متحده ممکن است از اسرائیل بخواهد میلیاردها دلار از وجوه مالیاتی فلسطینیان که مسدود شده است را به حمایت از طرح بازسازی غزه توسط ترامپ اختصاص دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/alonews/120309" target="_blank">📅 09:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120308">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1860318fa.mp4?token=JDewH6F4h9sK1MPgJJOGqbKZJKuWZES2XuLZhKS88Ir5IkjWULB7uhNGVPhA0Vj0zrzSNVUxIwltfD0plLImsNp0HrZ94xKlWcsoiOFAXJ6CQ3kZcVJPkuMl7l1KgNMC_nSJTQ4yT5OM1MgcdZgVET0RFMA-bxKJ8GMhMITqHvpi5ZhLXT5AOhnUxTN25hCyfMOzmvu29hh3AJycNieWPbtM3JFPsTljnC8CVpG6y3JYQYXTNp0oMEMXQ8kzeDB0CoQdHAGw_iSEgKLdsoK16Dob7cPaBFuT58sjwmWmXf5duLpvcu7o8V4grjjWZPC20tXSXTjha0RQmpVufPzqB5vvtzRFZotHvGeSvZNev3ezaQ_ZGu9iazTHFY_QfC4lDrAzwqEeITtp4REuFpWeJkjaRSgqJx1wqZb7mjeEdY_iHenb--s8ZIyz_1kPcW6iMk3xw2EnlBi2c5FQzGJbBhH2Up3nL1CyvvZGdap1b3d5cLxpcjkUN1qbAEUEXIwWPAyOZIA9Dr_v4RCywr3mIHDqvhq0ESuh2UWcGsalllazqnFdbUhmqQGP_iNijZsjQtqBDGZ7rA3yckUvoUJeNXsrUPqdlx9p7X1pBS6VkogUbH6zSPpmmQoKnkQI44se5GZPvBtoM2wiRWsmTI12OjL5O3tYIplO4DBMOlYT2zI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1860318fa.mp4?token=JDewH6F4h9sK1MPgJJOGqbKZJKuWZES2XuLZhKS88Ir5IkjWULB7uhNGVPhA0Vj0zrzSNVUxIwltfD0plLImsNp0HrZ94xKlWcsoiOFAXJ6CQ3kZcVJPkuMl7l1KgNMC_nSJTQ4yT5OM1MgcdZgVET0RFMA-bxKJ8GMhMITqHvpi5ZhLXT5AOhnUxTN25hCyfMOzmvu29hh3AJycNieWPbtM3JFPsTljnC8CVpG6y3JYQYXTNp0oMEMXQ8kzeDB0CoQdHAGw_iSEgKLdsoK16Dob7cPaBFuT58sjwmWmXf5duLpvcu7o8V4grjjWZPC20tXSXTjha0RQmpVufPzqB5vvtzRFZotHvGeSvZNev3ezaQ_ZGu9iazTHFY_QfC4lDrAzwqEeITtp4REuFpWeJkjaRSgqJx1wqZb7mjeEdY_iHenb--s8ZIyz_1kPcW6iMk3xw2EnlBi2c5FQzGJbBhH2Up3nL1CyvvZGdap1b3d5cLxpcjkUN1qbAEUEXIwWPAyOZIA9Dr_v4RCywr3mIHDqvhq0ESuh2UWcGsalllazqnFdbUhmqQGP_iNijZsjQtqBDGZ7rA3yckUvoUJeNXsrUPqdlx9p7X1pBS6VkogUbH6zSPpmmQoKnkQI44se5GZPvBtoM2wiRWsmTI12OjL5O3tYIplO4DBMOlYT2zI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئوهای منتشر شده در شبکه‌های اجتماعی از یک انفجار مهیب در مکزیک خبر می‌دهند که یک جشن مردمی را به تراژدی تبدیل کرد.
🔴
این حادثه در ایالت «خالیسکو» رخ داد؛ جایی که پرتاب جرقه ناشی از آتش‌بازی به مخازن گاز، باعث ایجاد یک انفجار قدرتمند شد.
🔴
در پی این انفجار، دست‌کم یک نفر کشته و بیش از ۲۰ تن دیگر مجروح شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/alonews/120308" target="_blank">📅 09:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120307">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2419fa5807.mp4?token=i1CUHnHxG9RS578IaeoryUjigLzm_7oKJISRtZdNmcMZSbVkK1eGiOEgFFIIoaObSBspBaHkJHKf0yOVQP3NmsJPCjbxV7a0VBG26urKa3Xf7QbZNvFe3vEAydb7FRHJfEX2m6QKL_wJ_Zs7zcyQ8bjX9Vq3xpkIvsnDJb9W_xJYBR31FhSOzU-QUBx13M-NrNT06S0_Jsu_QELBXhZ6BHe11BYQP0Xix09_VrCoPzo6m5-5i89mg5_q9l_JDG5-bdkhAYSatZmtZ1cgIj4ndCIGMK49y8NMjT9byVsWKqnejjdtUJpLwgV-ubu7Y2l3mnqRVqcH6jOGnDphyY4Zuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2419fa5807.mp4?token=i1CUHnHxG9RS578IaeoryUjigLzm_7oKJISRtZdNmcMZSbVkK1eGiOEgFFIIoaObSBspBaHkJHKf0yOVQP3NmsJPCjbxV7a0VBG26urKa3Xf7QbZNvFe3vEAydb7FRHJfEX2m6QKL_wJ_Zs7zcyQ8bjX9Vq3xpkIvsnDJb9W_xJYBR31FhSOzU-QUBx13M-NrNT06S0_Jsu_QELBXhZ6BHe11BYQP0Xix09_VrCoPzo6m5-5i89mg5_q9l_JDG5-bdkhAYSatZmtZ1cgIj4ndCIGMK49y8NMjT9byVsWKqnejjdtUJpLwgV-ubu7Y2l3mnqRVqcH6jOGnDphyY4Zuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بن گویر وزیر امنیت ملی اسرائیل:
ما در دوره نصرت الهی هستیم.
🔴
ما در دوره ای از آغاز رستگاری هستیم و فقط باید به راه خود ادامه دهیم و بدون توقف ادامه دهیم
🔴
در لبنان، غزه، و یهودیه و سامره (کرانه باختری) توقف نکنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/120307" target="_blank">📅 08:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120306">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/66b24dd163.mp4?token=KluH3fRMNSLNoaFB0QcTzRCxcgQBtqq2k0uTNeZypYnx8I4lY4hsBMQPq0z4HFWEGWVzUDCzLoVcChMRpZAMNy_g0-yD0h067paND8n3BqEMEJxbv6jXwIQsj9HYzd_qw1_Weavi8ZSJ-_7dBxBWngk3ujtSa87_kzgIqlnR81qd56sFnMRpRi-gsPuifq7IX_IzJY7x6PrKBBSY0OlodXoIc0nW65LPzGBvF7hgl0qH_smG7rKgAf4qMf9RfGKtE7BVa30m9cEmAdLyoOe9k-AsYjV0Vneliqt73Xu21gKRpBoyFJakStARakYo_GPyD8T97biELn_M12p9Yz8pqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/66b24dd163.mp4?token=KluH3fRMNSLNoaFB0QcTzRCxcgQBtqq2k0uTNeZypYnx8I4lY4hsBMQPq0z4HFWEGWVzUDCzLoVcChMRpZAMNy_g0-yD0h067paND8n3BqEMEJxbv6jXwIQsj9HYzd_qw1_Weavi8ZSJ-_7dBxBWngk3ujtSa87_kzgIqlnR81qd56sFnMRpRi-gsPuifq7IX_IzJY7x6PrKBBSY0OlodXoIc0nW65LPzGBvF7hgl0qH_smG7rKgAf4qMf9RfGKtE7BVa30m9cEmAdLyoOe9k-AsYjV0Vneliqt73Xu21gKRpBoyFJakStARakYo_GPyD8T97biELn_M12p9Yz8pqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
به دستور ممدانی شهردار نیویورک، ۴۰۰ موتور سیکلت این شهر که رانندگان آن ها از کلاه ایمنی استفاده نمی‌کردند منهدم شدند
🔴
به گفته وی، این کار در راستای تقویت فرهنگ استفاده از کلاه ایمنی انجام شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/120306" target="_blank">📅 08:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120305">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrtb6G9AGVZ07kcHG4pKmq1PXcnrJ2k7IeXfGBNSFuRFw5qehD1s--gNiqO4-YW5Ef-OaNh8s4eUJhaouKCXQnqHGQooE33j9_C1H8hyGQ-P2sFC43JIFJs85PJ0DgHmL1NLcM0LWtlyt1HyIJg4PqtLBOpZ1CZYh58IFodCVii8-cg3mkTC4HtDaFEiRkRB4ZcngvHSd5JTP2ekAOZujsQWkRd3BAtjRRXayEqycIgpvC4rHftv3-nwwGQ6WRUp8GDXb-8XKEPhsbaoXhnHhaTxor7cOocWeIBQUOrXa1BBFnZXlr1qINo51ueOmF0t8YW-mwnWgyslVx7XyOGkrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس‌جمهور فنلاند: آمریکا از ناتو خارج نخواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/120305" target="_blank">📅 08:49 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120304">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNxJKSr3oIE9ni9GVWyYWX3q9_T7CKTdkuk9EHUn3AlHB2r0eGEiAw1lObzfe745IB3imGVjaBqokGgIBr3KatoW5CrKi_LNHWC2omoCwPuToBSkwL6q2mkW3IkxgnL8Hb2aRP2DmnBd53yXIWr8atoE3kJWWPDDldSnzuesouMPv6bxm9Veh8CtCtceIMJqFe65DvdtIWMbwBLQ7TLAKiy53EyUy0x4FG4__RdJKl-ky0IZStKb_uRAUGNf_m9SarmwUyNXGf9vxipsN9aYUjcVU4wXSW5Psq8f7Ng1DhzkNEiSP8nMhgpCmJ65NDUhoqTvl5L99TkBz3bXEE-wZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس سازمان اداری و استخدامی: ساعت کاری جدید اداره‌ها از امروز اجرایی می‌شود و تا نیمه شهریور ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/alonews/120304" target="_blank">📅 08:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120303">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ta_JZxfn7iFR53U80XQNr9vXHYOq1qqpnlBoBPWe1OrAxGS0h0suYD6tYGGXzujnBuKXLXaDC8QKZOcJg6yhnDzfduFx54YhSq6MCFqnnKdnaIJkoWT8NHArOF_i0EFvASD74SIyvwgk6QkshVwKoCV6aaZlrv6uaNS0_3SwAaJT5b52Z8J4DRCrzzWw_jxvw5DpfQ0ID6_i7SIkuqAnWTiAuUQp_d7X9rxXFKMWQUB9G21YkQciZOVjulKEvmWDcdzpT73p5ijZRAkWjGNRSYkO1tdIUg-Y4OAdZPLfhTu4WsJfmH2HcprAiPGHuUB_B2Oiygxfj7W7cGnLlzh85Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روزنامه دیلی تلگراف گزارش داد، احتمال آن که کر استارمر نخست وزیر انگلیس از سمت خود به نقل شهردار منچستر کناره گیری کند وجود دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/alonews/120303" target="_blank">📅 08:41 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120302">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
دونالد
ترامپ
، مدعی شد در جریان یک عملیات مشترک میان نیروهای آمریکایی و نیجریه‌ای، «ابوبلال المنوکی»، مرد شماره دو  داعش را از پای درآوردیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/alonews/120302" target="_blank">📅 08:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120301">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
سفیر چین در سازمان ملل، از پیش‌نویس قطعنامه پیشنهادی آمریکا و بحرین دربارۀ تنگه هرمز انتقاد و تاکید کرد که محتوا و زمان آن مناسب نیست و تصویب آن کمک‌کننده نخواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/alonews/120301" target="_blank">📅 08:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120300">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47a9d3010c.mp4?token=SDLgv5badNwpR6Z4nMlLddsXbk_DNdj0uYNroYQ6ld26pxfJNEkRi2lNxcIZ1q_pU75WBw6nLVilNZzxxhKv6RwuZgbqjn-KegVCIu1AYn1gcEEsasY6yU9KaopxKYdFcB8eTljAowcKJNuzTaEKGSriHlYlW38GGLGOuS7O5kgRk6hg6uJXkSrw6CIPthLq3PW3UpKM1YrGljqebiuVPwTCBXEpqpsMAx0dM2ErL9d7-hjSt9z5zHpoIcutxqd5eu27SoYRy24RTEDE3bXKRuZnRFHAkVtGcwxA7M3XzmLnIJEKu01ipkmd8Uw9Roa64Ukt9fwMFZtvmTHEWid9Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47a9d3010c.mp4?token=SDLgv5badNwpR6Z4nMlLddsXbk_DNdj0uYNroYQ6ld26pxfJNEkRi2lNxcIZ1q_pU75WBw6nLVilNZzxxhKv6RwuZgbqjn-KegVCIu1AYn1gcEEsasY6yU9KaopxKYdFcB8eTljAowcKJNuzTaEKGSriHlYlW38GGLGOuS7O5kgRk6hg6uJXkSrw6CIPthLq3PW3UpKM1YrGljqebiuVPwTCBXEpqpsMAx0dM2ErL9d7-hjSt9z5zHpoIcutxqd5eu27SoYRy24RTEDE3bXKRuZnRFHAkVtGcwxA7M3XzmLnIJEKu01ipkmd8Uw9Roa64Ukt9fwMFZtvmTHEWid9Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس جمهور ترامپ در مورد ایران:
ما نه تا دوربین مختلف توی اون سایت داریم و دقت به قدری بالاست که ما می توانیم نام یک شخص را هم بخوانیم.
🔴
اگر اسمش محمد است ، بیشترشان محمد هستند ؛ شما می توانید حدود 50 درصد درست حدس بزنید.
🔴
هر کسي که به اون فضا نزديک بشه ، ما میفهمیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/alonews/120300" target="_blank">📅 02:23 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120299">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8501d1acc2.mp4?token=uMd3aK_eQcn6Vd89DtQ_ZKRC8rZ6d9mSXd9WiEvcQQBm7i1Fuk8j5u_Bu1xs6Zyp_U77yDLfmmrkQB7uBfOt6EWww9GNpxyaNmvYp6NIQptQS2vmxx9Ngst_MAjM6p8Vb5AqOsxKfjZMhwTCkSPyURIvw0CPkRd70RgapCiPA8XFC-WXM51WThn2p_Y1Or8oVT8Z_pBlLj7pmAx-h1lnPZus1hOJfqEqGP-nGYcouT_S9bp33p2v1UHEVJgIRltBz21_nzuVFuxF-WwObkG83U23npPjKIrZdipjDe9w91IeigQwRUbCENrFew1xVluh_2BUdEhlLjq6BXl3QWQ-lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8501d1acc2.mp4?token=uMd3aK_eQcn6Vd89DtQ_ZKRC8rZ6d9mSXd9WiEvcQQBm7i1Fuk8j5u_Bu1xs6Zyp_U77yDLfmmrkQB7uBfOt6EWww9GNpxyaNmvYp6NIQptQS2vmxx9Ngst_MAjM6p8Vb5AqOsxKfjZMhwTCkSPyURIvw0CPkRd70RgapCiPA8XFC-WXM51WThn2p_Y1Or8oVT8Z_pBlLj7pmAx-h1lnPZus1hOJfqEqGP-nGYcouT_S9bp33p2v1UHEVJgIRltBz21_nzuVFuxF-WwObkG83U23npPjKIrZdipjDe9w91IeigQwRUbCENrFew1xVluh_2BUdEhlLjq6BXl3QWQ-lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: گفتم گرد و غبار هسته ای را می گیریم ایران گفت: "شما می توانید آن را داشته باشید. اونا گفتن ، " ما نمیتونیم تحملش کنیم. ما توانایی مصرف آن را نداریم. گفتم: "چرا؟ اونا گفتن چون خيلي ضربه خورده"
🔴
برت بایر فاکس: چرا این کافی نیست اگر هدف شما این بود که آنها را عقب بیندازید ؟
🔴
ترامپ: از نظر روابط عمومی به اندازه کافی خوب نیست‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/120299" target="_blank">📅 02:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120298">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/013d87334a.mp4?token=r88osW5Qlyx2uVNmKgSv_BBihPx9JAPu5Uel-2wJKk2yGnYSPefwz3vhE1yo6RZlj6Hm6Mty2keT-ZdDsVKmw8dZ9Zj9mZ5a9tPJL9wSklQLdygISm90KLC8_EwSsTE6iW1k-9skMXNn7425LXOl0XG2dEsGYLI01AJ6ltrBriMZ2icIHvdigBlsJ4Ubtv6xCmQV_lxqvIsWm70E8xHg_KjhqDp9Yn8NWyLU9lXy2R-J3qTZlMnAl0S4luA5EsXLjAbQVq0pyBpG5yuE01qD8FBfSw_R7uNPce8_tlLPbxHWK3G0mUQh8nz0bi19j5HYgUHLY8MbQsAqkLcO705RGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/013d87334a.mp4?token=r88osW5Qlyx2uVNmKgSv_BBihPx9JAPu5Uel-2wJKk2yGnYSPefwz3vhE1yo6RZlj6Hm6Mty2keT-ZdDsVKmw8dZ9Zj9mZ5a9tPJL9wSklQLdygISm90KLC8_EwSsTE6iW1k-9skMXNn7425LXOl0XG2dEsGYLI01AJ6ltrBriMZ2icIHvdigBlsJ4Ubtv6xCmQV_lxqvIsWm70E8xHg_KjhqDp9Yn8NWyLU9lXy2R-J3qTZlMnAl0S4luA5EsXLjAbQVq0pyBpG5yuE01qD8FBfSw_R7uNPce8_tlLPbxHWK3G0mUQh8nz0bi19j5HYgUHLY8MbQsAqkLcO705RGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برت بایر از فاکس: فکر می کنید ایران به زودی تسلیم خواهد شد ؟
🔴
ترامپ: بله ، من هیچ شکی ندارم.‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/alonews/120298" target="_blank">📅 02:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120297">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/057506e9d2.mp4?token=i11YOhqw32iBGkfQ14mdlfhLipa8vSU4GRqlG029Qj8Y4GfzhTcSd40oGT8CKZTbl0dHv0bRFQ29QGx9FBUimsdxT9v9Ke8BrKu6Z60UrB-sm_e3IlnBndaiVSKx-nVJsh2HdAVP2xcMt8ZBdWg7VuIL7uqB06ywdfdrlNpv0h21oOL-MsMg2iwZiqP04D2EBJpLiFYXNXyJvkho5FQjl2bJpY9ATWoBMWPFpzuq0u3hjCd5w9h_LtDIggdHJiqIbeHqY-YVGc4VtmXPNUN1EwbvEqgOD2atfizgjrUerQ_LyyK0ohwRj7KZH5fofZSZEVOYehsKCYwLBDcl_OBa0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/057506e9d2.mp4?token=i11YOhqw32iBGkfQ14mdlfhLipa8vSU4GRqlG029Qj8Y4GfzhTcSd40oGT8CKZTbl0dHv0bRFQ29QGx9FBUimsdxT9v9Ke8BrKu6Z60UrB-sm_e3IlnBndaiVSKx-nVJsh2HdAVP2xcMt8ZBdWg7VuIL7uqB06ywdfdrlNpv0h21oOL-MsMg2iwZiqP04D2EBJpLiFYXNXyJvkho5FQjl2bJpY9ATWoBMWPFpzuq0u3hjCd5w9h_LtDIggdHJiqIbeHqY-YVGc4VtmXPNUN1EwbvEqgOD2atfizgjrUerQ_LyyK0ohwRj7KZH5fofZSZEVOYehsKCYwLBDcl_OBa0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس جمهور ترامپ در مورد ایران:
ایران سالهاست که جهان را با تنگه هرمز نگه داشته است. اونا در گذشته تنگه رو بسته بودن اونا ازش به عنوان سلاح استفاده ميکنن اونا ازش به عنوان سلاح با من استفاده نميکنن
🔴
رئیس جمهور شی دیشب با لبخند گفت: "خب ، آنها تنگه را می بندند ، و بعد شما آنها را می بندید."‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/120297" target="_blank">📅 02:13 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120296">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65d4e78216.mp4?token=tE-tCVklohY7KeJlzkGcR53NeXlBkNQrBQpRzp1cHjOqVipZTov6c-SFyKtmkIpZ2gB0L4IIYaw6WlNXsHWncKm8x8G0V0_n4g8l-3683XFx1STjqTq7VS-FWTwRR_iwrjmWjma8PNXC8ZD7qrnvgVQDrZVM1AbeVNq9YphF8h4q_Tl4XN8PNewVJZwODQp54hI-pHJpGY0h3Hv0G6pDGybE_titM8TZ2Zv1LVIIaPZOHuBPfgGu7Twcb34lNwJk2g9JSUbSieHpaN8vAqVk6SHO59tt_fSGL_Qr3Y-U56bvdRcx0lMrJ_qzlQ9im8SVn6pRGAbDjqSlovfXYM7zBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65d4e78216.mp4?token=tE-tCVklohY7KeJlzkGcR53NeXlBkNQrBQpRzp1cHjOqVipZTov6c-SFyKtmkIpZ2gB0L4IIYaw6WlNXsHWncKm8x8G0V0_n4g8l-3683XFx1STjqTq7VS-FWTwRR_iwrjmWjma8PNXC8ZD7qrnvgVQDrZVM1AbeVNq9YphF8h4q_Tl4XN8PNewVJZwODQp54hI-pHJpGY0h3Hv0G6pDGybE_titM8TZ2Zv1LVIIaPZOHuBPfgGu7Twcb34lNwJk2g9JSUbSieHpaN8vAqVk6SHO59tt_fSGL_Qr3Y-U56bvdRcx0lMrJ_qzlQ9im8SVn6pRGAbDjqSlovfXYM7zBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برت بایر از فاکس: آیا تاب آوری ایران را دست کم گرفتید ؟
🔴
ترامپ: چیزی را دست کم نگرفتم ما می توانیم پل ها و ظرفیت برق آنها را در دو روز از بین ببریم.‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/alonews/120296" target="_blank">📅 02:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120295">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7b5ca6f24.mp4?token=eMgdtdRtc7aVWHG4kj5Jo_47kVcP16E9a38XpXMw8zFZQmzKLJj_DLvLx05UYFlShRriU7JZQ7FZdf1kDgr9CvyPMa8VRgOXumk6ODrT2Wu92koL61fyPVK3nZDI1l1V-65_dJRfjk8SH4Y-R44hFW-KhobGf79_fQ_rjU_GKKBlwBadHSvbqchk92gdVYnhlTOZoP8yWinJsMRLymgm09BPc6P4wAQW9S_DK_MrajnWzDJVdICKcc2ZVwwuDNWFXR6CsXxqrHla69dFNEDnTxJsd1l8hUs7HX0KM_QlfjAQacCwfh-UB3wQC70JohXuJFeQj_bOy0YiMx4hHRxk2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7b5ca6f24.mp4?token=eMgdtdRtc7aVWHG4kj5Jo_47kVcP16E9a38XpXMw8zFZQmzKLJj_DLvLx05UYFlShRriU7JZQ7FZdf1kDgr9CvyPMa8VRgOXumk6ODrT2Wu92koL61fyPVK3nZDI1l1V-65_dJRfjk8SH4Y-R44hFW-KhobGf79_fQ_rjU_GKKBlwBadHSvbqchk92gdVYnhlTOZoP8yWinJsMRLymgm09BPc6P4wAQW9S_DK_MrajnWzDJVdICKcc2ZVwwuDNWFXR6CsXxqrHla69dFNEDnTxJsd1l8hUs7HX0KM_QlfjAQacCwfh-UB3wQC70JohXuJFeQj_bOy0YiMx4hHRxk2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : ویتنام ۱۹ سال طول کشید، عراق حدود ۱۰ سال، کره ۷ سال، یکی دیگه ۱۴ سال، یکی ۱۲ سال، یکی هم ۹ سال
- ما فقط دو ماه و نیم اونجا بودیم
- چین هم این هفته سه تا نفتکش پر از نفت ایران رو برد، چون ما اجازه دادیم این اتفاق بیفته،شما اجازه دادید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/alonews/120295" target="_blank">📅 02:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120294">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: چین جرات اقدام علیه تایوان را در دوران قدرت من نخواهد داشت‌‌
🔴
پکن از عدم نیاز واشنگتن به هیچ کمکی در پرونده ایران یا ایمن سازی ناوبری در تنگه هرمز خبر داد‌‌
🔴
چین برای تامین 40 درصد منابع نفتی خود به تنگه هرمز تکیه می کند‌‌
🔴
خب، به هر حال ما به یک راه‌حل خواهیم رسید. بنابراین یا این مسئله به‌صورت خشونت‌آمیز حل می‌شود یا بدون خشونت. و من خیلی ترجیح می‌دهم که بدون خشونت باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/alonews/120294" target="_blank">📅 01:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120293">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtJilXCWqskyisHWOCDL8nRodaZLLwmowQEyfSrU6_1yp2zAjKCPPnCQNuyJLV42hDOValHkgIKcvgtYqfFmz8DXNV_90zxS5vuAf5NwuuH515L6XHE9r9WdXeHNYFTfPjPE4GfesW4-Xbwwo8YF42bH7DXw6m5EcvklTY1qj3xiUtHHSU2GKlaixK7jnpU_2xN6bNuFZ1o3tVMrfpanK6ufV6MfsUpxY9Qe-X8SJnsuVdYvINECnykPjCi3AUOdWlPnY0K5PVmc3G3x4vncrN2td9pT5ULMf8SBZtHrdXNwDZZ7eolELIWQWLY_AjQvrH1k0oxtFAl3hX0ClUP-6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پک ۱۰عددی کاندوم با افزایش قیمت به ۴۸۰هزار تومان رسیده!
🔴
دولت باید به اینجور چیزا سوبسید بده تا همه بتونن استفاده کنن اما.....
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/alonews/120293" target="_blank">📅 01:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120290">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ee9cf6e98.mp4?token=mybfeosUrxXC6T54etAfnhA-VdrD4_tlDY4sjph1VVQwjxIaEMRhhEqueh5iwIehLMG343yNlLQhGGJ53OV2Nh1oZUwHUxWGI1TU1ewqIkgU9G-HYzGgIxRH-s_w3yippVmxXhYgl6ZCNzEKSpkEgexL-3dkkJYixE3nAhAzW1BzukXI39aeYEOZfW9D9PpYZwhl_Dgu1WFmiANPcuhGynzuKZ-cKfvKX5EV3cbamKgcgZZ-W-gmG7nHQWmR9MLav5VceAP8BPYnvQ-mdIv6bBCMtXqfghiSxVBUsuKlkhuIMz06nnsZTw-aHOPkuZN8r0FuBcMHpGHJYgY1L0qvkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ee9cf6e98.mp4?token=mybfeosUrxXC6T54etAfnhA-VdrD4_tlDY4sjph1VVQwjxIaEMRhhEqueh5iwIehLMG343yNlLQhGGJ53OV2Nh1oZUwHUxWGI1TU1ewqIkgU9G-HYzGgIxRH-s_w3yippVmxXhYgl6ZCNzEKSpkEgexL-3dkkJYixE3nAhAzW1BzukXI39aeYEOZfW9D9PpYZwhl_Dgu1WFmiANPcuhGynzuKZ-cKfvKX5EV3cbamKgcgZZ-W-gmG7nHQWmR9MLav5VceAP8BPYnvQ-mdIv6bBCMtXqfghiSxVBUsuKlkhuIMz06nnsZTw-aHOPkuZN8r0FuBcMHpGHJYgY1L0qvkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجریان بیسواد صدا و سیما برداشتن یه تصویر هوش مصنوعی رو گذاشتن و دارن تحلیلش میکنن!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/alonews/120290" target="_blank">📅 00:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120289">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/444d83ba6e.mp4?token=cRlz6M1ADneTrHR1PqN7Z7L5wU6dTr69zMyHbdjz90DXFjm00nK7Q3uRRuhmOM-YjDxXZ2-KuLtgqgwMZSRkmTmo6Y9UBDcWDzJyYAdO7RuEKvnQd83Uqh-WSHPnGGAb8Mp6fZwuoHPkwLT4SwMFyx2bHYjCiNJziC89eVhLt3Ez2c14oeda82APO-adT82murt4r3DisVgWJBqWumcF7EEdutnaApNsRgJCwBuDlR1eVK9VLM5wSNGJanpdJqA937aBuOcDlxNctRlyrw4cuV5q9FtKY9_84FOmFue9a48T3H1MdkHMjszD0BE4z21fVvOkDhyrFnMB66P8zDX2RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/444d83ba6e.mp4?token=cRlz6M1ADneTrHR1PqN7Z7L5wU6dTr69zMyHbdjz90DXFjm00nK7Q3uRRuhmOM-YjDxXZ2-KuLtgqgwMZSRkmTmo6Y9UBDcWDzJyYAdO7RuEKvnQd83Uqh-WSHPnGGAb8Mp6fZwuoHPkwLT4SwMFyx2bHYjCiNJziC89eVhLt3Ez2c14oeda82APO-adT82murt4r3DisVgWJBqWumcF7EEdutnaApNsRgJCwBuDlR1eVK9VLM5wSNGJanpdJqA937aBuOcDlxNctRlyrw4cuV5q9FtKY9_84FOmFue9a48T3H1MdkHMjszD0BE4z21fVvOkDhyrFnMB66P8zDX2RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مصاحبه‌گر : قبول دارید عامل گرانی‌ها محاصره آمریکا علیه ماست؟
🔴
حامی حکومت : نه، قبول ندارم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/alonews/120289" target="_blank">📅 00:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120288">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
نیویورک تایمز: گزینه‌های ترامپ در ایران شامل نیروهای ویژه زمینی برای کنترل اورانیوم است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/alonews/120288" target="_blank">📅 00:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120287">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09e3b53b1a.mp4?token=sunbuM-6fQ3pNkPCIh5hkaBZnpZ__FvaYgwXIdyNHo0Op_Pct0XuTNZaurgRof2hf3hWn8ov92ZQ0iGnL-dIpYF-m5rCdUWMhnqovqR3Xo0fk7Cbr586dqLs8mfyk_0Idr5YACuLx59H2df3k8QscPcxaiHW7GqxvrE_4SsjJ3sDmaTIe7-reMYAN6j37JUu5qqkn3vXIkxYYrBe3p0sWsHbgJ13-9B78BirVrV_kCSesWfKBAYs_aOlP0LDUPDw_1QymERnWgTZdn5cN0l_sclZH7CagicWD9y9i3oI1_GLCIk1xQHOv38unvtGDjEP9tUBAQNw6-n53cyapDuTqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09e3b53b1a.mp4?token=sunbuM-6fQ3pNkPCIh5hkaBZnpZ__FvaYgwXIdyNHo0Op_Pct0XuTNZaurgRof2hf3hWn8ov92ZQ0iGnL-dIpYF-m5rCdUWMhnqovqR3Xo0fk7Cbr586dqLs8mfyk_0Idr5YACuLx59H2df3k8QscPcxaiHW7GqxvrE_4SsjJ3sDmaTIe7-reMYAN6j37JUu5qqkn3vXIkxYYrBe3p0sWsHbgJ13-9B78BirVrV_kCSesWfKBAYs_aOlP0LDUPDw_1QymERnWgTZdn5cN0l_sclZH7CagicWD9y9i3oI1_GLCIk1xQHOv38unvtGDjEP9tUBAQNw6-n53cyapDuTqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گلایه مخاطب ایران اینترنشنال از قیمت نجومی عرق سگی
🔴
قبل جنگ لیتری ۲۵۰بود و با دوستام میخوردم اما الان لیتری ۱۵۰۰ و تنها میخورم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/120287" target="_blank">📅 00:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120286">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
ادعای نیویورک‌تایمز: دو مقام خاورمیانه‌ای ادعا کردند که آمریکا و اسرائیل در حال آماده‌سازی گسترده برای احتمال ازسرگیری حملات علیه ایران هستند؛
آماده‌سازی‌ای که بزرگ‌ترین سطح از زمان آتش‌بس محسوب می‌شود
؛ این حمله ممکن است از هفته آینده آغاز شود
🔴
مقام‌های نظامی آمریکا به‌طور غیررسمی می‌گویند پیروزی در حملات جدید بسیار دشوار است، زیرا ایران بخش زیادی از توان موشکی و زیرزمینی خود را بازیابی کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/alonews/120286" target="_blank">📅 00:06 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120285">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
نیویورک‌تایمز: ترامپ روز جمعه پس از بازگشت از چین، با تصمیم‌های مهمی درباره ایران مواجه شد؛ در حالی که نزدیک‌ترین مشاورانش طرح‌هایی برای ازسرگیری حملات نظامی در صورت تصمیم او برای شکستن بن‌بست از طریق فشار نظامی تهیه کرده‌اند
🔴
مشاوران رئیس جمهور آمریکا می‌گویند ترامپ هنوز درباره گام بعدی درباره ایران تصمیم نگرفته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/120285" target="_blank">📅 00:04 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120284">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
فارس: نمایندگان مجلس پیشنهاد افزایش ۵۰۰ هزار تا ۱ میلیون‌تومانی رقم کالابرگ را داده‌اند اما دولت گفته که تنها منابع افزایش ۲۵۰ هزارتومانی رقم کالابرگ را در اختیار دارد و سازمان برنامه هم اعلام کرده که پول نداریم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/alonews/120284" target="_blank">📅 23:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120283">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
ترامپ رسید آمریکا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/alonews/120283" target="_blank">📅 23:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120282">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHitin_D1tV6B6BVGQkhjajQ1OfX-yahDB0s-BhXlC2DrvpYPB4Wa5hC7anWtjng7kuGFDuVGjDNAwUcGplfpKzDeL0aWEEtX6Zsep4Sa_TMmkt6w9T4sVBnjp1L6N2uAsBgAOk1ZePIf1_JvBAe0ZsqqT4R8gC8wv3wpWzUJe0JompIBSRcyaGUTDq4brTlkkMcveuRocoPs8ECDqWeb2oHq-HHSXQqZUE_GoaqULPxpQR5Wdk3OXU4nTIXRZYm8pGHDw1_MtnrwfSmcYOkVIcXCKUwiO5UqXxG-dl_-MboybpwjkphJonkYizdxl6n8AOdbicBhYPe192LEye3Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مقامات آمریکایی مشکوک هستند که هکرهای مرتبط با ایران ممکن است پشت یک سری نفوذهای سایبری باشند که سیستم‌های نظارت بر سوخت در پمپ‌بنزین‌ها در چندین ایالت را هدف قرار داده‌اند، طبق گزارش CNN
🔴
هکرها از سیستم‌های اندازه‌گیری خودکار مخازن که به اینترنت متصل بودند بدون حفاظت رمز عبور سوء استفاده کردند و این امکان را برایشان فراهم کرد تا خوانش‌های نمایش داده شده سوخت را دستکاری کنند — هرچند نه سطح واقعی سوخت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/alonews/120282" target="_blank">📅 23:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120281">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
ژان-لوک ملانشون، نامزد ریاست‌جمهوری فرانسه، درباره ایران و تنگه هرمز: «وقتی کشوری از خود دفاع می‌کند، از تمام ابزارهای دفاعی خود استفاده می‌کند.
🔴
ما هم همین کار را میکردیم.
🔴
ما تمام کانال مانش را مین‌گذاری می‌کردیم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/alonews/120281" target="_blank">📅 23:39 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120280">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
منابع عراقی از حملۀ پهپادی به مقر گروهک‌های تجزیه‌طلب در کردستان عراق خبر می‌دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/alonews/120280" target="_blank">📅 23:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120279">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
فیلد مارشال ، محسن رضایی: قواعد نظم جدید جهان دیگه آمریکا محور نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/alonews/120279" target="_blank">📅 23:24 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120277">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f3b1bc7ef.mp4?token=TNkqwX8EdVvjSAlCEQN4zktzEfp6rLxdrZC_0HQmkrpLotpmFUjq2N8WKDajA5mwhaKOZkX5jGb5urvPX_23gUAoWszQn2BDj6x4d-N4Vs5wFjmYgWNnVr7BZSZkdZWsht4Ks2G12XdQVad3cnP4Is9yldjmsYkOWqyknLspZhmmtW9zP1gSh_9UQRJaWS3TcsA2rvvKSLOVHGrnM_pi1B6XFMEQsIYb_4xnvM8JOZSs94KLqy7gWPtCEV5CAIDXMvII8InUPgk9piuKsr_Q-pdMBjFk_pD2rbsR3WzC9X6i2hZM4Y-6SexIksqQDmOHnRRKbz_actSyW0nQ3eDVsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f3b1bc7ef.mp4?token=TNkqwX8EdVvjSAlCEQN4zktzEfp6rLxdrZC_0HQmkrpLotpmFUjq2N8WKDajA5mwhaKOZkX5jGb5urvPX_23gUAoWszQn2BDj6x4d-N4Vs5wFjmYgWNnVr7BZSZkdZWsht4Ks2G12XdQVad3cnP4Is9yldjmsYkOWqyknLspZhmmtW9zP1gSh_9UQRJaWS3TcsA2rvvKSLOVHGrnM_pi1B6XFMEQsIYb_4xnvM8JOZSs94KLqy7gWPtCEV5CAIDXMvII8InUPgk9piuKsr_Q-pdMBjFk_pD2rbsR3WzC9X6i2hZM4Y-6SexIksqQDmOHnRRKbz_actSyW0nQ3eDVsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهر صور تو "جنوب لبنان" بعد از حمله‌ی سنگین ارتش اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/alonews/120277" target="_blank">📅 23:20 · 25 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

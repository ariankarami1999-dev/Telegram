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
<img src="https://cdn4.telesco.pe/file/tqyPWGgS29dBqWB_cTpsyJeCKGnSmYnqJUY7dm68an3Yvw_gsguum4DbR6seRAcB7lMzB-eAiRQU7PgmyKfPLjo4oExLBH5KPKsFFCmhc-L1PK4-8O99kf4dxtHeTbaM7Px9FJ-RgjybB_7Et_oJsNmzGVaZqhhGn3qLpVWeFjGqfSn4rRTnDy9g_n25Hv1_xI5U_MNWrEnps7wo7QVEyBOu8-jOS6VzKhDpb2zgyKrqmHIksFyJ_1DAnqyYOSMpXPmmVe9GRW1yzbFppZS0nosustvNTnqRLNKJ7aUy0rwaLkZ2fyHWOFcwI_Ju4Lwoa-Bzc862PgU6vuVpPPmQUA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 182K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 23:09:05</div>
<hr>

<div class="tg-post" id="msg-67810">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6SQAYQEacjJIYewbt08DmeYsnXCPconFZFu4DaSj2WxAcuwlKJnwGaHhcRF3p-uhZmR6YNn1CSuL5IzMBNH2pnCAWBqhKhKel9jbLwW4D8Vk5zVsRuYQRQIWZWI4AnhIOfyIJQvKE4Lv3n_rWE9CWfew-Gj_36I2X6UV2SD3vE9eRPDJciU5GDhduyDBCGdkva2l4e7SebSAPr3LKCXBVC4DhRlxxUqPIjz586yyZ9YuFzSP7xQQRKeEESIbgIoK5UzM1S8tn_MqwwMQK2w9J8Qleataxjx3RH17nXSz86_l0yF7iSYKuyJFptSwFwCeXObtVySDBupuOV0RK4pMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علی قلهکی:
قرار بود سفرِ عراقچی به عمان منجر به صدور بیانیه مشترک درباره مسیرِ شمال و جنوبِ تنگه هرمز گردد و در ادامه نیز «قالیباف» و «ونس» به مذاکره اضافه شوند که با بازگشت عراقچی، گمانه‌زنی‌ها درباره به بُن‌بست رسیدن دیپلماسی در مورد «بند ۵ تفاهم‌نامه»، بیش از همیشه تقویت شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 613 · <a href="https://t.me/news_hut/67810" target="_blank">📅 23:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67809">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
اکسیوس:
ایران نتوانست در این جلسه، موافقت عمان با این پیشنهاد را جلب کند و مجبور شد این پیشنهاد را برای بحث و بررسی داخلی در تهران مطرح کند.
@News_Hut</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/news_hut/67809" target="_blank">📅 22:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67808">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHZbzYSGDz8f-9G5srP9cFpHBl0kBs9jVnTeE_Va4wJjyE9FqWS3UVPYiUMUA_VcpRuG8fvPHjbSfXA9xEELec193cseb37jxJyn9fyIAG0LoKPbjzQbtyyna-wv3Q0vTlnILu4-fh1FJZBlQ4MBYZm4K9HWcDGZHVWPCUl9XPzm3LFNqxVjxa1DrgHNJnx1i6KUXerEUcX2sidmTfavHPfewvGf31blWVS3icn5a6S6k_r_aC9WZcAQKfXzPbhLMdXI0AClY8HAvuoLRGSi4USIqRj34RuiEchm7Ksb6hPvoJnB9XR9f_B1oh671onzjjbGsjQwvi-haJVyeKQfUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سی‌ان‌ان:عمان پیش نویسی را برای مدیریت کشتیرانی از طریق تنگه هرمز با استفاده از دو کریدور جداگانه کنترل شده تهیه کرده است.
بر اساس این پیشنهاد که هنوز نهایی نشده است، کریدور جنوبی از طریق آب‌های سرزمینی عمان برای کشتیرانی آزاد در شرایط پیش از جنگ باز می‌ماند.
کشتی‌هایی که از کریدور شمالی از طریق آب‌های سرزمینی ایران استفاده می‌کنند، به تایید قبلی تهران نیاز دارند، اگرچه ایران هزینه‌های ترانزیت را تحت ترتیب پیشنهادی اعمال نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/news_hut/67808" target="_blank">📅 22:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67807">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d2e49f67.mp4?token=OCOIYXEXZ1uii4GXh-5RxmTv3g9OqR0AbUrf9hfHSEOjsBkFEtOJDJ_Ew0lWrcRI03zGXAiyKtdPLnIzIf6kxSmOLg2ks5gO9OhrEe_duRUN6DKNHb8QUHPJqxjdXumt2M-7iA7hLWHBCW5lFU9feffh34NPFZn0iO01fN13yG1hii36wFNKnltOLSDNkNqgbZUUYhVWK7cv4QrRISURgabsKOxx3ZX8dHt64Q4tvsJuASOhQ4x7b2CDnDbOKueKtn47DImMvhUyPRPNNFvFDWMStJ4Q_jYuU70apR4HNW0pJRnI9lncmdp66CpU82RkSQRvMMd34BkPpQWzMeUpgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d2e49f67.mp4?token=OCOIYXEXZ1uii4GXh-5RxmTv3g9OqR0AbUrf9hfHSEOjsBkFEtOJDJ_Ew0lWrcRI03zGXAiyKtdPLnIzIf6kxSmOLg2ks5gO9OhrEe_duRUN6DKNHb8QUHPJqxjdXumt2M-7iA7hLWHBCW5lFU9feffh34NPFZn0iO01fN13yG1hii36wFNKnltOLSDNkNqgbZUUYhVWK7cv4QrRISURgabsKOxx3ZX8dHt64Q4tvsJuASOhQ4x7b2CDnDbOKueKtn47DImMvhUyPRPNNFvFDWMStJ4Q_jYuU70apR4HNW0pJRnI9lncmdp66CpU82RkSQRvMMd34BkPpQWzMeUpgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سی‌ان‌ان: برای نخستین بار جزئیاتی از حمله موشکی رژیم جمهوری اسلامی به ناو آبراهام لینکلن منتشر شد
.
شبکه سی‌ان‌ان در گزارشی به موضوع شلیک موشک‌های رژیم جمهوری اسلامی به ناو هواپیمابر یو اس اس آبراهام لینکلن پرداخت و جزئیات تازه‌ای از این رخداد را منتشر کرد.
این گزارش در حالی منتشر می‌شود که تنش‌های نظامی میان واشینگتن و تهران همچنان در سطح بالایی قرار دارد و موضوع امنیت ناوگان آمریکا در منطقه بار دیگر مورد توجه رسانه‌های بین‌المللی قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/news_hut/67807" target="_blank">📅 22:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67806">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
کانال 15 اسرائیلی:
ایالات متحده منتظر پاسخ ایران به درخواست‌هایش مبنی بر توقف حملات به کشتی‌ها در تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/67806" target="_blank">📅 21:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67804">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08bce6837f.mp4?token=DfTxbI6w8w7m86O-1VOcNeUUd0NXRMnlAk8Ua-Xvek3YQLLD9_XcFWfp-qT6NLxrZtf_qAdyYNq6Y4_-wHEINPUtJFiaEsHAB3-7RaCuuqZhunpVmdbEYtREd6w5JnwKzOG_ZpJNo_iGksz8f5eHZ_yO2-bb_i4laMj_17fE-SBDbR3trLoK8ygvHg4zREW-OC3yaQm3SoAh3uUz1utZm6FWq6Xs97nxgnpPyhh0XRiaFlIkCBPw0t-NWBmmKsIhvC3yvf2V0BIViC8bnm2w583HIcBizCcJSsYPLet7LsMtKVhThMFTnsm8SoRBNdPkF5bIMAYRtx6HMjlu2E6T5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08bce6837f.mp4?token=DfTxbI6w8w7m86O-1VOcNeUUd0NXRMnlAk8Ua-Xvek3YQLLD9_XcFWfp-qT6NLxrZtf_qAdyYNq6Y4_-wHEINPUtJFiaEsHAB3-7RaCuuqZhunpVmdbEYtREd6w5JnwKzOG_ZpJNo_iGksz8f5eHZ_yO2-bb_i4laMj_17fE-SBDbR3trLoK8ygvHg4zREW-OC3yaQm3SoAh3uUz1utZm6FWq6Xs97nxgnpPyhh0XRiaFlIkCBPw0t-NWBmmKsIhvC3yvf2V0BIViC8bnm2w583HIcBizCcJSsYPLet7LsMtKVhThMFTnsm8SoRBNdPkF5bIMAYRtx6HMjlu2E6T5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ارتش دفاعی اسرائیل:تروریست‌های حزب‌الله در حال انتقال موشک‌های ضدتانک در داخل منطقه امنیتی در جنوب لبنان بودند.
این تروریست‌ها موشک‌های ضدتانک را به یک ساختمان در آن منطقه منتقل کردند، که نیروهای دفاعی اسرائیل (IDF) آن را از هوا هدف قرار دادند تا این تهدید را از بین ببرند.
پس از این حمله، انفجارهای ثانویه شناسایی شدند که نشان‌دهنده وجود سلاح در داخل ساختمان بود
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/67804" target="_blank">📅 20:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67803">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e14ad8a91f.mp4?token=qLKniKMiuujJzWRqIcoyi1IhTSj_XJcIIHvVmN19wKB0I7vBM3QfnbcRQlsAOZ4xrkr4qBLxfSxgrVKD_ZFCHQ_3aqMPSMo36bUi2g8bCHjzFqkc1i0sHEVKozHfhWYbW9EKLjm187wlVzLQFIjOhlCQS8LNN9248ohwCDNL3ZPtFpPdyllE0uABtN_KvjTQ7oc6IvENb020LoI87QgqaLtm7LT_VpYrKx9KsPAVB8tZYVAyps8iU006MVQLFZKFPGcBBF4vtEcR-KIz-NQnxW2f9jNVRz6vh0Jc6AMo9TyWmb-n2xDcnv6hm92WX_hwiQJVPAWImGj6aVO3EluKlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e14ad8a91f.mp4?token=qLKniKMiuujJzWRqIcoyi1IhTSj_XJcIIHvVmN19wKB0I7vBM3QfnbcRQlsAOZ4xrkr4qBLxfSxgrVKD_ZFCHQ_3aqMPSMo36bUi2g8bCHjzFqkc1i0sHEVKozHfhWYbW9EKLjm187wlVzLQFIjOhlCQS8LNN9248ohwCDNL3ZPtFpPdyllE0uABtN_KvjTQ7oc6IvENb020LoI87QgqaLtm7LT_VpYrKx9KsPAVB8tZYVAyps8iU006MVQLFZKFPGcBBF4vtEcR-KIz-NQnxW2f9jNVRz6vh0Jc6AMo9TyWmb-n2xDcnv6hm92WX_hwiQJVPAWImGj6aVO3EluKlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که رسانه جبهه پایداری از تغییر موضع ممد سامتینگ نسبت به مذاکره با آمریکا منتشر و وایرال کردن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/67803" target="_blank">📅 20:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67801">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iz47oX4HCwlfkPryYs7n9U5n7J2U5tT5z8Grm_ewaNuF5hMtmAl00JuZl2fxrciAXrnrAxMr_pKAU0psEUwj52obDXIJBFyAZAaloBY0M291PiwLDEHBlD1ym_k7WYaaGttDQwNN9Q11WJSHnGDGnpP3_fchB4LB_Ub0L08AsxZNnyj3MSamSX6FwacP4dNoxxFN58iNLpbaajet-R1cx_GZH-Tthue5ea8V4wzhTqzV_1pxUSXv_LIXrOqN1laRQ3qSxbuAAaNQJ_qXh4ryaSoT2V3xXPvf3iqQJtF6F_lwmk8NIp7QRbg-PcE6_TPCNjeRTGLYMjNdKceDUXu46w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rQg1odY-yEUCL-LYsgG9F8cquKXFPWK6_PuzMb0zDFsYCpz_xXeg-f6eeJImnXpWffpzKX7H3SQDVAVa3L3I07iT-H79akB-Zf017DsfAQAINwCgv85gXWCQU1bsY3apepDv0LMxY10CS5Xz2J4BEm3A46n33dV_eaEnD6VxsRUXg_LlODD4LpCwGaK6ZDSia0EoM-KtNamBQySeXaTRln6-Cs-Q1k9DkEB9bMvf-LJGt957yefaoBuFebaclFPbq8XiZRGrxDMVd9uEoewT_XdN7mc7JZiAhwiJpvVPHOqSu3FL2yhhss8-plMctu1XLIKt3MEn1UfwkAwsOzjcSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
بسیاری از هواپیماهای تانکر سوخت‌رسان آمریکایی از پایگاه هوایی الامیر سلطان در عربستان سعودی خارج می‌شوند. این هواپیماها معمولاً پایگاه‌های خود را در منطقه ترک می‌کنند، زیرا نگران هدف قرار گرفتن توسط دشمن هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/67801" target="_blank">📅 19:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67798">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mM2TcBq79wEhytebcB7FQbq8WXShpBg9uRIhACJytvxYB_mFT4yNOccNBLQrF8X8A_XhiUlovw7kqkVVFs3GdnRZD2DRq_U7217v4MW7w4lhLtAJ3ZrctoISdWW9XzeGGsrRmsMlnWDv3RAkK2hhvgAGHaIHPQCJc7YhdzLzM16Lb5HShckTZV2zEkyVdsZhYGP-pFSBPglrMJmPx4DCyjjQe-cxewhD6YvKWU9jU7mTfM2vIrGxL8kY-fUS4MgWDyFHUvi0LXabeteImvWbkEt450Z057WCfZVRnYed1fXQSSbvL5VkCyAJul_e0cA5-uQcu6GJEsagrR5hxjNkOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنالیز و پیش‌بینی نتیجه تمام بازی‌های فوتبال جام جهانی 2026
💻
📈
🇫🇷
⚔️
🇲🇦
وین شد
✅
🇪🇸
⚔️
🇧🇪
وین شد
✅
پیش‌بینی نتیجه 2 بازی‌ باقیمانده 1/4 نهایی انجام و در کانال تلگراممون آپلود شده
⏳
🇳🇴
⚔️
‌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
󐁧󐁢󐁥󐁮󐁧󐁿
🇨🇭
⚔️
🇦🇷
لینک رایگان ورود به کانال
👈
بت جی‌جی</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/67798" target="_blank">📅 19:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67795">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgD_8dv7aLb8S6xzrgq-OFTHueI9s9WVu6uwbWtMcguMQ5wFo7oizJSTq_-lnI_lF7vPGqsZXPlrZBorcGWvNCljQ-IUYFGhFChwsvDRSYXZ14wp-mheXV34YZlpwvGx7xBgrMSCv3rXci-J0h3DLW6we4uEf-kLRLrhbdkIgnaeeXb10dMfK_ra2BfbrNjcB0Wpg03NQZ0bfLaGdFiwYMTkTueyJcv0SjEeaY4bhXdROAhuHoFbvKCuTSPVDZPLvwUfTLV0e0NjiDYXuMJEf8ADzHx_mkEpfGojgPnWQIqI-HzwLmr8ssHRJimgbMRhIDocBFVa9B1sC5fG0xAVlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید:
به گفته یک دیپلمات مطلع، مقامات قطری در حال مشارکت در مذاکرات میان ایران و عمان در مسقط پیرامون تنگه هرمز
هستند.
یک منبع منطقه‌ای اعلام کرد که طرفین در حال گفتگو درباره بیانیه‌ای احتمالی برای بازگشایی کامل «مسیر میانی» در تنگه هرمز (که در آب‌های بین‌المللی واقع شده است) جهت تردد کامل و آزادانه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/67795" target="_blank">📅 18:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67794">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a00f69c138.mp4?token=tNB1Z6PA3IGDPlnwXTqUYDEY8Bo4LGhl1zjy8VW6p-R9vVfHVHcRdmeS2Ui_W6pXi2Dqq6tNXYu02eamclWWxGXmoWSuzEzBgpoBqBfKiYzqAwKDMUxYZIDElV1pYc1rj-ZmRNZpIhQNUNXrSbFl5ct73gkLdghOmFQJVMUCUJXLgf-j6Nif8c8Lj8UuB-TXz4NtJw0eShIs7fegLDg34kqpNM1U799modQRbXB8l7PtI1bCoFeDBOF-x_Sbo1cCnRSUPRfRGJYLo1WqRcyJB9nRF3wIVpa2gIn5XZViL__qXSPteDYvI3qSSr-UEDOexe7IRpC2o02huoxeD-5U1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a00f69c138.mp4?token=tNB1Z6PA3IGDPlnwXTqUYDEY8Bo4LGhl1zjy8VW6p-R9vVfHVHcRdmeS2Ui_W6pXi2Dqq6tNXYu02eamclWWxGXmoWSuzEzBgpoBqBfKiYzqAwKDMUxYZIDElV1pYc1rj-ZmRNZpIhQNUNXrSbFl5ct73gkLdghOmFQJVMUCUJXLgf-j6Nif8c8Lj8UuB-TXz4NtJw0eShIs7fegLDg34kqpNM1U799modQRbXB8l7PtI1bCoFeDBOF-x_Sbo1cCnRSUPRfRGJYLo1WqRcyJB9nRF3wIVpa2gIn5XZViL__qXSPteDYvI3qSSr-UEDOexe7IRpC2o02huoxeD-5U1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریاست‌جمهوری core:
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67794" target="_blank">📅 18:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67793">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KySb-tBVe_lgLfk3Q-0xfTvWBdP8P8leVnsU7w-u3CbqrZlIKzDuiCQjF-8F-OGYGTcQ1MtNy62BmfDwVybsDEQ3AXtKtvMGGOESvl3oVhLC65lD-2YHO2HOIMd8A9i5XbapJgTGi9NfZZYK8rWS9mp1zcHeg4QmLQ6glHuonlmLn599BFSdi0aJ1CAemUv1kaTVv1YJhOPmA9tDQ2TCTkSLJ4hlNsuc6lxE0ttnAOpvzTsr_9gVJYq79FX3hAlkHTGSdwIUAjKsAcg-hYmoTN8PCb5PeEAhuOiiIgkfTMS5P91VdsTJV9SOaIJKT9HOyjGVBhp-NrKLbzScItrePA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری مهر:
یکی از نهادهای امنیتی برای حضور فیروز کریمی در  یکی از شبکه‌های ماهواره‌ای گردش کار قضایی برای برخورد با وی را تهیه کرده و در دست اقدام قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67793" target="_blank">📅 17:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67792">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJUvuQzhnslbkp4rMznMiIBNOvAETStYvkvPUQM9veLN0euFmhog0K6I17oR4lV56eC5giZvY-8cU8-uNthIZby3JIkiT0HRiRCFm7wL5z0g1Pb0Qsv9SpTWmptCSz7-m7Y0U0s9k_4Bgw3Xat9ce0wzclHdPRW2fV5FBfroRzjQHbnTO83cxboe5liifN2xsLG2iugynAhdhexaXzYNoxorDspeu5DOikZKjjGc_Jvi2hYTaKZbQIlZvxZcq4NeSSBaErUkR6f_K82eWRp8TGd9h5xFuNgYJSfq9hD2pIdh2ZaJ3iquCEIGtL6g9IXk75gJj3WEXSyUOAN5nRztmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستهای این توله‌سگ خمینی رو ببینید؛ مشخصه تا حالا حتی یک ساعت هم به سیاه و سفید دست نزده. یک عمر از خون و جیب مردم ایران مکیده و حالا هم نشسته میگه «جنگ جنگ تا پیروزی»!
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67792" target="_blank">📅 17:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67791">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57c1e2ae31.mp4?token=GFL2jq7Ag2Avgkvnq-4_pgdlbJtQJjl7uqVWDq9yEd2DYOcQ1Y6qWiO740bQ1F2QYF8PmmAPilU8xXBJzjvbTeVz2XLuzN2wPwDvWLpNysSnqJz3mFC9FTUj5svyqOeOuvHyOD1XiKvDB8eY1i_am-603uDAYHtx-cPTKVnS-shiMpFeibLHQSuitVkp4n-XurUNmW7cS3Dwxx_huP9ndUF5ufe1mcYRQGcEhQOSxlepAjmz70Vt-1chkexLBogEGPFl16TU4G2viB58tNG0ZwJArQb8eXLLZ2ab8s8WMxBFa6kqvfJHm0W2zZv2_Qbl8P_iD8DthDHV0_B1WOOnHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57c1e2ae31.mp4?token=GFL2jq7Ag2Avgkvnq-4_pgdlbJtQJjl7uqVWDq9yEd2DYOcQ1Y6qWiO740bQ1F2QYF8PmmAPilU8xXBJzjvbTeVz2XLuzN2wPwDvWLpNysSnqJz3mFC9FTUj5svyqOeOuvHyOD1XiKvDB8eY1i_am-603uDAYHtx-cPTKVnS-shiMpFeibLHQSuitVkp4n-XurUNmW7cS3Dwxx_huP9ndUF5ufe1mcYRQGcEhQOSxlepAjmz70Vt-1chkexLBogEGPFl16TU4G2viB58tNG0ZwJArQb8eXLLZ2ab8s8WMxBFa6kqvfJHm0W2zZv2_Qbl8P_iD8DthDHV0_B1WOOnHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو یکی از کوچه پس کوچه های مملکت، یه دختر و پسر شروع کردن بوسه و مالیدن همدیگه، تا اینکه دختره دستشو برد روی شومبول پسره
👀
یکی از همسایه‌هام وقتی دید داره کار به جاهای باریک میکشه اومد و گفت جمع کنین بیست نفر دارن از پشت پنجره نگاتون میکنن!
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67791" target="_blank">📅 17:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67790">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‼️
ویدیو وایرال شده از بساط عرق خوری لات های کرج
😳
امیرعلی امیرعلی امیرعلی....
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67790" target="_blank">📅 16:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67788">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUsKyeUwJWagUq9Xmm5M7KjlV9V0ZxivECpwo3leTzQXJLIrYCFu9xhrxh1m8VylDgkPyTvBSalE6KkkjVSFdRd1KonBTrg0PM9eD7W7RjbkA0PllxWkEUJ1xAcgxw2trX1t1u9jUTLSjrBQ4WE9c0UyEsbKTJtKSkFgaySDMWqUSR7e-ipkYHokfjtTTSJF5nFek_r4U71iiMGTjgHgxuegAtyX20Vy5Hea0LvqUusm3vL9yvxllpQrvJveMoi7aJRjfME7RxSsJL7rJcfr3_-HJGRqtI_DhIieYS8U74AnQUwTxXTgncDjfQ96nqgXW9NvSUKIMt8j6Hu66v37eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3354c0af73.mp4?token=oWB1bv40y4YyBeFFKynBiXYUdG3eSHOaw2bT317P5vNJLXAgIL7CpqJguHB4LbJsIhs2ZB6oaQ85Il_IA32TtCrRdgzJUmNybaenq-Dj-RdMATqo5ZOVLRPPIAftP9ltF5jnKcUFXcXko-u2tRmHpx5g2KS8rGzNntkFm_9GczI-PS4KkJI9IdkH8b1_ktXcd-kd0tVd5l-fs7lnQXC2Cmeeiof1kdYUEyOvR-whPaV3x8g6cR6xlXBZ5SRXU3pwuhviBO0HA3ir0rsga4w-iEUwM3IXMRgiGpxzu74NhaoqvuBXyH2BsnvsZNllJpVSpC3WKATBN8W59wzJ-5zKfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3354c0af73.mp4?token=oWB1bv40y4YyBeFFKynBiXYUdG3eSHOaw2bT317P5vNJLXAgIL7CpqJguHB4LbJsIhs2ZB6oaQ85Il_IA32TtCrRdgzJUmNybaenq-Dj-RdMATqo5ZOVLRPPIAftP9ltF5jnKcUFXcXko-u2tRmHpx5g2KS8rGzNntkFm_9GczI-PS4KkJI9IdkH8b1_ktXcd-kd0tVd5l-fs7lnQXC2Cmeeiof1kdYUEyOvR-whPaV3x8g6cR6xlXBZ5SRXU3pwuhviBO0HA3ir0rsga4w-iEUwM3IXMRgiGpxzu74NhaoqvuBXyH2BsnvsZNllJpVSpC3WKATBN8W59wzJ-5zKfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
حملات سنگین ارتش اسرائیل به شهر المنصوری در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67788" target="_blank">📅 15:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67787">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a812a42d8.mp4?token=C0map3kY2GJ3mSOQ6-RwzycWd1ehb_MeIwc2IGLBE58PrhrmeYq6bATDbPomUqk4m-NNPGS6I1bxHwDGTeZOfQWfzSVMWPbsU4R2zCXWGblHubwLRilejoh71uXf-n3SGezyHDyPbYxNj-UThQCtX7dP0hzEwvjvuwy2BpvU8C1Ur1Q6qfB5uzJJImPxwtBn2O9ItQ-ZbB9KMiERTt-JAEi4wieiILyJ2BsjnwOsKzGxPYHLHry_XEabfuYU7Slqa4LifrqDVcZqBm_XPHLdBmCOUF67O3Sl63AUVugSndywkCYu4N8VB7KjHgJoOfRfQSvVuOlRBRZObX8JB6HQcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a812a42d8.mp4?token=C0map3kY2GJ3mSOQ6-RwzycWd1ehb_MeIwc2IGLBE58PrhrmeYq6bATDbPomUqk4m-NNPGS6I1bxHwDGTeZOfQWfzSVMWPbsU4R2zCXWGblHubwLRilejoh71uXf-n3SGezyHDyPbYxNj-UThQCtX7dP0hzEwvjvuwy2BpvU8C1Ur1Q6qfB5uzJJImPxwtBn2O9ItQ-ZbB9KMiERTt-JAEi4wieiILyJ2BsjnwOsKzGxPYHLHry_XEabfuYU7Slqa4LifrqDVcZqBm_XPHLdBmCOUF67O3Sl63AUVugSndywkCYu4N8VB7KjHgJoOfRfQSvVuOlRBRZObX8JB6HQcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مجری فاکس نیوز:
رئیس‌جمهور می‌گوید ایران دوباره به میز مذاکره بازگشته است. آیا شما واقعاً معتقدید که ایران با نیتی صادقانه و با حسن نیت به میز مذاکره برگشته است؟
🔴
هارلی هیپ‌من، تحلیلگر سیاست خارجی:
قطعاً نه. البته دوست دارم این‌طور باشد. هیچ‌کس خواهان جنگ نیست، اما ایران کنترل تنگه هرمز را رها نخواهد کرد. آنها به اهرم راهبردی‌ای دست یافته‌اند که به‌گمان خودشان، شاید حتی از یک بمب هسته‌ای نیز برایشان ارزشمندتر باشد. همچنین قرار نیست از تسلیحات هسته‌ای خود دست بکشند. بنابراین، آنها به دنبال حل‌وفصل مسالمت‌آمیز این مناقشه نیستند.
احتمالاً این وضعیت تا ماه‌های اکتبر و نوامبر به شکل اقدام و واکنش متقابل ادامه خواهد یافت و پس از آن، ترامپ میداند که در آن مقطع چه اقدامی باید انجام دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67787" target="_blank">📅 14:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67786">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🇮🇷
مجتبی خامنه‌ای:   آنها باید بدانند که این امر، متوقّف بر وجود شخص من یا سایر مسئولان نیست. ما باشیم یا نباشیم، این مطلب محقّق خواهد شد و بزودی آحادی از آزادگان در سراسر دنیا هر یک بخشی از این مأموریت الهی را انجام خواهند داد.   @News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67786" target="_blank">📅 14:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67785">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🇮🇷
بخشی از پیام مجتبی خامنه‌ای:   عهد می‌بندیم که انتقام خون پاک رهبر شهید و همه‌‌ی شهیدان این دو جنگ را از قاتلین جنایتکار و بی‌آبرو بگیریم.این جنایتکاران آرزوی مرگ آرام و در بستر را به گور خواهند برد  @News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67785" target="_blank">📅 14:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67784">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🇮🇷
مجتبی خامنه‌ای:
انتقام خواست ملّت ما است و به‌طور حتمی باید صورت بگیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67784" target="_blank">📅 14:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67783">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🇮🇷
بخشی از پیام مجتبی خامنه‌ای:
عهد می‌بندیم که انتقام خون پاک رهبر شهید و همه‌‌ی شهیدان این دو جنگ را از قاتلین جنایتکار و بی‌آبرو بگیریم.این جنایتکاران آرزوی مرگ آرام و در بستر را به گور خواهند برد
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67783" target="_blank">📅 14:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67782">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
پولیتیکو:
آمریکا انتظار داره جمهوری اسلامی در بیانیه‌ای که قراره امروز منتشر بشه، «به‌طور صریح یا ضمنی» قبول کنه که در حملات اخیر به کشتی‌رانی در تنگه هرمز مرتکب اشتباه شده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67782" target="_blank">📅 14:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67781">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xm8FhAvXjLMMrX46WIBm_paVAuAyFbF5_nfVY90sxKGgMQDrqgaM9iIdEgqxPI3SSQpkvWLq4ClwxSr1xb7BMtwM7HCq9k6-kJRQhNWlnhc7U1_hEOT4Obzb0ETVGrpMCrorEa3dKyBHsYXsKGFFqMRLZ6nZMvE1eWkJ2WUA4Ppk8npvtBrHpg432ZQxrMKG87ptKNIz3--cjOxdiG19ZdAFwAkmxPP7WuajVTOlGOEbbpiajhOC_Ts6RW_lBUdpajVRV0pmDgsX0E_bTklrDfIQNLmpKkj0Tmg4UdzEQsQ0rdbgOoDsxPMx6oa9fLk1qMvYx87ttVFV21zjqUBpqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
امشب رو باید تا صبح بیدار بمونیم که ديگه کم کم جام جهانی داره تموم میشه؛
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس vs نروژ
🇳🇴
| 00:30
🇦🇷
آرژانتین vs سوئیس
🇨🇭
| 04:30
🇮🇪
کانر vs هالووی
🇺🇸
| 02:30
[این فایت خیلی مقدمات داره و احتمالا ساعت 5 صبح شروع بشه]
🇮🇷
دانش آموز vs دین و زندگی
📚
| 07:00
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67781" target="_blank">📅 13:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67780">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآپارات اسپرت | AparatSport</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fITeOkj7hUw2bgCGG2XC38YbG60Kgxt3o9nVfx3J_CrSjm4jptJ1u2U47dBkVDWOTuQP0NYgtFfhGZQlDLBJUf0KwZeKsIdPY346f8UdV7iTHTFO6BmDNcWLm8Zh-ydQ1YYvCq7aV1i21Jw2adT5rYtQvhL3XcBrguxMd8XEadl2tOXPf8a22TPDPs9SlknltJKAxY0OmDdPBpvpRUA-_Njf4gSAYl9A3gAE1HWtsqOuUudsId-N1wLeaz6qrl2xZFQZPANueFqIPPjR_Sra109iUIJ4iBEBCeKNizWJp9_blii-6IpbjjAnISWBcJAtxieYwVYDYOMF7bo2iOzoLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پخش زنده و اختصاصی بازی نروژ و انگلیس با گزارش محمدرضا احمدی در آپارات اسپرت
📅
یکشنبه
👈
ساعت ۰۰:۳۰
🔗
لینک تماشای مسابقه
(بدون فیلترشکن وارد شو)
@aparatsport</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/67780" target="_blank">📅 13:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67779">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYGQbSGM6uZ75q0u3FFtilTMi-Adt9_75zqoLPjL2ag0g8leUhPZSC9Beota4t-kTNn0Wf_0Ofib7GE5EtCc8bLTaWx6nYidHE3JPJ6X_prUCM8DmjKcnKilZucjSFmkgfYpT34qupNx-iTN-PRm0TFuUO8Dy4Iesqe4jMKx26MthDU47YNlrCw0CKTpfzDMTm84L6RIzT2cpVRcjMQ2NM2k9jxbS41whfr6mcnvOD0CH2uqRnnqVDEc5K5jmUGCN5uVtjm8mseY_vlqicKIffauPvYquSBTZ326_6Pww2MX-P5CkeY0y2I5oWbD4aaa7gc1J-wDVwdawRhtIPZXSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ تصمیم نهایی برای عدم تعویق امتحانات گرفته شد و شبکه خبر ساعت ۱۲:۵۰ امروز زیر نویس کرد: با اعلام وزارت آموزش و پرورش، امتحانات نهایی از فردا و بر اساس برنامه اعلام شده، آغاز میشه.  @News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67779" target="_blank">📅 13:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67778">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2gMhdm4QJlQte11G4BKVfP-iwldSbFoZvUccA2PP9h-tmaH6TyylAKaBrhA9oy_nQmakrEX8RECMamcmnNTipv4GVTSv8O1HyWUk_MIvU6s60BYihPVbyIkJ5Us5qDn7520HYyKzMNmxkOQue2zIyR8VvpUCAY6lsEALqqpgbCI8mdqbvd5fKZeiH7UY23d_o4QpEouuxG97t9c80gsRosNZZLBlQkfOzm7U697j7XLaR1gQyd5P4oasehFSNqWDaZwzTfkt87lzlwtLf1N3odU1OH8QGZmUBwj1orbYF2-az39nLsjsL8YjN7sy9uaVX3iBErZzGPb1zVbVUAw1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ تصمیم نهایی برای عدم تعویق امتحانات گرفته شد و شبکه خبر ساعت ۱۲:۵۰ امروز زیر نویس کرد: با اعلام وزارت آموزش و پرورش، امتحانات نهایی از فردا و بر اساس برنامه اعلام شده، آغاز میشه.  @News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67778" target="_blank">📅 13:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67777">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e80649858.mp4?token=Sab8sSjKmXcGaZbO9K8VjYQ2UvyeTxGvC91t1tXe-dtx0Jq-WYgOqSnEZTeEiGZnj8vpXLguoQ43OBxrSui7FvIj9G3F6kBw82AOQUs4EcJ4mRjLvWUS1Bdy1Q7ugIDuI5KxXk4can04pVSlQRHjWh2W_xFIOjTQkZuekC6RzQ02TjaZ8sguxog21BvKQbkRwTHHN8en7L6fqWfLehygHo7aq-vCC3We9EIIZuFHyAT6hq9gM3B_B9cteV61S7j_KTc4oP4szlbkWHjYu2c4JBJIn5VgCchZHqqKMwHTDOflxyQJKqQiyoc5bmgDLJK_N1WPlg1GlZUvaQlfzEn6pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e80649858.mp4?token=Sab8sSjKmXcGaZbO9K8VjYQ2UvyeTxGvC91t1tXe-dtx0Jq-WYgOqSnEZTeEiGZnj8vpXLguoQ43OBxrSui7FvIj9G3F6kBw82AOQUs4EcJ4mRjLvWUS1Bdy1Q7ugIDuI5KxXk4can04pVSlQRHjWh2W_xFIOjTQkZuekC6RzQ02TjaZ8sguxog21BvKQbkRwTHHN8en7L6fqWfLehygHo7aq-vCC3We9EIIZuFHyAT6hq9gM3B_B9cteV61S7j_KTc4oP4szlbkWHjYu2c4JBJIn5VgCchZHqqKMwHTDOflxyQJKqQiyoc5bmgDLJK_N1WPlg1GlZUvaQlfzEn6pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
#فوری
؛ تصمیم نهایی برای عدم تعویق امتحانات گرفته شد و شبکه خبر ساعت ۱۲:۵۰ امروز زیر نویس کرد: با اعلام وزارت آموزش و پرورش، امتحانات نهایی از فردا و بر اساس برنامه اعلام شده، آغاز میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67777" target="_blank">📅 13:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67776">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:   1000 موشک در حالت هدف‌گیری شده به سمت ایران قرار دارند و در صورتی که دولت ایران به تهدید خود مبنی بر ترور رئیس‌جمهور مستقر آمریکا که در این مورد، خودِ من هستم عمل کند، شلیک خواهند شد دستورات از قبل صادر شده است و ارتش آمریکا آماده، مایل…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67776" target="_blank">📅 13:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67775">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
ان‌بی‌سی نیوز به نقل از مقام آمریکایی:
اگر ایران امروز در بیانیه اعلام نکند که تنگه هرمز مانند قبل از جنگ باز است آن روز برایشان روز شادی نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67775" target="_blank">📅 13:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67774">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
مجتبی خامنه‌ای  قرار است تا ساعاتی دیگر پیامی به مناسبت تشییع جنازه پدرش علی خامنه‌ای، منتشر کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67774" target="_blank">📅 13:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67771">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70c6c6a4dc.mp4?token=q1siNxInuXuiCaTXg6_4ZRbyt87NbYucMdo4Cnw2LLMne6Yj_AbA9AZQzcTTBMxK9Sx56KvHJ49809FEM9HafaE9AK52KLy4de2f2_aNsN1Z71n1HMnnUZjKjPcu8y3wGtUDH_-tagD6NbVFdfGiaXTSDKiTRs-Snlf3x6dcjDkz75i-Im2mRydoNFCZfuzTFh36PEDbyGF2J-5iMW15rLjZ4Sklnj6h4biUAYoKHPAKt3RFDD8Qee_rV7R3tNmublvtVYMKsS0BIEBz9o7LlSZOBwUEt0rxzydRcKixmUCiLPETWd7aTl-f6obZPggl3N8cmnyr-FOc9aQu0LtcTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70c6c6a4dc.mp4?token=q1siNxInuXuiCaTXg6_4ZRbyt87NbYucMdo4Cnw2LLMne6Yj_AbA9AZQzcTTBMxK9Sx56KvHJ49809FEM9HafaE9AK52KLy4de2f2_aNsN1Z71n1HMnnUZjKjPcu8y3wGtUDH_-tagD6NbVFdfGiaXTSDKiTRs-Snlf3x6dcjDkz75i-Im2mRydoNFCZfuzTFh36PEDbyGF2J-5iMW15rLjZ4Sklnj6h4biUAYoKHPAKt3RFDD8Qee_rV7R3tNmublvtVYMKsS0BIEBz9o7LlSZOBwUEt0rxzydRcKixmUCiLPETWd7aTl-f6obZPggl3N8cmnyr-FOc9aQu0LtcTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعد از انتشار ویدیویی که توش یه فرد ماسک‌زده برای علی خامنه‌ای نماز میت می‌خونه حالا طرفداران حکومت مدعی شدن که اون مجتبی خامنه‌ای بوده و بصورت مخفی و بدون جلب توجه توی مراسم حاضر شده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67771" target="_blank">📅 12:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67770">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJV1UJwaND-hA86zRXVNHoxqip6sI6O2pmT-C-mrXsi9-47S6FPvYjcYmVqyM4YKxgmJ5CxtJu50b1Y4Sp5OTcCchbZRgg_q6K4JCAr-cN0FMJTbNLdLPV_-ulKW3F3eY73u_TWg2aB9YTHJ7Rd96o6lSyJnTH5x_RX7IvusidxhYns45CXKlML1epwL1mS8nkaKcxz7bGlx3qA22-vIH4AKHYIkXSV3B5hscvx-fss7qVdxrc93QmLRmkujsQANNZgoZ4Sol0ThbIEdSgLmQua6fx8cnZgAilwYEZ3A82ggmuB6VG8YKRnw2YEMrM0Tu2dgyBLBoY2CkliwMA435Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
1000 موشک در حالت هدف‌گیری شده به سمت ایران قرار دارند و در صورتی که دولت ایران به تهدید خود مبنی بر ترور رئیس‌جمهور مستقر آمریکا که در این مورد، خودِ من هستم عمل کند، شلیک خواهند شد
دستورات از قبل صادر شده است و ارتش آمریکا آماده، مایل و قادر است، برای یک دوره یک‌ساله که قابل تمدید است، همه مناطق ایران را به طور کامل نابود و منهدم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67770" target="_blank">📅 11:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67769">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iS3gudT1DdvYmg_626f_5cW4wQGvOU2SfEscdU-8fupIeYWeLFxOkPcGICTf98UM6C0zSvQokh3JjtLZZubC2n--izp6lGJJ29Qkmvo8c17WDkhAux6BVnglEYgjeUVZgIGoMWp_siKab3dK1aknqBjvdpUnmNk_-u9pz3JFOhWBSDgTg9j6z3Pk_Dve6dqBc2qRBMgkEzDjBuIioBpVDnr0nIQ--d7QnYnEhCuwDioGaQDD15JoQSNAzvbkZozYrr5zc3uxWajExVwi9pGRnbhz2f0Oy2F6J9uJNCNhZ-cyzPwpkYDAglzCiYNgd5G89rcyGdTGWxtQCVCvq4RKNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تعویق یا تغییری در زمان‌بندی امتحانات نهایی دانش‌آموزان وجود ندارد
صادقی رئیس مرکز اطلاع‌رسانی و روابط‌عمومی آموزش و پرورش: آزمون‌های نهایی  بدون تغییر و بر اساس برنامه ابلاغی، از ۲۱ تیرماه آغاز خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67769" target="_blank">📅 10:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67768">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d25ed65b27.mp4?token=gl9DWW-FnkoMp1bKc4ZRy6BNIP-acGIA0o3nXrXHQoUB035iCjN3ECX_bmUAiWfQ2SRt3x76BTKaywgvFKhRr74NgYMte4yl962SyG5sfpArgn6JzfJKqh5IzSOmHRdrA1nJxOu7gVvJ82iUnU5Jmcx1j9pXBq0ROtGiopwmuSV5PtEg1LoY6NPcK2V0SZDzmE8wnyDtaaxOIV0a3_11OSm3RGEJCuO06rdhJQCTWnNHGwq984VvyU8_eWcqcgMGJ1RI52K5GCO0BfQJQkF9TPUKtsoo5-Ac1A2Xajr1uCH0fllJ22K7nQ_1rmfFARbf67MvmIVUi2pGshesp71qNS6SCglKcJsJ00iXU2ondrUPN06wJFApR_CHsElWot2HaBSdVzv2m7JusU55K7nAb6ETUEbDG4UO4GZANgrBcDbEk15eyvUC4bqOIFINlDdODCAFYndc8GcdSPi0eJrIYuCCab9URK_VUHmTLEDIwdtg5ALpHqdxsOeSr-_pY5HuEv8mYuwoUUXdsaru2jARNa6dvBmD7SJpX6dA4kN9QB04VD41eldYzcqtAx9g9axdmkkikvepgY7u0TuK8vJtn4Q0TXRRccPJPTEEq13bOdzm4S9-MlPQHkf0k8u4WpEIEju5Dp5MEhGH7SOpy74NLnOYGYioCE6oSPyeBOHXnlM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d25ed65b27.mp4?token=gl9DWW-FnkoMp1bKc4ZRy6BNIP-acGIA0o3nXrXHQoUB035iCjN3ECX_bmUAiWfQ2SRt3x76BTKaywgvFKhRr74NgYMte4yl962SyG5sfpArgn6JzfJKqh5IzSOmHRdrA1nJxOu7gVvJ82iUnU5Jmcx1j9pXBq0ROtGiopwmuSV5PtEg1LoY6NPcK2V0SZDzmE8wnyDtaaxOIV0a3_11OSm3RGEJCuO06rdhJQCTWnNHGwq984VvyU8_eWcqcgMGJ1RI52K5GCO0BfQJQkF9TPUKtsoo5-Ac1A2Xajr1uCH0fllJ22K7nQ_1rmfFARbf67MvmIVUi2pGshesp71qNS6SCglKcJsJ00iXU2ondrUPN06wJFApR_CHsElWot2HaBSdVzv2m7JusU55K7nAb6ETUEbDG4UO4GZANgrBcDbEk15eyvUC4bqOIFINlDdODCAFYndc8GcdSPi0eJrIYuCCab9URK_VUHmTLEDIwdtg5ALpHqdxsOeSr-_pY5HuEv8mYuwoUUXdsaru2jARNa6dvBmD7SJpX6dA4kN9QB04VD41eldYzcqtAx9g9axdmkkikvepgY7u0TuK8vJtn4Q0TXRRccPJPTEEq13bOdzm4S9-MlPQHkf0k8u4WpEIEju5Dp5MEhGH7SOpy74NLnOYGYioCE6oSPyeBOHXnlM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی رحیمی (زاده ۱۳۰۰ تهران – درگذشته ۲۶ بهمن ۱۳۵۷ تهران) سپهبد نیروی زمینی شاهنشاهی، آخرین رئیس شهربانی و آخرین فرماندار نظامی تهران بعد از ارتشبد غلامعلی اویسی بود. وی از نخستین افرادی بود که پس از انقلاب ۱۳۵۷ ایران و در ۲۶ بهمن تیرباران شد
👑
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67768" target="_blank">📅 10:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67767">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95215f1b5f.mp4?token=g4cJUBm8p8hcVHFVCk8qVGp33PHHTlphBoGMQQ0ZdeQuptAbXPket3poWDUlXsMFcdzqYdMzrMu10vzETlgJHEZlh5c6bsgNVDkSGpW9hrlBhIYyPjveLhQgZOHm5RE0nijVcZIWX_F6Mq-9I_plrU-FOG1PHdwyoaBpOvUQRgkbdK7nuVHQv6JIC0NQLmBkkGyJ3oVG9oW-yUDw1j3M6qXP0LdzpTp7ZxSWGbq7Ro4bfNRWFC_nZsnvPUAq0dRnVkN5Ds5yyF-uV9feHfO_J8enK9rSDk4s9fMHzm2glURupg2OW6wiIt1U_LMZri0i-iS0nY3p6c4J9rIC4wv3FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95215f1b5f.mp4?token=g4cJUBm8p8hcVHFVCk8qVGp33PHHTlphBoGMQQ0ZdeQuptAbXPket3poWDUlXsMFcdzqYdMzrMu10vzETlgJHEZlh5c6bsgNVDkSGpW9hrlBhIYyPjveLhQgZOHm5RE0nijVcZIWX_F6Mq-9I_plrU-FOG1PHdwyoaBpOvUQRgkbdK7nuVHQv6JIC0NQLmBkkGyJ3oVG9oW-yUDw1j3M6qXP0LdzpTp7ZxSWGbq7Ro4bfNRWFC_nZsnvPUAq0dRnVkN5Ds5yyF-uV9feHfO_J8enK9rSDk4s9fMHzm2glURupg2OW6wiIt1U_LMZri0i-iS0nY3p6c4J9rIC4wv3FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
انفجارهای دقایقی‌پیش در مناطقی از تهران بدلیل خنثی‌سازی مهمات عمل‌نکرده بوده است
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67767" target="_blank">📅 10:06 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67766">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a14613e56.mp4?token=gl7yBTDSxNt3WpJ-TFZWg9TBqY4FxKs8t0H8Gb7jBIfkvE_nCkDJX7DWGibCbnpLRpEt_j6Hvb25kAqiXMDNet-8F-EHKmhfEt_MU1ieY5H6yOoD0APYxSpYMky7fcm1nmAMKauJKFOWTpIh_nW_REpO-1jX2MSwamS0_gfMyxfYwv7OyPdSXfBs8c2htpeNikZdOLKgk7KBSSz2cIxxu79wZhIE-7N79i9Wf5IYJ3ZNVDz05azYvpv-K8PhrfzV6qsn6XUEcHicM-E6ZNUS0iddNMc8R_POluDwaHUu_KHh0fleO3H28-q8MqC2bcSiFjNULPnxiEd0SUbegzY1ujHHu6vRUGJ9FBlntuiQyfDXE08EVxqT2_s2xvTFE5cSUeHSufQ1LEQrLgu9JCQ1HeFeiGHh4YafSuRVA-RFm8PiqgFTUybfobG54rhQRcjW2jC63sgR7w2T_P4BFXPeNeSVYVaFOrANlhnaZjNxl5QDouedSjq6ISkOjZUYGsnz7qBmDsQ8MAz-FHgS0WC5zPqWVVyjIOObXwWViqhZQ8tYcHKyI8-fwOJc1IyckoKqZUCzV_uHgXpFaLWV7C-n1kSIaF-ubRnopQV7r2JtfedgxH5amiRE27jO_8MHeJnuHBSz76HpcQNNbXqVA_6_M9bNL9yt9bHqr4zRI67FeK0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a14613e56.mp4?token=gl7yBTDSxNt3WpJ-TFZWg9TBqY4FxKs8t0H8Gb7jBIfkvE_nCkDJX7DWGibCbnpLRpEt_j6Hvb25kAqiXMDNet-8F-EHKmhfEt_MU1ieY5H6yOoD0APYxSpYMky7fcm1nmAMKauJKFOWTpIh_nW_REpO-1jX2MSwamS0_gfMyxfYwv7OyPdSXfBs8c2htpeNikZdOLKgk7KBSSz2cIxxu79wZhIE-7N79i9Wf5IYJ3ZNVDz05azYvpv-K8PhrfzV6qsn6XUEcHicM-E6ZNUS0iddNMc8R_POluDwaHUu_KHh0fleO3H28-q8MqC2bcSiFjNULPnxiEd0SUbegzY1ujHHu6vRUGJ9FBlntuiQyfDXE08EVxqT2_s2xvTFE5cSUeHSufQ1LEQrLgu9JCQ1HeFeiGHh4YafSuRVA-RFm8PiqgFTUybfobG54rhQRcjW2jC63sgR7w2T_P4BFXPeNeSVYVaFOrANlhnaZjNxl5QDouedSjq6ISkOjZUYGsnz7qBmDsQ8MAz-FHgS0WC5zPqWVVyjIOObXwWViqhZQ8tYcHKyI8-fwOJc1IyckoKqZUCzV_uHgXpFaLWV7C-n1kSIaF-ubRnopQV7r2JtfedgxH5amiRE27jO_8MHeJnuHBSz76HpcQNNbXqVA_6_M9bNL9yt9bHqr4zRI67FeK0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
سید علی خمینی، نوه خمینی:
«هر کسی که بخواهد برای دستیابی به صلح با آمریکا مذاکره کند، خائن است.
هر کسی که پیام‌های دوستی برای آن‌ها بفرستد، دهانی نجس دارد.
مشکل ما با آمریکا، مسئله امروز یا دیروز نیست؛ این مشکل دهه‌ها پیش شروع شد، زمانی که آن‌ها کودتا علیه ایران انجام دادند.
اما با آنچه اخیراً انجام دادند (ترور خامنه‌ای)، بذری از دشمنی کاشته‌اند که هرگز از بین نخواهد رفت.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67766" target="_blank">📅 10:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67765">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ant37WIoYhs9m8c6y3BYXBRFqqdrpv8-SC8Dy-PpZyKFXr-KgeB9pHdBipNDwQ_8D-0Z-xNhf_47T5HUOino4Z6G1FflLKNEQihgF6b36mhiqzQtHVK-TWCecB3oB4Vqg_AzDueEhIgmSDqs_9L5bpBgtDGSqumlc3wte3XcswtBpGqVBbDd6PlGM3Wmbx_TTE41sqGyxIz6IToU7qM4KMPuAjxSAoy4wzpDLGn8MDp7opNcN20zurRdemUkgZQWv2cCxCBhR8_pKlGRtVps_dI28gMMHfpACd9uuBUiWH78A0OcfbqqH3ThsGeQUO1rBGM9Yq0hTL9h4AbrEsX-mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
اسکات بسنت وزیر خزانه‌داری آمریکا:
فردی که «رهبر عالی» خوانده می‌شود، در حالی که رژیمش رو به فروپاشی است، در انزوا پنهان شده است.
وزارت خزانه‌داری همچنان از تمامی ابزارهای در دسترس خود برای منزوی کردن او و دیگر نخبگان رژیم از نظام مالی جهانی استفاده خواهد کرد.
ما این دارایی‌ها را برای مردم ایران حفظ خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67765" target="_blank">📅 09:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67764">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app.apk</div>
  <div class="tg-doc-extra">51.3 MB</div>
</div>
<a href="https://t.me/news_hut/67764" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📱
اپلیکیشن اندروید بدون فیلتر لنز بت
🚀
🛡
ثبت نام آسان و سریع
✔️
📱
اپ
ل
یکیشن را روی موبایل اندروید خود
نصب کنید و بدون نیاز به
🔤
🔤
🔤
وارد سایت شوید
💬</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67764" target="_blank">📅 02:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67763">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/hEFWXZd9nYgcS9elrMTT6H__LKlK18xwSSoTE7MggSeXodl97jhl40ny1g63uEOHOSRvu3j1GROlPHwqkyNZJWi0BKK8BFVipsyTMygfrLvS2KH6aUl7X5FrJ-F94R_4ykI9AYZJdZESdj5HCBf7ssXoBmrCmGKiWB9dYkpTk20NYlpP7d3Tk_Jb_j13ZE9oZVl7MHlJdEMaQ3MoOqspGVw7yFoWIBPSIITvsnWLGb8ILOoRad8l3jJDK5K1d-LlNWvuHKK9R4VH30q7TuTU3p-nNPwmn5uGoEq9s6sAWKo2zcCUrLfQwb1vR54MgPHtGHOWZRA09DhdCUlF8zh-gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
قهرمان جام جهانی ۲۰۲۶ از نگاه شما کدام تیم است؟
✨
با پیشبینی قهرمان جام جهانی شانس چندین برابر شدن بردتو امتحان کن
🚀
💥
متنوع ترین آپشنهای پیشبینی در
لنزبت
😮
بونوس
🛍
0️⃣
0️⃣
2️⃣
خوش آمد گویی
💯
بونوس
🔤
0️⃣
0️⃣
1️⃣
برای هر واریز
💯
بونوس
🔤
0️⃣
0️⃣
1️⃣
کازینو
🏦
کد هدیه
0️⃣
2️⃣
🔤
🔤
بعد از واریز
🔣
0️⃣
3️⃣
کش بک هفتگی
📇
امتیاز وفاداری با انواع هدایای نقدی   روزانه مخصوص کاربران فعال لنزبت
💵
پشتیبانی از تمامی ارزهای دیجیتال و کارت به کارت آنلاین برای شارژ و برداشت
🔤
🔤
🔤
🔤
🔤
🔤
🔤
📱
@lenzbet_official
A19
📱
https://www.lenzbet1.living</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67763" target="_blank">📅 02:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67762">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qs_VPIUjxJDfIc8JZdq-SSTQ2OWRkZ-_OJVJO5jA1hI8ggQFcDWidrDwKOE3ycoOb5gz83MuAyehZGyH5zgz5f4uLqFR-miyigbcYV1JtNq43pKdmTjN92GRCo3zcey8NG3g9hbwtbqgwOZEFFluz5COazR-yuQoTCNXY-JeDLFNbHIAelOSQx5C-fTQzUBfqA3AGeNHcRjOg48LCAGIdDTyxnKihprxpV0f4hHQ6dzTkITBS7_D9GChz2FoyFZpcC57Ks7NpmLpmt4YvxLNiNRxzNbAiPYyZ8kHfRNa6PlnIRRAoI0197WVKA191E1bankBYcpA8Pfn6sEzjhraGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حملات ارتش اسرائیل به نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67762" target="_blank">📅 01:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67761">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
❌
یک مقام ارشد آمریکایی:
ایران‌ با عواقب وخیمی روبرو خواهند شد اگر از انتشار یک بیانیه عمومی فردا خودداری کنند که در آن اعلام شود تمام مسیرها در تنگه هرمز باز هستند.
اگر این موضع [آنها] فردا نباشد، روز خوبی برایشان نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67761" target="_blank">📅 00:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67760">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t72wwLuBddsBXRRSzu1KBY6EjbxYCwz8ATniTZCz7WwdbJ4zU1coM3s5SZ33UikBAMKaPHDeHcjhzVhaMHnPjrM41XH5-AEqTAuUzjbXqTDX8Jt3HMq-nCMZ5NhuJ-YLX21PVQCyXX-dloysQjI7Iqm6mqGVai2Dp6EeSI2c2qiInKVS875cdaga4ryw0Ye1jZkBbdnPplmjz2Wii6z4KfCKQf0LjQVXPbriYBPeh6-Xp1KjKPcPQaKHLkjYBvwl2FkpPnFYfsGH9s_keZUtgBvNCk2cjQVbtRt1qjRBxA103_IDZiCnBiedp34rU5YsZlBuNCQcS3TEnUzD8RjtPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید:
به گفته مقامات آمریکایی، ایالات متحده به ایران تا روز شنبه مهلت داده است تا حملات در تنگه هرمز را علناً محکوم کند و باز بودن این تنگه را اعلام نماید.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67760" target="_blank">📅 00:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67759">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">کشوری غنی، اما مردمی فقیر
💔
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/67759" target="_blank">📅 00:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67758">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
وزارت آموزش و پرورش:  ممکنه امتحانات نهایی به صورت داخلی برگزار بشه.  فردا در جلسه ای در موردش تصمیم گیری می کنیم.  @News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67758" target="_blank">📅 00:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67757">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
وزارت آموزش و پرورش:
ممکنه امتحانات نهایی به صورت داخلی برگزار بشه.
فردا در جلسه ای در موردش تصمیم گیری می کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/67757" target="_blank">📅 00:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67756">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/024bc9f4e4.mp4?token=pHRMmWH95pjyuJNLya5GRcj2XG1zSe9j_LNIRf0AFHKnq9ASrMDB7VIU4SJDklEOL1hMZlj3s-x8Pr7HYwIhNQ_MGqwgshytwc5pdyHIuUn_eXgZCxu7f2IaQbwyRtdmNGsczWc_rAFbnorR8HMLOUtenLX0areEYA6HhVs_DTAM6To_hdAeB5yfL5pSfITRRF-12eXfr4XCG6pLELzLSAWsaEvC7yjsQcLQjh3LkVm3bMxj5_rXrgNTl9jJUOvbjkYXBEjnduMoaaN7hXabW-3C7xoSE3HJOdZ3xrWv5-U823l-S-lc088ynxdKuDht7eJIgtQsmg7w2FVw-7t4DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/024bc9f4e4.mp4?token=pHRMmWH95pjyuJNLya5GRcj2XG1zSe9j_LNIRf0AFHKnq9ASrMDB7VIU4SJDklEOL1hMZlj3s-x8Pr7HYwIhNQ_MGqwgshytwc5pdyHIuUn_eXgZCxu7f2IaQbwyRtdmNGsczWc_rAFbnorR8HMLOUtenLX0areEYA6HhVs_DTAM6To_hdAeB5yfL5pSfITRRF-12eXfr4XCG6pLELzLSAWsaEvC7yjsQcLQjh3LkVm3bMxj5_rXrgNTl9jJUOvbjkYXBEjnduMoaaN7hXabW-3C7xoSE3HJOdZ3xrWv5-U823l-S-lc088ynxdKuDht7eJIgtQsmg7w2FVw-7t4DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
اسماعیل بقایی سخنگوی وزارت امور خارجه:
ایران اجازه بازرسی از تأسیسات آسیب دیده در اثر حملات آمریکا و اسرائیل را نخواهد داد و قطعنامه 2231 شورای امنیت سازمان ملل عملاً اعتبار قانونی خود را از دست داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/67756" target="_blank">📅 00:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67753">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OrAAOx8yri1zZF8PhYiLjJYOEKzMnknTeTQ3uaLs1qpq-zZlWfrNPgvIBk8km9UvKNDEjN73h9WgzM3zkopIqYNVnnYQV2-qLU6S3Uj0aMvcBdM-baKDdC1axRBTKzKXxA5gaK83SZ01KLoS8wzRY2hdLOfXZAQ3yLSLqD3kihnHmS3bX2H0iNugaF4qC0NXZtxLfE1VseBxwN2e6RhUmWWrW-LSqcpUnjgAwMl7_jdZ8tWWbkTjJqC1atNH7fDCZVVMxcsoAPke1G9AKq4SQ8aDhKuXNk7G3ZgcFUOFlKxcVwV2I-InWgCaphbDtpYTv5MnQZoCYupm4E4RetEQrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a4TOat7wOVM0DA88DiIE1aAMACf1TMz2MZXdkEyfw2eeNMYJcieWQbxbS53gkJYjTKOpXUaD2ykF7TkKPTyvemEFzGRDhEVwrqgNTxZ1e3VekMk_ATaob881WpHYJeLosipGoRakvr9qWinICPenbjL8yJqLwZR9NLsvSRTmDJwyAIqkah9sq2c7Db64j3nSR3Llh6xxsmTHX5KtPNMnaPfZ70mLy8ESw2G5UqW5yIdfiswZGunNACqxInmkNq3qG5cfyXLBne6NQnPmZVDPJ5tH0cyjmSlgv7AvAzibF-_B614DU57_4U7Zhy4dIZ4Eap7gbThLwQBzqAVGwbiYXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oXc7xZyiPGOPzeb-XgoVQbKEpmA4twvGxlHJ6cQkOIMwLum-9ul4tLdiTgY9zlhYWwcJyNdQ29D7NeTPxnfu_6qQWjlhMJGduguFdXgg49jX7wINPk8ipL_Cf5xXase2qln5QEv4A906k3AYy7F8K9f3EnOddVLwmoyd0Y3uEyEizECXcCw5y35c2H1r7-Cq1H5H7eZIKNz-LddXuMFiaidg28GFlpf_lh_VPdsCz0dpY3EvWDmOnyn7dCNZABUwusPXMKQ-2gAimjH7QB8Ge0iE5f-MevT1I-WudsddMbUotcgF1RN98w0X2tPLcKS7yOWbkZlMgWXBz4bWsjzOzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
⭕️
شبکه خبری CNN تصاویر ماهواره ای  ادعایی را منتشر کرده که نشان می‌دهد ایران در تلاش است تا تاسیسات هسته‌ای واقع در پارکچین را بازسازی کند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/67753" target="_blank">📅 23:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67752">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08e999307d.mp4?token=fXDi3GGUMhhCfaCg2AVbH4rY6QMzxIvSlUvvUjEK1kZ7vyfFUOl2nkdVm9dBl6EjLIrY25BxY2hAaJsv16n7hsW1Q5WsPXHwLMYnC2ESL_m7SkC1IXxl_al0t2FqTvP2Uj2WX-Ji-rlqGCC2C2yQZvX2ekYzkxOf0ziz5XXw3ZRoDX6gmN0_DIqqHOD7gUqSgSIeD54VyrKgYR5iga6JVC6BbzFedZ1D3DCK9c-mC_BblYe1AvzbGyRjy8o6BTcmXnDvebg6ExrLRbH_IIA0-LJvqDuyzZkUiJdovDi29jqt1hGJaLValAl7UbxlMGKzyau1oUeI3qjHSfOGiiuZxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08e999307d.mp4?token=fXDi3GGUMhhCfaCg2AVbH4rY6QMzxIvSlUvvUjEK1kZ7vyfFUOl2nkdVm9dBl6EjLIrY25BxY2hAaJsv16n7hsW1Q5WsPXHwLMYnC2ESL_m7SkC1IXxl_al0t2FqTvP2Uj2WX-Ji-rlqGCC2C2yQZvX2ekYzkxOf0ziz5XXw3ZRoDX6gmN0_DIqqHOD7gUqSgSIeD54VyrKgYR5iga6JVC6BbzFedZ1D3DCK9c-mC_BblYe1AvzbGyRjy8o6BTcmXnDvebg6ExrLRbH_IIA0-LJvqDuyzZkUiJdovDi29jqt1hGJaLValAl7UbxlMGKzyau1oUeI3qjHSfOGiiuZxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیشب ترامپ رو تو مشهد دار زدن بعدشم ماکتشو سوزوندن
گفتن خودشو که نمیتونیم بکشیم حداقل ماکتشو بکشیم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67752" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67751">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3bQeWSLaX-Vl7QoMSd1wkkOzN7A6pb3FxhRCrWEc1bvgLUlCCUxVNNdZpbg7IrYmK9BGZCnuiIpPSPQZk9IlkK-wUeiVxycqEiKTqoH3XGl6P2n9dU-kL1TgSPg1T6baVKZw51w4C3H_JWlUsNKRi3RXIDxVA5D61Nu4QegOxUiXM2hvkQ2Grh5uDjywJYYFAjO_LV2clPPlWQhUMp-Tio2vCIuxNDx__zfmc0mbXG9N9NL33Nc9Zrcps3wBOp5Ua4fgTlB6IeeE2155o-YXeXDR0CLT71IIL9DDSKE3ueBRHN7qQ9g_2MgFPttf0sgrLa8IFUSb4n__9fRIclGjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
قالیباف:
در جریان مذاکرات، به معاون رئیس‌جمهور آمریکا توضیح دادم که ما به شما اصلاً اعتماد نداریم.
به نظر من، تنها کسانی می‌توانند با ایالات متحده مذاکره کنند که برای جنگ آماده باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67751" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67750">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">⚽
تحلیل دقیق مسابقات فوتبال اگر به آمار، آنالیز و بررسی تخصصی بازی‌ها علاقه‌مندی، این کانال برای توست.
📊
تحلیل قبل از مسابقه
📈
بررسی آمار و عملکرد تیم‌ها
🎯
نکات و دیدگاه‌های تخصصی همراه ما باش و مسابقات را حرفه‌ای‌تر دنبال کن.  @bet_maxxx @bet_maxxx @bdt_maxxx</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67750" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67749">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromnegin</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owtAa_CtjWYxPQyDth1mllwI5TBuQ2NtcCBVj2tmGJp50x7n_re9test0JLZuZb0ZWFCg5zz8NRCTz72fF2RCHMd8oGdXQRkuFoTYZbQp3EpqOtW3jjiHfX-IYb2rIOemoaNIEKgyV2t6qPtxRm9F4Sbh9G2c_zPgoLHZ-MqbQP4tNvxeemww2b6c7GuoMKVX59c6npcWCj44ZezBDlic0TKxShQDjiwexZXapfHDfH9Ccs3c8ZBHbWSJnvmCIqAgk3-MHZINrJRzHzueBKcyDMiVyI3h158Ri7zCETjcQovwJg9zVWo6isFfvnewU_irUJy3YcbUGOPWPxbN04dxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
تحلیل دقیق مسابقات فوتبال
اگر به آمار، آنالیز و بررسی تخصصی بازی‌ها علاقه‌مندی، این کانال برای توست.
📊
تحلیل قبل از مسابقه
📈
بررسی آمار و عملکرد تیم‌ها
🎯
نکات و دیدگاه‌های تخصصی
همراه ما باش و مسابقات را حرفه‌ای‌تر دنبال کن.
@bet_maxxx
@bet_maxxx
@bdt_maxxx</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67749" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67748">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ad131e48f.mp4?token=v-oSfqYeUT2HvbZOSsm9UqCVF6X4sKCMb-QUTBE1UgCM1UtJ0071I3VO-cJDqMgbwxmvS-rYY7bAwhtzamxxJbMHaP8W-fvunU3qeIy41lgQZ084hv-4EFpq6xXkRF4grn9ne8v4kMAXAfyUu6RrwWwTJNfSrDrp-Vpqdh0ZSKKy0YTqaKPj-0CkbEw5BcVMD-yc6bb8pQs11aAh4aKu4Ofai-WqdX5fsYHacRUlC8K-zq1bWVGC6fkAaRzbNjX-JvlQQDfwW-9P3A3d6SSCuXvAUexytNTnqSqWrQL7_vNLZBKQfqAMDt7i2Mksndlc-LCHPQ6lHRHoz6KHxhXDXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ad131e48f.mp4?token=v-oSfqYeUT2HvbZOSsm9UqCVF6X4sKCMb-QUTBE1UgCM1UtJ0071I3VO-cJDqMgbwxmvS-rYY7bAwhtzamxxJbMHaP8W-fvunU3qeIy41lgQZ084hv-4EFpq6xXkRF4grn9ne8v4kMAXAfyUu6RrwWwTJNfSrDrp-Vpqdh0ZSKKy0YTqaKPj-0CkbEw5BcVMD-yc6bb8pQs11aAh4aKu4Ofai-WqdX5fsYHacRUlC8K-zq1bWVGC6fkAaRzbNjX-JvlQQDfwW-9P3A3d6SSCuXvAUexytNTnqSqWrQL7_vNLZBKQfqAMDt7i2Mksndlc-LCHPQ6lHRHoz6KHxhXDXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رونالد ریگان چهلمین رئیس جمهور ایالات متحده آمریکا:
در این سخنرانی، ریگان با یک روایت طنزآمیز، دیدگاه خود درباره نقش دولت و مسئولیت فردی را بیان می‌کند؛ روایتی که سال‌هاست در مباحث سیاسی از آن یاد می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67748" target="_blank">📅 22:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67747">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZLxxCpMlWwAUbnlFzJ93nv2E4F0wE5HJTzitsLc1JJg4V62QM6xW1-yHYIaPxNQ44sZbt2G474GQG2F3voXUZBdTpOlPCIsb8Y_9CXCDtmS5mma4CdE0zbZn3PPQ7-nboifhGycF5Tmx6PkTw0RX4XfsQNJPo4YkAsoNmonh-id2HtMv6iGw5clVXO9Nid8irvcOJWz7gYlWT-RMCNFKS3VDQnyOMvVlQRiEGjuUVac6BCkw6bYoidTQJhbRODkyVcXlDmcqkEDsqcFTpVCFrbuCgBZUBKKgiQzEiREDH-t9PIyDWDC7-zzTH-AjUVwHuvST7OAFAHh9fGCSQHBbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسرائیل هیوم: آمریکا و اسرائیل گزینه‌های براندازی جمهوری اسلامی را بررسی می‌کنند
روزنامه اسرائیل هیوم در گزارشی به نقل از منابع دیپلماتیک منطقه‌ای و غربی مدعی شد که ایالات متحده، اسرائیل و برخی کشورهای منطقه در حال بررسی راهکارهایی برای تضعیف و در نهایت براندازی جمهوری اسلامی هستند.
این گزارش همچنین ادعا می‌کند که در پی تشدید اختلافات داخلی در ایران، مسعود پزشکیان، رئیس‌جمهور، و عباس عراقچی، وزیر امور خارجه، با فشار فزاینده جریان‌های تندرو و فرماندهان سپاه پاسداران روبه‌رو شده‌اند و حتی احتمال کنار گذاشته شدن دولت پزشکیان مطرح شده است.
اسرائیل هیوم به نقل از منابع خود مدعی شده است که عباس عراقچی در تماس با میانجی‌ها اعلام کرده دولت ایران نتوانسته موافقت سپاه با مفاد تفاهم با آمریکا و توقف حملات به کشتی‌ها در تنگه هرمز را جلب کند.
این روزنامه همچنین مدعی است که یکی از گزینه‌های مورد بررسی واشینگتن و تل‌آویو، تشدید دوباره فشارهای اقتصادی و بازگرداندن کامل تحریم‌ها با هدف افزایش فشار بر رژیم ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67747" target="_blank">📅 21:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67746">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/We5iTmxL4fAjuqbXmLCcjMEwnesi1IybXqEp-50RqzO2exO-kJxVYOrst14_bJIr6buarPol9C4KL8Ap6jRoQsbruWv7GXP9UadNIakRDneCxEsT83627Hv1D3_ix03sRsnN-R1e7w3j9uDxo_L54Cf74OwYDxpwO20khGpilEN0t2nnAcxeJkFpf-QFUEJxmhMy6D9jMRWxL2l5WcAyqDCCfI5vUwCDMwDwy-DafXumSLdU8g9b2H3vVJSiHAa8g3iSfWqaMEiHdWoVIzLoO2TWFcR1I0CUTh01d2UA-gtjVPDn00xZIz6HUfvRIYzPttWHVBHn58edxLm-_EUeYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
باراک راوید:
بر اساس گفته‌های یک دیپلمات آگاه از این سفر، مذاکره‌کنندگان قطری با هماهنگی ایالات متحده، به ایران سفر کرده‌اند تا با مقامات ایرانی دیدار کنند و تلاش کنند تا تنش‌ها را کاهش داده و شرایط را برای از سرگیری مذاکرات فراهم کنند.
این دیپلمات گفت که جلسات بین مقامات قطری و ایرانی در تهران همچنان در حال برگزاری است، "اما واضح است که هر دو طرف تمایل دارند به توافق‌نامه اولیه بازگردند."
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67746" target="_blank">📅 20:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67745">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dCawr3OmP_f4TFQ95F7yIBmMtYaZEsSgVYeXIBBL0LQniX-uxP-zKxzoozUQwRDTT043TBg4SY7cx9N8CJnzXrETCY-74pFOGFNYJ9gJqcqPGbZc5DPrMtj-H_wa37Mu7k0n3P02vUVF4Qzb7FSbEaPKqboyCbNtx4TRlB58KgiaDLqJ72yCUPYwSI-qnGeQcrv_VNYyYFbzSzuTPUpcNJs4soOklG4-irWdeTy6Dwz85Fyq0PdaqDzvseEHDHjO7oZyOAlQonpV6Y7f0ZdNDRxIAvF0xssVDPOxxeK8Vvk67opvsokxA7uYYToZxmSc7hFT8W2FAaLE1JSJrZpRrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ به «نیویورک پست» گفت که دستوراتی صادر کرده است مبنی بر اینکه اگر ایران در ترور او موفق شود، ایالات متحده باید «به‌معنای واقعی کلمه، آن‌ها را چنان بمباران کند که هرگز پیش از این ندیده باشند.» او افزود که «مدت‌هاست» نفر اولِ فهرست ترور ایران بوده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67745" target="_blank">📅 20:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67744">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZscqkFlYO6YiR55jJWl7rK8twAhTkm0NitvzTUx6-l8wQufajaajJBX2CSeGnqaN-_Jg_g2kZ7MJ9nU8IPOaPr6egBfZoAM-ap-iKxCyBg7VPtEXz4Gldn5VzM5btV-uYjLIeJ0QTQXub4vYXuWLSUoR2x0a9B60e2Cg-6fw7p8GWZNF1oLQTTti0rLX3UlOF86RrO8Z9L3hh9l-Nd8yY6gMW_mOv2o0BSkLYenRNBT9ZKrvG_IMa1D8TZSinS-aDHb09equnts5Zht8X0Cr4024McKJ9UcWiH_uZUxpg1CBr8Di7Fk1azFGm90zfuTt6A4e6FpD06NCuQ-yG_guIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مرندی از اعضای نزدیک به تیم مذاکره‌کننده:
ترامپ و خبرگزاری آکسیوس را نادیده بگیرید. هیچ مذاکره‌ای تا زمانی که دولت ترامپ به تعهدات خود عمل نکند، صورت نخواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67744" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67743">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
آکسیوس:
پیش‌بینی می‌شود که ایالات متحده و ایران هفته آینده دور دیگری از مذاکرات را برگزار کنند، احتمالاً در سوئیس.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67743" target="_blank">📅 19:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67742">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/258d1105e3.mp4?token=L2HMTR29hZClaOAymjV2rbXS0xK-VvbkKfVEYGDBATyRUz-i0kj7KWdkVGWsdeJ_Zc8wfyljt1MHDAtXXQUG9fnZHa1nzxDmUaWB10mQ2h_MNbbpjhbftAJ4DLwd12N9gqUwWH96Y5cOjKegAIgq3P3B4KJ5uiujE3YBeSw2R_zV00zEzxJlqOwkhJ6hPczMJ1ts-TxKoC0N7oOS7RbPzkEe_B8XskOhc5KJ5Tbkhbed9-KV5Hr0lwvkkZSFiv1kzGriz7HNlM_9B-tVOb2z_WnVfpExz-gGSrAc1FymjxXNzrSAZ9nSWCGdizmc62f_9suyZ6brMa0OQOUk0P7MRA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/258d1105e3.mp4?token=L2HMTR29hZClaOAymjV2rbXS0xK-VvbkKfVEYGDBATyRUz-i0kj7KWdkVGWsdeJ_Zc8wfyljt1MHDAtXXQUG9fnZHa1nzxDmUaWB10mQ2h_MNbbpjhbftAJ4DLwd12N9gqUwWH96Y5cOjKegAIgq3P3B4KJ5uiujE3YBeSw2R_zV00zEzxJlqOwkhJ6hPczMJ1ts-TxKoC0N7oOS7RbPzkEe_B8XskOhc5KJ5Tbkhbed9-KV5Hr0lwvkkZSFiv1kzGriz7HNlM_9B-tVOb2z_WnVfpExz-gGSrAc1FymjxXNzrSAZ9nSWCGdizmc62f_9suyZ6brMa0OQOUk0P7MRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
آتش‌سوزی گسترده در مجموعه اکسین پلدختر در استان لرستان
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67742" target="_blank">📅 19:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67741">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKRP0az1mdGlpfX0TNw6i7MM8Ig6q8PE45l0nk0N9KSYDi1nuRc0r5kXQy4frTfeYV2W59l19V5lW9gwIhgaOdw4JsCC0WKwo4Gu5NCvjkn0qJeq2dPqrU1345SxoC3oIJgBwaAohexscXm_bzqS205cdRWbPJ47umaWXDYNaI_SarhbauGlIzSWbc-zQs5ka1AG6u6BTLTIgQpWeazaLOm825oB97TGD0D_gbCiN0k1TdOcjavSw2vCoZM2bvSIE-bd6X_JbboHQ6KNxiFULpa4QA2Hsy6F2i-5FPhHnbh80_gCAZnsjG-uDOQZYe_rGiBq-mJ5PTjV9oQF-vQTpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
انفجار در پالایشگاه نفت پلدختر در استان لرستان.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67741" target="_blank">📅 19:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67740">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgviOUHNGhfZ3BKYrJgkRnRyEzSZ9YIds16GPtxlbS90wXAFDTSK75Cy6Ux-YdS7LeNXZjsCx-RQy7W848tDWUbP3wXrElColDAxDSwUplwSaKIg2-Yy_JjoAhMakgA-8HWEEEfs5ITf2PfwAW3hLnPOcIBmxNr-X0gHw4s4X_OGJhV-jAcJNJ6cO4xKDsBIABql7QwfA7t45dUkS1aL3bk7gn9F1m716EBbGAUwPls7L3EELv5y-BfVT5DZOpaxeSfDMCrg_lp3h7TUI5q46MXqWXMdkKurr3CPvZTNgSMrT2uflU32J_ovZDKJc2u7OVmKu-rV0kyalCB_YApvfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
بلند شدن دود در کنارک پس از وقوع دو انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67740" target="_blank">📅 19:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67739">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d335d453d.mp4?token=S9zkbSezM1Ql0ZayD6ZDIcvNkCa4SoG0z8saFIm5rXeLVDu8RplzWNFcXccyOHf_qxHRO_Ns0cFG9z_5nk8OK1x5owPw2cMP8OXVt-5PovPKjST6cOA9DG9kK7srFeLvl4zdyIgkJmOdZlvEp14rnRlKcIus4PfEiI4WaurXSh-9EFY6ldSs7Mn-M8vjCR8Hbbjcr3_EZ2wPxDyrhOnFdRgOQqBkTS32foAA0bT-N5z4sp8QZ5rr9BTCtiDRbEirQVK1bg2vXxXOQL4IXaLtMIO922dSDk689Kxex1D0TTFwEnepPmxS_jPNns2U9dyVCBiUVBtCyvs5MQjP5Vo5Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d335d453d.mp4?token=S9zkbSezM1Ql0ZayD6ZDIcvNkCa4SoG0z8saFIm5rXeLVDu8RplzWNFcXccyOHf_qxHRO_Ns0cFG9z_5nk8OK1x5owPw2cMP8OXVt-5PovPKjST6cOA9DG9kK7srFeLvl4zdyIgkJmOdZlvEp14rnRlKcIus4PfEiI4WaurXSh-9EFY6ldSs7Mn-M8vjCR8Hbbjcr3_EZ2wPxDyrhOnFdRgOQqBkTS32foAA0bT-N5z4sp8QZ5rr9BTCtiDRbEirQVK1bg2vXxXOQL4IXaLtMIO922dSDk689Kxex1D0TTFwEnepPmxS_jPNns2U9dyVCBiUVBtCyvs5MQjP5Vo5Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری صداسیما:
اگه خمینی و خامنه‌ای، زمان امام‌ها بودن، امام حسین شهید نمیشد، امام علی حاکم میشد و امام حسن هم صلح نمی‌کرد.
پیامبر خودش گفته؛ من مشتاق دیدن اینا بودم و حسرت دیدار اینارو داشتم
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67739" target="_blank">📅 18:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67738">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzzwpYbCRzXMGRksUYQCMWxJDK9rZxdRddx_P8tJK-WES5oh7LKGd5-rsDcSdXLCrquZqYk6pYUK8D89WncFshYf3x3vjRh5qQcoQumK5C1CZpiWgLAy9EPAO__A3G8vrv2JWbsyPOFKAbysaSNJNzyjg7nMuLPD19yNrHDET8fgTZsx8m708qgq3gj208tIado9wYcb6HfGi3LGwY3AmX9CV2vpWpSch0ZWNYyy7_ZjI1npeU88vq1TnHFFoJYm6eowbPkb-efVAHsjXt6HKYZx2MWAXgOUa0JNSbCtGiAFix6yWxA440EJERGUkWfzC1cMrDZetmQsBtCxamG2IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایران با ما تماس گرفت و خواستار ادامه "مذاکرات" شد. ما به این درخواست موافقت کردیم، اما ایالات متحده به طور واضح به آنها اعلام کرد که آتش‌بس به پایان رسیده است. از توجه شما به این موضوع سپاسگزارم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67738" target="_blank">📅 18:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67737">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAPlh12nuJCBRAj75aZFd4J0_UBj865IzmBQQ48Hv9ZSbuvVnKD9CTIH0dzUQYnvaSoVm2N5kR7PaYTgKIQnaW8_rFrG-eksPy0q152-XbFDJw4SAFOYgjUew0Cf2mMDKg19UhwVDYPe1kVP-NsYJBoeQ9uLxk8HrSZUJQ_H0lQpDLmDgE6mVjcuvbeNERb_q7gF2odcVWIY77w-LOS_AcdzifE6miGWtBaE-yKz7f4L6y9n6fPX-PjfVTOnKWKTMS7igrOTmey2ZNFO_n-Xp9-T9PTVDYIhql-eHwiStQNlAt7PeZM9SmHYp3CSkgvnLKiQOAt8Lztc5XTl_jo8Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نیروی دریایی ایالات متحده امروز حضور قابل توجهی در خلیج عمان دارد. یک ناو هواپیمابر و اسکورت آن (حداقل 3 ناو جنگی و یک تانکر سوخت) امروز در فاصله کمتر از 300 کیلومتر از سواحل ایران مشاهده شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67737" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67736">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be0edc864f.mp4?token=n6mL0XeONMba-RWmlEzZdcViX1KyGnT2DLDO3DHpX_Rz-TrE7cBJUeyV-LY_-avnG9pVusAosW9gAlNCDXk0LEQNOQjAHemAmUwfQk3kEAyQnBrP0vJlnnjbC2MDPVm9uq6eO3J6HeqKU2V-GEfhr849DzMQvcJATMmUI9gxg6X-2GjuWfSligxLvd6BYvHFGwmajvdJz1YKiq85Zk2SHCYQco6bwUWLjIoWKeI7-6Tx8hl5Elm0yTfNW-gvEHlOhd3zlW7mgy_x-inFlhHvE_TABSI43ehvfBcmT2sgwbl_QDylGqSMeOea7rGpDudqLM7-I2N0gnIDj7oJ8tckug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be0edc864f.mp4?token=n6mL0XeONMba-RWmlEzZdcViX1KyGnT2DLDO3DHpX_Rz-TrE7cBJUeyV-LY_-avnG9pVusAosW9gAlNCDXk0LEQNOQjAHemAmUwfQk3kEAyQnBrP0vJlnnjbC2MDPVm9uq6eO3J6HeqKU2V-GEfhr849DzMQvcJATMmUI9gxg6X-2GjuWfSligxLvd6BYvHFGwmajvdJz1YKiq85Zk2SHCYQco6bwUWLjIoWKeI7-6Tx8hl5Elm0yTfNW-gvEHlOhd3zlW7mgy_x-inFlhHvE_TABSI43ehvfBcmT2sgwbl_QDylGqSMeOea7rGpDudqLM7-I2N0gnIDj7oJ8tckug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدیو‌ ای از صحبت های چند روز اخیر ترامپ که در حال وایرال شدن است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67736" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67735">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MelBet2.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/67735" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🤝
اسپانسر رسمی جام جهانی
🔵
کاملترین برنامه موبایل
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67735" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67734">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mGaZ9Njvu36Z6gLEtPr2aikxKiDSITVV-EuUBtI_XZ4_BH2hzYuf4S4u4g7Oct8ST-Lz23HGM5mcifhGxzCecPYdmE7o_XT9QY2ikx_PnHb4_9Bp6Y1yd1FQ9m5CvexMQ5uos6SQUlQcKCC9YzKFYCJcxo2hVHqRyU9oF8Cg8aDnsSo8AAv2DFcxIswDNY8SgaYNxZ3t8ADBxA1pJ8c0KJiG6pWw3lFmYXfvHtEdgdq_9Nz3ou_l3enqA8hOyKqabtlVRrWmDR_jEK33MTrNogWWme5b8faxz98KGypvBOzMIO7iyhRaD1ej6FNeciTjmZPxy0L1UimmNZWsXNszeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
55 درصد از علاقه‌مندان به فوتبال، فقط 4 سال یکبار شرط میبندن!
حالا چرا جام جهانی
❓
خیلی از نتایج تابلو و قابل حدسه
💯
مافیا که کارش دستکاری کردن نتایجه، زورش به جام‌جهانی نمیرسه و نتایج واقعیه
👀
به دلیل تعداد زیاد بازی ها، دستت بازه و کنترل ریسک و سرمایه آسونه!
🔽
🔼
💡
کافیه یه سایت معتبر پیدا کنی که شارژ کردنش آسون باشه و بدونی پولت امن میمونه، MelBet اسپانسر رسمی جام جهانی، همونیه که دنبالشی!
برای ورود به سایت فیلترشکن خود را خاموش کنید
🆕
Link
🔜
MelBet1.net
✅
🆕
Link
🔜
MelBet1.net
✅</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67734" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67733">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3d6c6e5dc.mp4?token=URN0ZIFwwrZE7eHB_XLphcyV0LBEqXVq6vYOGliT6J6gvhn8Q0XphobPEPgIUqgq2WcpEi_1CPfHaEExD9P3xhNBCAtnmCHjpFFAvAGcVR2jMtDnFTv9e-3FddMhmUyYtMiP2JTqtS4wYgk5pe-8CDmxOx9BwImv94C1hcVrMr0EOyILcz55BSbUz20YyDFAgG7lf-lrkhVwPO2s9wytXIg3RcaX-OYtzFzhkeMUuFg7dwqvO44d8-AOVyUVgGN9oI2v_V3QCytorDbmorjExbDVXeFCKH1NIPyuj3fUkClG7Y7VazkLqvT8lkBzzvJOdn2CCdHsG_72xiGLwRZMSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3d6c6e5dc.mp4?token=URN0ZIFwwrZE7eHB_XLphcyV0LBEqXVq6vYOGliT6J6gvhn8Q0XphobPEPgIUqgq2WcpEi_1CPfHaEExD9P3xhNBCAtnmCHjpFFAvAGcVR2jMtDnFTv9e-3FddMhmUyYtMiP2JTqtS4wYgk5pe-8CDmxOx9BwImv94C1hcVrMr0EOyILcz55BSbUz20YyDFAgG7lf-lrkhVwPO2s9wytXIg3RcaX-OYtzFzhkeMUuFg7dwqvO44d8-AOVyUVgGN9oI2v_V3QCytorDbmorjExbDVXeFCKH1NIPyuj3fUkClG7Y7VazkLqvT8lkBzzvJOdn2CCdHsG_72xiGLwRZMSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
🇮🇷
علی خامنه‌ای،22مرداد1397:
به طور خلاصه در دو کلمه به ملت ایران
بگویم: جنگ نخواهد شد و مذاکره نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67733" target="_blank">📅 17:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67732">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5sFB8dKISG-zE59frq25DFF3bQmjNf-gVUsxVhbhdPSZPH5MzyX8VZNdpn2BoOqW32ENe2RWexazYZI7o2BoYqKDzsjoIYHkRWgM3UV4GuLml2FAzdfjwU1S6BTcTUD1vC2LVP59WxXDx8fnmX8g7Qfz4ddseEt4WKUIZmmMZPaAZpcW4iBi6yXNeRtAdNNJO5Ci8vXnnnaE_YVTJPgBwsBriBpYtVqY-xyOsTNa297uZqIp1JcwuwYwse2IH9mcN73-f20E0histaPuhr2VG7VoGUl4Gho1wTx4fgH8gXMC2a4u5bLS4nLo8vnC0W-IMVouoUHgEyRForSWdGePg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کارولین لیویت سخنگوی کاخ سفید :
جوون‌های نسل زِد که از وضعیت اقتصادی و زندگی در آمریکا گلایه دارن رو بفرستید ایران خیلی زود قدر آمریکا رو میدونن و زود برمیگردن
😔
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67732" target="_blank">📅 16:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67730">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMh-AkjjHa1zNHnAspD6BuTYIZ3ZXW8XSLjusHO-G5GP6G-kWKiaMWqxm0mltJH77iG2Gf-eJlrtkrS3gIsDZlxgHtH3O1xcHG4n2FdsAmTjskq1dOETwFJnLOT5b-E1I8XnDhsVJ9KeBlMf_59Rv-_1AFl5Ejnc0ma2uXF1D0TlSK6e70N2Dx3JMUUd5QtB71ooEcqd-mbdZy8pJ3caM_EDxOahyRSlumymukc7acdY7k-lH-FYBnyPFYo-XegXLIGgxk2qHoP_X8wWOXfcVIXl0dqezXJV9xjICoAHHe3ASQ6N6K18StnwMoDo_xCFxmudC7RMfbvE_ILUjlOMrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1372691bce.mp4?token=ce-kHf6z4b_J-SZl7BZ09Qp2TPeZXKg5xa4jqqzr3Lp__T3EcwtF30vxbLRHq-dhM-0LX2wCHCk1SJh37IQN0cvyQOIY2pYZUYBsvJb-hm0eiA3LBO24Ttp-WUUU0n_3dIrkLIq6NsxOS9pR27w7sjiQBRP0fW6ifaHlf-IEYYWgU0OnBUkW8_0GzHim36Dk1eu7cQGq00oqlxl5c0xJqbnR0lyxiA0gZpyWYdy4t4XnkX3doIyiJjMy-2ynxe3_TtaVOlHjxf6R9F4GAEBXg8OOvWRPuVbm2pVV_5h5krSipzBG7fS-6roofA2HuY8TMFp3Qww3NgmUeh3EUU2k1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1372691bce.mp4?token=ce-kHf6z4b_J-SZl7BZ09Qp2TPeZXKg5xa4jqqzr3Lp__T3EcwtF30vxbLRHq-dhM-0LX2wCHCk1SJh37IQN0cvyQOIY2pYZUYBsvJb-hm0eiA3LBO24Ttp-WUUU0n_3dIrkLIq6NsxOS9pR27w7sjiQBRP0fW6ifaHlf-IEYYWgU0OnBUkW8_0GzHim36Dk1eu7cQGq00oqlxl5c0xJqbnR0lyxiA0gZpyWYdy4t4XnkX3doIyiJjMy-2ynxe3_TtaVOlHjxf6R9F4GAEBXg8OOvWRPuVbm2pVV_5h5krSipzBG7fS-6roofA2HuY8TMFp3Qww3NgmUeh3EUU2k1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
گویا دیشب تندرو ها داشتن بر علیه تیم مذاکره‌کننده شعار«مذاکره با دشمن، خیانت است به میهن» میدادن که مهدی رسولی مداح حکومتی صداشون رو قطع میکنه و میگه بگید«حیدر،حیدر».
این حرکتش باعث واکنش تندرو ها توی فضای مجازی شده و گرفتن روش
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67730" target="_blank">📅 15:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67729">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbUEVYzjaAoo-rOGSyTH8Hz4_PGsl4DxKNNa7d3Dia6katzc0tkEpsANeeaDG8Xnf3Xm5fTe8HQji3ehjUicVv8ei9qGfBA9ddEb4Sz108rR0twgPsaCnJ2i_kvHrfclx8FFuOJ64_xjHnSbCfWJ5-3sHwjAy633W1n9g9dC7Tj92wThHwmPGSv89w9c_JmMck0RLjwXPQ5PsYMi5b-SMo_9Ehq60TsnyletYJ_O8S93jvzweii5a4GhL9vtKlO2l6CxDPOXUsCOGYM7sXy8gTfUcrofm5PnkoTm5ruFLnUWjXYwzEKivSbHfU5MbrQHamynMSnp6V_JAaQzmA9m0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فرماندهی مرکزی ایالات متحده(سنتکام):
❌
ادعا: رسانه‌های دولتی ایران ادعا می‌کنند که عبور از تنگه هرمز تنها از طریق مسیرهایی که توسط ایران تعیین شده‌اند، مجاز است.
✅
واقعیت: ایران کنترل تنگه هرمز را در دست ندارد. از اوایل ماه مه، نیروهای آمریکایی به تسهیل عبور موفقیت‌آمیز بیش از 800 کشتی تجاری و 380 میلیون بشکه نفت خام از طریق این مسیر حیاتی تجاری بین‌المللی کمک کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/67729" target="_blank">📅 14:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67728">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d2iWJ9EVDTht9y2nMOlVhIxN6vMz39sZk4-f_KHMDpsyHOeAgVyeeNowkB9AXLyeFhcsfraa2OLmiiiUz61iHPZ7yLeE8Po84GxcNF-xdCRHKgit4ZaN2Nusc51sTDqLmNSn4vG_pfNrkSDF-33KatjmFOrIpdlEUqN8fpLShoNlJW069nWEcDwyYD2P5-XZWeRfBVYSExPMy1U6sKPC7-kXJz3pbaIO_RipcczHCb2jz1pjeg5ASGeQoZ1cld7snCVndCe3dPY_8x4YVcib56bdCtZrJnvYfgj8lDcc7lurwm_Jjh6Nci1ZUmZZy_GSEltvvna7x-IE0UyxxJ8m6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با اعلام سازمان سنجش، رسما و شرعا امتحانات دانش آموزا، بدون هیچگونه تغییری و طبق برنامه، از ۲۱ تیر ماه آغاز میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67728" target="_blank">📅 14:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67727">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3590c95ce.mp4?token=sFWuQZLr1Pj4ROhNbK-mEHSKB44W6qjDDoeULA-NPMNKOLSw8-WpGP7AWXB9zbpyy10r7syVrvaZqZrScP4B0HImQzQiLE_fh72Cv0em5tTP8BZwa6amN8MWsVldwh3cHgPpnGHZMDX_tnlyyMq9SmF57_a7J092PWycHJ20u7mQjN9P4Q5hLU_Q1LhXPsv_FZ6yAclHiq2EWu9sWDAR-Y_viEYBfKQdOxhwsxNR_PyWQPL0bMSXsc9_7lq68wpTyF__DyQ7PZNugryd3ZaOpUQoqQNU9FV0ncpQ5RyOzCuKLidelUir2m8aFhptogJnu47kpVJsd7iSseZWeomomQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3590c95ce.mp4?token=sFWuQZLr1Pj4ROhNbK-mEHSKB44W6qjDDoeULA-NPMNKOLSw8-WpGP7AWXB9zbpyy10r7syVrvaZqZrScP4B0HImQzQiLE_fh72Cv0em5tTP8BZwa6amN8MWsVldwh3cHgPpnGHZMDX_tnlyyMq9SmF57_a7J092PWycHJ20u7mQjN9P4Q5hLU_Q1LhXPsv_FZ6yAclHiq2EWu9sWDAR-Y_viEYBfKQdOxhwsxNR_PyWQPL0bMSXsc9_7lq68wpTyF__DyQ7PZNugryd3ZaOpUQoqQNU9FV0ncpQ5RyOzCuKLidelUir2m8aFhptogJnu47kpVJsd7iSseZWeomomQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اکسِ تتلو تو زگیل ابدی با یکی دعواش شد؛
پسره هم وسط برنامه خیلی جدی بهش گفت "
برو بابا یه ملت روت شاشیدن
..."
+ ستاره همون دختریه که تتلو تو ترکیه روش شاشید!
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/67727" target="_blank">📅 13:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67726">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSelo0PxN4I7yiHITI11g7MRkk3q9b7SOJpiCVmCAnTgj7CQz90L_m9_MVxkfHEeS_5cwGfw5j7s5PhqGqivl_SlBYhdOolww2VVqn3QUavqUmsfI4qhDecO_-dj6bDO821nGVEt0sZpTnZr33huQOOQqZUog1NcaYOj-W3PUThDmJsWARv58Ze-227sHv4btwbfTJ5TobmNDaS0Pis7Z3l7givbgk6GSAn5D41-ydWWU396UCTm0h_oQN_V9w-Rq2oJ8rGjqWM0HO1pLNX_7eL2weY54M4yOVv4VTdpeUZKgRrdb_g5edn0JFhOS9JuHMhMCg-wfoWktOcuXmedQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
زیرنویس شبکه خبر:
آزمون‌های نهایی بدون تغییر و براساس برنامه ابلاغی از ۲۱ تیر آغاز می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/67726" target="_blank">📅 12:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67725">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/606bce162e.mp4?token=kcU2F6tNX0DzrUhJPk-7CP6RMB6BiRb72OE-hLttQkExiVyejygpos5dmZ3RAWpqXGzzu1R19TcqDY2vpVm7VxqhQBBed3mF7IlIGDE4fFRGY2BViC_hxlZRAJJhJbY_UlEWPFM4skqRgsMwcyc399LuQj44P57sIyvogmYSogMbWMwE47wVp_AUmaeq3lA1IfNLDU5VdYYBmR6eTQ8WRxYQqUStlj_QsxSPaBXYkm1DjlHrM1-VY0p73JcFWhsmaf4gT0t92YwKirLOcisuTC73gLA1tkYOMuS_2napWJmHeqhQShHZTkrleHHGMxPVNY_-tluqMlwk6iNC-JB1qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/606bce162e.mp4?token=kcU2F6tNX0DzrUhJPk-7CP6RMB6BiRb72OE-hLttQkExiVyejygpos5dmZ3RAWpqXGzzu1R19TcqDY2vpVm7VxqhQBBed3mF7IlIGDE4fFRGY2BViC_hxlZRAJJhJbY_UlEWPFM4skqRgsMwcyc399LuQj44P57sIyvogmYSogMbWMwE47wVp_AUmaeq3lA1IfNLDU5VdYYBmR6eTQ8WRxYQqUStlj_QsxSPaBXYkm1DjlHrM1-VY0p73JcFWhsmaf4gT0t92YwKirLOcisuTC73gLA1tkYOMuS_2napWJmHeqhQShHZTkrleHHGMxPVNY_-tluqMlwk6iNC-JB1qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آمادگی مجری‌ صداوسیما برای ترور ترامپ؛
نگوزی‌ داداش.
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/67725" target="_blank">📅 11:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67724">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
⁉️
تسنیم:
مراسم ترحیم امام مجاهد شهید از سوی رهبر معظم انقلاب اسلامی حضرت ‌آیت‌الله سید مجتبی خامنه‌ای جمعه ۱۹ تیر پس از نماز مغرب و عشاء در شبستان امام خمینی (ره) حرم حضرت معصومه (س) برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/67724" target="_blank">📅 10:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67723">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‼️
یه ویدیویی از دعوای دوتا خانواده تو شمال که به صورت گروهی با هم درگیر میشن و همدیگه رو تا سرحد مرگ میزنن وایرال شده؛
حالا فکر می‌کنید دعوا سر چی بود؟
گویا یه خانواده داشتن از خیابون رد می‌شدن و هم‌زمان یه نفر هم با سگش از همون مسیر رد می‌شده.
یکی از افراد اون خانواده که از سگ می‌ترسیده، به سگ طرف مقابل یه لگد می‌زنه، بعدش دعوا انقدر بالا می‌گیره که همه با هم می‌افتن تو رودخونه و اونجا هم به جون هم می‌افتن و به این صورت همو میگیرن زیر چک و لگد :
@News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/67723" target="_blank">📅 10:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67722">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
تماشا کنید: پهپادهای اوکراینی شب گذشته به ۱۴ شناور در دریای آزوف حمله کردند، که شامل ۱۲ تانکر، یک کشتی باری و یک یدک‌کش بود.
از جمله اهداف مورد حمله، تانکرهای روسی به نام‌های Chelsi-6، Aura، Sana-1، Ilya Repin، Venus-3 و Penelope، همچنین کشتی Mercury، تانکر Galasar Kamal که پرچم پاناما داشته و تحت تحریم قرار دارد، و یدک‌کش روسی به نام Alfeo به همراه بارج Aphrodite بودند. جزئیات مربوط به پنج شناور دیگر هنوز مشخص نشده است.
در طول ۹۶ ساعت گذشته، پهپادهای اوکراینی به ۳۵ شناوری که به "ناوگان سایه" روسیه مرتبط هستند، حمله کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/67722" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67721">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/67721" target="_blank">📅 01:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67720">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vOX3NkHZGx9Ks7pH6NImp3zBYWflD9XdPdw9OsA1m8RJRKWMSD5yiwTFRfua5YZ_EQwVe_RiWCCdF-B-TluzJX99mYqTsRS0PARLDUHInD7yXC_Uy0fd51k2CH6mQW-OlpIATTNT1eWCDFkl0ZgEXgyQc1tTAE59r8gx_s3HAL_aapHmvafhNSmA8nEkDDHjCHnBseBLq0mdRutfBc90UipskD0DWUUnnQ5VLjxyWb9WC3Xn6_XTdFZ6J4-U2vk9HVdI_arN8bR5-NScZm1eVeKW6ZLMjeRiDTYWKv8XWJ3GvmB-m22FpauyX7mDyJgLqFsse1zEw4vr30ACk4XrSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/news_hut/67720" target="_blank">📅 01:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67719">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPD2iC-_z5gGrIvfz9W9viTOeoiOslBB157teeqoRdCa3lx7bcfF13MHrxaUqd4gWHhmsLeI-CciwP9zOhq1x_D-aBL_2cGaCjXwiJ_gEJVqlQwc687PPwTc6L-j7XFCcomLWsrCgbhl79rqGSg1yM7NjhycriH8ZYy5yN_PQs7iTVnqS_hVPMPbxcafbvoPCFdSHZj13F---jUEFqc_s3Gy-Bh4c42pw3sGGEe58x7W1ic2Fbkz5pR9w1YqutNab8gCeGJU1QRxvbsX4_3FS7hAy8HEJXDWFZFYyBuQvxNBXSLjzhqbwGlc3OsZgppw1UTuz1_XEDXQVfm1Mp_ohQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وال‌استریت ژورنال:
اسرائیل اخیراً اطلاعاتی را با ایالات متحده به اشتراک گذاشته است که نشان می‌دهد ایران در حال بررسی طرحی جدید برای ترور رئیس‌جمهور دونالد ترامپ، بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/67719" target="_blank">📅 01:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67718">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
صابرین نیوز:
سخنگوی انتظامی استانداری خراسان رضوی اعلام کرد که درگیری مسلحانه‌ای در منطقه "بلوار سرافراز" در شهر مشهد رخ داده است که در نتیجه آن، دو نفر جان خود را از دست دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/67718" target="_blank">📅 00:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67717">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‼️
خبرگزاری فارس:
41تا43میلیون نفر در تشییع جنازه علی خامنه‌ای حضور داشتن
😆
@News_Hut</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/news_hut/67717" target="_blank">📅 00:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67716">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‼️
در حمله به ایست بازرسی در مشهد دو پاسدار کشته شدند. افراد مسلح لباس نظامی به تن داشتن و بعد از زدن نیروهای امنیتی با موفقیت فرار کردن.  @News_Hut</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/news_hut/67716" target="_blank">📅 00:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67714">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ElD8xdP7hoOXQdKAtApSIedKlWPsfBmPwHjoxrbqoJd27KcYPY2gbfrx6tRPDiZ-miVd0xBjh7XXgbWgtK7BxEdTbHwfP_D3fHMDB6KF6Wd-ZHC0lav9zQv8gO72vpH7n5qN0u-P9QxpT4LAVnA6vcg7BBlex_JV35hGQ5TJwV0JJczzJVX5ea6tEobyz1PPdg8bSL4l-7LULWg8w7ZZi9vhmSnyOfUanTbo4L5wV-xLvGsvxgyh1nUchjT3s4qdlzFxnk5PULBrQtcgA2JWtiw7T8DiPpsXiZ8iCHCAAh2hlKrgXHoCRqks0lS5qWWRsYtkXLDA8lCDOcK45EqNiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fF-aaqjN-wvpOacQ98fFEQYr3IZXmSkOawtAUYWF--pUS6m7Mf7JPwvst8ltn5f3weYkdMvsQbK9QeiL0lNYcbRk34FbOhKlsn2on7ZtzNBwuFk0m5AuoVkgcHNyUtt6ww0FGGPwwolPshFaEiIoddTQVaXFXFS8CXh05FoT9xr68COfwY0JkCTKPLD3JIlVmYcFYmVE7uCIdvoCz65VPDgCBTZXSU3NjzeSQ6vgF1xMH3IgtWX03EnWrSVizlUhgaJpjQtPoVUxvvPMirc0WrCVX5Y47abwUVMIvepd4D608VeWjMgEp9hpXTWr0E3KsoW68k3yByDQyXRArCV4wQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚠️
اولین تصاویر از حمله مسلحانه به ایست بازرسی اطراف حرم در حین مراسم علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/news_hut/67714" target="_blank">📅 00:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67713">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bfu2s2LbpFbPNQkBsb3qdeNtQwjEsFrQzlASgJr7NJ5HaIog5IR5s5NfarioyXgs2f03K7r3eHOXLBTiMkugzuLbuYCxY1f3PHnkCas51bQ6p9ZxFrB_ZySw4m0jDQKvA5V90GnPu6He9TKRpkIroG9EjyroRHnWfeLetvjCsmut9P-o8m07ZaTHXim7SR1j1tcCfsCQbOJnpWcRFbwcBY3slZjse1SWFCKL8Lh96h1b4fHMJzNsge5er_XCvkQxA5kge1uYu-igMExF2FowBKSweuv_7m0-pmDur3sqyfBAlU-_7xCOVuT8nUsrLDzX5qye_UVfD709VkMcCwm2og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حمله به ایست بازرسی در مشهد دو پاسدار کشته شدند.
افراد مسلح لباس نظامی به تن داشتن و بعد از زدن نیروهای امنیتی با موفقیت فرار کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/news_hut/67713" target="_blank">📅 00:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67712">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dfY_fTJHYw7sTZ36x7eCl9-_rCxafaF0ba8p8kKKWF5c5hkHnc2RvPV5r4XZINYWtOS4CiAK7flB-5mMbY5vZl9ZqXwWFbojXO8PYfHOI3v5LPOJLk_BthzUF1aKZn960mNsQ7el0W4twr0K1SX_K1BrHNQR5fWpH6qb2dX5a5mY4YLDFHmj_zleFBZ8Xh3jWsL-ewhcimfzBZj6tndDjLvqF-1D8xLByS2Ol7RQ4u4s7en9aPWICZVRpqMohOM1Wz-iVL05tj9l5VQg5jbi0aK2fsOZ3WiOp2zpa1dn43mtOmdSF5tGss8pvpELlti0z7yKD3bQ8aBqFyqkP5nV8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
محل تیراندازی در محدوده استقرار یک ایستگاه بسیج، واقع در ضلع جنوبی و خارج از محوطه اصلی حرم است.  @News_Hut</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/news_hut/67712" target="_blank">📅 00:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67711">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
محل تیراندازی در محدوده استقرار یک ایستگاه بسیج، واقع در ضلع جنوبی و خارج از محوطه اصلی حرم است.
@News_Hut</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/news_hut/67711" target="_blank">📅 00:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67710">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
❌
گزارش های تایید نشده از شنیده شدن صدای تیراندازی اطراف حرم امام رضا
@News_Hut</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/news_hut/67710" target="_blank">📅 00:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67709">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ce06a68b0.mp4?token=VUSicFZ_OOeflcZ4Z3lAkcXkdHkIqK_vVxCByPFm9eSWjkkZjILikkPR0EoD0CAleuIxZ78BfaukMvpNFMk3ey8gl8RvSIbqSH288BT4rYHrisVu8YQFeca_exbh3mCLAejYhWsNnzfT9C14-B7DcUOaCp3kewXqH7uxvVr1kJQTCBWaZ27u4-GX0Dy2C2VHD7OxuDZ0CJOeXrH47IPXxJkMkRoTZoKp5yDpO0qUL8o6zjNzanX-rzqGJSoYJVSvrxr2kD4hTjxCYm2M-S7ivUN9lDkRZOfOOFndbWmZGtN3QM6TMcnQHVGBl8X_2VT_C546yC9Vx68rXLIXLYeafg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ce06a68b0.mp4?token=VUSicFZ_OOeflcZ4Z3lAkcXkdHkIqK_vVxCByPFm9eSWjkkZjILikkPR0EoD0CAleuIxZ78BfaukMvpNFMk3ey8gl8RvSIbqSH288BT4rYHrisVu8YQFeca_exbh3mCLAejYhWsNnzfT9C14-B7DcUOaCp3kewXqH7uxvVr1kJQTCBWaZ27u4-GX0Dy2C2VHD7OxuDZ0CJOeXrH47IPXxJkMkRoTZoKp5yDpO0qUL8o6zjNzanX-rzqGJSoYJVSvrxr2kD4hTjxCYm2M-S7ivUN9lDkRZOfOOFndbWmZGtN3QM6TMcnQHVGBl8X_2VT_C546yC9Vx68rXLIXLYeafg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امشب تو مراسم تشییع تو مشهد؛
یه مرده داشت شعار میداد (به احتمال زیاد علیه توافق و سازشگرها) که یکی اومد بالاسرش و رسما دهنش رو بست!
@News_Hut</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/news_hut/67709" target="_blank">📅 23:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67707">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
خبرگزاری ایرنا:
یه پایگاه نظامی تو حومه شهر بوشهر مورد حمله قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/news_hut/67707" target="_blank">📅 23:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67706">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldS5_magGD1ExlPCNG1JnU5cCLSHeFbsFHr4oHypyUx2UsUT5OE1MfWu_GORyUrWMiptTk0FN3x3omfkFZnnSfG1U4q9X0XIvT-LAnal1wkPjh5UeWw_Lb3NduSGjmPmneZsq0yBo25LP3hhkg9gxb1m7K-PSd9m-21MQTipyw8-kangiLKKChw0-gVeVVfiy3MSVn39fCAUqpfR7xVN0O0Qzn7c38BbB3fqRDQtAgl7-NPuwNCs1bmdprdfisPsmKvgE3E0nUqFo2WUa9DD3U3LRzgpPx-PFewIpqQekDYpRANDJr_T4afO8FYmdDOrRPlbBkPrAWo0IMoA-_PPZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون درخواست زیاد بود دایرکت رو خالی کردم تو ربات ۳ تا پک شد، کلیک کنید
💦
😁
🔞
🔗
دانلود پک اول
🔞
🔗
دانلود پک دوم
🔞
🔗
دانلود پک سوم  @News_Hut</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/news_hut/67706" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67705">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">خب دیگه بسه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/67705" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67704">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3ltBnbQCzMSUfBV44fVAVoxuBhYr-FY5sczUVWXxzAeGHlBcYrfmc9Wxxs8GwcRZzd5D3ZRun89wgraDWecsmN-wMqAmD1VX8x4O5-ERZgmJbI1HQlZSWTSkqpr_t_Z8TFVsOQYQKnVu88w4xfAf90cjNP1gJxZHRO6T273sT06ipVIlntlhVn1gbPxgRVGaEgmY-CYPJ03_6gBsZM6ly__WSrmnSaNUBOMbBw2T_M_pccBLt2bGY2cta8eaNclmgU9LEAtywGxTvYDYx1lWOvRfqymaPzy2aSqZxMWVGq8Bu9tTGZAdSYRxnoVNURcmiEZ90B5iTcuhJKDLaC-ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به به بریم برا دعوا #hjAly‌</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/67704" target="_blank">📅 22:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67703">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aws-D5gtb_SRdRYwwbSBOfURyAQikxj7MHpquQorxnmC_OqOmeZc3u_nLMk1jYoeNajN_mdS5L4ENyq_WnZVIFQqFUX6E-sKXToOV4lb9ohiP7rIhgicva2ygDXuMCVCwcCVfiEtvRGHMeFHDeeE__mJcVxOxdzH3M5Y37PwHiqNf-VECfsSZ7sJe-vdOsdHDygIJ29WSFjPt1n4JHVEtSr8wDQRpI4xrcFE9AcqgZO0kThJzjKCJrUqkMQsJWZtl9fDvTuHKc1tqOzyFygE7OnSSL4uBlTLrzU83FcNraewZUT9lQj0Orw9QOFEwpBPdK52EeRPH8Dba4jO_-6xXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه عده هم هستن تو دایرکت فقط دنبال عقب افتاد امتحانا و کنکورن، بشینید درستونو بخونید دیگه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/67703" target="_blank">📅 22:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67702">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">یه عده هم هستن تو دایرکت فقط دنبال عقب افتاد امتحانا و کنکورن، بشینید درستونو بخونید دیگه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/67702" target="_blank">📅 22:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67701">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
نایا: ممکنه حملات امشب کار کویت و بحرین باشه  @News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/67701" target="_blank">📅 22:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67700">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ارتش آمریکا اعلام کرد که حملات امشب به ایران از سوی سنتکام نیست  @News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/67700" target="_blank">📅 22:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67699">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ارتش آمریکا اعلام کرد که حملات امشب به ایران از سوی سنتکام نیست
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/67699" target="_blank">📅 22:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67698">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FeXEVjG95Wd_uA-p8ELlMYhdPaB2F2bTqsGjIHLkOsavpfm4PofNSxZBCgezwXYe3N4hjS1uNBem-zeGzEyZFKMOHAfMUhpD5WQHo9jksKOBbvcQQROWH9bY5gLCEcORU48zR9uD6U_Akf3CnbC5vOv3lSaFfG5lMxoL2skul3npAlp7lPa5BDyDRQo4hOqBBv14q04X5CKAC8Sm7cyrqR7kUo8fViALdWYgVFtlQ-0DiV8DOAeAVH0GDhTsSIYJJx1VR5dFqEDnoJBaBNHKCpnr6FnOIPhTmcYULb2GscS5XJXIAyPTzPqd6qAPRh3RR7bfCv3noYKcJHGwKQp28A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آماده‌سازی قبر علی خامنه‌ای در مشهد
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/67698" target="_blank">📅 22:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67697">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8449992fa.mp4?token=En1wQ_PezJ3KM6rMRRjwSQKtHrVfu1xT-3vaeLK_5QvbCrl6FSjEC-nDIoFNg_QSmaj5aNqmDid8rUssWrw_s3b6Ve-nS4Fp0neUCcliNb14NbR4opGwmMEV0p-bWCFeZb3KxZWKqtwa1tnlhK4BlXGWI1Y_5SlUPUmBdLPLYtZLxdy1Hpv2ua9KjTlMz-fq2AoFaCTnTN1SaSQ0QZUSNRsQIMmNbCcQZaO9ImopjRw2qgm5mpWLPDwKQwvx5B-PXs5oTanEWW4zzlxAmxeTWv-da7O3LAl51kGI7F2E3-R0X-C5oBjkHva8qsS6SHlR70R-k_LGmhkt8py5atuiRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8449992fa.mp4?token=En1wQ_PezJ3KM6rMRRjwSQKtHrVfu1xT-3vaeLK_5QvbCrl6FSjEC-nDIoFNg_QSmaj5aNqmDid8rUssWrw_s3b6Ve-nS4Fp0neUCcliNb14NbR4opGwmMEV0p-bWCFeZb3KxZWKqtwa1tnlhK4BlXGWI1Y_5SlUPUmBdLPLYtZLxdy1Hpv2ua9KjTlMz-fq2AoFaCTnTN1SaSQ0QZUSNRsQIMmNbCcQZaO9ImopjRw2qgm5mpWLPDwKQwvx5B-PXs5oTanEWW4zzlxAmxeTWv-da7O3LAl51kGI7F2E3-R0X-C5oBjkHva8qsS6SHlR70R-k_LGmhkt8py5atuiRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‏
حمله سنگین آمریکا به چابهار/ صابرین نیوز
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67697" target="_blank">📅 22:05 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

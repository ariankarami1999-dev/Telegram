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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 00:09:02</div>
<hr>

<div class="tg-post" id="msg-67813">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTwwQCV3_97xVktyLNW26IMNq9JqI-FofyvrCtrmglRhuGnFav_8C_qUynClfyT0NEct5OsazdmEESCWapcNBzRa7bnVyFo3LKp1X7vr_8GvxOovt_nMwN_Vfl26m0E9wykGbRQ04DWOCYRfmNS3VspuoxJgNNyHO3vo__CcceqLgAHB1abXJNTlAqtc__t7y7kKnn-zDMh-PYW00SASW7-Q8G4gDmxMZ-XAVuvmQZVSxLb4GpR0NdL4hWaPL9-Xc_ObJiBHiB-O9Jt-sTfXRBF7b5acr_k8VFMdu2gfB_pOt9GKJpaxyLqG9OLxmbEIJ0Id95oDFiCn4fsd9zKseQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کانال 14 اسرائیل:
اعلامیهٔ مهلت ۲۴ ساعته دولت ترامپ، که روز جمعه، ۱۰ جولای، صادر شد و از ایران خواسته بود تا حملات در تنگه هرمز را متوقف کند و از آزادی تردد کشتی‌ها در این منطقه اطمینان حاصل کند، در ۳ ساعت آینده به پایان می‌رسد.
این توییت دو ساعت قبل زده شده و تقریبا یک ساعت دیگه مهلت یک روزه ترامپ تموم میشه
@News_Hut</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/news_hut/67813" target="_blank">📅 00:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67812">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
🇺🇸
مهلت اعلام‌ شده ترامپ تا پایان روز شنبه به‌وقت شرق آمریکا ادامه داره که میشه حدود ساعت ۷:۳۰ صبح روز یکشنبه به وقت تهران…
تا اون موقع به ایران فرصت داده ترامپ که اعلام بکنه که تنگه هرمز بازه…
@News_Hut</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/news_hut/67812" target="_blank">📅 23:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67811">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSaeq9_lx3B74WbosOjnaZROFUFG3Wd8VwaIK8oY0sgELkMs6mVFQ2D8MVokOal1tv2sv9UaCcrQgHLsVGju3dOR3NfMsL-IO7703kbrih1IrdhBg5Zsf2l4jUeNkARFao8ARMOSSxCeCFl8HPxZ7nCVeMWMHR7nP-p_qMO7oJiWm15txI4DWB4hTmqLwnoaB1cwj9heRHl9JEjxiJHWLOOMo7XBC5SdGdVmIgU7E9bf3KsV8KcmJyi40aMHcm-Dmhj4C8Pemj1DseIBjfaZSm_gPB5fohqMK7XcmILKrJ1ZeMiEs4_r6HGgEeZx8REZL3TffJM5zx-s-lsvKW4I4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پویان مختاری گرداننده‌ی سایت های قمار که خودشو مخالف شاهزاده رضا پهلوی جلوه داده بود و معتقد بود عاشق جمهوری اسلامیه؛
امروز صبح ساعت ۶ با هواپیما به فرودگاه امام تهران اومد؛ که توسط وزارت اطلاعات بازداشت و راهی گونی و منتقل به طویله شد
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/news_hut/67811" target="_blank">📅 23:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67810">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6SQAYQEacjJIYewbt08DmeYsnXCPconFZFu4DaSj2WxAcuwlKJnwGaHhcRF3p-uhZmR6YNn1CSuL5IzMBNH2pnCAWBqhKhKel9jbLwW4D8Vk5zVsRuYQRQIWZWI4AnhIOfyIJQvKE4Lv3n_rWE9CWfew-Gj_36I2X6UV2SD3vE9eRPDJciU5GDhduyDBCGdkva2l4e7SebSAPr3LKCXBVC4DhRlxxUqPIjz586yyZ9YuFzSP7xQQRKeEESIbgIoK5UzM1S8tn_MqwwMQK2w9J8Qleataxjx3RH17nXSz86_l0yF7iSYKuyJFptSwFwCeXObtVySDBupuOV0RK4pMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علی قلهکی:
قرار بود سفرِ عراقچی به عمان منجر به صدور بیانیه مشترک درباره مسیرِ شمال و جنوبِ تنگه هرمز گردد و در ادامه نیز «قالیباف» و «ونس» به مذاکره اضافه شوند که با بازگشت عراقچی، گمانه‌زنی‌ها درباره به بُن‌بست رسیدن دیپلماسی در مورد «بند ۵ تفاهم‌نامه»، بیش از همیشه تقویت شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/67810" target="_blank">📅 23:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67809">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
اکسیوس:
ایران نتوانست در این جلسه، موافقت عمان با این پیشنهاد را جلب کند و مجبور شد این پیشنهاد را برای بحث و بررسی داخلی در تهران مطرح کند.
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/67809" target="_blank">📅 22:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67808">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHZbzYSGDz8f-9G5srP9cFpHBl0kBs9jVnTeE_Va4wJjyE9FqWS3UVPYiUMUA_VcpRuG8fvPHjbSfXA9xEELec193cseb37jxJyn9fyIAG0LoKPbjzQbtyyna-wv3Q0vTlnILu4-fh1FJZBlQ4MBYZm4K9HWcDGZHVWPCUl9XPzm3LFNqxVjxa1DrgHNJnx1i6KUXerEUcX2sidmTfavHPfewvGf31blWVS3icn5a6S6k_r_aC9WZcAQKfXzPbhLMdXI0AClY8HAvuoLRGSi4USIqRj34RuiEchm7Ksb6hPvoJnB9XR9f_B1oh671onzjjbGsjQwvi-haJVyeKQfUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سی‌ان‌ان:عمان پیش نویسی را برای مدیریت کشتیرانی از طریق تنگه هرمز با استفاده از دو کریدور جداگانه کنترل شده تهیه کرده است.
بر اساس این پیشنهاد که هنوز نهایی نشده است، کریدور جنوبی از طریق آب‌های سرزمینی عمان برای کشتیرانی آزاد در شرایط پیش از جنگ باز می‌ماند.
کشتی‌هایی که از کریدور شمالی از طریق آب‌های سرزمینی ایران استفاده می‌کنند، به تایید قبلی تهران نیاز دارند، اگرچه ایران هزینه‌های ترانزیت را تحت ترتیب پیشنهادی اعمال نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/67808" target="_blank">📅 22:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67807">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/67807" target="_blank">📅 22:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67806">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
کانال 15 اسرائیلی:
ایالات متحده منتظر پاسخ ایران به درخواست‌هایش مبنی بر توقف حملات به کشتی‌ها در تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/67806" target="_blank">📅 21:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67804">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/67804" target="_blank">📅 20:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67803">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/67803" target="_blank">📅 20:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67801">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iz47oX4HCwlfkPryYs7n9U5n7J2U5tT5z8Grm_ewaNuF5hMtmAl00JuZl2fxrciAXrnrAxMr_pKAU0psEUwj52obDXIJBFyAZAaloBY0M291PiwLDEHBlD1ym_k7WYaaGttDQwNN9Q11WJSHnGDGnpP3_fchB4LB_Ub0L08AsxZNnyj3MSamSX6FwacP4dNoxxFN58iNLpbaajet-R1cx_GZH-Tthue5ea8V4wzhTqzV_1pxUSXv_LIXrOqN1laRQ3qSxbuAAaNQJ_qXh4ryaSoT2V3xXPvf3iqQJtF6F_lwmk8NIp7QRbg-PcE6_TPCNjeRTGLYMjNdKceDUXu46w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rQg1odY-yEUCL-LYsgG9F8cquKXFPWK6_PuzMb0zDFsYCpz_xXeg-f6eeJImnXpWffpzKX7H3SQDVAVa3L3I07iT-H79akB-Zf017DsfAQAINwCgv85gXWCQU1bsY3apepDv0LMxY10CS5Xz2J4BEm3A46n33dV_eaEnD6VxsRUXg_LlODD4LpCwGaK6ZDSia0EoM-KtNamBQySeXaTRln6-Cs-Q1k9DkEB9bMvf-LJGt957yefaoBuFebaclFPbq8XiZRGrxDMVd9uEoewT_XdN7mc7JZiAhwiJpvVPHOqSu3FL2yhhss8-plMctu1XLIKt3MEn1UfwkAwsOzjcSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
بسیاری از هواپیماهای تانکر سوخت‌رسان آمریکایی از پایگاه هوایی الامیر سلطان در عربستان سعودی خارج می‌شوند. این هواپیماها معمولاً پایگاه‌های خود را در منطقه ترک می‌کنند، زیرا نگران هدف قرار گرفتن توسط دشمن هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/67801" target="_blank">📅 19:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67798">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67798" target="_blank">📅 19:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67795">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgD_8dv7aLb8S6xzrgq-OFTHueI9s9WVu6uwbWtMcguMQ5wFo7oizJSTq_-lnI_lF7vPGqsZXPlrZBorcGWvNCljQ-IUYFGhFChwsvDRSYXZ14wp-mheXV34YZlpwvGx7xBgrMSCv3rXci-J0h3DLW6we4uEf-kLRLrhbdkIgnaeeXb10dMfK_ra2BfbrNjcB0Wpg03NQZ0bfLaGdFiwYMTkTueyJcv0SjEeaY4bhXdROAhuHoFbvKCuTSPVDZPLvwUfTLV0e0NjiDYXuMJEf8ADzHx_mkEpfGojgPnWQIqI-HzwLmr8ssHRJimgbMRhIDocBFVa9B1sC5fG0xAVlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید:
به گفته یک دیپلمات مطلع، مقامات قطری در حال مشارکت در مذاکرات میان ایران و عمان در مسقط پیرامون تنگه هرمز
هستند.
یک منبع منطقه‌ای اعلام کرد که طرفین در حال گفتگو درباره بیانیه‌ای احتمالی برای بازگشایی کامل «مسیر میانی» در تنگه هرمز (که در آب‌های بین‌المللی واقع شده است) جهت تردد کامل و آزادانه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67795" target="_blank">📅 18:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67794">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a00f69c138.mp4?token=tNB1Z6PA3IGDPlnwXTqUYDEY8Bo4LGhl1zjy8VW6p-R9vVfHVHcRdmeS2Ui_W6pXi2Dqq6tNXYu02eamclWWxGXmoWSuzEzBgpoBqBfKiYzqAwKDMUxYZIDElV1pYc1rj-ZmRNZpIhQNUNXrSbFl5ct73gkLdghOmFQJVMUCUJXLgf-j6Nif8c8Lj8UuB-TXz4NtJw0eShIs7fegLDg34kqpNM1U799modQRbXB8l7PtI1bCoFeDBOF-x_Sbo1cCnRSUPRfRGJYLo1WqRcyJB9nRF3wIVpa2gIn5XZViL__qXSPteDYvI3qSSr-UEDOexe7IRpC2o02huoxeD-5U1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a00f69c138.mp4?token=tNB1Z6PA3IGDPlnwXTqUYDEY8Bo4LGhl1zjy8VW6p-R9vVfHVHcRdmeS2Ui_W6pXi2Dqq6tNXYu02eamclWWxGXmoWSuzEzBgpoBqBfKiYzqAwKDMUxYZIDElV1pYc1rj-ZmRNZpIhQNUNXrSbFl5ct73gkLdghOmFQJVMUCUJXLgf-j6Nif8c8Lj8UuB-TXz4NtJw0eShIs7fegLDg34kqpNM1U799modQRbXB8l7PtI1bCoFeDBOF-x_Sbo1cCnRSUPRfRGJYLo1WqRcyJB9nRF3wIVpa2gIn5XZViL__qXSPteDYvI3qSSr-UEDOexe7IRpC2o02huoxeD-5U1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریاست‌جمهوری core:
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67794" target="_blank">📅 18:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67793">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KySb-tBVe_lgLfk3Q-0xfTvWBdP8P8leVnsU7w-u3CbqrZlIKzDuiCQjF-8F-OGYGTcQ1MtNy62BmfDwVybsDEQ3AXtKtvMGGOESvl3oVhLC65lD-2YHO2HOIMd8A9i5XbapJgTGi9NfZZYK8rWS9mp1zcHeg4QmLQ6glHuonlmLn599BFSdi0aJ1CAemUv1kaTVv1YJhOPmA9tDQ2TCTkSLJ4hlNsuc6lxE0ttnAOpvzTsr_9gVJYq79FX3hAlkHTGSdwIUAjKsAcg-hYmoTN8PCb5PeEAhuOiiIgkfTMS5P91VdsTJV9SOaIJKT9HOyjGVBhp-NrKLbzScItrePA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری مهر:
یکی از نهادهای امنیتی برای حضور فیروز کریمی در  یکی از شبکه‌های ماهواره‌ای گردش کار قضایی برای برخورد با وی را تهیه کرده و در دست اقدام قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67793" target="_blank">📅 17:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67792">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJUvuQzhnslbkp4rMznMiIBNOvAETStYvkvPUQM9veLN0euFmhog0K6I17oR4lV56eC5giZvY-8cU8-uNthIZby3JIkiT0HRiRCFm7wL5z0g1Pb0Qsv9SpTWmptCSz7-m7Y0U0s9k_4Bgw3Xat9ce0wzclHdPRW2fV5FBfroRzjQHbnTO83cxboe5liifN2xsLG2iugynAhdhexaXzYNoxorDspeu5DOikZKjjGc_Jvi2hYTaKZbQIlZvxZcq4NeSSBaErUkR6f_K82eWRp8TGd9h5xFuNgYJSfq9hD2pIdh2ZaJ3iquCEIGtL6g9IXk75gJj3WEXSyUOAN5nRztmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستهای این توله‌سگ خمینی رو ببینید؛ مشخصه تا حالا حتی یک ساعت هم به سیاه و سفید دست نزده. یک عمر از خون و جیب مردم ایران مکیده و حالا هم نشسته میگه «جنگ جنگ تا پیروزی»!
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67792" target="_blank">📅 17:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67791">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67791" target="_blank">📅 17:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67790">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‼️
ویدیو وایرال شده از بساط عرق خوری لات های کرج
😳
امیرعلی امیرعلی امیرعلی....
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67790" target="_blank">📅 16:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67788">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67788" target="_blank">📅 15:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67787">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67787" target="_blank">📅 14:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67786">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🇮🇷
مجتبی خامنه‌ای:   آنها باید بدانند که این امر، متوقّف بر وجود شخص من یا سایر مسئولان نیست. ما باشیم یا نباشیم، این مطلب محقّق خواهد شد و بزودی آحادی از آزادگان در سراسر دنیا هر یک بخشی از این مأموریت الهی را انجام خواهند داد.   @News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67786" target="_blank">📅 14:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67785">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🇮🇷
بخشی از پیام مجتبی خامنه‌ای:   عهد می‌بندیم که انتقام خون پاک رهبر شهید و همه‌‌ی شهیدان این دو جنگ را از قاتلین جنایتکار و بی‌آبرو بگیریم.این جنایتکاران آرزوی مرگ آرام و در بستر را به گور خواهند برد  @News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67785" target="_blank">📅 14:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67784">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🇮🇷
مجتبی خامنه‌ای:
انتقام خواست ملّت ما است و به‌طور حتمی باید صورت بگیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67784" target="_blank">📅 14:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67783">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🇮🇷
بخشی از پیام مجتبی خامنه‌ای:
عهد می‌بندیم که انتقام خون پاک رهبر شهید و همه‌‌ی شهیدان این دو جنگ را از قاتلین جنایتکار و بی‌آبرو بگیریم.این جنایتکاران آرزوی مرگ آرام و در بستر را به گور خواهند برد
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67783" target="_blank">📅 14:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67782">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
پولیتیکو:
آمریکا انتظار داره جمهوری اسلامی در بیانیه‌ای که قراره امروز منتشر بشه، «به‌طور صریح یا ضمنی» قبول کنه که در حملات اخیر به کشتی‌رانی در تنگه هرمز مرتکب اشتباه شده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67782" target="_blank">📅 14:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67781">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rLEHfARz3jb64BoYFXOnUcV084qIXHXGWcKg4tPO48XhNmQk5JYl0KJH_0CyRuVQgI3UrbAtSYVtDJp_DR0HE-0xrVooRXaq2PIJkuD0HlYZJLiijWJ0yebAMSScNNDkXA1tK3RCx2-an17aAo7lrRsqieKcSoP-RHWxQpHvEe74obxekTRKp0tdU-lI5C56yRqlV_HVHF8rywgNbaDlTwDTB4GWJTvZkEyrF-2-Yix7dsx0RSURikTEB05brzwTj-ZgQ-IdxuT58U8uIQpTKDrzKplpCv80oqLJdYIo2mTAQL9j7hCOfYkDjM7NEUk73d9bEHnKzeuu2FuRWvfRAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67781" target="_blank">📅 13:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67780">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآپارات اسپرت | AparatSport</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrWbvPorhPH3EyleCMj2W9MjrP0SrGPbXz9zilXr9xTH_KmCLqggDhrrXSjOn2Trn2gCW091Fkqzav-vSouFAPm8cp7FOjiUrDaqnjBr_5Px-DrX9iZ2TJsVE8_HcOj_DfynDRGW_RCSZjkcUdgiZ2BJbbrYnndTAgWBGsx3Cx5Q_j6ovymgVSSWqDU3vDw5JbxaxLI-VFMHJJzFRDnLEGhdkA2UDGUUs28kCdkqgAjnsOm8ZTfnJ4w5Ba02sPbfAQOvYL8P081aIEqLPnNkfebDPJLUG6E1-tDacMeQEd3C0N4p-2RmSSQlHMwZ1c5SdCWNJ3mWUwwBynQopQZwNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پخش زنده و اختصاصی بازی نروژ و انگلیس با گزارش محمدرضا احمدی در آپارات اسپرت
📅
یکشنبه
👈
ساعت ۰۰:۳۰
🔗
لینک تماشای مسابقه
(بدون فیلترشکن وارد شو)
@aparatsport</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/67780" target="_blank">📅 13:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67779">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VsbQGhxTRA9RVEXvDAqNaN0dtCnUfH07w_P6eKDCol2pGfylVF1afH8ifEImV27vhLojNoBbYS0M9hz_l5WcZ3kLlQrHqcxHqxOfgmJBjpHEJg01D1527lNBBLe8TUOj9Eq-4KC8XAMDasjf2wdpSEdR7H6sxijUP9vFhd7Or_2Gm1j9b4HpCUbVUNlt5sO4Gh8uohVUlNqctNzNS8eD89Goff9HQ4RFxZPImp9pdo4L74EqNOHlLevjuye1iRhnBD1ClsCon6d8Ma6iWuhg7rgL5JdE4NEUjeDT1n44nUd4stIanGD4ImJb67btmvs9RU83PsIrQ47JnB5GG7Fo-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ تصمیم نهایی برای عدم تعویق امتحانات گرفته شد و شبکه خبر ساعت ۱۲:۵۰ امروز زیر نویس کرد: با اعلام وزارت آموزش و پرورش، امتحانات نهایی از فردا و بر اساس برنامه اعلام شده، آغاز میشه.  @News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67779" target="_blank">📅 13:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67778">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2gMhdm4QJlQte11G4BKVfP-iwldSbFoZvUccA2PP9h-tmaH6TyylAKaBrhA9oy_nQmakrEX8RECMamcmnNTipv4GVTSv8O1HyWUk_MIvU6s60BYihPVbyIkJ5Us5qDn7520HYyKzMNmxkOQue2zIyR8VvpUCAY6lsEALqqpgbCI8mdqbvd5fKZeiH7UY23d_o4QpEouuxG97t9c80gsRosNZZLBlQkfOzm7U697j7XLaR1gQyd5P4oasehFSNqWDaZwzTfkt87lzlwtLf1N3odU1OH8QGZmUBwj1orbYF2-az39nLsjsL8YjN7sy9uaVX3iBErZzGPb1zVbVUAw1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ تصمیم نهایی برای عدم تعویق امتحانات گرفته شد و شبکه خبر ساعت ۱۲:۵۰ امروز زیر نویس کرد: با اعلام وزارت آموزش و پرورش، امتحانات نهایی از فردا و بر اساس برنامه اعلام شده، آغاز میشه.  @News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67778" target="_blank">📅 13:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67777">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67777" target="_blank">📅 13:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67776">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:   1000 موشک در حالت هدف‌گیری شده به سمت ایران قرار دارند و در صورتی که دولت ایران به تهدید خود مبنی بر ترور رئیس‌جمهور مستقر آمریکا که در این مورد، خودِ من هستم عمل کند، شلیک خواهند شد دستورات از قبل صادر شده است و ارتش آمریکا آماده، مایل…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67776" target="_blank">📅 13:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67775">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
ان‌بی‌سی نیوز به نقل از مقام آمریکایی:
اگر ایران امروز در بیانیه اعلام نکند که تنگه هرمز مانند قبل از جنگ باز است آن روز برایشان روز شادی نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67775" target="_blank">📅 13:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67774">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
مجتبی خامنه‌ای  قرار است تا ساعاتی دیگر پیامی به مناسبت تشییع جنازه پدرش علی خامنه‌ای، منتشر کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67774" target="_blank">📅 13:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67771">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67771" target="_blank">📅 12:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67770">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c27W8buSf3seeBpUse_p2bVBTEO-51WPQ1B9R8-dRqMnV7DuV80AlWk01RN4h7L2QNGqa0QEN-Q9QIZL1rwIE5VXNSYGtOa6kkpxY05Malx3S0GAq0OwakLbOmh8zyG3i7H6yEQ8uCsQH-rGGc28-PlE5ozTtW0mExiZYMaMThP0Z0bmMXutNdWzVkyyLMQ6r0AboncZwzEXJ97BhJp_pWcYkSjXKsXzmoAl2fRyQ2zGimYBgJC5YlQmG0hnvnJFoh6_59CROZd58Saqc8ZcQskwz_Il4leXE8vS2gXYU49YwZD4pPITNdvi0HoOrRWrEu8HlE0yJvpzz1wBldOG6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
1000 موشک در حالت هدف‌گیری شده به سمت ایران قرار دارند و در صورتی که دولت ایران به تهدید خود مبنی بر ترور رئیس‌جمهور مستقر آمریکا که در این مورد، خودِ من هستم عمل کند، شلیک خواهند شد
دستورات از قبل صادر شده است و ارتش آمریکا آماده، مایل و قادر است، برای یک دوره یک‌ساله که قابل تمدید است، همه مناطق ایران را به طور کامل نابود و منهدم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67770" target="_blank">📅 11:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67769">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uy3NxXsQd9ihafxLKVdvp7aEpvoiXM15Dse4ftMmOTPZWiKiceNnMFNScX5xFQyPuW9YfMFzoR5aOtN-aEOa6YqGXPxm65MA1jkGK1-TxIWp_xxz_tFoEx9Cb5CDkPTJYWcQeLHLdCroV9RZO5pqM4D-OqoJAWiC90OigB8Lyfp-fg_xHCpWWBn3PPxBcq6L1zUZjjtAgsCCjPa_JlPLthDb-JQYDQ6Jx3_EivIuYLVtZwMUwOd6KTMiwWz785lzzbN_cJcUZkCDIMuu3ZlKTRmMD0ZLF-inIua8i6Bt0Ai1kDIF2lwaAjVsmkRFgTi3_u2WyO1mzyae3T6JRtZ2dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تعویق یا تغییری در زمان‌بندی امتحانات نهایی دانش‌آموزان وجود ندارد
صادقی رئیس مرکز اطلاع‌رسانی و روابط‌عمومی آموزش و پرورش: آزمون‌های نهایی  بدون تغییر و بر اساس برنامه ابلاغی، از ۲۱ تیرماه آغاز خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67769" target="_blank">📅 10:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67768">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95215f1b5f.mp4?token=AB0711uqWzmYoAUYqqPB2sHzRqexiZ1kW7fB20LK6O5X2HdP6wB0pttmABootReIkoiUviXko617bYb14fLEztEPelTgwzY_zaemgoKKMf6-yWRslGk_hiKcTH0xsxnAVGqiDhHlNbM7CWtSvK4mfaFj7zpIXGuGBEFBeQ4dt9sR4p9wtVPq1kuSMeAJrQ1iuy0YPqFuwhBD2II3tFpSxu4TF-_dB6KrA-vw9a9Uer5W9REtjvj9bsIDkzAK1pdB8wxJ25PT16qVPr0ct3gyh4YZeYnmK2DLnNZcdji-legFMaX7qRPOZLOgvINjjm_BMD7hqL6IkD6dP8NFwq1qCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95215f1b5f.mp4?token=AB0711uqWzmYoAUYqqPB2sHzRqexiZ1kW7fB20LK6O5X2HdP6wB0pttmABootReIkoiUviXko617bYb14fLEztEPelTgwzY_zaemgoKKMf6-yWRslGk_hiKcTH0xsxnAVGqiDhHlNbM7CWtSvK4mfaFj7zpIXGuGBEFBeQ4dt9sR4p9wtVPq1kuSMeAJrQ1iuy0YPqFuwhBD2II3tFpSxu4TF-_dB6KrA-vw9a9Uer5W9REtjvj9bsIDkzAK1pdB8wxJ25PT16qVPr0ct3gyh4YZeYnmK2DLnNZcdji-legFMaX7qRPOZLOgvINjjm_BMD7hqL6IkD6dP8NFwq1qCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
انفجارهای دقایقی‌پیش در مناطقی از تهران بدلیل خنثی‌سازی مهمات عمل‌نکرده بوده است
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67767" target="_blank">📅 10:06 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67766">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a14613e56.mp4?token=jAcK1LLz6hx9abugb7mry6YJ6T25Yv9l8xwId5BPzdrXzHVx9IYwSP2VzN9GojQ8L4LlgWDWwFDbfscpKiT_OzJJq8lzXCAzuSOZvBgDuO9p01t-fmVe7PFBLj8gvTcU0bOlbKgO-oXB444JyE-kdpSTnc4zktBYc8WdNKQwawQ88ylh2Jnoc_i_it5NAAeyZMPNgPytaUazZb8hyEqFAvgf67rB0r8kij_BqLUIe11ziC2i5fEidjLgAdbF7ppIwAKvH9fmFJ0FS82NvLQPzVEF0FUV5htFYftfH7uAF6Tuvy17GC0tyE7qG1z0AoxgR18YPdXp-WdGjL4n-pbVOGxTwUfybspfsQObTQI0paSxqQ3EAtxtJbj1HW-hzC1dvaYrrXe8kbdn7QL5MEKKETost4TovQyJ0KammTLgF-35zoxU7TR3GBcgzngwT2CGagY8pWCLuIWq0Z9K9iP_HO39C1WMXs9MlVTfp-KYuYFvdNRyZLztSk9m_H9oPeryVfp-y7BBk8QZTsjzDuNVgtmY8i4_A-2kM6SxmEJkqEnbIBeSeC7yytmGaRqu1A0Iid6tzqSO_r_kjNi1Z_jbkxcMUlj0oY78vOfQ2RFbDc5GOXbGONtk3GCITk6lnbkzcYL9AEEvfqy0bxyficotBzJvgSGRXnRV6q-jmpPj4Uo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a14613e56.mp4?token=jAcK1LLz6hx9abugb7mry6YJ6T25Yv9l8xwId5BPzdrXzHVx9IYwSP2VzN9GojQ8L4LlgWDWwFDbfscpKiT_OzJJq8lzXCAzuSOZvBgDuO9p01t-fmVe7PFBLj8gvTcU0bOlbKgO-oXB444JyE-kdpSTnc4zktBYc8WdNKQwawQ88ylh2Jnoc_i_it5NAAeyZMPNgPytaUazZb8hyEqFAvgf67rB0r8kij_BqLUIe11ziC2i5fEidjLgAdbF7ppIwAKvH9fmFJ0FS82NvLQPzVEF0FUV5htFYftfH7uAF6Tuvy17GC0tyE7qG1z0AoxgR18YPdXp-WdGjL4n-pbVOGxTwUfybspfsQObTQI0paSxqQ3EAtxtJbj1HW-hzC1dvaYrrXe8kbdn7QL5MEKKETost4TovQyJ0KammTLgF-35zoxU7TR3GBcgzngwT2CGagY8pWCLuIWq0Z9K9iP_HO39C1WMXs9MlVTfp-KYuYFvdNRyZLztSk9m_H9oPeryVfp-y7BBk8QZTsjzDuNVgtmY8i4_A-2kM6SxmEJkqEnbIBeSeC7yytmGaRqu1A0Iid6tzqSO_r_kjNi1Z_jbkxcMUlj0oY78vOfQ2RFbDc5GOXbGONtk3GCITk6lnbkzcYL9AEEvfqy0bxyficotBzJvgSGRXnRV6q-jmpPj4Uo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfHneVe7pwQg5dZcoVErJFJiDEsYP2u7HFZX_J_YE9qNBKKou_gw9CMHFNmaLnbyFlCaHaKKOhDuk9I7qcq_CQi7DCxdqQaPwPE4ezSriMfHED72dJXrZB6nmTdbzaSQdGM1f1Gf_ijRWk2QaQ33pB6c6Z0ab3kiIbab3nkPrh4PI1hx2Pv5p874P1BLup1PtRDJqVI_XHG_ltDQ8bqp6PQLEK9mqirZjbByrEEKtvSeMTKuXqVnpToJCqkcSxc7rOVhdKBxvv0aV_NdDnBaVc6Otpiw-4_b3GXDOrmnQ3HaMh2KMbZ6bCYEgjc-YnAUfVlWF-7tsLFC8LLUObcUiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/pHlyyW0FsGO01TBeMz6pTMqbugG7d7ajVMNjAyAEiDKQ2nu8RktfXRFoQBP41AbwB8gYhGQ9ybxdIBb9pAXXa0WvMcc0w_kZfWfXOX5QtAjHuLT8_xJoK9xa1rkgMToFyl1Lc8bscuA6J_P2vEt5jkCVtqJxHfw3WokGMwXD4zZmra487UZuzd9UkDo6scKdid4zrodDLQL2IXWrQPpW0A47ZahZvs4jkoibvJkPi9ggdbJGjJfYr2ozhNe284LpwSWm0QWo31R3mz_6IQbCI_e9jG_qMnJkDAImLy9v89ubRvXR5eU3btLRgjZYMzfJS6qCRtXeW11mLBAwvR2aWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulgCdVf5GtQVoxzqnFL2Ysj-WSiEFEa6bFg6QJXGXNkfaULJvqLT41gI0ewcPyPPMnVCw1EiNnjV-5illwVz7qAwHMquDG0mSON4kP1kcPdIFe4SwH9auqOml34tf4gy_7A3KwdFSlW0avMJGn5-DrwYv5L99y_m3LqbhEJ2o9I6zzD6WZkjovTXkXRuXcNBiNnHlVIeegCLTOiN2pmmtbwaZoYnJHfAB9hUNj30kBEQabeGI3TD9sowgIepIa7q69QuZNHsTE6o1KbmsCPrFBEJ3XUhudr-TV2CektjSyi9dwTiV-1A4Gx7lCKxyKlnzVr780PK7Um7zM4UcdhCsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حملات ارتش اسرائیل به نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67762" target="_blank">📅 01:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67761">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZY4JxDGoNwW5Gj6nn1X6evRuR1bo1-5Wf3DC_mY1J0BTINzAf7SsiueiFwSDnpjeWcNmvH40GZBNJ5N47tgZM4R2Erx4TXEqNQCKt1vfnXcNvfhxNiaVVBNzME9fJbDjQEpwwAYkEqqBVO7eC68mZimxKceNN8NQOkVRL2SrHmnP45joiFhnykFvdXj3MwuW-etqB4Cn4Y6n98kAn3mAdl_NYf47JTADLDMSv1heBwT0ilbvYl15dN_SoWs1BcY-ytjiIW5KoBkfgxqMoMB_14oVMB_uGZqzXplu2N9QOjtpnydCeT-FPixnH87zSodFDdSVaySjEjgQF-kc39tP9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید:
به گفته مقامات آمریکایی، ایالات متحده به ایران تا روز شنبه مهلت داده است تا حملات در تنگه هرمز را علناً محکوم کند و باز بودن این تنگه را اعلام نماید.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67760" target="_blank">📅 00:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67759">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">کشوری غنی، اما مردمی فقیر
💔
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/67759" target="_blank">📅 00:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67758">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
وزارت آموزش و پرورش:  ممکنه امتحانات نهایی به صورت داخلی برگزار بشه.  فردا در جلسه ای در موردش تصمیم گیری می کنیم.  @News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67758" target="_blank">📅 00:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67757">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
وزارت آموزش و پرورش:
ممکنه امتحانات نهایی به صورت داخلی برگزار بشه.
فردا در جلسه ای در موردش تصمیم گیری می کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/67757" target="_blank">📅 00:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67756">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/024bc9f4e4.mp4?token=Tm_qSgGF83f7nO8xDp-NdUXo38ymkmB0WcjMKcQxk8NFu2TW7dt4sKvCfH_ZqYIVzIOuhMtB37kjXVsITY29a8o63qQT15tpT95G_V1BOTRvk80d6Dx9vUscZa4-GHazbbUjLJTqIVp1ahRiPUHJnx4mzL7DjvTA-rW-LNjHgCiyqz5ppL4xyXZDbRhJwtcqtCh-ksLlUzvHWOqbwYvAy8B2uof3uE9ZfYZtmniepbaSuhDpYEOHsr6dzvymYcpKsk6w8heofVfHr_SPM6nwjX50AVvPwRUkS_1Y4rpP7pLAuz9SWY1SdIKvjwNdDm0-3fJmJKXpxRj5liJAu_1GUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/024bc9f4e4.mp4?token=Tm_qSgGF83f7nO8xDp-NdUXo38ymkmB0WcjMKcQxk8NFu2TW7dt4sKvCfH_ZqYIVzIOuhMtB37kjXVsITY29a8o63qQT15tpT95G_V1BOTRvk80d6Dx9vUscZa4-GHazbbUjLJTqIVp1ahRiPUHJnx4mzL7DjvTA-rW-LNjHgCiyqz5ppL4xyXZDbRhJwtcqtCh-ksLlUzvHWOqbwYvAy8B2uof3uE9ZfYZtmniepbaSuhDpYEOHsr6dzvymYcpKsk6w8heofVfHr_SPM6nwjX50AVvPwRUkS_1Y4rpP7pLAuz9SWY1SdIKvjwNdDm0-3fJmJKXpxRj5liJAu_1GUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
اسماعیل بقایی سخنگوی وزارت امور خارجه:
ایران اجازه بازرسی از تأسیسات آسیب دیده در اثر حملات آمریکا و اسرائیل را نخواهد داد و قطعنامه 2231 شورای امنیت سازمان ملل عملاً اعتبار قانونی خود را از دست داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/67756" target="_blank">📅 00:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67753">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jrGIaH9k8iDb7_PqzOyzNxGuFD0RVzj47X-Vf7dahmDa_PVvMbJBFrda21nqkxOxbbuM1VmLc1vVTwPisE0u-N1zuxnZ-hyCwLIixpBv-qgTy5FcjAkxX1vKty52IPX2v7aGGdluBcnEApbunt3Xtrv7FyhVRZCQJKTL9R-CrTZgx3uI_87GvPZaGsb3dKPIZ_NBsEcoHxdFbF8MPBUlddpWoYqDlnGTGbAmmNj5XfGJSVk26vwLJRNHAAiv1BmX3XX64B1c3WcRd4W4PmI58-2I48deffDoaWHe945HVtxGXRauXhhsNBon8oIAGSH1a_btbfjva9IY6tQQn4k2rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ItsJ3JLbXVATp-6aqkZaleFm4CTXnOEYbBLTJ3T8AfwI6vJ8xw8we_gFP2nmlcBG-aMwd8cBFUD9qZHhx3pNYVWyt-7t3KMXyVboBBNVRerTipcme0EH5MiPTQLmCGUrK64NmjxZeFtVFcT2BLP5f-3F5Yq3Q4W8i-ysw7Jxt7mEU2YO8-C_KOS62YeRN__AiQWsR-BMbm3Cz58jcGkpJNgGNu6ps0zK03_tDbbaJc2j9x7hIc-ZQlytHZz9hw7MEfNpytjIrvrX9cc23Ascaa-RIfG-wrFIBOwnPytZrPQm10rRCCjWoapJcWcqy5ix-44jFRlnXfm6Ygd2_1lz-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/to9vQFAElTjFQRdMs7vz6pGQJyQMMeusUGEoMU3EPv4avk9ADSd_G_bEhYD2tzIQVOpktrZNN1T3O4QVBWfAakQJncR1-AbFF6INGjkebeTgEAm_iF6MOlEKSv0ID2hRjPjVqg3sdRh6s3e6TFfBse1LCWDsh850GyyMmHZmlOJGzp6EAWNJ-IIYk9U40aXiM-yAueN3GZc8_gNsNIgRRZMuax1-qzAkYnWVHbO1UgLg4E6BfZ_I3nsr16tsATO0B19C09IiJKwTBN6v5xM2MnIzKm4DhCOYmKEoszi9Z7NWO35muAbI0d2p6bbeOB37yqJdoUbvdGts9aTcaE7zeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
⭕️
شبکه خبری CNN تصاویر ماهواره ای  ادعایی را منتشر کرده که نشان می‌دهد ایران در تلاش است تا تاسیسات هسته‌ای واقع در پارکچین را بازسازی کند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/67753" target="_blank">📅 23:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67752">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08e999307d.mp4?token=FRl0VB3IJGWidJNj3JDioXP3p__MmHyAm65eHr4LPWh9APx2nmciJ62P6Gj0Q_arKhoODO-6pY979IE-4S51RCVy8MpxjHJu8GjmJly1xX1v5y_vzjRObnjPhcTzCuPusSw-WDSTnFKBPGo87Z-nVk58l7H1meBaf6BCycndLPhOlYF-wOQMlJwEZTzxBd7hUcbNu5sa7utQKUiXsks2eGI5XSkRqyWIoLuKVBy6-M4Y_Q8gKIubAssBQIAu9J2krJcDF0qDbvIY2nXzpnf1_QhsqHYCzH50yonf976jv1NHDSKHl8udJxtPfLujkEjEJLU02fBEdvPtE-MeFB0DyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08e999307d.mp4?token=FRl0VB3IJGWidJNj3JDioXP3p__MmHyAm65eHr4LPWh9APx2nmciJ62P6Gj0Q_arKhoODO-6pY979IE-4S51RCVy8MpxjHJu8GjmJly1xX1v5y_vzjRObnjPhcTzCuPusSw-WDSTnFKBPGo87Z-nVk58l7H1meBaf6BCycndLPhOlYF-wOQMlJwEZTzxBd7hUcbNu5sa7utQKUiXsks2eGI5XSkRqyWIoLuKVBy6-M4Y_Q8gKIubAssBQIAu9J2krJcDF0qDbvIY2nXzpnf1_QhsqHYCzH50yonf976jv1NHDSKHl8udJxtPfLujkEjEJLU02fBEdvPtE-MeFB0DyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیشب ترامپ رو تو مشهد دار زدن بعدشم ماکتشو سوزوندن
گفتن خودشو که نمیتونیم بکشیم حداقل ماکتشو بکشیم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67752" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67751">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InWkLU4eYCA9VknGg_rba6yYcXhZcqsxIRNKfVcK8KiRlpVUappAWHHTtTwCioSLAH-xCJVKjqjjWUIhUOHMuuiGi4sngTo_IM6S8cCr5w3dGrAoPBl3E3jPl0bz3Mg_9tGv7XJTQ47vIOqKy2nXoC88jDOlAw212nh2tsfmGwLkCJC060sXcrNvXSNAyAEZDG8GdQPQVLCj_Z51lV9bC8aLdRKOdpYahrpQ4c7z_b1wres5yxFlz_nKI9s7PF27xbthzB_RUe-v4zfWAOzso1qYB2SoVOaIpM9U0RuFMGaHT6QDisHgSvrJ7pkMNf2dDnv5S7c9z4ht3C_Qe6PiWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
قالیباف:
در جریان مذاکرات، به معاون رئیس‌جمهور آمریکا توضیح دادم که ما به شما اصلاً اعتماد نداریم.
به نظر من، تنها کسانی می‌توانند با ایالات متحده مذاکره کنند که برای جنگ آماده باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67751" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67750">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromnegin</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXwI5HhdHWKryZrE1unskc4amEcftxxSWJDh6iU_9HxPKLLnBrNfKa7mgKiEa91xIFCU_Sll0wpMOYfJAWnzvdeDHuD-8vy1diAYlmpFDadKf1laClKi9uUMXus0WqKFVBmDTfj5JBAixph07GtCExjsDdGpLZwbWka753Rld5-B_AcZZ6VKpv6D9kzS4NAWMyMpvbje4l1PiWh9Du8wM0dqvzQtYdwtl7jdbXk7IL07SqMFdtVI46Jt0Vper403DkCIvJWlk9nKZs6ZxfTX6723zIXtmCjHIWk1_pdKHse2eY8CDF9ARM2buZZ6FLyViRBvFBFV7dkV4KjNHiJcKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ad131e48f.mp4?token=HnhIPPlMBtANjbUjZj6qJvS_OP75ms5RvXWy9jKFylDg--MZZX6q90r8rr_eCHfcWcAq4S_0m_Alwt_62biS_VmaJ1CH25cNfu1YngQoAYq1q3thRIZmem3nrKiW9alLHTSVOj4SGAXxhdQlSl_6cvCb_AaUB1h4PNHe6r1kaEGw8QAtsIUye2bxhP6qDMzfc-tMC6wqM5w7JpMlxnyIP_lzSu72Larte4vX319OxQYMBXQSvXtOWBBa2EfNsGpIIzu7CAjSZXgKbZUv0Bf8PGOoiJjIc8nFsfz9dBaBJhX_a4QbOJ_veiVY7xVAMANxUqj1PrmzWm2YQb5ZctwhaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ad131e48f.mp4?token=HnhIPPlMBtANjbUjZj6qJvS_OP75ms5RvXWy9jKFylDg--MZZX6q90r8rr_eCHfcWcAq4S_0m_Alwt_62biS_VmaJ1CH25cNfu1YngQoAYq1q3thRIZmem3nrKiW9alLHTSVOj4SGAXxhdQlSl_6cvCb_AaUB1h4PNHe6r1kaEGw8QAtsIUye2bxhP6qDMzfc-tMC6wqM5w7JpMlxnyIP_lzSu72Larte4vX319OxQYMBXQSvXtOWBBa2EfNsGpIIzu7CAjSZXgKbZUv0Bf8PGOoiJjIc8nFsfz9dBaBJhX_a4QbOJ_veiVY7xVAMANxUqj1PrmzWm2YQb5ZctwhaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رونالد ریگان چهلمین رئیس جمهور ایالات متحده آمریکا:
در این سخنرانی، ریگان با یک روایت طنزآمیز، دیدگاه خود درباره نقش دولت و مسئولیت فردی را بیان می‌کند؛ روایتی که سال‌هاست در مباحث سیاسی از آن یاد می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67748" target="_blank">📅 22:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67747">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkGp0QFkbnRvTbNxQfk5JcWMD-fc10P2g6LqhnwKQwMStqVqIUaCXh0VbSRaZBRH_Dfiy-iy4XK6jvjmqgkgKkxUUlzGl6OWxd69waPkgA2Adn8psXQwakFSqDOUjrpwnOfLDpx46ZS9X9o2ygPvBApThOyI7xTWTu1ZjJRXYhHiQXAmTkz_eQERiZtaiO3QjhBByAudwOOIPjxK0FOrvmHlKkuqT4wnCjneeIlqvsRArNVMUY0ob55BCfVsdNxUq9K-PO5rMt6T4d3zvGCLuh8oASDBy1LOvJgG2Xslp9PdxU7rBhY_V4I24WugzptbP2iyNnFgelXKPqwCzh4W3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسرائیل هیوم: آمریکا و اسرائیل گزینه‌های براندازی جمهوری اسلامی را بررسی می‌کنند
روزنامه اسرائیل هیوم در گزارشی به نقل از منابع دیپلماتیک منطقه‌ای و غربی مدعی شد که ایالات متحده، اسرائیل و برخی کشورهای منطقه در حال بررسی راهکارهایی برای تضعیف و در نهایت براندازی جمهوری اسلامی هستند.
این گزارش همچنین ادعا می‌کند که در پی تشدید اختلافات داخلی در ایران، مسعود پزشکیان، رئیس‌جمهور، و عباس عراقچی، وزیر امور خارجه، با فشار فزاینده جریان‌های تندرو و فرماندهان سپاه پاسداران روبه‌رو شده‌اند و حتی احتمال کنار گذاشته شدن دولت پزشکیان مطرح شده است.
اسرائیل هیوم به نقل از منابع خود مدعی شده است که عباس عراقچی در تماس با میانجی‌ها اعلام کرده دولت ایران نتوانسته موافقت سپاه با مفاد تفاهم با آمریکا و توقف حملات به کشتی‌ها در تنگه هرمز را جلب کند.
این روزنامه همچنین مدعی است که یکی از گزینه‌های مورد بررسی واشینگتن و تل‌آویو، تشدید دوباره فشارهای اقتصادی و بازگرداندن کامل تحریم‌ها با هدف افزایش فشار بر رژیم ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67747" target="_blank">📅 21:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67746">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gA-bsKa5vnV6qgOJpe3BoyS3lJOY4PxzJQbvtLxlc5ZdyCFS89R4lfnc0csOM78WEuGrXqF1wjRdI-xsomUCWIFtPgipQXFaMOV8Fr_zZBJYWdGCeIgXjqLPy5nldlvOxgolEjwzQQ61FBwHSjfLZayDwpFTssR4hZXBJVyJWATWS5OU5aon0HQtxj5K_kwSGWi0e03BEU6BsctcQ3Twyu4gvEH6N4XwP8GKu-omwMpNSHCKTeDHMpfx3evYh_Zruim85sEDK4iCdX3zC9F5QmHi8kkA9OrsPTDaFaO3AJKA4oOxsPF3RPLCb8BjIQkskuXqXni8WmkkI_Sj9QTwQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
باراک راوید:
بر اساس گفته‌های یک دیپلمات آگاه از این سفر، مذاکره‌کنندگان قطری با هماهنگی ایالات متحده، به ایران سفر کرده‌اند تا با مقامات ایرانی دیدار کنند و تلاش کنند تا تنش‌ها را کاهش داده و شرایط را برای از سرگیری مذاکرات فراهم کنند.
این دیپلمات گفت که جلسات بین مقامات قطری و ایرانی در تهران همچنان در حال برگزاری است، "اما واضح است که هر دو طرف تمایل دارند به توافق‌نامه اولیه بازگردند."
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67746" target="_blank">📅 20:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67745">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkZ87W_0d2LWM_nVJALABo38j2cA3bsel8AwQ1O1cLeeru1tsIDF58RAN2OtQp4hTVr3vqxjG1RBEZNRHgjuzs73cQICPZw9mRexD6wgZOn54ua6Vt-f9tuWFUJwle7lxZUbpTaLw2jtST2EK5s0syUSvIUoNgjeaNFBJh86MdxavEtu2NpJc6XrbkPfwJc7FFiE9gDzf7jeer22GKyUsBRyDQ6d61p2D15XMealeF1ZYTfgRtmO1L5CkQFQ0Y7P_17jxvd3AfN16TyDrqTxlMfJGuvpgSA3GHOioeAgAiiU8vqwVPSzSeqGzVu5gH6ATu6SL4i8L1C0LaluTbS1Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ به «نیویورک پست» گفت که دستوراتی صادر کرده است مبنی بر اینکه اگر ایران در ترور او موفق شود، ایالات متحده باید «به‌معنای واقعی کلمه، آن‌ها را چنان بمباران کند که هرگز پیش از این ندیده باشند.» او افزود که «مدت‌هاست» نفر اولِ فهرست ترور ایران بوده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67745" target="_blank">📅 20:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67744">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0ZynsOtxOeStnxBL3Ni8eBhmDTDmQ-E8P7M0XLaoRtI07VjGZ5pdGUMGLCTyxdGDiA0xYSISxCqmMFkmRa45Sej1WnlV8V1Q5AInHlNlCcpFI0E_lgrbq5P92YnC_qwml8hUGhd_Q9SRA3YyYiffn3lOkD5rZuW1SFRDQTabJjAqxFC9_MgUosVXiXLTggkmQR9kt-C8LzqkSk4dBAs7tPl8ueeAB2Ml8PZzHo2nkunNUkgFzdAYfWXTWDQDNhr4HR-4Lj4MMGXyh-qQEfjwNMYQo-9I9Scou-s1RjaHeYuQZzTo_IoABQTj5y5AffqYw4lhs7Ir0ehrfxAT1l79Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مرندی از اعضای نزدیک به تیم مذاکره‌کننده:
ترامپ و خبرگزاری آکسیوس را نادیده بگیرید. هیچ مذاکره‌ای تا زمانی که دولت ترامپ به تعهدات خود عمل نکند، صورت نخواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67744" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67743">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
آکسیوس:
پیش‌بینی می‌شود که ایالات متحده و ایران هفته آینده دور دیگری از مذاکرات را برگزار کنند، احتمالاً در سوئیس.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67743" target="_blank">📅 19:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67742">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/258d1105e3.mp4?token=rd4XqYNWz4AjeFRNyy51ZdS9upaQD88tI7dANQH2d-Wry2svsbXKYg0HOyiHBFgHc5_WweVQSRBsilxCHzER4l6m376Mafuo0QMGAxxp6qtjtMUguCxPocvMvLFmaLVgmdmGa2iC9SEzznPP5m6T_Y2jEn6OPzurHhXRhDcuhO-Sg5mgMYLDaDCP46xiPdkM0RbDLzpfKS2dPWtuyvBkYRy9QDnBMdHPsA0Sp-GV1t_sgD9TtOE3twAUJrvsLIL9QgSQ3hX-SLKreRJI5u5Yvp5sztU5Hx0R848v-o-7eWDT2sMGIvI63JXufeGB_398FawRgggPTThthBDMF-lMxw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/258d1105e3.mp4?token=rd4XqYNWz4AjeFRNyy51ZdS9upaQD88tI7dANQH2d-Wry2svsbXKYg0HOyiHBFgHc5_WweVQSRBsilxCHzER4l6m376Mafuo0QMGAxxp6qtjtMUguCxPocvMvLFmaLVgmdmGa2iC9SEzznPP5m6T_Y2jEn6OPzurHhXRhDcuhO-Sg5mgMYLDaDCP46xiPdkM0RbDLzpfKS2dPWtuyvBkYRy9QDnBMdHPsA0Sp-GV1t_sgD9TtOE3twAUJrvsLIL9QgSQ3hX-SLKreRJI5u5Yvp5sztU5Hx0R848v-o-7eWDT2sMGIvI63JXufeGB_398FawRgggPTThthBDMF-lMxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
آتش‌سوزی گسترده در مجموعه اکسین پلدختر در استان لرستان
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67742" target="_blank">📅 19:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67741">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ua6iUeC_c8SHdanJ0--FCo86cPoXUa0BiQeXmH5NyuBrwWaQcU4aGrMXilBtUkcOnWDgI1_aKDiGvfputnnwSujM05SZ7-Vm3Z4ycvSrbLnxYK5rpdJnVyQM3sTmdp47BF4-I74UAVDrBmA-1G0yMztwjiELapzMcDptUWJmufKUuaqOeXZG2B9NayxNeiOfEqqBsHO3enlsvUsbmnU9eT2-3reqNEDNwXDeuBWScQMKnjJbUD8ecqIxFztoaqjvKX2Vbtw4i179JY_l3D1cRZSSHLoUqpvZ2141i6AHtAyQ4cdAAVHRVymgb0rPd4OUF2Qy8m5cLHFksEzN6Xq8EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
انفجار در پالایشگاه نفت پلدختر در استان لرستان.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67741" target="_blank">📅 19:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67740">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvzCjFOHt0KJhocmqgVJLKVMs6rdxc3t45xdOW9biXCU54uoypRAG5GkFEvh4a6dy6b_aN7Ic9_7ePj4kY1GIOrMzi1eFUHg5j50GgeRlmkTeSmPbp5Y2-UlRIRMnxyOnVBAfhRBzMA0vBJ1TShdz_9KOesP2KwRhFRpCYVczermVAnT-JRyUKhDj4cs0bQEYgnPk6DTreHVHTJ8X7lzA7p85XFdE4mZ2eR0WUtU27DZ0yH26kOCC20cWnacFOoHO6KMbXOlkHa8W_rmRFwItfIZ-gbbnicDvrNs-c9PY0poRVgHvTtsrQc-F0zKcGaXNnfIFPzfB4EWfysygYTu_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
بلند شدن دود در کنارک پس از وقوع دو انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67740" target="_blank">📅 19:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67739">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d335d453d.mp4?token=d5QwhNujW5SJPriNqIUm09dnxKdjxS0O5gWJcIhytwZo_1iHSjBdCF2b3ivUbrZPCUkk5Daqjh7vCumDUFk15opaAjIFFSivgK8Jp_Kx-BbCivvzyAyeScRHEvfXeDa2_CzS1TxbHMCYvg63ezqftTFm9Ig-DlcbdqjX26MX7bcb8I-zibPt-RrR9KvbIe74jm9j4BF0e-QmVkMfGYZCdL2gTvb4_PmB2ThuTa5UmyBqFkK0EuBKWCdJSzFv4b1QbuluZf16NISs_4CET2qgSZQYY0al6LqyNE0hP0jQovg8aX2FeigyfjwXDmErf7zV4PbkJKCKHAswov70mVgwuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d335d453d.mp4?token=d5QwhNujW5SJPriNqIUm09dnxKdjxS0O5gWJcIhytwZo_1iHSjBdCF2b3ivUbrZPCUkk5Daqjh7vCumDUFk15opaAjIFFSivgK8Jp_Kx-BbCivvzyAyeScRHEvfXeDa2_CzS1TxbHMCYvg63ezqftTFm9Ig-DlcbdqjX26MX7bcb8I-zibPt-RrR9KvbIe74jm9j4BF0e-QmVkMfGYZCdL2gTvb4_PmB2ThuTa5UmyBqFkK0EuBKWCdJSzFv4b1QbuluZf16NISs_4CET2qgSZQYY0al6LqyNE0hP0jQovg8aX2FeigyfjwXDmErf7zV4PbkJKCKHAswov70mVgwuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivv1tm636dy-uBk5dhKQezSzgBzTvzLhRlA_oZHPfHJHNIQiXZIEVH3zHgMYD1RUJcyI7c57Njc7HUn_OHMvJ-0qTQoOzSrX2roT7Uyj1-S1PRAUKwc1hiXlEtX656y-hKXV64SrJKQBFAJVoqRRKhtMrGVwyrUJBQI_TVjEjmJhwLXzKnQ10Wp-bIGOen8hkDbyHOaMYOOY33y6mkXdhVIUVw4MMfEuFOtmtSgLWILI0ds2BCVYyNUVY66DKXM5pOl9ER-yp4blnDny2Pim8eI6quhtC4vE3KoOh1hls5KbAqzLumfUFXVYPT1hO7pog20YgSN4UUsmzEcLWjrN4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VACFcQ3ZyWA-iBHzKQzhBtc5YE3hxbRy7nqCcVCnTw9RMRfJ3rJU_3mZYNyqtBFP2AVVedS8AINsU3GOq5ZSJeBRTkFTpFC698JhuXT9bjLgeJ_TaEtEY3n_zAj7N7KmVW4-UdN2bNPqm0T-uMRFupLTxHpAOMiLFOhm-dwHjbpJjYPFgHs5UlM5SPnfgONY_Vea7a4skC8m5VuTOdDXM4PKs6rECxQfiI2mraINXVVDfNEB2pR2X1oCz49UveFGikyUsHsmzIxvzE4lr-4FyBLY1xPwKALxMltC5yv_nyuh1roWRWrzbuJufdmg198O2u2OEOECTMpBXtp_io-a4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نیروی دریایی ایالات متحده امروز حضور قابل توجهی در خلیج عمان دارد. یک ناو هواپیمابر و اسکورت آن (حداقل 3 ناو جنگی و یک تانکر سوخت) امروز در فاصله کمتر از 300 کیلومتر از سواحل ایران مشاهده شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67737" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67736">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be0edc864f.mp4?token=mNasvUklbI6zVWBi7qAkukgOiJMRwAkfJ18IOFbN8rsLPOl4atVS8pGggf1vMhrP1CJvqqtnH29UVGndNhToJZMnNpXFLfjVMg4uuoI3FDT7PafJXyURVr_AHIgb7yG8zXjRkXYW9nC5nGCtBaNc80Cm9LAjc_6A-10BZOs_SwFoG1AppgFo-hozqXo68IZwN_JmcZHgW_qCuUif8S6mBnnuU4kbMAQoVVWnXf3P8BH_t9TR8fvY2QsGCZveszWfmzzCQSJvifyDcSSd-Trz9oi6pablVLkjcEDzNY7akJWqWKUjOViEx9qoQfhiMQfl9dE7RifeyRT2nZeNmvGvmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be0edc864f.mp4?token=mNasvUklbI6zVWBi7qAkukgOiJMRwAkfJ18IOFbN8rsLPOl4atVS8pGggf1vMhrP1CJvqqtnH29UVGndNhToJZMnNpXFLfjVMg4uuoI3FDT7PafJXyURVr_AHIgb7yG8zXjRkXYW9nC5nGCtBaNc80Cm9LAjc_6A-10BZOs_SwFoG1AppgFo-hozqXo68IZwN_JmcZHgW_qCuUif8S6mBnnuU4kbMAQoVVWnXf3P8BH_t9TR8fvY2QsGCZveszWfmzzCQSJvifyDcSSd-Trz9oi6pablVLkjcEDzNY7akJWqWKUjOViEx9qoQfhiMQfl9dE7RifeyRT2nZeNmvGvmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدیو‌ ای از صحبت های چند روز اخیر ترامپ که در حال وایرال شدن است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67736" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67735">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JJZ-6ygbbnfulMkwgUraFN62oDRQCXNBYGQpPb4bY2cssdpVX_i0kJuON-R9vIrKkg-MDyfzjciKwwCuRYZ4eipbWfg28O5PT_npkz_7NXtMQeeDuQKqMsDeYwhzEvqMCdHDCU5TxDwhmNtqUVJei24oEE5Lv9RahtER1z5tRmfZG7mCnvxMb8bfgLVpVfuohZsal8aEvtTStEBoOmcTbObGV_Ad5GV_klPtOhqnnno2lT7zUY4OXMccu-j7kKBkZhW0Z0q14JGL6Z574UZgAljSk_zpWvEp-Zssqc1o2IgsfiAzvV8C6zH1KjLJ0wvdbELXxOsFy9GEx79xPiS5jg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3d6c6e5dc.mp4?token=ROK98T8hunVzdkOBZKF7AX8O41fO67bPNan1YCyU5awQyM0h9JF2TinIXetvO7ufLniZ-yJa8cX7hhUT5tR9sUILOvy9fCG_stj0Y4fqfIA_0NnTiP4o0kSjYn4FVmhFiJCCH8cEj8ADuF3h11E8UAjNEB1T-gcVX3Hqr6oJ0Im2zNWU1ZbGTozFYz_z_MZ03SANF60SKUOcV3KwbTU2y0LokXlRyw07a286-fZ1bdybJzBAtN4tUFO2iD6hkP9flvC1FBGEaOEnWV72slDsTeTFQrSohV-XbVOpX_4JrNiIp6--l9VheV3qz_shGaPLCTcciMoWfJXxpTF2WXqb8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3d6c6e5dc.mp4?token=ROK98T8hunVzdkOBZKF7AX8O41fO67bPNan1YCyU5awQyM0h9JF2TinIXetvO7ufLniZ-yJa8cX7hhUT5tR9sUILOvy9fCG_stj0Y4fqfIA_0NnTiP4o0kSjYn4FVmhFiJCCH8cEj8ADuF3h11E8UAjNEB1T-gcVX3Hqr6oJ0Im2zNWU1ZbGTozFYz_z_MZ03SANF60SKUOcV3KwbTU2y0LokXlRyw07a286-fZ1bdybJzBAtN4tUFO2iD6hkP9flvC1FBGEaOEnWV72slDsTeTFQrSohV-XbVOpX_4JrNiIp6--l9VheV3qz_shGaPLCTcciMoWfJXxpTF2WXqb8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLqVza3LDbPzcXf0d-roZ3du1Z8GBuf4I0AQwP8Gt02dqlTMwlx1UJFtHU6cPsAZP7NyQtMFMxDDfh-V_nw0LWo0hbqPAoihvoIqwiS3fsyU6cn_cGBhAY36kBuOQjVx-WHBwIEv01KqxVp2NU4SKbUT3-HbLUdQzSOjLsWZ_oMh4JbNJJ4A2pptoeDIP5KbjT_Q1a6AOJlfqu-vTP2WmpIiVfv3mg9K3IJEiEJPn1p0a5N_hb2aET_awOo-rZNxlvXEwTXjW3r9s-kSQ45ktWZvFlD_xt871eLyIF0kHlIACwEYCWDBl97BVMB_VOvcpx2y1_lre8Uwq8gyWeax1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کارولین لیویت سخنگوی کاخ سفید :
جوون‌های نسل زِد که از وضعیت اقتصادی و زندگی در آمریکا گلایه دارن رو بفرستید ایران خیلی زود قدر آمریکا رو میدونن و زود برمیگردن
😔
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67732" target="_blank">📅 16:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67730">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s75zF__51UA_hRVK1XudY_1-qfj5FF1fQjseIa8Ek10JL1uaHj9lJJu_hhnc3xeVU2KUD2P4yh-7vdP9IHw03XxpS-a-CotoabnuesgrL0Q-dznDCdnqHg90YRP0L_G-7rcR2uIv3CdAHRBdCNgWM36BkcUji-IY3RciXbIccuuKloyvwbeP_ld7MeWdOIGg8p3xFjmIAFuuCCAbJbF4xrZPd0Z7tCQUPvQcL_VkcngEYJlf4uEjizY7GMg1z8KtE8AJ3ZB3xx59QiFo6roG6d41IJ9rk3tBEDj8hijYqxNDjXA2ngOCBJWYlQ_4BGCKXb5lUnNDsIfe0wyz2wbcVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1372691bce.mp4?token=g5Mh68SRIGhpepgaCe3FmjqwGvq--i5-BDe6ljC3UAvImCgoc82FylWyqDiUnskekpLgXkgPhI_M409nDRExe4h6XKA4fZH6QCxmydMzRkNhCY8w1VZCiqscDPTm8rc41URCCjs3iHj71VubS0Y1G87z5ME5bKy_sRJQVe9ivFQ_B2Cf9d4ts4WPKMimrx5EBgexpzJKm9E1zjdhU40yQ-I8Efqg-JgAAZQuLzi_OBszym71pOjbvubARukZo27SrjVESLgTHr4a9iDeGhrrBFKhP-W5YA7JLvERb4anrIN-QBy098Rgv5RqVWUMSjM4szX5xhkc0tTXAxibruu8dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1372691bce.mp4?token=g5Mh68SRIGhpepgaCe3FmjqwGvq--i5-BDe6ljC3UAvImCgoc82FylWyqDiUnskekpLgXkgPhI_M409nDRExe4h6XKA4fZH6QCxmydMzRkNhCY8w1VZCiqscDPTm8rc41URCCjs3iHj71VubS0Y1G87z5ME5bKy_sRJQVe9ivFQ_B2Cf9d4ts4WPKMimrx5EBgexpzJKm9E1zjdhU40yQ-I8Efqg-JgAAZQuLzi_OBszym71pOjbvubARukZo27SrjVESLgTHr4a9iDeGhrrBFKhP-W5YA7JLvERb4anrIN-QBy098Rgv5RqVWUMSjM4szX5xhkc0tTXAxibruu8dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
گویا دیشب تندرو ها داشتن بر علیه تیم مذاکره‌کننده شعار«مذاکره با دشمن، خیانت است به میهن» میدادن که مهدی رسولی مداح حکومتی صداشون رو قطع میکنه و میگه بگید«حیدر،حیدر».
این حرکتش باعث واکنش تندرو ها توی فضای مجازی شده و گرفتن روش
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67730" target="_blank">📅 15:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67729">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fuj_s-S2Zq2NEhDQCZFo0mCzvpitLthwepVL67j3k7l6sPRv6dKUJTOL72YIjtAaOYDkEsH7uizzFdsE1fLqJJCd4e4yMpfUVqRLC4X4XqXppOk_qQ5G_8Ro3ZOc85YFiEmP3DHOFMH47FMlELSwkTWl6UB0PXRuUbykhx0d3PEVUNYAnGZKnYYB-w-E-1GWHkEAe1ay557Nv5rnHM1MciFIdz-dojHBhT_R8kxEOsnxGfD-bV6wYOq_NJawORspaUG1lua4m-DCI7ZsTb-ZRA1cGxmYNaEbDL3PQ9arzgHSavbC1uqUnRkv5SPpwZ8bOua4ZVjuL-Ot9WHNgkwVuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DMbA3-gpzB8dNsUjSi7HLJqbrlbIVLtFxI6ChdCSrj8gnY9RY0UzpRlfN7c8Xl2bK7xmlGCkFJlFy9SxyxILotSPIK-GPY8r3k38oeyi69r6fgGaHoIMn6MfJfUGSk_CvS_CT44MN0FxJh1UB2FPQWiQGMQUFLL_zB3A-5FHyHcEHqsFtY8TByoC0gbjMjkNtS86xCnqOrB0Q6c0NWUktbJNinQ8aN5wS0Toss4YN8_tOcATRyD2Wy8c8jh3-Er0ewY1qtwMAHjwzZruxZEha3G0U-66X5vBPj2Idkj52OVFVRjivEu5V9e0KQOAII5pw2nz80Md5EY5PbGusF5D7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با اعلام سازمان سنجش، رسما و شرعا امتحانات دانش آموزا، بدون هیچگونه تغییری و طبق برنامه، از ۲۱ تیر ماه آغاز میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67728" target="_blank">📅 14:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67727">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3590c95ce.mp4?token=s1ZLo74KyXI-_wimy2-CqkbZGNqjmKh8bTkqLxLm8jkFIJXM3BPiEENklJYPDduY40U7d9ifbngHFuKbn28fK_9qFTlPCzj08BbIV-aeh3YMB29Ldqv4mKIaSZB6koXde1D8z4K3vaDgLizr2Fl9oOo5T7usKRqSGjpKdKrDOx_RZSW4k7nMsbS5vcVt7nzWRvHtGHoauXYJeWtV9xyz0bxMks01BYBA-PgsdS77dXR0MWb-k28ITiVJ0uNobOcHEM4ev0W6wUktv3WWELEJuRNv6-NfCFNdNNofBfGGfUMQY8HdHSF9HvC0iMHJXFuGMfeItbdA4AEMpl2_MIj-Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3590c95ce.mp4?token=s1ZLo74KyXI-_wimy2-CqkbZGNqjmKh8bTkqLxLm8jkFIJXM3BPiEENklJYPDduY40U7d9ifbngHFuKbn28fK_9qFTlPCzj08BbIV-aeh3YMB29Ldqv4mKIaSZB6koXde1D8z4K3vaDgLizr2Fl9oOo5T7usKRqSGjpKdKrDOx_RZSW4k7nMsbS5vcVt7nzWRvHtGHoauXYJeWtV9xyz0bxMks01BYBA-PgsdS77dXR0MWb-k28ITiVJ0uNobOcHEM4ev0W6wUktv3WWELEJuRNv6-NfCFNdNNofBfGGfUMQY8HdHSF9HvC0iMHJXFuGMfeItbdA4AEMpl2_MIj-Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/diHFuasUFg8luqEI7LoV5QLhW1hZ343hpUmb1_MBCKKj8QmjfX-u-uGxIOzaSD5u_zvnZm96JE_gq_hjg5wp-vlp-nqEiOQraoso7PCIVpvNFJvuLEDp7KLMpRfaX-SQyOnT_Xfr1krHfQoIHl0CEqbZUND1nfclSHPeLvVEh0jjH6rPCv57GZj4LLyQihQSRIz-SPeRKxSoYhn0ierck6AiHh4shGrOB_LNpTdqWBfHbbNK2KFY63pqtMUkv80w5IO7xmqCrsD6CKn9SJi76dMl29rJlu6VwaVQDWTt9Re69r3qkT3FVqyKrrXKXgv9UuOQiTkQ9FjTv1NhwEkGWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
زیرنویس شبکه خبر:
آزمون‌های نهایی بدون تغییر و براساس برنامه ابلاغی از ۲۱ تیر آغاز می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/67726" target="_blank">📅 12:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67725">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/606bce162e.mp4?token=XqPllhRPixxctAtKtqWS9yy2ZnWWQvvRaww85qkGLxIGBEFiREEB4gPaZKBPIA14p-aBvrTs-LqLZWFI-YiTRKAusKEZlrCjq7xpXmxphsEEALY0Fg5lJjEecmv2yV8a5IICVhjFh3H1uni7KUA-o5R-aWG0owWFITLgmpeDizFHtwk92CxfQMmVrcc9iCbrP1bxgudVee3ufnhnFBRCskF24d0u0X605Rv5ift-i4J7awgAEzw5WQentAw__yRO_r6BPbknEoNJYozy9mlVjZ_O4llUNtA-yEn-Y5fgOJPdTHsTI9zCS2-98lX52A4UwSqaM6SnpldZlrI4MN-NuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/606bce162e.mp4?token=XqPllhRPixxctAtKtqWS9yy2ZnWWQvvRaww85qkGLxIGBEFiREEB4gPaZKBPIA14p-aBvrTs-LqLZWFI-YiTRKAusKEZlrCjq7xpXmxphsEEALY0Fg5lJjEecmv2yV8a5IICVhjFh3H1uni7KUA-o5R-aWG0owWFITLgmpeDizFHtwk92CxfQMmVrcc9iCbrP1bxgudVee3ufnhnFBRCskF24d0u0X605Rv5ift-i4J7awgAEzw5WQentAw__yRO_r6BPbknEoNJYozy9mlVjZ_O4llUNtA-yEn-Y5fgOJPdTHsTI9zCS2-98lX52A4UwSqaM6SnpldZlrI4MN-NuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آمادگی مجری‌ صداوسیما برای ترور ترامپ؛
نگوزی‌ داداش.
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/67725" target="_blank">📅 11:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67724">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
⁉️
تسنیم:
مراسم ترحیم امام مجاهد شهید از سوی رهبر معظم انقلاب اسلامی حضرت ‌آیت‌الله سید مجتبی خامنه‌ای جمعه ۱۹ تیر پس از نماز مغرب و عشاء در شبستان امام خمینی (ره) حرم حضرت معصومه (س) برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/67724" target="_blank">📅 10:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67723">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‼️
یه ویدیویی از دعوای دوتا خانواده تو شمال که به صورت گروهی با هم درگیر میشن و همدیگه رو تا سرحد مرگ میزنن وایرال شده؛
حالا فکر می‌کنید دعوا سر چی بود؟
گویا یه خانواده داشتن از خیابون رد می‌شدن و هم‌زمان یه نفر هم با سگش از همون مسیر رد می‌شده.
یکی از افراد اون خانواده که از سگ می‌ترسیده، به سگ طرف مقابل یه لگد می‌زنه، بعدش دعوا انقدر بالا می‌گیره که همه با هم می‌افتن تو رودخونه و اونجا هم به جون هم می‌افتن و به این صورت همو میگیرن زیر چک و لگد :
@News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/67723" target="_blank">📅 10:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67722">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/67721" target="_blank">📅 01:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67720">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/THPvVJRTTqNmebcErwAGbgFyzEs4MxqQugV2J9NWiNcf_cCYsELbFT6RuCAuouUmw9PysMd5LFKp6LEwGuNaPHJTbE7r0HZQyECnJtw7Fwd-N0VdB1cKFpgm-hxWv-xvbtP86ojHHb98yd8UTfc-i0GhMpayxuVt7jTqyMD5xghMMijcq8jTUjvP0zqk6GOBAxcqx_hHtHqpRVmHxRW5z-ezDg_lSd4qlGQe8GENfCPT2iDhLz8_tMzvWZ1vGlLwVsu7F82cro-tS8C_QsIl4AdwUbiUP3UY1TAkAHlra06hnsbjKwnjGVQ_B_9as78bXnTvfKhBdlv0PfnCWcdljg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtSQ5FrEninjsSFSR4IVTlQOZnlvXjQlkhFTlYWYt7g5edArnOg0EvrZWXsONd3Dxibp3MIEjQ5IJNPnVcwx9-4ezrxnBVICqpTlQBd5eN8OzltoEnL1Q-mdreKdvRkR71lvAzdIEl4ZLchS2udc0N3hlwoo3hep9Fl_HYNK2lffTCYJbWND6URUjfgPRyHHwtkbRSeT2Ecw8mnq5l78ormvzah047aW2ldcW9yZ89Jy1_Q-75ZJgsB9K9sTVH3Gx0AQLao0bkmzshU7lY_8GprA17Si079YY9zR98P9pWNT6TJbhvnerGZaLxYB6REf8RhgQ0owJU9rIcDS2Owbcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وال‌استریت ژورنال:
اسرائیل اخیراً اطلاعاتی را با ایالات متحده به اشتراک گذاشته است که نشان می‌دهد ایران در حال بررسی طرحی جدید برای ترور رئیس‌جمهور دونالد ترامپ، بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/67719" target="_blank">📅 01:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67718">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
صابرین نیوز:
سخنگوی انتظامی استانداری خراسان رضوی اعلام کرد که درگیری مسلحانه‌ای در منطقه "بلوار سرافراز" در شهر مشهد رخ داده است که در نتیجه آن، دو نفر جان خود را از دست دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/67718" target="_blank">📅 00:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67717">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‼️
خبرگزاری فارس:
41تا43میلیون نفر در تشییع جنازه علی خامنه‌ای حضور داشتن
😆
@News_Hut</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/news_hut/67717" target="_blank">📅 00:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67716">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‼️
در حمله به ایست بازرسی در مشهد دو پاسدار کشته شدند. افراد مسلح لباس نظامی به تن داشتن و بعد از زدن نیروهای امنیتی با موفقیت فرار کردن.  @News_Hut</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/news_hut/67716" target="_blank">📅 00:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67714">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uaMokSJ2agzFCGum_2O30zrKOB3ITGJl7Lb7pCnK_Xi9qj6RuIRohAbCF9soKdNzRUR8HSfw79nIiC-pMV9h-NzM0kWm0pzjJjnQmRN4KfXHWWlPhgp0Vky0AwcahBFKAh27rE565ckPwsYvrdzAn_djZehWJJhq5eGpBVCRmHiKfIytVxELMbiCCfFLwYuisHK892Ls3qrnXQGhTiax491MxEAGvc_PbFrcd3d9uDU-lQQVTQdRfu8ca3agBg2cBOFOb_eHGet2bsrDcY55lgZKPi1zPDapLVdVNA6BXSsw3W45AsJKV7ig2bILh5vrdD0i_k8Q4efI8VWkO9e4UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fF-aaqjN-wvpOacQ98fFEQYr3IZXmSkOawtAUYWF--pUS6m7Mf7JPwvst8ltn5f3weYkdMvsQbK9QeiL0lNYcbRk34FbOhKlsn2on7ZtzNBwuFk0m5AuoVkgcHNyUtt6ww0FGGPwwolPshFaEiIoddTQVaXFXFS8CXh05FoT9xr68COfwY0JkCTKPLD3JIlVmYcFYmVE7uCIdvoCz65VPDgCBTZXSU3NjzeSQ6vgF1xMH3IgtWX03EnWrSVizlUhgaJpjQtPoVUxvvPMirc0WrCVX5Y47abwUVMIvepd4D608VeWjMgEp9hpXTWr0E3KsoW68k3yByDQyXRArCV4wQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚠️
اولین تصاویر از حمله مسلحانه به ایست بازرسی اطراف حرم در حین مراسم علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/news_hut/67714" target="_blank">📅 00:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67713">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSD9ajnu05HVRAi18PLIEHzH6ngWYfGxCy_ybIT1zN9Kx1WpPnWLkk5okACSNkJTEMoFuzpVoRhpjaMdsUmsxIY2_FhDFzYEW4xzRo31zodOE2aauaHQsrstD5xEXIZv4c1_x-JGXL81ABL4GOm211L8Gsn_9V0Jkf9cpGNLrSVHsPZHfHQ4Ao1wn45XR_hJiaXtXecK0iCWcWpjN1Jm-f5hEpOknzXQRSGUWrezFBEpruNLgx2G0GV05fGkI03ZWF6P72Y4EexWNmUmPTHa0C1dKcQKVW3Vwzuw1E6fUSa-iaqZkMdRgTvh_muMP1dsGF4sdVOZsToYnPbRTgClmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حمله به ایست بازرسی در مشهد دو پاسدار کشته شدند.
افراد مسلح لباس نظامی به تن داشتن و بعد از زدن نیروهای امنیتی با موفقیت فرار کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/news_hut/67713" target="_blank">📅 00:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67712">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QEEYZnn6ZZ4J2HYRM3WLSiRO0BFM1hbWqcaxJnBoEV67RiWZBn5DCGWw0JfD8SLoJD-WuHYZGDSq7pUh_xXM74FhzSc-dQD88WIsWg-3jG6kAcUNsAccX3jz2_V8z1s797b6EndVMMhWQ7wD_cLr8ue6VZMDD00DO4FUJzVZgE-iVUlhAzKnJekpWclbHKlijlxZlx1dY7VR7hKOr1lrZUFkFgTqmLN0yBKns_c3lZEYf8YbN8DIzUlSUDc14KEdMQIG6NhMWQ6j6ldT3vNxaY04DyqlZzH-xNsjB5lyo2Uob9ge50FHT9p6605qU9_gbPglQ3BHP3ezplmmKh9chg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
محل تیراندازی در محدوده استقرار یک ایستگاه بسیج، واقع در ضلع جنوبی و خارج از محوطه اصلی حرم است.  @News_Hut</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/news_hut/67712" target="_blank">📅 00:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67711">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
محل تیراندازی در محدوده استقرار یک ایستگاه بسیج، واقع در ضلع جنوبی و خارج از محوطه اصلی حرم است.
@News_Hut</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/news_hut/67711" target="_blank">📅 00:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67710">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
❌
گزارش های تایید نشده از شنیده شدن صدای تیراندازی اطراف حرم امام رضا
@News_Hut</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/news_hut/67710" target="_blank">📅 00:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67709">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ce06a68b0.mp4?token=BmQGshCQGTqowoFot-6eUJaOtC7RF_xmQ5fVw-3oJxEtLibbtdTDqtvD6MWu79pv2hXun0MNAr0QggfuQj8QdxQ43BQSUfSiS4ObpBlheZHPMV9AdASBJdlPkcAgrzb5xVFJmfmqNEunYsVH1tnBJ5eV3pqvD3rDr7k3qylkxakS_JD8GwlGn6DN5owLsqHQzL6UOpCplngvpuIBMowzwZEls7aObq1TaRFsPpQj1UBjmybulzvmoaX_Zoic_YT8-zcLx4G5lzGalBJHEnDgzWWQwsVoFVklezWEC9u98C88yqhkS1fT3qKHmobg60P1_D5OlBf77pc3lvbAQjMiNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ce06a68b0.mp4?token=BmQGshCQGTqowoFot-6eUJaOtC7RF_xmQ5fVw-3oJxEtLibbtdTDqtvD6MWu79pv2hXun0MNAr0QggfuQj8QdxQ43BQSUfSiS4ObpBlheZHPMV9AdASBJdlPkcAgrzb5xVFJmfmqNEunYsVH1tnBJ5eV3pqvD3rDr7k3qylkxakS_JD8GwlGn6DN5owLsqHQzL6UOpCplngvpuIBMowzwZEls7aObq1TaRFsPpQj1UBjmybulzvmoaX_Zoic_YT8-zcLx4G5lzGalBJHEnDgzWWQwsVoFVklezWEC9u98C88yqhkS1fT3qKHmobg60P1_D5OlBf77pc3lvbAQjMiNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امشب تو مراسم تشییع تو مشهد؛
یه مرده داشت شعار میداد (به احتمال زیاد علیه توافق و سازشگرها) که یکی اومد بالاسرش و رسما دهنش رو بست!
@News_Hut</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/news_hut/67709" target="_blank">📅 23:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67707">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
خبرگزاری ایرنا:
یه پایگاه نظامی تو حومه شهر بوشهر مورد حمله قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/news_hut/67707" target="_blank">📅 23:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67706">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-Mx4xiGWOHPHt0Q56OWgQbipw_fpU7jDigN8WSKhnoBaniIltdknMesOhYdF7jEY8QG0RZRlhe1W9yXyFuhXi-amUlLeA3L0m9aqrNiy5LL6LXDZez4KwQYBzSkdGmldAgDwF2Mwx3GBr37qwJlsmnLz7nJIThP3nOylS200M57IPQAXcNgBL8PDi8CuRXu4lqFdRI10ue9KH1VBlnqoyWKUKu_OhheR-XUkkm9LS1cuXCcUVQDrxpIrBtY0ENQ9i4p2jx5163IUgKqNdPGoizpM9g44WZyq3I01rNv58HCRJ1QYNkwRlp9II2bbVtlBfh9L1c0GXcbaIfSCAk0zg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">خب دیگه بسه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/67705" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67704">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfPyd01fNHdudORXS5H2mOuUI9DLkMDb9r_5ItQ8HouMbqwlVOHtunk9wdBGT7_-XphBv3S7zDBEwU5I6e1yEDuVEScDClNT6YdEg6MV0ZpwEQnMiLTmCPkfRxwvsLCw1qOd7Ju0PaeKlPbAOuOuXyo3ZFGieL5LtbM8JzpaOhdtdVYK7RDMOajrlvzUGEVsNuTwU8JCGfKI0rpGirH3Sw9feMcPtLf9wCYjLVLm_b4h_frF0l5ABJjg--UtrzZIKKkYU_chZCdXmhTo8U0zk7h3K30zh96pv0KfKdHF5UHNkXP9bG72-7UNgPsnbWFFrGfmSMAoIsWb1y2k65F8sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به به بریم برا دعوا #hjAly‌</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/67704" target="_blank">📅 22:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67703">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oc5dcTllfjY8vUjGBIOk6LYf5js7vUfCVDF51756OyVYOZnZ0hpWgAkS1c8yjCes6mEkrBPN_7Wq2LzSvBHVxYP-F2Ok88O0B-CanOA3cHbOUQzIRNli2WjeFtmiJyrsrjTm9hwWfstHGZU3WcpJcrdti2nCnq3AQ4f0jxNtDQqNpPFB1oBEUF8a4SfGA8oPTiXA4f98mT6U5zo35FaXOJ-AKhrluzhtY9tZ-QcdpVav3JQLKbAS4vDm-DlpgSwh6AKIkuNw93Wb8eV7F4p6hmKAePtiihoQxrEuvMJWcoF3Y3Jk6VW3UGIrqVv9LduqprV1Q3733FiKMpPyRNQ1dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه عده هم هستن تو دایرکت فقط دنبال عقب افتاد امتحانا و کنکورن، بشینید درستونو بخونید دیگه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/67703" target="_blank">📅 22:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67702">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یه عده هم هستن تو دایرکت فقط دنبال عقب افتاد امتحانا و کنکورن، بشینید درستونو بخونید دیگه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/67702" target="_blank">📅 22:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67701">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
نایا: ممکنه حملات امشب کار کویت و بحرین باشه  @News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/67701" target="_blank">📅 22:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67700">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ارتش آمریکا اعلام کرد که حملات امشب به ایران از سوی سنتکام نیست  @News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/67700" target="_blank">📅 22:27 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

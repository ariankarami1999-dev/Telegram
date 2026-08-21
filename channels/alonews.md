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
<img src="https://cdn4.telesco.pe/file/V-IDURumeBKRfzRWD2XFEYpkC81_byU5ueuSUek1tmZ6q8Omaffbwo876uIg47sJedshZnnTZ3BSkELKc7iNMKaS8y4DA0b1-pUi8GamC7iEH4lN-bpVwpBfkunEwqN3fP5MW0wbLeHWBIZfDF0IS-pY-wiSDyjRtqXRclY65FS_hQMryS7b31KNg-qhlW0xNH_eVorMb3i7dx0CsyeePrK5eYi2ki4YpK2-xA4aCNg49P3vXkC7ZbeAI6ecd9SWG9WXNEb1XjPCMdO7qz1zpFMvY9--xco0OblMJDBicrRM2bFxRb0vTynrROP_81O7uAaQmCS2xdECmmdjOQwBQA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 990K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-30 11:58:21</div>
<hr>

<div class="tg-post" id="msg-142990">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
ستادکل نیروهای مسلح: پاسخ ایران به تهدیدات نوین ویرانگر و پشیمان‌ کننده خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/alonews/142990" target="_blank">📅 11:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142989">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jv-Ki4bGH9Hjq5T2foK9qyDpya5qZG0bzaND9ona5lYlQ6N90wR6DprzTtAsGe7onM1Mx71gu-hMawpQE3q9QyOxxVjhJjlIHSUUeLnz8v4Yo0TXHcpQR3WUzSEj-JqYnCZvMPMHCqhgryVujnDzQftiqKvSDxMOMidEuyNOYof0mO9WiXoULpO0ny0FyYgParUO731Rx56yegHaaU5jBfrll8x0775RDiFoy6_Al1zU6PC9RzPxB2WLpacG8Cg00Sp_Gg0wuGWDuEuFQGiRhi6I8UkavwhQC9vgR114tyDCMebj9KPyQ_R6H_fyrs38NN6_HR8v6kNvR_jYZbtaEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری پر بازدید
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/alonews/142989" target="_blank">📅 11:51 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142988">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
قاسم روانبخش، نماینده قم در مجلس:
قاسم روانبخش، نماینده قم، از مطرح شدن طرح خروج ایران از NPT در مجلس خبر داد و گفت این موضوع در حال پیگیری است.
🔴
او همچنین با اشاره به مسائل فرهنگی مدعی شد برخی جریان‌های غرب‌گرا، حجاب را به «دیوار برلین» تشبیه کرده‌اند و معتقدند با برداشتن آن، موانع دیگر نیز کنار می‌رود.
🔴
روانبخش تأکید کرد نمایندگان پیگیر موضوع حجاب هستند و از رئیس مجلس و رئیس‌جمهور خواسته‌اند نسبت به این مسئله توجه جدی داشته باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/alonews/142988" target="_blank">📅 11:47 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142987">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JkZdR2rFMzcioq3Qyn_AM7M0SfZK0LxyQ2YMmgECTVwM-5-R1ghSxhKQoGcgPWd0-RJ9cTF1l2BjVF2-i1mp529KuxmuBN52CEqSGyDoeLWlVA39owITdm4Bxo7unk4xewEMdlNAE2hz9bC998Abi8SV9lvoZ_G4a18_KUXHyfEx37yMSNOrJJcCKQsj4aPpWGM5Fokyx9ow3IS-Hd_EMmLxwm57AX_aWLjHSAax20KM6fDmhGl-EZ_QPii3_y12CwXeGSfZrbcsruJI2fF47e22V1-F9qxc5a9UnlTWo_T4u17_zm80dSSjADQ22AsiBUoCLJ-ilIEvoVre3CEkkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پالایشگاه نفت پرم روسیه در پی حملات اوکراین حال آتش‌سوزی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/142987" target="_blank">📅 11:42 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142986">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
رسانه آمریکایی سمافور به نقل از یک مقام آمریکایی و یک مقام کاخ سفید اعلام کرد: دولت آمریکا معتقد است مذاکرات ایران و عمان چند هفته پیش شکست خورده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/142986" target="_blank">📅 11:27 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142985">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‏
👈
منتشر شدن فيلمى در شبکه‌های اجتماعی که انتقال تجهیزات زرهی و لجستیکی ارتش ترکیه به سمت سوریه را نشان می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/142985" target="_blank">📅 11:16 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142984">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
وزارت امور خارجه لبنان: وزارتخانه قبلاً به سفیر ایران اطلاع داده بود که اعتمادنامه او پذیرفته نخواهد شد و ویزای ورود او تمدید نخواهد شد، زیرا او به عنوان فردی غیرقابل قبول (پرسونا نون گراتا) تلقی می‌شود.
🔴
مجوز اقامت سفیر ایران، محمد رضا شیبدانی، در بیروت قرار است در ۲۴ اوت ۲۰۲۶ منقضی شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/142984" target="_blank">📅 11:03 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142983">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3m7lkoyAIiwvD-SCzryadLI8slasqyz1z9ByD6-lmg6FbsarWtwLEa0RL3aj0dhN_Z2Wm92-mAn_fyABV2IYg5resFyoHutQRvTR8Wxg8w1mzwHEJ2OnxpWveK4-JOLW4hYEaT6NSaTB0QuoC-_7VUTm48vKrRKTxfv-ofgeIjw-a1zlJ3Sn7DQoWf0xMzbb6u1x7fze8D-sk-JLBAHrQ3lUrJCfq5jcGbZr2CWcVzzaNTeFg0KCsEI4sSXeXI3a1zEO2MOyahfvtxC-Zl6bVQdJgp4Br5GjCF2wisL4F5H40wI2lxNEbVFkUb3LMt0xgQqcm1Chg5kxeB7RSHhSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت بیت‌کوین از ۷۶۰۰۰ دلار عبور کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/142983" target="_blank">📅 10:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142982">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
الجزیره: چین احتمالاً واردات نفت ایران را با وجود خطر تحریم‌های ترامپ به صفر نمی‌رساند
🔴
پکن توانایی واکنش متقابل، از جمله محدود کردن صادرات عناصر خاکی کمیاب را دارد
🔴
در زنجیره انتقال نفت ایران به چین، هر بار که تحریم جدیدی اعلام می‌شود، طرف‌های درگیر معمولاً راهی برای دور زدن آن پیدا می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/142982" target="_blank">📅 10:48 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142981">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MZq4a25YUknI5r_S8wDimrrs5RZreCrar8LhGGBi-NeoIEjHPTlCjGJbFn1aFNRaWX-OVniLV4Lsh31foOGrcz5e3CNDBt57-hfJAHxDAH8qx0DCMyU4Y3sh6deV9vSa6umW08vx1Cs0012w-IBnqOOZTMSE-0YBWgRyD29VII7UQS9om6NmmQJkhHRM1IxK_cKol7C4sHqS4tUXu4ZXhTatTRc_MpbU8hq8VeR1HDpOU4rMNQ5R1Is5OHeg2D9EGTdlFCv67vaRCF2UyT_vfwjuP1V-fIcSbP_Gj2U_D4oKrjQi9KK_ga59O58vNknxoCpFAh9u3Jjr7OSSijUx7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پالایشگاه نفت پرم روسیه در حال آتش‌سوزی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/142981" target="_blank">📅 10:42 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142980">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpQUXo2ufvQeH-cmHf71KcqzIYHkxj5fTO2li1GvDpnc9taCm-zWY4p_mkMATr9CaH1t61ABG9i1YQdmXXyX6vv4LLEmN-lxg2qDvuDeZqDriUhDeVG9zdw4n_1sYt1kpAEyxSiF6FFuRwQSci0goQj0Lyhr2qSMiWsXRq4u-AFawH6Kxx92KRkXUbT1-YAtlDwKttPzvtwIKij6CS1BWvwE0cPqmCMO2yWslI0jNgku2wQUgMFC43SbqigNYe3k_qzB34KMhB59LzWGamjSNxoeID2N1Sl0P_ewaYbvghymWJwgAClicpHqideXCa-572Y9QNcWPdDJlUe_6IzQRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
معاون ارتباطات و اطلاع رسانی دفتر معاون اول رئیس جمهور: در پی انتشار ادعای ساختگی برخی کانال‌های غیررسمی مبنی بر «اظهارات دکتر عارف درباره بنزین ۸۰ هزار تومانی»، بدین‌وسیله این ادعا به‌طور کامل تکذیب می‌شود.
🔴
موضوع مدیریت مصرف سوخت در مرحله کارشناسی قرار دارد و هنوز هیچ رقم یا تصمیمی به جمع‌بندی نهایی نرسیده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/142980" target="_blank">📅 10:38 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142979">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/964b9429cd.mp4?token=diSZJP8QQXrKIwnu8KccAJGPVUe0seUjsHc4jKzkBicohBLreTiadNgfQSvOif8l98xj1vuqT810iE5AIHY0jihIM6pdfLnx4JEcZiYeeA0IgShcihjY9UJ9ifbZe6vJUOw3Obf1UqQMLDKVWJEtFIkbC41xd0iTryMBCpD0cVAuWl9icf2BvoyPuLcfvVRhSYQKOAfhvUXOLHPJh6F3sc93_AT9ecL2KtKHMq9L7vjw9JpTP7YSdYhcWUaz0V3A7_jpOINi59i6N3CoGRFQVbmDikYaOQZxsqA-3ctelzb3L0tJOb_sLNLu80M8j92v3dUjLjYE1kHki575_1TsDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/964b9429cd.mp4?token=diSZJP8QQXrKIwnu8KccAJGPVUe0seUjsHc4jKzkBicohBLreTiadNgfQSvOif8l98xj1vuqT810iE5AIHY0jihIM6pdfLnx4JEcZiYeeA0IgShcihjY9UJ9ifbZe6vJUOw3Obf1UqQMLDKVWJEtFIkbC41xd0iTryMBCpD0cVAuWl9icf2BvoyPuLcfvVRhSYQKOAfhvUXOLHPJh6F3sc93_AT9ecL2KtKHMq9L7vjw9JpTP7YSdYhcWUaz0V3A7_jpOINi59i6N3CoGRFQVbmDikYaOQZxsqA-3ctelzb3L0tJOb_sLNLu80M8j92v3dUjLjYE1kHki575_1TsDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خوش چشم، تحلیل گر صداوسیما: ۵ _۶ تا مین دریایی هوشمند ببریم و در خلیج فلوریدا بندازیم تا این تنگه استراتژیک آمریکا را ببندیم و آنها را به مصیبت بیندازیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/142979" target="_blank">📅 10:33 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142978">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTda8wbLafys7awb-sB7ldh05NmF0GA0ltmWbdO0--i2ThVdUw5FHliMTkuZvJpRJvQRkqlYsZYQO1pMQpZT3WrTWaLaOeT2bYOXPmjQN67_QhP59Sc_qkJJWIapIPwz1UV0Md2K52cUKiFP4-_l1UTP3e5g1DkzYlwove0zkXa2Vf6FDImoyekdG-lSnqsSkRUXsCNbrV8jelcaq4WiJUMllkA8Q_ate1q_TQC9ejLxZYd-UP912YR2Q8g0PQkmQxqhji12p08e3jCejML0uLEpRPaQCyneYFM4oOhhxHFqgucM-01YAWLbmUuF4AShwt5o9nrOz9ZDwILbxbBebg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
نیویورک تایمز: پشت تهدیدهای ترامپ درباره جنگ اقتصادی علیه ایران این پیام وجود دارد که او نمی‌خواهد دوباره وارد جنگ شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/142978" target="_blank">📅 10:27 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142977">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
کانال ۱۴ عبری: با وجود هشدار‌های  نتانیاهو، گزارش شده است که ترکیه، دسته‌ای دیگر از تجهیزات شامل ۲۰۰ خودرو، از جمله ۲۰ تانک، را به سوریه اعزام کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/142977" target="_blank">📅 10:23 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142976">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2oThw7S5KDlmAb67Eza9TFEbQSyhBxD_W3tH40oL9wod_Mw30reFZ5N0nUnkA1NkUGphWcbRB4jxqWw_sifyJx5ltorYgPgULc4pNEeSFnpkmfFTn6mQliT35v8-Hrc0uJbK5vNVXrMHRmFqFM6OGgamqH3scKaETWlXzUKHgpL0vRL1d_Zq3PgYB34w_VZnD2BLdK6HyAQnbQKNFMp877P4tokQ5yTD58LjB7855REaBC9Nzd8q-qRnj3uH9VxDrPuEmw96k4BAwt7wLU0ob1QdkH8iorsxTXxf0d-WSWRSHoIsXzWAF_U-pIIOuT5gLdOP8hjnBipJD9m8CFOQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: ما هر چقدر قدرت نظامی داشته باشیم ولی اگر مردم گرسنه باشند و گردش مالی و رشد اقتصادی نداشته باشیم، دوام نمی‌آوریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/142976" target="_blank">📅 10:19 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142973">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af775012e6.mp4?token=mk3fCBmFwNHjj4C6bOwyiz7DUIwZeI60UwREU1EMmHoiPT7F7nTjEHgzA7s0BrVeJpcikpde7R-b4s5DI3-3FDXBVSXj70JdVOd20pzyyXeUX1LHYcfwXYTVGz68dv-tUXKQOeB6TcEL1sZLdDcSH1ZOxDMwR11Y8SbeCB9DpgQc4W_S_izWVcBa8B8v-OEKy20NbokUUmvy1k0zus_AgeMFOOlQV-lsdX80boD4ojaTsaS7dyOZCm3TbbBH-T79kZbKIA3UjDcJZzj2St5NaiOPfZyQ4Gd7qDUmGAFWYxONdNDby17am2tP1WJ8wW26uGfREySHPW0qW_ax--d6UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af775012e6.mp4?token=mk3fCBmFwNHjj4C6bOwyiz7DUIwZeI60UwREU1EMmHoiPT7F7nTjEHgzA7s0BrVeJpcikpde7R-b4s5DI3-3FDXBVSXj70JdVOd20pzyyXeUX1LHYcfwXYTVGz68dv-tUXKQOeB6TcEL1sZLdDcSH1ZOxDMwR11Y8SbeCB9DpgQc4W_S_izWVcBa8B8v-OEKy20NbokUUmvy1k0zus_AgeMFOOlQV-lsdX80boD4ojaTsaS7dyOZCm3TbbBH-T79kZbKIA3UjDcJZzj2St5NaiOPfZyQ4Gd7qDUmGAFWYxONdNDby17am2tP1WJ8wW26uGfREySHPW0qW_ax--d6UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر تکمیلی از حملات هوایی اسرائیل که اوایل امشب ارتفاعات علی الطاهر و مناطق اطراف آن را در جنوب لبنان هدف قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/142973" target="_blank">📅 10:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142972">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c0312f82a.mp4?token=VRNfceuYU2Ko3arAuAbuDLVonRuRbq1XiaM0w2GjuaGKjLTkCRMopQIFwSbxRkUNI_L25PEIXaul9IsHJDOfCllJ6JWfEhch08gORKAzmrGK9rF-RdsfGfejPkZNMCi9AzosGkkJKNG2Mgc7JSa-7H9_VCbkJFvnVQviI6WU829dskHRRI1ubiN3ZYgoOMb7WKOIgfbBCu0nusaYIMuAeYzgK17sZbAIszTAsQUxgDQUXWU7Klop5rrJPFyIu-oLLGgx_r-Ghde-19OV_y_8ZRXaUDbbBlKrRD-w1Eh-pBn5YOjD2rdReZduHQYQu2LxC1n-9E-pJjg1h9Tl_2xubw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c0312f82a.mp4?token=VRNfceuYU2Ko3arAuAbuDLVonRuRbq1XiaM0w2GjuaGKjLTkCRMopQIFwSbxRkUNI_L25PEIXaul9IsHJDOfCllJ6JWfEhch08gORKAzmrGK9rF-RdsfGfejPkZNMCi9AzosGkkJKNG2Mgc7JSa-7H9_VCbkJFvnVQviI6WU829dskHRRI1ubiN3ZYgoOMb7WKOIgfbBCu0nusaYIMuAeYzgK17sZbAIszTAsQUxgDQUXWU7Klop5rrJPFyIu-oLLGgx_r-Ghde-19OV_y_8ZRXaUDbbBlKrRD-w1Eh-pBn5YOjD2rdReZduHQYQu2LxC1n-9E-pJjg1h9Tl_2xubw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شورای انتقالی یمن ویدیویی منتشر کرد که در آن ادعا می‌کند حمله‌ای به جلسه‌ای از رهبران حوثی (انصارالله) در استان حجه صورت گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/142972" target="_blank">📅 10:04 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142971">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
شرکت آمریکایی «پاوروس» قراردادی به ارزش حدود ۲۲.۳ میلیون دلار برای حفاظت از زیرساخت‌های نفت و گاز خاورمیانه در برابر حملات پهپادی امضا کرده است.
🔴
سامانه این شرکت تهدیدات پهپادی را شناسایی، ردیابی و طبقه‌بندی می‌کند و اطلاعات را به مرکز کنترل مشتری می‌فرستد تا اپراتورها تصویری یکپارچه از تحرکات هوایی منطقه داشته باشند.
🔴
نام مشتری و کشور محل اجرای این قرارداد اعلام نشده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/142971" target="_blank">📅 09:59 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142970">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
رویترز: در تهدید ترامپ علیه کسانی که به ایران کمک می‌کنند، حتی متحدان واشنگتن که در میانجیگری مذاکرات صلح نقش داشته‌اند هم ممکن است در این دایره قرار بگیرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/142970" target="_blank">📅 09:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142969">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
وال‌استریت‌ژورنال به نقل از منابع آگاه گزارش داد محدود کردن مبادلات با ایران از سوی امارات بخشی از برنامه‌ای از پیش طراحی‌شده برای افزایش فشار و بازدارندگی بوده است.
🔴
بر اساس این گزارش، ابوظبی قصد قطع کامل روابط با تهران را ندارد و رویکرد خود را بر تشدید تدریجی محدودیت‌ها قرار داده است.
🔴
این منابع می‌گویند امارات ابتدا محدودیت‌ های حمل‌ونقل کالا را افزایش خواهد داد و در صورت ادامه تنش‌ها، ممکن است اقدامات گسترده‌تری علیه نهادهای مرتبط با ایران در نظر بگیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/142969" target="_blank">📅 09:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142966">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64d76a6c81.mp4?token=kFc4S_0OKNJuUVHZ1cGgX0eQ91I02MaPm_gbqmdHT11yVNGVtjgDOoo14xMm7jkcmytAKj6PCrsq1h6sb6MIR0NoBgI3abjRMgUjpEVinQEyxTUwYDaXMNHJPU1SVrODUWSpEoAj6wEWXztnN5P2pDyxAkMU-YUI2XECU3zZnv9R_p15FTJBZvZ3mjzZu9pQ3vLg27k-MElnhO-a27dkibUOM6q5balE2eVEV_EPkpBTlCl1KQBI6DUwOBbNfvZggioikfmeASqrFSGr46sh_lezDX7pSINm9scpQhUKFyKm2Ts_yQIH9CBD1xEaTh8QOH5rmBwIUVC9Ljo-yKKBhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64d76a6c81.mp4?token=kFc4S_0OKNJuUVHZ1cGgX0eQ91I02MaPm_gbqmdHT11yVNGVtjgDOoo14xMm7jkcmytAKj6PCrsq1h6sb6MIR0NoBgI3abjRMgUjpEVinQEyxTUwYDaXMNHJPU1SVrODUWSpEoAj6wEWXztnN5P2pDyxAkMU-YUI2XECU3zZnv9R_p15FTJBZvZ3mjzZu9pQ3vLg27k-MElnhO-a27dkibUOM6q5balE2eVEV_EPkpBTlCl1KQBI6DUwOBbNfvZggioikfmeASqrFSGr46sh_lezDX7pSINm9scpQhUKFyKm2Ts_yQIH9CBD1xEaTh8QOH5rmBwIUVC9Ljo-yKKBhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات هوایی اسرائیل کفار رومان و ارتفاعات علی الطاهر در جنوب لبنان را هدف قرار می دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/142966" target="_blank">📅 09:52 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142965">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1g0J0IrLFI-JO4wR8MpAjSOzWZXfs5IfI2EaYXyskqL5prhCojCMT7wNzzaSPB_Pr8CTmnh0rdnuQVHQhsbZwUmW3VF8IMILYbx4g-wDMRQX8hvo36-LO8rIgyhvBXVum-YDpZ3baClJpvHWeTrnTY1BFD9r3NlwgyiOLosqy4bR-mQE5n_AeYi-56B9jyd7YIpAx8fJuewNsbIm-2FqD2xHrpRQDUBkptNLUWxzukczais8J2z9JASJw--5JyO4ThxATazJZLr2nv-Hri39SVXxAR73cBrdR31NakiR837MbOyELTLfu0xZTsEM6zYeDvC3oSHnqaoPUc0IqT4Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این قیمتا مال ۵۰ سال پیش نیست این منوی یک رستوران تو اکباتان تهران تو سال ۱۳۹۹ هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/142965" target="_blank">📅 09:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142964">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
وال‌استریت ژورنال: اقدامات امارات علیه ایران گام‌به‌گام خواهد بود
🔴
به گفته منابع آگاه، محدود کردن مبادلات با ایران از سوی امارات از پیش و در چارچوب تلاشی برای بازدارندگی در برابر حملات سپاه پاسداران به کشتی‌های این کشور برنامه‌ریزی شده بود.
🔴
مقام‌های اماراتی اقدامات اخیر را نه به‌عنوان قطع کامل روابط با تهران، بلکه به‌عنوان بخشی از یک روند تدریجی تشدید فشارها ارزیابی می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/142964" target="_blank">📅 09:32 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142963">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
«کپلر» اعلام کرد که طی روز گذشته تنها ۷ شناور از تنگه هرمز عبور کرده اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/142963" target="_blank">📅 09:26 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142962">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
اسپوتنیک: یک هواپیمای هشدار زودهنگام آمریکایی هنگام پرواز در نزدیکی خلیج فارس و تنگه هرمز، کد اضطراری ۷۷۰۰ را فعال کرده است.
🔴
بر اساس داده‌های پروازی، این هواپیما پس از اعلام وضعیت اضطراری ارتفاع خود را از بیش از ۶۷۰۰ متر به حدود ۵۴۰۰ متر کاهش داده و به سمت غرب تغییر مسیر داده است.
🔴
هم‌زمان سه هواپیمای سوخت‌رسان KC-46A آمریکایی نیز در محدوده تنگه هرمز و امارات در حال پرواز بوده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/142962" target="_blank">📅 09:22 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142961">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3mOGdCuwOvIMbgvgBqVF3zEwgDeZknCViTYqjwuUPQubw7mXm7tkwmLvZOGWUpedOE7TM0WikpHFjyNKaFquSMCVq_Pe0T_GAf3IZc8hZWp0e6CHy-sAoN6VFgW9nxIoEQgoAcCbq-VUIvracV2aihrX78ffqfmEGWNdr3vactO686hqf7JyhIzAA3KFx6NGkummDFR7mq-ouqZREZJGeO4LLR-vRfc085oRGvkyA1iRdcYM0eQtW_sOKXmmmkEqP9lcFqnjKTHfHZVR5vBgkmzTJy_JmYw_uC-UlT0bBVRPIy4CtImETX7RHjp8Ctyi6c4vhfOrnv0-0dQEjMU2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش آتلانتیک، اوکراین طرحی برای ارسال تا هزار پهپاد خودکار در هر شب به فرودگاه‌های مسکو بررسی کرده است.
🔴
این پهپادها با کمک هوش مصنوعی می‌توانستند بدون کنترل مستقیم انسان مسیر و اهداف خود را پیدا کنند.
🔴
هدف این طرح، ایجاد اختلال در پروازها و افزایش فشار بر روسیه برای مذاکره بود. این پروژه فعلاً متوقف شده، اما مقام‌های اوکراینی احتمال ازسرگیری آن را مطرح کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/142961" target="_blank">📅 09:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142960">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fbc460410.mp4?token=gopRPUl-lxFwPMTEuPGmw18_ZjSdetU-GyG-4t3wBH4WuW-wotPCMUrVK4Jj--2Le87IO5YFRnyE0b4eGtXkddKn3KbpO7PgdVe4n34Na2Ppp2Q7eb5FUDIa2cmLkRmqptnKd1rPeT6-6a_3jBgnw0mIjiXaBUVwzLdgeGh8p73d0DgsQzm_5qOoFGL_QU-MYn4HJuDl0HvAMqGkcu-hkxQv7w1zoG9HV0IxSoHrSsyiTX0GqE6QpKSnbhzkPwm-Z8rhrsSLi2xVH2CgVtor4qtng5UvkGsGb_3rTWbpodw1OCSxaNqFmfIscqMhxzalxzKpkn573YO69SpIhgt3DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fbc460410.mp4?token=gopRPUl-lxFwPMTEuPGmw18_ZjSdetU-GyG-4t3wBH4WuW-wotPCMUrVK4Jj--2Le87IO5YFRnyE0b4eGtXkddKn3KbpO7PgdVe4n34Na2Ppp2Q7eb5FUDIa2cmLkRmqptnKd1rPeT6-6a_3jBgnw0mIjiXaBUVwzLdgeGh8p73d0DgsQzm_5qOoFGL_QU-MYn4HJuDl0HvAMqGkcu-hkxQv7w1zoG9HV0IxSoHrSsyiTX0GqE6QpKSnbhzkPwm-Z8rhrsSLi2xVH2CgVtor4qtng5UvkGsGb_3rTWbpodw1OCSxaNqFmfIscqMhxzalxzKpkn573YO69SpIhgt3DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهرک‌نشینان اسرائیلی یک سنگ‌بری را در الخلیل به آتش کشیدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/142960" target="_blank">📅 08:57 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142959">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
از دقایقی پیش کنکور انسانی، ریاضی و فنی آغاز شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/142959" target="_blank">📅 08:51 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142958">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sg-W-T05oFGxgr4_caaxJp-UvDxcTQatXJLJFsyMn39HUYCvAuzhNym4zQRBFyWKtxw6bToJjVYNUgUb75EGev7Ld-Be4TpejkiBQARBMAOwNHAJHS7XWfJ4LG8u1U-KX5Hyk_2y5CjOT0ODgT56qVuEwPf-5tU2aJDF5_K_128BRvFwhuEuzG0r21skUrNK-0iQ8POXhmUotSucCLQ6jbnm4ftCOPt_m0Bzgw-2qvR3Rj3YzNQFQV9Qwd6ElI1wG1b_FY6zUYjQ2gByN-0oTyH8XrHrVpRWOUTTgoLUVi0QwSuS4vo5tZw61xfaWK4zlIZblMv3oITCF4m2PYNgPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چین از آمریکا و ایران خواست با مسئولیت‌ پذیری رفتار کنند و برای حل اختلافات از راه دیپلماسی استفاده کنند.
🔴
لین جیان، سخنگوی وزارت خارجه چین، تحریم‌ها و فشارهای آمریکا علیه ایران را مورد انتقاد قرار داد.
🔴
این واکنش پس از آن مطرح شد که دونالد ترامپ تهدید کرد کشورهایی را که از ایران حمایت می‌کنند، با تحریم‌های شدید روبه‌رو خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/142958" target="_blank">📅 08:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142957">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
روسیه: فقط تهران درباره مذاکره با آمریکا تصمیم می‌گیرد؛ ما بر هیچ‌کس فشاری وارد نمی‌کنیم، چه ایران باشد و چه هر کشور دیگری
🔴
آنها خودشان تصمیم می‌گیرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/142957" target="_blank">📅 08:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142956">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
یمن (حوثی ها): از عبور ۴۸ کشتی متعلق به عربستان در باب‌المندب جلوگیری کردیم؛ ۸ نفتکش را هم هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/142956" target="_blank">📅 08:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142955">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1263ed070e.mp4?token=SJRy5MOzPP2uCGjxxKRiTOGisB9rx6vgRBthdxo6ecyrET3awJuEYikJPYlgGuFRQFbYGhEpN6fWkLsZvE_F-zAlCnjGjDFI8k2OuNtis5f9Z7ehIoynNDAlX_VeZXQ3GOWB8ctTdd5eIdybOKWF-GIW2We0itBGsJ-fL05C7Dqsi4TeqiLRfQ4N0UMNCEIbcLKN_Ai9RR07i0jZ-nTxGDm2rF-BGDzm9HOa_TUtnyOtlElGO7dCBFRrfumBeS087wWrKYrAHC7EdnOPimb8kEGhb8pscLYq07XDFygG8pAeRxjSUHOo9fKLJetNEpHhNu8mXN_LoGiSHSz7bPthaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1263ed070e.mp4?token=SJRy5MOzPP2uCGjxxKRiTOGisB9rx6vgRBthdxo6ecyrET3awJuEYikJPYlgGuFRQFbYGhEpN6fWkLsZvE_F-zAlCnjGjDFI8k2OuNtis5f9Z7ehIoynNDAlX_VeZXQ3GOWB8ctTdd5eIdybOKWF-GIW2We0itBGsJ-fL05C7Dqsi4TeqiLRfQ4N0UMNCEIbcLKN_Ai9RR07i0jZ-nTxGDm2rF-BGDzm9HOa_TUtnyOtlElGO7dCBFRrfumBeS087wWrKYrAHC7EdnOPimb8kEGhb8pscLYq07XDFygG8pAeRxjSUHOo9fKLJetNEpHhNu8mXN_LoGiSHSz7bPthaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انتقال عمران‌خان، نخست‌وزیر سابق و زندانی پاکستان، برای درمان به یک بیمارستان خصوصی در اسلام‌آباد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/alonews/142955" target="_blank">📅 08:31 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142954">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
ترامپ: ایران در وضعیت بدی قرار دارد زیرا نرخ تورم به 300 درصد رسیده است و حقوق ارتش خود را نمی پردازند.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/142954" target="_blank">📅 02:27 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142953">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
ترامپ: ایران تعدادی موشک و پهپاد دارد اما توانایی ساخت آنها در مقایسه با 5 ماه پیش بسیار پایین است.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/142953" target="_blank">📅 02:23 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142952">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
ترامپ:
ما ایران را در بحث نظامی شکست دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/142952" target="_blank">📅 02:18 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142951">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
ترامپ:
هیچ‌کس نمی‌داند چه کسی ایران را رهبری می‌کند‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/142951" target="_blank">📅 02:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142950">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6a2752a41.mp4?token=s6EflDUM5Sr6jysbQ2kQBitE6bywTYXmFWTxAynTUeud6qIK6-gxyz-vWoLg6ALva0CS3zQ9JlsCk2iUBvpvErEy6icZbdBb137iEEM62a6GO7FEls35GXhyuvAule7t-ihGXrHAy-YT50RfPQC5vpBmRCKI9p4j14_eEr7TQWPrrUxY6MjS6C4AotwX1QUvktNTjzKDb6qXfMR-LvylGO2uoW8Z7f9I6JuGz6XQjrGLWINc5h8ApgzLR9b3tB4_axo-d78EYDueHs4UeW3io961KskcBvAL0fb8U0TtADOyInu2-0CnmEB-bd5m8JMuCCON8tC4OAsrPIoadufHtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6a2752a41.mp4?token=s6EflDUM5Sr6jysbQ2kQBitE6bywTYXmFWTxAynTUeud6qIK6-gxyz-vWoLg6ALva0CS3zQ9JlsCk2iUBvpvErEy6icZbdBb137iEEM62a6GO7FEls35GXhyuvAule7t-ihGXrHAy-YT50RfPQC5vpBmRCKI9p4j14_eEr7TQWPrrUxY6MjS6C4AotwX1QUvktNTjzKDb6qXfMR-LvylGO2uoW8Z7f9I6JuGz6XQjrGLWINc5h8ApgzLR9b3tB4_axo-d78EYDueHs4UeW3io961KskcBvAL0fb8U0TtADOyInu2-0CnmEB-bd5m8JMuCCON8tC4OAsrPIoadufHtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ درباره ایران:
ایران به کشورهای نیمه بی طرفی مانند عربستان سعودی، قطر، امارات، کویت و بحرین موشک شلیک کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/142950" target="_blank">📅 02:13 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142949">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
ترامپ: نیروی دریایی و هوایی ایران را حذف کردیم و توافق آسان نیست زیرا رهبری ایران را حذف کردیم‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/alonews/142949" target="_blank">📅 02:11 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142948">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
ترامپ: اگر ایران سلاح هسته‌ای داشت، از آن استفاده می‌کرد و اسرائیل و کل خاورمیانه را نابود می‌کرد.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/142948" target="_blank">📅 02:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142947">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0583bdb8b1.mp4?token=nHIIsBaGdSGyWLk8m-tn5G7tFXo5lmUp2H0LpAH_pBTvsucMRcyhahFKDBj2Am1KiXGBFQHeOR49ItmaijmXvgZvk3lKsFBay9TviAZxRTLT2THBlQLHA4UbezBACw3iHTYJKM9WG-vi0IXut7nFucPpFrSvX0p3u_CkqpcMvIPHReoPmezJC2Opas_PDi8530RjHdfKTa3sjtLNXzcZkoIEntNr9aVB6jHIUnhXUEVlrAcBs-L-aJtnkZTD0p3qy--xByvMysy3DOZ-QeWta3e7wbutNoYq_5Wg9YZx2iW2rfqRNCaf105nZCOErK21FQJkLiaWWaKEPweLxKdh1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0583bdb8b1.mp4?token=nHIIsBaGdSGyWLk8m-tn5G7tFXo5lmUp2H0LpAH_pBTvsucMRcyhahFKDBj2Am1KiXGBFQHeOR49ItmaijmXvgZvk3lKsFBay9TviAZxRTLT2THBlQLHA4UbezBACw3iHTYJKM9WG-vi0IXut7nFucPpFrSvX0p3u_CkqpcMvIPHReoPmezJC2Opas_PDi8530RjHdfKTa3sjtLNXzcZkoIEntNr9aVB6jHIUnhXUEVlrAcBs-L-aJtnkZTD0p3qy--xByvMysy3DOZ-QeWta3e7wbutNoYq_5Wg9YZx2iW2rfqRNCaf105nZCOErK21FQJkLiaWWaKEPweLxKdh1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اظهارات ترامپ درباره ایران:
ما هیچ انتخاب دیگری نداشتیم. من این کار را 100 بار دیگر هم تکرار می‌کردم. آن‌ها نباید به سلاح هسته‌ای دست پیدا کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/142947" target="_blank">📅 02:04 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142946">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
ترامپ: ایران هرگز سلاح هسته ای نخواهد داشت و ما کنترل تنگه هرمز را در اختیار داریم‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/142946" target="_blank">📅 01:59 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142944">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd25da48a8.mp4?token=ivwBcJrMvsS39PqqcgJQuC5FFWbiciw1hZ9dVUGdSOyNnAKZaFvtwPY7A89LMgFYWhNujJdUe-G-1sc9wik-svGBFd5fykTZ4mqhn_CiHHJa31yHTjtByFBdwo6_-VurdZdxX-LVmSkYxX2vHYNNto90_OoqX0kwOHg2YcNbCj-ZjjtKrmSv0IOcsIr6xwM1gekcxs1D1zsSlLQbSFkqhCpJ3lJuh9JiD57rlZPtECCgYjQnGWATk2sK7rqoVMLl6Jv52ZL39Y2jdmG1RyKdfEKZUxRjxECbVY5mIjFsi0IxL6UNCSNVDUYaHFWWzpxrJgTAgrYGZ8EN5gQeo5MOjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd25da48a8.mp4?token=ivwBcJrMvsS39PqqcgJQuC5FFWbiciw1hZ9dVUGdSOyNnAKZaFvtwPY7A89LMgFYWhNujJdUe-G-1sc9wik-svGBFd5fykTZ4mqhn_CiHHJa31yHTjtByFBdwo6_-VurdZdxX-LVmSkYxX2vHYNNto90_OoqX0kwOHg2YcNbCj-ZjjtKrmSv0IOcsIr6xwM1gekcxs1D1zsSlLQbSFkqhCpJ3lJuh9JiD57rlZPtECCgYjQnGWATk2sK7rqoVMLl6Jv52ZL39Y2jdmG1RyKdfEKZUxRjxECbVY5mIjFsi0IxL6UNCSNVDUYaHFWWzpxrJgTAgrYGZ8EN5gQeo5MOjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شلیل دونه‌ای ۴۱ هزارتومن
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/142944" target="_blank">📅 01:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142943">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
وزیر انرژی آمریکا: روزانه ۱۰الی۱۵ میلیون بشکه نفت از تنگه هرمز(مسیر جنوبی) عبور میکند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/142943" target="_blank">📅 01:07 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142942">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
واشنگتن پست به نقل از یک مقام دولت ترامپ:
ایران «کاملاً ورشکسته» است و ترامپ ابزارهای متعددی در اختیار دارد که می‌تواند طی هفته‌ها و ماه‌های آینده با شدت بیشتری از آن‌ها استفاده کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/142942" target="_blank">📅 00:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142941">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9190ed7396.mp4?token=kepKSY2QpM76JCAk1Der0cy9GuDGDT8MybPfDunk2c1MnlVKb6qvQ8ZGltp1hzXoOAnh-5Y8OZojzZY8MM7UBnxuQp1r_eCUVdmNiuzk_Re0LfbhBpMU9AShSHWMQkCBKODZnKYWJPX8LtUsQBlJGEhNdxpv0M1EE-n-8u2bw71VcR-abOWTkHsMSBz6V8v-_fPW-63dbdyuc5iExcTgCY7W9vl-SBCWnIJowanbNqCcVah2dsTLU4Mc2-etFV86rTux1-scsVoUJbmTyVreV1n52TRaLmoq2JAnKbEPxBMQvvRnQHw-winZvmxdQJQo8wZNqNSvBKNVp1CMW5aA-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9190ed7396.mp4?token=kepKSY2QpM76JCAk1Der0cy9GuDGDT8MybPfDunk2c1MnlVKb6qvQ8ZGltp1hzXoOAnh-5Y8OZojzZY8MM7UBnxuQp1r_eCUVdmNiuzk_Re0LfbhBpMU9AShSHWMQkCBKODZnKYWJPX8LtUsQBlJGEhNdxpv0M1EE-n-8u2bw71VcR-abOWTkHsMSBz6V8v-_fPW-63dbdyuc5iExcTgCY7W9vl-SBCWnIJowanbNqCcVah2dsTLU4Mc2-etFV86rTux1-scsVoUJbmTyVreV1n52TRaLmoq2JAnKbEPxBMQvvRnQHw-winZvmxdQJQo8wZNqNSvBKNVp1CMW5aA-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
‏قالیباف، ۱۰ تیر ۱۴۰۵:
‏اگر به سوئیس نمی‌رفتم ۱۲ میلیارد دلار ایران آزاد نمی‌شد.
🔴
‏همتی، ۲۹ مرداد ۱۴۰۵:
‏یک دلار هم از پول‌های بلوکه‌ شده ایران آزاد نشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/142941" target="_blank">📅 00:30 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142940">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RpmwN1hcdMKFpX01s_ZXLQj_sX4RB1SDzIBBB_qEPXf5bSFWE1MDQ3Ao6gBmgeL7JmB_tWCwFE5upP5A55cYdzo1rnT0TxejEPcT3GJh7HiKU1xfDw5ApZZNsXFZogczxKiE91te6VRRCx5zhRIzLZ5anX26Ceg2Bp685K5UdSfGegKXjeBqBn_r96q17goJekMroK1rQ1CnkUo3x6xWFtvmLxhgIexYkY2WkqSoo0D5sgxuySv_XgMR-7mDp9UddDemspQ98M-aRveZWMgsg7K1cKZeCRaFuv1e2UERC-zV1rHxj8bsDivJasqET9a8bHJ0iPAuR47HkaEDsuv1hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانال 14 اسرائیل: مجتبی خامنه‌ای «
ایزوله
» شده و سپاه کشور را اداره می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/142940" target="_blank">📅 00:19 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142939">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
نشریه موندو: همسر رونالدو بصورت پنهانی با یک نفر دیگر در ارتباط بوده
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/142939" target="_blank">📅 00:11 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142938">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFf_Sskt3JIH0Af3Mv4PxDqf8bCJlBOYjFCtJfysAHsVTMr6Gn2s4TBwYNlImDiCf5SEdAVPi72Pe283usfEjxsgDbcISljPDH7LAQ6uB_4Dr6EwfbV6XTh7xekuq9PKyE7Ppsz1vKQC3OINm2fNX3naHglN3_BYcarENSeiOa7Yr2pBMDUDPrdbyU5AXwBF56-Eu4QUI7fdkfcvCPtKITMgKfp9vX5xZM8maY89hnVrpWq67QFPQBzdi2VEQprRaOEdpUjaR1aQhZ8GuPKDrnHzDRAmzvVOl_Cv2hiB_YE6XBfNItSQ2hshkZK8tgaK2gP3ZXmuWs7_xOFUK7tPZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نشریه موندو: همسر رونالدو بصورت پنهانی با یک نفر دیگر در ارتباط بوده
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/142938" target="_blank">📅 00:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142937">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
الحدث: محمدباقر قالیباف از بغداد خواست تا به طور مخفی یا موقتا، سلاح های سنگین جمع آوری شده حشدالشعبی را به ایران متقل کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/142937" target="_blank">📅 23:59 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142935">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
واشنگتن‌پست: آمریکا در حال بازنگری حضور نظامی خود در خلیج فارس است
🔴
واشنگتن‌پست گزارش داده پنتاگون در حال بررسی کاهش تعداد نیروهای آمریکایی در کشورهای خلیج فارس پس از جنگ ایران است.
🔴
بر اساس این گزارش، آسیب‌دیدن برخی پایگاه‌های نظامی آمریکا در منطقه فرصتی برای بازنگری در آرایش نظامی واشنگتن ایجاد کرده و ممکن است تأسیسات تخریب‌شده به وضعیت قبل از درگیری بازنگردند.
🔴
یک ارزیابی اولیه در وزارت دفاع آمریکا در حال بررسی این موضوع است که آیا بازسازی کامل پایگاه‌های آسیب‌دیده ضرورت دارد یا نه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/142935" target="_blank">📅 23:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142934">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
سنتکام: یک فروند هواپیمای سوخت‌رسان KC-135 Stratotanker نیروی هوایی آمریکا، هنگام پرواز بر فراز خاورمیانه، به جنگنده‌های F-16 و یک فروند هواپیمای سوخت‌رسان KC-46 Pegasus سوخت‌رسانی هوایی انجام داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/142934" target="_blank">📅 23:51 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142933">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37134f889c.mp4?token=NNuHNmMsse0s6-rf02_hhNgfv9u_Wxv6AlnwoUdmwoRFYJLeWh1o6nhKHqmwT2z7B8bYEAUCXAgtQRuMNZqE48MDSHCR0Ih245iajDbw9DI3A5kiwG5QbjQeRB_Fwiw5vIw86YsaAVWttsuobEkPZcqg98Ik1zJw9H5bTW6YCoCl2RD7QmDMY9wcQ0ar-VkQ5a0r2W5WCpf3VoztF2Y1EJI-8buJbh1eUtA2-XLRp_4U5F8lloTDuFmO0k8u8QIDfk48HbJ-bOKHPHe9aX1mULRLPR5JOuLVOZvv4ocatsd2RUsehylcb8EYYMe7bWHf28mrc2VIGz14EZWUUhEmjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37134f889c.mp4?token=NNuHNmMsse0s6-rf02_hhNgfv9u_Wxv6AlnwoUdmwoRFYJLeWh1o6nhKHqmwT2z7B8bYEAUCXAgtQRuMNZqE48MDSHCR0Ih245iajDbw9DI3A5kiwG5QbjQeRB_Fwiw5vIw86YsaAVWttsuobEkPZcqg98Ik1zJw9H5bTW6YCoCl2RD7QmDMY9wcQ0ar-VkQ5a0r2W5WCpf3VoztF2Y1EJI-8buJbh1eUtA2-XLRp_4U5F8lloTDuFmO0k8u8QIDfk48HbJ-bOKHPHe9aX1mULRLPR5JOuLVOZvv4ocatsd2RUsehylcb8EYYMe7bWHf28mrc2VIGz14EZWUUhEmjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ملانیا ترامپ: شنیدم که دلتان برایم تنگ شده بود. این منم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/142933" target="_blank">📅 23:47 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142932">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7078093477.mp4?token=NDq_kRqAx_a1Y9U87T6WwRZ1YryakHA0q9mrOhzMMxKGhkZDVPaUcw7z5Q4esl_Xq0MoJTT9N_O0vxjbnp_zA9xubTpoaUEHcNc-0S-67lGUEo5IQ6kdNuEDWRVlZuXQX5Me19VTekEhIfpSsApzQXIlrbNqp6yxD2X-etFoUx5wnD9Lf_XVTVWVTDGQgobuPE29_JvW1HebDTQ866HxZXLFdAr6bQV4AHevkSfREzusa787xh23xaPwhf972jwX9h5hfcTk5MDCBL4VLbTfQhg-q1WNDtriy3ayhq_hb51p8wUzqtEcLJV6yjDlYTTld-mAXIx4vDNlRzx0EcETWzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7078093477.mp4?token=NDq_kRqAx_a1Y9U87T6WwRZ1YryakHA0q9mrOhzMMxKGhkZDVPaUcw7z5Q4esl_Xq0MoJTT9N_O0vxjbnp_zA9xubTpoaUEHcNc-0S-67lGUEo5IQ6kdNuEDWRVlZuXQX5Me19VTekEhIfpSsApzQXIlrbNqp6yxD2X-etFoUx5wnD9Lf_XVTVWVTDGQgobuPE29_JvW1HebDTQ866HxZXLFdAr6bQV4AHevkSfREzusa787xh23xaPwhf972jwX9h5hfcTk5MDCBL4VLbTfQhg-q1WNDtriy3ayhq_hb51p8wUzqtEcLJV6yjDlYTTld-mAXIx4vDNlRzx0EcETWzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دکتر مصطفی مهرآئین:جمهوری اسلامی برای اینکه بمونه، کشور و تاریخ و دین رو نابود کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/142932" target="_blank">📅 23:44 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142931">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9209031f2e.mp4?token=PJRyRNXrNEikIMCkEx6zorgrw-kAla4UHSIama3L0LO6S4wuFpu_MsmOmYCLgB_dNR2r4cHnONdVfr0yRkfS2pujRwebDQg-VqdlWN3sh-XinALBQXierWoNfulOksE40G02fnOpK2l-PdnefuchMPG5xLuUm5lvBjw6d9sXn7yX3jEXuOg-bbrThQNWGHKI-NH0zN6Z4fteYEhFyRR5yjTjjgInGyrsC8Rek2QF67AHIebPMKcdkZN1_CiXgb4NgpllxuNhTh9eomghnXYUrjj28rDYx8GF54x3DM6e52aXvsbGwyXPcrRAJMRMTke_eYYvEvwqztNfzNgl_C77Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9209031f2e.mp4?token=PJRyRNXrNEikIMCkEx6zorgrw-kAla4UHSIama3L0LO6S4wuFpu_MsmOmYCLgB_dNR2r4cHnONdVfr0yRkfS2pujRwebDQg-VqdlWN3sh-XinALBQXierWoNfulOksE40G02fnOpK2l-PdnefuchMPG5xLuUm5lvBjw6d9sXn7yX3jEXuOg-bbrThQNWGHKI-NH0zN6Z4fteYEhFyRR5yjTjjgInGyrsC8Rek2QF67AHIebPMKcdkZN1_CiXgb4NgpllxuNhTh9eomghnXYUrjj28rDYx8GF54x3DM6e52aXvsbGwyXPcrRAJMRMTke_eYYvEvwqztNfzNgl_C77Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرمانده سابق نیروهای ویژه ترکیه، زکای آکساکالی: اسرائیل نمی‌تواند با ما رقابت کند.
🔴
ما مانند سایر کشورها نیستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/142931" target="_blank">📅 23:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142930">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7390372dac.mp4?token=ubYIyAWuBQlaBjg4_LTaBJspJ14phOnOtYjPD4LrH6GIJejwNBHxkS9LsJFnhFWzdr0Iiu66MHPLJ_jhjsVfj00aKf_bd7p3mQAakJGNr4hvAxmYWp7WD2WdFzs6SdF4C8GfDhb81wlM7Z0aw3tfU-4eRLCuPg6IJA35n2R3M8RvwLvVDOxi9tbqtAwI11-tnYPBSFDs_M-_KBft4Vo2uZ7pvyFYH6FSxdkpCUugAVrCS7Nq8ruBzMnP1YHXs_4THhnVsHi7cG9ixRwUooW--9ZnESgI4UXKJx68Lapw7G5yuOYb9URB8W7dM3t6Ul9BvdqoNHG2mDEUDLfANnXyJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7390372dac.mp4?token=ubYIyAWuBQlaBjg4_LTaBJspJ14phOnOtYjPD4LrH6GIJejwNBHxkS9LsJFnhFWzdr0Iiu66MHPLJ_jhjsVfj00aKf_bd7p3mQAakJGNr4hvAxmYWp7WD2WdFzs6SdF4C8GfDhb81wlM7Z0aw3tfU-4eRLCuPg6IJA35n2R3M8RvwLvVDOxi9tbqtAwI11-tnYPBSFDs_M-_KBft4Vo2uZ7pvyFYH6FSxdkpCUugAVrCS7Nq8ruBzMnP1YHXs_4THhnVsHi7cG9ixRwUooW--9ZnESgI4UXKJx68Lapw7G5yuOYb9URB8W7dM3t6Ul9BvdqoNHG2mDEUDLfANnXyJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس درباره کشته‌شدن چارلی کرک
:
من میل به نپذیرفتن روایت رسمی را درک می‌کنم، اما اگر وارد مسیری از تئوری‌ها و گمانه‌زنی‌ها شوید که در نهایت شما را به حمله به
اریکا کرک
برساند، باید بگویم تنها کاری که می‌توانیم انجام دهیم این است که به غرایزمان و در عین حال به عقل و منطقمان اعتماد کنیم.
🔴
من اریکا را می‌شناسم. او انسان بسیار خوبی است و اکنون تلاش می‌کند دو فرزندی را بزرگ کند که به‌تازگی پدرشان را از دست داده‌اند. او واقعاً سزاوار حملاتی که علیه‌اش صورت گرفته نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/142930" target="_blank">📅 23:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142929">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7469eeed2.mp4?token=oBM0gdfCVRsHSquZ42gN-hrPH5tVNvC1ZyYa6zVbgMzjOMzr9WDvXmg5TSwNG1FLDPOLIaEL_5LRx7zrHURqoktG5YlxWbCi8fg48GHd3BOAmajxkqyX29B6GCaDTr9oiOYOk5UI_WXXmWF7kiaW-qrGyKop0rRyzRDpCahC-x4wnVU85-5uE11YslKekpHIww-TcdBGcUNaJ4PATHTeBfsoTiJwzv5NEkBXt1sJCYq-__XclXrey8SQtei1ZTq9to0p7xq5b02UBbeqh1z5bS-BU_e6yhWUKtxFXMpX6yn5nfgJHWgIZrQpUoGCId8Ifq9oQfIBa7rVe0Cy42rwOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7469eeed2.mp4?token=oBM0gdfCVRsHSquZ42gN-hrPH5tVNvC1ZyYa6zVbgMzjOMzr9WDvXmg5TSwNG1FLDPOLIaEL_5LRx7zrHURqoktG5YlxWbCi8fg48GHd3BOAmajxkqyX29B6GCaDTr9oiOYOk5UI_WXXmWF7kiaW-qrGyKop0rRyzRDpCahC-x4wnVU85-5uE11YslKekpHIww-TcdBGcUNaJ4PATHTeBfsoTiJwzv5NEkBXt1sJCYq-__XclXrey8SQtei1ZTq9to0p7xq5b02UBbeqh1z5bS-BU_e6yhWUKtxFXMpX6yn5nfgJHWgIZrQpUoGCId8Ifq9oQfIBa7rVe0Cy42rwOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس درباره ایران
:
باید به نقطه آغاز برگردیم. رئیس‌ جمهور گفت ایران نمی‌تواند سلاح هسته‌ای داشته باشد.
🔴
تأسیسات هسته‌ای آن‌ها نابود شده، اما سؤال این است:
آیا تلاش می‌کنند آن‌ها را بازسازی کنند؟
🔴
بنابراین، اساساً کاری که ما می‌خواهیم انجام دهیم، ایجاد یک واقعیت جدید در میدان است؛ به‌ گونه‌ای که نه‌تنها بتوانیم با اطمینان بگوییم تأسیسات آن‌ها نابود شده، بلکه بتوانیم با اطمینان بگوییم هرگز برای بازسازی آن‌ها تلاش نخواهند کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/142929" target="_blank">📅 23:24 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142928">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb2a22dac6.mp4?token=CkfP-m6wRJwsks_bL5VP3iMmVyEbKbdDuopUztrs_UxCWsZBk9n9VpgItqzG9_pad6qz_eIPrLkMrG2_-lw0yL-64SecvaFzuvlfSuhC0yjvr8I2Qhj_FPHo5wAPZLg2d332GfudxQINRN9C_5vwIqZsxm4T9o0JQptnvzrTv5P_Z2CzxlX3DprfT8ZYeTpB491OKkCaOCRbc4yihggGx6Q3E2NrCb2VBjwxocdjQbqBiiD89D1yXo0HDoj5KUQXVXFAF7Jm0BwXFG11oAD1e1Mh9Me-P5HasfRyuvhcDFeBdWWogIIofo39wvGKeaaZzr7wH9CiP_V_6JkglhVd8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb2a22dac6.mp4?token=CkfP-m6wRJwsks_bL5VP3iMmVyEbKbdDuopUztrs_UxCWsZBk9n9VpgItqzG9_pad6qz_eIPrLkMrG2_-lw0yL-64SecvaFzuvlfSuhC0yjvr8I2Qhj_FPHo5wAPZLg2d332GfudxQINRN9C_5vwIqZsxm4T9o0JQptnvzrTv5P_Z2CzxlX3DprfT8ZYeTpB491OKkCaOCRbc4yihggGx6Q3E2NrCb2VBjwxocdjQbqBiiD89D1yXo0HDoj5KUQXVXFAF7Jm0BwXFG11oAD1e1Mh9Me-P5HasfRyuvhcDFeBdWWogIIofo39wvGKeaaZzr7wH9CiP_V_6JkglhVd8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس درباره ایران
:
ما اکنون تا حدی در مرحله جدیدی قرار داریم که در آن مؤثرترین ابزاری که در اختیار داریم، فشار اقتصادی است که می‌توانیم بر آن‌ها وارد کنیم.
🔴
و این یک رقص ظریف است، زیرا ما فشار اقتصادی بر آن‌ها وارد می‌کنیم. آن‌ها نیز سعی خواهند کرد فشار اقتصادی بر ما وارد کنند.
🔴
اما آنچه در چند هفته گذشته صادق بوده است این است که آن‌ها فشار بسیار بیشتری نسبت به ما احساس کرده‌اند.
🔴
ما این روند را ادامه خواهیم داد، زیرا معتقدیم این بهترین راه است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/alonews/142928" target="_blank">📅 23:21 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142927">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0441732671.mp4?token=NmK1Wd4-3T8GMpwcqFtt_ofX7Myn-9bqaEdQjtTBAlk-5HpvNrc-qMzr9E6tVkRV7kdaGX1f79RbAwNI51NiZpFpHcXYPRDQI40YB-cKnl04U3v1zkgGHpqKjO0zPlD4XpXxSN-C3eVPvxY44ehPns7STQbbieXr0jKKfdRl7VIPnWWTQAQj4rhIc5PiJVFeqP1LteYddvac0Nlf7N_QOZVbtmgUP34iEgrBhOai1HHwo-fz1tonZY-uJv5IFNQH31vttqdSq0VsRbp4ng4PdbqXmEd4Tp2HJdGq-i5eXV_NUn9Yulhc3GPA683j7_TmUx-Soca5VYvSLGqP040HhHycz9WiVbJLm6PJ3T8HAAP0TNlYPTmr5JY1YrbQnuVnwUOtQmqOiYGjSRbwNO7kP2uzRV8EmwxAjtK4CH5qjlp3--PD53pO9HUU7qfjS092Rfvxks9NZW8kaOSamf9XRTjHV02LGTHIhN-LcvBkVfVg52H-gjmeR1SJNYJU0z8ER4SGG_QNNY-5OK_dVlZhHuXVVoAUARlsqciUHAJltt3Jt5viCoLwTGnBKB2i_Yv5ajw7yP2gmF-4_TUhWPPs10injfsPHgPX5MD4LcuEjhKe2iOPlDdd9YU3oWboaeo0FIdSe_f9KIMzs9PYNnhbgYygo6c84RHx7xopkXmoggw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0441732671.mp4?token=NmK1Wd4-3T8GMpwcqFtt_ofX7Myn-9bqaEdQjtTBAlk-5HpvNrc-qMzr9E6tVkRV7kdaGX1f79RbAwNI51NiZpFpHcXYPRDQI40YB-cKnl04U3v1zkgGHpqKjO0zPlD4XpXxSN-C3eVPvxY44ehPns7STQbbieXr0jKKfdRl7VIPnWWTQAQj4rhIc5PiJVFeqP1LteYddvac0Nlf7N_QOZVbtmgUP34iEgrBhOai1HHwo-fz1tonZY-uJv5IFNQH31vttqdSq0VsRbp4ng4PdbqXmEd4Tp2HJdGq-i5eXV_NUn9Yulhc3GPA683j7_TmUx-Soca5VYvSLGqP040HhHycz9WiVbJLm6PJ3T8HAAP0TNlYPTmr5JY1YrbQnuVnwUOtQmqOiYGjSRbwNO7kP2uzRV8EmwxAjtK4CH5qjlp3--PD53pO9HUU7qfjS092Rfvxks9NZW8kaOSamf9XRTjHV02LGTHIhN-LcvBkVfVg52H-gjmeR1SJNYJU0z8ER4SGG_QNNY-5OK_dVlZhHuXVVoAUARlsqciUHAJltt3Jt5viCoLwTGnBKB2i_Yv5ajw7yP2gmF-4_TUhWPPs10injfsPHgPX5MD4LcuEjhKe2iOPlDdd9YU3oWboaeo0FIdSe_f9KIMzs9PYNnhbgYygo6c84RHx7xopkXmoggw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس
: اگر بتوانیم مقدار کافی نفت و گاز را به بازار برسانیم تا برای برخی آمریکایی‌ها در قیمت بنزین و هزینه‌های انرژی کمی آسایش ایجاد شود، در همین حال، ایرانیان به دلیل شلیک به کشتی‌های تجاری تنبیه می‌شوند.
🔴
این کار فشار اقتصادی زیادی به آن‌ها وارد می‌کند و محاسبات آن‌ها را در مورد نوع توافق یا چیدمانی که می‌خواهند با ایالات متحده آمریکا داشته باشند، تغییر می‌دهد.
🔴
آیا می‌خواهند اقتصادشان برای همیشه خفه شود یا می‌خواهند رابطه بهتری با غرب داشته باشند؟
🔴
همیشه این گزینه‌ای بوده که رئیس‌جمهور به این افراد ارائه کرده است.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/142927" target="_blank">📅 23:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142926">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
تانکر ترکرز: دلیل اینکه دیگر در خارک شاهد بارگیری‌های زیادی نیستیم، این است که تولید نفت خام ایران در ماه‌های اخیر به سطحی کاهش یافته که فقط اندکی بالاتر از میزان مصرف/پالایش داخلی این کشور است. این یعنی ایران در حال حاضر فشار چندانی برای صادرات نفت ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/142926" target="_blank">📅 23:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142925">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c71e411fb.mp4?token=KgXqqLx6R3KcmvzfwtatNnN59I3G7OqZiBYeh2pFDwz3nXOLcZ8XuDhoq2CUV0Uxy5TbSvZj0rzx3Ejy8ljbzEajGXwf6azltzdrKpNlmUp2MnyuQtJEoL5fEdClVGilHj65nt8iGDSbcX6LlFzxtioV4XGkh6dSR_99hOTVaWVMk2PKsgyTWm8fI22_AHeHADEUuylXa5BrNJydAGQf6un2BeIsVFH4Uqmp-CeBRHhL8Rn5HaJWdlp0RjKjHNY6D0VIlA0hblfmBzL_wC2P7j7wX9Tz4kb2_AMAz3O8H0MPuiyeQd1sTOAeGFGd7pDVj0G4IzTg_CJNSJSuv6rZ0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c71e411fb.mp4?token=KgXqqLx6R3KcmvzfwtatNnN59I3G7OqZiBYeh2pFDwz3nXOLcZ8XuDhoq2CUV0Uxy5TbSvZj0rzx3Ejy8ljbzEajGXwf6azltzdrKpNlmUp2MnyuQtJEoL5fEdClVGilHj65nt8iGDSbcX6LlFzxtioV4XGkh6dSR_99hOTVaWVMk2PKsgyTWm8fI22_AHeHADEUuylXa5BrNJydAGQf6un2BeIsVFH4Uqmp-CeBRHhL8Rn5HaJWdlp0RjKjHNY6D0VIlA0hblfmBzL_wC2P7j7wX9Tz4kb2_AMAz3O8H0MPuiyeQd1sTOAeGFGd7pDVj0G4IzTg_CJNSJSuv6rZ0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
سانحهٔ هوایی مرگبار در آمریکا
‏
🔴
برخورد بالگرد پلیس با یک هواپیمای کوچک در فرودگاهی در ایالت پنسیلوانیای آمریکا، یک کشته و ۲ زخمی برجای گذاشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/142925" target="_blank">📅 23:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142924">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‏
👈
شریعتی نماینده مجلس: نزدیک ۸۰ درصد قاچاق سوخت مربوط به گازوئیل است، نه بنزین
‏
🔴
رئیس ستاد مبارزه با قاچاق کالا اعلام کردند روزانه ۲۰ میلیون لیتر سوخت قاچاق می‌شود که ۸۰ درصد آن گازوئیل است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/alonews/142924" target="_blank">📅 23:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142923">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‏
👈
ونس: تنگه هرمز اصلی‌ترین اهرم فشاری است که تهران در اختیار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/alonews/142923" target="_blank">📅 23:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142922">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
به گزارش i24NEWS، بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در جلسه‌ای امنیتی با حضور رؤسای نهادهای دفاعی و اطلاعاتی، درباره سناریوها و تحولات احتمالی پیش‌رو گفت‌وگو خواهد کرد.
🔴
تمرکز ویژه این جلسه بر تحولات سوریه و افزایش تنش‌ها با ترکیه خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/alonews/142922" target="_blank">📅 23:05 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142921">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1be81d77a.mp4?token=ufJdUJPz9RzmUhS2w6MTvOWgrr0JewMrtKZ9E2BB6UvThQf5G4B3F90rSX-hLzy8RgYevpOpff1rDYDcc6yZTyk_jVKx1x3t2PB9iesn41YtBTuVgjll0m3tuJy2Pb3Ke_TPIf36pGsjjAZS-xpRsktaJ3D1r6GD_vBLblG5sO0dS3GgdrwTlZOmLtGzyzjEC1S6giYFZ4HM9IIElZeCfF53IQqn8DZwdwJqR9vTWtX_Oo6VaxFm157q5q4tPrDjbTx-kJrBCO3pVA_9HGcCW84Obi35Op3R8GLGGhy-_6G-mRmLJXFpZVUC3YyMFRy7cQTV2ppeDb42WYZjFJlIaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1be81d77a.mp4?token=ufJdUJPz9RzmUhS2w6MTvOWgrr0JewMrtKZ9E2BB6UvThQf5G4B3F90rSX-hLzy8RgYevpOpff1rDYDcc6yZTyk_jVKx1x3t2PB9iesn41YtBTuVgjll0m3tuJy2Pb3Ke_TPIf36pGsjjAZS-xpRsktaJ3D1r6GD_vBLblG5sO0dS3GgdrwTlZOmLtGzyzjEC1S6giYFZ4HM9IIElZeCfF53IQqn8DZwdwJqR9vTWtX_Oo6VaxFm157q5q4tPrDjbTx-kJrBCO3pVA_9HGcCW84Obi35Op3R8GLGGhy-_6G-mRmLJXFpZVUC3YyMFRy7cQTV2ppeDb42WYZjFJlIaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس، معاون رئیس‌جمهور آمریکا : «ما اکنون وارد مرحله جدیدی شده‌ایم که در آن، مؤثرترین ابزاری که در اختیار داریم، فشار اقتصادی است... ما به اعمال این فشار ادامه خواهیم داد، چون معتقدیم این بهترین راه برای دستیابی به هدف نهایی است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/142921" target="_blank">📅 22:54 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142920">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VS_OJL44NnyMxHiaLbAlGbJtA5VRhpBwHC9IBh4L5_LM4Z3xdslArnqPzeYvrfw3K2ki3xguXPE_dK4iOlZw83-9PMX9wo2_UMV7tDGlQAVRhXhdai2-zmFqOuIGL-ROLHnzchT7kM5kuKOcpn8VYdlxjRtvfpX5KU1vlZ1ELNtnI9w1L11LaN0vM6TPOulCan74AYFMO97ChQc8SlaJkv7kOkGawz6eRxuOSnOLSacSyLaT0bsqoTea07l84p2A9fi58vaYMKYP87Eg_G-KafzbCoksG0aA2ZnP3m31j9R8GUrIWXyfC4vA_4IYzA8jHSxy_sS9jkYF94KcuxhxNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ناو آبراهام لینکلن، روز پنجشنبه پس از استقرار ۹ ماهه سفر خود به سن‌دیگو آمریکا را آغاز کرد؛ این ناو که بیشتر از عملیات ایالات متحده علیه ایران پشتیبانی می‌کرد، اکنون در راه خانه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/alonews/142920" target="_blank">📅 22:51 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142919">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AS6K7QI14iFcrZYD59rka-CaLspYl4dom-jkRQnyihvLaizw6NVhIppPodNmY_w3JOvCY947WJiDtjw4w_NZxJY1TXODkwdgK9WcP_gO8cAljJlsk-dSE4FxaVRUcncck0MWiZv_LKLHRWVlO6CRY6cpy4F_XqOhJqIuavp_lvVxtP4UfMBss57lQe6WcWrGySzHLwVwX2QJphwVDfdJ0rla7EArYKdvVxWbNPA44cjUTvfK6GzdL7_yfQ29hjJ2qFnWRyUB63CYT4lsrJXBg5WDbJS4kkhA19MK-BFkquzx-DNiZVLMPtpSUK0jE1VqhAMr53WquNK5zPEZDW4JDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💍
گفته میشه که جورجینا تو مراسم عروسیش با کریستیانو رونالدو ، بیشتر از "55 میلیون دلار" جواهرات الماس به تن داشته
@AloSport</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/alonews/142919" target="_blank">📅 22:49 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142918">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
قیمت مسکن منفجر خواهد شد
⁉️
این تحلیل ترسناک رو ببینید
👇
https://t.me/+S8mMBRHkHmFiMTFk
https://t.me/+S8mMBRHkHmFiMTFk</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/alonews/142918" target="_blank">📅 22:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142917">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
یک زن به اتهام تلاش برای بمب‌گذاری در ساختمان کنگره ایالتی نیویورک، پیش از اجرای عملیات توسط FBI بازداشت شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/142917" target="_blank">📅 22:47 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142916">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af1609ea76.mp4?token=jWlOIevMv_jGaRYxHltEEDxkKq4D5Ampk-AeHnW6-r91th7DAeQg7fmzzv4420mJVIZ7_Xo_cEXyCAlhaWVvHECEWZwBX6Zz_r1tF1chZwR8ETohGhwkGcpjEMBuTjrvMe4P1EXtzoNRQl1R0Q61E1QiF-nWVkUgztwcHEBGGG7_dIxv0ACswZnR8LuPerBfYNvmuOcf-Blqphg-QoJxKPGDYPQNjqqdJw1eD_Ioo228eFYYG08xrdDYrZEdK5jXnywultf4kOn7JLo5ITDtwe_WQ3nfdMWU3Ds-gekKvIG-F5IcGBbXG_4kNUYNw3LxNOhtt1RWFBykm-clIm77zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af1609ea76.mp4?token=jWlOIevMv_jGaRYxHltEEDxkKq4D5Ampk-AeHnW6-r91th7DAeQg7fmzzv4420mJVIZ7_Xo_cEXyCAlhaWVvHECEWZwBX6Zz_r1tF1chZwR8ETohGhwkGcpjEMBuTjrvMe4P1EXtzoNRQl1R0Q61E1QiF-nWVkUgztwcHEBGGG7_dIxv0ACswZnR8LuPerBfYNvmuOcf-Blqphg-QoJxKPGDYPQNjqqdJw1eD_Ioo228eFYYG08xrdDYrZEdK5jXnywultf4kOn7JLo5ITDtwe_WQ3nfdMWU3Ds-gekKvIG-F5IcGBbXG_4kNUYNw3LxNOhtt1RWFBykm-clIm77zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
شریعتی، نمایندهٔ مجلس: ۶۹ میلیون ایرانی خودرو ندارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/142916" target="_blank">📅 22:44 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142915">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzHVYdZlDniooaLxepX9_kLnL7lzFVVOP_oOontoLMhbHmL36OMImfDva9Da7rqu6CpAoSUWDmDJRdKg67LbM_hq9_dy4N16Gxl-d9J8ScykbeUymzDniD-Nl5PiqIhE9SYF8DdSvMGRScMPUqXIw0f091Kpc-TFXc8MbBkMGqUkovaUXVYjv0TMQhyHmRnhy6NiITJHQf7nbEfdTRs_mk3WRryMM1q2QaXIK4PrWQ62t2AxDHJnHS09v245TbjTHBdwYz_1mXIxZVgmBLdorum1Fp9OCg1BwWVdPOPNsMXZLSbzK_f7nyxglAy0k0bWFOcn9KS2RR2Uat-xDBUG-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری فارس: در شبکهٔ نمایش خانگی با بازی «نون بیار کباب ببر» لمس نامحرم را عادی‌سازی کردند و امت معکوس حشری شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/alonews/142915" target="_blank">📅 22:41 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142914">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
گزارش‌ها از وقوع حادثه دریایی در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/142914" target="_blank">📅 22:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142913">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1269f75683.mp4?token=NaUpneuqZsCQAlO5duam09YqLhQcgpWr1n8ca4JGYtxmaVCnLopS8nkB3FIvFGIy5SUsahRdPLeOpTWGfQQqdi8fyQ12M35lI8zmQbJf1P03EFHSxNhobscodcJ_O62G_o7CSnuWEVOHDqhsuKqqLUxabnzoJt2VfeIzPf8CYDbo39nDZ0tJc54bL3NiUOh-incJB3VQbRRzoHqCRmTN19WdtM3R3kxvMZR1Pv29GuUVWbHL6WXwMF5h0ziln8Wj6YnznIJkS0S9Ez2UPv0PMjLody_wZMhH8_XPgiBcwvRRMJjn9HNxc9x7g4QSvIXAb6BjBVbcVqalJs0N9mSAPr6FExXAhXQkwFA4fC6OIWRoh1USwZeIyIvHE4ToNHy5fM5-ltV8_HFfZYEiJpGOzMYnjsRafApWbuh7x6ohOJiSTYSBL_RVlkSEaTWtS2fNVvsaXEs6cwktj4bgujvYQw2cUcXDfkT7vpUb2_su91kccsUG1AtDVehxcKTwobUFgWREYeyl_oLIZYrb0vqKVQwk6dC2CgwReXtJhploMVJjiaJorveICA9qUligH2YWDBgI4aCerQytztQQuPU-ifyQSqMk5rg4cGqs3fUFBrcwbS1Pfvx2QzPcyXzzT_aRwbGPos8i2dMJdb7alX_lPSGOfmvsg0q0RMosqVPPrmU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1269f75683.mp4?token=NaUpneuqZsCQAlO5duam09YqLhQcgpWr1n8ca4JGYtxmaVCnLopS8nkB3FIvFGIy5SUsahRdPLeOpTWGfQQqdi8fyQ12M35lI8zmQbJf1P03EFHSxNhobscodcJ_O62G_o7CSnuWEVOHDqhsuKqqLUxabnzoJt2VfeIzPf8CYDbo39nDZ0tJc54bL3NiUOh-incJB3VQbRRzoHqCRmTN19WdtM3R3kxvMZR1Pv29GuUVWbHL6WXwMF5h0ziln8Wj6YnznIJkS0S9Ez2UPv0PMjLody_wZMhH8_XPgiBcwvRRMJjn9HNxc9x7g4QSvIXAb6BjBVbcVqalJs0N9mSAPr6FExXAhXQkwFA4fC6OIWRoh1USwZeIyIvHE4ToNHy5fM5-ltV8_HFfZYEiJpGOzMYnjsRafApWbuh7x6ohOJiSTYSBL_RVlkSEaTWtS2fNVvsaXEs6cwktj4bgujvYQw2cUcXDfkT7vpUb2_su91kccsUG1AtDVehxcKTwobUFgWREYeyl_oLIZYrb0vqKVQwk6dC2CgwReXtJhploMVJjiaJorveICA9qUligH2YWDBgI4aCerQytztQQuPU-ifyQSqMk5rg4cGqs3fUFBrcwbS1Pfvx2QzPcyXzzT_aRwbGPos8i2dMJdb7alX_lPSGOfmvsg0q0RMosqVPPrmU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحنه‌هایی از منطقه آیاکوچو پرو هنگام وقوع زلزله.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/142913" target="_blank">📅 22:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142912">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
صحنه‌هایی از منطقه آیاکوچو پرو هنگام وقوع زلزله
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/alonews/142912" target="_blank">📅 22:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142911">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
به گزارش سازمان زمین‌شناسی ایالات متحده، زلزله‌ای به بزرگی ۶.۷ درجه اخیراً پرو را لرزاند.
🔴
مرکز زلزله در منطقه آیاکوچو قرار دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/142911" target="_blank">📅 22:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142910">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
جی‌دی ونس، معاون رئیس‌جمهور آمریکا:ما باید نفت بیشتری را از طریق تنگه هرمز عبور دهیم، زیرا این همان اهرم فشاری است که ایران در اختیار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/alonews/142910" target="_blank">📅 22:30 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142909">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_ch0lyzPIHtvM60ab3IK9mtmalh_47Ip3ZP9WEzadUyIdef0AsyeWiX7csSphj8MGGQ7vZHylAeE4A7-3WUZPUYKq7eUJ5fQiXsZxwkZBfA412XPGzH0j1-CnTZ9-QY43AX6Y7DXGMzcfI2_E84COVekcp2rTZ5brGw4f-wWjY7_4VvdfTLcctSgqctyGotsshufL4BSaULpTR9oG21lcSABlYp9mrILL5BpehqY9NF_eQaMbV83ZehbaVjBkUSOojlr404OgSh3ouKbfxJnbGpV_AsYnTkiSzcB7LInwT4h4raZaa2FPXVeExZ-CtmTaCeMRG09qxKbJUZCqn38w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خانوارهای ایرانی‌ چند خودرو دارند؟
‏
🔴
️۳۴.۵ میلیون ایرانی خودرو ندارند، ۴۰ میلیون ایرانی یک خودرو و ۱۴ هزار ایرانی ۱۰ خودرو و بیشتر دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/142909" target="_blank">📅 22:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142908">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
الجزیره: قیمت نفت پس از تهدید آمریکا به اعمال تحریم علیه ایران افزایش یافت
🔴
بهای نفت برنت با ۲ دلار و ۲۰ سنت معادل ۲.۴ درصد افزایش، در ساعت ۱۵:۳۶ به وقت گرینویچ به  دلار در هر بشکه رسید. نفت خام وست‌تگزاس اینترمدیت (WTI) آمریکا برای تحویل سپتامبر نیز با ۲ دلار و ۳۳ سنت افزایش، به  دلار در هر بشکه رسید.
🔴
هر دو شاخص به بالاترین سطح خود از ۲۴ ژوئیه رسیدند و برای پنجمین جلسه معاملاتی پیاپی افزایش قیمت را ثبت کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/alonews/142908" target="_blank">📅 22:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142907">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
حاجی بابایی نایب رئیس مجلس:
کشورهای حاشیهٔ خلیج فارس تو کشور خودشون نباید خط لوله بزنن برای انتقال نفت چونکه اینجوری خاصیت تنگه هرمز رو کم میکنن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/142907" target="_blank">📅 22:19 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142906">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
مظلوم عبدی فرمانده نیروهای دموکراتیک سوریه، ادغام نیروهای دموکراتیک سوریه و نیروهای آسایش در وزارتخانه‌های دفاع و کشور سوریه را تکمیل شده اعلام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/alonews/142906" target="_blank">📅 22:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142905">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
وزیر خارجه عمان: عبور ایمن از تنگه هرمز به امنیت و شکوفایی کل منطقه مرتبط است
🔴
وزیران خارجه عمان و ژاپن بر ضرورت تشدید تلاش‌های بین‌المللی برای تضمین آزادی کشتیرانی در تنگه هرمز مطابق با قوانین بین‌المللی تأکید کردند. وزیر خارجه عمان تأکید کرد که عبور ایمن از تنگه هرمز از امنیت و شکوفایی جدایی ناپذیر کل منطقه  است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/142905" target="_blank">📅 22:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142904">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
زمین‌لرزه ۶.۶ ریشتری مرکز پرو را تکان داد
🔴
یک زمین‌لرزه شدید، بخش‌های مرکزی کشور پرو را لرزاند. لرزش‌های این زلزله در مناطق وسیعی از این کشور احساس شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/alonews/142904" target="_blank">📅 21:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142903">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4Q2wvyrS8vj4E68qLsVisoQhwtqIqsCwW95t66fCNnHqxULNr0ePRt0tyyhFsJuHUUQFHVfcsbSO54Hn4P23Yl4ZdOgnnzKAgYRZz3uy9G1m5qBU74WGbweIrKR4I1kWFGW4Gt9Y1IZkKtZ4W6b8IEJ2x5DYgPgv9G0g-ltXkz_dyNqnthzQLAUQS2M2WnbROZ1IcbphXdgWZPrmYUmPiXMNmNrBK-aHiwx5ICNqgjH1R3hDh_-gms-y5vJfwqRA-TbPGcApbmDNZZOgS7NW-83iiY5Jbi7HYtI-gPMRpUpdxsdrDe1vZc-w7usl-QYHYNPzRMUuo-toQrxjShvxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طارق صالح، معاون ریاست جمهوری یمن: تشدید تنش های اخیر از طرف حوثی ها مستقیما از سپاه پاسداران در ایران نشات می گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/142903" target="_blank">📅 21:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142902">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
گردان‌های "جنوب"، که با شورای سیاسی یمن (PLC) همسو هستند، تصاویری منتشر کردند که نشان می‌دهد تک‌تیراندازان آن‌ها در حال تمرین با استفاده از تصاویر برش‌خورده از عبدالمالک الحوثی، رهبر عالی‌مقام ایران، مجتبی خامنه‌ای، و سایر فرماندهان حوثی (أنصارالله) هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/142902" target="_blank">📅 21:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142901">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/777ea22755.mp4?token=uO5i15ctxcWOvJuNk8daAkkh0B6QTvmKs-10Z4J53DEbyryvmh-ZR5kjRi75kNqitWydxuX5-PcS0XlbpwXz7ZAN7kugsIJpQQo0BxKcYrAYmQPuf-uqxmtRu8q_VFcQp0dTKofFljTm6iB-5lxpmokh6vdBYsvxOrMAwv2WaN3MXTAA3zphhx_b9FPkWkDEMlpXHzCYZ_hrnsD-b92omMKkHD4nmmotpInPIBEn6yl04GChj6gU4GiCGpBPV1Gl-tOAGnJN4gArkTKakyj6OSFTs4wbJZbVvYRG6cpY-W3iLYinnZ1hAgdGXbMqMkQLLIkqJ8Yq7wsOGoA4JsEbeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/777ea22755.mp4?token=uO5i15ctxcWOvJuNk8daAkkh0B6QTvmKs-10Z4J53DEbyryvmh-ZR5kjRi75kNqitWydxuX5-PcS0XlbpwXz7ZAN7kugsIJpQQo0BxKcYrAYmQPuf-uqxmtRu8q_VFcQp0dTKofFljTm6iB-5lxpmokh6vdBYsvxOrMAwv2WaN3MXTAA3zphhx_b9FPkWkDEMlpXHzCYZ_hrnsD-b92omMKkHD4nmmotpInPIBEn6yl04GChj6gU4GiCGpBPV1Gl-tOAGnJN4gArkTKakyj6OSFTs4wbJZbVvYRG6cpY-W3iLYinnZ1hAgdGXbMqMkQLLIkqJ8Yq7wsOGoA4JsEbeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معاون رئیس‌جمهور، جِی.دی. ونس، اساساً دولت جو بایدن را مسئول افزایش بدهی ایالات متحده به ۴۰ تریلیون دلار می‌داند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/alonews/142901" target="_blank">📅 21:27 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142900">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
رئیس جمهور پزشکیان: شرایط ناشی از ناترازی‌ها به دلیل آسیب‌ های ناشی از جنگ، موجب افزایش فشار بر صنعت برق شد
🔴
سیاست دولت، استمرار تأمین برق صنایع و جلوگیری از توقف خطوط تولید است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/142900" target="_blank">📅 21:24 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142899">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cce6c887b.mp4?token=sOmAriS-T5Fq5B9X7lgTiZ38nUeaDXfCGZYovkmJF1Qr7lsJkRtGQeKrafNMqL4xGg0Xo1P4hX2qi1J4l6oaQQPJa-6QJSKNZ5Jxz_x24CvfJkZYMs2l1_BPOy4XlBiFNeXhlOYkWGWV7aD5orj2X0PYtFYG_JFnZcMWqQTjE2X6m5w2XwnoAjaBhBfgzN2n-TpFR63pQ5hBqm83DjCWQX-NqJ55Ua-85WGPXJIf6GTHz5mnPSCZ-wgXrvzddmR9Ok4dQJhjL8gP2fmAzi8HeMzAGAmYXfGArzKKfH-ebakm-ogR_wqws1rTihTY9F0k7S8eedomE_CRAMKinnce1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cce6c887b.mp4?token=sOmAriS-T5Fq5B9X7lgTiZ38nUeaDXfCGZYovkmJF1Qr7lsJkRtGQeKrafNMqL4xGg0Xo1P4hX2qi1J4l6oaQQPJa-6QJSKNZ5Jxz_x24CvfJkZYMs2l1_BPOy4XlBiFNeXhlOYkWGWV7aD5orj2X0PYtFYG_JFnZcMWqQTjE2X6m5w2XwnoAjaBhBfgzN2n-TpFR63pQ5hBqm83DjCWQX-NqJ55Ua-85WGPXJIf6GTHz5mnPSCZ-wgXrvzddmR9Ok4dQJhjL8gP2fmAzi8HeMzAGAmYXfGArzKKfH-ebakm-ogR_wqws1rTihTY9F0k7S8eedomE_CRAMKinnce1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واکنش وزیر خزانه داری آمریکا به نفت ۹۴ دلاری
🔴
بسنت: امروز شاهد افزایش ناگهانی قیمت نفت بودیم که من واقعاً دلیل آن را نمی‌فهمم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/alonews/142899" target="_blank">📅 21:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142898">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا لیست جدیدی از تحریم‌ها را علیه اشخاص و نهادهای مرتبط با جمهوری اسلامی ایران وضع کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/alonews/142898" target="_blank">📅 21:05 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142897">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
به گزارش بلومبرگ، شرکت فیدلیتی قصد دارد سه سال پس از راه‌اندازی، از واحد صندوق سرمایه‌گذاری کاملاً تحت مالکیت خود در چین خارج شود.
🔴
این تصمیم در شرایطی اتخاذ می‌شود که برخی شرکت‌های مالی جهانی در حال بازنگری در حضور خود در بازار چین و ارزیابی دوباره فرصت‌ها و ریسک‌های این کشور هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/alonews/142897" target="_blank">📅 21:01 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142896">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
پالایش ملی: با ۹۰ میلیون جمعیت، روزی ۱۵۳ میلیون لیتر مصرف بزنین داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/142896" target="_blank">📅 20:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142895">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-fhKGJzAzCx6DEVA5MttuKWVbM_rhVss_VpPuJxu0y0vvHV3TClyGibdzpAr8ASLUPG94TK2rqkfoOFnu0Pkk20EdhjUg4YL4OmuoRUekY0Fdq-dd0swObqe50xjVjT0c_6h6lwP2Z_BApmGVDI8KQeO2x4T_HSoJXPJJGKbWwcv0-DP6bonMb2y3-fl3m7xyPqFvkYJQU1o_3__dEx28fRkr0HxJKzrGSMp32RdVBfi8fLWSIaNZVA7gchp-aN1rsMjGDjVL3h4oUY74qxOie9ZDO3oFe7GvRgO9Ptyda1jmG4j_-gqkdOMOx94u440T7GVSxQUFlvkM1lMKcS-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار لبنانی: دو منبع به من گفتند که ایالات متحده امروز رسماً حزب‌الله را به عنوان وابسته به سپاه پاسداران انقلاب اسلامی ایران (IRGC) معرفی خواهد کرد و آن را یک سازمان ایرانی و نه لبنانی در نظر خواهد گرفت. انتظار می‌رود وزارت امور خارجه ایالات متحده امروز بیانیه‌ای صادر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/alonews/142895" target="_blank">📅 20:52 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142894">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
بیانیه مشترک بریتانیا، فرانسه، آلمان و ایتالیا: تصمیم اسرائیل برای برگزاری مناقصه‌های پروژه شهرک‌سازی E1 غیرقابل قبول است.
🔴
شهرک‌های اسرائیلی در کرانه باختری غیرقانونی هستند.
🔴
پروژه شهرک‌سازی E1 اسرائیل، راه‌حل دو کشوری را به خطر می‌اندازد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/alonews/142894" target="_blank">📅 20:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142893">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2-4DIaBqM8OG1zCE07-quLVWu57MDH10-H0oBK4_2nNIiH03W87FNHJofNP94wyIN8BhrmxbRG02xbuqO4aKgZX5YFJLSuzY8txuSU2q5_w8KR6kTxn1AMS8I-XyejFMakzRyUjoRhb62I7in1AzCX1EmxUELiZ0gVh_NAnxbxXT8RFmAxCqhxgT9ECRXQQK4Y7jfNgRVUSZZr-uxKKnCPUd0LCa-S5-KHmycOxj7B-Q8XtKGsVG_Kx73kPBkBTO-9UnxwxZSLRkm7jF1591YLLt0N4ZX5BCAvKHwhJzPv_BIWTFQFp0MPq02mXIWviyAFLZjrIDnasIBn83nz8FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلتفرم X زیر توییت رئیس پارلمان عراق با عنوانی جعلی برای خلیج فارس، یادآوری کرده که خلیج فارس درست است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/alonews/142893" target="_blank">📅 20:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142892">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه چین در واکنش به مطالب ایران ستیزانه رئیس جمهوری آمریکا گفت که تحریم و فشار به تنش‌های خاورمیانه پایان نمی‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/alonews/142892" target="_blank">📅 20:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142891">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
نخست‌وزیر عراق: دولت در مسیر قانونی کردن فعالیت‌های حشدالشعبی پیش می‌رود
🔴
جایگاه حشدالشعبی را به عنوان بخشی از پیکره نیروهای مسلح عراق، تثبیت خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/142891" target="_blank">📅 20:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142890">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
طبق داده‌های کپلر امروز چندین ابرنفتکش از آبراه جنوبی تنگه هرمز خارج شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/alonews/142890" target="_blank">📅 20:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142889">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LD1zZUXqMzhZ4gNGizk2gWwZAdwk14OvMzPtUKf6pSzG5wyQj82MsYrvMdkBbU4cNnWjdxtHcvJsiud9BvUxN4JocL6UPBo7thE0QNCzjn4orsGJ6La_Q2EpEgPFwfeN7yd27NenI98v_1TwjKJoCAHQhzrFA-IMn6t46VtRqCKg5eKiR1gGGwHEUT3VG9ICeU9MHry_Un6EFGBSXcLjP0wJKqnb1UKHv8PqTUgvxScxlQAF10Grbv4ltt11Au_j135DlkAMhJGO0aZm4OM5a0XlO2e4y9MH7T3ALUjCrS5xZ41Rjx8HiEUqLgBscs46IFhPHOroAPHpFb5s2KBWJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نورمن، خبرنگار وال استریت ژورنال: این اولین باری است که یک مقام ارشد دولت ترامپ پس از مدت‌ها خواستار تغییر نظام در ایران شد
🔴
اسکات بسنت در صحبت‌های امروز خود از تغییر نظام در ایران صحبت کرد. بازگشت به اهداف ۲۸ فوریه؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/alonews/142889" target="_blank">📅 20:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142888">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1f44565584.mp4?token=dAYpzlXdc4WyCxDK2Trq66u7dD1S2WNKQhfFKzZ4y8Mx4CPI2WkAVLw3wR9epcKskofF-Y1zv2fNneDBnjIrW-VYgIfNKO5eyUgFw_cD8QKHxC0ECpTL5wirYCSZXFh5vQDc22f4BBYxZ960PJt3LUssS6G5k4kVTaH05BysSYgYtVbFl7kw993AsXWc6chsAkPkP4KDnjYP8sNAuVmvEPdFv3nWLstKMSmm1o-nCF4CtmEC64L5onDKzKi2etA9tq0B1wB2DU3GyAYDleX1ETpRkmDvRLNJhQ2rlkKbnLrviQBPAJEJjJuUMzB7LuL-a4HgEaikQQdzzvI63i7aoA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1f44565584.mp4?token=dAYpzlXdc4WyCxDK2Trq66u7dD1S2WNKQhfFKzZ4y8Mx4CPI2WkAVLw3wR9epcKskofF-Y1zv2fNneDBnjIrW-VYgIfNKO5eyUgFw_cD8QKHxC0ECpTL5wirYCSZXFh5vQDc22f4BBYxZ960PJt3LUssS6G5k4kVTaH05BysSYgYtVbFl7kw993AsXWc6chsAkPkP4KDnjYP8sNAuVmvEPdFv3nWLstKMSmm1o-nCF4CtmEC64L5onDKzKi2etA9tq0B1wB2DU3GyAYDleX1ETpRkmDvRLNJhQ2rlkKbnLrviQBPAJEJjJuUMzB7LuL-a4HgEaikQQdzzvI63i7aoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیامدهای حمله بمباران با پهپاد به تپه تل الدبشه در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/142888" target="_blank">📅 20:17 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142887">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUPh3Q2WNIMLxf_ikWX6K6v-48UDlOjwubZEXLeODxt4XtPoB6Tn1dYTt2W1yOU-Y5_GonzgFugefSnH9Rgh8ZknQlcgN0GNN0_8g8ycjOaWrjo1oYZsK-bN5Q9HtEyD0VmIuyGwCaRo1dsN-4zpfogzZMKszGBHQr9ZQGS_RRbvFibBriqE0WAcgEovUyabHY_VjeK1NU6eEUBLqmJskN4EZPzgQkUAZWPtPgVD4dV81r4paPaAf7gOWau4xehYTPafWfZTPGc59Wxm3fY8eZVPjzi1y-2-tjUD2Ssx4PbnPc-FJ7BMtWUIUZw0k_sEpudzczX-Vrlraotng3lUUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر اقتصاد دولت رئیسی: تمام نشانه‌ها از آشوب و جنگ در شهریور و مهر حکایت دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/alonews/142887" target="_blank">📅 20:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142886">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
شلیک ارتش اسرائیل (IDF) در نزدیکی تپه علی الطاهر، هم‌زمان با رها کردن بمب توسط پهپاد بر تپه تل الدبشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/142886" target="_blank">📅 20:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142885">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOnZT_g4AprNz9pc1HSyWyVykwZR060MeiE3fdhovkdATna9TXdscA-IP171LluZbJyipBPdBYkhTlIVl51zTnqw5cKTRYyjlcrfOW1ONnKJ8RpOI1cDrOeh7Dq7j3hkYTkJWTdAcYmsgl8YySGQYSQruaH76EoPxxNciY3k4jHMpKVB4ZUODSESNKJOMcIpTbGNcm7_FQNv3ZxrrfPHe2gMWvsPHfl2xQC5239wOQVL6YlEN6qD11do4iKk8t-ls1H2rcP6KBusDc7q_H-PAlPKl5SHvUdqEynBARLF0d8xIJM7lc4AdF9E2biJcx9UNLS8_O-QtQvbW_mdSELEcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام : هواپیمای ترابری و چندمنظوره MV-22B Osprey متعلق به تفنگداران دریایی آمریکا، هنگام حرکت ناو آبی‌خاکی USS Boxer (LHD 4) در دریای عرب، از عرشه پروازی این ناو به پرواز درآمدند. این ناو همچنان به اجرای محاصره دریایی آمریکا علیه ایران ادامه می‌دهد.
🔴
تا ۲۰ اوت، نیروهای آمریکایی برای اطمینان از رعایت مقررات محاصره، ۶۷ فروند کشتی تجاری را تغییر مسیر داده، ۳ فروند را از کار انداخته و ۲ فروند را مورد بازرسی قرار داده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/alonews/142885" target="_blank">📅 20:12 · 29 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/muQNAevQnzCpyE6TwLUaFcwc77yvDswawaAvRoEzAL3HdtvFRZScQv13OhImWgsuf5x0mwx-UzPHflXzdcvU8nPHxIIWyMd2SG96HhcbUDIYKAedV1F1PpoAZd3Tm88smepCgW_NMPlxOo7KV1pjtDvQ9nZQbGB5ehnxS909mhc2Kq72TtqHLMnpt9CvMAPJLsAagcqsHsbpswbcjUZ9w0yRBZP98hn01ev_RVhD6fWZO5F2eYK7azai4gWO_TYkQtNRMh_yNta26tRTLNxNE0CeOr67MEFXL67RA8Av3R_QDN-UhhjZeJyhDh2Rcws2L6OGgmRPm54QcY4dWRAIwQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 937K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 18:55:36</div>
<hr>

<div class="tg-post" id="msg-136073">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7d3c1d446.mp4?token=Bm3G9Wrcg5peSFlDV83gRjM2VqfWNtayUt1RE5-Rm9xdwhO6Y_zbZ3k9iqjrW3hwMWpJKKyFqctOBoL_n2qdlasUXm-nY2k8XH3oxHZrh8jYhpS7kVNX3ExTRATmXApBpE2EUeT6c3Ih7t8h55AN-XzbYFngxZxeKB7FaexQKUMYYRVX9UT6oyEih1PqbDWB9NU9fpoKKP4SzjOahCabpKuS_VIG6yHFEHANFrRuUFyhuSSvmNK8txiPoKJ0YK7B4BwzpEJRFlYclDmPkub0XyfWUo-bQX29gc1fkzt6WAiuSpvepi6s0aIVuEHrHCJsWIc5d-R7yXq825j9VUkKYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7d3c1d446.mp4?token=Bm3G9Wrcg5peSFlDV83gRjM2VqfWNtayUt1RE5-Rm9xdwhO6Y_zbZ3k9iqjrW3hwMWpJKKyFqctOBoL_n2qdlasUXm-nY2k8XH3oxHZrh8jYhpS7kVNX3ExTRATmXApBpE2EUeT6c3Ih7t8h55AN-XzbYFngxZxeKB7FaexQKUMYYRVX9UT6oyEih1PqbDWB9NU9fpoKKP4SzjOahCabpKuS_VIG6yHFEHANFrRuUFyhuSSvmNK8txiPoKJ0YK7B4BwzpEJRFlYclDmPkub0XyfWUo-bQX29gc1fkzt6WAiuSpvepi6s0aIVuEHrHCJsWIc5d-R7yXq825j9VUkKYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سرمربی نایب‌قهرمان ده نفره جهان اینگونه با گریه از مردم کشورش عذرخواهی کرد، مثل بعضی‌ها از حذف در گروهی جام جهانی دستاورد نساخت و پیشنهاد مجسمه سازی نداد
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/alonews/136073" target="_blank">📅 18:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136072">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oxax57wR9ZEg67CZfFK3Q01o10GhCxc_GzDII_1llcoD_f7aVxgcEQVnLT_HZ3A4Y-WgR6n6qCd1pfxvXp95h29vetLslVHea17Y0vqnZJ0OspE1stp0LfWpIX8RMuTsNZDwEqfYquQUzRgL-cG4KvHbIFQoZa3QwDfMgodX68QNe1UTYYbwF6oDnYAjpVpRbJhHYDYkpLihhac78gN_R9PRPQJ1ymuG2GlgKm-ES87OZlJZ7-yAUt2RS7oqlco1tQ9gyt1zyYMp4-P7OViWp8dbUFekhjZOCL_-GTY0LdwF9cNpHpC-v8ZymKkHMKr_YFS8DWw5rlhQTwZZ8jvW3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حرکت هواپیمای عراقچی به سمت پاکستان!
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/136072" target="_blank">📅 18:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136071">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5o1cxNIKxf0lbLJQSX4fB9mXJWiszoH52UH_CLD6TntdBeZbken_OO-64R5PoDALCZb2QCC24QrleA6BP0XN1J77EWMuwrJrarFA2rQFfwLblEgYxqIX8IxwN960hgGiZ0nM4yDmnU0kIeQToyrWh533vZuMgbmuSstz6-y8KcbauXVIpH1AX3kYyCETl2KTuE7oeUf2h0adzoCSUhdSlh3oeqvrUttHscmOvi9wIkWWvqPpUXvq1AnAPkIjTLyqqQJBXaE3tfKaUIR9XbRNxKkmM9IGyVRKZngF3i7Ox5Ho0l_hpll7JiBEDEOOEOGLV5rhJQjToPPjPyKZ2I6aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ یه عکس دوتایی با لیندسی گراهام پست کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/136071" target="_blank">📅 18:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136070">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
یک مقام اسرائیلی به خبرگزاری Axios گفت که عقب‌نشینی نیروهای دفاعی اسرائیل از مناطق آزمایشی در جنوب لبنان از روز سه‌شنبه آغاز خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/136070" target="_blank">📅 18:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136069">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
فارس: دولت با ناترازی جدی بنزین روبه‌روست و گرفتن تصمیم دشوار اقتصادی طبیعی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/136069" target="_blank">📅 18:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136068">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
صدای انفجارهای مهیب در جزیره ستره بحرین شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/136068" target="_blank">📅 18:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136067">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OfRiXpaBLS4HEDlG6_1-XrqlAeAQ_6EA8eKLOX4lLOpdeA_BJb_lF8Ob20amEX-mlaQq4YV_WsW5hub6khwcqGkPF7e6cw5LJJg8nFx-uKlxYPWwnseGYCXSSK-mcxD8ec54fqjfusKl-YtR2iFJz-RkYwZyAjBxSH-1XkYpPScmUdA4pco88R944vnT1dMT7diFpAYWFPzpBKS8VSHvLXDuWLQRemFLbus015ixqno8yVVqp3AQz4ysKySB7jmWW_1rr3NX6PziTDDoYrgnLpHDjUxUMDhBpC0hqNdwh0JVa3R5BpBfV9t91zD2v64Yrmkd22uszM1Jx72_liicoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آسمون شیراز
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/136067" target="_blank">📅 18:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136066">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
العربیه: دوباره آژیرهای خطر در بحرین به صدا درآمدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/136066" target="_blank">📅 18:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136065">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3Ne83jjbgEJXnvJtP-dFdMlrY11dm6vVqdU1wbv9KTuxXtZ-zztOZbPYs_LNI8VP7HLZfA1u_AFah9-5DeOatOnaL10ogr_RT9Etg3U_kz52xWGXXM3tm6g9ceM9yQ3EejUcRoUwmc-ysDTNFEA_v1PjNs9zNM7y690B7iJIH6famLphFO9-r9JjMZoLRt3QBrH-sjDw4Bkg0Kx5dDP8Wa0ibJTfp0O2QKMB0YmaKDn-vV6sSTtOaazwVeszc1R9l52sMWvMzumnZ7CBoRTJx2z22PPyL4md17GcNbc81U4cnVzgoOcyliTGNN654AbXlfQzHgXQBbsr_lzYz7ZBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از رد موشک بالستیک شلیک شده در آسمان شیراز
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/136065" target="_blank">📅 18:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136064">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ویدیویی از ستون دودی که در شیراز نمایان شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/136064" target="_blank">📅 18:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136063">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
الحدث به نقل از منابع خبری:
وزیر کشور ایران فردا با فرمانده ارتش پاکستان در اسلام‌آباد دیدار می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/136063" target="_blank">📅 18:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136062">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJoH7pQm59-tuyJbXJ31OEUH70UqlQmUnZB4Q6nSOj64ycZisCrXqLSj_b2hlsWAdm7BhL8sSAM_UQVMSDxlAE7S6P2u_eOCTJqyyvlbABUcZVSPN9CyWLURBbJGRboAsCt4MkW7pfu69ERxhKSGxYflsSDugGxnoY6GW-Ar7HUh5CiCIsTBlxPY2pl9D8x2MVWrjfTEWMcwXhRXLmwLhuDp5lcSuE5MfumWZqDTB997PRJ7ToR_IGTSvrnsIm_ocd-xs4G2Jbj8VfLI8RXs45ukUpIa53K31qPQzOyqUtwYvNGEzHXkh_GzQFaKAKSGwxzqoDT5V-xUOph7Da3QXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / رویترز به نقل از سازمان عملیات تجارت دریایی بریتانیا: یک کشتی باری یونانی پس از اصابت یک پرتابه ناشناس در نزدیکی تنگه هرمز، آتش گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/136062" target="_blank">📅 18:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136061">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gj8auJqCFFi8Q51AITr-Zje6oEIl1VGuraXyBaNkjH7TrJTW6NJ1xf3hMl3EuowEHeWAjMbHOIH-us1_atRZEYGhgAvGztCHmp1VAqigDNj7V5oEtZmIL8AwoNNVrgJuI67OTyzY7yLh_PloFTJIVkt0qEEKHWeZe-c-H1Y72b4G7N2GbqVBMaOXNULHnCGdej2Cl-R4MfGFD6LDKNBWO-qbjyrO8w3IdclONxYR2Szu5gcu7kL6B7goMOx1Nj1F77-SUU5GRwfbyohkI8XfkEd9C0w7kFC6SHjVJ9w0atqBECiStTmpGVnMenecOS94o22VLQXRSFze4goz1HDjQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علوم پزشکی لرستان: دودی که در خرم آباد مشاهده می‌شود مربوط به آتش‌سوزی در بیمارستان نیایش خرم‌آباد است مردم نگران نباشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/136061" target="_blank">📅 18:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136060">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
ویدیویی از ستون دودی که در شیراز نمایان شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/136060" target="_blank">📅 18:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136059">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9QyZf8uXUq7TyZxLKu_NzBWgfodPy-2wyHgeT9VmHA8UsaqTjF9ZHXsYOyjqZe0U4lRtH7g1dEb5ZY6WBOv8yaXssJTEZkjs2IWRzUfndDF3rdZDIFZV9UgYd-SYTATTk2NkEwY6Z5hxdcB9KsmD71B82V6XDYeFjiBC2i0qrsoH8ObpcWnASlSPIpas8x6e9mRNwPzdhUah15nsnmZOY83j4ZsGdQadimyA5qSVDCcFHp97ld8KjFNIppSt7-IXJbBEpVV5dRBXl32XfENURjsLi7xrNFy5OZGMphPPqkVSQgVcw_xmGkseLNUoAWrar5DR3FuEOxw_rFTCgsxIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش شبکه سی‌ان‌ان، ایالات متحده قصد دارد تعداد بیشتری از جنگنده‌های F-16 و F-35 را از پایگاه‌های مستقر در اروپا به خاورمیانه اعزام کند، و همچنین هواپیماهای تانکر سوخت‌رسانی بیشتری را نیز به این منطقه بفرستد. این در حالی است که دونالد ترامپ در حال بررسی گسترش دامنه جنگ علیه ایران است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/136059" target="_blank">📅 18:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136058">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3186bd6880.mp4?token=oRCY6Y3i-aKdImzUH4uL2MR8p7A32YJs4c74TzAod__lVgO4cS2xTwxKeCSgH5Pe3jX8N3VeBvXARL8aXj0YTDf5nrfzP8RJFO_vkzw5Okmjh0eI2jRKF8B4fbo_eyPwz3SR06Dc1hbh7OFgrYdHz68Eepw8d16jcV-MwCJB5SKP5k6Hq_82UXXmzoBw4SZHzcCwfLbNe9frMYlOjkE_o6ociKmfdDV0ff_5nJ3GIfB75yYY_b1GW0xCrWm5NweKiiH3rOpUh1d54s2IPQiuaILBuciNmlqoDWfxNr1p2b-yWjxuVYwX32QYgPDjkPyt1s3TMBox99sl-T3zi4jfEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3186bd6880.mp4?token=oRCY6Y3i-aKdImzUH4uL2MR8p7A32YJs4c74TzAod__lVgO4cS2xTwxKeCSgH5Pe3jX8N3VeBvXARL8aXj0YTDf5nrfzP8RJFO_vkzw5Okmjh0eI2jRKF8B4fbo_eyPwz3SR06Dc1hbh7OFgrYdHz68Eepw8d16jcV-MwCJB5SKP5k6Hq_82UXXmzoBw4SZHzcCwfLbNe9frMYlOjkE_o6ociKmfdDV0ff_5nJ3GIfB75yYY_b1GW0xCrWm5NweKiiH3rOpUh1d54s2IPQiuaILBuciNmlqoDWfxNr1p2b-yWjxuVYwX32QYgPDjkPyt1s3TMBox99sl-T3zi4jfEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از ستون دودی که در شیراز نمایان شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/136058" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136057">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1xhMEEwZhv_eEDOUf_nVrsbAdFQlS1EqrKOtkCMuZnZ4WMGdORjZomSZPyPJACJfZ1oL20arM-tNjSbZEG4bFwH68S5Vnnn8qYdPbSgyk3pDTqrcs_qsTx9fHTzTZhg_FbN7Ek-v-x-IQ-yunH9UUXV94WMAUksKafS-g68B0Phh4Z2WVdgxDN3P1KhITjRci_H3EzQjDVKQhelku1pN-kS9VFlr0LuYdHAL-HpcI1ELCklRATVJLJY206E5kg4TceVIoggDHqOvIaLL07ltzALyaqXFnqH1dzGv0pLJvB5JD4dVw2Tj9k0XLSpGnsVvLPdiHFyWV5UHJzPXisMrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منتسب به شیراز
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/136057" target="_blank">📅 17:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136056">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
فوری / گزارش هایی از شنیده شدن صدای انفجار در شیراز
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/136056" target="_blank">📅 17:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136055">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
به گزارش نشریه "گاردین"، نخست‌وزیر بریتانیا، اندی برنهام، برای اولین بار با رئیس‌جمهور ترامپ گفتگو کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/136055" target="_blank">📅 17:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136054">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
فوری / رویترز به نقل از سازمان عملیات تجارت دریایی بریتانیا: یک کشتی باری یونانی پس از اصابت یک پرتابه ناشناس در نزدیکی تنگه هرمز، آتش گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/136054" target="_blank">📅 17:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136053">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
وزیر کشور (مومنی) عازم پاکستان شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/136053" target="_blank">📅 17:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136051">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtVBju3NtXcUxRu3WOFkr0UVaDICXPVONc6L0vRnGOMUHwI1YATagsUZ9g9TI7amMALjb17-3h4UPzVC0QwpgmjvjfctUefYjH76-QEix1Dr_dmNGCNr8gHj1HAbpPCXhRJS0HryJLaudHXSXuCOy1eZ5P07P1lAmT_c2_Wwr6dW9rmB9WS3ypB3E9P89psio1oCt22ziDK8NVXCqlBWVKSvp98Z2FC5xG--jXdean5S_3bkKrnSFEGRrL5yqhCRvukELDNo1yF88QFTwvPOCk8aN8gnII22pucZSZb1A62wCSadpOmBUAlXrPF5XvkQf29vGja3UZl0BWAVIakk0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/289f1a32da.mp4?token=gpVb7XpBNl6gGHS5OCbCmD52EXdMllLu2hXALk2Ed-ynFLg2lT96qLhLLY47zot06IrMrWyMxxKxFFVuMop0jWaxCP4XLzNZ4yH_6BjxpSxUTGUjdtObDaAUv7BbOcY-E2O3R0gjf5z6GgDB_ZIDZ7TAyFfkrpIPb4M0Bg7r_THP2ADfIXrF3ih6tdjxAuPMDlYSK0WHaGG9peWCiITrYU532OZ5jw70Vmik0si52rp2zLDOifrApuEAX5YwcFleJ0fm6LWTat9MioyuOMkUdMXpdWxMgmPSAlK_nw85A9aeYRidACj8-qUfCvtoDESP-Jq-EB2zqsHr7RBpKJ9zow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/289f1a32da.mp4?token=gpVb7XpBNl6gGHS5OCbCmD52EXdMllLu2hXALk2Ed-ynFLg2lT96qLhLLY47zot06IrMrWyMxxKxFFVuMop0jWaxCP4XLzNZ4yH_6BjxpSxUTGUjdtObDaAUv7BbOcY-E2O3R0gjf5z6GgDB_ZIDZ7TAyFfkrpIPb4M0Bg7r_THP2ADfIXrF3ih6tdjxAuPMDlYSK0WHaGG9peWCiITrYU532OZ5jw70Vmik0si52rp2zLDOifrApuEAX5YwcFleJ0fm6LWTat9MioyuOMkUdMXpdWxMgmPSAlK_nw85A9aeYRidACj8-qUfCvtoDESP-Jq-EB2zqsHr7RBpKJ9zow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از کشتی ای که ایران اخیرا بهش حمله کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/136051" target="_blank">📅 17:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136050">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDeR1r_hKnB_dA3OiO1rIvaWh4sohKpd7nmHShDzQenqa_tfKeX-zj-ti2c0DaMm8tA65S0okCNNCv5A66C_06dE9PhwcHHZ7B0OTF1-zy1xicnQnx6QWGhyY_76FkRS5u_v7zKuJLPONsQhUamFJ9f-an9B5AmGjnhZ94QQ3K3aLaQgzBpRGtAJxqA19zxiZ9nTehFk-sQI0yxHJa8Rwru87psVQ3aXQ9NdAmohwmy2tTU7XqcbGKDaPXA0t02hN1rqaKDZ6NSM_Lssy51WN9UzFHOUlrQr3hDbRoctTK4FnkIMuO3h-IldeI310au-frQQZ4M864t849pQwj_NUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترکیه، پلتفرم "پولیمارکت" (Polymarket) را به دلیل فعالیت‌های قمار غیرقانونی مسدود کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/136050" target="_blank">📅 17:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136049">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9085a568d.mp4?token=iKtsegUc-0qt2NEqYoiEKaGGvFPA1k9Xpl0LEFSQ3BDArRr-MdrUTK21_MFRevPjrj7-ukKQIbyUU4sHlX2TbHdD5ci_p8VnxM2Mf0s_6EG5YU3sQ_TIwsaagBAW0YPOTdspTjcOuLny-qVISNW_ehKmVPv0qV3wTTbca-twU78qOe8VK_vwvRgsOu0WLx8PEk6whVsANx1y72XDrskxHJsvhh_fsi5NtWKhP8r25svOsX0ZJu6xEzS8WB7Bf5RZ5z0ze2iDvtDBoKUaWAOJNLcoLoqTewqffZW4Rj18g_8JrYCxi1Nl3Zs-d6EWC1-CzYAE1Yz-OrkvY0BQJ9oDkT8ufrubaIZbz861vBLlGUVvj-3KCwV6iJLXSIaephkyb2APFZD5QDtP0UzN8IuD77bQX2azyYr4G4dvn-8F_04gFdMhpghfMqN0dMbmmT_WbVjNqgZUKqYdOZv2ZJ5k2BwhWks6-BSCfYWdS4yR7P9K3flo-ztyA-6T6muyv0GbGaeonuEBokY7z6idlnLseleBaIT5iNaKK0T8bBa9ZwQhkAe7o9mBsc-ZZkbe3uHFE4BDyolEBkssItY8bjHKW1uFf6jFxASicYAceHgtb2OqM-Paxf_hOxF4YXTpgba3An-BCL45nyktPD9iDTd7sKmosPZzx3jGPToraqVqQH8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9085a568d.mp4?token=iKtsegUc-0qt2NEqYoiEKaGGvFPA1k9Xpl0LEFSQ3BDArRr-MdrUTK21_MFRevPjrj7-ukKQIbyUU4sHlX2TbHdD5ci_p8VnxM2Mf0s_6EG5YU3sQ_TIwsaagBAW0YPOTdspTjcOuLny-qVISNW_ehKmVPv0qV3wTTbca-twU78qOe8VK_vwvRgsOu0WLx8PEk6whVsANx1y72XDrskxHJsvhh_fsi5NtWKhP8r25svOsX0ZJu6xEzS8WB7Bf5RZ5z0ze2iDvtDBoKUaWAOJNLcoLoqTewqffZW4Rj18g_8JrYCxi1Nl3Zs-d6EWC1-CzYAE1Yz-OrkvY0BQJ9oDkT8ufrubaIZbz861vBLlGUVvj-3KCwV6iJLXSIaephkyb2APFZD5QDtP0UzN8IuD77bQX2azyYr4G4dvn-8F_04gFdMhpghfMqN0dMbmmT_WbVjNqgZUKqYdOZv2ZJ5k2BwhWks6-BSCfYWdS4yR7P9K3flo-ztyA-6T6muyv0GbGaeonuEBokY7z6idlnLseleBaIT5iNaKK0T8bBa9ZwQhkAe7o9mBsc-ZZkbe3uHFE4BDyolEBkssItY8bjHKW1uFf6jFxASicYAceHgtb2OqM-Paxf_hOxF4YXTpgba3An-BCL45nyktPD9iDTd7sKmosPZzx3jGPToraqVqQH8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلم مربوط به انفجار در نیویورک
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/136049" target="_blank">📅 17:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136048">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
فوری/صدای انفجار و درگیری در نیویورک
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/136048" target="_blank">📅 17:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136047">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTA2Qmgb-lmFZ42h30v4d3Z_GF63l0svvn6Jx5hsDs7TvHOBYpv81lpmO1d-goD3jOmOjP1fwaPDrjCv8KHFA8oI2tk7qezzB8NMrLLT8Zf_DDfaNl4EQprZvGB6PE8A5sg1Uv1SQpMulZFbfdE7772oI489FqFiAQtUVy7lg5hF-3Y2IBpK1K-nttUYqF5G-HmIPGk0Q5Zawu6BB2ADVXzCqia_Ci7BLwq5hWMGdg4UTTyJodw5V-bU4tGF95ZUmdai5s1aNBuMHuUq4DosGbIdoc_IlESPVHFjcM_PXGgMbDgCzU7ZIDVGBcV9-r-2sfw69nJHEjFLRDT5SS-rNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سوال عجیب بخش ترجمه امتحان عربی یازدهم که امروز برگزار شد.
🔴
فَشِلَتْ خُطَّةُ الطُّلابِ لتأجيل الامتحان
🔴
ترجمه :  نقشه دانش آموزان برای تعویق شکست خورد !
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/136047" target="_blank">📅 17:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136046">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/345c5a30b6.mp4?token=Uw8g_ZNo7CMdeCx4n1QHpBiBvdFiI239SnywDNPdTvUOEkBPGmJ7dnlp1amOgh5HIj-3IUVei6a1L77gtclM_-ZBCoTI4JAybjEtfV05_obqJeM9Fum_9NSj-Q5cl_n-ABSMbjbQPEkow_ZZ4Q3qJb8LV4P1BwqDLc9E69znlQKiQYdmgniVik6K0G_h4lB_-FWHPdAktSKeweamcjkSUPhSiYkU4hHLmWnEpVi2C0E7n9iMSYuO6h0IWnNHwcMSUc8WD9QshILqpzmmS7MKA7dxoKFcBC2P1resv23SoAMrpk0PPaY7hCuA9Q98Z0FF1-GhJYT1Ev8FRx0CcyMXU01_zO9U4iGk6EL9Doejhm4sNn73ENGnOx8WEVFbSLQhE1YjSsbLzdLpIvntNeIXVdWADJr0ox466cECfEtpVRiYmIn2eXupJnswVXKQPbfaBGVmDtCpwJFLPLIL01tJ6g9KURQaE5KkdVTwMs9LGXAOlAfm8tn0z3Yx9LA5hCfxaUBZEs0_nhUB9QZL3LAUlJX4Ww0rX0eoMEmhw3TW6-48nMKaBNbDC4qpnNNo3MYTYKMIrKb975F4E-IHeuVcW9dqrgOiDPJqip-U9ZBRRIyn_rJMiGIb-CsBeqapMMQ64EORkFQUfNKg7_waNmPu-k5NtpXVb_JjK_-gtZgpxs8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/345c5a30b6.mp4?token=Uw8g_ZNo7CMdeCx4n1QHpBiBvdFiI239SnywDNPdTvUOEkBPGmJ7dnlp1amOgh5HIj-3IUVei6a1L77gtclM_-ZBCoTI4JAybjEtfV05_obqJeM9Fum_9NSj-Q5cl_n-ABSMbjbQPEkow_ZZ4Q3qJb8LV4P1BwqDLc9E69znlQKiQYdmgniVik6K0G_h4lB_-FWHPdAktSKeweamcjkSUPhSiYkU4hHLmWnEpVi2C0E7n9iMSYuO6h0IWnNHwcMSUc8WD9QshILqpzmmS7MKA7dxoKFcBC2P1resv23SoAMrpk0PPaY7hCuA9Q98Z0FF1-GhJYT1Ev8FRx0CcyMXU01_zO9U4iGk6EL9Doejhm4sNn73ENGnOx8WEVFbSLQhE1YjSsbLzdLpIvntNeIXVdWADJr0ox466cECfEtpVRiYmIn2eXupJnswVXKQPbfaBGVmDtCpwJFLPLIL01tJ6g9KURQaE5KkdVTwMs9LGXAOlAfm8tn0z3Yx9LA5hCfxaUBZEs0_nhUB9QZL3LAUlJX4Ww0rX0eoMEmhw3TW6-48nMKaBNbDC4qpnNNo3MYTYKMIrKb975F4E-IHeuVcW9dqrgOiDPJqip-U9ZBRRIyn_rJMiGIb-CsBeqapMMQ64EORkFQUfNKg7_waNmPu-k5NtpXVb_JjK_-gtZgpxs8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یاشار سلطانی: جمهوری اسلامی هرجا پاگذاشته بدبختی براشون برده
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/136046" target="_blank">📅 17:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136045">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtncL9f2_txys11DxA4huCdwdIoWXlvt8IaQgdIdB7IQhTOB4sDlFdZj2RohI0JdfjixMrn7ZxHFZtTHfCn7LYVYHogO2mv7T_nX01fuQ-xm529r4MRG15nR9SSdhNQsAjncXkH-Ub7LSi8Pm2XodZN7GQ7JCp3hZEok-P-IwJZUGo1Ai-6Zp0_G4X-VGH8NuujAn3Nza79Qj_vvN4PAyqO3DJyS2r_rZ5oOjcUmK1V-xq4Ix62-jb_F3Y5bjNt9goI7hajtley9RpRvtwK1YbA0DwF8nynT8ylgk2-bSamyy6gfz8xpkjZlmXZTxtjx0rghrwwDmvbm2fJdImA4tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت خارجه مصر حملات ایران به کویت و بحرین را به شدت محکوم کرد و آن را نقض حاکمیت این دو کشور دانست و اعلام کرد حملات ایران باعث بی ثباتی و آشوب در منطقه شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/136045" target="_blank">📅 17:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136044">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
گزارش انفجار در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/136044" target="_blank">📅 17:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136043">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4hYlMHuq0gV0VgjUbBtEam8zUKo-1wH8bmWcjsFZWdXkkaVx0pZDfQqq3sVcY893mqgvx2ILP4olPP2XZpuyWh5Ho8GHUw7W5YottSofQUzpEfcFRFOrmQriesvJtYrjlvYtEapN84M62PUp__66eFGqLpiPiRlqdAyrmP5HMfhK-xyZsOQ6GND6njtUT0YvCQ1cJZzYSeEOKfWBaev6FcojsPm0APvUr9wNXbYRctLzUJ9N9m8C1r9XVWe-LmthBlg8ooIoRR5a6LZh_G-ea88adhW5p0LcDZ8qgyJylW8LJP2AKRr-vUJ-XZ_ZrDewVhqTgbOpi6sRJKT60Phdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کویت: درحال رهگیری حملات موشکی و پهپادی از طرف سپاه هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/136043" target="_blank">📅 17:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136042">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZeNNlylGFY3_2rqUDwcS0dN8K1wepUIjVkjKw_bQRYp07okWFnfw-de3OlC6ZmX0C-HgN2AGF0VPvn88xfE-1TD2TgYL8Sq_e2OC9Lg_sPzu4vnmqsk26NYpoQsIKQuCAXDVpofi9R0jgXQp86M4TjcSgMfuCe_gZYmuHL8ZM17JnoPss1KUK_KPm46ROax2XrLGqKI5PvFXeT4HMSI7um7NgNDjgXYBy-Yj4oresMHdlpUEFkKQuJlchHrtzOHZgPs4jea2PnVk4LBFESyCwpmhnaPIWLPla9zFXfQgIr5pd8N-NNYmQn236usEC52ZFEbijuzUK3wErjUmtTc1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت شونه تخم‌مرغ یه‌شبه ۸۰ هزار تومن رفت بالا
🔴
دیگه املت که ساده‌ترین غذاست زیر ۲۰۰ هزار درنمیاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/136042" target="_blank">📅 16:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136041">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
گزارش صدای انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/136041" target="_blank">📅 16:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136040">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flaH2AZ7EkZv71Luwy55y9BZVUB6PbuCEzqTW41EcbzFjJPDZUPSW3qBXVqnXR8-T6kuBXGqVnHAjEbpYLAlDOuPLJdSV4FRgvv4rLbxhZswlrYwD6is-uhj0Hd-Z4fXzv2tixOaRHPUIvUe8APtv9nRf6O6HbuKdkH5gTLqkehAubcTZmzHQ9sFaHStXp3fSETsv-CSUyvns7uI0YOKbzDA8BGaWW8GxsJiI6z_BP5P4qlTfdBmfToFMjQabxuNsZipu1BB-FAm5YmHy7FZkko8isJWASJG9rYzal6zJJSPrlfTlqsW3MEBtqpUHylkJaAHOzrNzHFqiZ64syJ9FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ستوان یکم تایلر جیمز فیهان، ۲۵ ساله، اهل اوا بیچ، هاوایی، به عنوان یکی از سربازانی که روز شنبه در اردن کشته شدند، شناسایی شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/136040" target="_blank">📅 16:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136039">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/empD6fwNIFBlAOvVtsFcwArV6wdbR41fpbHDJ39-n-9PuHjKQ4SUgSztE-PDl6K-r4fWBS4CNANl9avgf2kSHqphu_wQ4I2ReXeHsIBcnEQV5IWXtYOLasfaFOa8Ma1jrXD9Us4WfyFeDH8heskX5ElQmctfMuNh1YOlZbtO1VupuMIgE8Jx-p7N1gwU_Q1cb5FoudMOOT5WgB6HFMGpdHaJhHLr14zfUUl_UjhbVbEpAyo_5jE0Vo--GJE6OWgFOhjSvKfQXeqcN53qed0fG3XblY_sNxv7J_nPZrpWZGGSZCSa2Mt_xU7T7zzpYLlYQqfWNZWRo9B3pMFMD35T0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رضا پهلوی: حملات آمریکا نباید متوقف بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/136039" target="_blank">📅 16:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136038">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4x59ofCjLQkoK2Xy2mGZvitIjkTj3wte7T23dvfDRASNceRxX8dyimPBoslZjQsQi7g6zNkuy7p_vA5v87v2VI2SzbCOM5xvC5DGeEDsN8ircxKG8SQ85WFr_1lMF1mW0IEUhz1YAOpRmu0xVlO-I6DY7o02MehB3NDH9YbQxraxCNt_KZe0-R2xj00O96nTNFbLFojtf5RCvPqUCELW3kfU-oqzImuRPseZ55e1xm_jaFwZIggbTj5xvYf_H4UzBWT8szqFHpWjJ5-HbVjg9LoEkuxA4wh6moucUVJijghsSs_xoCQtCQcvq1csqEJJMBZw8-VnagfDwz00xqktA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از سرباز آمریکایی ۱۹ ساله که در حمله ایران به اردن کشته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/136038" target="_blank">📅 16:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136037">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldp_dMZ0DPYn9UuxTLcPau43zKzQQvqOTOlrqBSVgwarmQm3qwbvEKIEHwYhEdRMW4KaB8huNGdCcuaZl0J7xZBvCkEAkW4tt6l0WlE8x5EWCTbs5SNZ1FjX7MMs3lcanXxBYFnKHyo2TT36Flci6S8YE_K2Jvba2e33I4I1jxUwrkPBd-_XLzBuhszTzEmMFPjqfeKdOqj3B8MpEQfAn0zycQjfXzjLM-hho5HpgTwjmaRIomoYrH9566cKixxEesBu1dFmrA-OH7m1coYoCGCRkjKIFCOWBmAT_7CI3jTIqswZetYtoB86yATJYwBzyHYx5zOLqCQPnxKuc_FWqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت معاملات آتی نفت همچنان در حال کاهش است و قیمت نفت برنت از مرز 87 دلار به ازای هر بشکه پایین‌تر رفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/136037" target="_blank">📅 16:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136036">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
انفجار در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/136036" target="_blank">📅 16:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136035">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‏
👈
فرماندهی کل سپاه: با همه وجود، هم‌صدا با ملت بزرگ ایران، فریاد «لبیک یا خامنه‌ای» را از ژرفای جان سر می‌دهیم
🔴
ما سبزپوشان حریم ولایت در سپاه پاسداران انقلاب اسلامی، پیام حضرت‌عالی را فرمانی نافذ، میثاقی الهی و نقشه راهی روشن برای استمرار رسالت دفاع از عزت و استقلال کشور می‌دانیم و با همه وجود، هم‌صدا با ملت بزرگ ایران، فریاد «لبیک یا خامنه‌ای» را از ژرفای جان سر می‌دهیم.
🔴
میثاق می بندیم که پیوسته امنیت، استقلال، عزت و پیشرفت این ملت را ستون‌های ایمان، توکل، خوداتکایی، اقتدار ملی و تبعیت از ولایت پاسدار باشیم و هرگز سرنوشت این سرزمین را به وعده دشمنی کودک‌کش که کارنامه او آکنده از عهدشکنی، فریب و کینه با ملت ایران است، گره نزنیم. تجربه‌های بزرگ این ملت، ایمان ما را به این حقیقت راسخ‌تر ساخته است که راه عزت، از مسیر مقاومت، هوشیاری و اقتدار می‌گذرد.
🔴
فرمان حکیمانه حضرت‌عالی را نصب‌العین قرار داده‌ایم و اینک که آمریکای جنایتکار بار دیگر راه خطا، تجاوز و ماجراجویی را برگزیده است بر این میثاق استواریم که ، «درس فراموش‌نشدنی» را که نوید آن را فرمودید، با قدرت، قاطعیت، حکمت و اقتدار به او خواهیم آموخت؛ درسی که هر متجاوزی را از تکرار خطا بازدارد، هر طمع‌ورزی را در هم بشکند و حقیقت اراده شکست‌ناپذیر ملت ایران را در حافظه تاریخ و ثبت کند و مسیر حکومت جهانی مستضعفان را هموار سازد.
🔴
در اجرای تأکید حضرت‌عالی بر حفظ وحدت و انسجام ملی سپاه پاسداران انقلاب اسلامی در کنار سایر نیروهای مسلح، صیانت از همدلی ملت، استحکام جبهه داخلی، پاسداری از سرمایه اجتماعی انقلاب و جلوگیری از هرگونه رخنه دشمن در صفوف به‌هم‌پیوسته مردم و نظام اسلامی را از مهمترین وظایف در منشور پاسداری از انقلاب می‌شمارد و بر این باور است که اقتدار دفاعی، در پرتو وحدت ملی، استوار و نافذ خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/136035" target="_blank">📅 16:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136034">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
فوری/آژیر حمله موشکی در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/136034" target="_blank">📅 16:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136033">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gwq__qZVu1YIhAXeJEA97tE9QwYyE7Pl7fZkp5GyoFEzSrjK5-5bibACLaS9ZKMPHVChwKtsJlDlQuCgbsWu0g76-4D-UYBkdhuJAyBvWEsnF-3IyfPqyOARDykrridNEcbEF6bUX-pATkG42CpiKQz9SazPibxWtm3ONYW3-LED0BpgQKGSyIn0FXILboEN9RzWZbAXqZoiRyzApoeJownuQOjHN2QY256Fi44LPqNxCEHuplGEhx2nFxWEDsdmH4JJJJ9NBnA9NZrZEpiwEwnoW81Sdru5iZGILSru-9V9CUOJXyef4YdRAms0bYAH4Twf-1rO-PB6H0SORUJpsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری تند حامد لک علیه بیرانوند
@AloSport</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/136033" target="_blank">📅 16:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136032">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYMncsJXheDGBy9rFU-tyuO5W7t68C9trAjcfPMLKRu4vQ9nFMQzVjuM4bm4aomX94EJrleK2pAtVswhxu4QZzGPN9VhtkvRA-LZ_Fqa5Yfmj1FcPXQzc2_sp9Ry4r-2-GO2nDDqSshw9v0le9an-N7f4_uJp0gj1QNspO5IvJTBvSPiv659rEDQM-fum5THYOhXZVM1E2Pxu2tdUkp-mbqtLG-V7Mz3rr5myv7iw68k8jp7v_p78XAmW4MDGpvdPljHrvWUVSMf9-NZ_L5saTdiNdFLj5mEnK_juYbs9VhyBKCYvYfaxvQ8RTBVztsQ1kvASEHXFytMGmkzggcnYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلمب تعدادی از کافه رستوران‌های خیابان‌های سنایی و ایرانشهر در تهران
🔴
از صبح امروز تعدادی از کافه رستوران‌ های خیابان‌های سنایی و ایرانشهر در تهران پلمب شدند.
🔴
جو کافه، ۱۴۰۱، سام کافه، دو بار، نووک و تئوری از جمله مجموعه‌هایی هستند که تعطیل شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/136032" target="_blank">📅 16:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136030">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
مارکو روبیو ساعاتی قبل : ایران کشوری بسیار غنی و با پتانسیل بالایی است اما حکومت آنها علاقه زیادی به حمایت از گروه های تروریستی دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/136030" target="_blank">📅 16:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136029">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEMwaPhazZ6hesxqbFIhM2e8RUedFxviywVnZqytbuwLeY0BbSl0rZaTeh06akBpZX713txW6vBhg7ZC8wSnMdlZ7SIDe1M2BVbWRctYd2dPGBvfSdw7dnh1bqJWZCzrXRnR3TXsXaGbG6llfaPgcOXmpLrKrvgzbmdXkqwohi6jfUV0hVPfVdCAXttiQOMTGHNV2sYHoNsj5yOaaEneWv1_b7Y5KyMyRjZ_U6ooYHjXX8YkO69TRegiB40vkEDWGwLoYpJ82rw4ZIZG7AjlPyCWWikIUuGMUdci9nDy_sF_Ek6KAOQHAIZQiPAyxTjvu5cQE6YJgvj8UAvXpZfPSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیلی‌بست: ترامپ بالاخره مجبور شد اعتراف کند که هواپیمای ۴۰۰ میلیون دلاری که قطر برای استفاده به عنوان ایر فورس وان به او داده است، به اندازه مدل‌های قدیمی‌تری که بارها از آنها انتقاد کرده بود، امن نیست
🔴
️پیش از این وزارت دادگستری آمریکا دو خبرنگار نیویورک‌تایمز را به خاطر افشای این موضوع، احضار کرده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/136029" target="_blank">📅 16:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136028">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
دلار تا کجا میریزه؟
این تحلیل عجیب رو بخون
😳
/
کلیک کنید</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/136028" target="_blank">📅 16:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136027">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlS1bds-lvJ65hvcMTSp_g538xPUgjSvNBdwUv5f4HdV_P1zZrVPrKbdlSYLPxYSzNMzeaAEUHGq4eyG1iAbFDBZYInEinIwLw19SeZjauoCPTHQ_v4NJR4Bm_vK9mryN6TXDTY0wvRy5iK8c6b-O653kS82u2Z5vpucK7lHhDa5cDBAlmPeK1a4twOiVvitehChNl2jEiZeGnkuusX3IGN7oKRxSgulEEFkaIwQEasEnZfjfn1FIpF3pdfoIZ_fRB2OXhFRO34nPDR2edVtQd14TVIT3bFAbVSyT-S-luQFHKEHBmr9mqgvYauNbEO1X12GUAi1C9YeUgEr1quXkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
العربیه: پس از آنکه ایران اعلام کرد به دنبال ازسرگیری مذاکرات با آمریکا است، قیمت نفت برنت و نفت خام آمریکا کاهش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/136027" target="_blank">📅 16:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136026">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
دلار در بازار آزاد تهران: 188,000 تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/136026" target="_blank">📅 15:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136024">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/Kv10zWldvzx3uPp03QQd-HbCnCFNbcvzx7B4JrsYCv-qvpD7YJYP3sqISGWMwMLX6Gqja__GzzcSJ4xTT7vH-ECJpFYVI9NVR9bm4LTzhmS1pJDXN3si80x5CLpYKyBk4DIS4z8EtySKcezPQmkmR_JZ6vO-w0U_jT9mwWZ8fHWCklHHZ1MzWtfdCiUYDuQRrvWPzGgsgFZpcQSq8oyZm0uvThtlIw27uByLE1ypt48cS8kBxi2OuGRvisOw9uWzGFqWwwWIGItKUbiTySx_sxzeGEFMSdilVMjnhlEOOfPVSG4BMj4DNy8D1s8yTAvLWcFkqmhFnimg1t53raqpGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/txjBB87yTIKBd9kWAkAgBE78UaZG0xHeOgPjoJ-k78Df9i-a8lm-MszIn8ISmRT7tEFrz6B8EKy6U1t60uZLAdxJHcVToUgQH26J5JFeR6x9WBUCTX-lfpl0z9-J0fwXkzXcM0J2aDVAJuqYmlwYAUr8biJdCDy42McHfiLW7hyYbWTjvm1cQHBTCO5aGMnFOZ6AVftk7lRF3gK23cVNEAsy5mV_7VBllCxx_faHOSggS8vkkPc5DaUSZruD7ThdEepBomNqit0MC344_90t55uG2sqYVxO_h95MWgNrA9IzaeNQduSlgf5Ad1KuKaEMSyU3vQspW4QVH8pS8NtHng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
داده‌های تصویری افزایش چشمگیر فعالیت پهپادهای شناسایی اسرائیل بر فراز لبنان، به‌ویژه جنوب این کشور و ضاحیه جنوبی بیروت را تأیید می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/136024" target="_blank">📅 15:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136023">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0efe0662e9.mp4?token=Zi98If2CSQEnF9WL5pSaTerHTtIuOCe2oZVBELOfrbnUVzCgmXRas43Ou3qX8pW4ieHZabBDiN9AQQ6MF3MS7qZNRaYYDvelanJ5_r03nQ7OeegZ68qe6DNlkCKh9dtpjlCZTQ6G_js4769aNMs7efQ3nvv_sfQQ333yTGJXT065L1JqOFWZdXrLrvIvMDH-z5zbnzkGsn6TgPcBrxFUqB0x3WiX-ukhGnKvUKNCuZXSUmKh8QCqiKiYUg38RppPimvBa0inpUTNiePKzNbhrWIJdCpt5-bjQP9CAK4FbjsRxofizkGDarHCJN3TjszRgXzoevr2LOYGYFM5mu7895RkrTvD6dIHYyg5MlH0okNn6l3liVqWg0V1FBr2W6IDwpZPxFEpdcZWoovfHAYag5UGp4rFNsvN5-Rf6kgz3czMmNbFQPnTkvybtrEOCBoYs1eNYeitROnvXhGu5dpHIhCQ3doJ0rzUiV8xUjJmHxZHjxH5Ewy44KXpNGlkzSjaZ-d78mZJD31INdx8rVHrGsFy25eazx38CzAZewdrTOd5Pc6aLNt6PTOhv_hhOAY7zw67RMYaEKzqKdFLveu4ZhHVeANu8gfIKihDTUhcqM1WoTFZc-hpSqFrIWAJbWI2m-T0uwzoISpNWXRtu0qYjL10bTenFrcOHISHdtD4tSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0efe0662e9.mp4?token=Zi98If2CSQEnF9WL5pSaTerHTtIuOCe2oZVBELOfrbnUVzCgmXRas43Ou3qX8pW4ieHZabBDiN9AQQ6MF3MS7qZNRaYYDvelanJ5_r03nQ7OeegZ68qe6DNlkCKh9dtpjlCZTQ6G_js4769aNMs7efQ3nvv_sfQQ333yTGJXT065L1JqOFWZdXrLrvIvMDH-z5zbnzkGsn6TgPcBrxFUqB0x3WiX-ukhGnKvUKNCuZXSUmKh8QCqiKiYUg38RppPimvBa0inpUTNiePKzNbhrWIJdCpt5-bjQP9CAK4FbjsRxofizkGDarHCJN3TjszRgXzoevr2LOYGYFM5mu7895RkrTvD6dIHYyg5MlH0okNn6l3liVqWg0V1FBr2W6IDwpZPxFEpdcZWoovfHAYag5UGp4rFNsvN5-Rf6kgz3czMmNbFQPnTkvybtrEOCBoYs1eNYeitROnvXhGu5dpHIhCQ3doJ0rzUiV8xUjJmHxZHjxH5Ewy44KXpNGlkzSjaZ-d78mZJD31INdx8rVHrGsFy25eazx38CzAZewdrTOd5Pc6aLNt6PTOhv_hhOAY7zw67RMYaEKzqKdFLveu4ZhHVeANu8gfIKihDTUhcqM1WoTFZc-hpSqFrIWAJbWI2m-T0uwzoISpNWXRtu0qYjL10bTenFrcOHISHdtD4tSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حوثی ها (انصارالله) اعلام کرد که به عنوان پاسخی به محاصره و حملات انجام شده توسط ائتلاف تحت رهبری عربستان سعودی، فورا یک تحریم دریایی علیه این کشور اعمال خواهد کرد.
🔴
جنبش حوثی همچنین هشدار داد که هرگونه تشدید تنش بیشتر از سوی عربستان سعودی، با یک واکنش "جامع و قاطع" مواجه خواهد شد، و در عین حال خواستار بسیج سراسری شد و از حامیان خود خواست تا برای تمامی سناریوهای ممکن آماده شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/136023" target="_blank">📅 15:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136022">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/206a60f2dc.mp4?token=NKEr3EFTt9dFj8r2MUg4WoK3tcBD2cW6_D08fu1rRDSxOW8qeHw8wgu6dQAXVFZbfkV4pPY1gMhTxLi6BOLc12BUtbOphANfCOvqmzEzNsiXhCKzV704jZVMsdboYoxdxUMz81tzcE_NXaQ0d-Lfczb2hdvaq9Ew-LUXp6k-ApEnUMO12H7CQJYfKArWQuMs7XzMukMkCugikbNjxBDqofTGFDHgFVbzKta-H9dON4Ud9rhH7PAkpkrcInSuNRZ4JIQCttVIO3FhfVk8N18V9mXs_xU2Wso16RvA9HpH_Tpc_ppqkJmAtLuadGgmUXdKnVvS_ktVb8r_9yBcOEGcbTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/206a60f2dc.mp4?token=NKEr3EFTt9dFj8r2MUg4WoK3tcBD2cW6_D08fu1rRDSxOW8qeHw8wgu6dQAXVFZbfkV4pPY1gMhTxLi6BOLc12BUtbOphANfCOvqmzEzNsiXhCKzV704jZVMsdboYoxdxUMz81tzcE_NXaQ0d-Lfczb2hdvaq9Ew-LUXp6k-ApEnUMO12H7CQJYfKArWQuMs7XzMukMkCugikbNjxBDqofTGFDHgFVbzKta-H9dON4Ud9rhH7PAkpkrcInSuNRZ4JIQCttVIO3FhfVk8N18V9mXs_xU2Wso16RvA9HpH_Tpc_ppqkJmAtLuadGgmUXdKnVvS_ktVb8r_9yBcOEGcbTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری / نیروهای مسلح یمن محاصره دریایی علیه عربستان سعودی اعلام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/136022" target="_blank">📅 15:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136021">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
حوثی‌ها از هوادارانشون خواستن برای همه سناریوها آماده باشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/136021" target="_blank">📅 15:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136020">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
الحدث به نقل از یک منبع آگاه: پیشنهاد آتش‌بس و بازگشایی تنگه هرمز به مدت ۱۰ روز تا دو هفته، هم‌اکنون در دست بررسی و بحث است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/136020" target="_blank">📅 15:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136019">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
شمار مصدومان زلزلهٔ کرمانشاه به ۱۰ نفر رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/136019" target="_blank">📅 15:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136018">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
سخنگوی ارتش: جنگ تا دست‌یابی به بازدارندگی کامل ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/136018" target="_blank">📅 15:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136017">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_Q9CenPnn1PsoIOkaQEYWAHmjmZp2ejvFXSasdSVir8BpbzrDHshjuq5K0B6sDGFD-7ujV0pXe690cAa_PQPlmtq1sFyaNtSbpoO8GZy2CRgJxBDoPtvx6qYvnyLZ7ZVBkZ-HQnzWv7S97YRD3rjndzgEA2Zycm_LYv6DOALjvRuHvAgkReAmQOWyR1oNVy2T8q_ohKgr6QZ7n7z0h0TKCSwtZlEnDdmFMt50hrB8zAwXinasMoSnDx6lS8crPW0Ai2pj-1Y1zK5y6kqo1o46OTMiL8mfwGe3PF-4RbNX_qtXQsf2uYHHTrbUHANiwPv7kCxILyilg2A9tOihyiCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حماس خليل الحيه را به عنوان رئیس دفتر سیاسی حماس و جانشینی یحیی السنوار را اعلام کرد.‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/136017" target="_blank">📅 15:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136016">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
نیویورک‌تایمز: پنتاگون اطلاعات مربوط به حملات اخیر ایران به اردن را که منجر به زخمی شدن ده‌ها نظامی آمریکایی و آسیب دیدن بالگردها شد، مخفی نگه داشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/136016" target="_blank">📅 15:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136015">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
پاکستان و قطر امروز دوشنبه پیشنهاد مشترکی ارائه کردند و در آن از ایران و آمریکا خواستند به عنوان گام اول برای ازسرگیری مذاکرات، به مواضع خود قبل از ۹ ژوئیه (۱۸ تیر) بازگردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/136015" target="_blank">📅 15:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136014">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
سخنگوی ارتش: جنگ تا دست‌یابی به بازدارندگی کامل ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/136014" target="_blank">📅 15:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136013">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35e7c4c5e6.mp4?token=i367gjp_aqwasy2rzqfgCMB4O4hx8p5MWRsM4saXjESFbDxByUvQPqc5f9-qo7_CWfWJLoAv0mTv5efIexXYTk7QqJSg3I_djMmXk0V6PtjHMuFB8c-nBtNPZW9FIWC3V4cRAOmxYS9dqM7nmdyR-AuuZRORaPOO8ApjykNxWY31veLsknOIFA78gn4IVvWulwseKWj36Ym_r3t6ggt-itPZ84E_RX0z7GUQz6_r04qx1k5iiLnW-hUpF7iZNh-tBocmJ48kkWKeUQtBnLpywL4EU7iWJNs0jguyyMnJ1I84Pmtzjl8dc4veMxFJ1pl37xgYrOIxLVxit4TrE6iW_k0L8U3sZDzdZDUCGtK0LN3vf4ReNu2GG9M2DdKqJRgAIn3iA3PZAUPmVVn1-AWEnvQe5lFGsgysJbpmjBkKVBlIiKWOlbF6yX-GpeSEtUPHePG8fGPOkQjsoP3rHlWL1OeWLjs1MSj7uivJPBInSQECfEO6iqIJ6wkDzvgViiN3orfWV9phlac1gC6BHt30GsU-dAe5Fr-qhHncVQpuyE_HOr2ZUXVVCED1_Sn6YsUcA7whqGKre-svmGiUR3ptfHZCYIWLVWDiz27cHa2Ed_jC4VWrGzRUlMAkspHnOCZe0bWDsh5pDwFT82env_zx0opLSKTdsiUPsZlU3l75edA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35e7c4c5e6.mp4?token=i367gjp_aqwasy2rzqfgCMB4O4hx8p5MWRsM4saXjESFbDxByUvQPqc5f9-qo7_CWfWJLoAv0mTv5efIexXYTk7QqJSg3I_djMmXk0V6PtjHMuFB8c-nBtNPZW9FIWC3V4cRAOmxYS9dqM7nmdyR-AuuZRORaPOO8ApjykNxWY31veLsknOIFA78gn4IVvWulwseKWj36Ym_r3t6ggt-itPZ84E_RX0z7GUQz6_r04qx1k5iiLnW-hUpF7iZNh-tBocmJ48kkWKeUQtBnLpywL4EU7iWJNs0jguyyMnJ1I84Pmtzjl8dc4veMxFJ1pl37xgYrOIxLVxit4TrE6iW_k0L8U3sZDzdZDUCGtK0LN3vf4ReNu2GG9M2DdKqJRgAIn3iA3PZAUPmVVn1-AWEnvQe5lFGsgysJbpmjBkKVBlIiKWOlbF6yX-GpeSEtUPHePG8fGPOkQjsoP3rHlWL1OeWLjs1MSj7uivJPBInSQECfEO6iqIJ6wkDzvgViiN3orfWV9phlac1gC6BHt30GsU-dAe5Fr-qhHncVQpuyE_HOr2ZUXVVCED1_Sn6YsUcA7whqGKre-svmGiUR3ptfHZCYIWLVWDiz27cHa2Ed_jC4VWrGzRUlMAkspHnOCZe0bWDsh5pDwFT82env_zx0opLSKTdsiUPsZlU3l75edA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سرویس امنیت ملی اوکراین (SBU) اعلام کرد که یک حمله با استفاده از پهپادها علیه یک مرکز متعلق به سرویس امنیت فدرال روسیه (FSB) در منطقه خرسون انجام داده است.
🔴
این حمله شامل استفاده از 13 پهپاد بود که به این محل امنیتی مورد توجه، که گفته می‌شود حدود 100 نفر پرسنل و بیش از 70 خودرو در آن مستقر بودند، حمله کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/136013" target="_blank">📅 15:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136012">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
نیویورک تایمز: تهران و واشنگتن در آستانه یک «لحظه سرنوشت‌ساز»  بر سر جنگ قرار گرفته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/136012" target="_blank">📅 15:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136010">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TC6gBMAG8FYSeb8w-1sixRPtn5HQ7eX4yAjgVeRy79xZknK2iZ1lU4_eunU5ULM--hynKGEEMeYdJ06dV_nNvrONhyRZkyGw0a82k0AHeulqHl2jDGvkNi4-AZMBqhomd_bHQRH8KEn8lE5Qp64RS-eFIIpYw7RRvC-Bixu0KrpDTj0qMSUjgCEeSAuBWXeQLWFHlahJAIgliatX-F8tOFhRPFk8sS5XomNRR5U-fWCE1KS914l7rdkdbajl6CJhOEItn44leL0vk1_CLHmnXHQ2fwOpIiC43gLim9bT6t6CMwRyIgnl9oZUsm9A0QN-MI60GR9ZPU6W9I2lWG4Knw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k0vweA4-xejzDWpSBgXlKXdZvRN9FBPIm53kpBqtQv8b2B3EpspWAUtXwcD1Guxop5Xlf4BcIMqPfxFrnNaSSrkvbcNJwDtGBnijNYc2rIHKuVtlvzmm2RxkUgsQdwRC-dG04w4eCzMHX8zZrrdhefjW-dNCMQHVNCRBi3cFcnuXFVKubSbeQI7AQCc4jjOyJoR-2ib_7lIeSDz2Hw1Q_Lz1bsZFnB7tns-hjdmlKWjhUPJ8nFYB_34ZBGAI-zwmebu5ArV2sa6JcT4MLShNgIFsJkMgxc3pg463ZDnSqX52plvkwz3mSp6oFw-u3tXKtf6BYvnuNrrFzMFYewhaPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تغییر  مسیر پرواز های MQ-4   تریتون ، یکی از نتایج حملات ایران به اردن !
🔴
طی حملات گذشته ایران به پایگاه شاهزاده حسن واقع در اردن ، این پایگاه برای استقرار هواگرد هایی همچون MQ-4  تریتون ناامن شده و آمریکا دست به تغییر محل استقرار این هواگرد زده و آنها را به  پایگاه سیگونلا  سیسیل ایتالیا منتقل کرده !
🔴
تا قبل از این حملات ایران به پایگاه شاهزاده حسن ، پهپاد های تریتون از این پایگاه پرواز و بر فراز خلیج فارس گشت زنی میکردند و اطلاعات جمع آوری میکردند.
🔴
برای اولین بار پس یک هفته توقف در عملیات پهپاد تریتون ، این پهپاد از سیسیل ایتالیا به خلیج فارس برای جمع آوری اطلاعات برمیگردد. در نتیجه پرواز های بلند مدت این پهپاد و مسافت طولانی بین ایتالیا تا خلیج فارس ، باعث میشود که زمان جمع آوری اطلاعات در خلیج فارس کاهش یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/136010" target="_blank">📅 15:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136009">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccca6e59cf.mp4?token=PnNEY_dbF80PIrQY8w-nDxo9jb3kN3TrynnQQsCKXlSC4Iuqc7Sb2MYrs5LE6QbrWZBdCi3RHkvzhpgRfHIxwcRlc_EUJk72OpqH0GvkddClDqko9HnBSlMcyZ1X9lZE-zvLr7gtqoxkETj_8KiZZrY-n8vEpzppxmXLhki7O2_uO8gaK5Npe8-ypPbWdOoUv-i48qrXcKVEKQQ9VBfAxTIVgr_2dI0vIqCkkruY9-r3uGYu1N_oZIhM7IlgqP9P8qZLPmOQ8aDTK6kbxF1LGmEKNFgY_HU2t7QpDw3yV57Uqd9VzMV3p6WPOpVVaR_TyQzYUm59vDaeR-y4AeVNxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccca6e59cf.mp4?token=PnNEY_dbF80PIrQY8w-nDxo9jb3kN3TrynnQQsCKXlSC4Iuqc7Sb2MYrs5LE6QbrWZBdCi3RHkvzhpgRfHIxwcRlc_EUJk72OpqH0GvkddClDqko9HnBSlMcyZ1X9lZE-zvLr7gtqoxkETj_8KiZZrY-n8vEpzppxmXLhki7O2_uO8gaK5Npe8-ypPbWdOoUv-i48qrXcKVEKQQ9VBfAxTIVgr_2dI0vIqCkkruY9-r3uGYu1N_oZIhM7IlgqP9P8qZLPmOQ8aDTK6kbxF1LGmEKNFgY_HU2t7QpDw3yV57Uqd9VzMV3p6WPOpVVaR_TyQzYUm59vDaeR-y4AeVNxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پدیدار شدن و حرکت علنی زیردریایی هسته‌ای اسرائیلی در آب‌های تحت سیطره این دولت، شگفتی و نگرانی اسرائیلی‌ها از رویدادهای پیش رو را در پی داشته است.
🔴
موقعیت و تحرکات زیردرایی‌های اسرائیلی، محرمانه و غیرعلنی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/136009" target="_blank">📅 15:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136008">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
رویترز : یک منبع ارشد ایرانی می گوید که میانجی ها برای ایجاد فرصتی برای احیای توافق هسته ای موقت بین ایران و ایالات متحده، توقف 10 روزه حملات را پیشنهاد کرده اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/136008" target="_blank">📅 15:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136007">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_LKOxPZ2Vn76jWMhSwye0ck4jLTA9le69023hpcmulXUxj93NkqH3pPR8m-KHUKhNECHAGZGF8QhbHkTV9veqNaXczV3BDt8SRRaH_Tt5w7QhNTIcjsU2PtyzMnOMP8QLKENJc8Id-ms04MvwqzyeHHEGAJgrJEAM-TTSV58hA1SUlAvznnfXlaMz1UlZuGG3vunlwFIlqtroaF6tcMtuxH1NVAJTPzwrpXDeitk30F0tDfwyDGsRuPEGmfoXvh_jcPIL4Aj8SLggUhiHntIHZgP82BVP2criFaUw1Uj01TaI5gyo_KZLjCHvmLbnaC0EX4n0HmqbSmikb7MyLEmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اندی برنهام نخست وزیر جدید بریتانیا شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/136007" target="_blank">📅 15:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136006">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
وزارت امور خارجه چین: ما با حملاتی که هدف آن تأسیسات غیرنظامی در کشورهای خلیج فارس است، مخالفت می‌کنیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/136006" target="_blank">📅 15:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136005">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8728c0e607.mp4?token=OBlAeBRSlPvpXSWFyq3zY32qYiFFPGOaM9c0oCiAY1K70KXIG27dR_E385CxrFDa291hMPUrNicVhi1Ze7SvMVBbawonzAHVraxLWlM97CbJDcQBlsz3YbjiyjUg988j1JAqpiyHoDO0MWnT9XZtxFVntKKum3TWIQMzuSODRB5fblr2RJs0oMtLwSBqDW3CEIyZcfUTbIfLnZp2G4ec1WQPaOSY0O9nfEcn64LvuEfdMlsp-C_Mvsg6whiXxDk811OuQMqSERC9IcbBp93uMim8Y8hj-NxTpw2PsOG-42gYwQYjKuzNKGo1FrzKFWM20FUN2NVw3zd7dppqR46IJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8728c0e607.mp4?token=OBlAeBRSlPvpXSWFyq3zY32qYiFFPGOaM9c0oCiAY1K70KXIG27dR_E385CxrFDa291hMPUrNicVhi1Ze7SvMVBbawonzAHVraxLWlM97CbJDcQBlsz3YbjiyjUg988j1JAqpiyHoDO0MWnT9XZtxFVntKKum3TWIQMzuSODRB5fblr2RJs0oMtLwSBqDW3CEIyZcfUTbIfLnZp2G4ec1WQPaOSY0O9nfEcn64LvuEfdMlsp-C_Mvsg6whiXxDk811OuQMqSERC9IcbBp93uMim8Y8hj-NxTpw2PsOG-42gYwQYjKuzNKGo1FrzKFWM20FUN2NVw3zd7dppqR46IJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
یادی کنیم از درخواست کمک خمینی از آمریکا جهت مداخله نظامی و سرنگونی حکومت.
🤔
وطن پرستای الان هم، همین کارو کردن چرا ناراحتین پس؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/136005" target="_blank">📅 15:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136004">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkeNh5CNoGSjInFd5Q_10sUUCNl72wENpFR6hPc0G6-xfo6aTUaNjydQ4i69tDzgdGRtMpxRjNJcPvU67G96VSNEDdSgSynf8BUmtP-bOtFjCoM2L-vcNE6M2zk0ajFzekiaPxUAMiVwW1F2s0u92nOgnS7hsv-iTsR1sbrioOPDn8VGZMR9-ZQB4avu7zzNydNUO0QyEG9GbnUrTHyYsb82pjl3Jv2bJtHxGuCTnFRf8AyAAUoNlxUcsPVHIpNyY_t32yPIsDoF-zIpTo7qMp9aiLqfcu2PX8yCK0t_dCL_aNe-Qs0QG4cBYxr8ZsXQ3gBgr6ZSRd6Kc392TjNI3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: آمریکایی‌ها مدام تجهیزات نظامی جدید به منطقه می‌آورند و ادعا می‌کنند دنبال توقف جنگ‌اند
🔴
آمریکایی‌ها روی هوش ما اندازهٔ آی‌کیوی مختصر خودشان حساب کرده‌اند.
🔴
ما در شناخت این آمریکایی‌بازی‌ها به مرحلهٔ استاد تمامی رسیده‌ایم و بر این اساس آماده شده‌ایم. اقدامات باید مؤید ادعاها باشد نه ناقض آن‌ها.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/136004" target="_blank">📅 14:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136003">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxO_DDqnlXrcvWdRnkpBqsyhorJ_bDdGQBELBUPlADhOahuOz5QA4a-FCY_XWi2UcvPpxNMPpLvlW04jC4pqN6ol7PDAutVuu3o76ZMoMRba7c6Bge_f53qV6bHT4ZFupbAhwMA9wAEgnB3yYVNPwr7g4S5DkijS1PGDNiDClp2Io8hAh46Q1ctr0HsYoVAmdBaKMkDtGhSCjPPWXdS2qCgnhM96FuF5-DjVN34i2GqWYWGZXUKxXs94xdqeCR6nlh2P9YlXRgnt5TgfKQlH47m11qECoTBezdZ_-RUsR8wEWuG4dZm6Ee1PVb0uii18QXefhQJhNrUtNxHwrYJAbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ با انتشار این نظرسنجی مدعی شد که اکثر مردم آمریکا از توافق با ایران حمایت می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/136003" target="_blank">📅 14:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136002">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
پنتاگون هویت 2 نظامی کشته‌شده آمریکا در حمله ایران به اردن را اعلام کرد
🔴
وزارت جنگ آمریکا (پنتاگون) هویت دو نظامی آمریکایی که در حمله ایران به پایگاه هوایی موفق السلطی در اردن کشته شدند را اعلام کرد.
🔴
بر اساس این بیانیه، «تایلر جیمز فیهان» 25 ساله و «ایزابلا گونزالس» 19 ساله در جریان حمله روز جمعه کشته شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/136002" target="_blank">📅 14:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136001">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
اداره هواپیمایی غیرنظامی بحرین اعلام کرد که پهپادهای ایرانی، سامانه‌های ناوبری هوایی غیرنظامی این کشور را هدف قرار داده‌اند، اما این حمله، فعالیت‌های ترافیک هوایی را مختل نکرده است.
🔴
این اداره اعلام کرد که این پهپادها، تجهیزات ناوبری هوایی را در منطقه اطلاعات پروازی بحرین هدف قرار داده‌اند و افزود که مقامات، بلافاصله و مطابق با رویه‌های عملیاتی و امنیتی، به این موضوع واکنش نشان دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/136001" target="_blank">📅 14:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136000">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
مقام آمریکایی به سی‌بی‌اس:
تشدید تنش به زودی آغاز خواهد شد،
هواپیماهای ترابری و سوخت رسان آمریکایی به صورت پی در پی و بی سابقه در حال ورود به خاورمیانه می‌باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/136000" target="_blank">📅 14:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135999">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
ایلی کوهن، عضو کابینه امنیتی اسرائیل: اگر ایران بار دیگر به ما حمله کند، پاسخ اسرائیل از واکنشی که در رویارویی اخیر شاهد بودیم، شدیدتر خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/135999" target="_blank">📅 14:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135998">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7cdf507a0.mp4?token=L9jQO4zix5WvjOPW1I6OfwqeTkRrynD0ALHlhiu8-eY3SugH24dGYlE9oGJbV51f7zOS1Tlacn5esrk4Mxd6EUIJGMmW5lbBkup_B_vDme8GjWlpXUyEmYohH21mafAlDKGuyifPwimD1BkDmTodw310hDMdWrqr1hmcD8_uvpU9JH0HjrMHxAEcY2ZG6IvznCaAMZbKyf9ym95KPzliremxJ0okCIPWMq8bzsu8RjpfaBe4pfXkK61R14kYnDxSC2nTxKGf7H0UK2o_lv8fXMz7ovJE8MTKCv0d12LXL1L1xYgqj1YQEWIuWxBeBhk0J6P_Yn6ENxhvGzk7UXWf_jA46a6Iprqvxo_6eIhMzKuyf9KXsmeuEi7pUbAi8qISaxw90iVs6vXPlzQgFKSAi8ro2cxCpGpVoxNiDvA8Mpln9UC6hZ8tvGy4dIGv6YMg7VSB6tGtnHLJe9-pvicW9Mgkdy7BgP_CpteisZ36H4IGolF7Adk04hcb2cAlIHLpxPpFrIw4r846ItpC85jWpw6xRWb6Y3wtV3gyV6MiPtk470sHiELaxWbKMP9Cu2fN6NoisfGGmydsZwqQv7ofdwYiRA9vKdfbbjz0cYO8aSBVqLrY6K5ptBD20Gu9WP2aWswzAO_zxddNnfKsqt6k3rIYUZThEmTWjZBJ3JMl53M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7cdf507a0.mp4?token=L9jQO4zix5WvjOPW1I6OfwqeTkRrynD0ALHlhiu8-eY3SugH24dGYlE9oGJbV51f7zOS1Tlacn5esrk4Mxd6EUIJGMmW5lbBkup_B_vDme8GjWlpXUyEmYohH21mafAlDKGuyifPwimD1BkDmTodw310hDMdWrqr1hmcD8_uvpU9JH0HjrMHxAEcY2ZG6IvznCaAMZbKyf9ym95KPzliremxJ0okCIPWMq8bzsu8RjpfaBe4pfXkK61R14kYnDxSC2nTxKGf7H0UK2o_lv8fXMz7ovJE8MTKCv0d12LXL1L1xYgqj1YQEWIuWxBeBhk0J6P_Yn6ENxhvGzk7UXWf_jA46a6Iprqvxo_6eIhMzKuyf9KXsmeuEi7pUbAi8qISaxw90iVs6vXPlzQgFKSAi8ro2cxCpGpVoxNiDvA8Mpln9UC6hZ8tvGy4dIGv6YMg7VSB6tGtnHLJe9-pvicW9Mgkdy7BgP_CpteisZ36H4IGolF7Adk04hcb2cAlIHLpxPpFrIw4r846ItpC85jWpw6xRWb6Y3wtV3gyV6MiPtk470sHiELaxWbKMP9Cu2fN6NoisfGGmydsZwqQv7ofdwYiRA9vKdfbbjz0cYO8aSBVqLrY6K5ptBD20Gu9WP2aWswzAO_zxddNnfKsqt6k3rIYUZThEmTWjZBJ3JMl53M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزارت امور خارجه چین: تایوان، بخشی جدایی‌ناپذیر از خاک چین است. این، اجماع غالب در جامعه بین‌المللی است.
🔴
پیام ما به مقامات حزب دموکراتیک پیشرو (DPP) کاملاً واضح است: روند تاریخی غیرقابل توقف است و استقلال تایوان، راهی به بن‌بست است.
🔴
تلاش‌های مردم چین برای مقابله با جدایی‌طلبی و استقلال‌خواهی در تایوان و دستیابی به وحدت ملی، روز به روز درک و حمایت بیشتری را به دست خواهد آورد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/135998" target="_blank">📅 14:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135997">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
موگویی: «ترامپ درباره مشهد درست گفته بود، مشهد سقوط کرده بود.»
🔴
یادتونه ترامپ اون شب چی توییت کرده بود: یک میلیون نفر در مشهد تظاهرات کردند!
🔴
یک میلیون نفر در یک شب فقط در مشهد  اومدن بیرون، جمهوری اسلامی قتل عامشون کرد و هنوز داره تک به تک جوون‌ها رو اعدام،…</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/135997" target="_blank">📅 14:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135996">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
وزارت خارجه کره جنوبی به بازدیدکنندگان کوتاه‌مدت توصیه کرد «فوراً» خاورمیانه را ترک کنند، «مگر آنکه دلایل قانع‌کننده‌ای برای ماندن داشته باشند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/135996" target="_blank">📅 14:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135995">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
بقائی: حقوق حاکمیتی ایران بر تنگه هرمز غیرقابل‌مذاکره است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/135995" target="_blank">📅 14:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135994">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0792b06244.mp4?token=iG3bQjljLOTVy0H6rbERPbs5FJkgcpAgUTrk8tsJ3a36L1ogiEIHR8jlyCdfeASvcBMMCKB_cTzTjikYT7eJZjRr4LFdoPgazIeFkHAPa2nbdosviaDjR8HyxtTjNoVMzbtR5F-iv1kkbt-uo1b6cbP04b8lGbdh2GGdpygBVqKQ-BEp6EbHiRgbn6zXn9AIpyMshV2KM2USZ3FVd5JN7_MbFQ_Hq1WvsCa6KPUHwAcpr_8PU1KirY8hL5K1dRDta4JGBmo6ze2h8bcxiwRLPau7xAEXk6ASn7DQxuhx6szt3PX_AAeB5NDweoORqLzmRWlL2ZQL9YpbzzCFluv9Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0792b06244.mp4?token=iG3bQjljLOTVy0H6rbERPbs5FJkgcpAgUTrk8tsJ3a36L1ogiEIHR8jlyCdfeASvcBMMCKB_cTzTjikYT7eJZjRr4LFdoPgazIeFkHAPa2nbdosviaDjR8HyxtTjNoVMzbtR5F-iv1kkbt-uo1b6cbP04b8lGbdh2GGdpygBVqKQ-BEp6EbHiRgbn6zXn9AIpyMshV2KM2USZ3FVd5JN7_MbFQ_Hq1WvsCa6KPUHwAcpr_8PU1KirY8hL5K1dRDta4JGBmo6ze2h8bcxiwRLPau7xAEXk6ASn7DQxuhx6szt3PX_AAeB5NDweoORqLzmRWlL2ZQL9YpbzzCFluv9Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک پهپاد اوکراینی بامداد امروز به ساختمانی در شهر مسکو، پایتخت روسیه، اصابت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/135994" target="_blank">📅 14:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135993">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m31Ah6JeKuDZvfxuHirIHax4ahOPjJlrEHfSmcAfrpqRVx8e-WRB6vyplI9zZATFFRy7PtLCsPOhrskgdOkNyDFrCrpxkK_eTyVaixgWlUww8yWdezhsJX3I3O_5uVE5eI4DOLcWvqGtP9Kg-uMaeC56OZmZMc7EDPHOtWYX3jmYbq8s8UZFMLmq3IA2F24qKjxalEEwW2bEXKJHuCAiSqN5qwyisgoC5QQjQ-idsyN-KoDm7rrbwRy_sVPAFQqTTbH3cxWViWSo7R4-Ao1zQqhytvrotnumC3vjReqcIsocujEwjau22hKAHwTq-5EweVI3h8S_e2q10Wvej8oauw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پادشاه چارلز سوم، استعفای کیر استارمر را به عنوان نخست‌وزیر در کاخ باکینگهام پذیرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/135993" target="_blank">📅 14:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135992">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0b2fcbad5.mp4?token=IlEFieB-3yAgDwHFcn116XfKL2aMIGe26lMOFgWzIzjvCY92Cdb2dhN2A97JXR09-AtipErT3mTWQrRLP6lrp0X-rnZOIPIx-hLsuK-BWIsXngs3e67lVOQQZ3hXYND1n6sb1QM52n6hWVrwyL7PCJ3Y3s015brzipOxLOVD53G18rN1d68h9klckhdrIoeHOwYEMRkHtbBcC4HRngsfYiW7PVtvVYFJHNG3C7NIqQvZsw3yPlvOL6N754ZRIJXljLLaTg2EdITjrelfNRfzBOEe8GZ85oY60xnQfOJrl0sigXz2D3baz-hDLl_kBGxr9pg4aJDYRjkyUwHIz842DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0b2fcbad5.mp4?token=IlEFieB-3yAgDwHFcn116XfKL2aMIGe26lMOFgWzIzjvCY92Cdb2dhN2A97JXR09-AtipErT3mTWQrRLP6lrp0X-rnZOIPIx-hLsuK-BWIsXngs3e67lVOQQZ3hXYND1n6sb1QM52n6hWVrwyL7PCJ3Y3s015brzipOxLOVD53G18rN1d68h9klckhdrIoeHOwYEMRkHtbBcC4HRngsfYiW7PVtvVYFJHNG3C7NIqQvZsw3yPlvOL6N754ZRIJXljLLaTg2EdITjrelfNRfzBOEe8GZ85oY60xnQfOJrl0sigXz2D3baz-hDLl_kBGxr9pg4aJDYRjkyUwHIz842DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ایزاک هرزوگ، رئیس‌جمهور اسرائیل:
ما نوادگان پادشاه داوود هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/135992" target="_blank">📅 14:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135990">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e1ddfa795.mp4?token=JsNeMczEXNg4ppQYoJwsasIAsdjCvDBykDMM1KFoqGQVsBJaB7Xn6_zDLjVNsTo2vCcw_jM3TgJKHfNikiFGkfs8w2gzQhmXdchXFqG-OUTiVP0tsBPLx92LkUJoC5pKrpwXQG-SXjj9j0YN3gluAFL6YVIKIlmbdo5BG5KBSPmk3M4FbXfJOHCYDgwzNmdrW_J-c8GQx6nF0PTUyuHn5e88FdOH5ZRoRPkkHEIPpCRSH53amVUkXA_nagzqmE_cCAD2aLads-kNXRDfmseFvzCMbUO3w3CwO4jDs4JCWzvmWFnlc_kDSMJSM2CfugIQlxeoJLTp0B-1c2FaYi4cUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e1ddfa795.mp4?token=JsNeMczEXNg4ppQYoJwsasIAsdjCvDBykDMM1KFoqGQVsBJaB7Xn6_zDLjVNsTo2vCcw_jM3TgJKHfNikiFGkfs8w2gzQhmXdchXFqG-OUTiVP0tsBPLx92LkUJoC5pKrpwXQG-SXjj9j0YN3gluAFL6YVIKIlmbdo5BG5KBSPmk3M4FbXfJOHCYDgwzNmdrW_J-c8GQx6nF0PTUyuHn5e88FdOH5ZRoRPkkHEIPpCRSH53amVUkXA_nagzqmE_cCAD2aLads-kNXRDfmseFvzCMbUO3w3CwO4jDs4JCWzvmWFnlc_kDSMJSM2CfugIQlxeoJLTp0B-1c2FaYi4cUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دقایقی پیش، یک پهپاد اسرائیلی به یک خودرو در شهر غزه حمله کرد.
🔴
گزارش شده است که حداقل ۱۴ نفر مجروح شده‌اند و برخی از آن‌ها در وضعیت وخیمی به سر می‌برند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/135990" target="_blank">📅 14:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135989">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca140d784d.mp4?token=edepPKHo5kaYgcyOTbzovtQKr58lokpXv5eNRq4EhiGv1D1UFenVN8xKdQUtJtKsKhHnIPu8_poesgUC7rvUiuZm4XqGWSGI9v4czyHrlpLv-H5UtRvM5SLPE0K_EMFL8RjLCzCMoGjGuwXgSsvYiKOlMsfuaiuaO1uZW1E3aVaj0rHDc5EQw3N8vJZ2AMoecCP04JX0hGxIBXL6AEOqFtxTsetwxNhabTegWMYVz9CuWAYUdgGpWpmawXjtmSZ6Kh1zPo3EEzfGcxCwuki7BtWPOWcyvO7Axx4JHDDk87acn23X4tFqFZhESb8uUByTmdfqjLa-RziYwxaOp-uckna07DDD7VbrC6JmnFlYhf6AEW1C-t2GAi8eUL0jdLGOvaAz1oeNqAVsbwZ_XeyqpOP_-VM-qG2qyj6DMilZqLQH61OfgWaD4KoX4_CrhcMsaVYS5mxSoOHeIKu0QdZV79GXuS4Ov-YfA8ztn6-Rw08VwD2dUOFoNIFFtXCA73Xb8lZ7eTCFZDJuXjslc0WyfpVSbzLjdawlDh8-cbpE4TL3B7nM24Y6KzBZImkQyiIkWU0-rTtfOkxdJ22ycge2tIQ_pf8g7ZNKe4wsq3cEUFOKmBDIKi8U4jL7GsMulP33R4vtISrYXJIiLwYsN46EEN5-PcpUUX6QmZcuXouV_Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca140d784d.mp4?token=edepPKHo5kaYgcyOTbzovtQKr58lokpXv5eNRq4EhiGv1D1UFenVN8xKdQUtJtKsKhHnIPu8_poesgUC7rvUiuZm4XqGWSGI9v4czyHrlpLv-H5UtRvM5SLPE0K_EMFL8RjLCzCMoGjGuwXgSsvYiKOlMsfuaiuaO1uZW1E3aVaj0rHDc5EQw3N8vJZ2AMoecCP04JX0hGxIBXL6AEOqFtxTsetwxNhabTegWMYVz9CuWAYUdgGpWpmawXjtmSZ6Kh1zPo3EEzfGcxCwuki7BtWPOWcyvO7Axx4JHDDk87acn23X4tFqFZhESb8uUByTmdfqjLa-RziYwxaOp-uckna07DDD7VbrC6JmnFlYhf6AEW1C-t2GAi8eUL0jdLGOvaAz1oeNqAVsbwZ_XeyqpOP_-VM-qG2qyj6DMilZqLQH61OfgWaD4KoX4_CrhcMsaVYS5mxSoOHeIKu0QdZV79GXuS4Ov-YfA8ztn6-Rw08VwD2dUOFoNIFFtXCA73Xb8lZ7eTCFZDJuXjslc0WyfpVSbzLjdawlDh8-cbpE4TL3B7nM24Y6KzBZImkQyiIkWU0-rTtfOkxdJ22ycge2tIQ_pf8g7ZNKe4wsq3cEUFOKmBDIKi8U4jL7GsMulP33R4vtISrYXJIiLwYsN46EEN5-PcpUUX6QmZcuXouV_Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که یک ستون دود غلیظ از بندر الاحمدی در کویت به هوا برآمده است، این اتفاق پس از حملات اخیر رخ داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/135989" target="_blank">📅 14:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135986">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AVUycls9NIDyFXIVLMl86HhTkwPIQZ7wx_f-5vRUprJ54BR2fsuqms4eLBN4DZZwXpzi6MZXTgY_0Cyj0O8dVaVfKPeh07L9LiyiQhjUwBVZK5g6Rh6hhwceS83uAx7J50h250quPNoRUhP4PSmSgcHkLuI-6QH3e_afR50oHlbT1hk2B--TjwVF5_aKwKLb6S7-CJ6kK_RM3hQVb9sANTLTvzvuxvxCpxMSuyVLgZM8iv9XHu5a8rRmjTuo37LSGjUIH8VupdrLCwz3W4T529lCAh-IBKuUQMZHanKlOPXDchjoAWaiGd1urLGkQKyCcldh2znS6klrw2nXqcqRIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iW78NF03Eb18nn6-gp-t7XDiGr42NA_cRXuZ-J2dljTcTj0utiWsk6zG_w_44r8mLHd7XeFPeaiR593VD8XHzWqz3IWE4kXfnDcMajvgeC0EwzlaDm_VBwqJYFEN37UnF12ypnk6iAErE9T6-34PJishorF_t2Si2_bTgYLZsU2EfpyIQvG6OI2KB-Z1MFEKQxTuzeE_0TkE792LpI60v5nT1dMQ4yykYP6DTJ2yeCyFcz4hr4pVDxWEN077znHschXR1KOcN8sIuL10YQSdy3xP2r1FKBh-kZcV-ZnEJdQEDcNoampbCwPcPJivAE5VyeZibk040YBVe29LyJIY8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B33nsMJ6ZrxMgS9HEE_1i9WeXNMmUwcFyWxxVlHjWxPBDhGfVAjAcGFTlX-ddT1wEAhO0_phymGyfLo7UkJUbSIN6cNKQWyXDG1Sq1is4AHrIYFN076A2TT_E3OCBaMWwtyykHS-7_iN8R_s9yD2bbv3reJ0IazGRW9h5o8V6Fe4GELESI4qtIGWZ6gdcz7t07UdZnbhZbqPN5dorvCJ81fq-v1drqE6dw54Ceb934kbIGTnvZtFZtum5mSMc-xC81i-qefYPDBv2OH7Ik4nZ1pf1i8JbB2GlMeMxu9NRKbEs6PKQl-dx3xg3IZwLdse0Xf9l68oMXR-ySmBzoyFKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر جدیدی که توسط ماهواره‌ها گرفته شده، ویرانی‌های گسترده‌ای را در پایگاه "الأزرق" در اردن نشان می‌دهد. در این تصاویر، تخریب محل‌های اقامت سربازان آمریکایی، به همراه انبارها و محل‌های نگهداری هواپیماها، به وضوح قابل مشاهده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/135986" target="_blank">📅 14:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135985">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e93c584a72.mp4?token=Ynvwj_6xz-UjdYHVKdha0pylTByLdWTD6IuK0cpbHhN8tzvDVuQXo_KLoune6JB5aTePKgxgogvoMTP5GhPG3szy9u2alBUop89a6XFTHKGBSlViN-Ya4pL6P5-LzqGSXwTSvuxDuksxuDibav32UcwsYzKS9aPTXE-2Pta9hgOEg3N9yLRu4dX5tapGNrENveCN6yRygvYJo51ZpHPifCsfE7NI_ELYlK14sSiq9mfTYF87xgldXZa5Yja0VucfZV5HqVV-b0OPVuxtHQWr9YQyRpp_HtFe5nhUnAJycEaHIzWj8FOf5YpWqiP18zXGi8HgcDzaDyeueMtPSYjRNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e93c584a72.mp4?token=Ynvwj_6xz-UjdYHVKdha0pylTByLdWTD6IuK0cpbHhN8tzvDVuQXo_KLoune6JB5aTePKgxgogvoMTP5GhPG3szy9u2alBUop89a6XFTHKGBSlViN-Ya4pL6P5-LzqGSXwTSvuxDuksxuDibav32UcwsYzKS9aPTXE-2Pta9hgOEg3N9yLRu4dX5tapGNrENveCN6yRygvYJo51ZpHPifCsfE7NI_ELYlK14sSiq9mfTYF87xgldXZa5Yja0VucfZV5HqVV-b0OPVuxtHQWr9YQyRpp_HtFe5nhUnAJycEaHIzWj8FOf5YpWqiP18zXGi8HgcDzaDyeueMtPSYjRNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این روزها که شرایط جنگیه و پدافندا هم تو اکثریت مواقع  کار نمیکنن؛
پیشنهاد میکنم این ویدیو رو یه گوشه‌ای ذخیره کنید، بعداً حتما یه جایی به کارتون میاد :
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/135985" target="_blank">📅 14:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135984">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hh7Qw89i_dZIsQz3AxnghPSPd2_kc799KTb5KQ-mOlrPHKP7Hj7hoo8hZ9taeG1z3jmnmaaYl6Bqmv-4_lNuPP-vwRQdVaW3QAiCiKRHd-fwLNmwIYCeiQM46mCMMptpk76NjN4lgeSIXpdi0yw-QnW_KYDPX3LTBWtP5WGdpA2BV6MTLeYJaDhX_kiJhC3ybjzrNrbnCOWe9GI7Fc247bigs2_bbdttaLFAkB7-bY4ys0vNvmS9HNHeHNGsF-Kj6_ij1akqW_nBeC1wiqe7uxEcRp6420gFcgFjBALhO1FbtwLprsqy0Mb8M8v9SvN5pKqdK4xAduXkEdYLV5XMEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
فیروز کریمی :
میمیک صورت مسی رو ببینید داره الکی گریه میکنه چون دید رونالدو گریه کرد و وایرال شد اونم همینکارو کرد !!
@AloSport</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/135984" target="_blank">📅 14:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135982">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SrHpnVquIcq09ldEOXdkJASBE6pCJoyBNFHZWZyyItKIsF4aWbogtwr3iDZAaaeutVKzebvgvNbkBkl9OmunQtWAF6FddB-mV4yDb49EbkMJBh02u1gd1MQXLzWQWhVQXawWlHZ1zJ_3bcOn5dkQhH9oKjEEDLWhWOzrayMnjeT0v8h7C4SKiw7url8zyvn1Z_msc9KSDOjrWLjvbyXzFKXAZlG2yksdrs30RWKMSTmQrP0NDvUM_JBuROTBHwYBFy90IqdUf4GOfkKNi83M4BL2esaDhCCHDFisGKvwa73IhGdhAJK_z0P9Uswez3gFSnw-dhVGRxZm3p5GAnLIsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vBmMLcI0U9bW7ZHpqcK-N2trnquh_vrD0bQjjg8CFutpjpZreiNsiNNzUkwV6wS8uYxd939PHbVIYvtuOdu3YW121UdvxrgkfdvRJsit-Gtz9pisNxs4ntzNOB3eN9fVAAqwJPX-9hIxeKFZ04prQ5hTuEWakTTkuLOgUuuf_-qTwm1PRU8J20Gr3IKLe0BgQd0baJq3_BGJ343FoNnFBO0sU6JWGEkCrrfzV62rK98WCQ2Xs2YP5AHAJZNYptG6T8nDhJkJyOexWuLsg6eEqEbz_dGPK9Ge9_lbCKGEy7-zoJfetjy5cSX3DO609cylSP-JB5hrTYewYAORewV5Kg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
کامران غضنفری با شکایت حسن روحانی به حبس محکوم شد!
🔴
دادگاه بدوی کامران غضنفری، نماینده مجلس را بابت هریک از دو عنوان توهین و افترا به پرداخت پانصد میلیون و یک ریال جزای نقدی و بابت نشر اکاذیب رایانه‌ای به سیزده ماه و شانزده روز حبس تعزیری محکوم کرده بود. دادگاه تجدیدنظر اعتراض متهم را مؤثر ندانست و حکم را عیناً تأیید کرد. این رأی قطعی است و مجازات اشد قابلیت اجرا دارد.
🔴
کامران غضنفری، حسن روحانی را به «جاسوسی برایMI۶»، « ارتباط با سرویس‌های خارجی»، «داشتن تابعیت انگلیسی» و «افساد فی‌الارض» متهم کرده بود. دفاع او این بود که مطالب مطرح‌شده را از برخی اعضای کمیسیون امنیت ملی مجلس یا گزارش‌های مربوط به مسئولان دوتابعیتی شنیده و ردصلاحیت روحانی در انتخابات مجلس خبرگان نیز مؤید ادعاهای اوست.
🔴
دادگاه این دفاع را نپذیرفت و تصریح کرد که هیچ‌یک از این انتساب‌ها در مراجع رسمی و قانونی به اثبات نرسیده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/135982" target="_blank">📅 14:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135981">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1232873fbd.mp4?token=EtqaW0iS2Fnv5FGi-et-oV1AWIBGRB7NkAFQrk4hJdYguGj1oopyTaC6Xbth1VQNLoJfScnAe4fW4oBsAU7Hk2gc-4yhGkpRmQEG59-TSjKlPSTcNJKbyBiRc028s9K-5qiYLz8unu_X2RJPzA_LLbjugUdnJnhB_ySIt6eHo_M3E4uppwVIwUxivnutSbzQi-EIgJTSvRSP58_xpxsdvqfsQy01Mni0RF-wqA_T0yMFiAMjlP5GXwMpqFD1InhD7WgCcrcA4N3cp0OKJX1EyVoX5B1pqBduIH3JLkDlgibT_VFsI7mx-26dLRaMsO3qOzebjEIzvTUU2JS0pWcCYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1232873fbd.mp4?token=EtqaW0iS2Fnv5FGi-et-oV1AWIBGRB7NkAFQrk4hJdYguGj1oopyTaC6Xbth1VQNLoJfScnAe4fW4oBsAU7Hk2gc-4yhGkpRmQEG59-TSjKlPSTcNJKbyBiRc028s9K-5qiYLz8unu_X2RJPzA_LLbjugUdnJnhB_ySIt6eHo_M3E4uppwVIwUxivnutSbzQi-EIgJTSvRSP58_xpxsdvqfsQy01Mni0RF-wqA_T0yMFiAMjlP5GXwMpqFD1InhD7WgCcrcA4N3cp0OKJX1EyVoX5B1pqBduIH3JLkDlgibT_VFsI7mx-26dLRaMsO3qOzebjEIzvTUU2JS0pWcCYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بندرعباس - دی ماه ١۴٠۴، حرومزاده های حکومتی که جلوی چشم بچه به پدرش حمله میکنن!
🤔
بعد مارو از نیروهای خارجی میترسونن. نیروی خارجی با مردم معترض کاری نداره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/135981" target="_blank">📅 14:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135980">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
پزشکیان: درست نیست افرادی که هیچ مسئولیت اجرایی و نقشی در مدیریت مستقیم امور ندارند، خارج از فرآیند تصمیم‌گیری صرفاً بگویند که باید به شکل دیگری عمل می‌شد. طبیعی است اگر همه واقعیت‌ها و محدودیت‌های موجود بیان شود، بسیاری از این قضاوت‌ها نیز تغییر خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/135980" target="_blank">📅 14:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135979">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
پزشکیان: امروز در شرایط جنگی قرار داریم و اداره کشور با همان قواعد و رویه‌های معمول گذشته امکان‌پذیر نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/135979" target="_blank">📅 14:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135978">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
پزشکیان: زمانی که تصمیم می‌گیریم در برابر دشمن ایستادگی و مقاومت کنیم، باید پیامدهای این تصمیم را نیز بپذیریم و نمی‌توان انتظار داشت که در شرایط جنگ، جامعه با هیچ‌گونه دشواری مواجه نشود
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/135978" target="_blank">📅 14:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135977">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
پزشکیان: فشارهای اقتصادی می‌تواند به دستاوردهای نظامی ما آسیب بزند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/135977" target="_blank">📅 14:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135976">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
پزشکیان: از هیچ‌یک از بندهای ۱۴ ‌گانه عقب‌نشینی نکردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/135976" target="_blank">📅 14:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135975">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
پزشکیان: امروز بیش از هر زمان دیگری به وحدت، همدلی، تصمیم‌گیری مبتنی بر خرد جمعی و همراهی همه ارکان کشور نیاز داریم و دولت نیز با بهره‌گیری از همه ظرفیت‌ها، اصلاح ساختارهای ناعادلانه و خدمت به مردم را با جدیت دنبال خواهد کرد.
🔴
پزشکیان با اشاره به مسیر دیپلماسی و توافقات انجام‌شده: برخی بدون توجه به واقعیات، مطالبی را مطرح می‌کنند که از اساس مبنای درستی ندارد. گاهی نیز ترجیح می‌دهیم پاسخی به این اظهارات ندهیم، زیرا بسیاری از این سخنان با واقعیت‌های موجود فاصله دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/135975" target="_blank">📅 14:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135974">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/859193bada.mp4?token=JojL1lwNQXUxV3f5_itf4e6pTSANNor87dhnTEIv0RCGfXNvJpJknAwoO_JXGVWbpIvibSvFMcE-JiLW3CYOGYht_dOz-33V7dQe52Ktco6k_w9P_QRzogex7N5ezG3wFAl1elx-qaN6_HkBOiP9YvRtTqpOwZogwu8kFtw9uT2jpsIXu091624BgPmWTHcKy8i8b8qAjZzLNnteZQO2K4hplruCEFhDdtpDtCwKDP_3wmNme1T1Yr5tdRbSyhbHq7NIN-GbvKkiUvMHplzVQ_lWLor3bUggCQ2l4kRvbIFFZTu5920HnQGLbfg6mdkZMT8jjjlmgkS23BiRLIdBuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/859193bada.mp4?token=JojL1lwNQXUxV3f5_itf4e6pTSANNor87dhnTEIv0RCGfXNvJpJknAwoO_JXGVWbpIvibSvFMcE-JiLW3CYOGYht_dOz-33V7dQe52Ktco6k_w9P_QRzogex7N5ezG3wFAl1elx-qaN6_HkBOiP9YvRtTqpOwZogwu8kFtw9uT2jpsIXu091624BgPmWTHcKy8i8b8qAjZzLNnteZQO2K4hplruCEFhDdtpDtCwKDP_3wmNme1T1Yr5tdRbSyhbHq7NIN-GbvKkiUvMHplzVQ_lWLor3bUggCQ2l4kRvbIFFZTu5920HnQGLbfg6mdkZMT8jjjlmgkS23BiRLIdBuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کیِر استارمر : من برای اندی برنهام آرزوی موفقیت دارم. او از حمایت کامل من برخوردار است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/135974" target="_blank">📅 14:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135973">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/494c3c2054.mp4?token=PZetjf2MpKeS-zYavTOk3aLw6tXzX5EO7jbcob0dvYwrP3HoX3Y70slqh0syDl7TGIqW3bsRwWKiotYtXVJ_aIgDAJQ0-RzWw8fcUH8TQIemjIdK2hE64fw17mAb_QmSxhbxQ5nFvQIPQz3QLMg9oEf6UDoiFDa7E5BI6cLBjaFZkjSqAyKKHoKkFENKiXBIz6I8Ux5lEnA0ANo1k93d9jdeIVGDAqouZPKMPk6C8mva9ebJ3_yNz2v_C-3B4BNPPjybKKY_ieu0cNCJWvNSfG8FtpbDw7LuxOhjzRKaCX31rW4kk1IgBLDvG4Iv3oa3DE0txmToRv2e9UCX1E-Cxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/494c3c2054.mp4?token=PZetjf2MpKeS-zYavTOk3aLw6tXzX5EO7jbcob0dvYwrP3HoX3Y70slqh0syDl7TGIqW3bsRwWKiotYtXVJ_aIgDAJQ0-RzWw8fcUH8TQIemjIdK2hE64fw17mAb_QmSxhbxQ5nFvQIPQz3QLMg9oEf6UDoiFDa7E5BI6cLBjaFZkjSqAyKKHoKkFENKiXBIz6I8Ux5lEnA0ANo1k93d9jdeIVGDAqouZPKMPk6C8mva9ebJ3_yNz2v_C-3B4BNPPjybKKY_ieu0cNCJWvNSfG8FtpbDw7LuxOhjzRKaCX31rW4kk1IgBLDvG4Iv3oa3DE0txmToRv2e9UCX1E-Cxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کیِر استارمر، نخست‌وزیر بریتانیا (در حال ترک سمت): من با آرامش، با لبخند و با افتخار از دستاوردهایی که به دست آورده‌ایم، این سمت را ترک می‌کنم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/135973" target="_blank">📅 13:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135972">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
فوری / الحدث اعلام کرد که هواپیمای نتانیاهو حریم هوایی اسرائیل را به مقصد نامعلوم ترک کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/135972" target="_blank">📅 13:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135971">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
وزارت بهداشت جمهوری دموکراتیک کنگو اعلام کرد شمار جان‌باختگان ناشی از شیوع ویروس ابولا در این کشور به ۹۳۰ نفر رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/135971" target="_blank">📅 13:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135970">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXgc6BJdY33FtxUh3_Pivm0wy5hjpb37s4VL4UKbppWZsCBzIN08FzmTu24dAYAqO16j6BFKAhjFfLd72oOrJ7e22VjcXaa68HWqc9NwhGp0FKzfgAm0Tcfv_QOYMsH8tYo-HazoXeZFdEg7kYJAMTjkTQn1A_OownRNtDQG00em-C2C0QWl18uYga6pHs-43dLMdzc9JnoS1V4sLFsDKL3cHq3m9MA80iTPybUG50GzaFpeD59RNp-qQPioQZE32_utt6dsDAGrnPevjhbn2301ru6o_6XxSPQtWpU7S04lRtQIz42Jfj-ALz6mN_9jsjKI8qgsKn0EV4opESaU5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از چهره مسی هنگام دست دادن با ترامپ که در فضای مجازی وایرال شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/135970" target="_blank">📅 13:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135969">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0116054239.mp4?token=Jh7NtsHcBa6C4LRsdYQ2qY2Si-ljJNiJqu8TA4A5hUttaiDy7iqnMsg1R6iyTBqKIc0gFxqop08lI3f245nqnBq3HX4mDqFd3qzuvCShygRrrcThVMIEySTMOSbTWZgkqhsRLKw2x9cFwJRPdZNqW7QWN-utaEktNiAj_B6Qdr_IW6o1WVPisFl4hiPVSIhFWNvdtMMN_6B14y40s80VbfQOdurzGcz8WJhqQjDsJemafh9m9REBMlcjyd3MgHFUxkiyQtXYT3TKP-ABulJ0HuEqH72SWuSfbzWOLQOwpaG66HfumbwaTZGH1o0me_ycALs_fDb--WBOZu01hUADag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0116054239.mp4?token=Jh7NtsHcBa6C4LRsdYQ2qY2Si-ljJNiJqu8TA4A5hUttaiDy7iqnMsg1R6iyTBqKIc0gFxqop08lI3f245nqnBq3HX4mDqFd3qzuvCShygRrrcThVMIEySTMOSbTWZgkqhsRLKw2x9cFwJRPdZNqW7QWN-utaEktNiAj_B6Qdr_IW6o1WVPisFl4hiPVSIhFWNvdtMMN_6B14y40s80VbfQOdurzGcz8WJhqQjDsJemafh9m9REBMlcjyd3MgHFUxkiyQtXYT3TKP-ABulJ0HuEqH72SWuSfbzWOLQOwpaG66HfumbwaTZGH1o0me_ycALs_fDb--WBOZu01hUADag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
همتی: ادامه فعالیت بانک ها ناسالم و ناتراز را تحمل نمی کنیم/ مهم‌ترین ماموریتی که برای همکارانم در بانک مرکزی تعریف کردم، کنترل ناترازی بانک‌هاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/135969" target="_blank">📅 13:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135968">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a594ec6809.mp4?token=ZGaI1_J7BC3F5ZXnjDmA_uVwHx4mtL_HAwvZYUV8OHSzCmhZpbk4h_0nGsc7-Iy1XQ3TkPFAy64K5_rrI_DfRIFgUknME8tIg-R5at0DgtH-Z42dp-G369VlV6a27mad3cQsDsFQQpWFVdangGKqwcasVyk0KEFBvpoP5HexZyyZM8CpivvlQaO3ICqtDqjN4e6EiGWnNuSJ2lInZx9dumlu1VeBSsIu0xAp1r2P-77uQsUg76Ctw9TSK9ZryS7wUHNme7Uj1hrZRwTCQJqkWBcX3PU6s_mAnbNlUmL2M3uMg86a4lCzNof_N4AMP4_t5CmXaVwx3OHGjULge4S2PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a594ec6809.mp4?token=ZGaI1_J7BC3F5ZXnjDmA_uVwHx4mtL_HAwvZYUV8OHSzCmhZpbk4h_0nGsc7-Iy1XQ3TkPFAy64K5_rrI_DfRIFgUknME8tIg-R5at0DgtH-Z42dp-G369VlV6a27mad3cQsDsFQQpWFVdangGKqwcasVyk0KEFBvpoP5HexZyyZM8CpivvlQaO3ICqtDqjN4e6EiGWnNuSJ2lInZx9dumlu1VeBSsIu0xAp1r2P-77uQsUg76Ctw9TSK9ZryS7wUHNme7Uj1hrZRwTCQJqkWBcX3PU6s_mAnbNlUmL2M3uMg86a4lCzNof_N4AMP4_t5CmXaVwx3OHGjULge4S2PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
همتی: اجازه اضافه‌برداشت به بانک‌ها نمی‌دهیم و هرگونه اضافه‌برداشت منجر به عدم صلاحیت مدیران بانکی خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/135968" target="_blank">📅 13:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135967">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TltZ64BLDI1Ovph1UjIesGXUtfrv6GmZEj-Kynwa7Iq2nX1MFy4bc1rzddLYVF5ORKT0OuioQrwEM_epumbqwmpzsyU58lAFCMoVJkQbcNCMktvPgQHygZnObf51MLNcg-7eUau2Da2Cw0vip_cXUEL6fU_jkC73iA1uzUiECeHvgv3sqbqZm6Gykpr48A2ivZx_vnnQjANMeJLn2ZNTutjtx0kBO2Y1iFzJC5fSfoc-fIUTT576MEUpXdVfW1rynV6MNry3oDqhSss8NaQUwuhbuqXzrd7bEdSliux6Vym334R4BnlUrhMGCVHJFUPkm7VfaR9sxHlmVoczOpSPcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سرپرست وزارت دفاع: جنگ و تحریم، موتور جهش فناوری دفاعی ما هستند. در جنگ ۱۲ روزه که یک جنگ فناورانه بود، با وجود بهره بردن دشمن از بزرگترین شرکت های فناوری دنیا ، ما پیروز شدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/135967" target="_blank">📅 13:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135966">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTcX_v9GFtgoSfsoU9u1PviXslhMxD3HeEZPVE3jm3HnqqdcTN0Khrof1tihDujMYIk4VRWEWFyB51BihY1sLvTnhqj2Kl7IsDm2QAayVo5o0msztWBZN_p71pRHIImSFyeUSab7Sp103cfayYJIzck0rce829vw4Wz0jwfAhti5pUXzUHxfp_hV11ZLPywgu3mKdBnKKhD9CK6r1QvgyIEDJhp8hCLc4f1CWuXV5UAc9CLwdf_Vc-i9X4TF1hlXBoIPjmeIrE46g9zmRykiJj5CC7NFDumcA6-yW7XMGCMEow30nbbJBLsVsrve_dTwodyGaMfcY2O9tUtdZ2OutA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز دمای احساسی زیر آفتاب تو تهران به ۵۰ درجه تو قم به ۵۷ درجه، خوزستان ۶۰ درجه و هرمزگان ۵۸ درجه رسید و روز گرمی تو اکثر نقاط کشور داشتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/135966" target="_blank">📅 13:31 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

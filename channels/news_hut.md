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
<img src="https://cdn4.telesco.pe/file/U3MfJiXJ6lyJ-mSvlAvGo1gTMsKafdfL3tuwCJ7tC-VfMv-0FYjL9mKoUssHD-f-3MuCsn4NpqaVjPueQshbAEk-Yusl9nt3V1fZxUk829e79LlE4n9rLyRtSnVuqkfg5B-5pb3ckDpVHxZmY5xCSHlGHB3qp3MgU_vpLuIH78fEt0GsJOM1dLOTvwo6rgI4MEf4q6bnBbNDbCahq61vvAsRUmTal4jdluFOZOCsMB1q4Q1WXcxMNOgdE9rartWPTf_Lctklo_p1EPwC_SVl4XD1dXmR50zZPLWLzcp4x5K6NDr1tHdY62clUBFrIq-87QNByfkggNtxY3YwQGhhyA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 219K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 18:41:18</div>
<hr>

<div class="tg-post" id="msg-66873">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aU1OWhfM8N0SaZAh-Y5yeieVZjEdV3q65BCJIFksxXudlwziIFfTtAtfTRCh4c7U3BiXrPUYr8sfnuBNBaq2T5OeMeqDSLXM0vTbbshy93x_IKDiPJHfGFVMrxfOv2CnKJZYcd8S5aI3WbnBy1wjdC2XhuLO2WWwEjDz1qJ2IybUjrZNX7VZ6YjRc5Ae0TpRUxg5Yn7YV4EymSVg-se2SXlM9I5ymBW2w0bmmgxQ9iUZtJHD54VxXYOpljofOI04_BVoannKeyHgqtdBAJ9hMkzXjtjnOL91nhgV3sdx-Yfq2CU-nE7qR17k0Rk46slMBD7r9EQGZ3tRV2NR3nsofA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇱
توییت کاتز وزیر جنگ اسرائیل که قالیباف و عراقچی و پزشکیان رو تگ کرده:
فرمانده نیروی قدس، قاآنی، این روزها مدام اسرائیل را تهدید می‌کند.
به نظر می‌رسد نقش یک جاسوس و خائن خیلی بیشتر از این ژست‌های مضحکِ تهدید به او می‌آید.
در هر صورت اگر جمهوری اسلامی به اسرائیل حمله کند، بزرگ‌ترین اشتباه خود را مرتکب خواهد شد.
نه هرمز به آن‌ها کمک خواهد کرد و نه حمله به غیرنظامیان، هیچ‌‌چیز ما را متوقف نخواهند کرد.
نیروهای ما آماده‌اند تا کار را به پایان برسانند.
@News_Hut</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/news_hut/66873" target="_blank">📅 18:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66872">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a88d77cf.mp4?token=CWIGrBnjgfKVpN8dm7e7jfnNgTP9MsuZh80R-B7582cc0sQ9u1UD3A0eEDEBBpiyQeyYbyG4IK4A4hVrmJB00A3peASuDuRVc5xpitSllP8SqBedv_VNaZooMsW_E6mpCTymdMhL8LYKX_FJQFFJ2X6BZstaGXPgtzp_Dp2WxBb7YVus-uKNsZMxfxS7zulp0yxL8JSVxWbF7SJxwEGYNbe4HOsX2OOMgRCLRBlx8JF_rjOTvs2yHPdFNwT8e_ZzCLE3GZeImVuiNTyc4ORpob6ViZOK-uJyvz70Qe48T_Vla2ZlqfWRq7Mwl5s8ky9mNL3GrObu7gbvQQa8TAvwVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a88d77cf.mp4?token=CWIGrBnjgfKVpN8dm7e7jfnNgTP9MsuZh80R-B7582cc0sQ9u1UD3A0eEDEBBpiyQeyYbyG4IK4A4hVrmJB00A3peASuDuRVc5xpitSllP8SqBedv_VNaZooMsW_E6mpCTymdMhL8LYKX_FJQFFJ2X6BZstaGXPgtzp_Dp2WxBb7YVus-uKNsZMxfxS7zulp0yxL8JSVxWbF7SJxwEGYNbe4HOsX2OOMgRCLRBlx8JF_rjOTvs2yHPdFNwT8e_ZzCLE3GZeImVuiNTyc4ORpob6ViZOK-uJyvz70Qe48T_Vla2ZlqfWRq7Mwl5s8ky9mNL3GrObu7gbvQQa8TAvwVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبتای وایرال شده‌ی یه آخوند تو یکی از هیئتای مملکت :
حضرت آدم دید هر عضوی از بدنش به درد یه کاری میخوره که یهو یه نگاه به وسط پاش کرد دید یه تکه گوشت اون وسط اضافه اس٬ گفت این دیگه چیه؟ هرچی دست بهش مالید دید اضافس بدرد نمیخوره؛
حضرت آدم خنجر یمنی رو کشید که کیر خودشو قطع کنه که یه دفعه حضرت حوا ظاهر شد گفت آی آدم چرا میخوای بیچاره‌مون کنی که یه دفعه آدم دید کیرش راست شد؛ بعد با خودش گفت این مال کس دیگه ایه٬ این تو اختیار ما نیست!
@News_Hut</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/news_hut/66872" target="_blank">📅 17:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66870">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B5BhspcJvWsUHX1l_ZSYx4BLbOVS6NIKr1ZiUlW-0WrO697-hC_lJ-kpoKxfLSTVwjNOb0ik0kv_Ww3wN34HHUpC-OQ4KchX8LX8UzRbc-22AiW6Bh0BpXI1c0d25PVLjd8ObxX5aZoFyHsQc9aog595GIsCCEdzn7dGlbKrPxgI0L-6DS5AK8qI8X7RXR1-RGPHT5obwGalHPNNN-noqKQ5EvRTnFIhPxAgqR0PrTdjwXVcXht2R5JK-simj_R_EDkVafF6GOYIjgAyeBOIKkNG7jAdJynwVR4dH9tGMo_sWQLxWw6DQfwx__NyknA5UnevSAj0A4mU_MINzdII7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P-wfIfJA9gB7FOkniKShwI1dK3lPW5NHbA0uBcFQzWeCE5VuU7STcl_P7r7n38nDIbXFDJdh8BfgOjgZCL5-IIe17uJz9hPeOfCDtzw4diMvPZqTbXByU39PdsNI-CELEbpXmudMQXDVQy-rsxXPj10tNeDouoUOGIWQT-K0fHRqqNSyjgIiaq-zia7Xoo_oTFxGLuijp5SaSUVX9j5QIVTTPNR1BqnHEkqSOARNN5lF23QPhOrvUSRRxT_gsqRy47M4l3yeqXO5be8v3mxr2pVXyvtCaZFVCIeWY3mDL4i7ZVKHG9NXvwL-nuZsLuC61tJq13ZPAXWyHRG13gB7NA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
‏
بر اساس تصاویر ماهواره‌ای که روزنامه وال‌استریت ژورنال تحلیل کرده، حملات موشکی و پهپادی ایران خسارات گسترده‌ای به پایگاه نیروی دریایی آمریکا در بحرین، از جمله مقر ناوگان پنجم، تأسیسات ارتباطی، انبارها و ساختمان‌های پشتیبانی وارد کرده است .
با وجود اینکه پنتاگون اعلام کرده عملیات ادامه داشته و تلفات انسانی ناچیز بوده، این حملات آسیب‌پذیری قابل‌توجه پایگاه‌های آمریکا در خلیج فارس را آشکار کرده و موجب بازنگری گسترده در آرایش نظامی ایالات متحده در منطقه شده.
مقام‌های آمریکایی در حال بررسی انتقال یا بازطراحی تأسیسات کلیدی به نقاطی دورتر از برد موشک‌های ایران هستند. گزینه‌های مورد بررسی شامل پراکنده‌سازی نیروها، تقویت استحکامات پایگاه‌ها و گسترش استقرار در مکان‌هایی مانند اسرائیل است.
برآورد می‌شود هزینه بازسازی خسارات واردشده به پایگاه بحرین حدود ۴۰۰ میلیون دلار باشد و مجموع خسارات واردشده به پایگاه‌های آمریکا در منطقه از ۲ میلیارد دلار فراتر رود.
@News_Hut</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/news_hut/66870" target="_blank">📅 16:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66869">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60f93beda6.mp4?token=cEQC29bSzRPs-ULVhZ9NZ5GaHMCbloToKLv-FVQNLZwzjnq6GtcLh9xfgUd7fOtZJKzXpQSZS2RLjQHpTtJJTyyw-d7FSKnjy6_xU1x4TF7AwOjK25IBMC6MiS55ly-CC-G2sefcnF5MGQzK-Yr4WU3ze6ovX6lpdBS8mtkZBytGLiWHiNt1pq7KwfxCg0ueZnDhstltjUdoho1Ziv7Dikwj_I2N8PvjNqLQ6OiHawK-Mhc3lLmhl9FxENi8UO3UECtat9hwkEGD54vsROxMMJaKyr9fxmUEcWnh2E_YfUKuFJB9uUBFFHY-j6QA7sKTsHdSssheb0RPo9Nni8Ji7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60f93beda6.mp4?token=cEQC29bSzRPs-ULVhZ9NZ5GaHMCbloToKLv-FVQNLZwzjnq6GtcLh9xfgUd7fOtZJKzXpQSZS2RLjQHpTtJJTyyw-d7FSKnjy6_xU1x4TF7AwOjK25IBMC6MiS55ly-CC-G2sefcnF5MGQzK-Yr4WU3ze6ovX6lpdBS8mtkZBytGLiWHiNt1pq7KwfxCg0ueZnDhstltjUdoho1Ziv7Dikwj_I2N8PvjNqLQ6OiHawK-Mhc3lLmhl9FxENi8UO3UECtat9hwkEGD54vsROxMMJaKyr9fxmUEcWnh2E_YfUKuFJB9uUBFFHY-j6QA7sKTsHdSssheb0RPo9Nni8Ji7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🟥
فاکس نیوز:
دبیر کل ناتو  فاش کرده در جنگ اخیر فقط ۵۰۰ جنگنده آمریکایی از مبدا ایتالیا به سمت ایران پرواز کرده اند؛
«اگر ایتالیا را به‌عنوان مثال در نظر بگیرید، ۵۰۰ جنگنده آمریکایی از پایگاه‌های آمریکا در ایتالیا برای پشتیبانی از عملیات “Epic Fury” به پرواز درآمدند.»
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/66869" target="_blank">📅 16:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66868">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403bcac56e.mp4?token=Bno6dqFGbg5gGeG4E7PFD8BoIrQv_vhe_Cypp27SuEy9fEMJQhYuNmX10aRBHeKbN0Zs6Url_YSId55ruIKJCbeaiiydlY3HnT8lKeGQDIJh829ex6khDsWNxEaBp2ebA9ggwNzraHNLpPGEpdXOP8juueW51lV2GEI5NZRNhI6cXmJldmC2m4FDFhd4qx_xU63BdDvmkVP4Sktew7-JW5EUvXwGLokHRyefUiUYx31HDACdA1vD8Gw0WvZaeSNJuKjZEqG_MIGwfPRUWc8Q02kQOD7aj7sTMji5zpKPME6Qm5ZvuXEEJHtvbjCjuToeah_tnPvPqN4Wb-wJ1chpGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403bcac56e.mp4?token=Bno6dqFGbg5gGeG4E7PFD8BoIrQv_vhe_Cypp27SuEy9fEMJQhYuNmX10aRBHeKbN0Zs6Url_YSId55ruIKJCbeaiiydlY3HnT8lKeGQDIJh829ex6khDsWNxEaBp2ebA9ggwNzraHNLpPGEpdXOP8juueW51lV2GEI5NZRNhI6cXmJldmC2m4FDFhd4qx_xU63BdDvmkVP4Sktew7-JW5EUvXwGLokHRyefUiUYx31HDACdA1vD8Gw0WvZaeSNJuKjZEqG_MIGwfPRUWc8Q02kQOD7aj7sTMji5zpKPME6Qm5ZvuXEEJHtvbjCjuToeah_tnPvPqN4Wb-wJ1chpGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پاسخ سخنگوی وزارت خارجه به دست ندادن تیم مذاکره کننده با ونس با شعر مولانا:
چون بسی ابلیس آدم روی هست
پس به هر دستی نشاید داد دست
@News_Hut</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/66868" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66867">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66867" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/66867" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66866">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=HmhlsvLs2aoaWWWlO_Bjy4uwWJE0N_9B2zpI0GlEO4awMfhyzwkE_WfjrfDvmc7yC3Tbmblb5xY9ZvvCLceNHreOe1n9p0yj240QWMUjpjQal0gGry0fCsMLHjCEy_VIp3Jt00IPq_CpBq4nQpu0kaRFBvLnH2uP4VtwTGGlKex-HDg6bysO57oj0W44j1zAqDRn_KKES-_VbJtNpKmzUizJggZfh2DNp2HN2fJcGIt5BX9Zgg-ItoI0JHAjk1J21ewIPxCTJbQywlueTeCzGuZUr5Gh0a1LT0Nj3cVC7MH3Kn_64wQHjC3EvxDrkrs82jB5qEqmCXE4LzFAocO0M3vwAMWhhoU7cMTb3rLXDCjujP9JRo4cNJvg1cgjUfoznE9VT6L8aMZstB6D25HkF8Q1GidzAcBKVCmGsolxazQ3iLdz5umakFZ2PgRtOtjQwcSFExaqnO4HJ8DZBwER34ohif9WDnDW5tisv_8oghDKCSU_EQ7Yv4la9o6ehbakaLnE_G38xCMTFBvFeFKs9djaI5_0Lhm1XW4PN2iIBOEW5461H4n0_R5aJRv9Kd5dFu8ujN9hTCHLyNfNSrqzfblG4_z48j9PDW0OlTVGu4fWMxL-tTY92Fgb3334oevBUF68QXXBqxvXbH_hJaHKlmF6M6udzaX3jrARA7y9JRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=HmhlsvLs2aoaWWWlO_Bjy4uwWJE0N_9B2zpI0GlEO4awMfhyzwkE_WfjrfDvmc7yC3Tbmblb5xY9ZvvCLceNHreOe1n9p0yj240QWMUjpjQal0gGry0fCsMLHjCEy_VIp3Jt00IPq_CpBq4nQpu0kaRFBvLnH2uP4VtwTGGlKex-HDg6bysO57oj0W44j1zAqDRn_KKES-_VbJtNpKmzUizJggZfh2DNp2HN2fJcGIt5BX9Zgg-ItoI0JHAjk1J21ewIPxCTJbQywlueTeCzGuZUr5Gh0a1LT0Nj3cVC7MH3Kn_64wQHjC3EvxDrkrs82jB5qEqmCXE4LzFAocO0M3vwAMWhhoU7cMTb3rLXDCjujP9JRo4cNJvg1cgjUfoznE9VT6L8aMZstB6D25HkF8Q1GidzAcBKVCmGsolxazQ3iLdz5umakFZ2PgRtOtjQwcSFExaqnO4HJ8DZBwER34ohif9WDnDW5tisv_8oghDKCSU_EQ7Yv4la9o6ehbakaLnE_G38xCMTFBvFeFKs9djaI5_0Lhm1XW4PN2iIBOEW5461H4n0_R5aJRv9Kd5dFu8ujN9hTCHLyNfNSrqzfblG4_z48j9PDW0OlTVGu4fWMxL-tTY92Fgb3334oevBUF68QXXBqxvXbH_hJaHKlmF6M6udzaX3jrARA7y9JRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/66866" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66864">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzAlNAuqqwSgXqo8NvmErGWn7enByHW8GRYhiXiKN-CS_a7OpbXtNvNyWBELH_und9x2t9cokX2yvYW7Yvkem9F2vconDE--oCR3eWK6u8CfR2AkJVXmmZGvL2910oOL-bQO0WEhjFP_KqDxrygyUN6KwWDDsdYcBO2LDWFXM33Aurf1u7vuvnVtWfADO1if9bj4GyKRatj3e87rxpFyk9UIQZJKONf4A3THfNahMwuCuQHCLck3lmPVyKjHceAcGjzCxAD8d3GpX7krns8nKSJhA6jH7ltD3PqVi0imRp4QDYbfYuKoUw3mMm8T5pC2CEgVGT1Qlib04rvIJwEe5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a41ee6c687.mp4?token=K3fXCXlqSWhH1d0hwhiYuvSUvmEVOQuYRcwm3FV-cH5wfgW6Ky4f01aEDl6X_yFoLtk2t57Ho_09T_rSz-mIxbwZYAocp5fUFlth1zELr0EMptBJ8EU4Kvj4s5j_H6-OYq1msV91nOLo75aIAcg0SfXggnxWlnX0BDobYxz-JQRdNSau8raZzI21ALnCIKeg3uPn314KLUo2lPZigRGpdU-r57kSY39Y_iIKkXg3-RFro9iXgjF8fyDGm4O4hYBOdrY40k3GIrQKxcodBz4YS7CA-Emv2DbOGthfBi-WdhelhlviiA65sYnYLbf9LZMFOXVgvbuevoa_dHFc46za5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a41ee6c687.mp4?token=K3fXCXlqSWhH1d0hwhiYuvSUvmEVOQuYRcwm3FV-cH5wfgW6Ky4f01aEDl6X_yFoLtk2t57Ho_09T_rSz-mIxbwZYAocp5fUFlth1zELr0EMptBJ8EU4Kvj4s5j_H6-OYq1msV91nOLo75aIAcg0SfXggnxWlnX0BDobYxz-JQRdNSau8raZzI21ALnCIKeg3uPn314KLUo2lPZigRGpdU-r57kSY39Y_iIKkXg3-RFro9iXgjF8fyDGm4O4hYBOdrY40k3GIrQKxcodBz4YS7CA-Emv2DbOGthfBi-WdhelhlviiA65sYnYLbf9LZMFOXVgvbuevoa_dHFc46za5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسانه‌های لبنانی گزارش می‌دهند که یک پهپاد ارتش اسرائیل، اعلامیه‌هایی را بر فراز شهر منصوری در جنوب لبنان، نزدیک صور، رها کرده است.
روی این اعلامیه‌ها نوشته شده است: «منطقه خطر! دور بمانید! هرگونه نزدیک شدن به نیروهای ارتش اسرائیل شما را در معرض خطر قرار می‌دهد.»
هنوز تأیید فوری از سوی ارتش اسرائیل وجود ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/66864" target="_blank">📅 15:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66863">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22157b34b4.mp4?token=HyciqR9ojR75gyeIv1CfKQxS8Hv5FKNjuov7Mpqq6IRvXZ4Q1PgfB6z_tiX9FjE0Jle6VHvO28QBBUmSRIXlhTmki7cVqqqDFNx_iAqtIYxvElWUDsRf-YtsYsyPMYrRfClu78Gpl-_D-34HHwdJZgz3DrmkxyIPD_lckp59dB_G4Gqn142p_WFxrHvcfbzJtCSu5EgcPet_UISyI1vVWuX9Ipc0QOdibhqMHjsuxzaBVvkIryn3wFdY4lWOVkVL64ookuDrrBWIh2gXm-Tu7AS2DBKAOOuDcLAUac3j5rn4bjZdocWwap80VRvsV6wAACMCDeLDk4GDDIN9T22Wfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22157b34b4.mp4?token=HyciqR9ojR75gyeIv1CfKQxS8Hv5FKNjuov7Mpqq6IRvXZ4Q1PgfB6z_tiX9FjE0Jle6VHvO28QBBUmSRIXlhTmki7cVqqqDFNx_iAqtIYxvElWUDsRf-YtsYsyPMYrRfClu78Gpl-_D-34HHwdJZgz3DrmkxyIPD_lckp59dB_G4Gqn142p_WFxrHvcfbzJtCSu5EgcPet_UISyI1vVWuX9Ipc0QOdibhqMHjsuxzaBVvkIryn3wFdY4lWOVkVL64ookuDrrBWIh2gXm-Tu7AS2DBKAOOuDcLAUac3j5rn4bjZdocWwap80VRvsV6wAACMCDeLDk4GDDIN9T22Wfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ:
اکثر مردم نمی‌دانند که حرف B در کلمه dumb وجود دارد
😢
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/66863" target="_blank">📅 14:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66862">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">⚠️
خبرگزاری فوق معتبر فارس:
درب تاسیسات فردو، نطنز و اصفهان به روی بازرسان آژانس تا زمان رسیدن به توافق نهایی بسته است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/66862" target="_blank">📅 14:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66861">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bfb3904efc.mp4?token=GS_o9lYqhihINSJvMvIgyBWS4DwOSq1UhsGVIqwzfC9_RmbAv3MKuKFC3dJs78MHMCr70ZcqnKS0n5s-QEBI-tR-DuAaRjws5oYQ-MPPvPgWYMRLQGDdnGFhcV123feI2qaNfF7i4BxkUlEoMlzs52j4SuxmHWPDLJqt2SQjaZ8KIy5Wv2bL5ptHHXGTx35r7kczO_elgvoyXWv_lX-drzmEMxTNQyy8YA8y1pR3kM083Wm4PswRITlkdNzCmcNKU_2yRBF9nMsWfnqiJKYIehNfz4IioqjQF93tG3jP47SuSsGjl7PFWonkRTcuJUQedzUmpDE50mSC0XYCrdQvsA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bfb3904efc.mp4?token=GS_o9lYqhihINSJvMvIgyBWS4DwOSq1UhsGVIqwzfC9_RmbAv3MKuKFC3dJs78MHMCr70ZcqnKS0n5s-QEBI-tR-DuAaRjws5oYQ-MPPvPgWYMRLQGDdnGFhcV123feI2qaNfF7i4BxkUlEoMlzs52j4SuxmHWPDLJqt2SQjaZ8KIy5Wv2bL5ptHHXGTx35r7kczO_elgvoyXWv_lX-drzmEMxTNQyy8YA8y1pR3kM083Wm4PswRITlkdNzCmcNKU_2yRBF9nMsWfnqiJKYIehNfz4IioqjQF93tG3jP47SuSsGjl7PFWonkRTcuJUQedzUmpDE50mSC0XYCrdQvsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو یکی از مراسمای محرم، شیر تعزیه افتاده بود دنبال یکی از لشکریان یزید، که یه لحظه جلوش رو ندید
🤣
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/66861" target="_blank">📅 13:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66860">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
قرارگاه مرکزی خاتم الانبیا:
🔴
پرواز هواپیماهای نظامی اسرائیل در نزدیکی حریم هوایی ایران یک تهدید مستقیم محسوب می‌شود و اگر ایالات متحده اسرائیل را مهار نکند، ایران این تهدیدها را تحمل نخواهد کرد و حق پاسخ را برای خود محفوظ می‌داند
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/66860" target="_blank">📅 13:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66857">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oo9oZVqERXKjmwXTpesSOcxfIK3aYviuAMHyDSiybq3cAD88M8EkFNjBou2OEMxQgawpJETCZBi_KOYPFCUkXYojrWD2Qz_wfk0gQat4aRY97uS5XuTmg_ZcD-QbXX1GmjEgu8INxsMgo-bu-CSy2CM1jdLhSh00Mano3jbR9X158m7A3nM9emv05alybIA524LNRuJlxjBJytZijWS2odW4x_H4Y3epDDyvISN-kS1PdlrtMnT0m-kuLQgFbHKvoIAEpxafc6xiQZqXZVL5iJLi1tRc-zW__3I4-CbYo9AGHC_TKO57IVccZasJG6s2buhPzzfNZ5mGcJDoRZTouQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C7GizzHGf8hvvaBAEApqeqCRlR2ZJeOgigwCWvJutssSZOSOlhWJxBZiVfC4fDfjSVAGrbBEEruiVAgHvqtphLpqv6YlxmYIqeC-H51h7KaQQ2hq7lIto07jji0ukbnYh4MxxeZSS-dLMz1vTPnZHyjMpMZCDgfF37-ASghRIinvQE9mgB2AlhiAPLyVUEOLvieZ_bE7k8TZ8i9qOBlvn7iEsEtxFHMRsrlxwHkvR-Br4dhoFQ1ZvPs_8mjfF2ekIGILwJdG-_yW2l3UfasHw0AMuAEhXDmJNPYY-FuJQtQIM3YdRdbPAfKDOMzxcZkIh4_2absD8FCF58KiajXuWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/URih0d8VX1o8K7N46CIbvO4OH4PgK9l9tpn6x4kZnELTLrvpbM3SC7kCoOYfLBc4RcXDUyATDbcvmxFJ0W4rJE1j29p5pyQ2Om_WUcWplPjKx4uJyyYc7WuAiUmb4KbY4WMEFsvvJKxErARC9jAbaNewRqXOR0QUOw-HB8MU66oqaqNWEtRceD-K4yg_CaumXlUUuf-Mp0zGuZ_KAIfeRWrXXYDtyFXCdGAvf9m_EbiirsDVNhEg7idDTBPLtYEOleFiq0Y_Sk6aCg4pRoaE96SB-wV44GavelJHFLLJqsu2Z-XiNUCc2IRb1Q9rR_Sm0YBPq-q0HHsdvzc5zqjsPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
حملات هوایی صبح امروز ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/66857" target="_blank">📅 12:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66856">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67fdc892f6.mp4?token=lAf6jOf4_85WDzYRyCrMHBCu2m79MxePKfOgxW_aXTUIagQ59yQlIHxyUtH7HPdSKFEdXd6w8bvEpTBwBNfepmeIwIJu_W7C9YfxdilaXn53IvHpJiYz00lyIQYRUVofRj33c-S18WBcHuVfQokzPjC-8IYFqtUdC5xtAdKLejdfxVRvTgiJpwqBEjtjIKvlcVvvGLJRlBSij8V2wFaEKmUwl6m77EtdYEYIHvq-g0NG0dy4Ape5D-eUO_U8rDwRdZOwqUxUhFqPenibKKoMaJIHly34Qx6CpLedBH2MuJKGeBq7J_LoVLc-hXn_RAxMc4LIWBaqBhIXsa7wv0JpHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67fdc892f6.mp4?token=lAf6jOf4_85WDzYRyCrMHBCu2m79MxePKfOgxW_aXTUIagQ59yQlIHxyUtH7HPdSKFEdXd6w8bvEpTBwBNfepmeIwIJu_W7C9YfxdilaXn53IvHpJiYz00lyIQYRUVofRj33c-S18WBcHuVfQokzPjC-8IYFqtUdC5xtAdKLejdfxVRvTgiJpwqBEjtjIKvlcVvvGLJRlBSij8V2wFaEKmUwl6m77EtdYEYIHvq-g0NG0dy4Ape5D-eUO_U8rDwRdZOwqUxUhFqPenibKKoMaJIHly34Qx6CpLedBH2MuJKGeBq7J_LoVLc-hXn_RAxMc4LIWBaqBhIXsa7wv0JpHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
«یک بازار جدید دیگر هم در راه داریم و آن، کشور دوست‌داشتنی ایران است.
ایران کشور زیبایی است. کسی دوست دارد به آنجا برود؟ جمهوری اسلامی ایران با مشکل تأمین مواد غذایی روبه‌رو است و ما قرار است بخشی از پول آن‌ها را بگیریم و آن را خرج کنیم. همچنین قرار است مقدار زیادی گندم، سویا و ذرت خریداری کنیم و این روند به‌زودی آغاز خواهد شد.
این برنامه هم بسیار بزرگ خواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/66856" target="_blank">📅 12:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66855">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daTywHm-ItI3_atB5Lc7sXyrTsp12sdNA6f-hQnbWUC8KNXQcfsrAQ9Rv1drS6AgOYBHI3wjyTIOtCZ-xruIFykqDfRNaam2u0c0f9ODvF8nXkQ9ssB85LyqtpGryyn4sz2i4Fwj3KlboFOq3qVA95fDN3_g1sm1arMMBJ5xDqFqYnDALo7ycURL7AQ_wBYX71-O9TvRiVN3hiGVpwWwK84ydQHqbM-O9okQ97YopEXUuiN-2nYcv5kc4x6Mk_jwNshSiUZ2r4AYVFVfy2vTtxLod6FNU3Ta4YQxN9WJenRdT9LDOE6TTQ5Jy_Hs5wbjAsdlEg1YdjM4cExmQCf3Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت ترامپ:
روند خرید محصولات کشاورزی ایران از ما خیلی زود آغاز خواهد شد و من انتظار دارم که حجم آن بسیار زیاد باشد.
ما پول ایران رو گرفتیم و بجاش ذرت و سویا خودمان را دادیم!
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/66855" target="_blank">📅 11:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66854">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‼️
جی‌دی ونس درمورد ایران:
🔴
آن‌ها دائماً سعی دارند مأموریتی که دونالد ترامپ برای ما تعیین کرده است را تغییر دهند.
🔴
او در ابتدا چه گفت؟ «من می‌خواهم ارتش متعارف آن‌ها را نابود کنم. من می‌خواهم توانایی آن‌ها برای اعمال قدرت را از بین ببرم. و من می‌خواهم تضمین کنم که هرگز سلاح هسته‌ای نداشته باشند.»
🔴
آنچه دیده‌ام این است که برخی افراد سعی می‌کنند بگویند: «خب، این عالی است، اما شما باید هدف متفاوتی داشته باشید.»
🔴
به نظر من دلیل موفقیت رئیس‌جمهور این است که او از تسلیم شدن در برابر آن تمایل خودداری می‌کند.
🔴
او می‌گوید: «ما کاری را که قصد انجامش را داشتیم انجام دادیم. ما اهرم‌های دیپلماتیک، اقتصادی و نظامی باورنکردنی ایجاد کردیم. بیایید از این اهرم‌ها برای کسب پیروزی بزرگ‌تری برای مردم آمریکا استفاده کنیم.»
🔴
این همان چیزی است که او از ما خواسته است انجام دهیم. هنوز تمام نشده، اما تا اینجا همه چیز خوب پیش رفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/66854" target="_blank">📅 10:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66853">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aefac4ff7d.mp4?token=mvPEUuA9R4oRc96JqMWkU_qpS-ynxrR_MZnrkMBzD3WnQ1uxmxuQlUW4CEumcUpIjTdSrsj-v7HBn5IKsO9VlYUtuwhqvKcKHl-nAf-B58kdkj29yZNiHgqspGGdey8yG1rnOxXje3c2budLH90gOw1qP9AoicpqEbq-dLB0gzDemAUDinYmZFxjyGf-LQhZY-lkNV79tBAVLSL3nkmz6ysN5zmNbqDVUBisGN-69wWJyM_5ToKIYk5-Wrge4otK5yzYfoPC9LSDXkXLv2i4_zzCSiAbt44cKArgu_7bcdfEvXRonTRz8ZKpxMoxq-WBW6K-nMz5bbWR60Esz7m24g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aefac4ff7d.mp4?token=mvPEUuA9R4oRc96JqMWkU_qpS-ynxrR_MZnrkMBzD3WnQ1uxmxuQlUW4CEumcUpIjTdSrsj-v7HBn5IKsO9VlYUtuwhqvKcKHl-nAf-B58kdkj29yZNiHgqspGGdey8yG1rnOxXje3c2budLH90gOw1qP9AoicpqEbq-dLB0gzDemAUDinYmZFxjyGf-LQhZY-lkNV79tBAVLSL3nkmz6ysN5zmNbqDVUBisGN-69wWJyM_5ToKIYk5-Wrge4otK5yzYfoPC9LSDXkXLv2i4_zzCSiAbt44cKArgu_7bcdfEvXRonTRz8ZKpxMoxq-WBW6K-nMz5bbWR60Esz7m24g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎯
ارتش اسرائیل: ۶ عضو حزب‌الله را در جنوب لبنان ترور کردیم!
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/66853" target="_blank">📅 10:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66851">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73a731d25b.mp4?token=Y-EIPrhAOrrlgNiZ7X8luJukKlcxFv7fVLhYcV4Ghi1mU5s42s8OvvDLW4c_tj9Tk24WvobqEmAHuAOqGBaBbZBqMMD41zKUW5AVRb5wRdZKby56sWKrMxDWqIBwYMS6k0Fk1EwfYL_09Fdx-aUOR26PiExAWkLQY7Z3pmtzXo6JU2VHl-0AT8M2NgN3OD_JBDhg_TgOaiAFcD0pTJxboRSF-rqWLWX-WkQVqJTDSPsqzO5rwVGeOgScfNqM55-wEviuxHY3I8S1VP6a06qFMucK-zL4pQZyLEU0MfpWpUnJ5BHF4MI0sGy7WcZ7gFmuat_NyBAJjWfQgu97bkbl6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73a731d25b.mp4?token=Y-EIPrhAOrrlgNiZ7X8luJukKlcxFv7fVLhYcV4Ghi1mU5s42s8OvvDLW4c_tj9Tk24WvobqEmAHuAOqGBaBbZBqMMD41zKUW5AVRb5wRdZKby56sWKrMxDWqIBwYMS6k0Fk1EwfYL_09Fdx-aUOR26PiExAWkLQY7Z3pmtzXo6JU2VHl-0AT8M2NgN3OD_JBDhg_TgOaiAFcD0pTJxboRSF-rqWLWX-WkQVqJTDSPsqzO5rwVGeOgScfNqM55-wEviuxHY3I8S1VP6a06qFMucK-zL4pQZyLEU0MfpWpUnJ5BHF4MI0sGy7WcZ7gFmuat_NyBAJjWfQgu97bkbl6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف با روسری و ماسک اومده بوده هیئت
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66851" target="_blank">📅 09:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66850">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cff13197ee.mp4?token=E0JeZChsoT9J-jZlUqztweGxfySIm2AJlWHzvE3zr6X8FG5RnK-NuIBT8LYhIhtREFerYuEyZjG1vD65276fCS057y7e9W2KmSMDEXT62r70574E89Ii0_gyXUH7C6gqOEcFjnNOTg0rO2XxHu_LrfPoc8d0JLoKLeixFrQcgjQ7TN53Mnxde_NfXDOdZRfaiDtqEMpLaRpOWGyZHsdpznRF-mbASh32GSKy-fHzSYJRuq-Jxs_L2rl9eMfKrUr19peczuP8Y4hpug7RpoMIituWbguaMaN53TEee8W_uuSA4a_Q9EbMqggAp8o-YBdnEjRflMG1ibMBIL-azYc9Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cff13197ee.mp4?token=E0JeZChsoT9J-jZlUqztweGxfySIm2AJlWHzvE3zr6X8FG5RnK-NuIBT8LYhIhtREFerYuEyZjG1vD65276fCS057y7e9W2KmSMDEXT62r70574E89Ii0_gyXUH7C6gqOEcFjnNOTg0rO2XxHu_LrfPoc8d0JLoKLeixFrQcgjQ7TN53Mnxde_NfXDOdZRfaiDtqEMpLaRpOWGyZHsdpznRF-mbASh32GSKy-fHzSYJRuq-Jxs_L2rl9eMfKrUr19peczuP8Y4hpug7RpoMIituWbguaMaN53TEee8W_uuSA4a_Q9EbMqggAp8o-YBdnEjRflMG1ibMBIL-azYc9Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فرماندهی مرکزی ایالات متحده:
جت‌های جنگنده اف-۳۵ بر روی ناو هواپیمابر یو‌اس‌اس تریپولی  (LHA 7)، ناو پرچمدار گروه آماده آبی-خاکی تریپولی/یگان سی و یکم اعزامی تفنگداران دریایی، در حال برخاستن و فرود هستند. ملوانان و تفنگداران دریایی ایالات متحده در دریای عرب در حال عملیات هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/66850" target="_blank">📅 09:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66849">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال @Palang_Bet شو چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی @Palang_Bet     @Palang_Bet</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66849" target="_blank">📅 02:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66848">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNl1hpjsh1osc3qEo1IY9vTdgMt1lrsl9k7XNpOGYeYNcE9etLSX4-6FXacAycEooQZ8zjfNwrXwaeFo_H_goln9xD-5_jA5PSBV2-MwRipLB4qzWx0Okz1NjOmp96WgL6XayYIKQuBqRekkf_mL7eaQtiVl7wqjgyqjQ4_BEMBiAwPqKdRKcc86mZpfZHq7PJ_oniNed4KiygC8XH1yzMZsYfxXfSrl-SoWOpeaVdEtT1okbQtgzaYq_BNj4lHpT1-nwGnYIqixBHqpSWNLQ46FrdY2klwqNfLLQIDpLRt0jr3Q7qGpcuvxqYgJxuvhc4elzl6X-Fgf6hH-Z7Bpwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال
@Palang_Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی
@Palang_Bet
@Palang_Bet</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66848" target="_blank">📅 02:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66847">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFodfH1BHMEeLUV-gksrkOwWv90cafYgEer2CSI_7_-ESLtNepEXYAi0Bor2TlW1tqeBar5_MWNWf_rRLK4gMGOeYmuEvl1WRQ4uCFVKoL1WcmYDCiK2Y7kHnQI7ZifrOmbPIEKo3j40ltCe8fYbcu0O0h2yfvC6dJ2ePVUXh3XSqOAnBI9qVOAJzdxS49xptvs_N9kBTxPSrPsm1bNvmr3UHolhzOKouIBt8gfbXMj0wIa0p8eYGlyh5o7QbWnp9DuKZA84MsTkTUzR9Moru-_14xh8pLaSFTliWO9Ut8NDVZUqwnPFi3FDMJll1W-eHxRbNg9l3jadud5r5v7arQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏بر اساس گزارش وال‌استریت ژورنال (WSJ):
🔴
ایران روز پنج‌شنبه به یک کشتی باری با پرچم سنگاپور در تنگه هرمز حمله کرد؛ اقدامی که به‌عنوان آزمونی برای توافق هفته گذشته میان آمریکا و ایران جهت بازگشایی این مسیر حیاتی کشتیرانی تلقی می‌شود.
این حمله به پل فرماندهی کشتی آسیب زد، اما هیچ تلفات جانی در پی نداشت.
این حادثه چند ساعت پس از آن رخ داد که ایران به کشتی‌ها هشدار داده بود از مسیرهایی که مورد تأییدش نیست استفاده نکنند
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66847" target="_blank">📅 01:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66846">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">رسانه های اسرائیلی اعلام کردند طی درگیری ارتش اسرائیل و نیروهای حزب الله در منطقه بیت یاحون در جنوب لبنان چند نفر از سربازان ارتش اسرائیل از تیپ ۷۶۹ مجروح شده و با بالگرد از منطقه تخلیه شده اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66846" target="_blank">📅 00:57 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66845">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">با بحرانی تر شدن وضعیت ونزوئلا و مفقود شدن بیش از پنجاه هزار نفر گویا به نظر می‌رسد مثل زلزله سال ۲۰۱۰ هائیتی که ایالات متحده آمریکا به این کشور نیروی امدادی/نظامی ارسال کرد دولت ترامپ هم به سمت همچین سناریویی پیش می‌رود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66845" target="_blank">📅 00:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66844">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
وقتی نت ملی بود ، تنها سرویسی که برامون قطع نشد همین بود
🔥
🔗
@Kaviani_Vpn
🔗
@Kaviani_Vpn</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66844" target="_blank">📅 00:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66843">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHFLEHf8y9mg00my4rHF8Q-JTPMcF6taitL4U3WX5zOOSd8UgsEXP_WyRl4Qb0dKgg0WzhT82NeXrpBYJoOY0R1KtF39Zjvcv2k9p6SujCkpobVa5V343mpGLcxUL8YH5JXY5N9OQ9XnK5dBaGJw_hBQcjFEnBEtCQIsvZAOV_R0xsqJEuN6tPfsAIxSy7e_N0SmIYk92gthex5Ss_CqGkreGlTruuIfQayRuBlUzSCEyJEwJcXcpVaMOeHEZP9M7ntIZT-N5LssSXRsv-dQSiBbNoYRS5LbstwnpElf5ljgsR6-dp5fluLcJOIBND2ujMmEWTDbsyfE1M12SlTH9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
کانفینگ نامحدود برای همه اپراتورها
🔥
⚡
سرعت بالا | بدون قطعی | تحویل آنی
💵
یک‌ماهه: 380
❗️
پشتیبانی 24 ساعته واقعی
❗️
✅
سازگار با تمام خطوط
🚀
اگه سرعت مهمه، همین الان پیام بده
🔗
@Kaviani_Vpn
🔗
@Kaviani_Vpn</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66843" target="_blank">📅 00:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66842">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CS-fH3qzGeFuZItzovKGlFk23q_0vh4wbwAU6oSoGWqg2c1z1J_g5Y6N3hKgfvQlLEqnBBVxHLi5jCR6_vADQGbJLYnrXXXjrca4E1QTVYCWAHm179PBxQNSwfAsX5HuOAxbCRFYeKUaImC_YqE5evDETrmOQInxWvLX2GACHZ3wxzpa0cSG0hl9U7cx47THTgc31m4vkwwEUcKmZts-ET4eF85uwXHh0lhrUaR8bVgAl9ya3kInpbWyRXImJG-Epe33hnMzkDa-E2T7MUMR2sbDNnFMfQPBLoxiYbYiezThlEmIfEuLxPydMLC25mzVKLnt1FjClL0IP3PqiyJ_aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
گزارش از لبنان: جت‌های اسرائیلی به بیت یانون در جنوب لبنان حمله کردند.
این پس از تهدید امروز سپاه پاسداران علیه اسرائیل صورت می‌گیرد
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66842" target="_blank">📅 00:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66841">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b6d00bedd.mp4?token=JLALEFAEuJy3pWqRgagiHGzoVUTNJJe4Dq-GCeQg7NwaSHSMj03J9mo1HrrxxXs0kHT1JXfGExh2Rd4ISlafwVqCTfr7TXKtMku3thnlITfDRino0lD9nS8OSAfWO2PvjCWolP9NXy89yG9n1VW_JLr3FPIX0usIG_6wjYCOxcBLKaAhPN_Lpp5TYph4uPD5e-x8ufy0Q2eIEk6_8mTz0Ti_RxWpdAjP47QhR8hg3A0shcSQnjBFws490IWdpciMxTJxbpchu-kkttXn3G12v8od0EeBFhn-BfVHiDnzkNpLhfIR9t_VS3t3zwWbvPSA0bgv14WAW78TJRWhZe3bbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b6d00bedd.mp4?token=JLALEFAEuJy3pWqRgagiHGzoVUTNJJe4Dq-GCeQg7NwaSHSMj03J9mo1HrrxxXs0kHT1JXfGExh2Rd4ISlafwVqCTfr7TXKtMku3thnlITfDRino0lD9nS8OSAfWO2PvjCWolP9NXy89yG9n1VW_JLr3FPIX0usIG_6wjYCOxcBLKaAhPN_Lpp5TYph4uPD5e-x8ufy0Q2eIEk6_8mTz0Ti_RxWpdAjP47QhR8hg3A0shcSQnjBFws490IWdpciMxTJxbpchu-kkttXn3G12v8od0EeBFhn-BfVHiDnzkNpLhfIR9t_VS3t3zwWbvPSA0bgv14WAW78TJRWhZe3bbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار:
«شما قبلاً آن‌ها را «دیوانه‌های دین‌سالار مذهبی» می‌نامیدید. آیا هنوز هم فکر می‌کنید این توصیف دربارهٔ رهبری کنونی هم صدق می‌کند؟»
🔴
مارکو روبیو، وزیر امور خارجه ایالات متحده:
«ببینید، موضوع این نیست که من باور دارم این‌طور است؛ واقعیت همین است. نظام ایران توسط روحانیون، یعنی روحانیون تندرو، اداره می‌شود. همیشه هم همین بوده است... البته در بخش‌های سیاسی حکومتشان هم افرادی هستند که ظاهراً انعطاف‌پذیرترند یا تمایل بیشتری برای همکاری با ما دارند. ما در حال مذاکره با همان افراد هستیم. باید ببینیم نتیجه چه خواهد شد.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66841" target="_blank">📅 00:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66840">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/345e633380.mp4?token=bjmCyKpod0FvrEZTqNqs7gBTpPlzQ4ACvFsD3gC7e3iIMcAfg4kf96tOf3eDB_oDn3uQYQRPxQ_8c1XiLZ4BeTiH-EQTh3u0qy2W0riBkGOTfGKj8QoEOEZja-OfXg53rZNkhUQlQOp1VjM6SPQKctqsWRZU_lm3x9d0zoKpCTPzyrKNg4b6GQLXI-WEv8iucFPEfqQgvTxNGoXofdfnDtWAiJlnbWcGLFe3DkDbCtqE8yn2w_A8SUUlcWJ5BsvhNr6gQrdYAyn3yRgSc4KPhSLjEQpZcLwq4xzZF6ZvOJtk3KeFRE-np0ERcqIPcRo9i5iupaNH4Mh_63NGW0Tpmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/345e633380.mp4?token=bjmCyKpod0FvrEZTqNqs7gBTpPlzQ4ACvFsD3gC7e3iIMcAfg4kf96tOf3eDB_oDn3uQYQRPxQ_8c1XiLZ4BeTiH-EQTh3u0qy2W0riBkGOTfGKj8QoEOEZja-OfXg53rZNkhUQlQOp1VjM6SPQKctqsWRZU_lm3x9d0zoKpCTPzyrKNg4b6GQLXI-WEv8iucFPEfqQgvTxNGoXofdfnDtWAiJlnbWcGLFe3DkDbCtqE8yn2w_A8SUUlcWJ5BsvhNr6gQrdYAyn3yRgSc4KPhSLjEQpZcLwq4xzZF6ZvOJtk3KeFRE-np0ERcqIPcRo9i5iupaNH4Mh_63NGW0Tpmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری:‏بهای بسیار سنگینی.
رئیس‌جمهور ترامپ این جنگ را آغاز کرد،
و وعده‌های بزرگی دربارهٔ تغییر رژیم داد
و وعده‌های بزرگی به مردم ایران داد.
آیا ازنحوه‌ای که آن را به پایان رسانده،ناامید شده‌اید؟
شاهزاده رضا پهلوی:خب، نمی‌دانم هنوز تمام شده یا نه.چون همان‌طور که می‌دانید، هر چند ساعت یک‌بار ما یک توییت متفاوت از این
رئیس‌جمهور دریافت می‌کنیم و ناگهان موضع
از یک چیز به چیز دیگر تغییر می‌کند.
بنابراین من خیلی به هیچ اظهارنظری
که مطرح شده، وزن نمی‌دهم.
و در واقع، من فقط، می‌دانید،
کمی دنبال می‌کردم که
در به‌صورت زنده چه می‌گذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66840" target="_blank">📅 00:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66839">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">#فوتبال جام جهانی فوتبال
📊
2 گل آلمان و ساحل عاج  کد:YXA6P ضریب:2.3
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
دانلود برنامه ملبت @Palang_bet</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66839" target="_blank">📅 00:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66838">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f455bc9393.mp4?token=EadIj45nYFyBHcPkfVnQmVwRbROMKHZlNhLTa0r_CFjgnG61Buxz2Otw6bobUhNcX0U94hmF7Lnd-a8V105z-y-wXsac_y_gn7-Jbmkdxg5pIbbnd2C0IBxIbCwQ11u_dX_KQnOAi9uFg8WBqxhgaP5d8bZ16TS5BkoaKVdUpIn2bZ_MpDcxMXTbDt3DAiEXoIp31AdgaKkDklVcjaY25udT8JO5BrDmXTQK3NLU42oTP6FOsrwPv-4A9RrwuLeTQIwLuorBoWSCkDeUV28gH7GWFr4FJzEWn0MVjuMDTOoLjVP8WyKxT75cPmFHGbVGisHt81GVy9FsCGOj2lKHNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f455bc9393.mp4?token=EadIj45nYFyBHcPkfVnQmVwRbROMKHZlNhLTa0r_CFjgnG61Buxz2Otw6bobUhNcX0U94hmF7Lnd-a8V105z-y-wXsac_y_gn7-Jbmkdxg5pIbbnd2C0IBxIbCwQ11u_dX_KQnOAi9uFg8WBqxhgaP5d8bZ16TS5BkoaKVdUpIn2bZ_MpDcxMXTbDt3DAiEXoIp31AdgaKkDklVcjaY25udT8JO5BrDmXTQK3NLU42oTP6FOsrwPv-4A9RrwuLeTQIwLuorBoWSCkDeUV28gH7GWFr4FJzEWn0MVjuMDTOoLjVP8WyKxT75cPmFHGbVGisHt81GVy9FsCGOj2lKHNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مفقود شدن بیش از ۲۱ هزار نفر در پی زلزله‌های ویرانگر ونزوئلا
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66838" target="_blank">📅 23:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66837">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFm06uSYg6159Puts4R1f_fpEhfqXtoJ7eyjgLVjtnMxjCLgrh9Lb-btuuY3_h-vV6xwg7H75UQSxhg_2dAuKDJbgb_seP1ty53gdBFDuY0mGyWxIxZs8fM0K1XGHSfJmaS5Sja1UimKL-chjGK1RkRXWkx197oI9cAl8xQ5WzG-a27Y-BBcwW7s01gOKlZpRHiJp08NJ1zljPzQ9E21hAag39Y2bjgb65f6VU6XfivzUmA5YyIQEpm781NvGvs3CbBOHOGV_nQcxLd_5dRXqDV0yrFuA6RPWy1Zm-LItURLndxvGmD88GxL09x55nvbD7pXZxljl72xUGtO84A8ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
پس از بیانیه مشترک اخیر در مسقط، تماس تلفنی سازنده‌ای با وزیر امور خارجه عمان داشتیم. ما مجدداً تأکید کردیم که ایران و عمان «برای تعریف مدیریت آینده و خدمات دریایی در تنگه هرمز» گفتگو خواهند کرد. ما مصمم هستیم و این کار را با همسایگان خود انجام خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66837" target="_blank">📅 23:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66836">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab5d7e42e.mp4?token=oSmrcDH3bi__OqeZLupTGPKauVojLwNvDZn0_AncEwRo6JSMe5TqDC53UKXvQWc1zHzMWiGLe_0TRQL-0-0GrKELQT71uRTgxFOA42BcH6rBGa-Wx3Khpz31EhWjWYX2UWpMNfmI019aA5rb3VDt69ZPs2hqx_GWqi9-fAd2b_4GreaOiT4E6mq-x4WQ1WNSMi_xNQYE9WIsUe46FRD3RJIHCVfsvlTNVAvyacZHSchnIcXD-kzfSmynuLzEwENgXQ_zarPJKBwMTAzsVNB6JpNy8-l_KNlWOmxHSWVHYiGWQJCU0WaZZiZUN2mjldOAk_dPTYLwHuhvm7qrsV4bLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab5d7e42e.mp4?token=oSmrcDH3bi__OqeZLupTGPKauVojLwNvDZn0_AncEwRo6JSMe5TqDC53UKXvQWc1zHzMWiGLe_0TRQL-0-0GrKELQT71uRTgxFOA42BcH6rBGa-Wx3Khpz31EhWjWYX2UWpMNfmI019aA5rb3VDt69ZPs2hqx_GWqi9-fAd2b_4GreaOiT4E6mq-x4WQ1WNSMi_xNQYE9WIsUe46FRD3RJIHCVfsvlTNVAvyacZHSchnIcXD-kzfSmynuLzEwENgXQ_zarPJKBwMTAzsVNB6JpNy8-l_KNlWOmxHSWVHYiGWQJCU0WaZZiZUN2mjldOAk_dPTYLwHuhvm7qrsV4bLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
روبیو درباره ایران:
ما می‌دانیم افرادی که هنوز در بالاترین سطوح آن حکومت حضور دارند، همان کسانی هستند که به همان ایدئولوژی و همان طرز فکری پایبندند که رهبران پیشین آن حکومت به آن باور داشتند.
نظام ایران همچنان توسط روحانیون تندرو رهبری می‌شود.
همیشه همین‌طور بوده و همچنان نیز همین‌طور است
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66836" target="_blank">📅 22:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66835">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd736f47d9.mp4?token=BRuj3x6ARAPp7zMP_wB_A2tiW6YjGhacu3xqvC4RHpT3vBChRpXlxD1x8Zub29qPRnynPdDc7a9l6nkqZvz95e4xTaidxRkaAQ2VNkab8ThvVEYJ_ZdPYWR2ObyYP2Ud57H2SUvjNORJuZbJsyS_DNmYaR46DiBIlVMEGBswaxNr20KU7GbTLfRZPb2az0vIwTOLJGUZ6ZpU0ZutICh187e0L0dQwQv4hXmidb4KPII4cmh9qAUc9j72N7jy51c0ysqlMYn48-Zx9foYFRWtuoP8CpEg0lyZSGnhHziUapvSQaPp0x8Xwq79f5LWElnkcgCxtAjMewkHKLtFVSxaAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd736f47d9.mp4?token=BRuj3x6ARAPp7zMP_wB_A2tiW6YjGhacu3xqvC4RHpT3vBChRpXlxD1x8Zub29qPRnynPdDc7a9l6nkqZvz95e4xTaidxRkaAQ2VNkab8ThvVEYJ_ZdPYWR2ObyYP2Ud57H2SUvjNORJuZbJsyS_DNmYaR46DiBIlVMEGBswaxNr20KU7GbTLfRZPb2az0vIwTOLJGUZ6ZpU0ZutICh187e0L0dQwQv4hXmidb4KPII4cmh9qAUc9j72N7jy51c0ysqlMYn48-Zx9foYFRWtuoP8CpEg0lyZSGnhHziUapvSQaPp0x8Xwq79f5LWElnkcgCxtAjMewkHKLtFVSxaAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
نمی‌شود برای امام حسین اشک بریزیم اما در جامعه شاهد ظلم، بی‌عدالتی، فقر باشیم
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66835" target="_blank">📅 21:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66834">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dm2dEeQh4y_skKjM6wcngDG1C3Sx3amBxupjkJggt70mQz3C87wPfFs2uBumnrMEGbRuvXSoN7l_wKJ1PU41F58xvHafyb0PYsPGQPcD1RFcWZBfCOXRw6vRMd8vElH5wVAwVu6ZXHQx32_ALO7IDQEnqDSC2oaX5l7YwgFbBLKhDkOis7vq34m75r-OirT2OXXG_KqQdXTPzRPNiMAkpOKl-U9PR5nWMaXwoCGH2yCsRXslap9HAqDxlFw7Tuv5UEML0MIm1GV18hpgkVRLDmP3Hl1sNCKPe-gYXLMU3y9VBcxKw9skFnOMhX6pf75rbqwn0Lg7ZasgrBYON-WtvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه پایانی نشست مشترک شورای همکاری خلیج‌فارس و آمریکا:
🔴
تاکید بر اهمیت بازگشایی تنگه هرمز بدون محدودیت و بدون اخذ عوارض عبور.
🔴
تاکید این که هر گونه تجارت یا سرمایه گذاری با ایران باید به انجام تعهدات آن به موجب توافق منوط شود.
🔴
تاکید بر لزوم خلع سلاح همه گروه های مسلح در غزه.
🔴
تاکید بر ادامه حمایت از دولت سوریه در بازگرداندن خدمات، فراهم کردن زمینه های بازگشت داوطلبانه پناهندگان سوری و مبارزه با تروریسم.
🔴
مذاکرات لبنان نباید به نتایج دیگر نزاع ها مشروط شود
🔴
حملات متجاوزانه گروه های شبه نظامی مورد حمایت ایران در عراق علیه کشورهای خلیجی محکوم شده و از تلاش های دولت عراق برای حصر سلاح در اختیار دولت این کشور اعلام حمایت شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66834" target="_blank">📅 21:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66833">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/965348f417.mp4?token=CH7x9TwX3aIKYg8M10Weplll_oP2qMI_f30n8chzeCwlRDMEVtwdiDl0PTk0kGNQB_IijCujLlDt-lCAhHjIEUVtjRCjrjsvz_asOLWnOEA8EUhnr-uiKqBl3finE_VZ4kNxapAt3MMaP48iJn3Qbifgy-wd237_CNPXjhgEM42Mrdc6C-wGB0-l0YhpqqOhh9yy1nTiJdlutoBR_TXNBfu6y26CCPm7Na-VwER1A-e2rn2AZ07GM6yCtYVDjQT8y5kpeZN6SqpBe4Jyp84SAqvVl4nh6tSuL8lc97BAGxcg4vj_TURENcaG6MdNrLil8JK0pU1Flks8PAPHBgV5ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/965348f417.mp4?token=CH7x9TwX3aIKYg8M10Weplll_oP2qMI_f30n8chzeCwlRDMEVtwdiDl0PTk0kGNQB_IijCujLlDt-lCAhHjIEUVtjRCjrjsvz_asOLWnOEA8EUhnr-uiKqBl3finE_VZ4kNxapAt3MMaP48iJn3Qbifgy-wd237_CNPXjhgEM42Mrdc6C-wGB0-l0YhpqqOhh9yy1nTiJdlutoBR_TXNBfu6y26CCPm7Na-VwER1A-e2rn2AZ07GM6yCtYVDjQT8y5kpeZN6SqpBe4Jyp84SAqvVl4nh6tSuL8lc97BAGxcg4vj_TURENcaG6MdNrLil8JK0pU1Flks8PAPHBgV5ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
فقط یک آدم کور می‌گوید هیچ دستاوردی وجود ندارد. دستاوردهای عظیمی وجود دارد.
من همه آنها را فهرست نکرده‌ام چون می‌خواهم شما را نجات دهم. شما اینجا زیر آفتاب سوزان ایستاده‌اید - فهرست کردن همه آنها زمان بسیار زیادی می‌برد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66833" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66832">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0J4m7ZtyuWxj8PMAdFOSR21Y1e--yjrgtV_VEOMLZ6qxTxYN5MlqAzXoOnbZrtySATY2ekmgbquDGE31pz64zZQ1xH2G-jqptmLaQiQN3PPygLUQok7LD3YcywAtGpw7KYsosoE4CPpu_CCnwtFpWB8AW0Q5WrON4eUlXwCjz-rHdOPI3j5S8F9c3vKESup1wQLxZycCgszD0ACYlB3fmTtAxspMTmYHNZg6Ak52evG6xW9K6XJzN3yl5b_h1uoTqJh4yaukfFNswRKvKcV50dATNvUraOAZ-HCIky6p_MojGgF3EOP2NYtzT300yIqW7se2FYyspVnkjTNFONvMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
با نهایت تاسف از وقوع زلزله در ونزوئلا. مراتب تسلیت خود را به دولت و مردم ونزوئلا، به ویژه خانواده‌های قربانیان، ابراز می‌داریم و برای مجروحان آرزوی بهبودی سریع داریم. جمهوری اسلامی ایران با مردم ونزوئلا ابراز همبستگی می‌کند و آماده ارائه کمک‌های کامل است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66832" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66831">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">این آمار فقط مال روز اول جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو پلنگ بت جویین شو بهت آموزش میدم چطور پول دربیاری و تا اخر جام جهانی سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet @palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66831" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66830">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwJmv_LX_PH9Wt5x7I4FtLznHpbeW0mQpU8A-Thzfpwvl4keth9dMp2KGYVg7bffiry4hc_2jKo87G1vCOKts-TOKaa9GoO0VKgpZUUkPDvNB48DTmlcmDuyvtUpGBFhW4shZvkgR0rfaxjQ3V6c9R8P0elnphSLiCKXc3I0xI40JwnUxuOqfmiWRft5g7V0hxEIFdjHEHuwVzrSRyJmaJur8dlKRQxTFoooPWf1dK_PlCpt095GH2N0zHZC_EwvQo8FlFyQsRkbEr8z8cvgsaSJqGz4xshfMIfm2y1wHVG0O0Xro-D8OocGd7pChNWDuwfJLwAQvMwi4V9ZsvCYyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این آمار فقط مال روز اول
جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو
پلنگ بت
جویین شو
بهت آموزش میدم چطور پول دربیاری و تا اخر
جام جهانی
سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66830" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66829">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c8c286a22.mp4?token=vR5IPMukM5gtvdY78U7RFsyeeMmhBkW7KaMLumD-gxqI1fCuJHpWr7SX_zHMIMI7mdjh8ffcKg_jf53VRlRk_5waV-7eFqxOOQlUmRvGLTsF7Td2GNAFfbBYFTEx8XlqHmMT7miK1D-KSPcj-Ql5S51A_GZEWwfz_Tfi1oHrWP3KMbEEQUNlCp65FTUE6V5kd6s6wCIkxy1K1XaMPN79TKNTFvfAv1jt2JmsfJ4McUa4bIOFhoTOHwdwVunBXhc74wbbpNp_zLp9tF0SlBqkMvw5G2pReQO0-f2ifT8ZNRsV_Gn3MKp34Gad9k8uiT5at4bLtkb1HAAXXyqK6juBnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c8c286a22.mp4?token=vR5IPMukM5gtvdY78U7RFsyeeMmhBkW7KaMLumD-gxqI1fCuJHpWr7SX_zHMIMI7mdjh8ffcKg_jf53VRlRk_5waV-7eFqxOOQlUmRvGLTsF7Td2GNAFfbBYFTEx8XlqHmMT7miK1D-KSPcj-Ql5S51A_GZEWwfz_Tfi1oHrWP3KMbEEQUNlCp65FTUE6V5kd6s6wCIkxy1K1XaMPN79TKNTFvfAv1jt2JmsfJ4McUa4bIOFhoTOHwdwVunBXhc74wbbpNp_zLp9tF0SlBqkMvw5G2pReQO0-f2ifT8ZNRsV_Gn3MKp34Gad9k8uiT5at4bLtkb1HAAXXyqK6juBnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو:
من ادعا نمی‌کنم که پیامبر هستم.
اما فکر می‌کنم می‌دانم چه چیزی بقا را در منطقهٔ ما ـ و به‌طور فزاینده در سراسر جهان ـ تعیین می‌کند:
قوی‌ها زنده می‌مانند.
برای ضعیف‌ها جایی وجود ندارد.
آن‌ها طعمه می‌شوند.
و از میان می‌روند
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/66829" target="_blank">📅 20:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66828">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d4c620ba.mp4?token=O4QCZlwpXNBXUd2JP3gWj4stwj-hhQdVK8_llI9vVFen0x7nQrlgGZEXJk-symLbTSEGwOqic1zP3Pt-_ulIZACbKpE43Peq9E64VizSStMFehQEgevzrU2yZJ6lfc53X6Jefp_BACz-z1byjaFF1_2qtmJ8e3jwXzPBDrNtuDMFkmsJhWevUXUVcRcWEC1IL0jiWX0OvSIvEpY3KfvbPpYcWBwCaAQIgTHrDumw-Qo2bpgXIobPgXjttKdglc2p9tz2GEImtRkoldA_781EoSJF3UWAs0NtqxG4Bw6ERg9DuNPQIm9LCGHXQixLn49M2OZ39IggzlhnhCcVROM2xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d4c620ba.mp4?token=O4QCZlwpXNBXUd2JP3gWj4stwj-hhQdVK8_llI9vVFen0x7nQrlgGZEXJk-symLbTSEGwOqic1zP3Pt-_ulIZACbKpE43Peq9E64VizSStMFehQEgevzrU2yZJ6lfc53X6Jefp_BACz-z1byjaFF1_2qtmJ8e3jwXzPBDrNtuDMFkmsJhWevUXUVcRcWEC1IL0jiWX0OvSIvEpY3KfvbPpYcWBwCaAQIgTHrDumw-Qo2bpgXIobPgXjttKdglc2p9tz2GEImtRkoldA_781EoSJF3UWAs0NtqxG4Bw6ERg9DuNPQIm9LCGHXQixLn49M2OZ39IggzlhnhCcVROM2xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بنیامین نتانیاهو: در مورد رژیم ایران، من فقط یک چیز خواهم گفت: با توافق یا بدون توافق، تا زمانی که من نخست‌وزیر اسرائیل هستم، ایران هرگز سلاح هسته‌ای نخواهد داشت. به هیچ وجه اجازه نخواهیم داد ایران بمب‌های هسته‌ای توسعه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/66828" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66827">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته  جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn @kaviani_vpn</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/66827" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66826">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N44UMwe8q28-Q-74uWtaP9m5w__GCj3Ww9kHgjiIC3AkfJ7CyxAl4HIRuAnEcRiRUBug1HDGlLLeCzlUlk6AV-PS595ZR-GZWDKzN-NjXwBVl_d4OUO4nDg-2VB2b4324kI0Z9MJpUH_6anTjhEoJMsqJEYIAsPpIZ1Za2jeYih8tJ1DkK5xjpLEV0ZMC1VTfXz_YYU7fDK_YD8f718NDWN3-muN4ZZ3xdXto2fcdiC8LFVkqz_nboxKeX24dp5MowKHIm7mgyzRL9PgFrXFm7Wg4igr7zhjwRNfReqQBUyOS7hFlvO5owzjlkoNxr_BCxfuMDumMlU8imPW6F9F7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66826" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66824">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9rLnnOpRbRFRIi9bWm-WTH33ymeMhTy4Uk32nYXo7PfKtzFIJfD39pjvIP2Z0bEIWYDmoOHZNtL-kRe8bp1N_t7uCIpIHczSVBomz_4R0nip1WXShrxZEnfNzlsKp82woncB6rPj24p6RdfCDU6hha5uGNMkh6BOFz-F0WaGeW3D9NJPvZeGwjmBbKB2iY4eEAVfvba8wQfwAFvfY2ESDcctAty2aDC-UDEif1zC4IHAQZrYDCYoNfPfkbwlbEleupFqIlSf7Huw90bqmhlBQlrsP8FE8h0_dDzneqKs3eW38tpvbsjm8-fvrtavROfo4nGLPd5nuPqh_hgnPTF4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1b8ae4df4.mp4?token=hWzZ4jkwFGQ0maNNNkdFRm3jFG6A0ulLnJ-lknMbs8aY3uIqW9cAG56B258HBKbkG7_4AJv09YX_FSHDLc_ZbXHCkkzsFHlcnlaxDnQRFLzSU7ahu0-blKscUm8OZzT3xkGPg8oXf1ovOm_8N9MJv8jTijrVO8l2mAfROcaI8uWJ2DNbyVmvvqUwA5N0i41k4n47B1hwr2I8nFVEpFWuRJ2hXhOShOV02T_1gHXwM7owTqcWf4l3WE_Yw0ue_H9Q1BRa2IbKda08vMUoOg4Y8R0-adjjyWGT3hX1LpRTC9chdAUYD5cx5JNkI08qyF5-552OlyG5AIyx3TZrjvnQEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1b8ae4df4.mp4?token=hWzZ4jkwFGQ0maNNNkdFRm3jFG6A0ulLnJ-lknMbs8aY3uIqW9cAG56B258HBKbkG7_4AJv09YX_FSHDLc_ZbXHCkkzsFHlcnlaxDnQRFLzSU7ahu0-blKscUm8OZzT3xkGPg8oXf1ovOm_8N9MJv8jTijrVO8l2mAfROcaI8uWJ2DNbyVmvvqUwA5N0i41k4n47B1hwr2I8nFVEpFWuRJ2hXhOShOV02T_1gHXwM7owTqcWf4l3WE_Yw0ue_H9Q1BRa2IbKda08vMUoOg4Y8R0-adjjyWGT3hX1LpRTC9chdAUYD5cx5JNkI08qyF5-552OlyG5AIyx3TZrjvnQEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فستیوال محرم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66824" target="_blank">📅 19:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66823">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/113cb570d9.mp4?token=AUueXeZa2trxVeIFV0dn_Gj45Yve3zwE455JTKnDjSiDTPN_J1eH0C3C_D5oZSpjfHFEBkR4S9vSqUqDh6KmHH7YwpnQmCzt1eLEHUWRLn7LOOrpjy3uQpanAaoGTG7hdm0jzES0njUzH3_vvbtwTe9sFg-2j5dp4733w2sepmGoIkW9A6x2tu3xk1I1eFV6OMckxRV3fudyX0n46GXappYWMhVA4pJ0oWwVtfvYcWauv9OvFH06SqQugoXbK8pl9lE2D05aXmk32J6w5TbyzToMsvl-zhxIKF-GwuvU_7YNJ6Xn9Jhn6yIuN4mv7U7JXFQOnaIBcVqpAEgJ7bIoxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/113cb570d9.mp4?token=AUueXeZa2trxVeIFV0dn_Gj45Yve3zwE455JTKnDjSiDTPN_J1eH0C3C_D5oZSpjfHFEBkR4S9vSqUqDh6KmHH7YwpnQmCzt1eLEHUWRLn7LOOrpjy3uQpanAaoGTG7hdm0jzES0njUzH3_vvbtwTe9sFg-2j5dp4733w2sepmGoIkW9A6x2tu3xk1I1eFV6OMckxRV3fudyX0n46GXappYWMhVA4pJ0oWwVtfvYcWauv9OvFH06SqQugoXbK8pl9lE2D05aXmk32J6w5TbyzToMsvl-zhxIKF-GwuvU_7YNJ6Xn9Jhn6yIuN4mv7U7JXFQOnaIBcVqpAEgJ7bIoxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
قالیباف پاسخ مجری صدا و سیما رو داد
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66823" target="_blank">📅 18:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66822">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0453856b46.mp4?token=OU7iPW8GrwvE-svYvARVUI1qg8IkuNydViqCm4_Ukcldrvua1_arlSo-zEy1SPPzTXgvPi_Zb6O0jL_DKfcCMLt3WO5zBT7dJ_653AdUy-ympsLqEmVozK_22AJVqEtuqdihbq3L0jPXIjU-i2dgBtjRbcbj1jWt1v2JrYYN3ShbulCZxsupQ95qFN4ZPwtyUeiZ-bZpjjcTyaHs63jcP8pm__INqqPUQZozAe6-GOuR5neNAJdXpCHP_lbQ6HwTDzZaVpLY8JFFsiLrrkwpKGzEzUYdfSImmb3n9j2cGV3dUTm1SLM0wHQ2ouINeUPJQE_S9cBMuQcJUscr7g_X7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0453856b46.mp4?token=OU7iPW8GrwvE-svYvARVUI1qg8IkuNydViqCm4_Ukcldrvua1_arlSo-zEy1SPPzTXgvPi_Zb6O0jL_DKfcCMLt3WO5zBT7dJ_653AdUy-ympsLqEmVozK_22AJVqEtuqdihbq3L0jPXIjU-i2dgBtjRbcbj1jWt1v2JrYYN3ShbulCZxsupQ95qFN4ZPwtyUeiZ-bZpjjcTyaHs63jcP8pm__INqqPUQZozAe6-GOuR5neNAJdXpCHP_lbQ6HwTDzZaVpLY8JFFsiLrrkwpKGzEzUYdfSImmb3n9j2cGV3dUTm1SLM0wHQ2ouINeUPJQE_S9cBMuQcJUscr7g_X7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
🔴
اگر کشتی‌ها در حال حرکت باشند، واکنش ما هم بر همان اساس خواهد بود.
اما اگر کشتی‌ها حرکت نکنند، این نقض توافق محسوب می‌شود و در آن صورت با یک مشکل جدی روبه‌رو خواهیم شد
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66822" target="_blank">📅 17:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66821">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50938460f0.mp4?token=uS1ft07y38uI-sn7aoU9VzZlx-9Y4Ap7KBfWh4-vxCUcitPXxDlqlYwh9o9PeeohaJiSXzXXbTzm31X6ZGZI5XXou5id1FKwCEIZ2eLgerkwNytGUorBVqt36Ekb5E9-jhYVXGG1QodrvgBtE4FPeBGnVsb8FwB2vj8sCXD545Wk-brNQvisbdOTaNhNGk7R-fwr4e-_q1NawjTKvV40sf6tllOpW5QkUlGi70If9yvFjFRMNy4_qOOTJij5dS6I4DnIaA-8JGpSj6i-n4alSiA1rkoFsb3DVNFTecmb0lWFTHAunTJ_jvYIPVLszBhLyd8k1nI2lpvZP4k5HO57oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50938460f0.mp4?token=uS1ft07y38uI-sn7aoU9VzZlx-9Y4Ap7KBfWh4-vxCUcitPXxDlqlYwh9o9PeeohaJiSXzXXbTzm31X6ZGZI5XXou5id1FKwCEIZ2eLgerkwNytGUorBVqt36Ekb5E9-jhYVXGG1QodrvgBtE4FPeBGnVsb8FwB2vj8sCXD545Wk-brNQvisbdOTaNhNGk7R-fwr4e-_q1NawjTKvV40sf6tllOpW5QkUlGi70If9yvFjFRMNy4_qOOTJij5dS6I4DnIaA-8JGpSj6i-n4alSiA1rkoFsb3DVNFTecmb0lWFTHAunTJ_jvYIPVLszBhLyd8k1nI2lpvZP4k5HO57oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
🔴
فرض کنیم که ما کاملاً دیوانه شده‌ایم و عقل‌مان را کاملاً از دست داده‌ایم و تصمیم گرفته‌ایم با ایجاد یک سیستم عوارض یا دریافت هزینه موافقت کنیم.
این قرار است چطور کار کند؟ اصلاً شدنی نیست. چون اگر کسی هزینه را نپردازد، چه اتفاقی می‌افتد؟
فرض کنید یک کشتی بگوید: “من این هزینه را نمی‌پردازم.” این مثل عوارضی یک جاده نیست که بعداً یک قبض جریمه برایش ارسال شود. به آن شلیک می‌کنند.
اگر به یک کشتی شلیک شود یا یک کشتی غرق شود، دیگر هیچ کشتی دیگری حرکت نخواهد کرد.
بنابراین چنین سیستمی نه‌تنها غیرعاقلانه است، بلکه اصلاً نمی‌تواند اتفاق بیفتد.
حتی قابل اجرا هم نیست. پس بهتر است همین حالا این خیال‌پردازی را کنار بگذارید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66821" target="_blank">📅 17:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66820">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9ZDqQ6PiU7tzQrIC3HNcDnCkcaLSnthUUXQSiX1qt4acX0qToTK024HIO8bSFyOoeGI7R22wYqXtTeQiV13lM-06ZRFgJmwDPMtTa7ThqRVkJklw6Nf6eAa0Kk_vVJvYrtG3zRpzmqpAwjbb0WBgYCGnvnaa130TGvfjzF5rxoJPPJ0akffUd2VBN8dY7GCIWD-iK0tj6L_mamQZjnThuQ643WdTl4zo2aUAt_o-nztqzRwuFAVUUPrY06t0Q1e1whhmFhaO9fJXRSwgyI2CMXIujSSi40B86ziFYb-uTn8YtqyxtdWLQO7y2GMTZpPq9ihNSNi0Dtyzfe4ZyWRyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
آمریکا به دروغ ادعا می‌کند که دارایی‌های آزاد شده ما، کشاورزی آنها را می‌خرد. جالب است. تنها محصولی که ما برداشت می‌کنیم همان چیزی است که شما کاشتید: دهه‌ها بی‌اعتمادی. این محصول ارگانیک، فراوان و تولید داخل است. اما ظاهراً ایالات متحده فقط سویای تراریخته، وعده‌های عمل نشده و حرف‌های بی‌اساس صادر می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66820" target="_blank">📅 17:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66819">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/477cde7837.mp4?token=TSqdNW8r6pYNFOa-eJbDlnXLuH3jRkxvD1CT4Dsg81MK8GOh7poy5JaWi9Rrg8a-pRcp1ptipdyYWzz5ve1rH6p8iW6RsUpIAx0IWwtA6G2ElPNrlgpZUOe1a7rLy0mBcNH-OwouObTzBNdyLJBMcPA9G1kFZTLbI5-h4BiZBSYkeTTFcrOybyXuYymv6Ek7slnQHXJLNVXGDQrcoCZs2Ue9eNMG_Ubzri2fyDYfGFtUU03K8pooVUNZ4lKgitOqcZT5zUHXFiLLkw4kdyXW9qjqu0gmQtugCk0_d6zHQwu0iBPl_2ykdGE3kTe4jpuevTBTpOltCgF6Ms24KYSlFTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/477cde7837.mp4?token=TSqdNW8r6pYNFOa-eJbDlnXLuH3jRkxvD1CT4Dsg81MK8GOh7poy5JaWi9Rrg8a-pRcp1ptipdyYWzz5ve1rH6p8iW6RsUpIAx0IWwtA6G2ElPNrlgpZUOe1a7rLy0mBcNH-OwouObTzBNdyLJBMcPA9G1kFZTLbI5-h4BiZBSYkeTTFcrOybyXuYymv6Ek7slnQHXJLNVXGDQrcoCZs2Ue9eNMG_Ubzri2fyDYfGFtUU03K8pooVUNZ4lKgitOqcZT5zUHXFiLLkw4kdyXW9qjqu0gmQtugCk0_d6zHQwu0iBPl_2ykdGE3kTe4jpuevTBTpOltCgF6Ms24KYSlFTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویرانی‌های بر جای مانده از زلزله مهیب ونزوئلا در شهر کاراکاس
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66819" target="_blank">📅 17:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66818">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyY-weTMQyUB_jlcoA-cJe1HPLcyp92ToF0d0GalcwMeVCDJbEtwnMUcC3ZrJErRhn_5Iqp-93fBxxKHx_j-TNOmF9An3pDlMv0AOjuNf1pFuqgGzZNo3In_hRHsJtMU0UEE7uq1nkgKPGzErhA4rb_XQT6sWA9Xzx_zqRdw1DBC3KBWclnlOn9hF4QyNqH9LtKcUhRQNqsdafsQdFreKdrmPp6QH39LnG8yZqPVVupKE1esMOiSgjNcosG7TfXVm2IoqWhFqS2XIxDvQbn8PTrEl9wKKSU6AWSoykgoXmqwkK-K6zMWQQYHr5bOS-QXmayz4ax-TFekX_M0VrGbiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل قاآنی فرمانده نیروی قدس سپاه پاسداران:
اگر اسرائیل امروز داوطلبانه از جنوب لبنان عقب‌نشینی نکند، فردا مجبور به فرار با تحقیر و شکست خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66818" target="_blank">📅 16:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66817">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4301a5bfb2.mp4?token=JCs_n_gONWPccUK4gopH5gX6KKIxMc44Iu0J-KkD-PE0jfvIV5gGYNEYNgxuq57v5paE2Uj8mmWWy0D2l41_4Lj3FhDeR-hXUHS4HPzf9KHYgI9gyaJylWRTKVqphGKjiFtaTyawGm6H0JLkDuWe3k-BSUS_xDO32H6CYvPNxvn3XACXyMqk4x-W3-HEo9uBiOzUAIFFFk9VAf9swyC_Usid_Lsbl5RfhzihiW48Eq0DVwRM13S_i9yq-heydr1xNG9hQL75LHXP0GVGwnV19mUc27nE3OoU0Lq9ZwJ8tsB3v2Mc1VggVsIyTjrxX7hNsKmaRMDinj2dAa0E3YPpjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4301a5bfb2.mp4?token=JCs_n_gONWPccUK4gopH5gX6KKIxMc44Iu0J-KkD-PE0jfvIV5gGYNEYNgxuq57v5paE2Uj8mmWWy0D2l41_4Lj3FhDeR-hXUHS4HPzf9KHYgI9gyaJylWRTKVqphGKjiFtaTyawGm6H0JLkDuWe3k-BSUS_xDO32H6CYvPNxvn3XACXyMqk4x-W3-HEo9uBiOzUAIFFFk9VAf9swyC_Usid_Lsbl5RfhzihiW48Eq0DVwRM13S_i9yq-heydr1xNG9hQL75LHXP0GVGwnV19mUc27nE3OoU0Lq9ZwJ8tsB3v2Mc1VggVsIyTjrxX7hNsKmaRMDinj2dAa0E3YPpjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
نیروی دریایی سپاه:
تنها کشتی هایی که از تهران مجوز دریافت کرده اند حق عبور از تنگه هرمز را دارند و با هر شناوری که از این دستور تبعیت نکند برخورد خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66817" target="_blank">📅 16:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66816">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_ps8W58eYD1r2s7d9bdmgDMX_OpklUz5ZOoUn5WYNxnpi5OVfldGeOXe7MnydXLJxBR0xz5_wdBrqnmzYtock9bANGgyFV2TEUIzn0CN5HNO3ognUczl0vUb1MLaBSEmF6SglDGTNwoYklf3wCFdNGkzXsBJ3DyoS7J3e6oRMWUh8bsOEGrXDCjJjS61bjaroxgeq_uOTn54Qht5hvW0pr04SeyZuS973eOOQYDZzJILVOLDsppVoCYPS0v4eGLgeJO8Oqb-mabn389qzTFhVEsjoJG34P8W35HXdp5HwMfZSLZiqudhGh3F1jwFd8PC4pfDi07XLtJfS8Zg7_wzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت
ترامپ در تروث سوشال:
«شگفت‌انگیز! سنا رای خود درباره ایران را از ۵۰ در برابر ۴۸ مخالف، به ۵۰ در برابر ۴۷ موافق تغییر داد. رند پال و بیل کسیدی رای خود را تغییر دادند. از جان تون، لیندزی گراهام، برنی مورنو و همه سپاسگزارم. این رای به ایران هشدار می‌دهد.»
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66816" target="_blank">📅 15:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66815">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
خبرگزاری رسمی عمان:
وزیر خارجه عمان اعلام کرد ترتیبات آینده برای تنگه هرمز شامل دریافت عوارض از کشتی‌های عبوری نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66815" target="_blank">📅 14:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66814">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a64b900d33.mp4?token=KYTFaoXmXjL-c5CcA5QQaeInBn2AbH0zxPs3iUBRIhC06v4onVkokOgTcQx6BBHPNyA02-f5Vi-W7tPi3skhVhvoAACwWxmJ89O41wxipWPAo2bjFT8P6CqVZfqyZuEigSE0YXfWoL9YOH2acER-gl3X_1lSn3TxSikIxFKKrfN4UibKjeiedsk1QB2JEUfFt6p10hfqOimbPNA1tNh3o70AAGiEwLJdeKMclyKXQqEyEeMbfQNo9hJon19p2S1-Y7XicoA22cwHXW2xBtm4T5S2lpDxCR6N_WuPWCQbeGQkjA6vd5IK4TfI-fDXF-Re0LSQT7GsD2gDaXDATsxogA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a64b900d33.mp4?token=KYTFaoXmXjL-c5CcA5QQaeInBn2AbH0zxPs3iUBRIhC06v4onVkokOgTcQx6BBHPNyA02-f5Vi-W7tPi3skhVhvoAACwWxmJ89O41wxipWPAo2bjFT8P6CqVZfqyZuEigSE0YXfWoL9YOH2acER-gl3X_1lSn3TxSikIxFKKrfN4UibKjeiedsk1QB2JEUfFt6p10hfqOimbPNA1tNh3o70AAGiEwLJdeKMclyKXQqEyEeMbfQNo9hJon19p2S1-Y7XicoA22cwHXW2xBtm4T5S2lpDxCR6N_WuPWCQbeGQkjA6vd5IK4TfI-fDXF-Re0LSQT7GsD2gDaXDATsxogA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره اردوغان:
🔴
او دوست من است و از جنگ دور ماند.
می‌دانید، او یکی از اصلی‌ترین گزینه‌ها برای ورود به جنگ با ایران بود.
شاید هم در طرف ایران، چون همان‌طور که می‌دانید، او طرفدار  اسرائیل نیست.
و من از او خواستم که وارد جنگ نشود. او هم وارد نشد
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66814" target="_blank">📅 14:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66813">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klbWPBbOCru-YG5WIRpBVXeSQwg396jWru-b2Fy8Ma16mmZ-duBOzmUpWbZkWmHNS9iHuD5I85HLTEBmQ4J_X9Vs3HA-QZUGITQP_yR9huaJ_XrVIW9oKRG8BEPKNQw602OCW6RJvFCil0dpVqD-FzJPC-sf6Y_c023hMZETlOA1Fx1EItbiPtMjfk8Xi8Rr0_PVYe9_YftkLCNdzdYPNpe4oHhj-8Ox9Pzdg7xQqdlRHDzVFmgKmnafUrLkkB5hJHcsBOqUAx1lBW8rOGXeA8JOFjNkSR9u1d6c5xV9eoxtLMpVSGHlXGzlNODusFst4a5To1KoP_aebDeEuF2ftg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو:
🔴
واشینگتن خواهان توافق با رژیم  جمهوری اسلامی است، اما نه به هر قیمتی.  هر توافقی باید واقعی، قابل راستی آزمایی و همراه با پایبندی کامل به تعهدات باشد. اگر رژیم جمهوری اسلامی به جای صدور ایدئولوژی بر رفاه مردم ایران تمرکز کند، آمریکا و شرکایش آماده همکاری خواهند بود، اما انتخاب مسیر کنونی نتیجه مثبتی نخواهد داشت. هیچ توافقی نباید امنیت، ثبات و شکوفایی شرکای آمریکا در منطقه خلیج فارس را تضعیف کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66813" target="_blank">📅 14:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66812">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0835d639a.mp4?token=dGDVQ5F-ny3ka_McqkzhOXbQgODx_n4obvQh7E3hKf-mqrTMro2VTnydx58yt63b-pCHdUJC051nb-IAlAQT_wGAXwQtqxLy6q_Gp6DVbzZNj70xbZooupqVdN__xBeKyqinUpCFcJmjK9h2mNbU5Yk56gBIw039MzMJLb5_MxYtvebIdHnZYiJM2lfaZdprYErBE_MF11W41tSH0UlMqwm0YJxKYvU79KMPMUn5-zvBaDbQfcb9zmHDRKX04H1xkIIZarY-NMC_ocK5gvmeqeXXKjOAiAEnzQBncEpYCP6lNdAK6SlCYPVTiWT5mBTQOAedHDdo1cebNhyT8zcQFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0835d639a.mp4?token=dGDVQ5F-ny3ka_McqkzhOXbQgODx_n4obvQh7E3hKf-mqrTMro2VTnydx58yt63b-pCHdUJC051nb-IAlAQT_wGAXwQtqxLy6q_Gp6DVbzZNj70xbZooupqVdN__xBeKyqinUpCFcJmjK9h2mNbU5Yk56gBIw039MzMJLb5_MxYtvebIdHnZYiJM2lfaZdprYErBE_MF11W41tSH0UlMqwm0YJxKYvU79KMPMUn5-zvBaDbQfcb9zmHDRKX04H1xkIIZarY-NMC_ocK5gvmeqeXXKjOAiAEnzQBncEpYCP6lNdAK6SlCYPVTiWT5mBTQOAedHDdo1cebNhyT8zcQFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حتی در کیس بیماری هم عجیبیم
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66812" target="_blank">📅 14:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66811">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce6df862a9.mp4?token=OEcolkqvzXWCxQDwzIMV379PDVcAz6hulDKtslBreyoIWN19xTeNtql4dXQhTOTq0LfDMkCjVPXhdvhd_NnpR4kq0HfoiO5GYR-1LsqWKDHQ3DaeYzioYMXnFsUczTkuWYA0eCbqzPZ1oHCXXf2RdcuWHXhuwbY1n7PfqDuuLogmGhmKhJ5IG-2W3ylARVCe9zbc-9hHMysNScIi_HOVy5okouZZjnPxhnjgEFRP88EE8wXkW-gfaMmfIpSeGLgpDFPYFRaq5Zwb-W8-dtbN1n1yE58cFDZVOEYk4QVYJYPbPhkD9_82Y7tE7Re-D1rsWtCEio7XZ2qIoFIGVBkndw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce6df862a9.mp4?token=OEcolkqvzXWCxQDwzIMV379PDVcAz6hulDKtslBreyoIWN19xTeNtql4dXQhTOTq0LfDMkCjVPXhdvhd_NnpR4kq0HfoiO5GYR-1LsqWKDHQ3DaeYzioYMXnFsUczTkuWYA0eCbqzPZ1oHCXXf2RdcuWHXhuwbY1n7PfqDuuLogmGhmKhJ5IG-2W3ylARVCe9zbc-9hHMysNScIi_HOVy5okouZZjnPxhnjgEFRP88EE8wXkW-gfaMmfIpSeGLgpDFPYFRaq5Zwb-W8-dtbN1n1yE58cFDZVOEYk4QVYJYPbPhkD9_82Y7tE7Re-D1rsWtCEio7XZ2qIoFIGVBkndw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حدود ۷۰کشتی در ۳۶ساعت گذشته از تنگه هرمز عبور کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66811" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66810">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.2 MB</div>
</div>
<a href="https://t.me/news_hut/66810" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
نسخه آپدیت شده اپلیکیشن ملبت
🔶
• لینک سایت مخصوص کاربران خارجیMELBET:
🌐
t.me/ConnectMELBET
🔶
• آدرس سایتMELBET
🌐
bitly.uk/connectmelbet
🟠
نکته: اپلیکیشن بدون فیلترشکن کار میکنه برای ورود به سایت باید سرور فیلترشکنتون رو کشور های اسیایی یا کانادا یا ترکیه تنظیم کنید</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66810" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66809">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CECpNCUPkl55esYvKy8oge3OFXPVj5np_1g6gxr3zzEIHeWqCZVS5eImykDNh2mJLDY_WUulvIgw7l3ZJbxkqAbcnxUT6FUM_CurZc10eglfsH1LvmVi8kVQD6NmyHQ_tw1pDyyYcRnCqPC0pk1UdkalOzXAcIpzf8spg3sk6ZTsXZ4Aj41ymIz-mK_RWbevHUw5YLfUns6PXkDuVYg1hyx6ViOr342qVPLd-5-5lb-saCD7hXtzZXCdAhv-NFoVBZLlgmVdTiSahroeunm99vrxdR0CUApyNuSY7-tG3Y8dgSGrv65RVXd0lrvlSXRZuOrR0O1YuMa1fuGtvojlnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
بهترین سایت برای بت زدن سایت MELBET هست که مورد تایید ماست و خودمونم چندین ساله توش بت میزنیم
💸
با اولین واریز اگر با کد هدیه
ml_459049
ثبت نام کنید تا سقف 100 دلار 130% بیشتر شارژ میشید
واستون لینک و اپلیکیشن ملبت رو میزارم که ثبت نام کنید
🌐
https://refpa3665.com/L?tag=d_3312431m_45415c_&site=3312431&ad=45415</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66809" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66808">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ead28978b.mp4?token=ZQLNvSbxLn0lmwIzFjb5qQaDaN8tT6qgkof9TaGv5Nd2HDLmWuceMQE7ou0ihWA6wkm5DPf0u-160-FcipN-ZBNbSPuWJAGHd41IcoaGOSKTeElYQHt_lrVrHuRo7qdaZpFZEdsFD43l2crgrp8GFFXkUihtruwMvWU4SDf_w0FdCQhRslBOg_S3YTU0-NgaO70Jh1vFkRWaVvJvOH-_Par3iFDHHVuSOfo5bif8IQxFetHgZdfDaF_zlSEvoNUt51WIudBiR8Iuyb7rczWUp8QDjNcS_ZWOFY2JOnhPI6VDGZvC2uMIsK_qsyIHmljHWIluIvsq2OAUxMSVhOTmHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ead28978b.mp4?token=ZQLNvSbxLn0lmwIzFjb5qQaDaN8tT6qgkof9TaGv5Nd2HDLmWuceMQE7ou0ihWA6wkm5DPf0u-160-FcipN-ZBNbSPuWJAGHd41IcoaGOSKTeElYQHt_lrVrHuRo7qdaZpFZEdsFD43l2crgrp8GFFXkUihtruwMvWU4SDf_w0FdCQhRslBOg_S3YTU0-NgaO70Jh1vFkRWaVvJvOH-_Par3iFDHHVuSOfo5bif8IQxFetHgZdfDaF_zlSEvoNUt51WIudBiR8Iuyb7rczWUp8QDjNcS_ZWOFY2JOnhPI6VDGZvC2uMIsK_qsyIHmljHWIluIvsq2OAUxMSVhOTmHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
بسیجی‌های صادراتی دیشب تو میشیگان آمریکا نذری بین آمریکایی‌ها پخش کردن
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66808" target="_blank">📅 13:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66807">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba9d2db1fa.mp4?token=nhFCL63OFbHjZUmRsrvAbZbo0fr3LL7_CSO2YYNv_df1EdY0zxCn_KQGV9becVM-7yYGHBgVYTl2ekA0h3s5D7yslSfpZhetyBFH7t5t_zkLyhz7ykMvP9ml0CnJSUxbr-WUzo524Meza8JfX7-aLxRjPZDEbMAK8GBGhqjEvow1ZWmInIg_XSGhgn33X5E7O5MWqJtRZQu6C9lIwG6TF6f4zEJbBPJ7cdWa3UOF2bkko3_3Gy2htUE11IyFVPISIq2G8a8wPZfj-iZSSYYclJ24UBenaeaYTHzsJKCUFQG5tWAd7dxeIPlmcqqkivF2UrhIq16oqSoUmBYatQ0JyIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba9d2db1fa.mp4?token=nhFCL63OFbHjZUmRsrvAbZbo0fr3LL7_CSO2YYNv_df1EdY0zxCn_KQGV9becVM-7yYGHBgVYTl2ekA0h3s5D7yslSfpZhetyBFH7t5t_zkLyhz7ykMvP9ml0CnJSUxbr-WUzo524Meza8JfX7-aLxRjPZDEbMAK8GBGhqjEvow1ZWmInIg_XSGhgn33X5E7O5MWqJtRZQu6C9lIwG6TF6f4zEJbBPJ7cdWa3UOF2bkko3_3Gy2htUE11IyFVPISIq2G8a8wPZfj-iZSSYYclJ24UBenaeaYTHzsJKCUFQG5tWAd7dxeIPlmcqqkivF2UrhIq16oqSoUmBYatQ0JyIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنوز تو این دوره و عصر مدرن یه سری کسخل وجود دارن که با عقاید عصر حجر خودشونو بگا میدن
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66807" target="_blank">📅 13:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66806">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81f4c39a8d.mp4?token=u0z-_yRIfmgi2facqwmPdfvC0GUBTpl6MDzPwsCSBMBXtllALz1izfszT-y5I8YKcBDCTmK17_4fyM1XP_AUBQV0BM0NJZZlW8RCuVM6garNigpvFISwi29tic7NzWfCaS3JTEBmM3DCvQACDmcCoXbCMX_zLdDR333qhkhEhtVMzM8Vnlk4PzOZOgVqD_go-J_AiVVx5XCrFkbEePC4_UpK4d34oEEhBbrsOH0ISAy29qZadT-Y3LDoW8Z543beAW2PqW88l_h2ZypPNQLaxTKzSjm1LoZY0xWYq02C5E6CiDL3l0ko6CIL_lapYjDMq5fR8uTarUtdZw_lsAfrPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81f4c39a8d.mp4?token=u0z-_yRIfmgi2facqwmPdfvC0GUBTpl6MDzPwsCSBMBXtllALz1izfszT-y5I8YKcBDCTmK17_4fyM1XP_AUBQV0BM0NJZZlW8RCuVM6garNigpvFISwi29tic7NzWfCaS3JTEBmM3DCvQACDmcCoXbCMX_zLdDR333qhkhEhtVMzM8Vnlk4PzOZOgVqD_go-J_AiVVx5XCrFkbEePC4_UpK4d34oEEhBbrsOH0ISAy29qZadT-Y3LDoW8Z543beAW2PqW88l_h2ZypPNQLaxTKzSjm1LoZY0xWYq02C5E6CiDL3l0ko6CIL_lapYjDMq5fR8uTarUtdZw_lsAfrPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرستو نظام با کلی عمل زیبایی که البته هرچیزی شد بجز زیبا: قلب من با امام حسینه
😐
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66806" target="_blank">📅 12:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66805">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f836563943.mp4?token=SYN17N8_oOzTuqBgAu_KDaW3rMTLDhUvL3xSqo_xZXNoBw_Dt-TsERiweKbr3BB2FDYkEnkUoJr3djrhZpJNBYFB6hhnYhlaEicXGY5ssZDUXrqJqLa26SYYIEiMa_c6PxjppFrDX5OGfUY8JW1J5t-5uEI7oF0G6I4Ro1EQ-898H7fETk_gQT5Co2mUMKHLXdY1-LySsZW7kkpXzgmnlcNhzKAfn9La6mh0aDR-hLcCo_hXiic4-tbMRpqEG2FFM2Syfn_XT7VI6hXJFJOs7u2XB3jL5VGzz4vTNnykKW9_a2drUVVYqjevyp9LIFPeWzmT0jtpGlavHTh3_xaGcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f836563943.mp4?token=SYN17N8_oOzTuqBgAu_KDaW3rMTLDhUvL3xSqo_xZXNoBw_Dt-TsERiweKbr3BB2FDYkEnkUoJr3djrhZpJNBYFB6hhnYhlaEicXGY5ssZDUXrqJqLa26SYYIEiMa_c6PxjppFrDX5OGfUY8JW1J5t-5uEI7oF0G6I4Ro1EQ-898H7fETk_gQT5Co2mUMKHLXdY1-LySsZW7kkpXzgmnlcNhzKAfn9La6mh0aDR-hLcCo_hXiic4-tbMRpqEG2FFM2Syfn_XT7VI6hXJFJOs7u2XB3jL5VGzz4vTNnykKW9_a2drUVVYqjevyp9LIFPeWzmT0jtpGlavHTh3_xaGcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی از هیئت‌های گناوه بوشهر یه مداح به این شکل از جاویدنام‌های وطن یاد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66805" target="_blank">📅 12:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66804">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f61a8cbb.mp4?token=iRjspsBrxuIBCG8qkcILtRuruJKzXc8G4PpNbRdUKrSn8EcPiWFYXU7J5f5YQc_1C8mRjT8qWwWULv9PGroT24R9WvNCWljTKHG0mkWmqW-C4Wv0ZwiR9IKO5Pqn_rb6bIbnwN54hAbtmm_l0tzwtyCjaXj4CBPf2KoEXHXbjS1qVByJL_BDTjGgiYTMHMDOqiZCX0dvPF3m6U6zVaSnxGBAIB6L80gCvXkWfLrBxirlnvSdzgqDep9HUl6BPwyqRKIUdXz4emi5lLJcvDUawov09Ni8f-BibIgTXR0AEi2OJjope4a-e-FnGrF8Eb6JJGLxdwMuiBBv6WtSmGIf7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f61a8cbb.mp4?token=iRjspsBrxuIBCG8qkcILtRuruJKzXc8G4PpNbRdUKrSn8EcPiWFYXU7J5f5YQc_1C8mRjT8qWwWULv9PGroT24R9WvNCWljTKHG0mkWmqW-C4Wv0ZwiR9IKO5Pqn_rb6bIbnwN54hAbtmm_l0tzwtyCjaXj4CBPf2KoEXHXbjS1qVByJL_BDTjGgiYTMHMDOqiZCX0dvPF3m6U6zVaSnxGBAIB6L80gCvXkWfLrBxirlnvSdzgqDep9HUl6BPwyqRKIUdXz4emi5lLJcvDUawov09Ni8f-BibIgTXR0AEi2OJjope4a-e-FnGrF8Eb6JJGLxdwMuiBBv6WtSmGIf7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیره چرا شبیه یارو خپله تو آل زبیر نشسته
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66804" target="_blank">📅 11:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66800">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80f5246ce8.mp4?token=kNZwC_d7jOaaBS1Ef-HvqXMeCceO6mKpNajQ6q9bM-z8g3WNfPtEcDdjppC5JP5QW1ui8NqP7T_l7amiqPcm74h2YRxuP1bVGGh2vpKKlZKO8ZHqU2ML54IHqhexlmX-AXM13g0-fARoTsII5NvG6CjW8fTKNlu_bp4Ju000Ee49GXuWRgGrWmbd3CZXEbA3W0FT2mjOFndCvUDerLQ-1-g6MQY5eVFfgXIBbHo1S78T2_PDQhSZRtilu9R29gSQH32CT0irWuGrqPQQ3BGupZszTg1i9k7g5wzxEyMX0b4bGXY0exnPpgfUPnwe6pSVG1ovvD7EqQXM0f9-DS5tow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80f5246ce8.mp4?token=kNZwC_d7jOaaBS1Ef-HvqXMeCceO6mKpNajQ6q9bM-z8g3WNfPtEcDdjppC5JP5QW1ui8NqP7T_l7amiqPcm74h2YRxuP1bVGGh2vpKKlZKO8ZHqU2ML54IHqhexlmX-AXM13g0-fARoTsII5NvG6CjW8fTKNlu_bp4Ju000Ee49GXuWRgGrWmbd3CZXEbA3W0FT2mjOFndCvUDerLQ-1-g6MQY5eVFfgXIBbHo1S78T2_PDQhSZRtilu9R29gSQH32CT0irWuGrqPQQ3BGupZszTg1i9k7g5wzxEyMX0b4bGXY0exnPpgfUPnwe6pSVG1ovvD7EqQXM0f9-DS5tow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تخریب آخرالزمانی در کاراکاس ونزوئلا پس از زلزله7.5 ریشتری
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66800" target="_blank">📅 10:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66799">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3743ac3a0.mp4?token=k7oQjEhZyTD3enBO4bdvSQwpFGWGzem90gCGxC5owzrWr3lXf_4HjAhHcyKq72K_djLRV8rMX6nzKbJZUVP7F04mLp7-7Fsspd3RuMT--x7JeFejrg8AKf6X9HA6sv79aDAWntYD-p4wqjSCtWFUA4MT2HXhzrE6jyri15Do_2SbHztHvpuT1vvG4NG9cHuumkhG6VgnAnnZLdu4-su95B3DrzWSuE6_IugRrRpgcfbPOIfpY3ctG31IUy_hxgNXn_8SWOiNT-T2sC7BP4NGaM4DBAckrEsGFnjPyNAcQ7lf3TCMO-jBSU3yIhNUHTrtS_JXHcyVVAy2jKn3GZmbvZJtRrwxQEE30aQOV73lEyax3d7iMa5jDRY4VfXqCzydPUdsJZmshJpF5QFuSNIyJZ6nZ4uu8z63ziaPQjtIZFMB7onchFj7hTIcvNn5xSthYuWoLubBy_pJFUc1HTJn1mJzuEPcIiCCllri3c12xwy6Qz8fT_VYA0P12Vjoa8ZD7nZNFYBqIVW05rDB7b0uSqVbdDMkJqvhMgX4C26pShUgFHlbiDPppH1CDtDqqgagmCJE9z1cA6NfBb_pgN7uqiEqkisUS7z8bqAmaGuzTNzALztnqE_vB2V4941j0plbjCg-J4ZYRhg7rtWi0T8A5ARMFZkIV6mhavKC9lyHJsY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3743ac3a0.mp4?token=k7oQjEhZyTD3enBO4bdvSQwpFGWGzem90gCGxC5owzrWr3lXf_4HjAhHcyKq72K_djLRV8rMX6nzKbJZUVP7F04mLp7-7Fsspd3RuMT--x7JeFejrg8AKf6X9HA6sv79aDAWntYD-p4wqjSCtWFUA4MT2HXhzrE6jyri15Do_2SbHztHvpuT1vvG4NG9cHuumkhG6VgnAnnZLdu4-su95B3DrzWSuE6_IugRrRpgcfbPOIfpY3ctG31IUy_hxgNXn_8SWOiNT-T2sC7BP4NGaM4DBAckrEsGFnjPyNAcQ7lf3TCMO-jBSU3yIhNUHTrtS_JXHcyVVAy2jKn3GZmbvZJtRrwxQEE30aQOV73lEyax3d7iMa5jDRY4VfXqCzydPUdsJZmshJpF5QFuSNIyJZ6nZ4uu8z63ziaPQjtIZFMB7onchFj7hTIcvNn5xSthYuWoLubBy_pJFUc1HTJn1mJzuEPcIiCCllri3c12xwy6Qz8fT_VYA0P12Vjoa8ZD7nZNFYBqIVW05rDB7b0uSqVbdDMkJqvhMgX4C26pShUgFHlbiDPppH1CDtDqqgagmCJE9z1cA6NfBb_pgN7uqiEqkisUS7z8bqAmaGuzTNzALztnqE_vB2V4941j0plbjCg-J4ZYRhg7rtWi0T8A5ARMFZkIV6mhavKC9lyHJsY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاروان اجنه و فرشتگان:
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66799" target="_blank">📅 10:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66798">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/638875c442.mp4?token=px1ngKP6oKzJgjeuZQt6F7hsVJbaLA98dKPBwIfV-WBLIqWI2wrXlmDXXCCxKS_ZdhgQbsWfVHV6QPqAKovR68LwLxE9kTWWLswwYwn9DrKjsLKKAL6FepD39WfsrAT2gNvTpii_X5OaVpticF3_ztKBf86lRDw1jsxxH2mpnkc1ZIKzsRiwAJP6pmmreWmnw2fsDLt6I3YS-UR9NU_Q0KrAl-98Ep-iEx5PEMK49aW1L4l6Jkf8cM7nyzyDZhiZkpXFh1Gg7wVtfYJzWwn6YVTJveW_ASHLbBLUCLHlj33MbJJIrNdbm8p-gjUBK4uFGlmiLuzT1jL3qHKvuCV0sw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/638875c442.mp4?token=px1ngKP6oKzJgjeuZQt6F7hsVJbaLA98dKPBwIfV-WBLIqWI2wrXlmDXXCCxKS_ZdhgQbsWfVHV6QPqAKovR68LwLxE9kTWWLswwYwn9DrKjsLKKAL6FepD39WfsrAT2gNvTpii_X5OaVpticF3_ztKBf86lRDw1jsxxH2mpnkc1ZIKzsRiwAJP6pmmreWmnw2fsDLt6I3YS-UR9NU_Q0KrAl-98Ep-iEx5PEMK49aW1L4l6Jkf8cM7nyzyDZhiZkpXFh1Gg7wVtfYJzWwn6YVTJveW_ASHLbBLUCLHlj33MbJJIrNdbm8p-gjUBK4uFGlmiLuzT1jL3qHKvuCV0sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه سریزد  ، یزد
شاهکاری از معماری باستان
جایی که قرن ها پیش مردم اشیاء ارزشمند خود را در اتاقک‌های امن آن نگهداری می‌کردند
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66798" target="_blank">📅 09:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66797">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lh2nlEs4i5VJB0Gl0FDiuCBkjNPWUhy0d_vpbfSSyU0FMTHx__EOzF0FrhEFBf1JqYYwgKdPiwN0b_mhFvqgfdAdG-piMfv_KdNDIGyw3f3icXQ5bpE1PDTBpis0NUF8cknnt2gg40h_Y3NwJXd2YTw6xrDcB5UejGu6Aamn_TBbd2tId2dgsQKKWBO9LaxUGEFC1QvIOhE3W0BOuhQoXzZeK8HX4cJJ4k9j19pxsWiWSIQUh43l2onWXFTjchuUPS5PS2O6_baGFo6qPNOv4svZ28a6kreKiIml3gPvmZfw3zgC4IeyUYt1H-jRonDboR50J2UxsmxkxUZ2HBcTvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
دونالد ترامپ:
دو زلزله بزرگ که اخیراً ونزوئلا را لرزاندند، بسیار عظیم بودند و تعداد زیادی قربانی برجای گذاشتند. ایالات متحده آمریکا آماده ارائه کمک است!
16;من دستور داده‌ام که تمام دستگاه‌های دولتی ما برای اقدام سریع آماده باشند. ما برای حمایت از دوستان جدید و فوق‌العاده‌مان حاضر خواهیم بود. گزارش‌های اولیه امیدوارکننده نیستند!
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66797" target="_blank">📅 09:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66796">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‼️
از ناوشکن هسته‌ای کره شمالی رونمایی شد
🔴
رسانه‌های دولتی کره شمالی گزارش دادند کیم جونگ اون اعلام کرده است نیروی دریایی این کشور به سلاح هسته‌ای مجهز می‌شود و کشتی چوئه هیون رسماً وارد خدمت شده است.
🔴
این ناوشکن ۵۰۰۰ تنی به سلاح‌های ضد هوایی و ضد کشتی مجهز است و قابلیت حمل موشک‌های کروز و بالستیک با توان حمل کلاهک هسته‌ای را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66796" target="_blank">📅 09:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66795">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66795" target="_blank">📅 03:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66794">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66794" target="_blank">📅 02:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66793">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sTftlcqtrc52I8jPE2LLlwBfukEsRlZpOfVQ_O_Sak-qVjLLUF7YdsY1ohoivN5vpgGfu92YInrijsvbj_-uCuxa5wpoZ-gvkzsfBeXl93_X1k-j-UnqCj60kro9nAt1ejc6QtnJyv8IWgmevuFWygcc0wIknu7gWgw_bLjme1yd1rj1-JP8eby2KxuzyNXm9b2_ajZ4G_uiok80RJdsHeGMknXLORudeDNK58oqZEaxd6vtoG0MCT8Vb9AXPKNm1pTdVj3vhBzxvLiYLeqCdbF0lRs1xwK4Cck-4bmqts0HJ4AIRWm1t8h4Eiur0DHmQgSnOexxtHHLOcxky9wzqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66793" target="_blank">📅 02:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66792">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17bcbdae9.mp4?token=VphUXa_8oniRom4s9UZNkKrs6Pqch3DuSFSXVWxUKiCm3MES-hvxMZQzJ2NEqfSYJ4VKXJvDHzcxEPEqEfmxry0iYYRgv-wp68iWicJVRJtJZHicUUFD_LoyfAoU1f_9kKdGnZGGJNSBPRVRhN3_MSxej9wscF21lEefmuc52ggHDSebp0ELrfqOHZTRAiwfWiW81l7E7PNj7XgCi-ocAOJHCcIBFGKLh32TymkIutN3fIwG0BFBivPMOIy5O4Wrn0hMTt25eGEfSLOoObv1cx1iVTEXsPIwoVmztjjW1AZKE5ugmbDwSOAOVVg1zYZxluFE4oxNMjHXsSEBGUlb_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17bcbdae9.mp4?token=VphUXa_8oniRom4s9UZNkKrs6Pqch3DuSFSXVWxUKiCm3MES-hvxMZQzJ2NEqfSYJ4VKXJvDHzcxEPEqEfmxry0iYYRgv-wp68iWicJVRJtJZHicUUFD_LoyfAoU1f_9kKdGnZGGJNSBPRVRhN3_MSxej9wscF21lEefmuc52ggHDSebp0ELrfqOHZTRAiwfWiW81l7E7PNj7XgCi-ocAOJHCcIBFGKLh32TymkIutN3fIwG0BFBivPMOIy5O4Wrn0hMTt25eGEfSLOoObv1cx1iVTEXsPIwoVmztjjW1AZKE5ugmbDwSOAOVVg1zYZxluFE4oxNMjHXsSEBGUlb_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
درست در میانه یکی از مهم‌ترین مسائل، ناگهان خبر فوری منتشر می‌شود: “سنا رأی داده است که می‌خواهد ترامپ جنگ را متوقف کند.”
ایران این را می‌بیند و می‌گوید: این دیگر چیست
؟
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66792" target="_blank">📅 01:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66791">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6928b1a5c.mp4?token=NCwbXj-1qBCBZqTTT8_1n1dv06BByCPB0b6zcg0BJ85om9Axsv2EaeFjRHZ0rXdWDrjehc2smW2qaVV-1Sr_Q4NHb8Zfgh-kCgvgokhtVaWZhBa8pX1NfR8RsIrLM-wU8DSjTDEkPCUDwPVbk4NxZKUZtFU0zUB1fA8DGmj2nxEYrnopiHnG_-1ErYiVDjvGkdlI13thgxtdP2p7pF_QCkMFTf54PD04lYsJ80GNr56dY82RR7fGawD5vZphJUyy6lQohd-gwf9Hb_CZyVuu7THeeBSmcUg-1IRcR2QhjoQC8YXsqp0uonsaL6xl-riXlQAV-x6Jwh8bbVSt3PbMHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6928b1a5c.mp4?token=NCwbXj-1qBCBZqTTT8_1n1dv06BByCPB0b6zcg0BJ85om9Axsv2EaeFjRHZ0rXdWDrjehc2smW2qaVV-1Sr_Q4NHb8Zfgh-kCgvgokhtVaWZhBa8pX1NfR8RsIrLM-wU8DSjTDEkPCUDwPVbk4NxZKUZtFU0zUB1fA8DGmj2nxEYrnopiHnG_-1ErYiVDjvGkdlI13thgxtdP2p7pF_QCkMFTf54PD04lYsJ80GNr56dY82RR7fGawD5vZphJUyy6lQohd-gwf9Hb_CZyVuu7THeeBSmcUg-1IRcR2QhjoQC8YXsqp0uonsaL6xl-riXlQAV-x6Jwh8bbVSt3PbMHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره حمله به مدرسه میناب:
«نمی‌دانم که آیا آن‌ها هرگز خواهند توانست این مسئله را حل کنند یا نه.
موشک‌ها از هر طرف در حال پرواز بودند.
کسی گفت که آن موشک متعلق به ما بوده است. شاید بوده باشد، اما من هیچ چیزی ندیده‌ام که مرا به این باور برساند که واقعاً موشک ما بوده است.
موشک‌های فراوان دیگری هم توسط افراد و طرف‌های دیگر شلیک شده بودند.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66791" target="_blank">📅 01:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66790">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">Live Volleyball</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66790" target="_blank">📅 01:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66789">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fa6495873.mp4?token=pJrwLVw7PbAh5GAkHSbA9trdDxKm8gVzhgZL8vQqRgHoFlR1PPmFXETLB1oZ-BukROwd4MkeaFmC5uUOUXELkV0X-ne0NOb-_wwmjlZRI2R7YdtTKF0xwEbhQGDXj6AYENROimFHdSA5N9qsgJdfzfN2L5hlkPbtha4-arPtthUG3KRWhiigQJUPHXLgfUM2drR1oj1K5wToQR42EQivp3g_G_nrW5yc2jHs9dR9jgCCxaVcb0zJzb18hZ5sT2oRqI9DJZ831pjjipg-9wqNmwcZQZWxIdj0EPUSzEXRmsNoKV-Wr2ZS77FLuKm3U39bmPBF9_DUxQ_9uIvm-pGnDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fa6495873.mp4?token=pJrwLVw7PbAh5GAkHSbA9trdDxKm8gVzhgZL8vQqRgHoFlR1PPmFXETLB1oZ-BukROwd4MkeaFmC5uUOUXELkV0X-ne0NOb-_wwmjlZRI2R7YdtTKF0xwEbhQGDXj6AYENROimFHdSA5N9qsgJdfzfN2L5hlkPbtha4-arPtthUG3KRWhiigQJUPHXLgfUM2drR1oj1K5wToQR42EQivp3g_G_nrW5yc2jHs9dR9jgCCxaVcb0zJzb18hZ5sT2oRqI9DJZ831pjjipg-9wqNmwcZQZWxIdj0EPUSzEXRmsNoKV-Wr2ZS77FLuKm3U39bmPBF9_DUxQ_9uIvm-pGnDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرچم نروژ فقط یک طرح ساده نیست
🇳🇴
...
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66789" target="_blank">📅 00:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66788">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6390fb697.mp4?token=YDBZM6DEalm6SrOVonP25qo7TxHXKZVIGZkKoON-Gua-6d4Exr3SwVlD3RduL2IlMMIxil8UM7-ppunSPXy_O6gaYerIvKeV-3e8fWvbAdye4H-C_KMBlwLKo7SOY3TokQEHe2M4rtx4P09L6QTJGdzOLdr8czWwJqQwCRvizLtHFBNi1-ijsxv36t4owd2DqruS44wuX9ehPvsAll-UJtkKqOeVVRqaGBLQI0rhwcwP0jhHHoJDIw_4FvLq90jc39ACEi-ARR8DgeJpJ0lMq_gpnDtLeFRvAi6AxfMuawD15ZLqBAr74lrYcPrDSP47xoVmIMYw1R-DAJjAnS198VsrYGlhZoICvcUkuW6bv3u9cZLSX4TjoJSx5DQjFo6aljUoViPheQcAx-0UNA2ku4sYTZ1onmTGOEqBNDoZwfcOiYDQ4mXQfVIkgdjTdbpxu1pWBR-tGDGf4MeHbFvHdS730NMblYOKb8CCQUFYcKcpKNEeW7EaMwShbHNxwzKaXPbauOGBYoVIjIh3jHzlUq9TsXDpSr--FS1Wys1erVHjD7N8fmi25CesYYSYFcAXZYi7EDAcjaPjT12bgRiRIxacILXRqg2atDM0BTuCmHQiFPz0i_IkUvBYkMZCGJQJmg6IAwMxCQU2YSzx4Nd4a7VwSqvmH1rkJLt6Zar6F_Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6390fb697.mp4?token=YDBZM6DEalm6SrOVonP25qo7TxHXKZVIGZkKoON-Gua-6d4Exr3SwVlD3RduL2IlMMIxil8UM7-ppunSPXy_O6gaYerIvKeV-3e8fWvbAdye4H-C_KMBlwLKo7SOY3TokQEHe2M4rtx4P09L6QTJGdzOLdr8czWwJqQwCRvizLtHFBNi1-ijsxv36t4owd2DqruS44wuX9ehPvsAll-UJtkKqOeVVRqaGBLQI0rhwcwP0jhHHoJDIw_4FvLq90jc39ACEi-ARR8DgeJpJ0lMq_gpnDtLeFRvAi6AxfMuawD15ZLqBAr74lrYcPrDSP47xoVmIMYw1R-DAJjAnS198VsrYGlhZoICvcUkuW6bv3u9cZLSX4TjoJSx5DQjFo6aljUoViPheQcAx-0UNA2ku4sYTZ1onmTGOEqBNDoZwfcOiYDQ4mXQfVIkgdjTdbpxu1pWBR-tGDGf4MeHbFvHdS730NMblYOKb8CCQUFYcKcpKNEeW7EaMwShbHNxwzKaXPbauOGBYoVIjIh3jHzlUq9TsXDpSr--FS1Wys1erVHjD7N8fmi25CesYYSYFcAXZYi7EDAcjaPjT12bgRiRIxacILXRqg2atDM0BTuCmHQiFPz0i_IkUvBYkMZCGJQJmg6IAwMxCQU2YSzx4Nd4a7VwSqvmH1rkJLt6Zar6F_Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی که یه عده از طرفداران حکومت با هوش مصنوعی از «مختارنامه» جدید درست کردن
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66788" target="_blank">📅 23:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66787">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_bmiGk1OzmfyYhi5gHsruaj_P_XjviGP1OP5dIbqt3tYjAKD2pB-Evy439xu8_OAP_ZJjWQDvee-F0Nn_SCbcvCaYqwNInywfA59lvigVeepoygnWRhR2yNwY826GMdFVIwcibiUDDdySB9NVdMj_EKn3qD7HnbtZyDoveCUsfbKmZE_ADpBeDNi1nSTxWzg85P0e7phw0enrPn0imq9suzUbMHkm27s89MdPBGLoezR2RDryEfLDhvO6F7KSlEJRA-RHKURM0lyNpysrHMEEYipdFxJdD925uUEMrTSk0Wi1jxGN_YfPY3r6zLJn2br7oj4RcpNuDt5Eb25N5TAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سخنگوی وزارت امور خارجه:
اظهارات متناقض آمریکا درباره یادداشت تفاهم برای پایان جنگ به کاهش بی‌اعتمادی ایرانیان کمک نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66787" target="_blank">📅 23:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66786">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66786" target="_blank">📅 23:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66785">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jcf-mdqerDXMnV5tTsH9chXUTmEDWAJOps_3NhHLUyeIv8xAA7BWiaMcDMc0Z2_IiW9WrGrZRqgNYihF5Z_qitYoFSpBCNhU86Pa3XtrAeJNpluRq28aiZteK5R3YAuPut3owxAnj4jQBxaBt66DqRvQlFujmlP3feoD8mXicysrZO1Q6_R0bE8kgyG-fG6JONHRv04QWEMtSuuZvGK0ifMOQamAhuIvrGyuvplKO-4irn2DLg-aSjfNFQiPgFyX0ztWarAQHzsTVlKa1tcy42nzGb2Kn5UgCaFIBM5QYC5BgPwQHG1MO46Ww-LIdg7fhphR1siFNMNDlY0wpS21QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66785" target="_blank">📅 23:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66783">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f56950043.mp4?token=oDtxQGiEGLVfdwxSxuotm0D0AT8ur77n5bHialTHd5Tz_8ns2zWf60KYb8lHC-hPM_zTS-MFf4lCtG7qPUY-aLfj10Jc8o26l9mx2jFjxUbbpY-shjmaI0ab_G1CC8UdyGmjJ4O_ahhnODsqLVgbZNUMEtHlKQe8B8BRu2nptDwGCJy8CEp6bA3CNMSZw38GamuitNelOVb6Et44GtPb7qmXUGdE1e14I0q-ol16P2nAgj9qQJ1lbTMK7q3UPo_sJsY8fd1rLAvjpppgVXr235f2ifWeU_4Flq_pOzK6gmTZCeju09932tONzVVTZyIfyXE4i2-lcVhCD2EHO-pEUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f56950043.mp4?token=oDtxQGiEGLVfdwxSxuotm0D0AT8ur77n5bHialTHd5Tz_8ns2zWf60KYb8lHC-hPM_zTS-MFf4lCtG7qPUY-aLfj10Jc8o26l9mx2jFjxUbbpY-shjmaI0ab_G1CC8UdyGmjJ4O_ahhnODsqLVgbZNUMEtHlKQe8B8BRu2nptDwGCJy8CEp6bA3CNMSZw38GamuitNelOVb6Et44GtPb7qmXUGdE1e14I0q-ol16P2nAgj9qQJ1lbTMK7q3UPo_sJsY8fd1rLAvjpppgVXr235f2ifWeU_4Flq_pOzK6gmTZCeju09932tONzVVTZyIfyXE4i2-lcVhCD2EHO-pEUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ازای شهادت مقام معظم رهبری چی از آمریکا گرفتید؟
قالیباف:
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66783" target="_blank">📅 23:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66782">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78f387d3e0.mp4?token=OYjF57uzTSr5q3HeQEDKpgVNOk97A9IrtVzmKl8iOJiAj9qG_8cE5EiAwYyu_9rLRer0izKFtz4jKLYANRrgpVWIimUgdagbfHr8L6Zl8kMo0sukZG6Pc2MJks-CV6n6E4LnCQVLdFOmXdXHf3B7AVpRXpEdmf9quwkqH1eaLlLH0IE0fMIPqCKaHtOHD7HuiTOzH4zqoPJpYMwzClLZRlIXmnLV0GHmeqf898aWYQgq0GJGWwDeAnmLkBEDBl0UQpLCgKnZCfMs1S1M-A8T5W6jH9Z8ywyD0EUVb-_E1kigkRKK9E1BpvUWxTcr-w4rrqhEJhjmYQ2bw4pPGt07Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78f387d3e0.mp4?token=OYjF57uzTSr5q3HeQEDKpgVNOk97A9IrtVzmKl8iOJiAj9qG_8cE5EiAwYyu_9rLRer0izKFtz4jKLYANRrgpVWIimUgdagbfHr8L6Zl8kMo0sukZG6Pc2MJks-CV6n6E4LnCQVLdFOmXdXHf3B7AVpRXpEdmf9quwkqH1eaLlLH0IE0fMIPqCKaHtOHD7HuiTOzH4zqoPJpYMwzClLZRlIXmnLV0GHmeqf898aWYQgq0GJGWwDeAnmLkBEDBl0UQpLCgKnZCfMs1S1M-A8T5W6jH9Z8ywyD0EUVb-_E1kigkRKK9E1BpvUWxTcr-w4rrqhEJhjmYQ2bw4pPGt07Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ در مورد ایران:
ایران خیلی خوب رفتار می‌کند. آنها با هر چیزی که من می‌خواهم موافقت می‌کنند و باید هم موافقت کنند.
در غیر این صورت، ما فقط برمی‌گردیم و کاری را که باید انجام دهیم، انجام می‌دهیم
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66782" target="_blank">📅 22:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66781">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a05f2cc6.mp4?token=rmLxEa5dkhfLkU70wVPR6AulG1XFDx2zK2qJYoWoKZ_UAW0XjkaGEivp8jHipW1sL1wF3LkSoR7KBSm10gU1sbzlNAqchJ9aaLtQXU4vJyGX7ExOFgnSUayejcQ7suULiBpVVkR3I6JMcQC0j3w_WveU6uYvTeU8ypSzBe0dg_nQV23to_9lRfcOIh9bWsoY_1jfqEW3FX1Ye487WOKhP9M__6_-jLbyKF3kRqoKx-36bmls1oYLsk22ICTOG_slQsTZizZ5-Qef_yY0QotcpYHxftGEBE3R1f4SC44AT_JWwKv8HK4SVqBLkuTaG6akByrMnBaTDWtCaafZrOJG_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a05f2cc6.mp4?token=rmLxEa5dkhfLkU70wVPR6AulG1XFDx2zK2qJYoWoKZ_UAW0XjkaGEivp8jHipW1sL1wF3LkSoR7KBSm10gU1sbzlNAqchJ9aaLtQXU4vJyGX7ExOFgnSUayejcQ7suULiBpVVkR3I6JMcQC0j3w_WveU6uYvTeU8ypSzBe0dg_nQV23to_9lRfcOIh9bWsoY_1jfqEW3FX1Ye487WOKhP9M__6_-jLbyKF3kRqoKx-36bmls1oYLsk22ICTOG_slQsTZizZ5-Qef_yY0QotcpYHxftGEBE3R1f4SC44AT_JWwKv8HK4SVqBLkuTaG6akByrMnBaTDWtCaafZrOJG_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«جنگ خیلی خوب پیش می‌رود. همانطور که
می‌دانید، ما با اختلاف زیادی در حال پیروزی هستیم. ایران امتیازات بسیار بزرگی می‌دهد. خواهیم دید چه اتفاقی می‌افتد، اما بسیار، بسیار، بسیار قدرتمند بوده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66781" target="_blank">📅 22:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66780">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00a25b4d46.mp4?token=FtWgpWkTWrydsDSdiOUbGuBNo7HmhXQ6jTPIL3DwDON4ARsfr5M8Yc4854kR8qUkvfRB61OrDncfAlein2UIFf4oRxb8cBa6PSJMIUg36Fc-QE8jeLCwdqmABxJ80Wm-yPTJZX1my6I7MRXBsmnSbPyc5xaZy1baz7uiALzf4TUBBQ0Jc-dTXTrpms1VCAYkZAaz12-smOINHYA7opXvgKgXQhBJ8DEEqNbX-4zjouFhZj5J3Ns4XI5ghocS5v6zxjNa4USHv9VEJOJ0N7JTOFKAiyE2PqD5U5A7pdTC_qbPHzyGDr7CHtXnVSXR3poxO-EFRoYbqJOhwy_-z0Hc4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00a25b4d46.mp4?token=FtWgpWkTWrydsDSdiOUbGuBNo7HmhXQ6jTPIL3DwDON4ARsfr5M8Yc4854kR8qUkvfRB61OrDncfAlein2UIFf4oRxb8cBa6PSJMIUg36Fc-QE8jeLCwdqmABxJ80Wm-yPTJZX1my6I7MRXBsmnSbPyc5xaZy1baz7uiALzf4TUBBQ0Jc-dTXTrpms1VCAYkZAaz12-smOINHYA7opXvgKgXQhBJ8DEEqNbX-4zjouFhZj5J3Ns4XI5ghocS5v6zxjNa4USHv9VEJOJ0N7JTOFKAiyE2PqD5U5A7pdTC_qbPHzyGDr7CHtXnVSXR3poxO-EFRoYbqJOhwy_-z0Hc4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عبدالناصر همتی:
اگه کیفیت ذرت و گندم آمریکا خوب باشه ازشون میخریم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66780" target="_blank">📅 22:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66779">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9UFFOgadgu9HgqZvYurQu4vC1Fawv6dzaRGSmF6v6FY-5yKJ_eX7xZttLjOoGYwP75Fx9QUUJ6vzjEEJSZ_O30uL7kpj8iDdhT9wrSiWGluISWRMfA2N7WrclFq1IlJgm6Dm4NBcYQyZqPVjfFIPOsDcpm6mcP4ZUCGseyy7VJ_gpfk9T_1VspUwV0bj7tFc0USLarpiGwFlJW07hTKPuZotcoVJxVbwNsayS__uK7nPk9IwC6UZZjaGR2ThhBgcqwbHpFjiVR92DRS7EveS_ZRdKU47xnDbQGzAGOflTkv-7auz644qrF7LhXbL_fhLiMIWGON14XxGsSO_2llcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اتاق جنگ اسرائیل به مارکو روبیو:
رژیم جمهوری اسلامی و حامیانش در عمان در تنگه هرمز هزینه دریافت میکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66779" target="_blank">📅 20:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66778">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd80a69999.mp4?token=MiZmoPK10X58vZQxWNv3yFOoJw2UzqBTuMSV1zSCWEpOIM81S8HzOfeFF0_T4b46r_SbCmKR3wO9GqRKau97omO4XO3kMPuztHj7yTrIGbq1uS3RXf7PtptOI61MHzKURwW_FYV4RD8nCnXAOFZ9hD-HQUcAFV4TYY3v6faRulZxusEgf_AfHNsLPg0GHxpStEvxtDgTGG4DL4u_DjSAtjtxF-ndyffESNdh0wiVGDblVo6NR7vfAPdwXpahDYbS6QTAC_mipaZZ5wQ8BIvfWV8Bzt_6wN7um9bQbs9eVBdUB6xPxQT8eYx8onuj-g0rdeZKPKBv0bWCxzo4ZJjY9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd80a69999.mp4?token=MiZmoPK10X58vZQxWNv3yFOoJw2UzqBTuMSV1zSCWEpOIM81S8HzOfeFF0_T4b46r_SbCmKR3wO9GqRKau97omO4XO3kMPuztHj7yTrIGbq1uS3RXf7PtptOI61MHzKURwW_FYV4RD8nCnXAOFZ9hD-HQUcAFV4TYY3v6faRulZxusEgf_AfHNsLPg0GHxpStEvxtDgTGG4DL4u_DjSAtjtxF-ndyffESNdh0wiVGDblVo6NR7vfAPdwXpahDYbS6QTAC_mipaZZ5wQ8BIvfWV8Bzt_6wN7um9bQbs9eVBdUB6xPxQT8eYx8onuj-g0rdeZKPKBv0bWCxzo4ZJjY9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو:
توافقات اخیر با رژیم جمهوری اسلامی بخشی از یک روند مذاکره‌ای و یک اقدام موقت ۶۰ روزه است.واشینگتن انتظار دارد تهران به تعهداتی که در سوئیس پذیرفته پایبند بماند و در غیر این صورت، پرزیدنت ترامپ ابزارها و گزینه‌های مختلفی از جمله بازگرداندن تحریم‌ها را در اختیار خواهد داشت.این تعهدات به صورت روشن و صریح مطرح شده‌اند و ادامه مسیر مذاکرات به میزان پایبندی رژیم جمهوری اسلامی به آن‌ها بستگی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66778" target="_blank">📅 20:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66777">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ffe99615e.mp4?token=Vhu7Ufov1Yq5luSMRHgYj6OpD3KD35iopGhBOHRnX87RJ8Odr8aeRcOsem9vWK-ubPYIfqJtxBduYGDUEVoQYn4TmvDjcHXLw6XAlFK4PkLDmrQWEpcnvZbKThBil26d7S4kJmP3Uj0e5tCrbuxioVOq_svYDxTYoEcsy4oh-dAbD_IY9fJwSJevy7GhjhSvqeRbqrxIiGxNh0fwfuhYl_KRNtrpxBSRuTxMm2WP5EUzaygR2EhbejR20d_dE1oVkMT39ZRVMCWJOSRLOhxMDxdeFVytMLxi1hKwfydzJRtmow3zHXRkcx3B-Ua1OJUrB-q3iAKBqSQ66oSaOztnfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ffe99615e.mp4?token=Vhu7Ufov1Yq5luSMRHgYj6OpD3KD35iopGhBOHRnX87RJ8Odr8aeRcOsem9vWK-ubPYIfqJtxBduYGDUEVoQYn4TmvDjcHXLw6XAlFK4PkLDmrQWEpcnvZbKThBil26d7S4kJmP3Uj0e5tCrbuxioVOq_svYDxTYoEcsy4oh-dAbD_IY9fJwSJevy7GhjhSvqeRbqrxIiGxNh0fwfuhYl_KRNtrpxBSRuTxMm2WP5EUzaygR2EhbejR20d_dE1oVkMT39ZRVMCWJOSRLOhxMDxdeFVytMLxi1hKwfydzJRtmow3zHXRkcx3B-Ua1OJUrB-q3iAKBqSQ66oSaOztnfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار: برخی از عناصر اطلاعاتی ایالات متحده ارزیابی کرده‌اند که اسرائیل علاقه‌مند به تضعیف تفاهم‌نامه فعلی است.
🔴
روبیو: نمی‌دانم در مورد چه اطلاعاتی صحبت می‌کنید. نمی‌دانم این اطلاعات را از کجا می‌آورید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66777" target="_blank">📅 20:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66776">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b8948b47d.mp4?token=h38uuegHAiB1xcTYU1GgA5LPw_toZ2FSGui_Vda2WeyIKZmuwdSkw5gxDNjAP_YE0OpxGrD3nsoyBLM1DXrKrC_7wCOi8eWB0UsdhQq66lWWf4PRciCwryq8XaLy1VuzrAUL5i3kd13xisaVylOkkkgUzeAcVvbPVpR17KT6P_cBvLArmgh7FfZMrDvwdk3xHcjWhS9S1ItY7Kh-HP7aG0sGzD8cGLXm9JxvXgW2k3Mqcz3RsnoFK8eKyRyTZBc8lei_hevKqVPwWSng3IoHg8EIQyS8lDAuPzpLrJYHwy9cQtgoRWLJaZYlDDtNReLqxJMpXHcP20qgcoHNtVt-zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b8948b47d.mp4?token=h38uuegHAiB1xcTYU1GgA5LPw_toZ2FSGui_Vda2WeyIKZmuwdSkw5gxDNjAP_YE0OpxGrD3nsoyBLM1DXrKrC_7wCOi8eWB0UsdhQq66lWWf4PRciCwryq8XaLy1VuzrAUL5i3kd13xisaVylOkkkgUzeAcVvbPVpR17KT6P_cBvLArmgh7FfZMrDvwdk3xHcjWhS9S1ItY7Kh-HP7aG0sGzD8cGLXm9JxvXgW2k3Mqcz3RsnoFK8eKyRyTZBc8lei_hevKqVPwWSng3IoHg8EIQyS8lDAuPzpLrJYHwy9cQtgoRWLJaZYlDDtNReLqxJMpXHcP20qgcoHNtVt-zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو درباره ایران:
وقتی می‌گوییم تنگه‌ها را باز کنید، منظورمان این است که تنگه‌ها را آزاد باز کنید. آنها آبراه‌های بین‌المللی هستند.
هیچ کشوری روی کره زمین از گرفتن عوارض در تنگه‌ها حمایت نمی‌کند. این اتفاق نخواهد افتاد. ترامپ این را به روشنی بیان کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66776" target="_blank">📅 20:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66775">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50bf8d5d6b.mp4?token=jj4-Lx5I6gfJsdXPTAffUtr15bsjHCPRIp8dCTAEjESzxHJd-vgySu0AuBPKrciJZ0gF_Ma8jc005s-NKgJmQr9zxvOhLPnmSl4yDhuuAG46KIU4uacl9N3ZvtOfUOMFFyh_ik2wAzuolEe3lD6zwYo8_WBu1xsJLQVPIOszrOSccb0nTZgVHYyxFfX1POXeLz7H7nLQFt02pQbQFsmlsVhQPrBoITKqgm4R4-aZrWQpr7zNAbWGDOX5D0D4tkNBjW_8D6OFey6pxRHXNHmdYW72TDuqr4XLqBHcTW3Rb9t6qLjVal-g51o7BIS3K0qkM86c8bteJge6NRvn_yhy-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50bf8d5d6b.mp4?token=jj4-Lx5I6gfJsdXPTAffUtr15bsjHCPRIp8dCTAEjESzxHJd-vgySu0AuBPKrciJZ0gF_Ma8jc005s-NKgJmQr9zxvOhLPnmSl4yDhuuAG46KIU4uacl9N3ZvtOfUOMFFyh_ik2wAzuolEe3lD6zwYo8_WBu1xsJLQVPIOszrOSccb0nTZgVHYyxFfX1POXeLz7H7nLQFt02pQbQFsmlsVhQPrBoITKqgm4R4-aZrWQpr7zNAbWGDOX5D0D4tkNBjW_8D6OFey6pxRHXNHmdYW72TDuqr4XLqBHcTW3Rb9t6qLjVal-g51o7BIS3K0qkM86c8bteJge6NRvn_yhy-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
به من گفتند: «وارد رفح نشو.»
می‌دانید چرا این را گفتند؟
چون رئیس‌جمهور ایالات متحده گفته بود ارسال سلاح را متوقف خواهد کرد.
من گفتم: «احترام زیادی برای او قائلم. او در آغاز جنگ کنار ما ایستاد. اما ما چاره‌ای نداریم. وارد رفح خواهیم شد. و اگر لازم باشد، حتی با ناخن‌هایمان هم خواهیم جنگید.»
گاهی باید بدانی چگونه حتی به رئیس‌جمهور ایالات متحده هم «نه» بگویی.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66775" target="_blank">📅 19:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66774">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7873635e.mp4?token=rS_Sm57X0NX2xmnxUnDZIYDVzn1_ovJo-NtVSnv6T-qn_Zfh5G-5iP-05_jxd6l-e-RoZ4TiOD5UqrxpquB0cqL4a8JuaNoynWBFKEI8O5-vSItc7vHHWyVVfwn_dNYJlJOAwbJpGIJZfviHUTErObHJH274wd1aaAhCe_f-z-sXNNqawbHLQnPgMw4jWE5aBxWxsnVPwZsbKVwz4PHKTxZQLXWvlSVO1VVdd4tYLSxq1Mr1hDhiw0Ds9uLmJ-hui_aH6wOuAtqtacjZJJbpv1P4IW4FHZqvk6GWUBBB6iNTYCesqPIkFzzSb2wD5LsD3DUbpoK2SD8gPxIU_8DSGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7873635e.mp4?token=rS_Sm57X0NX2xmnxUnDZIYDVzn1_ovJo-NtVSnv6T-qn_Zfh5G-5iP-05_jxd6l-e-RoZ4TiOD5UqrxpquB0cqL4a8JuaNoynWBFKEI8O5-vSItc7vHHWyVVfwn_dNYJlJOAwbJpGIJZfviHUTErObHJH274wd1aaAhCe_f-z-sXNNqawbHLQnPgMw4jWE5aBxWxsnVPwZsbKVwz4PHKTxZQLXWvlSVO1VVdd4tYLSxq1Mr1hDhiw0Ds9uLmJ-hui_aH6wOuAtqtacjZJJbpv1P4IW4FHZqvk6GWUBBB6iNTYCesqPIkFzzSb2wD5LsD3DUbpoK2SD8gPxIU_8DSGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نخست وزیر نتانیاهو:
در عملیات غرش شیران بود که من به ترامپ حمله در ایران را اطلاع دادم و هیچ اجازه  گرفتنی در کار نبود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66774" target="_blank">📅 18:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66773">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1071e13e2a.mp4?token=lWKgBqtBwXZ-_9SYpognpKAyD3SUG0AcyhOQbb5jhuamZhIL8cg0e0-XhfSuCeZ8KyhQ62EWjX1BT2jJPDp2y7Xj2hVL_OW6hqqYqQPPl4d1MDwA0XUxmXz8sy-h1qUWzxM18q0gPkNTSiUh-lS2tKc-7OFjxCjsZc_Wa8oYJc8CWmL4loKuF62D2Oqjcb1hdGIcbyS5btt_DjXGYiZL4S3WV4ggrh6elmrhpkmSZHeHlGApqwLiXNuI6lrieR4m7WsVNIAji8M6pSCS_GKKbO5PlZIgLZ8OLTT1kl5b3MNnwoCXP8hTrsftxIHp7M5RJTg8Gv3CH3aAltpd0EUCcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1071e13e2a.mp4?token=lWKgBqtBwXZ-_9SYpognpKAyD3SUG0AcyhOQbb5jhuamZhIL8cg0e0-XhfSuCeZ8KyhQ62EWjX1BT2jJPDp2y7Xj2hVL_OW6hqqYqQPPl4d1MDwA0XUxmXz8sy-h1qUWzxM18q0gPkNTSiUh-lS2tKc-7OFjxCjsZc_Wa8oYJc8CWmL4loKuF62D2Oqjcb1hdGIcbyS5btt_DjXGYiZL4S3WV4ggrh6elmrhpkmSZHeHlGApqwLiXNuI6lrieR4m7WsVNIAji8M6pSCS_GKKbO5PlZIgLZ8OLTT1kl5b3MNnwoCXP8hTrsftxIHp7M5RJTg8Gv3CH3aAltpd0EUCcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مارکو روبیو در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66773" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66772">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66772" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66772" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66771">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=NviLW0OKNtVryKMIu8L-7dzIBl8DdL6lwN8lgsKga0WjW-_5ZqSJz19NyLklKcMyn9XPI6sgLCwOqo_Rpm0-FbQ6ZLXdIR98dsn99xOSSOJjFLQJD0edxtsEvhBhSG9UI2OB_6J-o9YhbHxXNOawc4Bw5I56tzORxlJb2d0ni6GW77wkgEWGra0lsHKKiqcwjOajI2k3trNAUuh2dDR5WdbPX8n_knHqnF1bmcTNcf9gAIoO-W5EIsE64fEggyXSgidtbq8LM_R5AaXAK5C3G4pN-UFnL9tNu4lwXQ4mzM6nRbcX_VTt6T4k1ZuhNdWThC9z-SIFi8kcRZwbCOOEdGfIrR8vH_SoK0acROD8JYRuJzTh5oZY-_mgXHowSuND2gaXDqnVQY0K6Oc7k7w6RgDf4jvlomy4nfrmI_nDDQkGlVP3iGiHWLszFM140noA1c4fT2SjtQpe0g2BkitBQpM9ZOojTkspFAYmeG7TtWuvqI5gW5vbjCLjMweLaZCkZuH8jPrG_WiJJhZ4c1OQuuDdSXtR-a59d0Ev9X4fse7wgHt-9NUy4a4cmUYjhZUaHdbMTZyfNkJiW0XNvDHz42As1iNTyD8dJy6ocVUQjSwFwtEMaXWdRx-8qYs0XxO9XCjdFawmPuE5gKdvt18uXep4Vqu3aZ3EKFRqgUwKfuo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=NviLW0OKNtVryKMIu8L-7dzIBl8DdL6lwN8lgsKga0WjW-_5ZqSJz19NyLklKcMyn9XPI6sgLCwOqo_Rpm0-FbQ6ZLXdIR98dsn99xOSSOJjFLQJD0edxtsEvhBhSG9UI2OB_6J-o9YhbHxXNOawc4Bw5I56tzORxlJb2d0ni6GW77wkgEWGra0lsHKKiqcwjOajI2k3trNAUuh2dDR5WdbPX8n_knHqnF1bmcTNcf9gAIoO-W5EIsE64fEggyXSgidtbq8LM_R5AaXAK5C3G4pN-UFnL9tNu4lwXQ4mzM6nRbcX_VTt6T4k1ZuhNdWThC9z-SIFi8kcRZwbCOOEdGfIrR8vH_SoK0acROD8JYRuJzTh5oZY-_mgXHowSuND2gaXDqnVQY0K6Oc7k7w6RgDf4jvlomy4nfrmI_nDDQkGlVP3iGiHWLszFM140noA1c4fT2SjtQpe0g2BkitBQpM9ZOojTkspFAYmeG7TtWuvqI5gW5vbjCLjMweLaZCkZuH8jPrG_WiJJhZ4c1OQuuDdSXtR-a59d0Ev9X4fse7wgHt-9NUy4a4cmUYjhZUaHdbMTZyfNkJiW0XNvDHz42As1iNTyD8dJy6ocVUQjSwFwtEMaXWdRx-8qYs0XxO9XCjdFawmPuE5gKdvt18uXep4Vqu3aZ3EKFRqgUwKfuo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66771" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66770">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOjyX4fYL5uAcBI65IInelQm1cbu-a0hNcgliQMI2KtOPvG1s40J4oIXviD2B5sSM_nczHK4Hsy5JR9DQPYNZVl83Zis2amdZ46TEz9X4wZNwk-a45pbeWh3ue_9Jvk8zzI66faDYvye_JA5FMM2XEMknAswJ_mk5fjNuQgAM40eVZBRWw5ZUKM5nz1eDSUI4kS8XI1AtnkxfxPqvUW00HbcOEHShfxmxysDOU_XRNV65XdV7AKFuT6OmNkvrJrueIURO7BYNRgjeiJh17O2Q_2qTOSPjGIcIzrGrd87t_Sig-BDCMztx1GKNAqDur1GIAr8aljA6Z7OgL0MzsxYPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت
ترامپ:
ایران به آمریکا اطلاع داده که، برخلاف گزارش‌های دردسرساز رسانه‌های فیک‌نیوز، «هیچ عوارضی، هیچ هزینه بیمه‌ای و هیچ نوع هزینه دیگری از هیچ کشتی‌ای که از تنگه هرمز عبور می‌کند، توسط ایران درخواست یا دریافت نمی‌شود. اگر این خبر نادرست باشد، مذاکرات فوراً پایان پیدا می‌کند!
همچنین، آمریکا هیچ پولی به ایران نداده و هیچ بخشی از پول‌های ایران را هم آزاد نکرده است. ما بخشی از پول‌های ایران را که کاملاً تحت کنترل خودمان است، برای حمایت از کشاورزان و دامداران آمریکایی آزاد خواهیم کرد تا با آن ذرت، گندم، سویا و محصولات دیگر خریداری شود. ایران به‌شدت به مواد غذایی نیاز دارد و ما این مواد را منحصراً از آمریکا برای آن‌ها خریداری خواهیم کرد.
از توجه شما به این موضوع متشکرم!
— دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66770" target="_blank">📅 17:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66769">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc755f3dc.mp4?token=iQVIyAaHqW0_VW85uPvnQ0NzZtHslXrpEBmrZpDXHNaSzBsBF_xzW_h_ER_QS441aYNkls_9PKI6m4zPrX5zvktBgg6qByk91RZ85HvLcrrUuhqmNQDtBiyQJXFmnqcGg55ogGHeVHdudLvGAtRnuqc2FyRy9anmO_fsQ6D8Pjek2W2-rwiMkVIF6cGr4Y12cBAFXuMHWF6jTNPftTu5OkeQ0Ki6uJJXvu2xaCYEBEw0Fb8XruAR2BDTal8j_NLitFbKzryVYocVCp4MIA6CI4mPuizuCZ-47I1TFdB1-A6u_rBDFD0JcFuaio6T3Cz8QJmb9PO4cYsv_8RhEj210w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc755f3dc.mp4?token=iQVIyAaHqW0_VW85uPvnQ0NzZtHslXrpEBmrZpDXHNaSzBsBF_xzW_h_ER_QS441aYNkls_9PKI6m4zPrX5zvktBgg6qByk91RZ85HvLcrrUuhqmNQDtBiyQJXFmnqcGg55ogGHeVHdudLvGAtRnuqc2FyRy9anmO_fsQ6D8Pjek2W2-rwiMkVIF6cGr4Y12cBAFXuMHWF6jTNPftTu5OkeQ0Ki6uJJXvu2xaCYEBEw0Fb8XruAR2BDTal8j_NLitFbKzryVYocVCp4MIA6CI4mPuizuCZ-47I1TFdB1-A6u_rBDFD0JcFuaio6T3Cz8QJmb9PO4cYsv_8RhEj210w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اگه
فکر می‌کنید قراره چیزی کسشر تر از این امروز ببینید عرض کنم که سخت در اشتباهید. فقط کافیه موزیک ویدئو شاهکار صداوسیما برای تیم امیر قلعه‌نویی رو ببینید تا بفهمید با کیا شدم ۹۰ میلیون
😐
😐
😐
😐
علی بیرو تو دروازه یا نیازمند ، کنارش شجاع و کنعانی میشن پدافند
تنگه هرمز ما تو دستای سعیده
شوت‌های قدوس و رامین مثل خیبرشکن، مستقیم به قلب دروازه‌ی دشمن میرن
ترابی دریبل‌زنه، نعمتی هم حامیشه، مثل هایپرسونیک از لای دفاع رد میشه
یه طرف میلاد و ازون طرف جهانبخش، پهباد شاهد رو روی دروازه میکنن پخش
حاج صفی ، حردانی و یوسفی مثل شیرن
توپ‌های علی علیپور از پاتریوت هم در میرن...
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66769" target="_blank">📅 17:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66768">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f90bbfd79.mp4?token=ZzzFTVb1R1-5fpEvmz7_mozqQKk9U5nYpE18RqanMIBNmq14Pn8Sybk96Yalb87Hq73J_8C1-btuakkEEkpicGutpCynhDCswOXUpGtbasKGGOvLmWleBOvPNzmdAqgop1AmRgO3rGqbhd_xenNoLt4SSCDboycKXrq_thDv2O-nrD1gfSDqRE7Sz7mrmBQkU7sDD3J8UF6j99j36jh-zVmojZoXVBlNyBQ3AtuFek8F-7CAlwJt3NgO7W33AQ34b2UoYU6AO8nI3Z4DGSQgwfVlMeOvah-3bUP0IW20q2OMaUYhNauEe1sPaT5HqfXpTWlyhfE7f2hKYFhhn2cqIh2pxs2Hrw8McPkEbQFbcouCU9cPAM142abNDj_H0djQ5iioVEOjgVJ4iCqBWKeIDy9TLIE7ZKp67yv50utp27CKG7q8zL16h1E018XcjbPPRWPXGhcOBL-S60NTOzGvjPq3IIDn7DFB7ysARsyb8gc0p2E0HDg-td4p6ukQ_7_rFTpgFlNfdfdlaUbpBbqkvhpguURgsUkctjyfuKRkEY9XdWYLteOVeQmqvayXqpzws-poWRRR2FEIY4e2sBXYM3sMun9Zpfh74SEV56l2oEuL1fZyC8HgkH_RljBUHJb02XKgHGdwObMxTYoWVzK6n7-TDS5KxYl2FjnlDAqgJDY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f90bbfd79.mp4?token=ZzzFTVb1R1-5fpEvmz7_mozqQKk9U5nYpE18RqanMIBNmq14Pn8Sybk96Yalb87Hq73J_8C1-btuakkEEkpicGutpCynhDCswOXUpGtbasKGGOvLmWleBOvPNzmdAqgop1AmRgO3rGqbhd_xenNoLt4SSCDboycKXrq_thDv2O-nrD1gfSDqRE7Sz7mrmBQkU7sDD3J8UF6j99j36jh-zVmojZoXVBlNyBQ3AtuFek8F-7CAlwJt3NgO7W33AQ34b2UoYU6AO8nI3Z4DGSQgwfVlMeOvah-3bUP0IW20q2OMaUYhNauEe1sPaT5HqfXpTWlyhfE7f2hKYFhhn2cqIh2pxs2Hrw8McPkEbQFbcouCU9cPAM142abNDj_H0djQ5iioVEOjgVJ4iCqBWKeIDy9TLIE7ZKp67yv50utp27CKG7q8zL16h1E018XcjbPPRWPXGhcOBL-S60NTOzGvjPq3IIDn7DFB7ysARsyb8gc0p2E0HDg-td4p6ukQ_7_rFTpgFlNfdfdlaUbpBbqkvhpguURgsUkctjyfuKRkEY9XdWYLteOVeQmqvayXqpzws-poWRRR2FEIY4e2sBXYM3sMun9Zpfh74SEV56l2oEuL1fZyC8HgkH_RljBUHJb02XKgHGdwObMxTYoWVzK6n7-TDS5KxYl2FjnlDAqgJDY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
⚠️
پشمام اینو داشته باشید. تو عراق از معاون وزیر نفت سابق این کشور حدود ۸۵ میلیون دلار اسکناس نقد از زیر زمین کشف کردن که دفن شده بوده!! فساد سیستماتیک تو کشورهای اسلامی ماشالا خوب رونق داره
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66768" target="_blank">📅 17:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66765">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c68737622.mp4?token=Ljv_QkBNPht7IvQE4WK3z4LRnOcawO0gND9HLy06tjIMqyxRI016t-eJRHoGFxrTie2W_F7IfFtOViZGlXO6h_iJwzccCvJj1_CQXHUX4FO5K7Ja8wc5i39AFixSoVJXMf-i-_bSN9Tq2pm--PayLa-m6qQ2N1naUpMeELwBpd1iaSyF8xfuWwwhPM6qMPc2GrDphj-fIzP31o-7uKCZxmIbjszeVQN4D3ryCssh4N1-EsBCQQTMqb0r26VjnPfPkMk0BwhDxLdZ9RHmI_nyQWphS-4fTGole4jzVmvuHnC4lPsj_u39EX_WCFdwGwMJDKcCQCZwX2BiHNw_EOFf5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c68737622.mp4?token=Ljv_QkBNPht7IvQE4WK3z4LRnOcawO0gND9HLy06tjIMqyxRI016t-eJRHoGFxrTie2W_F7IfFtOViZGlXO6h_iJwzccCvJj1_CQXHUX4FO5K7Ja8wc5i39AFixSoVJXMf-i-_bSN9Tq2pm--PayLa-m6qQ2N1naUpMeELwBpd1iaSyF8xfuWwwhPM6qMPc2GrDphj-fIzP31o-7uKCZxmIbjszeVQN4D3ryCssh4N1-EsBCQQTMqb0r26VjnPfPkMk0BwhDxLdZ9RHmI_nyQWphS-4fTGole4jzVmvuHnC4lPsj_u39EX_WCFdwGwMJDKcCQCZwX2BiHNw_EOFf5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
⚠️
ویدیوهایی که خیلی از دیروز  وایرال شده از کربلا؛
دیروز کاروان شیعه اسماعیلیه که تا امام ششم امام صادق رو قبول دارن، واسه زیارت به کربلا رفته بودن.
از اون طرف کاروان ایرانی ها هرجا اینارو میدیدن واکنش نشون میدادن..
تو یسری جاها هم نزدیک بود دعوا فیزیکی بشه که پلیسِ عراق اجازه نداد...
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66765" target="_blank">📅 16:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66764">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbff1343a7.mp4?token=acPwnIpXeSQS5AsJ7kOeWdKnkEI2kSSs5iC_jTkuMi-bCDo9DOvAG_GW3KYHcdyn-zmPgWSLWs6kghNoU3L3uGo0xesstdpD2nEPVuL7oxw1RGZPYqzBsoj5DSzzMHTZwHV8a-V6WziylkYBhiCWnyP8X7fxwy4PQnqr6ExE6NpF6_kKLeealzIOnPlk8AkR61L1sxa_v3hHhFJNy_MulMVC6soh0Y9wau-IsbtF-GCwyGxKYZ3Xr3E8dV5sp5ZqjlvS0v5XQSAC6jMFKKOvpQjMukirtjeb7YRq9iBDGn8qGUQT2hXFJqq1trxcbUYQfMvPD0kL2c2vUkHFCoMDdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbff1343a7.mp4?token=acPwnIpXeSQS5AsJ7kOeWdKnkEI2kSSs5iC_jTkuMi-bCDo9DOvAG_GW3KYHcdyn-zmPgWSLWs6kghNoU3L3uGo0xesstdpD2nEPVuL7oxw1RGZPYqzBsoj5DSzzMHTZwHV8a-V6WziylkYBhiCWnyP8X7fxwy4PQnqr6ExE6NpF6_kKLeealzIOnPlk8AkR61L1sxa_v3hHhFJNy_MulMVC6soh0Y9wau-IsbtF-GCwyGxKYZ3Xr3E8dV5sp5ZqjlvS0v5XQSAC6jMFKKOvpQjMukirtjeb7YRq9iBDGn8qGUQT2hXFJqq1trxcbUYQfMvPD0kL2c2vUkHFCoMDdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مترجم: «ما هرگز در مورد توانایی‌ها و تجهیزات هسته‌ای خودمون توافق نمی‌کنیم.»
پزشکیان: نه!! موشکی! موشکی را گفتم…!
مترجم: ببخشید موشکی.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66764" target="_blank">📅 16:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66763">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/d59ef82aac.mp4?token=JKNcMKD4H995JlPRKPG76Ieo3rN09_CWTbznnsrN9tZ-xMBDoBsSrWO9nVTl9ZxyItzRMIfE7KThntcYyJtVyeLQF2AM4H7yTuufP0zj2r3pRWzBY_0-U4o9CaOkKUeFKXDI7rQNXUpBc2n3vm9gX1NWXI9j9jaePKLa_9zm-yqAI5CLzaf7fk5F1L70pM6o2kukHHM2FcFCr8xRvT_E1TFuIm_w7cc1I72y2Jh70EM_XFIliMvPHvE2HhkY2Qzy3FE5cITRhN2HSRnBxeCf7pms_4WPSlfVCYmOiKek-jMM_GVD6QUSVrFYBvYa7GqYUU5poWgfuSb0b_QXBlDgdg" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/d59ef82aac.mp4?token=JKNcMKD4H995JlPRKPG76Ieo3rN09_CWTbznnsrN9tZ-xMBDoBsSrWO9nVTl9ZxyItzRMIfE7KThntcYyJtVyeLQF2AM4H7yTuufP0zj2r3pRWzBY_0-U4o9CaOkKUeFKXDI7rQNXUpBc2n3vm9gX1NWXI9j9jaePKLa_9zm-yqAI5CLzaf7fk5F1L70pM6o2kukHHM2FcFCr8xRvT_E1TFuIm_w7cc1I72y2Jh70EM_XFIliMvPHvE2HhkY2Qzy3FE5cITRhN2HSRnBxeCf7pms_4WPSlfVCYmOiKek-jMM_GVD6QUSVrFYBvYa7GqYUU5poWgfuSb0b_QXBlDgdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
مراد ویسی: با توجه به تضمین آمریکا، که گفته در جریان مذاکرات ۶۰ روزه مقامات رو ترور نمیکنیم، احتمالا تا ده روز آینده از مجتبی رونمایی بشه.
مجتبی قراره احتمال زیاد تو مراسم تشییع باباش شرکت کنه. اگرم پیداش نشد، یه جای کار میلنگه و مجتبی حالا حالاها پیداش نمیشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66763" target="_blank">📅 15:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66762">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e65be3ab63.mp4?token=Sg4yG1_mPhsZ-ST0fIFaFJpqopDDX1yJoCreMK1SExaBakrm7Kh8HTLLuu61mCrJ4YdxuNrTAX2Dd6T1PX7bJcD1T54BEPEo1vPLs62HfAKdE-v52FV0UmIWtNh5gs-mZpAVb9M0mjEG6OIw5cBbiJ44ryiz6Betz0nieN4idp1gGF8SedJZ6vs18VCXLgW14sEDVnR-OeUNNuFA2B9Qdj2KpXxZwjyesasoVnh6coQh4PzdY2KfYkMsgznjmbbUaWdevSLcbAN00686EInYG1_Ej89XCsYW8vB3kiPOxb-WQdsW9Du3ttrtGRHrlBExxV1qG2YmH8IVPZeehP3GUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e65be3ab63.mp4?token=Sg4yG1_mPhsZ-ST0fIFaFJpqopDDX1yJoCreMK1SExaBakrm7Kh8HTLLuu61mCrJ4YdxuNrTAX2Dd6T1PX7bJcD1T54BEPEo1vPLs62HfAKdE-v52FV0UmIWtNh5gs-mZpAVb9M0mjEG6OIw5cBbiJ44ryiz6Betz0nieN4idp1gGF8SedJZ6vs18VCXLgW14sEDVnR-OeUNNuFA2B9Qdj2KpXxZwjyesasoVnh6coQh4PzdY2KfYkMsgznjmbbUaWdevSLcbAN00686EInYG1_Ej89XCsYW8vB3kiPOxb-WQdsW9Du3ttrtGRHrlBExxV1qG2YmH8IVPZeehP3GUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مجری شبکه دو:
کاش قبل از جلسه تفاهم نامه یه سر گلزار شهدای میناب میرفتید.
اگه محصول آمریکایی کیفیتش خوب باشه میخریم یعنی چی؟! یه کم بهتون بربخوره
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66762" target="_blank">📅 15:33 · 03 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

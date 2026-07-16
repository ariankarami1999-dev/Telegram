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
<img src="https://cdn4.telesco.pe/file/L1tuLJfKpBwQjBwoQnAMDs_Wd_VONntmzu6aevS7cJv6M63wei3bkc5c0ObUFAQXSiHLDdxic2FzfTre-8-IZoOZBm5-h2cc33Dt0rVSAOros2HXUGHztN4GPhKhtEXkyW9s45OMBSabU87bC7YC6SP6nQ3PcnpbDdgQR5YccQVo35jc1Em-OGrGDLD7sYbRJft_hFsd0RNFKpdDRVb6YBPUWHZXRRKB2btinXRhKi3G1faYRK4F7DODSa1JL_Ho7uLULOEPivnow9GBHzY3Lhof2JDSDYxtKKX7HVNIlBlbkyR5luaDd9HzFfmiMSHs2UH8i8sLSS9slefJTKQjqQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 194K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 21:14:03</div>
<hr>

<div class="tg-post" id="msg-80516">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izIpDhQ3PyLVqYWWsCUC07Xiha0Ivm5jjOX6LFS_FnLDISnA-YXfX_idkh7codpXrSZN_it0hqoEoJsKkdxqlF-Az-W9Gzw_tfxeJJRcgn0ECwbPlDIWSgHjFNffW_kLeKwLho4sCgA6XIIG11XdfCUW3WKuZfOZFfUqS5bdo21fMaBAQcm_1VmiGRY2WCHR-uf1MUENSoVqO4wEZXggMk8ejT6qygEiOHWcBVhzysoSsT1FgjGr9Hb9aU8F3pOP5HfflfWaPLsDcYiDvP7QVZA1GGnmbn7DS87bMQgirrmSBKlU8XQxpPp7y6BziGvxUaR-cmFLH-DcD_ZG25vV2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ویناک به نام کارام هیته منتشر شد
YouTube
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/funhiphop/80516" target="_blank">📅 21:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80514">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">همان همیشگی (انفجار در بندرعباس)
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/funhiphop/80514" target="_blank">📅 19:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80513">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f999836d6.mp4?token=qYEAg5wtPOOcn7xgeqkNVBAHOqli-Ny5NBe6AbDemxklCH9OEskx56rQswekIOwpgbmsMAatqMeBVzBARJD7YbUBpyZpxR5d516Od-rsr6olTMNILN4XbTaWyY52JDt3SMyyFImrJ9VhkWQZdwVi11vcE2zFYj2HmYqYvACFvPdPLxZBeTK9AdvI22JXII882CxXpmjuBFR4EFUNXil6mhxWJBSS5jgZ3_UNS5AHvpPId_oNh31br0ib0R2LVtMhXYIghX41erag4_fTeb0bLfWnuUVn2nMgG5iF_ZfSVoqyP_6tlNnxbNy2470iqD767q4xSQrQpBet0SJRvtxp3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f999836d6.mp4?token=qYEAg5wtPOOcn7xgeqkNVBAHOqli-Ny5NBe6AbDemxklCH9OEskx56rQswekIOwpgbmsMAatqMeBVzBARJD7YbUBpyZpxR5d516Od-rsr6olTMNILN4XbTaWyY52JDt3SMyyFImrJ9VhkWQZdwVi11vcE2zFYj2HmYqYvACFvPdPLxZBeTK9AdvI22JXII882CxXpmjuBFR4EFUNXil6mhxWJBSS5jgZ3_UNS5AHvpPId_oNh31br0ib0R2LVtMhXYIghX41erag4_fTeb0bLfWnuUVn2nMgG5iF_ZfSVoqyP_6tlNnxbNy2470iqD767q4xSQrQpBet0SJRvtxp3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی: مسیری که در ذهن آقامجتبی هست، بهتر از مسیری بود که شورای‌عالی امنیت‌ملی رفت.
مجری: چه مسیری بود؟
محسن رضایی: نمی‌دونم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/funhiphop/80513" target="_blank">📅 19:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80512">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ee2obLFr4HF28HT8ZNEWnP9rG8qUIhWFVwUEN7n0kkzByKDMiHyOpmUzWi4tZnG6RpbF9v5UnLmonhu3nlYR1doZU5uDuqvA2TYIrneUQOx_RPhMBiYzbHymUf2hs6oMQdsvi6OpBcVpFBnIJ8orhkdNeAH5VLjrjxOrgNoo3Oi0iEJWthFZ91mmjxhw1x86XpEAfcC3Ws16ROR0eHGgK0hbmuxa7VJH6VMw_E-8GMEtwmuxctuSj0SResSbWPQaIiCwshR7oMK2OLqRuFYPslv_yY6FnXQHuiuYELTSzdlLrH4bexnpjbd21KSh88Fxs8b57Uo0jnXf8ZmnA6R6wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس ۲۰ درصدی انفجار
💣
⏩
در روزهای دوشنبه تا جمعه، با حداقل ۱۰ میلیون ریال شارژ حساب کاربری در طول روز و ثبت حداقل ۵ میلیون ریال پیش‌بینی ناموفق در بازی انفجار بت فوروارد، در هر روز ۲۰ درصد از مجموع مبلغ پیش‌بینی ناموفق خود را تا سقف ۱۰۰ میلیون ریال به عنوان بونوس هدیه بگیرید.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/BL100
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g25
💻
@BetForward</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/funhiphop/80512" target="_blank">📅 19:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80511">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">طرح استیضاح وزیر آموزش و پرورش رو یه نماینده ثبت کرد
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/funhiphop/80511" target="_blank">📅 18:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80510">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwvKTiizF6wB7p8JbEAZvy-faK6TZYqe-6-XRI6YhIgi1fTTpCG6SUKR2kul1uHFMKJPJ6bDkrwt5Plh6vkASZzvCJPrdXSLdxL_3FJQNlTKibljsyppZ1NTIsupb0uwjjK5lw1Kv_0yDh0Ixegqo0s3U074UdCuzu1ZzMjifrVsVz55s_dbliiVC72z_3tCTomJ452U8TkXX0-tBBQNgX3uWRub42gdqsf3ZqUjOejy2_npF_dBVf0ky-ZnWuIeYQ3GGRk7zVsGqOadA8Kgdvl8OuvUG7b69V-ACjlmJAr05N0W_6RAFPav6vIVtmWXcaXmcfAXz7045Kkzp8vb8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیل برد آرژانتین:
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/funhiphop/80510" target="_blank">📅 18:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80509">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef7072e45c.mp4?token=rn0EbGE6fzouV1Jy6uiR66X3Ger0Dcd_ZTY3Erov_FMr8tzTF9GUZhosNUstoc2utUYMUBFnIJ6j-bhot78AiwwcrdtgrQ7O07rSztGTruPAjtQh_ZwrU34BCrFWL7qaBSabjN1EUmcDZ0ONIm6-YyWWF9huWHkRBybuyN32_XnwOUsV2uD8ZVbb_LYkSRU7z5Kq2KZ_YqRodzNckwVk4_3b81KxxbA3FyfeMKfsuWg4Y9c3N6z6jBTzphQY8Ioxt5aYzMCjGylrYTI7oA8OBQJqZFSEMQRtxvmIsRLnC_eHVZBoA9Q608gTHmi10EOl2X0SNXNYfzKG7dyMQxKD3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef7072e45c.mp4?token=rn0EbGE6fzouV1Jy6uiR66X3Ger0Dcd_ZTY3Erov_FMr8tzTF9GUZhosNUstoc2utUYMUBFnIJ6j-bhot78AiwwcrdtgrQ7O07rSztGTruPAjtQh_ZwrU34BCrFWL7qaBSabjN1EUmcDZ0ONIm6-YyWWF9huWHkRBybuyN32_XnwOUsV2uD8ZVbb_LYkSRU7z5Kq2KZ_YqRodzNckwVk4_3b81KxxbA3FyfeMKfsuWg4Y9c3N6z6jBTzphQY8Ioxt5aYzMCjGylrYTI7oA8OBQJqZFSEMQRtxvmIsRLnC_eHVZBoA9Q608gTHmi10EOl2X0SNXNYfzKG7dyMQxKD3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ستار هدایت خواه نماینده مجلس، که توی تجمات شبانه کلاه خودشو در آورد گ گفت هر کی پول و طلا داره بزاره توی این تا یه نفر رو اجیر کنم بره ترامپ رو بکشه
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/funhiphop/80509" target="_blank">📅 17:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80508">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سلام همون همیشگی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/funhiphop/80508" target="_blank">📅 16:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80507">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ویلسون دیشب عرق لندنی خورده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/funhiphop/80507" target="_blank">📅 16:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80506">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f805fa8aa.mp4?token=Oio2oTG9VWwju00HNePY4PRhcjqD7e4Nqp82g5gVei6FCSVoWq2BzkiAPS6owYGXbyLinc-R9vxhGSc4f0-HzG-6D4ZWV_xgSk6DgxJg_fbXVwGeQBoUXY9GwSz8AJ7t6KOqV-aXgrlrjJKR6JwADXh-Y4iTOgJ4gVCb_4DjOT11OUeqWOTtmjBI_kOiOEF-O06JHAywOJ90lVspxBg6_U7LlwuQzTshS_Gg0_s1aVJYczOQvmcws9hdhW6p-Z8At0n-wcdF47WB_F8Ep8WBImaR8XbA41G_kqZDXgX4ab3ZsMmijMpe3twFOOtMHkB9LRloAIl2YsWZUjzJqlsXFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f805fa8aa.mp4?token=Oio2oTG9VWwju00HNePY4PRhcjqD7e4Nqp82g5gVei6FCSVoWq2BzkiAPS6owYGXbyLinc-R9vxhGSc4f0-HzG-6D4ZWV_xgSk6DgxJg_fbXVwGeQBoUXY9GwSz8AJ7t6KOqV-aXgrlrjJKR6JwADXh-Y4iTOgJ4gVCb_4DjOT11OUeqWOTtmjBI_kOiOEF-O06JHAywOJ90lVspxBg6_U7LlwuQzTshS_Gg0_s1aVJYczOQvmcws9hdhW6p-Z8At0n-wcdF47WB_F8Ep8WBImaR8XbA41G_kqZDXgX4ab3ZsMmijMpe3twFOOtMHkB9LRloAIl2YsWZUjzJqlsXFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فینال جام جهانی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/funhiphop/80506" target="_blank">📅 16:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80505">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">یادآوری بدهی هیپهاپولوژیست به ویناک تا زمانی که تسویه کنه، روز اول.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/80505" target="_blank">📅 15:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80504">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ی زمانی غزه و لبنان و سوریه رو سر اینکه بی در و پیکرن و هر شب بهشون حمله میشد مسخره میکردیم و در مقابل کلی منت میذاشتن که عوضش امنیت داریم، اینم از امنیتتون.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/80504" target="_blank">📅 14:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80503">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نت شمام ضعیف شده؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/80503" target="_blank">📅 14:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80502">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">عجب امتحان بخوانیم و بنویسیم سختی بود.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/80502" target="_blank">📅 13:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80501">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">لطفا فحش های جدید بکار ببرید
جی‌دی ونس: اگه رژیم بپاشه، ۹۴ میلیون آدم درمانده به اروپا و ایالات متحده سرازیر میشن! و وقتی تروریست‌ها در همه جای دنیا پخش میشن، زیرساخت تروریستی‌ شکل می‌گیره.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/80501" target="_blank">📅 12:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80500">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l27XI5Fhc7BQpG85NQBVSUSSHtFfz_oZqKwMhIHsIfgvdcRtab9UmmxrLaLqD7OLAtXgSwtSBNvrptfsEcVFwD0Z5aGso3g5mQNg0K-MiA5VBVyroqdW6AXCHdS_TZw6jn3ok9Y2dDbWBXHJ1Mcvpy56HCEyj3cSJ709agwFAmBP18yjcWY-IPH1c9pprIstPM1IVw-xwmMsUPAbbEvB5krEWnxYqwkOlaoqvWo8zI9xnokw5NSUP3AoLq-mhmdyr-QcPfVR-Aw1H-hMOjLf7zF7oLePD5rRXaQvGtw_RdSf_AjoQ2ocHVTosUc69CrLZLZbV6XT3Fso28vixPJkxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهی بعنوان کسی که مارکت شناسه میگم پول ویناکو ندی بدبختت میکنه خوددانی  @FuunHipHop | Mmd</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/80500" target="_blank">📅 12:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80499">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JEwkdeA_yMRkLkVAFFA0fhh2clboeJriasJp4_1nX-cHHczHWu1pVr7wTu2BW83p18NQ-weMbSTFvb1giJe6KkWvpCCf5mDdIEO4g9JY1w4HGwMPVt9jeuQTtv8Uq6fszpKqZTfdaW4vqXpicOKBBDgOyEnz1ZaOtPeQlYxph8vJxK8cFJ6uEwO9bH2o23A4Av32BJCp2icgPPj0ZhUYp0GQbIjD6THIuwyB6wqtm-BclqV5UryOPGyCtNLLbtRb0yCy0pi_L2lNn7sTFECMrE7Rhp_TuJy04JJfKhyElYrTV3-bHtEDgc99A_nLDPmsrjeGXC9N9vEIuZm-1Kq3XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس ۲۰ درصدی انفجار
💣
⏩
در روزهای دوشنبه تا جمعه، با حداقل ۱۰ میلیون ریال شارژ حساب کاربری در طول روز و ثبت حداقل ۵ میلیون ریال پیش‌بینی ناموفق در بازی انفجار بت فوروارد، در هر روز ۲۰ درصد از مجموع مبلغ پیش‌بینی ناموفق خود را تا سقف ۱۰۰ میلیون ریال به عنوان بونوس هدیه بگیرید.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/BL100
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r25
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/80499" target="_blank">📅 12:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80496">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05fceed0ed.mp4?token=BZxv5mvW1dmG8QBTxR96CwMt9V0FkRHWs4oA7tc-QGsbA0pT5x1Ef-pb0_LtbCb22OUwit5j6mUL-E9jz0ZttSirD9xdwc0ukf6JNLiMOyjrQigriuZYcEO6uBth4Z9TwtmqOFr1vMcUWWXCeOX1WpE1nVhQODuIFMEFOAWpktaLNq_BKyKRYruVPMtTQpVqYPVAYivYt_GC79WY-2Ypo9LW7DV8dmLhDP4nAlwvlF7F7Nj4JAHdWxp0zljUljoVuZJMd1ipbWH0UX7dcvfFiZ6Rpy4heLphft6vhMBrO-V94lZJSHyOJw75QB1Jl1CxjDGTN1KlfXXE4SEMh-tHUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05fceed0ed.mp4?token=BZxv5mvW1dmG8QBTxR96CwMt9V0FkRHWs4oA7tc-QGsbA0pT5x1Ef-pb0_LtbCb22OUwit5j6mUL-E9jz0ZttSirD9xdwc0ukf6JNLiMOyjrQigriuZYcEO6uBth4Z9TwtmqOFr1vMcUWWXCeOX1WpE1nVhQODuIFMEFOAWpktaLNq_BKyKRYruVPMtTQpVqYPVAYivYt_GC79WY-2Ypo9LW7DV8dmLhDP4nAlwvlF7F7Nj4JAHdWxp0zljUljoVuZJMd1ipbWH0UX7dcvfFiZ6Rpy4heLphft6vhMBrO-V94lZJSHyOJw75QB1Jl1CxjDGTN1KlfXXE4SEMh-tHUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کتکشم زدن تازه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/80496" target="_blank">📅 10:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80495">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FfpuU0DW8frTTSo4Lr6Bn-Y-2Qsq1baRKn0sNw9vcLIjN6jR6whsLbHN9dkXEQFqyL9X-2dWAS2NkC705xzLa_rcK0Vg9etPT5Kd2AOroTUVDsTQTxe30-g1KjOgFOFkzg0kROefjpE5KMrC1l47vtqG6pm7yIB42ACCICbuYlwUcQPF8bLZapA4JMlAQcUh07YivOAH-2vn7pBZS5G6Ucm7Ov_mK6iIMbjqcL8k0umQIBWT296ukFQt2c7UsKA4Q_m2bqAhmG6jw7jobNXR2A-0oXTC6Bj_DsbAJOqWv_HPtpJuW7O7bRpwHXIJSj_U903WBDaT8siTY9zQ-JEXSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان بخدا بلینگام بدبخت داشت خطایی که انزو روش انجام داده رو تعریف میکرد، گاییدید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/80495" target="_blank">📅 09:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80494">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">فکر کن خاورمیانه چقدر پیشرفت کرده که دیگه تا خودت صدای انفجار رو نشنوی حال نمیده و هنوز جنگ حساب نمیشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/80494" target="_blank">📅 04:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80493">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کسی تو سمنان زندگی نمیکنه خبر بده، چجوری متوجه انفجارای اونجا شدید
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/80493" target="_blank">📅 04:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80492">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">رئیس مرکز اطلاع رسانی و روابط عمومی وزارت آموزش و پرورش(صادقی): اگر خدایی نکرده شرایط جنگی در استان های دیگر امشب تداوم داشته باشد ؛ جلسه ای شبانه برگزار خواهیم کرد و تصمیمات جدیدی در مورد تعویق امتحانات نهایی در سایر استان ها خواهیم گرفت  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/80492" target="_blank">📅 04:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80491">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">رئیس مرکز اطلاع رسانی و روابط عمومی وزارت آموزش و پرورش(صادقی): اگر خدایی نکرده شرایط جنگی در استان های دیگر امشب تداوم داشته باشد ؛ جلسه ای شبانه برگزار خواهیم کرد و تصمیمات جدیدی در مورد تعویق امتحانات نهایی در سایر استان ها خواهیم گرفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/80491" target="_blank">📅 04:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80490">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">هگست داداش اگه مردی چنتا جنگنده بفرست باز کشور تعقیب گریزی شه
موشک مزه نداره ترس داره لعنتی</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/80490" target="_blank">📅 03:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80489">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">گویا اراک و زنجانم زدن، موشکا تاماهاک بوده
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/80489" target="_blank">📅 03:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80488">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بر اساس تحلیل های بخش نظامی سازمان فان هیپ هاپ، در موج های بعدی تهران، سمنان، کرج، مشهد، اصفهان و تبریز به شهرهای هدف حملات آمریکایی در ایران اضافه خواهند شد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/80488" target="_blank">📅 03:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80487">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">پارچینو زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/80487" target="_blank">📅 03:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80486">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/funhiphop/80486" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">شاهی علی الحساب یه‌مدت شماره ناشناس جواب نده
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/80486" target="_blank">📅 02:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80485">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">شاهی بعنوان کسی که مارکت شناسه میگم
پول ویناکو ندی بدبختت میکنه خوددانی
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/80485" target="_blank">📅 02:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80484">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtFTv8tvpeqppAD0B-oHJ22OAWDtxtq_g7_vNbBZlJqjJAkWbVlm9G340stL7ZBQRmThhCaOHTtABKGTy1iulTwclFybK91qBw4LaUPWx5e7_KX6_QqInEBYb-NmBzOSZvVe0Ee_a8UVvj6RVRn82dIfpaDK8_Y5Gw-Zh9n9GyOuo_pJve8_EtHcq0N9UoA2ID5xZ5B13AnKWLfs7_uzT6dQ_MODR4iZTiRjRCUKk2xL3t2-smnr1BaVDJKLe1ZYouEcagxroPYc6RPRBobVfkNz62S90EKTa9Zjpqn4Q66KwDxOs6VkPcNzh7RklcOKpqME3gqZgHv0V3iucGn9UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها کسی که بیشتر از من فن مسیه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/80484" target="_blank">📅 02:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80482">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvcMd03rf_Oo44ekxTJpr2DSArrP6x43mQVQRSB_qa-FD870fKjIsS3GJkSC68hBWjH-8QqVfJzh2W_Gc8QjcUVIXe2quNLYkgzx0_NB6kMA0qWTB7FEtKg7n0bRHbFL2ySm63ADPZVoZ3aWahsnMa3D3EP5T6cTUk7VmZMxHot1ncY28Np_XnYnAg4-RQ3F5kVZW8COjh6Xjm-PrFesJorQOTR9xj3ohQxlND6uM-79vuF_rfNzE-pD7Xt4cQSLu-8u7C9_jw66CDU_JLCIUrIcAeVf5HWyrb8AJrAqzfpwIxiSz4kSstcv2D46UI2-ebLKFpCrW6d3shRjCsZTgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان مثلا چرا مجتمع سپاه باید بغل بیمارستان باشه
بعد این فقط یه عکس از چندین عکس دیگه تو اهوازه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/80482" target="_blank">📅 01:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80480">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">متاسفانه گویا امشب حمله به بیمارستان سرطانی کودکان داریم
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/80480" target="_blank">📅 01:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80479">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ننگ بهت ایرانی، گرم فوتبال شدیم ندیدیم چیکار کردن با اهواز
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/80479" target="_blank">📅 01:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80476">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z008XXkEcBgl1m_AT_vHlp1W6_0OiuWjFKL4e0F2hQElDMtCL4_nURcTp05eZjx5zifrq0bOI4hVNYloPDrqVi2ol-EOkIFk229uvz_t0CLcpd-nlGRNd6TCDLOCHlb_gRcWNuEK821P5TykxOstOQpUbbQaMJkiAVzNxhyGG3uMxYph2y4gtHDqTBcsp5fMyKNvsTpFot7y45IF6TbxGHtp7uWIEQ_oZ42nyhlfRJAJZXKV5Lm-EY_piXG4pVdUvysBTDv7QTq_Difg5-Ta1L9quD18CaUcihBsFz9agQw8uhA9pCoLd5r7cFT7LUDJN3PKUivgoj3as7DLbn2GeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jKjH8VolGzCXQFVa5LkMc5zON8FkF2kThDUsGSgnbA8Sd7Fm_oEsOzrVHYhH_kp8eKaKrsPl7uwZagLxC9L3xUtnQlBLK3RcFErfGOoAOYATHpWweFjE5aSXyS3QJDAtORRHiz8CXps3NugN0S580qCOVnEfSJXdTquNgO8Au2EaBUFSBPvnoYtBw4W7IOXZ3OwLVmUXWboT68x9ZRrUmjwUlsBaWCU7fVPC7UEpCaWK6ZPfZHvCB5tQIKwfDiJ_AIRuBrHdi-hZRadug22JrwH7Kq9wG-EYqPVElVCZKnLJ-kytANVvJAG6CVsyEzlXl1Wrvm_aoj6Kn3DtuHD2uw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یا عباس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/80476" target="_blank">📅 01:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80474">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JEqwlwjvR9qaCW7DGajd7friNbRV-f-3EQWLxYO8zeM0R_ouXASIIRN3QUwBnsAHnInhe68QTr5N7apHhErx5X_6vceYBENGqQuqFj3JMJGmklWtCPzba1vivOuWsZlsq0VwYXDAuFxEj20N978Iych0DvgcoUA_p-_hXvL84UDwqXlfMie7sHZ0qNr-YCxCnMhujXKMZcDn3ocyQfE_c8Kov0E1i_Mha4Y70VsvliQZAg7XgAYYsnwLbEOS2otrt_h3uIL5rH5uvgTpbG-GNTXfGXLyhO3QSqxL56dywXCeuubEmYsZbhPSLZxKGQrpXn0TT2pM1wkyovwEZqcX4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزا جان ببخشید
🙏
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/80474" target="_blank">📅 01:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80473">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">رونالدو فنای عزیز صحبت کوتاهی دارم،
جدای از اینکه جام رو یا یامال میبره بالای سرش یا مسی
باید خدمتتون عرض کنم که مسی اقای گل و پاس گل جام جهانی میشه و توپ طلای بعدی رو بهش میدن.
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/80473" target="_blank">📅 00:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80472">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ساکت شید شبهه علی دایی نواخته
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/80472" target="_blank">📅 00:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80471">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromvahid</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrsjAoihpwqIClSTNZ_YF1VU_rhGHY3irf18JIxylXUTyz8Spl-XZ3cz_xp6s5Z-NyIYvB3BEHRKLPQ60CTzX6Wada_SgiCRLO2PTH8lRgBFNMX-d_YC17xSUaQjaWOZqN7fwXHDQJ0PkFdGkeCCZi3M6q99gp5MDWUi8iqWlv-a5xnAs2V7hQN9hFMxcEtPXDK1xeN53t-VHnpr07JdsJlFbXjUOfjsUTGUpBzXGbkBCA49tEsXBl4NA35JQoTjC1zsXnTvysEq9q0gfLbgbtgpBr2n2Zid70kPbosG7zIjFCGAkC4gpYs0vfFzV0VSnCjc4uLPaYeXoSeqp0Rq7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازم ی سری جذاب و خوش چهره ، جلوی این گوژپشت اوتیستیک کم اوردن
😔</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/80471" target="_blank">📅 00:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80470">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">تا ۲۰۱۸ رونالدو رقیب اصلی مسی بود
از ۲۰۱۸ تا ۲۰۲۵ امباپه
از ۲۰۲۶ به اینور هم یامال
تو دیگه کی هستی پروردگار فوتبال
🔥
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/80470" target="_blank">📅 00:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80459">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">دوستان بخدا کلیدی ترین بازیکن اسپانیا رودریه، چرا انقدر عکس یامالی که تعداد خطاهایی که برای اسپانیا تو جام جهانی گرفته از گل و پاس گلاش بیشتره رو میزارید رو پوسترا</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/80459" target="_blank">📅 00:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80458">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">صداسیما: شدت انفجار ها در اهواز بالاست، در خانه ها بمانید.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/80458" target="_blank">📅 00:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80457">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سجاد شاهی ویناک گفت پولو ازت بگیریم بدیم بهش واقعیت</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/80457" target="_blank">📅 00:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80456">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">انگلیس عزیز تو امشب به صورت استثنا فوتبالو از دست آرژانتین نجات بده ما فینال از اسپانیا درخواست میکنیم مجددا فوتبالو از دست شما نجات بده  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/80456" target="_blank">📅 00:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80455">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0EPksMtt7G606AKVeEZIlBuVM_6rKGlBeoFWbxj0pW4RmS-o7WEas-opxWV2EpJpJaD5QDOgFHwn_VBSs6DF0L07e2DFw00771V3qU9v1dUycgQpdWtV8vSGsoRh2ikEXa4zCQP8GdQpdIVjAGQ4NJdVA6gcf9XsLGhnOBikCbW8n_c2gBHL4bo28tXygMQMoorN3VIy9OA2Nd4wWArfH7KHU2_FVwMtiEzY1LejY8vOgleNGPeC_tUQQhLdy8g2gI4lAJA5hgcKIFQXbXIeFhLVdMoZB94w10wc_uETwBzPQadSJ8OyHQHZDPuJqiT5lWu6QBIhY_81cNj-BfWYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتقام سلطان رو بگیر پسر
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/80455" target="_blank">📅 00:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80454">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">حالا از دکل کی میخوای بالا بری رئالی
😂
😂
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/80454" target="_blank">📅 00:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80453">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">کوکوریا دکل بعدیه فک کنم</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/80453" target="_blank">📅 00:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80452">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">فینال بین بارساییاس محض اطلاع</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80452" target="_blank">📅 00:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80450">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">تموم</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/80450" target="_blank">📅 00:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80447">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">این مصدوم شدن بازیکنای تیمای بزرگ مشکوکه
رونالدو فنا پیگیری کنین بیکار نشینید
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/80447" target="_blank">📅 00:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80446">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">شاهی ویناک پولو نگرفت بزن برا من</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/80446" target="_blank">📅 00:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80445">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">توپ طلا نهمو بیارید بابا</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/80445" target="_blank">📅 00:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80444">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">پیکفورد چربش کن مارتینز اصلی اومد</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/80444" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80443">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">وای وای</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/80443" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80442">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گللللللللل</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/80442" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80441">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دومییییییی</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/80441" target="_blank">📅 00:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80440">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اکثر تیمای بزرگ مصدوم دادن حذف شدن</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/80440" target="_blank">📅 00:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80439">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔥
تکل موفق از جود بلینگام</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/80439" target="_blank">📅 00:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80438">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hg2fqGTgaoxsf1wbJ1_oAWbf7lHX1MXauvZCcqzhzBtI9EYuhTMWxk74E82sfLGmY1Y0uLo6uOTKXaBNkLq9CvcqfpfITqvgS5YWO__Yu_mf7ALvULwUHRJJ_8ENu0gtF8lnkc8f6ALoWAdfCmJNYY1HwftzYJFSH57cgRzabJ5jYlew6Yi0jEm7FtJUm2Gf8gTebGURiygx7OPXkj9m_fjdz1nl1TuBndhSVNgzGwN07V5o2BCtoPCqqK4gcuDZOIF0SodGtuTLdKAz_jUyCH82F9yzyLT3hQzVKEGrpDB67hfxfE_L_yJN45C5PgeV_mY7z7e1BVxDkrwECUbNDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به همین مسجد برکت میام برات بمالم</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/80438" target="_blank">📅 00:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80437">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">خدایا کیرتم</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/80437" target="_blank">📅 00:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80436">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">آرژانتین زد</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/80436" target="_blank">📅 00:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80435">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گللللل</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/80435" target="_blank">📅 00:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80434">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">پیکفورد چربش کن مارتینز اصلی اومد</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/80434" target="_blank">📅 00:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80433">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">مسی باید تو اوج خدافظی میکرد تا اینطوری یه بچه کون توپو از زیر پاش ورنداره بره</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/80433" target="_blank">📅 00:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80432">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">خدایا امتحانمون نکن</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/80432" target="_blank">📅 00:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80431">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">واااای کیر</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/80431" target="_blank">📅 00:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80430">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">چی گرفت کسکش</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/80430" target="_blank">📅 00:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80429">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مسی کیرتو بکن تو بکام کصکش از تیمش برو</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/80429" target="_blank">📅 23:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80428">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">گوردون برگرد نیوکاسل کصکش</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/80428" target="_blank">📅 23:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80427">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">انگلیس زد</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/80427" target="_blank">📅 23:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80426">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اهواز به طور متعدد و وحشتناک صدای انفجار میاد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/80426" target="_blank">📅 23:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80425">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">این بازی عجیب وایب بازی آرژانتین هلند ۲۰۲۲ رو میده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/80425" target="_blank">📅 23:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80424">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">نروژ عزیز لطفا تو دیگه امشب فوتبال رو نجات بده  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/80424" target="_blank">📅 23:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80423">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اهوازو دارن میزنن</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80423" target="_blank">📅 22:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80422">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">زلاتان ابراهیموویچ:  انگلیس دست خدا رو قبلا دید، امروز پای چپ خدا رو هم میبینه.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/80422" target="_blank">📅 22:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80421">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">زلاتان ابراهیموویچ:
انگلیس دست خدا رو قبلا دید، امروز پای چپ خدا رو هم میبینه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/80421" target="_blank">📅 22:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80420">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پایگاه‌های آمریکا در اربیل عراق مورد هدف قرار گرفتن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/80420" target="_blank">📅 21:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80419">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHeSaM</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOsnOicjtoEPriE7zQlvek9e08__id8giR-mWyK8uVl57vPSpPaIFuwgQZjqk7mUVnSRg3Kuksr01LRjXoXRHHt3YA1zTdoOcY3nbJ9vS67hZgOzcQe46uOxPQ9Xo4I0v0CePdmd2TD7qzABZ3Ho-hcYrxl308QHFjDA99-9QKRYUAIUCrPfgPebqOM5KvYchT4KgqPvD7Z0KqxU33UlD4U7DntTr32xnf90cFbsfyGSYYXdVA75XcTspqcpRMznS2e0IwRYMjoaKTjG2IqKU0Hjd0F__ZTEv_D1L6iw0-254YKK9kok0dy7NNwdC4BtB0XrooM864njbgH8JREIOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرتون وینه؟</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/80419" target="_blank">📅 21:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80418">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eD3QAl0uuE9CU5RJr9oQf9tT_S6IzROBtta4sYKpQUtCFxCxyVFTAIBDINBqVbpg8_bo41mNddqyYoBwd3x5yI_S3m3c_J1if8Wdytav58EQY4tw4XeMO-xe3W_LOD10FleN5zC69qPx8ffWwj-dn6nprs6eoCHtNW8ECVcR4TyLwz4HK4b7R__a2mhR3ydk-VSxbQtEdJPHObt8UoEuAFwjBGKhARxX_o3aG7nc_KOE77lox_JNIbZyNlTUsKuyeGph2DXuMRsjZHMezziYNNuS0GMDEsRosOpWlKutBz8dRZwlLQEP7LMchnCokXimCrwa5JkOqD83jPPQT7Jj0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واا مگه میشه</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/80418" target="_blank">📅 21:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80417">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from-FA</strong></div>
<div class="tg-text">واا مگه میشه</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/80417" target="_blank">📅 21:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80416">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">تیم برنده فینال میره برا سوپرجام با پرتغال بازی می‌کنه   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/80416" target="_blank">📅 21:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80415">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">تیم برنده فینال میره برا سوپرجام با پرتغال بازی می‌کنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/80415" target="_blank">📅 21:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80414">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpqVdCFBIJCr3s_nEoCdkZ82YU76lcGLLMuNcf2MsSBKFokvpSzjsEHonjLRDGfycwkhnNYMGDHLg7MzxroBteUntQx-7raYxHXBwOtvrkXhJihal4wY7A2t-3eN2ZHALfp_hBXjo_ZCq2kp2r5Ara6yNy7NNTKaFso6FG0Ds97-o-rloT2ZLNWvzRwN83N5VLy4qIln2QT03bB-B2RZ52IC7F_px5l1rKd0jxfth-WSO32h9yO3BB-RhRfL4Q_-M4uUKkqlPi4CJtfaZvLvHbdEhibZ7fxq5Y6XM-M50OBpmFt3UZuoRbkDWvvQE9CGTwK0mUvhgyOdn_uhJz3y-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب انگلیس
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/80414" target="_blank">📅 21:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80413">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">بیچاره فنای رونالدو اگه امشب آرژانتین ببره ناچارا طرفدار اسپانیایی میشن که پرتغال رو حذف کرده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/80413" target="_blank">📅 21:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80412">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgaLfr0B2CMonLgEvUR_LxGAJKQ8_wAMut8FSJz_36hBM4HZnZTBJw6jOTntrp-DB8eGFAvETcT5NdR2v4iF_QQF3-SIyDD4eFb7g37Leo-p5JTEkSRhboFI3gKMK3eBnCTmtGTOJ3ufoq8w4bIgm4Zfsa02NnRfxyx9qF_ei1kS0OKkeQec9xyypuqmd9Gy-vz5Ui_LbFkw8Fib8PZOKkqFU7o8hYVJ1RZ-RmCX-F0wOxAZEVie6hb4we1YLMqQt1jrdz2AgDW-4wUsCECuvYxKzM3TiMZjFBAdqdlDYy6L6YdJWjEA5Idn5QO-o4TSBgPw03GTMBKVRNzyze6j8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب دومین فینالیست جام
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/80412" target="_blank">📅 20:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80411">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUZyiWEOFpxeLlEYFx9rvVExa4oye1MBJlSbMXVhkueWKZKtN4eRWzQGFVeuNLmvgiklcgp86kOmwgt6gtVES_KhbW9XwxCaE633t8NQO_3IE_VMPTEfgXaxFlHNbcqTyIc6BKaLDHdYHBG0UPS7GuiLaXUwVQ6PaCpu7SyRTzjNl4nWEj0K5KX24XzM7278fauxdqb2crJoRXKUs4aKhgtZcdJB7qQ1agO7od5_FUaU5bTETRDasjJRqxVDL5p6cy3miO701ujA-dGPx3vpc-TlHX1uTSRZ-xyK0IltjKItqhHXlNx7BlpsD8Ho0Kq8-Nqydox8TDGEngf5hRiUxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست ۵۰ بازیکن برتر جام جهانی از نگاه مجله اتلتیک
پ.ن: گشتم نبود، نگردید نیست
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80411" target="_blank">📅 20:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80410">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اقا مثکه ویدیو قدیمیه ولی خبر اعتصابات واقعیه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/80410" target="_blank">📅 19:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80408">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e52b5708d.mp4?token=uOVjjCngWTBeadv2YysVb0h32zk5xi1v7dWY9KtRyuIneOnxb3qzy6iR9LtVMailc8afDhgjFYj0ulMkwBpVR70ldj9w9RstJ8gNy04UBHwkt6u97WxWkTXwbVj87QE91zUacg4KCwaeoM6yEHgk1ofwjNiuGQDWxxRX9ARm6n0dCEeeksgrCPXzx7_ZhsS0JGsPmmA03gEbmmR6udpI6RPAKyaZXM_JbXqfY3WBjkykPn2m9ovrJoKs5CAA4JKSH5xP1jeZRAzzBR6rXOxVL6XyqCY1Hn1_jGn2paw1ReklhqzDnFhFFdS7S6x3fwbta6MEDYtH7iqXsdU5B4iy3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e52b5708d.mp4?token=uOVjjCngWTBeadv2YysVb0h32zk5xi1v7dWY9KtRyuIneOnxb3qzy6iR9LtVMailc8afDhgjFYj0ulMkwBpVR70ldj9w9RstJ8gNy04UBHwkt6u97WxWkTXwbVj87QE91zUacg4KCwaeoM6yEHgk1ofwjNiuGQDWxxRX9ARm6n0dCEeeksgrCPXzx7_ZhsS0JGsPmmA03gEbmmR6udpI6RPAKyaZXM_JbXqfY3WBjkykPn2m9ovrJoKs5CAA4JKSH5xP1jeZRAzzBR6rXOxVL6XyqCY1Hn1_jGn2paw1ReklhqzDnFhFFdS7S6x3fwbta6MEDYtH7iqXsdU5B4iy3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتصابات در بازار چارسو و علاالدین تهران
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/80408" target="_blank">📅 19:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80407">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjuHYm-LLOC9xJ551YHjUblhvcQM6eFraSjZ3-mMvVLpHQxfwiDykNJhtAq9r2P9qzR83FTXROVB2nFJMZpEimf1AB41VaHSIxWx9BDLrHXUZYuUF-kITtO1UsnYumKqGBStgWoTX0hLG2Msr1rvoamcUBSlz_KtDDEijwKizvBmjURxTlOd_aP7-ZojWFAWDFcMOhQB8bADdLprE3q4oWJjJHoOusO_4TqXtEn-K2hzV6nOomHq9vYz3V50RgYf9KDpQzjOEKXGZNnJAQwa6MoF4STswbQvZGkoJVxV8q9CY5cSVu1MyS5aC6n1TkbX8DaXRX2q5EiuwJyrZNXP4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دقیقا بخدا
چطوری روتون میشه با زنتون سکس کنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/80407" target="_blank">📅 18:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80406">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/noIQh97jmkNbbSqxn8EuGH4_PpLyYuyalCVMKz6EEFiEtJJSpjqBEkVvJx6dKPxUqvLp26TiquNLSVFhJoO42LhaL4NkBTR9Sl92RkVnHcaRJ15j13RAZ4z2ZBilyHKdMHrLBkd7Li4-KCYnfiBO417h7iC4gIbXi71DDCrheGnuMuyN2Qws-47v3BrK29eDhuegCJFXPv_haWOJSvNZDegynS1l1cxQBn4Y_IvT-afBCzooCPrBjBXawBQUpbkIaNvK4DG6li1KmaFXws2VhJOGhI_5jpSWoFMXsNFIzPnH1vzcT0IVgF7KUBuyIT04rdJC_jfCGlSvkIg4PtUy0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
-
🇦🇷
آرژانتین
🏆
نیمه‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
چهارشنبه ساعت ۲۲:۳۰
📍
ورزشگاه آتلانتا (مرسدس-بنز)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
‌‏
⚽️
نکاتی در مورد بازی‌های رودررو:
در
۸
تقابل اخیر دو تیم، انگلیس موفق به کسب
۴
پیروزی شده، آرژانتین تنها
۱ بار
به برتری رسیده و
۳
بازی نیز با نتیجه تساوی به پایان رسیده است.
⚽️
حقایق داور:
🟨
میانگین کارت زرد:
۳.۸۴
کارت در هر بازی
🟥
میانگین کارت قرمز:
۰.۲۶
کارت در هر بازی
🧠
بودجه‌ی تفریح از بودجه ضروریات زندگی جداست.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g24
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/80406" target="_blank">📅 18:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80405">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1YwdfYXeVqkBhetVE8sVxV5zlojo9QYCNy3w7yd7wNy-0aeSLT6TBUX0pX4Vcs5rIsXCYTBdlG7wCxo59R2E9G1tJjH8YTynWkQgD5Ah2SdePto6LLbUQ5SbuusteWR367yAgQI91RJo-vNkiUwQrMej2XBm-Nnr0qpqVv5WF2LnkFwGX_GmsKLA_bu2CW7oyfmbvq2MPinDOowKAdzRgLqgfjQmVzDhm_qdtTy2EaTjMDsfut1JeZT4q9A2vg74DAee_s3LLS3owv6PIKrGRjEK2E15XcjmPlzS58EGh7YfCyk3VN5vNGuohOSmkVkHM6AGLDjfAWD-9tsrukThg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاخارا بخاطر پسر خوشگله ببندید رو انگلیس
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/80405" target="_blank">📅 18:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80404">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">به به به این خبر
عظیمی راد، نماینده مجلس:
به آقای کاظمی دقیقاً ۲۴ ساعت فرصت میدم تا امتحانات نهایی کل استان‌های کشور رو به تعویق بندازه وگرنه برخورد نظارتی شدیدی روش اعمال میکنم
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/80404" target="_blank">📅 17:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80403">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">کصکشا حداقل برق دکلای اینترنتو قطع نکنید</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/80403" target="_blank">📅 17:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80402">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/op6Eav6c0kt47ia-M-l78HoDh9RLZfemJOjUfN5HUO10DM2Eu6cs5nZMPWsFc9u5jG7u-Hv6C_ubwyL1rAWxOV67WP0kxv9T_9jyosZ1-7ZDvhCeDqiaT5KwfZI88WZmx_w9z1i2m9TNL33txKaycbtndq7JGfBSEJbsHHhPgf8YiosjBmY0jtDC5a3hG2YHW9SA8nx2QTRnw-8Y0I0fb4ba9JXhf1yDI03tcVRluDUSZJDOkCgDvOOdINoVzKIZJVfnNOFKygLQEodms6hxyQ063SiuqDui3gnDnAFNvuhWc4sfG4cYq4_PHtPHAO8QXMAo46T7_7qsEfnzjXurKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیک علی تجزیه رو از صدای امریکا زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/80402" target="_blank">📅 16:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80401">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtAdd-oCwpiyVNgmk1jEgbqo5_8ceVK-J3TAORo2--t74_BXCr6riSCrmbwyu3qpw0epXEEecu-jydl_u6fcaIHT4mFF9pDfXXORuG5jGL1ptfuMYyTV7BWpgSIDfTVrd2cd4wVqTaKL2VOV8uTsEWw7TJvDqw5_TO_cL6Ppm1_8X37DtbdASgc3sxMOttfScN0SnfNWJtNhNzyvR0B71pvOmHalZ1yvHxZvUxh9-ZWLxwmPf1DebOCOyumN4WIlpthk5GoAjNXoy6O3LdcZCKgSpdLFCtqKYP9g5YJvnfvwpgiA2nnHKWNOt7eKnfYOZ0wCjxMRjsTYi8pP0xu5EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این چی بود دیگه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/80401" target="_blank">📅 16:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80400">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترک جدید لنا و مهیاد به نام اشک ریلیز شد  Spotify  @FunHipHop | Mmd</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/80400" target="_blank">📅 16:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80399">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Npm4mcOdxfDxEbBmamCYnW7RbBle7W10s8vIPKX5MtkOET_Y4-_l44fEskR5EJHfD2Rbcg6kIBvZNKZ7NfHuhrsdOwZ-GZeLm3iWPTCyxZaakMbi4ShK5WpC3Uf0R3q6kJcOkRoZYpLr2Fi5emePrWVLufSdXOBBuy9JtHN5K2tyaAWtzWRAHFRAxgKLPSaLBE5H86ms2rM9TPUs4yFBDb0GMxGhzd69NdwWVLTh8ZggKf0j-n_xk05MxcGKBoCN0seXmZAYZcx3Nb6R3IuVXuM05kKnvj7PLZB-2_uyn6R9rBWDLCcvedhM3NdY1p-0eARI_pwBKuCWE0Ev8SsPNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید لنا و مهیاد به نام
اشک
ریلیز شد
Spotify
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/80399" target="_blank">📅 16:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80398">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">عجب ترکی دادن لنا و مهیاد</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/80398" target="_blank">📅 16:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80397">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pl2AeJ_2hV44jPVVGE9m9E_0ha1Dtiu1XW91h8sk9lrf0uFBdwLsKRzZHN0KK0FqS5o5SxJJuyn3NMcsRayMHrHSoOmVye7jjzuxl0vBkK_JVi4eEIhi1vNPBgjcHWaLUXquF1pEHOKx8Y0rQFYzR7-0gK_wn3X8V85Vjq2GWYr2h4Y6KN8_LmCmkoh2-EYZQwEouhK1LZbGjTPCrK-tjoemCcRg4PjIzXxNIg7tu8T-1XqNI-OFCkJZChj-__5Gy96kNUIyMx1pqgRFv28zzP4J7IuxLSjBUWZVNpnoyVOnNFmibyslkrJA9aPE560DihAywdQU6JAUiL8B7ZVtsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به پیر به پیغمبر من خشخاش نکاشتم، دست از سرم بردارید  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/80397" target="_blank">📅 14:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80395">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">جدی مملکت هیچوقت اینقد رو هوا نبوده
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/80395" target="_blank">📅 14:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80394">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">امتحانات نهایی سال دوازدهم در ۴ استان هرمزگان، خوزستان، بوشهر و سیستان و بلوچستان لغو شد  @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/80394" target="_blank">📅 14:19 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

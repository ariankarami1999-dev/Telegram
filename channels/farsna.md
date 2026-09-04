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
<img src="https://cdn4.telesco.pe/file/uh8VAOUqO5UZccEO-9qIfZHYBoTPfMYHN9NcoKX-gFSrGEYth1etg3a9Nldcg90u9Br0I3Suq_SCFeSONIgt7P6_QaVdP0JBKvN_iqjHRaA2Z6Wmo7tBlLAFWzn1F78cifs7UHCD_A74viOZeXKZZIuBxgbulqEhqlW_qpzUgJse9gyfckVmdMRpVSiZ8-7ubVhznpN0apkU7MNX483kRXnV2hbJzTd2sK-6637IA5GOn6wbpCCbGsV47ZzcZ6cZseONfOStlfTabdBdYG-k2J55qM7jw9L9tGtRZhHyKdLKL-ejCdLE-_UHHttJGySuaoE0FbDmHIy8Mp4GO6o_rQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.78M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 23:13:55</div>
<hr>

<div class="tg-post" id="msg-460169">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89f799ea13.mp4?token=PtD-1Ieit6pShFV5FqbrZi-ys2D3ZSF45S2c1Fq0G8kuzxUPGIMC6IuOS8LKMOO10L7TAyp_cfEzOprxD0jC6RZneDqiKY0oOE82Uto5zNcSpfYNAnpH-Vhfl_-BYK078QN6SX40Wlhl9xaovEFiUA2rQFl-x1_LnxiCn2RfoEeYV52xD9cQFeSwLd2_wH2t9_SPU18dJ-azUknrMVioOkyxjdX8Cw3J6hBgFj_4z7tAfj_YHP99tcMk-hxu-rxgABxDIRLp2l1AhcBEgx8fdTzvGizIvma5wjoNqX1RJz86MtI2_wIGc5Vq1X-0iVKFdhE-6sAXR-hDY5s6BeK4cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89f799ea13.mp4?token=PtD-1Ieit6pShFV5FqbrZi-ys2D3ZSF45S2c1Fq0G8kuzxUPGIMC6IuOS8LKMOO10L7TAyp_cfEzOprxD0jC6RZneDqiKY0oOE82Uto5zNcSpfYNAnpH-Vhfl_-BYK078QN6SX40Wlhl9xaovEFiUA2rQFl-x1_LnxiCn2RfoEeYV52xD9cQFeSwLd2_wH2t9_SPU18dJ-azUknrMVioOkyxjdX8Cw3J6hBgFj_4z7tAfj_YHP99tcMk-hxu-rxgABxDIRLp2l1AhcBEgx8fdTzvGizIvma5wjoNqX1RJz86MtI2_wIGc5Vq1X-0iVKFdhE-6sAXR-hDY5s6BeK4cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میدان‌داری مردم محلات استان مرکزی به ایستگاه ۱۸۸ رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 325 · <a href="https://t.me/farsna/460169" target="_blank">📅 23:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460168">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f61d130790.mp4?token=cHHrEG5XQ-z2qz9lWgdGWeU_muhNf50IdVbBeD4pZfXGl_zwinXbz95AT8Y88J9wUAqaxEo9Qivey1Tr9wqZO2Kd7aGmGR5HItpsbcjVYg7CAdhto9pN6aMraej0pZtp0Zcp0aaB0Lf9Xo_O-peDHEbpMIH0uABiOcQEq9XGw_leAEANn5hep9ZFmb0yqAcl2F2hP4JU8jJmDvMiDw4ocEHstrO6SgGhOCah-J4OXp9xaGRmOtxgiKIIHNiQ4DLMlB-HdTGUS1HlLe84KmgDQ76OgBkvybFOws6jHvtbahOfJ5dU8Boml1OYyt3e3_jX0cStQ71bx3TiMvzZswNdJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f61d130790.mp4?token=cHHrEG5XQ-z2qz9lWgdGWeU_muhNf50IdVbBeD4pZfXGl_zwinXbz95AT8Y88J9wUAqaxEo9Qivey1Tr9wqZO2Kd7aGmGR5HItpsbcjVYg7CAdhto9pN6aMraej0pZtp0Zcp0aaB0Lf9Xo_O-peDHEbpMIH0uABiOcQEq9XGw_leAEANn5hep9ZFmb0yqAcl2F2hP4JU8jJmDvMiDw4ocEHstrO6SgGhOCah-J4OXp9xaGRmOtxgiKIIHNiQ4DLMlB-HdTGUS1HlLe84KmgDQ76OgBkvybFOws6jHvtbahOfJ5dU8Boml1OYyt3e3_jX0cStQ71bx3TiMvzZswNdJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار بروجردی‌ها در شب ۱۸۸: لبیک یا خامنه‌ای لبیک یا حسین است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/farsna/460168" target="_blank">📅 23:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460167">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISnLhHUqSbRPdQZ-LsI3_PytYgMCG0mh9mwBCUrifNUsIltXx08GomGOrd3JJrSXzZMak5ihDmz0cEbrMkZ13o1ebgzu5BmO5BXoImkZ89RDORT-D4RaqJ35jwhM1IcUuYQC0qmARJPQWcoMLKpH1--aRwGxAf5W02sPJINd231AgPAnvd6oIcG7URLjRmnUg00O_jYZ34wuaMjSoAzIuYCAXX4Qm_YbW_z_ve2_94YWLJVqqkrSAs9_lXQ3AgwuFzHIHMecyvzr_kMemuVJK7fxWmx1_5T1my7kF-a8WEedCQ6M53NgJ_FGlC8RGvtkClXsysrIX57mFkvgjRQW2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکتیک جدید ایرانی که دشمن را آچمز می‌کند
🔹
در حالی که طی درگیری اخیر ایران برتری خود را در میدان ثابت کرده است حالا سخنگوی ارتش از تاکتیک جدید ایرانی سخن می‌گوید که استفاده از آن می‌تواند دشمن را به عقب نشینی وادار کند.
🔹
امیر سرتیپ محمد اکرمی‌نیا، امروز می‌گوید که دکترین نظامی ما پس از جنگ تحمیلی ۱۲ روزه به‌تدریج به این سمت حرکت کرده است که «باید از جنگ پیش‌دستانه استفاده کنیم»؛ ‌البته حقوق بین‌الملل نیز به ما اجازه می‌دهد که بتوانیم به‌صورت پیش‌دستانه از خود دفاع کنیم.
🔹
یکی از آخرین مواردی که نیروهای مسلح ایران عملیات پیش دستانه را علیه دشمن اجرا کرده‌اند، بامداد ۷ مرداد بود که نیروی هوافضای سپاه، یک پایگاه هوایی و مرکز فرماندهی ارتش آمریکا در اردن را پیش از آغاز عملیات آمریکا علیه ایران با موشک‌های بالستیک هدف قرار داد و مانع از اجرای عملیات دشمن شد.
🔹
سخنگوی ارتش درباره اجرای عملیات پیش‌دستانه علیه دشمن نیز گفت که ما «اجازه نمی‌دهیم آمریکایی‌ها ابتکار عمل را در اختیار داشته باشند و در چند مورد نیز همین‌گونه عمل کردیم.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/farsna/460167" target="_blank">📅 22:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460166">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad5d7220c4.mp4?token=N3j4fSUgQiLRlz-GVvPyxHSnNfWiQraKODXAz3AEhvt82tweieZpp1k2R4KOwDJb8jeNUazg2YuDMo3CVthpzoyqxhSE6nLhXyCBbrbXkVmaz9J7kJdNvH0dFSffsCnZ8hFwi6Ky6BfDw-X3STTW9gJzkq4jkLjcjymsuygkCx-xthwR57wK6eIBz-CAq5rxZuEe0_UG-M6Z1noAxGZrO6YNwTRic1gbLhAXQRSqu0Ugvrp7VH2qEoDrpIVGIcrgZN93Fnj5ow9GkZKSV3omMiSor4Bs0Ms-wO25fh167KX3S7-bjVSGlnf4xLRs-h28tyOOAs09rGb-lTYRodK77A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad5d7220c4.mp4?token=N3j4fSUgQiLRlz-GVvPyxHSnNfWiQraKODXAz3AEhvt82tweieZpp1k2R4KOwDJb8jeNUazg2YuDMo3CVthpzoyqxhSE6nLhXyCBbrbXkVmaz9J7kJdNvH0dFSffsCnZ8hFwi6Ky6BfDw-X3STTW9gJzkq4jkLjcjymsuygkCx-xthwR57wK6eIBz-CAq5rxZuEe0_UG-M6Z1noAxGZrO6YNwTRic1gbLhAXQRSqu0Ugvrp7VH2qEoDrpIVGIcrgZN93Fnj5ow9GkZKSV3omMiSor4Bs0Ms-wO25fh167KX3S7-bjVSGlnf4xLRs-h28tyOOAs09rGb-lTYRodK77A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادعای ترامپ: خطوط لوله در سراسر خاورمیانه درحال احداث است تا دیگر نیازی به عبور از تنگهٔ هرمز نباشد.
🔸
ترامپ تا پیش از این مدعی بود کنترل تنگهٔ هرمز در اختیار آمریکاست. @Farsna</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/farsna/460166" target="_blank">📅 22:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460165">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/266a94e115.mp4?token=uNyi1X4g5c1gCsXev_5LJ6YoMNIw1egae9Dbs7rcbwUtjOZigCvCgmH0UysTI_ZSbSyC1fU8sC1rorRlsz6tUWeYwa3_7P3fSyCoX8odsgyHarhYZOIPf8ESo-N_w2hlBpdbSwD3O2yhmeARXiBmM3VXxYBJ3RY06VK3FLw_LRfkNjhvwLtaZ_41E4joRN6kwYYQsxZKTmJRvanyeZNNN1zFhUJITB0s2eFzoSaQfczPAKmaMQspFUoka6Ed3P3cYh14cd0xO1SdH8JhYd2mKty6GjY9FheeMMHtwob3fFdgcMpM-Ci7jJsFc_jpXSBtrjDeGdYgTJGK3Zc7QPt1zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/266a94e115.mp4?token=uNyi1X4g5c1gCsXev_5LJ6YoMNIw1egae9Dbs7rcbwUtjOZigCvCgmH0UysTI_ZSbSyC1fU8sC1rorRlsz6tUWeYwa3_7P3fSyCoX8odsgyHarhYZOIPf8ESo-N_w2hlBpdbSwD3O2yhmeARXiBmM3VXxYBJ3RY06VK3FLw_LRfkNjhvwLtaZ_41E4joRN6kwYYQsxZKTmJRvanyeZNNN1zFhUJITB0s2eFzoSaQfczPAKmaMQspFUoka6Ed3P3cYh14cd0xO1SdH8JhYd2mKty6GjY9FheeMMHtwob3fFdgcMpM-Ci7jJsFc_jpXSBtrjDeGdYgTJGK3Zc7QPt1zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توهم جدید ترامپ: ما کنترل ایران را به‌دست گرفته‌ایم!
🔹
رئیس‌جمهور آمریکا: ما کنترل ونزوئلا را به دست گرفتیم و در واقع کنترل ایران را هم به دست گرفته‌ایم. اکنون چند روز است که هیچ شلیک و درگیری رخ نداده است.
🔹
تنگهٔ هرمز اکنون پذیرای کشتی‌های زیادی است؛ کشتی‌های…</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/farsna/460165" target="_blank">📅 22:48 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460164">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93c06f4c83.mp4?token=j4KzYCY8hb8Rdb7_oUk9K3Wz58yL32wv-8riKAP2gW1L0Xu1wHgOWFGRNCcSN6J0vH-jWZfnLaSN-ha53OS7O1xyB23GmFexEfvwSFmeI4BB8oo_Lg7O1Na0prqwaEf7wgoZy7QLdWdxql-ZAPQUrcvKR2Jm-dZlkChuc27h-tMth_WKV_TQU05IZHSARMwJfiDKVFkHMFmepZc4_UmQT16aHU_jDAyvgnIKHFO9rLfOvHbvwhK4CAFBduZ4T1eErV6QC_tQrfSMEFKPyaGIsWKBsFIPtiq-2yzBq2bxGLct7kOqQ3R8jINcPdAmMu9hrH8GkpqB34wZ7Q8wE2stqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93c06f4c83.mp4?token=j4KzYCY8hb8Rdb7_oUk9K3Wz58yL32wv-8riKAP2gW1L0Xu1wHgOWFGRNCcSN6J0vH-jWZfnLaSN-ha53OS7O1xyB23GmFexEfvwSFmeI4BB8oo_Lg7O1Na0prqwaEf7wgoZy7QLdWdxql-ZAPQUrcvKR2Jm-dZlkChuc27h-tMth_WKV_TQU05IZHSARMwJfiDKVFkHMFmepZc4_UmQT16aHU_jDAyvgnIKHFO9rLfOvHbvwhK4CAFBduZ4T1eErV6QC_tQrfSMEFKPyaGIsWKBsFIPtiq-2yzBq2bxGLct7kOqQ3R8jINcPdAmMu9hrH8GkpqB34wZ7Q8wE2stqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگار: اگر درگیری با ایران نامش جنگ نیست، پس دقیقا چیست؟
🔸
ترامپ: خیلی‌ها به آن جنگ نمی‌گویند. من به آن می‌گویم یک «درگیری نظامی»؛ چون برای ما موضوع کوچکی است! ما در مقابل ایران فقط ۱۸ کشته داشته‌ایم. @Farsna</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/farsna/460164" target="_blank">📅 22:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460163">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b2e1fb1a6.mp4?token=Dqqd_bpwUHtXBKDEZX5mKYu1txSYAq6M7wpEMq-akPgHfUrjeweWk1ipEV_m49lsCP7DzdkyuBRXbZiS27MRyyuQeHjgun7LbAkJB8lTKb4c7gVVrKIByeYDGYW3MmD59E__SX2RV5HupH8Y0Tsgn2090Ky9JRmeXfIZh5s8Jl-eJWZZ0dmfWZbkFHG53R70AWfytsERAobcHFYFmwSxT5yJCB7UtQzRKFkpbmUmR8s4_m6cfPy1tKzDkL2J5IYkJSxzA9rQtd2Pox4ODcFQXwl43LeENHuG3TC8ZEr4zJqeLPiqin8PhMRCGk7zmsT9ozKiRqkeHWFTH3u-cNHSeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b2e1fb1a6.mp4?token=Dqqd_bpwUHtXBKDEZX5mKYu1txSYAq6M7wpEMq-akPgHfUrjeweWk1ipEV_m49lsCP7DzdkyuBRXbZiS27MRyyuQeHjgun7LbAkJB8lTKb4c7gVVrKIByeYDGYW3MmD59E__SX2RV5HupH8Y0Tsgn2090Ky9JRmeXfIZh5s8Jl-eJWZZ0dmfWZbkFHG53R70AWfytsERAobcHFYFmwSxT5yJCB7UtQzRKFkpbmUmR8s4_m6cfPy1tKzDkL2J5IYkJSxzA9rQtd2Pox4ODcFQXwl43LeENHuG3TC8ZEr4zJqeLPiqin8PhMRCGk7zmsT9ozKiRqkeHWFTH3u-cNHSeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شاید آمریکا قصه‌های زیادی برای دنیا ببافد اما پایان این قصه را ایرانی‌ها تعیین می‌کنند
@Farsna</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/farsna/460163" target="_blank">📅 22:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460162">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4wvB7C9Wj0IddgJNxF1Y0JvGSTshYlpua7uRhEbn0IOQSkcRlGcAVLVHlqHlE1oVrkIP3jRGyweYlcL23q5ViBnxVpHmXn1xhZ58IZpecbXLgWMv8kKFnQDCeuzLPdYWr8PB5eNU6_ToE0EYR4k-F8yGqld3DnV2wGacrO3XYIWlu5kvl3dtupmUHlYQIO6JsdcR8gALEE6n0dI8CQ7hiA9X1gIRZ-KugezLrQDRTNyB0y0Dlg7575XMKDxM9R1bREcjGhIX14Eg0462Dpta2SUftdegXEPnTS_Bwxv0l4MioC-EOXnmTA8zQL5LWZc1PVnthctcdB8-LBRqUlG_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴ سال جنجال برای پتروشیمی میانکاله؛ روایت تازۀ پزشکیان
🔹
پزشکیان روز گذشته در جمع فعالان محیط زیست درباره پروژه پتروشیمی میانکاله گفت دولت برای توقف این پروژه تحت فشار بود و برخی می‌گفتند خود دولت مجوز اجرای آن را داده است.
🔹
پزشکیان تأکید کرد وقتی پروژه‌ای به طبیعت ضرر می‌رساند، پول آن را پرداخت می‌کنیم، اما حاضر نیستیم ادامه پیدا کند.
🔹
ماجرای پتروشیمی میانکاله از اسفند ۱۴۰۰ آغاز شد؛ زمانی که سرمایه‌گذار بر اجرای پروژه اصرار داشت، در حالی که سلاجقه، رئیس وقت سازمان حفاظت محیط زیست در آن زمان گفته بود که احداث کارخانه پتروشیمی در بهشهر بدون مجوز زیست‌محیطی امکان‌پذیر نیست.
🔹
در نهایت، سال گذشته رئیس سازمان حفاظت محیط زیست، از تصمیم دولت برای توقف پروژه خبر داد و در صفحه شخصی خود در شبکه ایکس نوشت که پزشکیان در جلسه هیئت دولت دستور توقف فعالیت پتروشیمی میانکاله را صادر کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/farsna/460162" target="_blank">📅 22:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460161">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8cc7bfb46.mp4?token=k7age0-dQqM3eNFmfJ_DDC7uYXfHZm_XeEJlPZS3EzznONZnb1isremcc0yYGJ8qwbR966knmpR8ewWymbHku7R3fe4K_rm8uRoA4_dnCqGhRkMZtghYoJzq-BDIhF-juyGeuBftGt_vaIRpNmpxD0kDBVlT9RuywHS3Hz2BKGP7rTYR2FSNhpltzaOL5FfCkpB-xqrECvsSbuI7FtbBPeDeE6GanbKuUoL3sX49uE6OsiFjjVbRuSR38ubV-65wG4FNb_jpaek0XJyfIBCuFMEFXS6OMx926E-qyBnSH1Rsgfm320dm37RYUvPWofjg-XnwqcSixfLJszsm49qIbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8cc7bfb46.mp4?token=k7age0-dQqM3eNFmfJ_DDC7uYXfHZm_XeEJlPZS3EzznONZnb1isremcc0yYGJ8qwbR966knmpR8ewWymbHku7R3fe4K_rm8uRoA4_dnCqGhRkMZtghYoJzq-BDIhF-juyGeuBftGt_vaIRpNmpxD0kDBVlT9RuywHS3Hz2BKGP7rTYR2FSNhpltzaOL5FfCkpB-xqrECvsSbuI7FtbBPeDeE6GanbKuUoL3sX49uE6OsiFjjVbRuSR38ubV-65wG4FNb_jpaek0XJyfIBCuFMEFXS6OMx926E-qyBnSH1Rsgfm320dm37RYUvPWofjg-XnwqcSixfLJszsm49qIbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگار: اگر درگیری با ایران نامش جنگ نیست، پس دقیقا چیست؟
🔸
ترامپ: خیلی‌ها به آن جنگ نمی‌گویند. من به آن می‌گویم یک «درگیری نظامی»؛ چون برای ما موضوع کوچکی است! ما در مقابل ایران فقط ۱۸ کشته داشته‌ایم.
@Farsna</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/farsna/460161" target="_blank">📅 22:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460160">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db96ccdf81.mp4?token=amclsvf-TfTuWTKCvYacB_6J9nip0KYDsf4XX-kn-slEXK_Cv_wTlfrS8eTMjDdGtoH57VL2WYUEmUsjLvIDpLwx1ba5tXnjyLNHlqfcCxbiRhUoHcZU5otJwAGRHS0V_2WybofE4tiJ5aDMeJfg-DdDMpNAkjHPWjOubyyhMMcUHwCW56TlFf4MkAfKPrKpTqXry3GzQACLVLW2L85KfCqdoyUDvqnIbPfOCoEWraeD_C0rvJ9JUu_RpEEecKXKtfYTNdauiCdcdm54va6rtWegKcAhaInQJ2XtQlNXgbeKoQqpg0zAYztHBD0uvH5vCMa4QXqRGO0LU6TykPT2Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db96ccdf81.mp4?token=amclsvf-TfTuWTKCvYacB_6J9nip0KYDsf4XX-kn-slEXK_Cv_wTlfrS8eTMjDdGtoH57VL2WYUEmUsjLvIDpLwx1ba5tXnjyLNHlqfcCxbiRhUoHcZU5otJwAGRHS0V_2WybofE4tiJ5aDMeJfg-DdDMpNAkjHPWjOubyyhMMcUHwCW56TlFf4MkAfKPrKpTqXry3GzQACLVLW2L85KfCqdoyUDvqnIbPfOCoEWraeD_C0rvJ9JUu_RpEEecKXKtfYTNdauiCdcdm54va6rtWegKcAhaInQJ2XtQlNXgbeKoQqpg0zAYztHBD0uvH5vCMa4QXqRGO0LU6TykPT2Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم‌های برافراشتۀ ایران اسلامی در شب ۱۸۸ تجمع مردم مراغه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/farsna/460160" target="_blank">📅 22:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460159">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d4d254ab6.mp4?token=d6RsIiLWlkgvL3GVuppx3SzOOUfBkcrOEydimc4YezNsqXdb6_zqQXUBy2ZKOCUW8zsskfCH-IJHkZLi9dbOCOTsMzmCfpoNWAcsaSPrDvT9ClBZmbZ1NrU-AF_9PHmKLEAx1pLaDZfC6vBab61mYr5_I9lAsu4gDh3Xij82eQRRQ3uuFYq70eP6mkPkmK-n3cDR-9gtbXg2B2TcRsv4dPEp1EcR_oQFIzhcYOdv3iTpOiiAQmY5F6Pxz2Syzy784q4imn1in_Pm5RGkFKVko8IjlKF-wqgKOebH4ga6_xxJWYjGe0zCMFWea-fOQIOo8fXosgkzE40Vm76iC13FUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d4d254ab6.mp4?token=d6RsIiLWlkgvL3GVuppx3SzOOUfBkcrOEydimc4YezNsqXdb6_zqQXUBy2ZKOCUW8zsskfCH-IJHkZLi9dbOCOTsMzmCfpoNWAcsaSPrDvT9ClBZmbZ1NrU-AF_9PHmKLEAx1pLaDZfC6vBab61mYr5_I9lAsu4gDh3Xij82eQRRQ3uuFYq70eP6mkPkmK-n3cDR-9gtbXg2B2TcRsv4dPEp1EcR_oQFIzhcYOdv3iTpOiiAQmY5F6Pxz2Syzy784q4imn1in_Pm5RGkFKVko8IjlKF-wqgKOebH4ga6_xxJWYjGe0zCMFWea-fOQIOo8fXosgkzE40Vm76iC13FUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم: تنها تفاهم ما با آمریکا این است که «هیچ تفاهم‌نامه‌ای وجود ندارد»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/farsna/460159" target="_blank">📅 22:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460158">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
خواهشمندم موضوع
عدم واریز مبالغ سبد کالا
به فروشگاه‌ها را پیگیری کنید.
🔹
از شهرستان شوط آذربایجان غربی پیام می‌دم. برای
بیمۀ اجباری تأمین اجتماعی
، در ماه‌های فروردین و اردیبهشت هر کدام مبلغ ۸ میلیون و ۵۰۰ هزار تومان واریز کردیم، اما برای خردادماه مبلغ ۱۱ میلیون و ۷۵۰ هزار تومان پرداخت کردیم. اگر ممکن است
علت این افزایش مبلغ
پیگیری شود. ضمن اینکه از پانزدهم مردادماه چندین بار به شعبه ماکو پیام داده‌ایم، اما متأسفانه پاسخی دریافت نکرده‌ایم.
🔹
یک
فرد دارای معلولیت
که تنها منبع درآمدش
مستمری ماهانه
۲ میلیون و ۱۰۰ هزار تومان است، چگونه باید با این مبلغ یک ماه زندگی خود را بگذراند؟ فرد دارای معلولیت نیازمند زندگی با عزت، استقلال و تأمین نیازهای اولیه است، نه مستمری‌ای که حتی پاسخگوی ابتدایی‌ترین هزینه‌های یک ماه زندگی نیست. لطفاً صدای و زبان معلولان باشید.
🔹
جمعه‌بازار خیابان بهشتی
محل خوبی برای خرید و فروش است، اما متأسفانه برخی فروشندگان به‌جای بساط‌کردن در محدوده مشخص‌شده، بساط خود را جلوتر پهن می‌کنند و مسیر عبور مردم را تنگ کرده و باعث کندی رفت‌وآمد و ازدحام می‌شوند. چندین بار این موضوع را به
مدیر بازار
تذکر داده‌ایم، اما متأسفانه تاکنون اقدامی نشده است. لطفاً مسئولان رسیدگی کنند.
🔹
لطفاً در مورد
برداشتن تعرفه تأمین اجتماعی برای داروهای شیمی‌درمانی
و همچنین قطع سهمیه این داروها هم اطلاع‌رسانی و پیگیری کنید. چرا باید سهمیه داروهای بیماران شیمی‌درمانی بی‌سروصدا قطع شود؟
🔹
بنده از طریق اداره‌مان، در تاریخ ۱۵ دی‌ماه سال گذشته از شرکت
کرمان موتور خودرو
ثبت‌نام کردم و برای تأمین مبلغ آن، طلا فروختم و وام گرفتم. طبق قرارداد قرار بود خودرو در تاریخ ۱۵ اردیبهشت‌ماه سال جاری تحویل داده شود، اما پس از گذشت ۶ ماه همچنان در بلاتکلیفی هستیم و پاسخ‌گویی مناسبی نیز از سوی شرکت صورت نگرفته است. این
تأخیر و عدم پاسخ‌گویی
باعث وارد شدن خسارت به مشتریان شده است.
🔹
حدود ۱۰ ماه است که
بانک آینده
با بانک ملی ادغام شده و ما برای
تسویۀ تسهیلاتی
که قبلاً از بانک آینده دریافت کرده‌ایم، با مشکل مواجه شده‌ایم. هرجا مراجعه می‌کنیم پاسخ مشخصی نمی‌دهند و حتی بانک ملی می‌گوید پرونده شما «مشکوک‌الوصول» است و برای تسویه باید به تهران مراجعه کنید. ما فقط می‌خواهیم تسهیلات قبلی خود را تسویه کنیم، اما چرا باید برای انجام این کار از شهر خودمان به تهران برویم؟ خیلی از مردم با این مشکل مواجه هستند و توان و شرایط رفت‌وآمد به تهران را ندارند. خواهشمندیم مسئولان این موضوع را بررسی و راهکاری برای حل مشکل مردم در شهرستان‌ها ارائه کنند.
🔹
تو را به خدا به داد مردم محله
کنارگرد حسن‌آباد فشافویه
برسید. حدود ۵ ماه است تلفن‌های منازل مرتب قطع و وصل می‌شود؛ ابتدا در طول هفته فقط دو روز وصل بود و دو روز قطع، اما حالا سه هفته است به‌طور کامل قطع شده است. مخابرات منطقه فقط می‌گوید «قطعی نداریم، به تهران گفته‌ایم و خودشان می‌دانند». بارها با ۱۹۵ تماس گرفته‌ایم، اما نتیجه‌ای نگرفته‌ایم. از طرفی برق هم تقریباً هر شب از ساعت ۲۱ تا ۲۳ قطع می‌شود. و متأسفانه
ادارات برق و مخابرات منطقه
پاسخ‌گوی مردم نیستند. لطفاً صدای مردم مظلوم کنارگرد، در ۳۰ کیلومتری تهران باشید و این مشکل را پیگیری کنید.
🔹
از
محلۀ افسریۀ تهران
پیام می‌دهم. این محله با جمعیتی حدود ۱۲۰ هزار نفر هم با
قطعی برق
خارج از برنامه مواجه است و هم تلفن همراه اول دچار اختلال شده است.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/460158" target="_blank">📅 22:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460157">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">کارشکنی کانادا گریبان بسکتبال با ویلچر ایران را گرفت
🔹
پانزدهمین دوره رقابت‌های بسکتبال با ویلچر قهرمانی جهان از چهارشنبه ۱۸ شهریور در کانادا آغاز می‌شود و تیم ملی ایران در گروه چهارم با مراکش، آلمان و کانادا هم‌گروه است.
🔹
ملی‌پوشان ایران که پیش‌ازاین برای پیگیری امور ویزا راهی ترکیه شده بودند، قرار بود امروز از طریق استانبول راهی کانادا شوند، اما این سفر هنوز انجام نشده است.
🔹
ویزای تمام بازیکنان صادر شده، اما هنوز روادید بهروز سلطانی، سرمربی تیم ملی و محمدرضا دستیار، مربی تیم صادر نشده است.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/farsna/460157" target="_blank">📅 21:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460150">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lTm6EnJgQ4MXQ6Of4aShXdbMx7LsZOdQZWFvA0QjdvSjOujFrBBpYbFpz60Od74frccnNZn912RoZPzDu1YF_nY-s40rnN2gx9_hFxDSITtf8gMQVJYJcAqJBGVQRfcFhqH-zwaj6qN9xLSznefvGQSMWQwThY2Rbvot4H9xHaqA1r2ODEtd_kctDq1I3P7o3VkBnRglfX8rvid-2lOamV4zBl_lwLA0PH6iJTNNZdCbPsnPWTZ65rrBj75Tkd_LxnOefWOJE3cY0_JxwRqr6AStE3p6aRmui2Q4mrR-7FT0HLZRkzB_iouyBLbzXHcZOM-tiwHADyBHf1e5Lh_4GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ThQUY6phNeodpixLdHgmCVrbRhqCVh1tdD8reGn15pXYQQSAUthPaZ1tRFfn04ACVkRLhXO2NKh0dn9E0VkmY2BZwD2dUII8aNGw5xf92BhVSC-EQTWvkZxyHppGmWKUmiG8-liRokm8u9UcCYr3dmSGxQ_eXIUcQ0RRZKoQl6sI69UE5ZEqZEwublSZIJgmi9iQfuGMt2Uvt8ysa18-YCoCX_k-9vGXVCZCVcqzjSByJ2uzo5El0tPwS_xDAntDep12Ck9tFLzX0O9fr2IL_kuDnGZE3OJpdRY0uaQar01Z9LMj-DsFuN8H-Jdx5ZKGoF_ymOYevLIEnYX7FchFIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X9ezQMoEkz3RbrsNWWP675PeootQdvNJujefgDhb_EUDg7nFk6ibz4oA7cSiKGRKlgNPjUvLtizcAJLZylmN6sm5SghjEKBN85J8J-5jk290O6w4VvtXsoTjqGgksDAJ9T4XeOTooqU70maeqTD-Zue1eKsU0a-7vc8vcJT-T8jhs_cMVwhG10-NqrPsyV0E-neUHulNjHgaykR8MH62wfg6QsH8hmOeOOfXshfgP1mw9S1N7FDcz8MVjYAAIbTkZShyFfw-_QSUyDZp4S2TjB0YbhEq77EAcLCm3JHOyBDwIK6xkIsCDiHbOUNM4xJm2jAfuvrNABhnqQfSSWFCmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PU516aZXV8qz8XbRnY62e9mT0G2P1yHE7HjaMpz7n8nVkpJ47RON8Da4kFYkZwnEK1wCcH4nUKpxjj00HUuR5XwiNYMx7kgTFV4HAjYaWyh1_Av8A24AskV4b_rpywhd-qZ_aucNzeaDyvUmvVHit1MxnHgLIpaOvzJzDKFbbWhrrQl8BOMilPzv4ox1gp2ns9JC5wK5zHTZwNvtxXktvmtNhthcfPDrpvI4u-TFMiDfZqHIFtOHCWv6WlFDV8m1A_6vxRLKpv8yjszXKir7nWrLgc6FvE_fOQoD7z_j4x39HuA3nsHPpKpvMUFC0x3eXeaZm_sQ8JGhf1zf0_ngGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XDk6nb7ppZE3QL9ewgZumYAr-qkardhsnF5ROZ07vLi0h4L76FXnQvBBK0zpLJjc2oWEBs6tHmtULOOvRHi10kPaD9h-mo6BOEyefDlQj7VlUJ-z3Dqxybzn9Eyin5cU6Lq59hVGOnm4O5ipoJogCXmdDFDlm49wYdhAQReW76hUHek9R1mvCLeWynvlAUc-L6LPOBdwuJ7PgmMSeYicGg-NRIBSOpFL-enco6IsXEK7noXWwRJeq2tv4TZeivATGu2SBWVt9mGaKySBr_l9IGhE7OywmrIICyzYr3i4yais-P1MXloTTYvsZh6ktBkjsr2rSetlCsQUN-1pAnu4Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BDhbSFmDiKDfeC2MswzL4nvFIjp1vIfeEpwpMI-hO0bbct2SrPqRQxknS3s2jXlGPy083XoWneqEaEB3lU5nnt5ARp1pWLGUz49OZuoUTXnTF4JR6_MraVPjHnkSI3VgB59TN7_NKFZsoOfPwhoIJezX7msG8dzqUnrXk51FgRhq4zTOdReJHDxl5vWaMtNuMggF5ofSxpWY86nKGkI-A6-Bx2glPgvvUFsPOFzcR3DXtoV9ztnCN9-rUmNnwP3UUqRKGW_Mb2xVJ7DXbIZuYRlhuAgkrtzqYLo02Ez5AS1QArXRClKBvxkaqdptyWOPihroNqPhz43ilWeYTn6koA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nW4JYiErlV-rmY-DHg2tekvEHldrIez5cj6URFIzTvwsTIicZBmxGrMBoLoLyscPUcS5ptIqrFJQRLOdyNq4vvZ-trMZ4BrWTzO65LzBjpsISV4ueEggN6PpZ6j7BRcGqDCsYLxRRsN78pHyl7_eRt2Ibqk7dZegQ-VKFiRzlBZ4OUFThquuXrGunmX8_YNA_F-PJfXSYZNIWWMjIn8mZmhrrzJchQEfILxOhbH5svlslaWwFL-RKK4DqARtrPKf6vDLc77yholb1IcjYZrNknMqA81RPIRhMqHnPCBnaeVIrYlhPoVzCXTOVenbuyrmgvUQ82leBbNKwu08f2eSmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پرواز ابدی خلبان شهید مجتبی حسینوند
عکس:
علی صاحب‌محمدی‌نژاد
@Farsna</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/460150" target="_blank">📅 21:54 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460149">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28e0e7346e.mp4?token=e-zz40w_R_j9ybN4RoIh3CgOhgz7p_vFLaiDUZPCZ-Xvwl7oHTi2v2vkrFGCoFFzguf_W6p32P3OPpIFW5tcmOxcz_QFMEfosIVIgENjUAPvxT_usNntCAsCsD-xwZVulSBir4i4olCaK8MJO4X4uxSFvW9veRUvDWCNO5Iy73ulO7UebG7xNfXue3u8G5wzxtIe3_WmGGl6jrr_tE4GJGQ7BrpEayahUZTjgvGCk4w0xXw0gZCBOTJ8chsa50oIXDF6cyEtJ1VRlFY3R6DBhr6LsxzGH_QSAZexSjz6MhdZvlMEI4kySqM66i5zGltbEkDMRTBm8o2S5ejOCktaTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28e0e7346e.mp4?token=e-zz40w_R_j9ybN4RoIh3CgOhgz7p_vFLaiDUZPCZ-Xvwl7oHTi2v2vkrFGCoFFzguf_W6p32P3OPpIFW5tcmOxcz_QFMEfosIVIgENjUAPvxT_usNntCAsCsD-xwZVulSBir4i4olCaK8MJO4X4uxSFvW9veRUvDWCNO5Iy73ulO7UebG7xNfXue3u8G5wzxtIe3_WmGGl6jrr_tE4GJGQ7BrpEayahUZTjgvGCk4w0xXw0gZCBOTJ8chsa50oIXDF6cyEtJ1VRlFY3R6DBhr6LsxzGH_QSAZexSjz6MhdZvlMEI4kySqM66i5zGltbEkDMRTBm8o2S5ejOCktaTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع شبانۀ مردم میدان در پارک ساحلی بندرعباس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farsna/460149" target="_blank">📅 21:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460148">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2zzEnko5UMPHzc9olqNUOvbvVHR2ZW0K-_nxBX2QMRgI-hP0XiqRMI5jiseKwZB_OYpyER6J_ge3hOKmsiDt84gB1LE7qIq7Z7K41Sm7nxF9N4UKd8SyaDb84qXigYHRy_aO9EnAXjtJsSUTZZKJDDnMoyDTZywwCpNM1LK168jIKDx8wSkQd3h5Um1c5r_tZE4wD1V58XkUG4jZskv999Y_GDltXNHfzvZv8VRVMmj5uqEyO8IPk0Ki-QCTaEFlUcjRTTzD2zAZsCeGlE3VP1MWsGJi2DBNFEbLMH8LFHcpjW5ljMlw2gl6UDJoAlkYguYI5yBBYMyl09Fu1kBeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری از دیدار سردار شهید تنگسیری با رهبر شهید انقلاب
🔹
این تصویر روز گذشته از سوی دفتر حفظ‌ونشر آثار رهبر شهید انقلاب به خانواده معظم این شهید والامقام اهدا شد.
‌
@Farsna</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/460148" target="_blank">📅 21:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460147">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b07b37167a.mp4?token=ORzlwgm8nIjmi0muMUtxUZ2PcV5ng590mdbCCnW1b_Xe45n6t27IraijDIEnrqzMsKbdzvUaJtIZwHrIfp7MKUobfcJL3hWhaMTC1GmgxHYnNIyUkEXo-fzdRCAdvFGLuKGm3ZYGlRyiUbLXm3Nd0YMNZXZfNubPEZNX-OrelesN_cammKM1wDcyGYf9zNjsLpFvHLvLtcb147WwQw23G3bsqQBzmQ73kdZv8GoMWqX38pPjuHH7bL65S0I8sYewuLLUVosfzF2-yzVcSsuZWlyobMh55xsLCrhRVkH09a__NQ00MRQuiFB1c7qxh28m8NUpMlaL9s1BUdeQ6sSVgkVMI7nAlgKj4o84MWizyqBUCSv-OMVcIzplFlN5EYD0QB45UAyFVc0Honxd_-O7j2Ecq4fWYeZI5Z41vO8XLFosQQd-fDQwj8NPyi1lV-ArnmLhgcNZMZxIU9kUBjYlF3KOrHwJdktn2TG9VZxc3w1FZfpLU4A8opWaZJXC6PiQsY7cR0UNGA4IyU36rvXcJ6L5Amz-jI0SlFuB9Md2htW735oy25ioFmzFjBDcxQr3pexIU-r99B5CS5lCxQxLMpfdgJkozQzH3Zxp2Bk-cAdtNY71aihU34OWO04kQJ8RAzw5GbH5PoIWAGEpzmWZAIpqKxvi89S4IMLFHPe-fGY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b07b37167a.mp4?token=ORzlwgm8nIjmi0muMUtxUZ2PcV5ng590mdbCCnW1b_Xe45n6t27IraijDIEnrqzMsKbdzvUaJtIZwHrIfp7MKUobfcJL3hWhaMTC1GmgxHYnNIyUkEXo-fzdRCAdvFGLuKGm3ZYGlRyiUbLXm3Nd0YMNZXZfNubPEZNX-OrelesN_cammKM1wDcyGYf9zNjsLpFvHLvLtcb147WwQw23G3bsqQBzmQ73kdZv8GoMWqX38pPjuHH7bL65S0I8sYewuLLUVosfzF2-yzVcSsuZWlyobMh55xsLCrhRVkH09a__NQ00MRQuiFB1c7qxh28m8NUpMlaL9s1BUdeQ6sSVgkVMI7nAlgKj4o84MWizyqBUCSv-OMVcIzplFlN5EYD0QB45UAyFVc0Honxd_-O7j2Ecq4fWYeZI5Z41vO8XLFosQQd-fDQwj8NPyi1lV-ArnmLhgcNZMZxIU9kUBjYlF3KOrHwJdktn2TG9VZxc3w1FZfpLU4A8opWaZJXC6PiQsY7cR0UNGA4IyU36rvXcJ6L5Amz-jI0SlFuB9Md2htW735oy25ioFmzFjBDcxQr3pexIU-r99B5CS5lCxQxLMpfdgJkozQzH3Zxp2Bk-cAdtNY71aihU34OWO04kQJ8RAzw5GbH5PoIWAGEpzmWZAIpqKxvi89S4IMLFHPe-fGY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استقبال از پیکر شهید نیروی دریایی ارتش در فسا
🔹
پیکر محمدرضا بادرام از شهدای نیروی دریایی ارتش در که در حملۀ ۱۰ شهریور آمریکای جنایتکار به درجه رفیع شهادت نائل آمد، با استقبال مردم وارد زادگاهش در روستای سنان شهرستان فسا استان فارس شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/460147" target="_blank">📅 21:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460146">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">حملهٔ مزدوران سعودی به یک منزل مسکونی در الحدیده یمن
🔹
مقامات محلی شهر الحدیده: در حملۀ مزدوران سعودی به یک منزل مسکونی، دو عضو یک خانواده شهید و دو نفر دیگر مجروح شدند.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/460146" target="_blank">📅 21:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460145">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aa844588e.mp4?token=lodG_P9jAsumMNqW3AdjWQfvD9_9UqcVoKWCdkNF93kfEa2RnSuGJK5M1iWxWK52hcbeHwxASvP-zEyFoq-vQJcX73CSrsqihyra0TOgSEZ9Zm9eH4Rtd5xC5oAYGt8sCteAIXGbU-xy4fZMqiQjo5PzgXyJhNhUPwml9pcM5YdIjhPgNyl1X9c0eEPky7ubidRdVHgsmNhZhNukhd-uwP9XFbIAasyie_sU_GbB6U7QvcuakgydVKwkPx9qvSR6bDBg4wb5B1pxM3EwHoKaXunjzbFm2kcmp8i8uIUreSXaq8Qg5Sb6LVBLE1rVExo_domV93QMJY7XiUT3hdqNITzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aa844588e.mp4?token=lodG_P9jAsumMNqW3AdjWQfvD9_9UqcVoKWCdkNF93kfEa2RnSuGJK5M1iWxWK52hcbeHwxASvP-zEyFoq-vQJcX73CSrsqihyra0TOgSEZ9Zm9eH4Rtd5xC5oAYGt8sCteAIXGbU-xy4fZMqiQjo5PzgXyJhNhUPwml9pcM5YdIjhPgNyl1X9c0eEPky7ubidRdVHgsmNhZhNukhd-uwP9XFbIAasyie_sU_GbB6U7QvcuakgydVKwkPx9qvSR6bDBg4wb5B1pxM3EwHoKaXunjzbFm2kcmp8i8uIUreSXaq8Qg5Sb6LVBLE1rVExo_domV93QMJY7XiUT3hdqNITzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خطایِ نقطه‌زن آمریکا در کوهستک!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/460145" target="_blank">📅 21:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460144">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fffbd748c.mp4?token=r8idoPoq-TQIrPYjIBUahExCYQMN5707ailW7MCHWjv3v09XoKJozzzayi1TqssywDpSIxEJDZFYBe6YYihjcyTJY58tEJ0rhDn_UITlIaqmEmO5e5De6eL7JmAxznTxf_IkSKbkbNywbmlnGJZ5tYylZmZa261zlUm58N_tHjvzjvCwgBm9eSbgs3n6L3lFUghJ0kDgCSlWrmeHmEkTrnGfkif_C4FmKAsJcwsOOGwy4xr1qN6TbZz9C9CuJGPMxhHhg_pURuavMttCiw7ageVDW5gIA4lj-Orack6H0fs9AF865NlpQ-A8L7Cjz7XOdr0NBTRHDe_cZo2ZDrgK6E3oUiUeYasGRMzkkhTbQNdO8wsBxQgNpHrdB6BuwytvjwncxiD4Q6_rr6Co-7Lzyv7bR3qPfiXTM63ZvU5PHpb921hCn0ms1Z292OPpapMmWgU2Gb5FgsF976tMI_RtLvT-4OJ6xf6-qmcb7roh2KoZ440QQDBzEjd2Vy5p4Mn4joVHQ6XiFBoKCK48ixqowMO0Z1pbQ_XxxXRcJ_-ugpBJ_aPSjpCYl1iRMn-AnpppxjiCC4i1xJlfxpFzN7cKMcd9xT0OQsONaFVaFXoZhfideQBvwdP2exJ8Gkln3TgBFiE1GowCRPgYZx-Yk3oazgkY4nPsR3FZyj7QEYyASwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fffbd748c.mp4?token=r8idoPoq-TQIrPYjIBUahExCYQMN5707ailW7MCHWjv3v09XoKJozzzayi1TqssywDpSIxEJDZFYBe6YYihjcyTJY58tEJ0rhDn_UITlIaqmEmO5e5De6eL7JmAxznTxf_IkSKbkbNywbmlnGJZ5tYylZmZa261zlUm58N_tHjvzjvCwgBm9eSbgs3n6L3lFUghJ0kDgCSlWrmeHmEkTrnGfkif_C4FmKAsJcwsOOGwy4xr1qN6TbZz9C9CuJGPMxhHhg_pURuavMttCiw7ageVDW5gIA4lj-Orack6H0fs9AF865NlpQ-A8L7Cjz7XOdr0NBTRHDe_cZo2ZDrgK6E3oUiUeYasGRMzkkhTbQNdO8wsBxQgNpHrdB6BuwytvjwncxiD4Q6_rr6Co-7Lzyv7bR3qPfiXTM63ZvU5PHpb921hCn0ms1Z292OPpapMmWgU2Gb5FgsF976tMI_RtLvT-4OJ6xf6-qmcb7roh2KoZ440QQDBzEjd2Vy5p4Mn4joVHQ6XiFBoKCK48ixqowMO0Z1pbQ_XxxXRcJ_-ugpBJ_aPSjpCYl1iRMn-AnpppxjiCC4i1xJlfxpFzN7cKMcd9xT0OQsONaFVaFXoZhfideQBvwdP2exJ8Gkln3TgBFiE1GowCRPgYZx-Yk3oazgkY4nPsR3FZyj7QEYyASwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بدون تعارف با تاریخ‌سازان والیبال ایران که قهرمان جهان شدند
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/460144" target="_blank">📅 21:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460143">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0a8b8a488.mp4?token=N_JvU9I0Iby399vSl1hZAtG7l37kH0QcrG9lS6gpCqLUpjXW8AqWyAqV_LuqgeAlTancx9EjtZW60jpptHM55uCHCMQmgTeikKV-w3Xg0mdp8SZdjAc7rUt4d5mAhr8YFPFCtylqbP3G4bODUXt8-rNzHPtFLk7UzqQaAxrPCW-4Gl0MGHG99i6QVVrtsOu9e5orY79BXT6MV7blwkIlcG2w0BPF-AqPHK2FYIt2JtycI_QCGujxEjZErMFwPA26s8lhmo7fWc0SNWj2mrVmyyguxd2DtCeR-H02L_C7DdC1fbCXctoeboPVCngJP7r89dJ8UbSugTaRRrQfmUvL1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0a8b8a488.mp4?token=N_JvU9I0Iby399vSl1hZAtG7l37kH0QcrG9lS6gpCqLUpjXW8AqWyAqV_LuqgeAlTancx9EjtZW60jpptHM55uCHCMQmgTeikKV-w3Xg0mdp8SZdjAc7rUt4d5mAhr8YFPFCtylqbP3G4bODUXt8-rNzHPtFLk7UzqQaAxrPCW-4Gl0MGHG99i6QVVrtsOu9e5orY79BXT6MV7blwkIlcG2w0BPF-AqPHK2FYIt2JtycI_QCGujxEjZErMFwPA26s8lhmo7fWc0SNWj2mrVmyyguxd2DtCeR-H02L_C7DdC1fbCXctoeboPVCngJP7r89dJ8UbSugTaRRrQfmUvL1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: دشمنان با جنگ، محاصره و تحریم به‌دنبال ایجاد اختلاف، شکاف و آشوب در داخل کشور هستند و ما نیز با تکیه بر وحدت، هم‌افزایی و انسجام ملی، این نقشه‌ها را خنثی خواهیم کرد.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/460143" target="_blank">📅 20:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460142">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twlI9ipuQ0Q8kUAEX3FUEAQrb8tLl3ndowuh4tE8W3DuoHMOqff7wAPYQnnKBBtiql6ILJo_kOXW9dDvoiXxP1Qkuji5L6SBqlrb-UV2g0zD99TyioNVSyWrzXiPLhpIitT5ONSd4gOyi9W5p-gRQmQgg5M7hcPcIJnULBmbmAFu5gGDnFjMnxN9KNAvUskQPymu1EBWLd8eZygJbc46ztcyzBilvs3T_lvNqo0aaj9-5MC91DtSjeWU02DnUR9i1SaOFUccWp7nqYphxOLXC29fXW3bW-tDSj_81fpPc1YAkr3vyj_OuzjVTTzv2PYpr84rFyCeJiR5JgcMzXARjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فصل عاشقی مرال‌ها؛ جنگل، مهمان اضافه نمی‌پذیرد
🔹
همزمان با نزدیک شدن فصل گاوبانگی، تبلیغ تورهای طبیعت‌گردی برای تماشای مرال‌ها در فضای مجازی افزایش یافته است اما معاون محیط زیست طبیعی و تنوع زیستی سازمان حفاظت محیط زیست، امروز اعلام کرد برگزاری هرگونه تور گاوبانگی ممنوع است.
🔹
فصل گاوبانگی یکی از حساس‌ترین دوره‌های زیستی مرال‌هاست که از اواسط شهریور تا اواخر مهر، همزمان با فصل جفت‌گیری این گوزن‌ها، ادامه دارد. در این دوره، گوزن‌های نر برای تعیین قلمرو با یکدیگر رقابت می‌کنند و با سر دادن بانگی شبیه صدای گاو، ماده‌ها را به قلمرو خود فرا می‌خوانند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/460142" target="_blank">📅 20:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460141">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQzn3bJfwEGK0VqewjNlwL405gCKtxHsGJ8Mbk2YHanDW_-e2mET7gBGvF_NxbvUjLq8FfHh1k26SGRlRkcIQsPGUFcT8joCLuUYyTKAZ81zwXNBHw30xtulgQ0K-Lgl-5g3c1UP-NKrCH5B__HMLYtJ13zKApCJyNQUdfUmRtRQvKV2ABCJvK52CwBQo92QziH819eUonrWRQ_HuzXaz5TjY7N0kI-rTkNe1eJx1V9J1HeYvQpEeB6su9CX-T7iFUlLRTbskzxf0E-GbnnrogF7jLiwGtuax2bIcUEPACC9B_fd61zwfTaE2R7EV883ZXJb_ivZTfBAA0jibRAInA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: ایران از ایدهٔ چین برای ایجاد یک معماری امنیتی جدید در منطقه استقبال می‌کند
🔹
نمایندهٔ ویژهٔ جمهوری اسلامی ایران در امور چین: تأکید چین بر تقویت امنیت مشترک، بازتاب‌دهنده اصلی است که ایران نیز سال‌هاست بر آن تأکید داشته است.
🔹
کشورهای منطقه باید آیندهٔ خود را با دستان خود رقم بزنند و ثبات واقعی تنها از طریق ایجاد یک معماری امنیتی جدید و بومی در منطقه امکان‌پذیر است. ایران آماده است.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/460141" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460140">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/930c9bbe22.mp4?token=gMzGJepo_rmpA-KVxu6IJQfisy0QqswlOFwo4e6sSNQ9PG0wV2BkZRBPhOEStl_21HlZwuba-ZX_Y4LXq2XocjblscXOfk762BX9o8Jbzj3YNlRXP8p0zyoLbIv-Gv83pc8thkRKxyOgDhWl6XIThDHVimbLqm3swcf5Tkq5wJNJZiGXf5QBmGYoLMRAfqSczqcsyJGXSdX75GtqnGXjw5pIe4QDDd5bZq9oYVKIA_Qbc2USXpPhAanKWrB9-b3rCEOjvALUewRQ6TKxkXu5gPGgw_ZrdaxicIvzS_K2HMRRsC73G8sI2bSUx-L_IJO2k34fVXL2v4sfNlQI-R8ak2aGMjS7Smdoqr1vOROu7TPhwCFBKbJD-Ut_rk2MP6kIuW8_U0kbRAm7GjhBpw24x_zayWhpzmCJ7hUAQowQ-pdQADEJYwLNTcm1sTpvEn7oDJoI1ahp3jifH84Hh0_IMfwVRWD6aeZE7DM8s3hMNEYgahcjUJt-E3Yu1qtml9qy1xCLRianDAvq4WInWTD_JLDkDEdAqmkRStQEyhxZBQDShykbh4TCSXkTrWVAE0IuolshsdHEYNmIq289oFAM-st0vkXUNWMVDitwUnoKXuRGVIt2mGT9AiKFi7dsgd4K2ge5TKbCoNdyZYwgW5qILRw1ZAMC4jXNwSXHGuV41DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/930c9bbe22.mp4?token=gMzGJepo_rmpA-KVxu6IJQfisy0QqswlOFwo4e6sSNQ9PG0wV2BkZRBPhOEStl_21HlZwuba-ZX_Y4LXq2XocjblscXOfk762BX9o8Jbzj3YNlRXP8p0zyoLbIv-Gv83pc8thkRKxyOgDhWl6XIThDHVimbLqm3swcf5Tkq5wJNJZiGXf5QBmGYoLMRAfqSczqcsyJGXSdX75GtqnGXjw5pIe4QDDd5bZq9oYVKIA_Qbc2USXpPhAanKWrB9-b3rCEOjvALUewRQ6TKxkXu5gPGgw_ZrdaxicIvzS_K2HMRRsC73G8sI2bSUx-L_IJO2k34fVXL2v4sfNlQI-R8ak2aGMjS7Smdoqr1vOROu7TPhwCFBKbJD-Ut_rk2MP6kIuW8_U0kbRAm7GjhBpw24x_zayWhpzmCJ7hUAQowQ-pdQADEJYwLNTcm1sTpvEn7oDJoI1ahp3jifH84Hh0_IMfwVRWD6aeZE7DM8s3hMNEYgahcjUJt-E3Yu1qtml9qy1xCLRianDAvq4WInWTD_JLDkDEdAqmkRStQEyhxZBQDShykbh4TCSXkTrWVAE0IuolshsdHEYNmIq289oFAM-st0vkXUNWMVDitwUnoKXuRGVIt2mGT9AiKFi7dsgd4K2ge5TKbCoNdyZYwgW5qILRw1ZAMC4jXNwSXHGuV41DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
ادعای صهیونیست‌ها در مورد تسلط بر ارتفاعات علی‌الطاهرِ لبنان
🔹
ارتش رژیم صهیونیستی مدعی «تسلط عملیاتی» بر ارتفاعات علی‌الطاهر در جنوب لبنان و تکمیل پاکسازی زیرساخت‌های نظامی موجود در زیر آن شد.
🔹
ارتش رژیم اشغالگر همچنین ادعا کرد که برخی از افراد وابسته…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/460140" target="_blank">📅 20:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460138">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xh53ER9YxqL75lBr7k_CSagnCLZ_52GaXB31fyb87oEhwZTH21qgV52OJMu22NYkEHJWtnbhN3NrWKSmZZXD1k4dePjGmCentvlfAyMCkQP9zlqAZoeRs5FkAkxlFXE_bIRRAE5xQiwV6CDr59FwuFws-wXl62AtnjH1jjcnkFAG9ItF8rHHZXzyP7tSvLtB39WzvByg0J8ARoS3VJjZwoHZrXZro6FyamU_UDZw4bryOkc-JOWTSwgXo27w77RyEjmVf5KFRozlXqDkZUjp3_gKUN-Jlgv0jB2Y3o5gb_6RWP9T_QNCzNeyD06_viPuCEhlYZ-PUgH5KeIecoBevA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عصبانیت ترامپ از شدت گرفتن انتقادها از او بابت جنگ علیه ایران
ترامپ در شبکه اجتماعی تروث سوشال نوشت:
«دیوانه‌های افراطیِ چپ‌گرا، دموکرات‌ها و کمونیست‌ها ترجیح می‌دهند ما در جنگ با ایران
شکست بخوریم
تا اینکه رئیس‌جمهور دونالد جی. ترامپ این جنگ را برای آمریکا به پیروزی برساند.
به عبارت دیگر، آنها ترجیح می‌دهند ما ببازیم تا اینکه ما برنده شویم! اینها آدم‌های واقعاً بیماری هستند که به نوع شدیدی از
سندرم
TDS مبتلا هستند؛ چیزی که گاهی از آن با عنوان سندروم جنون ترامپ یاد می‌شود.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/460138" target="_blank">📅 20:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460137">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
منابع عربی از حملهٔ موشکی به اهداف آمریکایی در شمال اردن خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/460137" target="_blank">📅 20:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460130">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R_9GJIhheXr9gLpFITpOC7IiAjBgo9SDMyCIDrI2jWzgLdJGF3oUWsdpx_v4cRPLP3zwzQbOlHSrlbAGuRczKEdrfw23LxE2xToeJGF0n9yo_YjCs_CKU-8c60ZU2tuZFUwRubMHAuRRLrapQKhmw5sLOYsIj948D1USZ4W6YrOD_Wcf0AHgmHQPOEdpaYgA6iQDZ4LIiaeWXr4zWOtYw50De5hYgmz8QDwMGBrOIthoyD5uY6kXpsf92j3ldia16qNEpMjhRqJzGdWAVct9lYCDQS38ngvWhNct0_ySXmflfXKgkaHXCef6tj9PRKfsD7rD4-Xviao3WCKv1fvXdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lTedLZqt1czJ5uTBRBUdohzKqldjECxBa3NSJC8WzhKJxFccn6vC9xCezUsqCDXLTDT1QcoVZOGHM4q1eAce2H--MwlyxNJpKphqNOLtVx19wWpNySbuXtMSD2dIGIYaLxcwngz7-lbzUegWuhfd_HXkU6gwYBcvyCcQek9OPdP_ZF8fYiLuGT06uH_ponWT1kS7JSjDxR8gpqYacjlht2eJ3N6LCS7sTcv3tH3rPnrnJ2h3g0zhpJU6v6GXLxaHqPvV85Flp9Ty5iw0rZZj-PtibsNXmVbSoBN5hJnsVPwvr9-B_ziHtjm0Vk2LlStuFCJICnoHX7U0-6hkcoJKEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k6BE9oBjzwCU1XwO2829_tVhahzyqCUayy5Lt7Ch-Az769gb4dbtObNwuEDc8OkI1kdDg04XnHo_HPXtugrrF1qC2tGxYipZ1MKccl496gV9-nnDORDBDLgk6C7_wwqasdOgPdgYvDl1MtFcDEw1MMBGGGOFzQAWh2aYfimqzmwhEdmd-gJW-hRLS-azXTdK_Uqy4JhayEX034Pvpf-26n9dUSMgNjk6zIu5aw59x1V5vr3Yon9r24SLs3HUIhdrCSlS-zl_eg2w3a5zO0VQRVqr-gMb2SfGIOMmPmG4kZQme7v1Y22BsZKPQU_s8PktDsQR3OX6GODOGD8BAu4H4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V4UpnRdmMdrtdR2Dr0Noj02jm82Rcbyyyx9TaPWwPjtQunHTcndE3VdmQ3ds4n76fyhf47yxPzpzAisNTlbPfxO8e9-m_dvT5_D2T3L4-flZYrubo0gsNDl4a2dnsEef-573JCoFaTFjqVDCKE7Fz7kqgWPK8BSo12dZy6Z-cxRt6zXKlsnUUwHXJy5Pv7SJjkiMVLfzRKzZa-UMVancsh8yvHPG29qMjFL0fC2ZRZ4Yt1wLAboERvwcLT9pNMVQX8AXsgoyUefzhMBNcpGeS5a0ajnK5b8FdYHWZBzU0WRRnyU4AgD_POdrFlYyDLvwjsjfM0VSFgNQOE8NeAPsbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rM0nU0yarh8pl1xG-v8AECKK0HJQaZxDRWNJcEYNeg74sqWqGnc7dyybQsk2u0OHwhlyJuNvGbMzDti0PuwtDOwqNZoplwtaRzyeVF6ubAxix-AHNvp-cola_fBdE0ScuYv54-oA_Aw5MLuqc2JXzSCOYD6x0pEKbphei_DuNyPaneDjqBg1mqSwMnvL0ASJlEDyBZTNI-uY6bbBmrFpwD9WZLsAjKpBUxvBCcxjRniqGNx_DKKKeQyYM_Vnk6i6gTg87KboZum5Ycm4p_iokFBd2WRXdwP7E-dSeUKFxBiq8GfTBRaevci_Uq_sEjURr39KCeuvtz7DCIhfzE9EGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DMTgrRkh0GEdcq_g35z2Kebk8cvIcKfXsKpwqQF6nWOEN_pU7fGvA-LVLcJoc9Q60nSZby4baJQ9afN7MwG22BP-unetABFM5XhmsUqRzFaJV2piT-2U5WxndWfONEYB4JwLkXTN4wcedZ2PDg-1CUw74PEr1DVsqPzZCdpxA5jS7ztFQ6Y7irsPcSY2PuWI9uDCNWA-rnLvYt4Zf03PQMfyfpoIgTlEbtvWFjxrwjXd6VPkjS04RdVxdoObnC5ynLYcRZoGH3lCTT4wIgB29VY_v8JVxr4OHP_jczf98YPCsGXcxjokGnm_C7VCJNX2C4hr_4sW1GCTF5ueO-x6ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cib0uowCP8mvdqYhvqvhr95h_R4h6T_uUm64uICtbxn7cqeCbLDbr8_daiN9NsrljN9B0u2k9uTbqFNwZt50CjV9SUuAQ7DqipjBB0InUuit_kl80FlZ0OjaQszKH3sOoRSDAXXNFgg57TIVvdLkG5NgkqFCbnCXE-PwC4FQb2zN8LNp47PXPadCjHLNqtF3Xv_qPl6GVXgYO_TbPYyKjgMTNupNz9JTY6kA03xw5JjrE1OF1j83AW124K-sDszF9HmzMBvitfscLPBFgaxllCld068Sgx786CQyOs92sbPSBaHpoTL7fqnRz6Pny3u7XcCvEVhm8n0bOV6SBld8fg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رقابت رزمی در «میدان‌یار» کرمانشاه
عکس:
بهروز احمدی
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/460130" target="_blank">📅 20:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460126">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UdW2mm1KKcCExXMbViptcGHT_w0xHpIOQ3Y5HhdR6457tjejAhv48DH_3z37HLvGXCXm6Ymd-D1JQzfMWU9RPN-pxaXTzMDtSY_1k-7lNmzZggn85yev3gCxAoqQJs89hh7SyC22b2BeX1Y6tnlZJS7LuUD0Z67VQ-dvTPv5onrMw5DbYDeySNQ1s3LI7LPFuRO69pNUHa9AC6JXg4TEOuxuzkJdfUU3GxsTojjBbfoma9MxGgf8ENlqusE5WiboaYAuBDT4KsyKYJ_qFWJwuNiupmu1olT_gCsslmyyfatnc1m-cwv976SZI3fQ-bhkobeMBoo6bazpSeTxKmCq3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L1ozs6afKjepdSYc1IdyaqH4ZUXJNjsiMQXjJVgwoNaGWJODQsJzkPVh0L6PKZWdHd8butONRm9b_Lynw5l84OK1fuk_JCK3P3tsvh9S_JZlnuGU1cfsp3nOVW1vQ2_jGX6JIJp5olRiR7ss8ta_MwjN8ZOUZvZdQf8HKkOYm12rlmgfURW3UsWG0ZiKuX9ZWh1OK_PnNLSWAX4cumpuWsTtbTOg4Qs5Hkljl4FW76P0BFrQcW8Fr8ZkIVuE6-tPICZ64DTLTm5V902W_iWV_OzdRDaj5ooLMdvmfrpPSCcPb3J7nvPF9aKxHZ0ZpLjdmk8dRSUmXEhafEDUx9eCSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bU2SCSeSGJ9Ff-MHW8wZW67B4YZLjDfA6J7DlwmHQxBAXL5rqMKHY2eGrgQqbbgdsV8sFLNrte36ayAmBh4CunvG0D-KNrkKZQi23M36mXUNxomBRhOW8ENyMqPwWTG10woDKxfyKZ9rylqLKBwuiZ0mZqHfn9--KccISqjklm-Yhkz1ADzq8qPBdtwLWvnUiILKE0D41cL6aEi5br4Hs7H0tTBQuAQ5SxxKHOKN_t5pZfHGv5Pkg_wsbVU9SAyphkFG2qgsRmOs92WlpwvadbF9XcA27OVMMGsVptjVreWOCFoPia8hJ4i95tNG5sDPfBXEPIx5k2Dtd2VRjfRAHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gskPBEfYzOBp25Ma5WPcQMHEygxhafDjwecilBUp_GySb2vNqHv78b5dugTwZtinGj6OsTYHXxiYc3t2b5FtDW926yz17YM3xWh7jPN-qd8BKE5pXOm8IkSjG3Vr7THNKJ1x-7RqLFoMRuFaK92CoTae-AJCl9O89Iu_QO0UgcLPiN4dkhZ-Yf7DnDaToh1WTG7EDDUOS5iaCIXH2BDoSkvCULJ2uQskgNOUZ7ZvotVvrVCLStuYTaFWlH7e9nQeGrgwYBp-bSPkaeV0nFDWxynLZcobeeUd49x46eWmFLhQxGv0jUiddmZkNB7pVwaguHSpg95h6tXD3lJJTiP1fQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تمدید بسته‌های ایرانسل اجباری شد؟
🔹
اگر در روزهای اخیر بستهٔ اینترنت ایرانسل‌تان بدون اقدام شما تمدید شده، دلیلش رویهٔ جدید ایرانسل در فعال‌کردن تمدید خودکار بسته‌هاست؛ رویه‌ای که باعث شده کاربر برای جلوگیری از تمدید، خودش دست به کار شود.
🔹
پیش از این، هنگام خرید بسته، گزینهٔ «تمدید خودکار» به‌صورت پیش‌فرض فعال نبود؛ اما حالا در اغلب بسته‌های اینترنتی، این گزینه هنگام خرید به‌طور پیش‌فرض فعال است و اگر دقت نکنید تمدید خودکار آن را هم انتخاب خواهید کرد.
🔹
در سیم‌کارت‌های دائمی، ماجرا حتی متفاوت‌تر است؛ هنگام خرید برخی بسته‌ها اساساً گزینه‌ای برای برداشتن تیک تمدید خودکار وجود ندارد و بسته با قابلیت تمدید خودکار ارائه می‌شود.
🔹
ایرانسل در پیامک‌های مربوط به حجم باقی‌ماندهٔ بسته نیز اعلام کرده بسته‌های ۵۰۰ مگابایت و بیشتر، با رسیدن حجم باقی‌مانده به ۵۰ مگابایت یا رسیدن تاریخ انقضا، به‌طور خودکار تمدید می‌شود.
🔹
در نتیجه، اگر حواستان به غیرفعال‌کردن تمدید خودکار نباشد، بسته می‌تواند دوباره و حتی چندباره تمدید شود؛ هزینهٔ آن نیز بسته به نوع سیم‌کارت، از شارژ کسر یا در قبض شما محاسبه خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/460126" target="_blank">📅 20:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460125">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1869c43e13.mp4?token=Wy5H8O9Udi1idl8PnNbacI7NTI07BRyKtmyLNNrGjjsCLkalUT7SmUDMeSoGhh6CP7Imki-Ji2zB89Qd6t-TETYHBAMOYsXKElyLjtzjaHOupHnkIzRMt9EU8g47iNXsO92MXSE2LVjSqGiWJAU_Gox1T4hAaDg4t5PC8yQBhbm8veDXA7xFEQSv_an7dMVcaykUTznX-5iMwun-aDQtkiHQIubuxsarRl1iBcFC5j2hRKieKZXw_JCaX7lSKh5icdXwpYobeCpQbtAShPPdbgb9g5siOmUmKi07nmHM7kJGymCscwIGqixd1hX5UO9Sjy4Dpdr2RdXw7NDB07vEQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1869c43e13.mp4?token=Wy5H8O9Udi1idl8PnNbacI7NTI07BRyKtmyLNNrGjjsCLkalUT7SmUDMeSoGhh6CP7Imki-Ji2zB89Qd6t-TETYHBAMOYsXKElyLjtzjaHOupHnkIzRMt9EU8g47iNXsO92MXSE2LVjSqGiWJAU_Gox1T4hAaDg4t5PC8yQBhbm8veDXA7xFEQSv_an7dMVcaykUTznX-5iMwun-aDQtkiHQIubuxsarRl1iBcFC5j2hRKieKZXw_JCaX7lSKh5icdXwpYobeCpQbtAShPPdbgb9g5siOmUmKi07nmHM7kJGymCscwIGqixd1hX5UO9Sjy4Dpdr2RdXw7NDB07vEQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی دولت: رئیس‌جمهور در حوادث دی‌ماه گفت اجازه نمی‌دهم اعتراضات به حق مردم توسط بیگانگان مصادره شود  @Farsna</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/460125" target="_blank">📅 20:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460120">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91d9f21b8c.mp4?token=eQHcDocq-LgpvA2FcOGbQsRGCCq8EmqTG1Ip0DIlGvuijaVhJ9JRoRK1W7uEp8CsawpMxdQNp5bOtzN4YmlIAHLyWbE8NOQPESInAKjsvazEAhz8Ni1KlDQhlpqz1wTuyWJrudRUO072vl7FD5xzvvnsnBJzo3ICg8ndLjIbCOPfAzSwAphtmHE9CSATbGTYS_4ykrAad5ckpCE4HGbkifiyUpDI26yc0lYJ_IJ8w3AnaDFvetgDkntLJA1u1T-oucowFKwiXcj2O5OG9_yRlUXUZc5MMblEmKJytMJIgNw5Oun741-UukhAh0DJKLSGSzrPVQDiyrvPs9tk5XpZ5QRS76wGEOEBAcU833NrtS3bBDrXNJqjvjSvnR6AdYA6rZSHdACDB9WdNqBTqd6gcMyYFkF8ITPQfjFs0R5yCbUXQp-VCiEA3-er7wvtiPGj8Q16R8wt-6iFnyoMqY9CjCGi4EP5njODOtfMxUDZ64mO-DUPJG2ruNBvT8aimD2_GzjNJhkMX7b8g_S80zUHlG7yY6t-tU0BfQx4-gIYXjDTnMBJq9unQMi_pehId9vD6g5Q8DxosLrqotwTePhvkc5s_6KDUJEJsKz3E-edFFpuScxyzwLnVpdKvLXHBscOwXpfWqTy2lKa0dq-_NGu_OueC8wDwT8SfFQ9sEJvKwc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91d9f21b8c.mp4?token=eQHcDocq-LgpvA2FcOGbQsRGCCq8EmqTG1Ip0DIlGvuijaVhJ9JRoRK1W7uEp8CsawpMxdQNp5bOtzN4YmlIAHLyWbE8NOQPESInAKjsvazEAhz8Ni1KlDQhlpqz1wTuyWJrudRUO072vl7FD5xzvvnsnBJzo3ICg8ndLjIbCOPfAzSwAphtmHE9CSATbGTYS_4ykrAad5ckpCE4HGbkifiyUpDI26yc0lYJ_IJ8w3AnaDFvetgDkntLJA1u1T-oucowFKwiXcj2O5OG9_yRlUXUZc5MMblEmKJytMJIgNw5Oun741-UukhAh0DJKLSGSzrPVQDiyrvPs9tk5XpZ5QRS76wGEOEBAcU833NrtS3bBDrXNJqjvjSvnR6AdYA6rZSHdACDB9WdNqBTqd6gcMyYFkF8ITPQfjFs0R5yCbUXQp-VCiEA3-er7wvtiPGj8Q16R8wt-6iFnyoMqY9CjCGi4EP5njODOtfMxUDZ64mO-DUPJG2ruNBvT8aimD2_GzjNJhkMX7b8g_S80zUHlG7yY6t-tU0BfQx4-gIYXjDTnMBJq9unQMi_pehId9vD6g5Q8DxosLrqotwTePhvkc5s_6KDUJEJsKz3E-edFFpuScxyzwLnVpdKvLXHBscOwXpfWqTy2lKa0dq-_NGu_OueC8wDwT8SfFQ9sEJvKwc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وداع باشکوه مردم دیّر با ۳ شهید حملۀ آمریکای جنایتکار
🔹
پیکر ۳ شهید بسیجی شهرستان دیّر که در حملۀ تروریستی آمریکا به جزیرۀ لاوان به شهادت رسیدند، عصر امروز تشییع و به خاک سپرده شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/460120" target="_blank">📅 19:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460119">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bfc862078.mp4?token=ntvxe8EC5N-4mrWRbNWrpdVxu48Gthv3lE0p2sdGz3PxiR3lZQxaj8sYN0j2o7hChXyDH3VP4gzuYpab7ZivJQtlrXk8RimLtnxitEvpwVXePOEsZjepwfTGb6VTyb7rh6u2hZIQs6wjnCrqckRQbn3tlUSCr7TWwN43j9wKGypb7EnYfnQNszutjrW5EZP6xUAp-OEQxV7id1KVwkaD2eKn9bZyGRLgsPf2Shfuwddk3eO7_hkIkOUvBXTR40JGC0iM6nGfz9LSQWm-VlSgYFZLtWNvNhfxbyGO4qz6grItjM61bUuO7KdcOEYowx8nQoZh9wQn3zEuBv6-eTTjmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bfc862078.mp4?token=ntvxe8EC5N-4mrWRbNWrpdVxu48Gthv3lE0p2sdGz3PxiR3lZQxaj8sYN0j2o7hChXyDH3VP4gzuYpab7ZivJQtlrXk8RimLtnxitEvpwVXePOEsZjepwfTGb6VTyb7rh6u2hZIQs6wjnCrqckRQbn3tlUSCr7TWwN43j9wKGypb7EnYfnQNszutjrW5EZP6xUAp-OEQxV7id1KVwkaD2eKn9bZyGRLgsPf2Shfuwddk3eO7_hkIkOUvBXTR40JGC0iM6nGfz9LSQWm-VlSgYFZLtWNvNhfxbyGO4qz6grItjM61bUuO7KdcOEYowx8nQoZh9wQn3zEuBv6-eTTjmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی دولت: رئیس‌جمهور در حوادث دی‌ماه گفت اجازه نمی‌دهم اعتراضات به حق مردم توسط بیگانگان مصادره شود
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/460119" target="_blank">📅 19:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460118">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس من</strong></div>
<div class="tg-text">سهمی در لبخند دانش‌آموزان نیازمند داشته باشیم
🔹
مخاطبان «فارس من» با نزدیک شدن به آغاز سال تحصیلی، خواستار برپایی ایستگاه‌های جمع‌آوری کمک‌های مردمی در میادین، تجمعات شبانه و نقاط پرتردد شهرها شدند تا خیرین و مردم بتوانند در تأمین لوازم‌التحریر دانش‌آموزان کم‌برخوردار مشارکت کنند.
🔹
ثبت‌کنندگان این پویش تأکید دارند با همکاری دستگاه‌های مسئول و گروه‌های مردمی، زمینه مشارکت عمومی فراهم شود تا هیچ دانش‌آموزی به دلیل مشکلات مالی، آغاز سال تحصیلی را با کمبود لوازم ضروری آموزشی تجربه نکند.
🎉
برای حمایت از این پویش
اینجا
کلیک کنید.
@Farsnews_My</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/460118" target="_blank">📅 19:37 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460117">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7ec2c47be.mp4?token=KWo73aes9XBRp2f5YJhLzlfxSzXXBS50xrbqLn5mt5SmGmixS3XJFdukOcF3CGbF8oX5nWenp3o1BDZ0dPvQuLVo7rk9qg297TSPBcnFnrJGhJjb3mYii3gctUKU59K8pBYkvvdBgfyEmMfc0bkcO8yK94GmNYhVNzL0GXfkFIAbrqrUq2whccDmFN-MEjLQ_tM34LPoFgcEZtVFjoeK5Yc6NM8qJCgLhp_D7bwXneCBwClMxdwyHyLRmmo8lOAYISwq0ip2KxVpLs5cS7KXCdrkBRKNlCn0TlLTt42x8vl4ATmgiT1YhjUSM3rq6JqBEDdMg6zPhBOJdmFqhiszDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7ec2c47be.mp4?token=KWo73aes9XBRp2f5YJhLzlfxSzXXBS50xrbqLn5mt5SmGmixS3XJFdukOcF3CGbF8oX5nWenp3o1BDZ0dPvQuLVo7rk9qg297TSPBcnFnrJGhJjb3mYii3gctUKU59K8pBYkvvdBgfyEmMfc0bkcO8yK94GmNYhVNzL0GXfkFIAbrqrUq2whccDmFN-MEjLQ_tM34LPoFgcEZtVFjoeK5Yc6NM8qJCgLhp_D7bwXneCBwClMxdwyHyLRmmo8lOAYISwq0ip2KxVpLs5cS7KXCdrkBRKNlCn0TlLTt42x8vl4ATmgiT1YhjUSM3rq6JqBEDdMg6zPhBOJdmFqhiszDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنین نقاره‌ها به‌مناسبت سالروز ورود حضرت معصومه(س) به قم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/460117" target="_blank">📅 19:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460116">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">آتش‌سوزی دو کارگاه بافندگی در تهران
🔹
سخنگوی آتش‌نشانی تهران: دود مشاهده شده در آسمان مرکز پایتخت مربوط به حریق دو کارگاه بافندگی در کوچه برلن است.
🔹
آتش‌نشانان در محل حضور دارند و در حال اطفای حریق هستند.
🔹
تاکنون مصدومی در این حادثه گزارش نشده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/460116" target="_blank">📅 19:24 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460115">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efbaf95122.mp4?token=sLnPOFCDTz4IyHfb8nOxuRODyA1bE4k2HMTRxRMKvVKQzIvVDYrsvDw6eP1kQrWsuTfU0vOOVDcK6ftsXrmmAxXPSeIGyyYkfP7iDP_g3upgzitCFEkyq1igFan6NKDEXfgDGmiP3rm9sfV9hCe2uF6KE1FiRVQzX2VoqRYQfvexUlMde1374BwjdV0Lr1PQNLdW_y84RXn_3QtnVU5UypgqXsr5gearQfN_tblR5YD2u8ELJy9ZH9eo4Kz8b3BpjSaBBCKrqtvE4AdGmBw0BvwWUPdyY5oBhaQuN2v3GJ3aI4HySJkUur7n1ngg5XFVi_cQ2JRJaT7mRgFwOZX0qTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efbaf95122.mp4?token=sLnPOFCDTz4IyHfb8nOxuRODyA1bE4k2HMTRxRMKvVKQzIvVDYrsvDw6eP1kQrWsuTfU0vOOVDcK6ftsXrmmAxXPSeIGyyYkfP7iDP_g3upgzitCFEkyq1igFan6NKDEXfgDGmiP3rm9sfV9hCe2uF6KE1FiRVQzX2VoqRYQfvexUlMde1374BwjdV0Lr1PQNLdW_y84RXn_3QtnVU5UypgqXsr5gearQfN_tblR5YD2u8ELJy9ZH9eo4Kz8b3BpjSaBBCKrqtvE4AdGmBw0BvwWUPdyY5oBhaQuN2v3GJ3aI4HySJkUur7n1ngg5XFVi_cQ2JRJaT7mRgFwOZX0qTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع ۲ شهید حملۀ تروریستی آمریکا در کرمانشاه
🔹
پیکر مطهر شهیدان رضا محمدی و شهرام جعفری که در پی حمله هوایی تروریست‌های آمریکایی در شامگاه ۱۰ شهریورماه به درجه رفیع شهادت نائل آمده بودند در کرمانشاه تشییع و دفن شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/460115" target="_blank">📅 19:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460114">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F428kHqpTJgjWQVR5H0KRdUouZ6jZPjk3Y8Mx3rIrhlzQZiPsNO34XU0OBafYn2NZ3Y8og2ybtYX0Brjeypkv38AKOFUFTVKxxZ94oYbBnBD1TMigQ12sWetD-2BQKTX3Lt5J-qtAkXSbsKxvLDGuTelZC7cGZQANOljmf11sVRPp6jDoGcjKyKEyO-tEW9xyQ79hQYnbycPvRc3NHgCivh_5ZAie9lAPBKnIQDdurdHNjPPmDZdAUZh_OlxWmdICNiXPKDlTnIeU9maqHmu4ccsiBz3Ef_KWRL1kkb0cc6XUtA9w10kLiSt9xV29Anpi0WS4j0ydB7HnMlBShQRLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های لبنان: ارتش اشغالگر اسرائیل به یک نقطه در شهرک المنصوری در جنوب لبنان حمله کرد.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/460114" target="_blank">📅 18:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460113">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eee7887d1.mp4?token=TBznAoYcuOfL-RnB3Uc0XnaWzCfRn1pFN6zg4m_RpUyjTZsViS9Ft5Kc9VeW1Th6V3i6do4lICLsqIezwEGmcozTTYHFrr3q3qw5qnxuP4le6SQm3_BiR2YWj3BO2S_Gy2M5U9etnVnuFLqIbBumcsVpyLC2OWNqivBpG8JgJ4mFD7dZNkNpBJL-5ejOP4WI8ohPluu7Mg6E6t1eJ9jWZ6UIS8NG5wlhDce_WoHQ_2wywulJmRXDSUav0ym9J63g7e8hJxsFHrGMMOtKlFxl61S1agDvbZhzkfvefaw-fzvnQ2muWkfacI8gvP6NG9sXl7YkcyeD__hqRqgGLB200A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eee7887d1.mp4?token=TBznAoYcuOfL-RnB3Uc0XnaWzCfRn1pFN6zg4m_RpUyjTZsViS9Ft5Kc9VeW1Th6V3i6do4lICLsqIezwEGmcozTTYHFrr3q3qw5qnxuP4le6SQm3_BiR2YWj3BO2S_Gy2M5U9etnVnuFLqIbBumcsVpyLC2OWNqivBpG8JgJ4mFD7dZNkNpBJL-5ejOP4WI8ohPluu7Mg6E6t1eJ9jWZ6UIS8NG5wlhDce_WoHQ_2wywulJmRXDSUav0ym9J63g7e8hJxsFHrGMMOtKlFxl61S1agDvbZhzkfvefaw-fzvnQ2muWkfacI8gvP6NG9sXl7YkcyeD__hqRqgGLB200A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
قیمت نفت از ۹۴ دلار عبور کرد  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/460113" target="_blank">📅 18:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460108">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mBaz9A-S3eLXxb1GZfUGvO_4FMoHqh84In9O2E36WNVgsFswbRZEwIhcBrpsnAYYy9kIaigGLp0odp-JYGZ63zSE5Ad5EYEBJYh63g0JLI1WKvqSqRuIo0skBAD1bIuu0mghr7gASgLQGv-HffJao-vdYzdbv45bLzeV4b_8pczpwZdOJEFuIx2OSpIHUVY379JtNr5YxoEqU3YrElCuCZrBP2R1OJZw9WkpKaYhw8eKqqTuQk5ZNebpl7_12hk3jZd4xMABkHMxNVR2119LvIkBVRD43Rr1KFvA7-42o4JCIP0S70rb_aSlEF8bpMsi0g4varrW4go8xECquyTdZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T7Ufa0Ps_VtE3e5Xya04svDqlBFoMtw9y9qbZbTDw7dqsedTXECJlvF8KkCYFkUWi16SnMlVAt8vrnKFHsSu0HUM-bqUZ00bslVJRjD_fuK3h6rYVc7Rr4Tfm2OCtGZ4_GfgyAtmZ6NM2iJKWre_R9ibNPzsY9eilOFqIfaO3iG8OT7qiwndjpQQYLAyN4eHTs-UxDessntUUQozZxJzNXgfJehsoTEet6NxVzWX0Gr0SKWL1dnvzcp3wqe6d66YZY1k2L8psk3rI-ZFRgWoK7nTPTFfI5KBGVle8NPCnpLCmUMR5H0CXSXj0aZLheGq_b2DDQArToKSM8woZNTMlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gO4n8Zb7mzw6fanQHjd-AT7BAIPYb2yrO8Xo6dCdjGFxjJDy3ji98ElGJpGPVJCwAKfRQycgIATCJ9ebAITCYUCX_oZzJFcnyNYOl6AE5WDhlc4jyIJwAvu68ckCl-xn5ZjlPRCVwYxSWKJQe48YIpTFodniI7khHMOo3BSEjB5YPt9mUEjMy6OM5FAHY4zIdDMzzs75MjlA818jgnQTAXRUNkErTl0t_sob_Ctd0PnucjtbinsIyUU6yE03l4PZY89gR5sM20K7YcKA7Oky6tj3jGKU1qZ5F5Fo7SnWQ4Gn6ozCGjinlIIwfgNo02ZD560n7tJGFrAgR7htNnpkJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UbBXyYieGIpqTuQ--bH8dSNJdOa_f0FfmiTxFRUIBRebCfwhECo9OljdUd_aeN_DCM4oUEnQ81L3A_pY6MssX9FwPJP-0zvG4C5mDIW9J6owPNMaZkDiEZWL4VbcdhLLlz2YvscI1B7FBRlHvRagZD176snTqUqqLbioRF0oHggqYNduaR-JCxZMHPhiGF6J2ycHXpxUNChkaDph9QukvKyGRwCoqngMaiDcsrmrrhFg-XXBv0-LpH7lUFXH-X26Pua_hNdzKFdZ2mzsLEQQSzow6HRFpJgegl3Vsf8V0g7A-WK9JTUFm3okvJVHOZLgQ95ZQ5KS8pz8PJBuuNSVPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NHF3N030Dkel17hyBQ0BVHFiytsiZ3REBzn7m_iEfzcNzOJXw4thh-sqWGwIU1Qos2PhttXkHRl7vbJhWGgzGaRSHu33EeM1d2SSWCTEZWsLhITesHhsH4D0jDXM3tauDk9BSpWBvhV9yQ4P_brglOtgaZ3kmT9JlxGAj9KvVR_eWl3rkemJvzLGmbUhgUbL47oaxHl3od2w9bYsOS9VN6pqnSv5Y9nyHT-d2WuAAdOE0Wf9jN4wITIH3M_aEPX-Yr0wCQ8Ea4ERYgG4gIalX_YnmAmk9C9_I92LZOwKewqJ3E-aMYu5mMroK4a6buN3SrHeEvymiwlsoyhhiN5fjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
از یاد نمی‌روی که نامت زنده‌ است، ای پیکر آرمیده در دارالذکر
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/460108" target="_blank">📅 18:37 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460107">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63ad405b00.mp4?token=tcca7OSG1Vcl3XFEt9yk2orY6kw7FkgkKhXhGMk6jnj1bFvcB7D4-KGKS27kgGQ_8Qq_ClwOaayTOu1YTutyIyXHM3crZRfhkPr9QMoxXXQcnpun0ODYKrPy_yzu-g3pN_yeAikbp4WaljMr9HKxZBoSnmTXJaSQvMnnUMK2op7oFaNMddzkC5ywOVtT07V6JA9xx6oseePsLRNBgcV6ERr3yMGm_Jzpi-r2m5E1CATEcD_8UeYrd6Weu5ufOlFL-WYI2M8DGvHl8KuQENt1mc2v53y-1gTmy3JaXjoHsX4BVA_dxH4QUd8tLACLmR42THSjSi_WXhLKIqCOfiK9tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63ad405b00.mp4?token=tcca7OSG1Vcl3XFEt9yk2orY6kw7FkgkKhXhGMk6jnj1bFvcB7D4-KGKS27kgGQ_8Qq_ClwOaayTOu1YTutyIyXHM3crZRfhkPr9QMoxXXQcnpun0ODYKrPy_yzu-g3pN_yeAikbp4WaljMr9HKxZBoSnmTXJaSQvMnnUMK2op7oFaNMddzkC5ywOVtT07V6JA9xx6oseePsLRNBgcV6ERr3yMGm_Jzpi-r2m5E1CATEcD_8UeYrd6Weu5ufOlFL-WYI2M8DGvHl8KuQENt1mc2v53y-1gTmy3JaXjoHsX4BVA_dxH4QUd8tLACLmR42THSjSi_WXhLKIqCOfiK9tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای:‌ آمریکا دنبال چاره برای خارج شدن از باتلاقی است که خودش برای خودش ساخته است
🔹
آمریکا و اسرائیل در سال گذشته و امسال همه توان و امکانشان را گذاشتند تا جنگ ظالمانه و غیرقانونی را بر ایران تحمیل کنند.
🔹
ایران پایداری و استقامت کرده است و آمریکا به هیچ یک از اهداف خود نرسیده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/460107" target="_blank">📅 18:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460106">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">فردا احتمال شنیده‌شدن صدای انفجار در قشم وجود دارد
🔹
فرماندار قشم از عملیات انهدام کنترل‌شده مهمات عمل‌نکرده دشمن در برخی نقاط این شهرستان در روز شنبه خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/460106" target="_blank">📅 18:16 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460105">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVVD1UThQ9HhHBfg4kYBaqZ-KdoTB7gST19CWuW_FnHOHmSDywWmeT_zYu2ZECRPJLDk50H65AWlrDSaRttcFg0_SFcAniK1n0ytG8vDHg6YehX50pT_J5nIc7oBYXCr3NROQhAoDB70iPCJnaO9JWSdxeAvHmW_XeNNS87gcotgqcGnIQ4wGzQu0oUtwcE4G8D1XNifu5suBFpU72blgd0qvlwBQsLRuvFDnQ_bZWsGmDbl55gUdLqmqmIFzx7wYSda1rUdABPPvb_kBaAO6O6E-Y95lyBxgwnamtEdwq02Kum1blHKliikhY5y-071NV-sUYko5Ykc9rmWV6s40A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز: تلاش آمریکا و اروپا برای ارجاع پرونده هسته‌ای ایران به شورای امنیت
🔹
خبرگزاری رویترز امروز به نقل از دیپلمات‌ها گزارش داد که آمریکا به همراه سه کشور اروپایی موسوم به تروئیکا شامل انگلیس، فرانسه و آلمان در تلاش‌ هستند شورای حکام آژانس را در نشست هفتۀ آینده تحت فشار قرار دهند تا قطعنامه‌ای را تصویب کند که بر اساس آن، این نهاد آنچه «نقض تعهدات ایران در زمینه منع اشاعه هسته‌ای» ادعا شده را به شورای امنیت سازمان ملل گزارش دهد.
@ Farsna -
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/460105" target="_blank">📅 18:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460104">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">آمریکا ۳ نهاد مالی را به بهانه ارتباط با ایران تحریم کرد
🔹
وزارت خزانه‌داری آمریکا سه نهاد فعال در زمینه مسائل مالی و بیمه مستقر در ترکیه را به بهانه ارتباط با ایران در فهرست تحریم‌ها قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/460104" target="_blank">📅 17:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460103">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🎥
وداع مردم بهمئی با پیکر تکاور شهید در زادگاهش
🔹
ناوسروان سید مالک موسوی‌تبار در جریان حملۀ اخیر دشمن آمریکایی، در حین انجام وظیفه در خوزستان به شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/460103" target="_blank">📅 17:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460102">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhtZEwNLVUh274EBN-NwfPkhk_lug9L-ruzAQwtXI3duSSCwKQ57i0AmXKN8yYlK5pMRlskE-JnvY4H1TlulKW6M8E-CW_qAFjUC5U2Av6A_U62mhG7vQsO0N-UV90Ha96DN_W4-cB2lR_zTEmktEVtQd6mMPheUPqsRNnsixfIdAN6YAxA18hicx2KTDAQ-xxYBC_UrHP1p5q2gL59lUOnvnb0i_yL90AFn6XYIOw4e1B1ACLzn0Oy-ddHb-NI41tH4yCkTBHr6URVuJsGoRgS8iUn5_bjkqGQmOA3ysQ96jmbEQdLXBTWdAedKQLds4Mu6ozJSK-Xeeuv--ghXHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی: اقتصاد کشور را نمی‌شود در اتاق بسته اداره کرد
🔹
حدود ۲۲ هزار همت نقدینگی در جامعه سرگردان است و باید این منابع به سمت تولید هدایت شود؛ اقتصاد کشور را نمی‌توان در اتاق بسته اداره کرد و باید از تمرکز خارج و به مردم واگذار شود.
🔹
دشمن به دنبال شکستن تاب‌آوری مردم و ایجاد اختلال محاسباتی است، اما بیداری و حضور مردم در صحنه، محاسبات دشمن را بر هم زده و نشان داده است که سرمایه اجتماعی و حضور مردم، از عوامل مهم عبور از شرایط بحرانی کشور است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/460102" target="_blank">📅 17:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460101">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtJpHUMWopzN_KEocT18TsGeeCVLqEExuBs-P71NG-5plyfez8GnymmcOIVSVDQ_tBf-GGlHmOfS2e_mIv5sDqdA2udD6pp8dN-CQmwRs_HI5loG7g_DWs6uxYtVHROtvDQVPF11okq-lY1khblbebxRCINAr5fgvXp1o3BID0Vgv-vU7ahORW0fGDV7pK_tm_00bAfAy4zIt6NUe5V52qOXWHM3Bo6JeAvhbcjJLNpkBShx50howKOS5Z1vEbvzoOrNjEliaP9WutblqBdQGvT-qyAeblwitOR3KRg1NZ9RuQ-H_-TnFTlbwzmxKHADt83awNth1ioIvFCgVjzvUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاسخ اولیانوف به آمریکا: واشنگتن حق تعیین‌تکلیف برای روابط روسیه را ندارد
🔹
نماینده دائم روسیه در سازمان‌های بین‌المللی مستقر در وین اتریش امروز در پیامی در ایکس به درخواست آمریکا از مسکو برای دور ماندن از تهران، واکنش نشان داد و تاکید کرد «بدیهی است که واشنگتن نمی‌تواند به مسکو دیکته کند که با کدام کشورها روابط داشته باشد یا نداشته باشد».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/460101" target="_blank">📅 17:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460100">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOnBkKnzRDPYN9BEVnwdBILC1TeYPAcPR5wx8xWO_TuuqWneehX6k-CdiFo5oSdKqPMt2W5Oz7H3QCvhPoHVz4NsSNc_FhxKKLWuAW-KXI6UiUmtjQKHd5XD4cx0cYHYkLprLTYQ1flCnd172ahoWyl0-eloLnlHcHIROmPSSQMN0GRbbN3GBZ-V1D6LyX4QOBirTcxDn91uTja7HI8BxBM87td5V5ylaekqqxBWb3O5Dg0znSOL7c46zg0fdq8SH1fwZqINoWfHbn-AFR_Ck-BuGNhcmahCXvzx6V17sgCzfEkU-A-Onvr0quqxERG0zymIDmPDqdelSKSrBgNd1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی: متروی تهران تا پایان جنگ رایگان است
🔹
متروی تهران در حال حاضر رایگان است و شهردار تهران گفت که تا پایان جنگ هم مترو رایگان خواهد بود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/460100" target="_blank">📅 17:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460099">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXMae0CTLzxQguQzslQvX0W2_MbRwELPLgoiFaVftB7cZ_0Fr4NwqIgDtMDhX6-YvGWe7HAWNlD8R-DctykP5okFLrpq5JITRD5memsVPklOk02KhcwbEhiiE7WGuG5mNbQM8tN6jlfUre8O4NbbPpDwQaNLcD_EqPpNBQnzJFj6VasT9DjCtIhr0y9H5svXOhMM-8F1zxSDfkJveVinqHom45RFsbXsPM2pG3cVurLnTlBzx-LPyKdk_Z1xj3G3d9zfBbOe7Bwd0M8OcDHdSCcv5a5TTH6Z2qoV4KFf2S_hdIi3JTy9IHT62RM8jMOJk2TjD8XIz99oZHLOO-fNQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار عفو بین‌الملل دربارهٔ خیز اسرائیل برای اشغال کرانهٔ باختری
🔹
سازمان عفو بین‌الملل: رژیم صهیونیستی با صدور دستورات غیرقانونی برای مصادرهٔ اراضی کرانهٔ باختری، سیاست تشدید اشغالگری را در دستور کار خود قرار داده است.
🔹
اسرائیل از طریق مصادرهٔ اراضی کرانهٔ باختری، در حال گسترش شهرک‌سازی‌های غیرقانونی است.
🔹
صدور دستور صریح برای مصادره زمین‌های منطقهٔ (الف) که تحت کنترل دولت فلسطین قرار دارد، شامل این اقدامات است که بسیار نگران کننده است.
🔹
اقدام مذکور شهرک‌سازی غیرقانونی اسرائیل را بیشتر تثبیت کرده و باعث تضییع حقوق مردم فلسطین شده است؛ فقط در ماه ژوئیهٔ ۲۰۲۶، ارتش اسرائیل حداقل ۱۵ دستور برای مصادرهٔ زمین‌هایی به مساحت تقریبی ۲۰ هکتار صادر کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/farsna/460099" target="_blank">📅 17:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460097">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cf864b3c6.mp4?token=q8Bfkr7sFmAZHMNyMUO9zpmYw3qSIQnYCwrcfQ97tQXjkQwb_fkfMRkAY6RKGwhkzpk0Sf1Zg8JgbZgZTPAEaSKJaZEBlXxjyO0NTJ-j1TQzgvL8-ln8qmvL_QbNf6y7wGuPbM3hy5kIKEDDwdQtTEit5P8RaNFeLtv1a02cSvJrA7zrPV5qEd4q4ksZ44nMhhb4gGmg9gwVm59MmONdt5tjF2mDaSBj9RVjdIuKgFNgp-NwV4N5Bal-XfHBdiQcoU9XQvLJQdENh3A8Z2PruOsAaZ363Q2nGiB3y1mMY2SMQrV4puycheVzlEYVWaeLTAxIpc7YW9yfaDYUQpOzs4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cf864b3c6.mp4?token=q8Bfkr7sFmAZHMNyMUO9zpmYw3qSIQnYCwrcfQ97tQXjkQwb_fkfMRkAY6RKGwhkzpk0Sf1Zg8JgbZgZTPAEaSKJaZEBlXxjyO0NTJ-j1TQzgvL8-ln8qmvL_QbNf6y7wGuPbM3hy5kIKEDDwdQtTEit5P8RaNFeLtv1a02cSvJrA7zrPV5qEd4q4ksZ44nMhhb4gGmg9gwVm59MmONdt5tjF2mDaSBj9RVjdIuKgFNgp-NwV4N5Bal-XfHBdiQcoU9XQvLJQdENh3A8Z2PruOsAaZ363Q2nGiB3y1mMY2SMQrV4puycheVzlEYVWaeLTAxIpc7YW9yfaDYUQpOzs4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دست‌دست کردن رانندهٔ کامیون در لهستان منجربه تصادف وحشتناک با قطار شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/460097" target="_blank">📅 16:54 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460096">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxCAZQSwk_V0WFmacSJWXElkkCL7GuSrMiGKjp4tck9EKPbjk57vqyQ5a1AisDAluA0ZZSG8xPESbXy1F67H6kYjtYmN0LLbWi-azjmqNjcP_SFMkxOyMDLcXc3NfgEklNywLfrOrplsZgkjnja48pHWp7hIouFAtDRlq8KlSWnCKgxjiwFcTeoBndoZpsN6cKmws06XnVx8pyONsGOLIoSk7il2j7YBi4kGp6OABVoNiGb-VqrKWhvJ_H0QOGzqUjEvtm20_An2kU0QeRw1T9pJ-CGocrWkvQhlPvUnPedG2fbDuaH1LZoLz5358JSUKO10HSlkQg8loKGfiLRolA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرستادگان ترامپ عازم مسکو و کی‌یف می‌شوند
🔹
استیو ویتکاف و جرد کوشنر در حالی قرار است فردا و پس‌فردا ابتدا به مسکو و سپس به کی‌یف سفر کنند که واشنگتن مدعی است برای ازسرگیری مذاکرات ۳ ‌جانبه میان روسیه، اوکراین و آمریکا تلاش می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/farsna/460096" target="_blank">📅 16:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460093">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16a6c9629a.mp4?token=PkAtGOYGHXJidoWaA9UAaCijOL5ynNdNilQfzSi9v5CRuhJKWp2sG6kpNv1UMTp_bLXiwX7ztpeXK4gNnZimNIDspiovsfJxkzU44O_lS5TxlovzTbk83GdmuztNTQ41kyYEuPFKGHYe9D2JT3zGvjqf5X4H_W71RmPYJYtzcfOBJ8g07UXSaK8fKUb89ciDrtGLE1HZg8BZ9cyLaxLp0BVazPAg3ERPVeSBBYj31XLUj-JJYlleKdo8EqL7YguUeIA-2crUBXfE3o8p9P1oUnpHKnaDT2wftFTa1btZ6pnhdC6yY9qYjHcYjr5rTsWsn77vWFlsbYr4bXBHEsFilg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16a6c9629a.mp4?token=PkAtGOYGHXJidoWaA9UAaCijOL5ynNdNilQfzSi9v5CRuhJKWp2sG6kpNv1UMTp_bLXiwX7ztpeXK4gNnZimNIDspiovsfJxkzU44O_lS5TxlovzTbk83GdmuztNTQ41kyYEuPFKGHYe9D2JT3zGvjqf5X4H_W71RmPYJYtzcfOBJ8g07UXSaK8fKUb89ciDrtGLE1HZg8BZ9cyLaxLp0BVazPAg3ERPVeSBBYj31XLUj-JJYlleKdo8EqL7YguUeIA-2crUBXfE3o8p9P1oUnpHKnaDT2wftFTa1btZ6pnhdC6yY9qYjHcYjr5rTsWsn77vWFlsbYr4bXBHEsFilg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارتش: پاسخ به تجاوز احتمالی اسرائیل سریع‌تر و کوبنده‌تر خواهد بود
🔹
از بین رفتن سامانه‌های پدافند هوایی دشمن در جنگ ۴۰ روزه به‌معنای بازشدن مسیر حرکت موشک‌ها و پهپادهای ما به‌سمت سرزمین‌های اشغالی است.
🔹
اگر رژیم صهیونیستی دست به حمایت یا تجاوزی بزند،…</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/460093" target="_blank">📅 16:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460092">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4176b4afb7.mp4?token=pdY3DLd1S7egaPaKayQOKu6JZIMbylvD3JCv6hh_-DRWosWKHZ9NA2iLCMfk0PCMLfGK-Mll-_iUKuXqs03LSvmxSrsqbb__7Fv9v5qMq08cpcrZuZ0_ZcBS4v7nIDrHYjdU9OpToJPRAt0itrSZo1MkQab3LhAhjhA6DWI3IuOVd8Keu3xAuBT_NoGz9xKn6nEvUt73a8XnzvHd50THfQyFWAiRU9pGnhRxdaA7veFainy0m34YV1mj6q-Iv2K2zgn5RmnQsVdPfC2Af4V5Xgm_JEf6mIM1RlDE8hhN0NGJjKZWeBjoVkV2EzN3WO1Mzhsn0ok5JR6gT49qrM_dEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4176b4afb7.mp4?token=pdY3DLd1S7egaPaKayQOKu6JZIMbylvD3JCv6hh_-DRWosWKHZ9NA2iLCMfk0PCMLfGK-Mll-_iUKuXqs03LSvmxSrsqbb__7Fv9v5qMq08cpcrZuZ0_ZcBS4v7nIDrHYjdU9OpToJPRAt0itrSZo1MkQab3LhAhjhA6DWI3IuOVd8Keu3xAuBT_NoGz9xKn6nEvUt73a8XnzvHd50THfQyFWAiRU9pGnhRxdaA7veFainy0m34YV1mj6q-Iv2K2zgn5RmnQsVdPfC2Af4V5Xgm_JEf6mIM1RlDE8hhN0NGJjKZWeBjoVkV2EzN3WO1Mzhsn0ok5JR6gT49qrM_dEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارتش: هرجا احساس تهدید کنیم عملیات پیش‌دستانه انجام خواهیم داد.
🔹
دکترین نظامی ما پس‌از جنگ ۱۲ روزه به‌تدریج به این سمت حرکت کرده است که مطابق منشور ملل متحد باید از جنگ پیش‌دستانه استفاده کنیم. @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/460092" target="_blank">📅 16:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460091">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b9986a958.mp4?token=orx1vw2s03yHYWM0F1cikakgfYf8_TEKtqwajDt4cGyco9qnXGKTJBIIOfSnEXGMahSlJ2f0Kj9-lcHbuel1K6Dox4TZeO8EaDxfDxZzCC5nLVh3ri4G-smPqevwVg8vRBF544RWJAwkp2NdE6qGSNPFz7Ci2B4QO-gddq8e3WFGv2tsT4qI4ffTDxFq-2iUobKebSm3ksfW2ffIZxmvomyrc0yE8IQmkJp6_F3JWrp15SB0B3JV_BitUe9fegBcG6GsfrxZUz9wtGcfchtLlSgQLevjbl36mqbjAYQQ90rYlcySQxk7cGsU6jcKP8pWdQ8f7BCWAS2uBlfVIOXV9oPUhNQ31bGFBU_UnhpQp34z7LkRwXq0ef8amjt8iVg3__IKRKxPxmRtOYLdtdfKADXvQZSB3l4VgbNthUqdhseCKsRx2FUjPn6vXxLP6qEJ4oBW5VlmA99ZQNGjc3Ti7qWDayolcFMT-un3El3AaF-6zuOI55pXHK7_ovO0HMi8RdK-VyQS4KT36kaknX0LOCi9v_PVJBObq12cUZlF1Sqvue-oIl9_Sw8OfM7cm57SdoPQNlIrNp3pVicUHV1F4XLPX-AQ754Yz_ILlE3fRIRS-nXzq64cd7YT9QphwltONedOiFF6MkEFZ3EuUY__rE6yHJuSQFduJWDRxPPEJqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b9986a958.mp4?token=orx1vw2s03yHYWM0F1cikakgfYf8_TEKtqwajDt4cGyco9qnXGKTJBIIOfSnEXGMahSlJ2f0Kj9-lcHbuel1K6Dox4TZeO8EaDxfDxZzCC5nLVh3ri4G-smPqevwVg8vRBF544RWJAwkp2NdE6qGSNPFz7Ci2B4QO-gddq8e3WFGv2tsT4qI4ffTDxFq-2iUobKebSm3ksfW2ffIZxmvomyrc0yE8IQmkJp6_F3JWrp15SB0B3JV_BitUe9fegBcG6GsfrxZUz9wtGcfchtLlSgQLevjbl36mqbjAYQQ90rYlcySQxk7cGsU6jcKP8pWdQ8f7BCWAS2uBlfVIOXV9oPUhNQ31bGFBU_UnhpQp34z7LkRwXq0ef8amjt8iVg3__IKRKxPxmRtOYLdtdfKADXvQZSB3l4VgbNthUqdhseCKsRx2FUjPn6vXxLP6qEJ4oBW5VlmA99ZQNGjc3Ti7qWDayolcFMT-un3El3AaF-6zuOI55pXHK7_ovO0HMi8RdK-VyQS4KT36kaknX0LOCi9v_PVJBObq12cUZlF1Sqvue-oIl9_Sw8OfM7cm57SdoPQNlIrNp3pVicUHV1F4XLPX-AQ754Yz_ILlE3fRIRS-nXzq64cd7YT9QphwltONedOiFF6MkEFZ3EuUY__rE6yHJuSQFduJWDRxPPEJqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارتش: در عملیات‌های اخیر علیه دشمن از موشک‌های زمین‌به‌زمین فتح و پهپادهای آرش ۲ استفاده کردیم که مجهز به هوش مصنوعی بودند.
🔹
درحال‌حاضر عملیا‌ت‌ها را به‌صورت ترکیبی و نامتقارن انجام می‌دهیم که آثار بسیار مثبتی داشته و توانستیم به‌راحتی اهداف را مورد…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/460091" target="_blank">📅 16:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460090">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75ddce6d63.mp4?token=f_0derLBxDud0fLOx6VCY5592_OXg5D-NsvJvxZdXxk6DlmB6_VZyeh8VJx_YuyvoDS6Wk3NhWekylqYEXiCvED58EGLvA1rQ71DrAdB2CjRbuSdjb3lOArm7yrYLBibc5h96j5Zq1aW06xhpduMmGEk_TlJCu9PO282JEjy2kvZU3b_W1CFZAyepxnx8qQsKciKZjc8ZB2jVZ8MrqEmDVxqvzX_HphL74uwgbojfm9ao3vvoLcdrxYpDAiS4WqZ_o_RwjrlgXPRP0kvs0qPw-Qpny14azv_bMel-l5H3nhbw6_PXyK2qe2PKjUKwJ4tAgzOrluysW1ppZV6_kWx3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75ddce6d63.mp4?token=f_0derLBxDud0fLOx6VCY5592_OXg5D-NsvJvxZdXxk6DlmB6_VZyeh8VJx_YuyvoDS6Wk3NhWekylqYEXiCvED58EGLvA1rQ71DrAdB2CjRbuSdjb3lOArm7yrYLBibc5h96j5Zq1aW06xhpduMmGEk_TlJCu9PO282JEjy2kvZU3b_W1CFZAyepxnx8qQsKciKZjc8ZB2jVZ8MrqEmDVxqvzX_HphL74uwgbojfm9ao3vvoLcdrxYpDAiS4WqZ_o_RwjrlgXPRP0kvs0qPw-Qpny14azv_bMel-l5H3nhbw6_PXyK2qe2PKjUKwJ4tAgzOrluysW1ppZV6_kWx3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارتش: در کمتر از ۱۵ دقیقه به حملات اخیر دشمن در جنوب کشور پاسخ دادیم
🔹
آمریکایی‌ها سعی کردند کنترل نیروهای مسلح ایران بر تنگهٔ هرمز را تضعیف کنند که با پاسخ قاطع و کوبنده مواجه شدند.
🔹
در این عملیات‌ها پایگاه‌های آمریکا در سراسر منطقهٔ عربی، از اردن…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/460090" target="_blank">📅 15:56 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460088">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e7c7a6a7b.mp4?token=QuevQJczxhrlQqF04kkoZzWTFB-DUqXeHxflM6VtPQ6vOPPqXaJGrJBsVjOJl5dUsn1bvonESLWrHbJkUoUqeeH9EX4_np-lxgvNILCBAExLGNzhF9t8G3OPl6t2j5EDmxjLHZwoKd_iTzJAWHWvyFRI35pZWh-wcmWgrgVTQ1m6ep1nOHmHWYjEznj1AHFW_7YNh-iYl2tCUFNAE60OweNKPHAOMXsasf56KGljbSRERVVlnDM2OAgVsq4KV-tvsYs7NajT_4cNyIbZhHXYu_huPrPHIHAdinAFTzTp5zGC2d5atrceImss7B-QfMi4Ud2OaHAokTbp96uQj_LWGKUFXC3uB5rELRSXoUbYjEPrP80rDC7mXttRZYle17N36RwkuFdJlOfFVR6EbhAR38Ym9fQJYdwmUK0QJPmOHZsURvvgTuLZHJFDfzxdt51puX-mDeGx84y0LL9t4IMuNxWAfWvghStBNa7ru31dagGDyawQg6o5Fwd18jE5v63i_k4UFlJx3KkxprlnN6cYTLa-ER8DkweUteG4Q1V6eOfrbp-1i6WsmyE1lNt1EJRipA4rEViMEgTQBs3pGPJcRfq2jtbU_ZkKjJ1VIQnVt6RzTSv41sSDzNQXVq5iH0dKEBVE0PI_4nGR2sLQpcnSymPmmaTC9q-N0lX-rH1yv-k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e7c7a6a7b.mp4?token=QuevQJczxhrlQqF04kkoZzWTFB-DUqXeHxflM6VtPQ6vOPPqXaJGrJBsVjOJl5dUsn1bvonESLWrHbJkUoUqeeH9EX4_np-lxgvNILCBAExLGNzhF9t8G3OPl6t2j5EDmxjLHZwoKd_iTzJAWHWvyFRI35pZWh-wcmWgrgVTQ1m6ep1nOHmHWYjEznj1AHFW_7YNh-iYl2tCUFNAE60OweNKPHAOMXsasf56KGljbSRERVVlnDM2OAgVsq4KV-tvsYs7NajT_4cNyIbZhHXYu_huPrPHIHAdinAFTzTp5zGC2d5atrceImss7B-QfMi4Ud2OaHAokTbp96uQj_LWGKUFXC3uB5rELRSXoUbYjEPrP80rDC7mXttRZYle17N36RwkuFdJlOfFVR6EbhAR38Ym9fQJYdwmUK0QJPmOHZsURvvgTuLZHJFDfzxdt51puX-mDeGx84y0LL9t4IMuNxWAfWvghStBNa7ru31dagGDyawQg6o5Fwd18jE5v63i_k4UFlJx3KkxprlnN6cYTLa-ER8DkweUteG4Q1V6eOfrbp-1i6WsmyE1lNt1EJRipA4rEViMEgTQBs3pGPJcRfq2jtbU_ZkKjJ1VIQnVt6RzTSv41sSDzNQXVq5iH0dKEBVE0PI_4nGR2sLQpcnSymPmmaTC9q-N0lX-rH1yv-k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارتش: در کمتر از ۱۵ دقیقه به حملات اخیر دشمن در جنوب کشور پاسخ دادیم
🔹
آمریکایی‌ها سعی کردند کنترل نیروهای مسلح ایران بر تنگهٔ هرمز را تضعیف کنند که با پاسخ قاطع و کوبنده مواجه شدند.
🔹
در این عملیات‌ها پایگاه‌های آمریکا در سراسر منطقهٔ عربی، از اردن تا امارات، مورد هدف قرار گرفتند.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/460088" target="_blank">📅 15:39 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460087">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4a03d5c8d.mp4?token=Y5ZdS_rbrbVQdtij44w310tV0NbbogFUt8U5WAAPVuKSnzs0ph7u-HN2KBIRcV5v0kHh_W1PR7A4y4gYOfrZzOEx-_v2rAwYZ638OnbCSUnk8z8OIRVGXtbVGUSN0hE65Az1cqn53eT7P4dFdBM1ki3e1980_zX-7oOIEIOZ3rQbiZou8ZCLObgaw8zKTttwbOc8-zrOSeoEz3XiuelwyUVPB1A9c2mCDEiEPPOVv5Ka2HtyYFpTGoMSDWyN_EAF0mDB-HPGP3jFQXaV52MVnyli1bczOoGQq5BslcTKASM_r5iAXIOD6haQ4n2BJZwqK8BJZ9zRhLRRMy1vabvgOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4a03d5c8d.mp4?token=Y5ZdS_rbrbVQdtij44w310tV0NbbogFUt8U5WAAPVuKSnzs0ph7u-HN2KBIRcV5v0kHh_W1PR7A4y4gYOfrZzOEx-_v2rAwYZ638OnbCSUnk8z8OIRVGXtbVGUSN0hE65Az1cqn53eT7P4dFdBM1ki3e1980_zX-7oOIEIOZ3rQbiZou8ZCLObgaw8zKTttwbOc8-zrOSeoEz3XiuelwyUVPB1A9c2mCDEiEPPOVv5Ka2HtyYFpTGoMSDWyN_EAF0mDB-HPGP3jFQXaV52MVnyli1bczOoGQq5BslcTKASM_r5iAXIOD6haQ4n2BJZwqK8BJZ9zRhLRRMy1vabvgOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تلفات سیل نپال و چین از هزار نفر فراتر رفت
🔹
تعداد تلفات سیل مرز چین و نپال به ۱۰۰۳ نفر رسید و ۴۴۶۲ نفر از جمله ۸۴۴ تبعهٔ خارجی همچنان مفقود هستند. @Farsna - Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/460087" target="_blank">📅 15:24 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460086">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qn5AlHGhYchdv6rnEa6IIU9IwaMiZg2ST8wxvS1kgoO6RkdBYMKJkTEvjyD6mDhmi7ue1dpkNXGG_EZ-wMj1rI2NdDR1Jfd0CJVoGVh0WTMyRzm4CzMpy_LzW28P30VDzSdd8WJwfUIJO8cWN-ZRiWAbOWq4cyPp8ys0EBWoOW081qoG3vu-Ws92k6MkyyOyA75PElwU-lZfn2NK4PZApSKynK629-U9_LN2jSWWfi0ZrvSGbEYgpIIAVtxYAUaA4PFo3_Rhv59_UgwS6Ng0WQ8QXB3qmFvoVe4FkzHizuBdC3128D3QUukGMcoiYM4iwK35-QqEnKcI3CwkoSygKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
افتتاح بزرگترین و مدرن ترین تم پارک ایران در مجموعه ارم با حمایت بانک شهر
🔹
طی مراسمی با حضور جمعی از مسئولان و مدیران حوزه گردشگری؛ بزرگترین و مدرن ترین تم پارک ایران با نام «دنیای گمشده» در مجموعه ارم، و با حمایت بانک شهر به بهره برداری رسید.
🔹
به گزارش روابط عمومی بانک شهر، احمد مالکی معاون اعتبارات و وصول مطالبات بانک شهر در این مراسم که با حضور معاون وزارت میراث فرهنگی،گردشگری و صنایع دستی، معاون بنیاد مستضعفان انقلاب اسلامی و برخی از مسئولان کشوری و لشکری برگزار شد، گفت: بانک شهر با سرمایه گذاری و مشارکت در پروژه های تفریحی و گردشگری گام های موثری در راستای گسترش فضاهای تفریحی مدرن و ارتقای کیفیت زندگی شهروندان در محیط‌های شهری برداشته است.
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/farsna/460086" target="_blank">📅 15:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460085">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromشرکت پارس خودرو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UuxAnRUrDndgISjXaoEMKc8Mx1JtT6a1cb4ewESUBV1U3EhCu1tKxarnlj6K2aw-dNiqVbQyxjw_z4L5lPwIUTkLoTHLBu2LWEL8IQNLGpTbtBw9_Jg5qvKWexZf5DiDnqRbbNAOz7kTlfHCPJx0JDOeE7BWKrAM8xcdN6WdA8F16URZgGWjDaVbp8m_OfkrYZiATfVB0E0eJP6LVCAgRUYxf49oOjpKFl-69HWAmnrFGaS0mCdVHquePr14gmYJFC0sQIbyK3ssUvps76ydI6dsqnGX9ADxVFQ8b3qSr-JiFhxhwYIjJzS0aGwDZ17qMKqfTCcUoh4469Vejf6S_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◽
رشد ۶۰ درصدی ارزش سهام پارس خودرو در یک ماه گذشته
◽
حرکت پرشتاب به سمت افزایش تولید و ارزش آفرینی
🔻
سهام پارس‌خودرو در معاملات یک ماه گذشته با رشد ۶۰ درصدی قیمت همراه شد و در این مدت مورد توجه معامله‌گران بازار سرمایه قرار گرفت.
مشروح خبر:
🔗
saipanews.com/news/id/24634
🆔
@parskhodro_pk</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/460085" target="_blank">📅 15:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460084">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/460084" target="_blank">📅 15:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460083">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYfK88viWClHnvFTpJ7IU-gHjsysOtpSJOuVuK2pWsMeEKvSJ8fnFGb8-ah5Lh6zredQ3rzKwWk8qoLOPhOCmeXNFwbq3oomCVXXloZ_jFyavIWYEoo0PBM1zNdA53ovMsRp99JjlHk3MnE4VvnbldTAQRoDAEz127DQJZ-xwR0E78cUPvEln5EcDCNeJbcZ_tUkMkIhUnqfEImQp1_WEIJ0mrggKl_Ru4tbi7akWF0AFGCfzLGhvwYcBDgp9DzsFS-TGzgBlRR4rAw1A4MDjj4d1gp4IPApeAeLv-Gr7zEHmEcNeh2CNBnUvWY2JdeThCJ5ErU3mUSK6GkFUWqAkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی ارتش: راهکار مناسب برای آمریکا پرداخت هزینه‌ها و خروج از منطقه است
🔹
امیر اکرمی‌نیا: معضلات ارتش ایالات متحده در منطقه و مشکلات مردم این کشور، ناشی از اشتباهات مسئولان آمریکا در تجاوز به یک کشور مستقل و متمدن است.
🔹
راهکار مناسب برای آمریکا پذیرش واقعیات، پرداخت هزینه‌ها و خروج از منطقه است. این کار منطقه را امن و مردم آمریکا را به رفاه نزدیک‌تر می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/460083" target="_blank">📅 15:16 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460082">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xa_Y7Wa9w0c2OsBVjTHD4KU6fnmFzXl1icpxBJ6fYEFdV5dxWPH5sRyeF-YcTnkQmK-AwZHVORrzd0cyQ38XTsl3DblPKGmdXykqeHNLyV4Bue0SmjguanT-Gke1DhdOlJb04equUyT_ioSOcnKnLSXKzRaqLkNntTbwxQ6xshgBIt5Cosn6cjMmc4P9XYGauVKLVBx5MGSvQk49tBqfnQ-1kUVgYD7dNn2N8utZ_I3fItaMutG1BNdQS1aM-wgVbj9l1foHtu5nQYxZqhIEfEwn3PtJCpPe1QDSfPfRKjinEsLjmltZVgQtTS1t-QxqaTuEz3zMydqljMdbr9PhdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سناتور آمریکایی: وزیر جنگ دربارهٔ حمله به جشن عروسی پاسخگو باشد
🔹
کریس ون هولن: هگزث تلفات غیرنظامیان را موضوعی فرعی تلقی می‌کند؛ نیروهای مسئول جلوگیری از این تلفات را کاهش می‌دهد و به نبودِ قواعد احمقانهٔ درگیری افتخار می‌کند.
🔹
باید دربارهٔ حمله به شهر سیریک تحقیقات کاملی انجام شود و مسئولان آن پاسخگو شوند؛ همچنین باید همین حالا به این جنگ فاجعه‌بار پایان دهیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/460082" target="_blank">📅 14:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460081">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f32f681c97.mp4?token=fXr0xx7JEuviM0s0lN7da2SCAfsiKDv84RuHJFuuhknfFTbsjZJ6W-OpzZ5G5jQQXhkKysesbXxDplgdsViMXkbh6MzseDekfWlSe8jCIxSu9mpwpsja_A7cVlVrc5_1gcrROMQQTgEzYnOe1U5SbeU3bHwfbXlgDIlwKizf8RWqKTouNOuomNwBlJvoLTs2TgFCb-_PLzUKRUpevZ2c43VZb2bC0wZm9MJyDOn9947x5R6RP6NPsbI8Fnw7gd2mYRlF8WQcGoxj4MNRiKHJSkK1qkdnPNf2qfWGrT8A19JhROzI4gORlxL2U0kaCPMKSVqMrdlk-uUMUjrcoKlMzTMKOhuZWl9JE4aNyzjnXyyIWEH75bVKL-bTYGl5XTevfDZtx_Rzr05kpjlummPReXCJmodFIP8fWiqLtzy4q9CueAsSMwGtiv12rcbV9sNLHwLTUQoCXYpRE0DPDDvvE3FqfganvPGidUISZysOEUMcH_f_SecwImffusIoDFjqP8f8fVHVVwBJoglqK0J2R1ovrL6U6r9MVoaC2WRh09T9uoqL55DH-ORTzds_KuiDlV1fIG1-wXFrlKg1yH8xHEKyqv6xAJId1w2y1mwPD3McKjFNptPFsL-fLqneR5e8ISKekAt8o15q093zN1-MlEgTOPJpLD45Gqmq13mYcHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f32f681c97.mp4?token=fXr0xx7JEuviM0s0lN7da2SCAfsiKDv84RuHJFuuhknfFTbsjZJ6W-OpzZ5G5jQQXhkKysesbXxDplgdsViMXkbh6MzseDekfWlSe8jCIxSu9mpwpsja_A7cVlVrc5_1gcrROMQQTgEzYnOe1U5SbeU3bHwfbXlgDIlwKizf8RWqKTouNOuomNwBlJvoLTs2TgFCb-_PLzUKRUpevZ2c43VZb2bC0wZm9MJyDOn9947x5R6RP6NPsbI8Fnw7gd2mYRlF8WQcGoxj4MNRiKHJSkK1qkdnPNf2qfWGrT8A19JhROzI4gORlxL2U0kaCPMKSVqMrdlk-uUMUjrcoKlMzTMKOhuZWl9JE4aNyzjnXyyIWEH75bVKL-bTYGl5XTevfDZtx_Rzr05kpjlummPReXCJmodFIP8fWiqLtzy4q9CueAsSMwGtiv12rcbV9sNLHwLTUQoCXYpRE0DPDDvvE3FqfganvPGidUISZysOEUMcH_f_SecwImffusIoDFjqP8f8fVHVVwBJoglqK0J2R1ovrL6U6r9MVoaC2WRh09T9uoqL55DH-ORTzds_KuiDlV1fIG1-wXFrlKg1yH8xHEKyqv6xAJId1w2y1mwPD3McKjFNptPFsL-fLqneR5e8ISKekAt8o15q093zN1-MlEgTOPJpLD45Gqmq13mYcHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نفت: برای اولین‌بار به صادرکنندهٔ گازوئیل تبدیل شدیم  @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/460081" target="_blank">📅 14:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460080">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzxzIYWYu1JaEVRcwaZ_AKN6uXTImtbRI_Lg4bZnstjvJP0n3mxkHj2duG6hUngS0H7_gtHYZpzhv2mYZmh7iP1NiiRbumC1-xMPeiJ82UAHNPBleEd_iHXsNqb_xU8Zvyn6882dGW9-f_0QzGz4uj0RloH-QdGpGtmrPX85lLYZMFRndLHRCvYWt4YcTxLTD_iX6OeGXDKMRv8Bkw6AQqFuwUO7qErLbFmbwmo6Jv6XzubVpCplvMebbCI5aAGHGDFeSAkz6IQet8cCc83IbZbuKun7KE5wmTotZsPC7o4qp-RD-lLMs4PafkBPSV7CtpfPBqiXTm5JPFt6fPbIRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت یک مرزبان در درگیری با گروهک ضدانقلاب
🔹
فرمانده مرزبانی کرمانشاه: گروهبان‌یکم مرزبانی «رضا دارایی عمارتی» در جریان درگیری بامداد امروز مرزبانان هنگ مرزی پاوه با گروهک معاند و ضدانقلاب به‌شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/460080" target="_blank">📅 14:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460079">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">جاده‌های مازندران یک‌طرفه می‌شوند
🔹
پلیس‌راه مازندران: از ساعت ۱۴  مسیر جنوب به شمال آزادراه تهران-شمال و جادهٔ کندوان مسدود شده و از ساعت ۱۷:۳۰ تردد از خروجی مرزن‌آباد به‌سمت جنوب یک‌طرفه خواهد شد.
🔹
در جادهٔ هراز نیز تردد به‌صورت مقطعی به صورت یک‌طرفه انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/460079" target="_blank">📅 14:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460078">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04dc114a09.mp4?token=nOh3Nh4IHklKWPdiGZXyn2rjCcNpZ4e2128cvrfrUZvdI8IHQWSg-9jubzUplUlg584ECUIXkJmcw8AWNVhPv35IdtIpMFcZPQKyrG5VhLThFmFFW-YG0CcNLOuxnw3MkLcJPa5_2ISGiq0OY6uJD6zj4E1Y1NV3_cfbQ7xKTiVq4gqFrRozNByQG9oMSrLHi9AcIU8w1ak0K33tFjY_s5kCEvsYGfmHQWt2iluAcKBQMx31365VPO-zBdg_U9PYTLHUjySeIA4gNZ5N7zS0W86u8S4311VM9_utQFrZfMMnrWRQ20qoZKxhx6tlS9CsEsWKVdyLzdkrJNsVoWNVkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04dc114a09.mp4?token=nOh3Nh4IHklKWPdiGZXyn2rjCcNpZ4e2128cvrfrUZvdI8IHQWSg-9jubzUplUlg584ECUIXkJmcw8AWNVhPv35IdtIpMFcZPQKyrG5VhLThFmFFW-YG0CcNLOuxnw3MkLcJPa5_2ISGiq0OY6uJD6zj4E1Y1NV3_cfbQ7xKTiVq4gqFrRozNByQG9oMSrLHi9AcIU8w1ak0K33tFjY_s5kCEvsYGfmHQWt2iluAcKBQMx31365VPO-zBdg_U9PYTLHUjySeIA4gNZ5N7zS0W86u8S4311VM9_utQFrZfMMnrWRQ20qoZKxhx6tlS9CsEsWKVdyLzdkrJNsVoWNVkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نفت: صادرات نفت در زمان یک ساعت هم قطع نشد
🔹
بیش‌از ۵۵۰ اصابت به جزیرهٔ خارک داشتیم؛ همکاران صنعت نفت زیر بمباران بارگیری می‌کردند. @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/460078" target="_blank">📅 14:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460077">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CiyJ29QZyFvCcHdbfqrR9Q_ZtX6DFpHoPSdlWvLJpJypzAZcaFU1gUSI01ZPUkcm1InDSv63QiD9x2MZEyR_8Rhyfd3tH2BABJ2xyRAvqs5mnZMmNIqsr6lTiDkwuO8mr_Pr5JvP1X2wH-53qWQnNtXYiJYo_1iyjmBVrA9Eu1yuLOWQRGQZyuaXqDW2dML7UV2RKtubwQyyhsJxH0nrsn3z1G8qh78tfgHNZvSm2QaUOY3GQCV7oqBjgYLeSSH6Bq-XQpHrAYuHZ0w_C9uMv7eHz2-zbmbwCSEiVXjvI4526eX3Jf1URNhyeUW_U-vewyFMlhPBaAmR809uX3RAEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: منابع حاصل از کاهش مصرف بنزین صرف تقویت کالابرگ خواهد شد
🔹
رئیس‌جمهور در جلسهٔ هماهنگی مدیریت ناترازی انرژی: سیاست دولت، مدیریت و کنترل مصرف با استفاده از ابزارها و سیاست‌های عمدتا غیرقیمتی است و به‌هیچ‌عنوان نباید تصمیمات این حوزه به‌گونه‌ای اتخاذ شود که جامعه با رفتارهای ناگهانی و شوک‌آور مواجه شود.
🔹
اطلاع‌رسانی شفاف، دقیق و به‌موقع به مردم پیش از اجرای هر تصمیم نیز باید به‌طور جدی در دستور کار قرار داشته باشد تا ضمن افزایش آگاهی عمومی، زمینهٔ اقناع و مشارکت مردم در اجرای برنامه‌ها فراهم شود.
🔹
هر میزان صرفه‌جویی و درآمد حاصل از کاهش مصرف بنزین، صرف تقویت طرح کالابرگ خواهد شد و محل مصرف دیگری برای این منابع در نظر گرفته نخواهد شد.
🔹
مهم‌ترین دغدغهٔ ما، دغدغهٔ مردم است و در تمامی مراحل اجرای برنامه‌ها و تصمیمات، از جمله موضوع سهمیه‌ها و مدیریت استفاده از کارت‌های سوخت جایگاه‌ها، باید به‌گونه‌ای عمل شود که نارضایتی و فشار مضاعف بر مردم ایجاد نشود.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/460077" target="_blank">📅 14:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460076">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b853d23c51.mp4?token=Z6kpkb8SfH6Yji3DE8Vj6vVlm5M1wohaOJyVMzBoRqWEfG7iaIdb0dWVdKubQ9G8mK8a8XI4cnGwh35EH-oAJO4IRPcMJ7RkskjKpC28skzVXtuuNUYg08C6GEyVTq09h_g8txRGtwoYxMTu3S21FgiGEBtBAgjNmJ7QePBV0jkz1OWKeMNynJp08lhTT8fC6jIClB0kvAsWQ67yrCSfP0Xt3b8okesXy9VepLI90U6QAWalgF9cFWdZqqewfCK0uIxG6VKyHmglTm_K8tzBMg77pN3Gq_mGkMhJIUyAfNMFYXbrBQazPPmsl-Czw_UIiJXKnRjMFFV_weUukvSExYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b853d23c51.mp4?token=Z6kpkb8SfH6Yji3DE8Vj6vVlm5M1wohaOJyVMzBoRqWEfG7iaIdb0dWVdKubQ9G8mK8a8XI4cnGwh35EH-oAJO4IRPcMJ7RkskjKpC28skzVXtuuNUYg08C6GEyVTq09h_g8txRGtwoYxMTu3S21FgiGEBtBAgjNmJ7QePBV0jkz1OWKeMNynJp08lhTT8fC6jIClB0kvAsWQ67yrCSfP0Xt3b8okesXy9VepLI90U6QAWalgF9cFWdZqqewfCK0uIxG6VKyHmglTm_K8tzBMg77pN3Gq_mGkMhJIUyAfNMFYXbrBQazPPmsl-Czw_UIiJXKnRjMFFV_weUukvSExYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نفت: در تلاشیم تا محاصره را به‌طور کامل دور بزنیم
🔹
در زمان رفع محاصره، نفت را به آن طرف دریای عمان منتقل کردیم. @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/460076" target="_blank">📅 13:54 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460075">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/697c3ea5cd.mp4?token=NY-lfqulfL1I_3sQNfD_kaP5X-djAUyN-9LnPz7HoyXTk2yvEYteLkxZfRlenzyFHlGtm3W_6hraAQ5COgzOqpI1x9HN6W-6Fwh2j2ZUKMRFjB1W_9l44NL9MV-YLsrvahLE-DYKIPhux8Yt7ftqQs9bBkN31M_s7sHH33tcsn-PFg-Y4AMYs-PL5v_LyK0X-jNHQnshKhqKN8fGVnJoTXXqEHZFueSL7FNs7ScX-GwBvU02nHfM84geJQHyGrKKE6M9RguZwqpLuKMZQJJ1bqLuLnOphIQ8ymIoDx8xHI_MjvbYC_JBq7JOFBy_zs255c_4WYniJguIImLHlVLWXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/697c3ea5cd.mp4?token=NY-lfqulfL1I_3sQNfD_kaP5X-djAUyN-9LnPz7HoyXTk2yvEYteLkxZfRlenzyFHlGtm3W_6hraAQ5COgzOqpI1x9HN6W-6Fwh2j2ZUKMRFjB1W_9l44NL9MV-YLsrvahLE-DYKIPhux8Yt7ftqQs9bBkN31M_s7sHH33tcsn-PFg-Y4AMYs-PL5v_LyK0X-jNHQnshKhqKN8fGVnJoTXXqEHZFueSL7FNs7ScX-GwBvU02nHfM84geJQHyGrKKE6M9RguZwqpLuKMZQJJ1bqLuLnOphIQ8ymIoDx8xHI_MjvbYC_JBq7JOFBy_zs255c_4WYniJguIImLHlVLWXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت وزیر نفت از شب حمله به انبارهای سوخت در جنگ رمضان و نحوهٔ مدیریت پیامدهای آن  @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/460075" target="_blank">📅 13:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460074">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6058e3237.mp4?token=NlaXj3eSfyIDtUDr12RkugtoZci1AJF27tFIBB55Qwuap3ARTOdBSLBaIx2IkC1vOl2o65QN1wRPzaSb42lbSh6BNPN6DwOiPbuCwardBtA2VYyN_tvEB3ikASkiE675-XLjGN1zr4MH6NPXXfiVLqOt000AlLQ1qHr5vScF298UinxycN4xmr5mOsavz8If-7CRI48hGkPsk4QbNtsaAF0QgBA4Km_lqsIlXrhY5oRJLJp8B1Leh6Ae59JyqmephH_xs4YAYfELJWgOR9blq0JYUx2CitQHiQ1qM6hss95HCdGxeIPlfpWnUjbk-dyLBhhktR6zAYC-ksmlTa4rZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6058e3237.mp4?token=NlaXj3eSfyIDtUDr12RkugtoZci1AJF27tFIBB55Qwuap3ARTOdBSLBaIx2IkC1vOl2o65QN1wRPzaSb42lbSh6BNPN6DwOiPbuCwardBtA2VYyN_tvEB3ikASkiE675-XLjGN1zr4MH6NPXXfiVLqOt000AlLQ1qHr5vScF298UinxycN4xmr5mOsavz8If-7CRI48hGkPsk4QbNtsaAF0QgBA4Km_lqsIlXrhY5oRJLJp8B1Leh6Ae59JyqmephH_xs4YAYfELJWgOR9blq0JYUx2CitQHiQ1qM6hss95HCdGxeIPlfpWnUjbk-dyLBhhktR6zAYC-ksmlTa4rZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
مردم سیریک با شهدای عروسی کوهستک وداع کردند  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/460074" target="_blank">📅 13:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460073">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4303f11b4.mp4?token=f0N2If2qUfX5Ns6O3CeKjMgXoOLCvT5nijz3cDVD0XEkf_tyaXNkIVDxWCrDMiK5NjRjGWn9JSMTSZLyXIPjtujmliyjR27Zq1yG9nUuFUmWX-31Xyr20SKpioqa7V-i61c1kIGI2oQjxqf_9lXyFVOn4tDlMiTu7aih9PZCvIuNT5zAZDVrLTn2HUFkOjjZwAbkcZ3-ErliVXWEwOt42soDzE5KNqdKH6ViTSMEQFIbY1vRhpd883LCBY1x5cpSTHhXNtcqTQy3TOBTVs_quoPD1qxrSixwDte4zGywCvah4d2IXtqNSwG1Dgo1dmbKFFsTM0jOgCl_Yv45J8u75zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4303f11b4.mp4?token=f0N2If2qUfX5Ns6O3CeKjMgXoOLCvT5nijz3cDVD0XEkf_tyaXNkIVDxWCrDMiK5NjRjGWn9JSMTSZLyXIPjtujmliyjR27Zq1yG9nUuFUmWX-31Xyr20SKpioqa7V-i61c1kIGI2oQjxqf_9lXyFVOn4tDlMiTu7aih9PZCvIuNT5zAZDVrLTn2HUFkOjjZwAbkcZ3-ErliVXWEwOt42soDzE5KNqdKH6ViTSMEQFIbY1vRhpd883LCBY1x5cpSTHhXNtcqTQy3TOBTVs_quoPD1qxrSixwDte4zGywCvah4d2IXtqNSwG1Dgo1dmbKFFsTM0jOgCl_Yv45J8u75zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی و توپخانه‌ای صهیونیست‌ها به جنوب لبنان
🔹
منابع لبنانی از ۳ حملهٔ هوایی رژیم صهیونیستی به شهرک المنصوری در جنوب لبنان خبر می‌دهند.
🔹
توپخانه ارتش رژیم صهیونیستی هم اطراف شهرک النبطیه الفوقا‌ و کفررمان را مورد هدف قرار داد. @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/460073" target="_blank">📅 13:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460072">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EK-HS5awr-F8iViZrU_FaInX5X54xZn5-FSYkbVCsF8_Godr7SnLaW7q45Fhk3fFtybJLXt4HzyWae76e0-F5heUkNVBQqXP5IXZXpW242lFYlTjE8T3dbD9ZMVKICax04yMlU6ZwklyzUWaS5sFWLn_nvJrdVLEyzAczl_4t6-x_8-MpVNmSaBbnJt_rKftfQk_jODgrwPLcFBRNGFkI7tuq7kQOuDc-_05KaeChdE_0X91CdG34rz7tvVG4hoXA5pULLNFYPTlP_c7GvIO6eNWAsOTJp0Uc9YGjhjgCn-HNN-SwhEIstXF8E_W_mNRyJ9RAv5Tgwh-KRlPe36E6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطیب جمعهٔ تهران: فشار اقتصادی علیه ایران شکست خواهد خورد
🔹
آیت‌الله خاتمی: از قرآن استفاده می‌شود که فشار اقتصادی موضوع تازه‌ای نیست که ترامپ به اصطلاح خودش آن را آورده باشد؛ بلکه از آغاز اسلام این فشار وجود داشته است.
🔹
همان‌گونه که دشمنان صدر اسلام شکست خوردند، تحقیقاً این‌ها نیز شکست خواهند خورد.
🔹
مسئولان نظام باید با کار جهادی بکوشند مشکلات اقتصادی مردم را حل کنند یا دست‌کم کاهش دهند.
🔹
هیچ‌کس در این نظام حق ندارد سخنی بر زبان بیاورد که بوی ضعف و ناتوانی از آن استشمام شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/460072" target="_blank">📅 13:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460071">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhZCkeF_fU_QkzPirZ0bZsYVYvTc6hXHXHvX5PEtV7iAk61Gl5lKbiEnYIKEcn2X8no_7QQ0m9S-CEEGhHdSb4RallpZ-EKtAhItVauML7ybqYBUMvMRR8otne8C3sKQE4M5VaDDXFkVqYaFWQOAZLKoNN-C5kZhO_tcthyvVdU61GlzoIEYZiDz5hYm3CV23EHAJPzPE-JX4CqG3x4B2YZD7uUlZuHVsCW92-QX9qgfUIxqqeQFqo0frlAhXRuEYinoWkdPcMwq7Mj5LpQ6XN6ZUre6nYxCYRHlwqjcmQwBnMUpFUqE346Fy6nDBEAZdrmRLb62V8ez85hfh-0PMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۵۰ کیلو مخدر شیشه در آذربایجان‌غربی
🔹
فرمانده انتظامی آذربایجان‌غربی: در بازرسی از یک خودرو، ۵۰ کیلوگرم مواد مخدر شیشه کشف شد؛ در این راستا یک نفر دستگیر و خودروی حامل مخدر توقیف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/460071" target="_blank">📅 12:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460070">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RyYenCqZguxfYMd095j5LDWwTAgFiqP13wSELLNEiM2snMrat-pR418V9SY211ZQ-j2TnB_CSssQSok0c7LtOhOnmLubz0T8G3pRX_fJEJtIFHlxGbTYf4-fD4xzcekwTIHjiL9GyNBfkYQ4O1P5VccCdQDzU5ZoRMMEKE-tcNAQK1Cv1gLUylHbEglYIDtLRG0H4etLjX5ufKjo6IPjhgGXHRjzk_UdnIYk2pniihIzBhLSLvpNUyRfTfJP2AcagQQddMGTwHYwmOK15mLGhf5j8-PgLOj72fNZTHr_4Xq16Dq4xS6CtLgRAjlvM2RMLi8_c_iB-bki4bXK5TFz1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر الهامی: برای هر نوع تقابل آماده‌ایم
🔹
فرمانده قرارگاه مشترک پدافند هوایی خاتم‌الانبیا(ص): ایران با آنچه در جنگ‌های اخیر از خود به‌نمایش گذاشت، تعریف جدیدی از قدرت ملی به‌دنیا عرضه کرد.
🔹
نیروهای پدافند هوایی ارتش و سپاه در جنگ اخیر سامانهٔ پدافند هوایی تولید کردند، آن را توسعه دادند، در میدان مستقر کردند، از آن بهره‌برداری کردند و هواپیماهای دشمن متخاصم را نابود کردند.
🔹
پدافند هوایی کشور با تکیه بر توان داخلی، دانشمندان جوان، شرکت‌های دانش‌بنیان، دانشگاه‌ها و تجربیات میدانی نیروهای مسلح، در تأمین تجهیزات و سامانه‌های مورد نیاز خود به خودکفایی کامل رسیده و جنگ را اداره می‌کند.
🔹
خود را برای هر نوع تقابل در امروز و آینده آماده کرده‌ایم و آماده خواهیم کرد؛ زیرا می‌دانیم تهدید تمام نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/460070" target="_blank">📅 12:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460069">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPDdjE--GSs6eccXKRF-bi9U38YVmZXHd05_5rVIC0pydH0eXG2MNClOuvzqyzIki87UVNPFqimR5ihWWsUyhrzyXjZxoupZaiS5fhPGJ8zbCKBPPG8afJ5EaKJp6Jea3adlVQ45taJeI-B-VTNK600YClo2d9H-58a4U8PNt4LIIiiuvJUvn0CI-EAfGG4gS_OOH81xL8GFXCQP4l1Xc7dkTnc9E82IzehKYP1MSPjucaG8AeHax1YhkUYlk4893DpXBKdDCmUoKug-AefklZUpj9ZQ_g2A93OHsWd2tj0aXAOWR7Wn79FiUdrfaMAAG-CNK4NJ2Sl59ZeEeUZ38A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون فرهنگی سازمان بسیج: ۲۹ هزار گروه مردمی، پای‌کار میدان‌اند‌
🔹
سردار مقواساز: استقبال مردم از «میدان‌یار» بیش از پیش‌بینی اولیه بوده و مردم با خلاقیت خود به گسترش آن کمک کرده‌اند.
🔹
تاکنون نزدیک به ۲۹ هزار گروه در این طرح ثبت‌نام کرده‌اند و پیش‌بینی می‌شود این رقم به ۱۰۰ هزار گروه برسد.
🔹
هدف اصلی این طرح آموزش و آمادگی عمومی مردم است؛ میدان‌یار صرفا مسابقه نیست، بلکه یک حرکت عمومی برای آموزش مردم و افزایش نقش‌آفرینی آنها در میدان‌های پیش‌روست.
🔹
این طرح در ۴ محور آموزش‌های نظامی، امدادی و خودامدادی و دگرامدادی، فرهنگی و هنری و رسانه و روایتگری اجرا می‌شود.
🔹
حضور بانوان، خانواده‌ها، نوجوانان و اقشار مختلف در این طرح چشمگیر بوده؛ قرار است گروه‌های تشکیل‌شده پس‌از پایان مسابقات نیز در محله‌ها و محیط‌های اجتماعی به فعالیت خود ادامه دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/460069" target="_blank">📅 12:06 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460068">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7xsdmUAA0hVjSX0NmNekjWy9Nec03icJOXZaLQHdxui1APBIHeNLuIayL3MP2EdsjqHIHIpst9z7obxRg011fg9uMySjvwlbs18GWohz6s4FTS3_LsUpm8e7JWeJBnRs2FogI-wRrmURGbbK2ZARK2_jM6qdXT1Q-G6SVUI9PyPN3KKQQqG-zey_NEqzwl94rqaQ5-2kacBCwpGfvAeTJLbkpU-0mTeukC0aXfB5ODQQiICJQqr9EyifRGLA0Zabih7qqlnJKTkkT78E512HELfadQMYWYAneA8UKLDQgUaqn808moqIgFmb_mV5jh3kvPNbwOsyovjEHIflljvbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمار شهدای حملهٔ آمریکا به مراسم عروسی در سیریک به ۵ نفر رسید
🔹
رئیس دانشگاه علوم پزشکی هرمزگان: آسیه مولایی‌نژاد، ۲۲ ساله، بعدازظهر امروز بر اثر شدت جراحات وارده به شهادت رسید و به این ترتیب شمار شهدای این حمله به ۵ نفر افزایش یافت.
🔹
در حملهٔ ۲ شب پیش آمریکا…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/460068" target="_blank">📅 12:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460067">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JprWMmjZoxYAC6y2NnjabVHSh53IDz33GbRCmKm1e0C2oVbinzZuXkUVj3pVPDcCcYEaX4Qyt73N8HNh-78ykLb2OGlaJohSScX2kwN2bBWv1uQ4jaVAv7RY5xHOy-NCSjH64QU03QXbd4IfbLHE-fxmMxxdOTVkLFI4PVESPFHqbrImHv--0oLRGljt-Iruwl4e-l9TsJDOB9psE0nT0Bv23oknPF5iP-Dyo44zVQ3XaXsMdgPJPcuDMV0goA-foquSP2iFqXOhIqHfHlQT9Uc1ordjOnSDkjViBPLDc0xPDbHihx0XpUlLA_O664qYCQg2BGMqkyfqf8ncUdB9Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرمای بی‌سابقه در فرانسه جان ۷ هزار نفر را گرفت
🔹
وزیر بهداشت فرانسه: تا پایان ژوئیه، حدود ۷ هزار مرگ اضافی در جریان موج‌های گرمای شدید که تابستان امسال کشور را فراگرفت، ثبت شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/460067" target="_blank">📅 11:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460066">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXBnp1IquPJ5mgWnprkODE6YBWr0mJfbzHe9cHSpi3VN44OqVtBKANhqveKyPm2CU8xBw6dSV3XhD2HwTffL9WdnJhXqiNJS_U3mWVRZ6Mb3X_wS5FfdoRVHxLUv2GMyyH3fVJdSRqVTYSZSFkPLk_bP5vEo7S3YUyd2PrkECzD8VtHIJ97oAHpsAAed0s20dSMjapk1JyoE_Z7KAvan8YCYuk7cyegngMxpZ5GR3Alyn1Kykb1_ulFB7xM785QBWQc-_XM-Bm6hjF7GQIaaZRyWZ9Ri5Oj6ZAZqj84josWcR7fXBzoKApilJY7Ivv-Kg14gg6jGLgrqdgXUhHEQfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی پاسخ وزیر خارجهٔ اردن را داد
🔹
وزیر خارجهٔ اردن گفته: «ایران ۲ ساعت پس از آغاز جنگ، اردن و دیگر کشورهای منطقه را هدف قرار داد و این یعنی حملهٔ ایران پاسخ دفاعی نبوده است.»
🔹
عراقچی در پاسخ به او نوشت: به نظر وزیر خارجه اردن ایران چه مدت باید منتظر بماند تا به متجاوزی که نه به حاکمیت کشورهای عربی احترام می‌گذارد و نه به حاکمیت ایران پاسخ دهد؟
🔸
آیا او واقعاً از این موضوع بی‌اطلاع است که در نخستین حملات آمریکا، از حریم هوایی، خاک و آبی کشورهای عربی استفاده شد؛ حملاتی که به کشته‌شدن ایرانیان بی‌گناه انجامید؟
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/460066" target="_blank">📅 11:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460065">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmKsbLB8AgeddfVN2XkWvBztzHbuCtboM5fP-F561fB4NRtFkg0a5uLMNiat3MLP75EDJRpBians--JnFj9ixq-GoAMpzrFbQkWkwBMlEX5z11Vw-7WWbdtHDU2ClXewLoItrybpy6B_KJ5Y2trQS99dO-C6N9CjC-M0c1XAijcOGYaQbwWXk-VUWv968XxPkttC5HSWmHVmjFY2JCB2kAsvIcVVY2PIo5x_3vkAJ3mAEQCdO2QG_ynNR2Em4r97_WGl4BFADN55CImSpkVUQGcJuOFerGzVFNPneZp9jjtj8TuZPRtzwUwaT0XD31KIAhpBGyoiVwxGCP-cUXEUHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامهٔ عبری: نتانیاهو و ترامپ زمین سوخته برجای می‌گذارند
🔹
معاریو: نخست‌وزیر رژیم اشغالگر و رئیس جمهور آمریکا زمین‌سوخته‌ای پشت سرشان در اراضی اشغالی و آمریکا برجای می‌گذارند.
🔹
به‌دلیل نحوهٔ رهبری ترامپ و نتانیاهو، اسرائیل و آمریکا دچار نزاع بر سر هویت و فرسایش نهادها شده‌اند.
🔹
ترامپ و نتانیاهو در یک دستورکار شخصی، قومیتی و اجتماعی اشتراک دارند که به‌هیچ‌وجه دموکراتیک نیست.
@Farsn
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/460065" target="_blank">📅 11:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460058">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SJydh2IOJrZJqhyjCCZXuhRdmgGrvQR-jXxAaPnJhwpX94_IVNqScg3Kx4dfRtsDYb-Bz0cZ1S46ApmvvEFcph5qEEAiUVqsZ_Y-kYOLAKcffe5W1zZf7HMgpK4T_5fuTNOHuOTLmtqjSfSKRtP7A8kK2EQNHp5V4WBYq9Nn8N0bhMwUh_xXyCeobN4ocMpwazWlpBDy5WxzSGIL0x9XxnAE4gS9bauY6wibjzg_B62n1MpZ7S_13FsKI20h88FwxDD4N5hnT4jJXFeLjIHGWHiPZOic3rYMZqQYaKMhdth89_0r-1BG9FUXmzALTQhSRjMIpBNX_WgGAR13mGr37g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ye-pJ5-2klJBhdU3vSvkuPYiRaoONgsRqOuS5wyc3cy-mBNJzbKFLIq1TwKcyAoUqH7xToU1e8aPUMPBZT2fBy4RsvaPbSZsgmMYRKygTbAaUnpw0mUc3fOzCe4k2X3fbhrSXA_B7UNnDLwQtN_KIYT8p7_BwWNDP7EmKnDdWEp-1JLAwsZZgR7xj8EV6w7lqVZMWT5KbDo9D-zTZCLj3LM9p9DjLnlJygLVIV4h7iPrgexdr0iaiy_9QgAoa9np2odWazg9ayla5uUowwaA1hxZpAL8gd92v-RBxU8dKblJffCKm0Am-jhfd4yVGiytOymZtewuSp1FyUUy16GOmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A70Qv5XjPz0rifnTJmBIYYGwwojFUB9ZuwIoDic6b2PCB_M5XhNtyta2ryk0cfm7peoQTTtp2vIhizpA6319Wv5kEUY7G2t14EBtA3XZxrsfBv7CJfiYwNCXMw16KxTjUci_IM5aAM_yxu4hBllHus4O2Ni8RSP9VVcTjcBXbfB6uzxkkztsMdeWPkD3_xnIPKWH02xYHWK3oxlkEV_pXfuzvTyyX75O0yUifh1g69-nvZ6Ae83sDKcy0SFuGeNd1xA_vfqCw0ixK_aNpU0nlrak8egzRGKNlR0VknOtd_3zf8jqxCCV0fL3WMftEoMFzH4azhIdPcT4wVeCJs8UhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jQC5hJPJD9Wx_aIUzCIFJo0TrGTwQAMeK2rNiJM8mQOL4e-tragWoTxmdTnUazTTC7hTMpJ81C0MufDjo0Wu0OtrFuZu4P-UWLnpstuO3Fbq6O0tCwUVi3WnvosUy7dWCFm2m_e0eD6Z1WXY2Irswjsjnmt0z6mLJ6cwWqHcmAr77yrrOp-SvGgUwye8kRC42-MaRhULZBBPYb_wKfNUNaZKyGckXe_n-lJcw0GasYkFTVEjLfFYPhqRggHwboW737P56I9uV6k9zzCrrKFfOYOZANDdPGSI6U7y3uHx2FkrrfvQ0Hv_BZzDSNqUtZeJM-llU__doc1H6m5xjCOaeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NuuxsWgCOPaLG1iLND4__k6-VTh3D-BfBdWtIv7Wk-atIrthCA9_WncsQLtOWp6b7dwtRjHG2RdwVNrxJGJqs93jR1DJLwv0lofHkuunUsrRk-3IL-eos4nXO_tVJ4mRmDArrXnLxe-ICLL56a-GZpN39VHRC6yTCFwUloUgmbw7OnFJEBLXZHPl8Y6ngYTbnzgluxYdhzPGFroOcVZagv6YP0-Rinx5-8DTc1FRKpFzM9IeIBKc0MFnxJmboGR41ZbIxfgOFK74eQkeKdDrUoAsdbnV5C14pGoVuUZN-23tDLaIxLSzrEKmFrwTiyN9MhRuNX1vY3qcgqUs3TV2Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N15MKBp0oPbHwFKW6qtiX9sMhwIC2jDdtBHSRbH3XDy-xH30J1ok3hKD-2sRklmK_XBiJAEmEe79A5h7XwhaMYz2XEwQ4iThoL03QNpxHiIdwsiLkOanlRFZBNsIaVUJ0b7KdFMZU5YVxUth2INrkesXQlc6lUZnnA-yjEGbJBINqatlDvzDjJbhBNnF9oDqt-6zsnS1C9f4BZmF1s4i_0nRQRRCCX2ccBhK0pOznLQgFD7fpGdrCdicTJZl2kLUatoAdvkILx80XhewQUPGRpXpAe8j_hTLv338eoMg00tdzt3yWm3SJnxzrpBuNGoBceJ5N1CbXyHa3GMN-iHzzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LJCpk4sALVdTG3ZlrUYVfQdgG7Wt_B4mqguvukntoc9ICB7yf0SPupBWhCE5zdve8oablvp6hTFK8-J9kY5_K5VDCXA_gNuDL2IAAspwnbqYV1-imwPwhcirW1nHRh63vOkhPoXxdAP6htQOx3iVIg6PTMv9UJ7j2f3yLEAMp4RgBrHXxhL3eCI7so8sDiXPkMLjOpv8YHa9dAWtkKOl2NSQA0txutn3NvDgVeCMnpgc78wyvodaH3-TF0YD06rIjdxgUaXJH2T6p9n7puQBMgg8JMN2daICNgCuZux3JBmfAuzMHgVKdYQVo-ErEJNqB6Zi87Y3nl8L1caXJVyl6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مردم سیریک با شهدای عروسی کوهستک وداع کردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/460058" target="_blank">📅 10:37 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460057">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRIxl4BKuXDqPptmWvb5b8VSEffvvrbgX3qBZGozUYz91rjsjd7NN1Vfyhcqt0e4ZBmSTxN31-aOGBgEQQNmzoMFO19ozRmw0YHp4FW0FJ4Wf_4JgyKwxU13RxnGJqIZ273P8SG2dNfVQ4fCHQH3GOxmX-fpCqQje3QOQEN7xK88j6oNT3iLmoi91QXB-29ObTCufxtXaPPpzoWAT6I4z9szzrDj_KgANuncfri04vbCanuxVzY7rvjV6huJgXoiexy77-2_4vZpJPLFqcEGYgOF0e3cjPdppWdctV1kiXmRYDtNDt8oTIpa9u_DEGQBA4Xp53TvcmM3ZMoGqenfZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توطئه شوم بن‌گویر برای آواره‌کردن ۲ میلیون فلسطینی
🔹
ایتامار بن گویر، طرحی را برای آواره‌کردن ۱.۸۶ میلیون فلسطینی از غزه طی هفت سال رونمایی کرده است؛ طرحی که بن‌گویر آن را «مهاجرت داوطلبانه» می‌نامد، اما هدف آن آواره‌ کردن بخش عمده جمعیت فلسطینی نوار غزه است.
🔹
وبگاه «کریدل» (The Cradle)، بر اساس این طرح که «جدایی ۷/۱۰» نام گرفته، قرار است در سال نخست حدود ۲۵۰ هزار فلسطینی غزه را ترک کنند و شمار آوارگان طی سه سال به حدود ۱.۱۱ میلیون نفر و طی هفت سال به ۱.۸۶ میلیون نفر برسد.
🔹
بن‌گویر اعلام کرده است این طرح یکی از مطالبات اصلی حزب «قدرت یهود» در مذاکرات برای پیوستن به دولت آینده رژیم صهیونیستی خواهد بود و این حزب اجرای آن را به‌عنوان یکی از شروط خود برای ورود به ائتلاف حاکم مطرح خواهد کرد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/460057" target="_blank">📅 10:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460056">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bn-7nDhFSsQxQCsuIBCfKUuv5BvlqN5TfxysNU57QivdWQ5OyC1F7nawbc2tfp26HFkvsTVz22sEoJ16F1hSIzbLvGuZljZh7KZdA7IYj7RsWvOmY4PRCWKgv0GO0JJ7wIf0VyJK4IT1e7j-dbHASB5SXbdtO244fvJduWbNzafAmib_rtUiT2CzAnDv0LInSDDGjkxaKmr6PhflUaeGsX4nzovpa7XAVHfXo-TRmTMg4PN9J7oUhgXzxCEeXCqDlAAjtoc84idLfX65gduJs3cdhW6wgfTZR6z-DPAMQ8DW-T7TIPpQ7CGXPYfSTIhPdEUj_PceOjdVgEoNP8Kbog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس قوه‌قضائیه: ارادهٔ ایران برای گسترش روابط با چین قطعی است
🔹
‌اژه‌ای در دیدار با رئیس دیوان عالی چین: جهان درحال گذار به نظم نوین جهانی است و چین نقش مؤثری در این فرآیند ایفا می‌کند.
🔹
ظرفیت‌های علمی و فناورانهٔ چین در کنار توانمندی‌های بومی ایران، می‌تواند…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/460056" target="_blank">📅 10:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460055">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6u-oxiXBkzRJ1JmOjwXGDvku6ZYQwKJmudUG0D9BosnWFFxbvV25V1JtnJxZdxyFt_lroCA4IESYMWx4eAJWUrQuBiHJXSmbMlFT14G-bcAAOc091nY19HJnl24Q4CKPOi8nJUbLxFgiO5-eIt2sUP3GAWYk2veaeQQXQMFZ9sVevDe0z4ZxxRko2k7v8yGdthrt0xDLWjEUpd19vjPSjfrbOJ6ubetZQEQkPKKcnm99nrRkvTYPt4tXUjjucj8w8MN8Pl7TYD0jTR8Rh5Thro67fuG8FVxLfBo8ulvUcCXn_85lsNGaw5EM5CwLPna8tjMVI4GNEb_MsKrMjXbVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس قوه‌قضائیه: ارادهٔ ایران برای گسترش روابط با چین قطعی است
🔹
‌اژه‌ای در دیدار با رئیس دیوان عالی چین: جهان درحال گذار به نظم نوین جهانی است و چین نقش مؤثری در این فرآیند ایفا می‌کند.
🔹
ظرفیت‌های علمی و فناورانهٔ چین در کنار توانمندی‌های بومی ایران، می‌تواند زمینه‌ساز جهشی نوین در همکاری‌های دوجانبه و تقویت اقتدار مشترک باشد.
🔹
همچنین ایجاد و گسترش بسترهای ارتباطی در حوزه‌های قضایی می‌تواند به‌عنوان یک بازوی پشتیبان، تقویت‌کنندهٔ روابط در سایر عرصه‌های راهبردی باشد.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/460055" target="_blank">📅 09:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460054">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دستگیری ۴ پیمانکار و ۲ کارمند شهرداری پرند
🔹
۴ پیمانکاران و ۲ نفر کارمند شهرداری پرند به‌دلیل تخلفات مالی و اداری بازداشت شدند؛ به گفتهٔ یک منبع این دستگیری‌ها بخشی از یک زنجیرهٔ تخلفات مالی در شهرداری پرند است و تحقیقات برای شناسایی سایر عوامل در جریان است.
‌
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/460054" target="_blank">📅 09:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460053">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee9832f4f5.mp4?token=u9mZgmJJX-RYPuI9vQKGYXFpvFvOC4mPVX4VyEzjDB8ZXIon_C5g_xZSzNZ06UBNC9NJ50w_ygpf_acQlE-b15VRg1z3TTyuI1H3ZpvdnBznEr-6voQVmVtRzSd-_-m765APqVYkMJ-A79R0H8kTuyW6X222YxEE8upqfZtB6tNiZnOt2F7kRkeiTzpK-siefUZACosNlyENgFZS8YPGOzmb8gwrjlFpfG97_Rtrq4bEUU4uGrrxgJKE6J8NgYqySI18hyeeBgJcWZc6nPiwSwFNAOdu_gI4dOrXZm8MojQ07ccCfzgL87BkT0B0O5QNJzmDmhUJKpIAdbgMrWtDQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee9832f4f5.mp4?token=u9mZgmJJX-RYPuI9vQKGYXFpvFvOC4mPVX4VyEzjDB8ZXIon_C5g_xZSzNZ06UBNC9NJ50w_ygpf_acQlE-b15VRg1z3TTyuI1H3ZpvdnBznEr-6voQVmVtRzSd-_-m765APqVYkMJ-A79R0H8kTuyW6X222YxEE8upqfZtB6tNiZnOt2F7kRkeiTzpK-siefUZACosNlyENgFZS8YPGOzmb8gwrjlFpfG97_Rtrq4bEUU4uGrrxgJKE6J8NgYqySI18hyeeBgJcWZc6nPiwSwFNAOdu_gI4dOrXZm8MojQ07ccCfzgL87BkT0B0O5QNJzmDmhUJKpIAdbgMrWtDQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس قوه‌قضائیه: امروز تمام اقدامات ضدبشری علیه ایران انجام شده و دشمنان به آن افتخار می‌کنند.
🔹
اگر روزی که تروریست‌های آدمکش بیش‌از ۷۰ هزار زن و کودک را در غزه به خاک و خون کشیدند، در مقابل آن می‌ایستادند امروز آن‌ها تجاوز و حملهٔ غیرقانونی علیه کشور دیگری…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/460053" target="_blank">📅 09:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460052">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iI2t_u3trXaVbuFpVt_zuRUsvrpE6Cd7qvGyN4uXVOrJAt7NG41eMdsnrN9gZFUQmy4yWZXPI0H-fprAebQLn5nOEydOXzLiY_YQo9h3mx6EADVKSclzDytmYZRqiW3fj3rXDxEXueZfrFG3KVNGNyTcFiohRPGevetWDl9hXtcyeJGlnjXj55A3C-tnTXfvKe4WcWU1saocDokvrzjrNL8Hp3LwrqmTIga-XO4xDjSgAvpofstpW9ZMbRU5W4bckorL2NSce3Qok97i5elcreSw7tXI3wl90P7Ph56VBzJUMncAG4KnY-Way58x1wo8Ct3NuwJV3rA9cb8l7VmxXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
فرصت طلایی ورود به دنیای رسانه با ثبت‌نام در دانشکده خبرگزاری فارس
اگر رویای فعالیت حرفه‌ای در رسانه را دارید، اینجا شروع قدرتمند شماست.
✨
چرا دانشکده رسانه فارس؟
✔️
آموزش تخصصی با برترین اساتید رسانه‌ای کشور
✔️
کار عملی از ترم اول در تحریریه و باشگاه خبرنگاران توانا
✔️
رشته‌های جذاب: خبرنگاری، عکاسی خبری، سینما و تدوین، گویندگی، روابط عمومی
✔️
کاهش هزینه های تحصیل با کار وتولید محتوای حرفه‌ای در باشگاه توانا!  (مهارت و درآمد)
✔️
پشتیبانی از اشتغال و همکاری با رسانه‌های معتبر مانند خبرگزاری فارس
📌
شرایط ثبت‌نام:
🔹
ارسال عدد ۱۴ به ۵۰۰۰۱۰۱۴
🔗
یا ثبت‌نام از طریق سایت
futurix.ir/go/rxDxXO
🔹
پذیرش پس از مصاحبه و استعدادسنجی.
🔹
ظرفیت محدود است.
مرکز آموزش علمی کاربردی خبرگزاری فارس</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/460052" target="_blank">📅 09:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460051">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ea54ba0c3.mp4?token=MGQbzL8rIK8qyC__BI8VZy5RNSt5lixx1xHYNHIQ0Uv7buHWt8kYohfFqlIdqNjL5q5bIfd1IYYxXkBOTGbISYjQW7Y7fyHA8DeB9yo-UPtZ8vK7sJbbOj-waT8R9oPTLDReVtOVt8zptRfjomd8ezmvuaCWLB_Olk7ygmwO9T-1UlTLrUt6G-tRe3O6CJFJYj_sqVA1osp6C2u5GGI2Esz8p_Z5hXHpENYYd0Td5iT4LZCeBJFeqbI9LUhtxUGFxyrtqfgJ6wDzeJ4SP4tYggcqLh4t9sZd-hoSdQDMPQJCrJsqVbJ2HHxBKmYZtirO9eeu_yS15iY-WUgwGIG2Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ea54ba0c3.mp4?token=MGQbzL8rIK8qyC__BI8VZy5RNSt5lixx1xHYNHIQ0Uv7buHWt8kYohfFqlIdqNjL5q5bIfd1IYYxXkBOTGbISYjQW7Y7fyHA8DeB9yo-UPtZ8vK7sJbbOj-waT8R9oPTLDReVtOVt8zptRfjomd8ezmvuaCWLB_Olk7ygmwO9T-1UlTLrUt6G-tRe3O6CJFJYj_sqVA1osp6C2u5GGI2Esz8p_Z5hXHpENYYd0Td5iT4LZCeBJFeqbI9LUhtxUGFxyrtqfgJ6wDzeJ4SP4tYggcqLh4t9sZd-hoSdQDMPQJCrJsqVbJ2HHxBKmYZtirO9eeu_yS15iY-WUgwGIG2Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس قوه‌قضائیه: ایران به‌هیچ‌وجه زیر بار ظلم و زور نرفته و نخواهد رفت  @Farsna</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/460051" target="_blank">📅 09:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460050">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_lOHiz2hsi74qYiLahiEbe4ogRFYxhqvp6Sz3H5jy_LyTelP3NdAEdk76EMG2KXaAvihqZyq_5nNFcJBEBl0fIYsbS4m2_am0wn8YuNajw1mFovPUCLfeBuhFySkIS4JGq-5Th7jdo0-beCoSR109oAffXQsOxBpy7c5n5gkp33pd3t2Ta6AbZLE5TmctE7aUPxs7pRNBf3sqtK_5NLH46jiv0QTjRMXxWc9oyFt-lqYax6e7iA2CX8Pg556GJB5M_65lPp54oMoVM4JC43oSPyR7INT3sqnEXRXT-Q1ktke-Ax0KTVe6dynA7iqfpAB_l1Cd4XkfzLgBNMC9SSYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظرفیت تولید برق کشور از ۱۰۲ هزار مگاوات عبور کرد
🔹
معاون برق وزارت نیرو: درحال‌حاضر ظرفیت تولید برق کشور از ۱۰۲ هزار مگاوات عبور کرده و اجرای طرح «۱۴ مگاپروژه ۳» با هدف توسعهٔ نیروگاه‌های تولید برق آغاز شده است،
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/farsna/460050" target="_blank">📅 09:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460049">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a4a32b4e7.mp4?token=sDMw55ffKoxYzBiHlmfB6pUxg4TrUdzgcAx6v4j36Oosp-OHX9CnZm4atcYHHjeU0YztHhSsRjbj9xhV32jWnq7aXrRDFDYos3r2tkMAxQBa4wzqSF3iFT9g3zBK5Xf9xoMqhD6nJ8mx8uUQjE9Gfi_CQyryPBo9b_-9cU9Z6FU9zQdEGWgq3xPc8cFnuphgbXkDtYnnd38TEVPGnuh3OmIPvv_m0UUiA5Az7xB2JMqFl_gOIC7BhyIi9xqhLqOYQtnNX-CFKfdSV8NDkaJ6ffrayBZ2z-bO3qM7XQ9OR1L5xFT8bBCWpQow5osamoseJ5CxQYeZBI6-pIYamM20Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a4a32b4e7.mp4?token=sDMw55ffKoxYzBiHlmfB6pUxg4TrUdzgcAx6v4j36Oosp-OHX9CnZm4atcYHHjeU0YztHhSsRjbj9xhV32jWnq7aXrRDFDYos3r2tkMAxQBa4wzqSF3iFT9g3zBK5Xf9xoMqhD6nJ8mx8uUQjE9Gfi_CQyryPBo9b_-9cU9Z6FU9zQdEGWgq3xPc8cFnuphgbXkDtYnnd38TEVPGnuh3OmIPvv_m0UUiA5Az7xB2JMqFl_gOIC7BhyIi9xqhLqOYQtnNX-CFKfdSV8NDkaJ6ffrayBZ2z-bO3qM7XQ9OR1L5xFT8bBCWpQow5osamoseJ5CxQYeZBI6-pIYamM20Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: ایران برای استقلال خود شهدای بزرگی تقدیم کرده است
🔹
رئیس‌ قوه‌قضائیه در دیدار با علمای اسلامی و بزرگان ادیان کشور هند: ما از خون شهدا، زحمت و تلاش خود نتیجه گرفته‌ایم و سرافراز و سربلندیم.
🔹
امروز ایران تنها کشوری است که به مستکبرترین عالم یعنی آمریکا…</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/460049" target="_blank">📅 09:36 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460048">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/291e1abe06.mp4?token=PxZJkbvRZTYf8RYvThzRiB-y2enu9ibipu3q9ViZtZwZOefnfh_pZdvoAc-Rk1mDcIqRWkCaGZ5Q_Z2dpc5VFrjKUe6A-SDcdIeX5j0Rgl2Y7ebnGEqVFDvfVZVEVAFUWFvDgQ1r8EqAsu6Ilkouy1Gc4oRiBTSvUhoL9SDP7Y3qWAaV0dmdxWK-GsfFgLQC4446_mE6pL5yvNlJ4FvZd1F7t0YZqYiAZNnKNXex755rUtNsMBpbDL2HTkAVckWpQ2s9e4bjddV_kkqjQiJ5PUBFe2NhtB811VUhNIVnIR3S0nUB91f_4GI2uftDJfcVeUA6sLNMGwHNJqAHxV0Hfa-D3Efz0jk2BQx3rMMNl4IZFHziNf0L1jwrR08lMAzhzWAd_LiP7hOYx6C46XZz7gJyhceqPwwFkeDu1M897PBdgfMi-EB5jJrZ_SYMdN9ZDD06oflLe_pLCreJcvrFTZXKJXf_KzhT9qMSSWH9SxVf8gq0bLpFyRWBYZt_ND7xcwX8HR_n62M27ogVz53NE1BE68yZ_ngSH4sn3C2uQ2dzLcnrZ8KE8qTPUUqC_peTkQweoFHWEExGjUPysxjwIJGVOTbOM5rTt5lzEGbpKvZmwatksxHyBlRTnFoiki-E0_AwvZZml2BIgwFoIrLYDj_QaO_UkvY7Lk81gBkSobI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/291e1abe06.mp4?token=PxZJkbvRZTYf8RYvThzRiB-y2enu9ibipu3q9ViZtZwZOefnfh_pZdvoAc-Rk1mDcIqRWkCaGZ5Q_Z2dpc5VFrjKUe6A-SDcdIeX5j0Rgl2Y7ebnGEqVFDvfVZVEVAFUWFvDgQ1r8EqAsu6Ilkouy1Gc4oRiBTSvUhoL9SDP7Y3qWAaV0dmdxWK-GsfFgLQC4446_mE6pL5yvNlJ4FvZd1F7t0YZqYiAZNnKNXex755rUtNsMBpbDL2HTkAVckWpQ2s9e4bjddV_kkqjQiJ5PUBFe2NhtB811VUhNIVnIR3S0nUB91f_4GI2uftDJfcVeUA6sLNMGwHNJqAHxV0Hfa-D3Efz0jk2BQx3rMMNl4IZFHziNf0L1jwrR08lMAzhzWAd_LiP7hOYx6C46XZz7gJyhceqPwwFkeDu1M897PBdgfMi-EB5jJrZ_SYMdN9ZDD06oflLe_pLCreJcvrFTZXKJXf_KzhT9qMSSWH9SxVf8gq0bLpFyRWBYZt_ND7xcwX8HR_n62M27ogVz53NE1BE68yZ_ngSH4sn3C2uQ2dzLcnrZ8KE8qTPUUqC_peTkQweoFHWEExGjUPysxjwIJGVOTbOM5rTt5lzEGbpKvZmwatksxHyBlRTnFoiki-E0_AwvZZml2BIgwFoIrLYDj_QaO_UkvY7Lk81gBkSobI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: ایران برای استقلال خود شهدای بزرگی تقدیم کرده است
🔹
رئیس‌ قوه‌قضائیه در دیدار با علمای اسلامی و بزرگان ادیان کشور هند: ما از خون شهدا، زحمت و تلاش خود نتیجه گرفته‌ایم و سرافراز و سربلندیم.
🔹
امروز ایران تنها کشوری است که به مستکبرترین عالم یعنی آمریکا نه گفته است.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/460048" target="_blank">📅 09:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460047">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🎥
هواشناسی: سامانهٔ بارشی جدید از یکشنبه وارد کشور می‌شود
🔹
با ورود این سامانه در روزهای یکشنبه و دوشنبه در اکثر مناطق شمالی کشور شاهد بارش خواهیم بود.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/460047" target="_blank">📅 09:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460046">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6761000c20.mp4?token=X24CrN3oSiJda6uurrS5ZJkGTHe_UBT59sU_7rpUn0hMMTkdwlP15S-BHlS_d4d4Q3zO7B_u0yCfz7_JfcQOUN5Xd7oZO5tM5GT5Iv8zmaS8PXhD2Hd8Q9OKeHngyNM7sEwHzc-wGeKxzKRMmNxMdSqcs-zCZkyyQ--6eKfC0fExaOwDPWrkzepxVhYYyr5tcd7JdohWQWRgptfktlTTWIo4WD5qJFi7td5uEtHD1UJ6Bq-coOWIXxfLc_vNzDH6au2Qj8XiLyEbBLi2fUozCNqcG0gGpHeW68JVszY3PRpQ9lq3sn4a1km5LZ6OuF9nhrAd451uHP29tGkT7qv0fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6761000c20.mp4?token=X24CrN3oSiJda6uurrS5ZJkGTHe_UBT59sU_7rpUn0hMMTkdwlP15S-BHlS_d4d4Q3zO7B_u0yCfz7_JfcQOUN5Xd7oZO5tM5GT5Iv8zmaS8PXhD2Hd8Q9OKeHngyNM7sEwHzc-wGeKxzKRMmNxMdSqcs-zCZkyyQ--6eKfC0fExaOwDPWrkzepxVhYYyr5tcd7JdohWQWRgptfktlTTWIo4WD5qJFi7td5uEtHD1UJ6Bq-coOWIXxfLc_vNzDH6au2Qj8XiLyEbBLi2fUozCNqcG0gGpHeW68JVszY3PRpQ9lq3sn4a1km5LZ6OuF9nhrAd451uHP29tGkT7qv0fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قوچ وحشی بر فراز کوه‌های بافق خودنمایی کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/460046" target="_blank">📅 09:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460045">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhF9u6jf0-8kWRjcemAtmtvDCo5IdBSDHNLm64l4pUUXtM5hlZIVl1uL_wYjrU5a90qEmXUWbdJh0eEBNMXWRTKKNsi46IQPLwxBwySdMDC9ch4aACCexdiYlu83pbUxKCG_Rpwjr6ddtdlsX2EWEaY9NPLd7HUiFJqDzgEEKAxErQlFEXcefk3PIoSxmFrbouzcmyUJ9yVPWMc4qpz4-tcUEUf-7zIUn-XTGvhqrSuH0yCZtrUkxl8-51IFxJVVfjjupPhEV38NWUf7Acp4dQIEUekoxgZ8xt-Z2QMcz3r1cfjNQuLPyqUg_EjJVW6VK_39g7nGsbTgSdPcN2Su6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیروزی شاگردان پیاتزا در اولین گام قهرمانی آسیا
🔹
تیم ملی والیبال کشورمان در اولین بازی خود در مسابقات قهرمانی مردان آسیا  ۲۰۲۶ در ۳ ست متوالی با امتیازهای ۲۵ بر ۱۵، ۲۵ بر ۱۲ و ۲۵ بر ۲۲ مقابل نیوزیلند به پیروزی رسید و در صدر جدول گروه دوم این رقابت‌ها قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/460045" target="_blank">📅 08:48 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460040">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rysv5UArE1VDqNDfZVtqFpMpSvd44A0OQyvJjanxwhyt7LZENO3vl3DL_fy96stnVQHzETSY1wKBgd7L42Lo_zBM5ZZdpHk30kEOkMhMW9n8_FuEVJpjpu2o96JeuMKBLgSE71g77TTt4JwU0nW-c62yQ-bos4fakcJgSRQNYmb9R3a-7E-_ztIHm_FNmjHmxtabTFurfchylecV51bQfDwGWNk6NNyC4QiR9MgahjOONe8V_F-OtLBDaB1KizsDXtnHq8oIB-sFG7bNufNXBfRBab07RBnswTVeuGheo6lN2O6Q9gWm5-kxh9xaAa3JjBc49cwIwB0uNHEsW74zXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SBSRn9hlIpSaL0FUEkSMju9YHcu-rmrr53e6Tv_jJ3eKKzxZyp4b5cBJDiwK2BhcWwBxWy2dxZKluUFQry-nF_QuBxWWO-ntXAukYYiWTnqqROeBCcEIUIjLsPcPxk0i80YsBXYXTlRaJyQ4YpK-To_2ZPtUzY5ovLAb_EsLI-9GLwEOkx2CV8-n4gGoLwCGgb5fJxiF8-UH5_HckYYtRHniyYbeqb78xBoi8XIeQ4r9dyk7Lsb6vsRKzcxCKGUgsmwnQ0T39lNa8_rs6Ud958ryfYdV1fTW9Af2RF_rwX6mdugvSBB7VvIdIGf6OyA50FT0bB1ZfK6Vsbz3ByFs0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZvIRkaxcv8xb6N2xa1ZR7Km4PmHKS0GFdHPcxAmsdgE1WaQqm4yebFGMfqc0k1QlN1a73a-ggjSAJqmwGA-AaX7ukXyXYQnzji5s7Ag3qdY9-sZO6ConXfQpybYG_lTiiac9ip7Fhyd-pc7Ivzr0PizYsgwVGRU5Ve0-zHRHxitqh8IsEp8YiGaazQmK8D12sJSf9BbgZwam2CvUO2tbHTEPlAkgTUIOOSBYDWInOuXKw4uugiQ2MJ_nCGmamxDpzet6T2MsjUmrJ7kWHg8LsMiSDUJMb2PSoKymdQ7wKkv8NBTLuI18HFRV4N3KcPevb1kqdfuMy8XtdDTEjCkSdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WvWrrKCvPwEYwF_6hDbdxwDpt0nt3krlnrc_rqa7Spgwy91YqJU9kFUpdk-RFzI1tLFKPxholHwK1S-NO33cPUCkda8Yk3HslmCfr1LoI_fWE6Idx7w8SlvBMdIoHVgAHRFrN2PfrhX8Dm7X010Myr3gwBIOM7Pd8sAqJMG-TlFayVreI8zOnQhHPoPVOq2hr5DyRC4SGXT9zHZV3aV9WZgLzjXmEKLk_o1CkS8lQxaZZydMb2razgcYGgeGy8ukJgCyOhIjNtcX-g4ZTKYm3gsE3oRffEDps3LsBaxDymQgdrGWyRBCJE3Lepdgf0UaKung3dC_SAd1SYAMk8_Rmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CzFDKuOnvPogfBs_BEr7hh16ghVUx2zjp5VL4kgn2-Wa6HIqSAD0ln4am9fvHktYRm6WGwZOvVwsIu8ZCbHLUEGJ-eS6GaVXy-KDo1J1pJAu1MVqTZNiOmvttJ2ahnpE7v8pvBD_dbc-Do0MskvhJjzhYyPvdqwYo7_DTBwVEWUyCMXtQQoBRzxn5Xqb1GxsLmfsMRQzyR26bzoeXC0_0ZEDMQ6N5GFqc7G7p4s9W7jjT2KMcvGbZxGQZpXqGL9mzjhG13k6TU2hTgQV8bK3Q16afcnkpE5CF-U6gPSMTbNSw05KJBVPmWwxkcVp6wpZ9hJ-RAdy3DwtC5MhbvUJ1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آیین تجلیل از خانواده‌های شهدای جنگ رمضان شهرستان لامـِرد
عکس:
احمدرضا مداح
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/460040" target="_blank">📅 08:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460039">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZsFIYd0SHSWXnlvQA3ovjZrq2thMv7_3x9OaVO0XYiPCkDRqedAk3E9uAFNrNtUPUiiWNRVvvI4rGt2vMGMst8M1fC5YgfbF6RUui6TZpjDnqgKKeVkmFbSBykXqQaJ36N-IsnGxF1wTyDrMtmHg7UG1JKj4arbHvXD8v1xK29TSRPRJl4EWiF-KXq-JeNmQIBbWNt3PhlKdSPzp3C8IknpAS6xAazTNuaN6du1Fww0lEbeh5S98QleVD1guuYhh-8akf1GIns7UaecuUEYpfuBe-eHsBbLmmvG8e_qQtsUowIHrAOh8f7_ebkaW9IV2V_1fYELOjZ08ObQf9lMvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فایننشال‌تایمز: ترامپ توافقی شامل برنامۀ هسته‌ای و تنگه هرمز می‌خواهد
🔹
یک نشریۀ انگلیسی گزارش داد که میانجی‌گران در تلاشند تا چارچوبی برای مذاکرات بین تهران و واشنگتن درمورد یک توافق جدید احتمالی ایجاد کنند.
🔹
همچنین این نشریه از تصمیم ترامپ، رئیس‌جمهور آمریکا برای گنجاندن تنگۀ هرمز در هرگونه توافقی با جمهوری اسلامی ایران خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/460039" target="_blank">📅 08:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460038">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ocu0jFWiP9-LK1JE-AFxVLF3nzeLaO00hF6SlX95vGIxsruA_Qpxpwk8Y-e2UVaBssq2FLd4pcCJdBAhV9r_tj3o5xeGsZDllX9ktjxUnm6kRGxPDmkLSsqiM_6ziy4v7rV4ld84yXKB61FuL3x4esKzsTvRvCG9x2r2zGNjXeWkDAcMaMXYoDKvMqoD7zV1zFK3O97IZBPTC3OCz-qw3wDp5rbObsVlmykQHJ1c8ElM_NpO1034RTkTTwjSS02M6dUlHt_Wm9px0YN74lum0O1kGX9bLfww3ZPb03z_OeIWDD9KcX5BF2tKdi6kyBAcu_0P1lG-HcGjPyQyRZ2f0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدارس از مهر حضوری هستند
🔹
وزیر آموزش‌وپرورش: تلاش ما این است که تمام مدارس کشور سال تحصیلی جدید را به‌صورت حضوری و با کمترین دغدغه و مشکل آغاز کنند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/460038" target="_blank">📅 06:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460037">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اعتماد به هوش مصنوعی کار دست کوهنوردان داد
🔹
اعتماد گروهی از کوهنوردان کالیفرنیایی به اطلاعات نادرست هوش مصنوعی جمنای دربارۀ زمان و تجهیزات لازم برای صعود به کوه، منجر به خطری جدی و عملیات امدادونجات چندساعته شد.
🔹
کوهنوردان با اتکا به هوش مصنوعی که زمان صعود را تنها ۸ ساعت تخمین زده بود، آب و غذای بسیار کمی برداشته و از همراه داشتن لباس گرم و تجهیزات مخصوص شب خودداری کرده بودند.
🔹
اما این مسیر در واقعیت ۱۶ ساعت طول کشید و پس از تاریک شدن هوا در مسیر بازگشت، کوهنوردان از مسیر اصلی منحرف شدند.
🔹
پس از تماس با نیروهای امدادی نیز به‌دلیل شرایط نامساعد جوی امکان اعزام هلیکوپتر فراهم نشد. کوهنوردان پس از طی ۹ ساعت پیاده‌روی موفق شدند خود را به منطقۀ دارای شرایط حضور امدادگران برسانند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/460037" target="_blank">📅 05:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460036">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d24f550794.mp4?token=q2MZWHLXxK52rl8-oxIbxC4pU5vlWz6wn91JgPeyHjJcVl2tRbWOAT7fdCZNJgQT6hdnapFZGEb0zp8cTGCvXkNtImGIt_pgkKzpfFKMod35NcWVzkXJsvFdJmWRegA4dbNLA-OMLlVY-JEPWMyhXcTdyHDjyjnYE0LjOaXR6vMNn27gQNiChbXNhi8szwauOgYsZU2tTNOCdfq9-NZxNxLIGBvwp6TVrjcgUmGrypz57LkkxYhAFQfPTFdxLbG7ID8ZNkT2apLPJTG5sKoLVDojMo_0ZEkiQWH8k8ZtcEiFO05UvXTA5KeqA0sTaeIomzd1793LhXvwuXI_JgQlFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d24f550794.mp4?token=q2MZWHLXxK52rl8-oxIbxC4pU5vlWz6wn91JgPeyHjJcVl2tRbWOAT7fdCZNJgQT6hdnapFZGEb0zp8cTGCvXkNtImGIt_pgkKzpfFKMod35NcWVzkXJsvFdJmWRegA4dbNLA-OMLlVY-JEPWMyhXcTdyHDjyjnYE0LjOaXR6vMNn27gQNiChbXNhi8szwauOgYsZU2tTNOCdfq9-NZxNxLIGBvwp6TVrjcgUmGrypz57LkkxYhAFQfPTFdxLbG7ID8ZNkT2apLPJTG5sKoLVDojMo_0ZEkiQWH8k8ZtcEiFO05UvXTA5KeqA0sTaeIomzd1793LhXvwuXI_JgQlFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرزندت گوشی نمی‌خواهد بازی می‌خواهد
🎙
هادی زینالی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/460036" target="_blank">📅 04:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460035">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ba6YJVcLJYGUANdNbjJ_iRE8d8yeE6pLyXZ-TJitxbmvaRmdg1EVLR6nFg5zg1B1ui5gtMbhDXH9vR7JeEJyU7nl8Om3rw3p-5648qG2DRvE0gg13gctUBgWK54P1AZh6gSUOBGRKYD5ss3tjx6CRJ9XZaqZh_c_mB4bpTSBtP2hT0Q--6kg3JO17Nty3wxbQRUkuU4hsR0G3TGH3bW1rdgAE2B7BfMqTHtqNtiNPzzZCpcgJcXwMHbMHEMgf4fZGH9krutqlry1h86ncLEobThDJLweOYTbKs_LWDB6eEClvJRZlZgB4NTVsoKx7WmSuNROzzBUWEYczwf9ZmpL5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴ متهم آدم‌ربایی مسلحانه در مریوان بازداشت شدند
🔹
رئیس‌کل دادگستری استان کردستان از بازداشت ۴ متهم آدم‌ربایی مسلحانه در شهرستان مریوان، در کمتر از ۲۴ ساعت خبر داد.
🔹
این متهمین چهارشنبه ۱۱ شهریور اقدام به آدم‌ربایی مسلحانه، و ضرب‌وجرح تعدادی از کارکنان ادارۀ گمرک مریوان کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/460035" target="_blank">📅 04:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460034">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ma2BWuK-9S4Ach9NPo2aue6PUdJ7cB8kJQjhGN3JigygFqUYYRoScMmZb0oQDx0jfpGp1TL60H54NjeKNbXBDzcUZwz5BBSaNp0qOppobpAmjj6cXzkO8Z9zVDW8AU7BY4G0BHJlMpaguGEsYvrfV0TaWq7q17zM6LO4C_tAyPEnm3fiAX2oPGwDidSVy3P_PQIaUD_PO8SDBorcBnzxrYM35g-1FQlTAjYCsTiv3YE4mDbkvqdno7oUWvpdWuD8ABeVqwBel72Wqj5sDSDGxTWYDqVx5SWj4U7_g4EXwQxcTHZhJn3ZpJ4bGyDqS3Yik9dYuMlaaGGyLecprzFPmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین مدل چت‌جی‌پی‌تی رونمایی شد
🔹
اپن‌ای‌آی از مدل جدید خود با نام جی‌پی‌تی-۶ آسترا رونمایی کرد و آن را بهترین مدل خود تاکنون دانست، اما هم‌زمان هشدار داد که این مدل گاهی تلاش می‌کند از نظارت انسان‌ها دور بماند.
🔹
جی‌پی‌تی-۶ آسترا سریع‌تر و توانمندتر از مدل‌های قبلی است و می‌تواند کارهایی مانند آماده‌سازی مالیات، ساخت بازی، رندر معماری، قالب‌بندی یادداشت‌های حقوقی و جست‌وجوی آپارتمان را انجام دهد.
🔹
اما اپن‌ای‌آی می‌گوید این مدل بیشتر از نسل‌های قبلی احتمال دارد روش گام‌به‌گام حل مسائل خود را مخفی یا مبهم کند و همین موضوع ارزیابی عملکرد آن را برای انسان‌ها دشوارتر می‌کند. آسترا هنوز در مسائل پیچیده نمی‌تواند همیشه این کار را انجام دهد، اما توانایی آن برای پنهان کردن ردپای فعالیت‌هایش در حال افزایش است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/460034" target="_blank">📅 03:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460033">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">هیاهوی تبلیغاتی جدید وزیر خزانه‌داری آمریکا دربارۀ تحریم‌ها علیه ایران
🔹
وزیر خزانه‌داری آمریکا مدعی شد که اتحادیۀ اروپا رسما به روند «انزوای اقتصادی» علیه ایران پیوسته است.
🔹
اسکات بسنت بدون ارائه جزئیات بیشتری از این «موضع قوی و زودهنگام» قدردانی کرده است.
🔸
پیش از این رسانه‌های آمریکا گزارش داده بودند که جنگ اقتصادی دولت ترامپ علیه ایران، تاکنون ادامۀ همان سیاست فشار حداکثری با دوز بیشتری از هیاهو و جنجال‌های رسانه‌ای بوده است.
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/460033" target="_blank">📅 03:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460032">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ko1N2-V-4fIn8yWjd5J7Ozv9KbycXT4fxAs1EcB1wxS9DWhEfjcepnUu9wF3GvuEplUEf-xwTPqtnKfKzrJE5vN_OvZT16F_QmYpO-KuOt383B6bIgQ6zoZ7y29THJEj-EXP-3k8NpH8qv1FWCyDpjjcTRvOKiRNu_5p-p8-VrMUfYUkcUfENoHlksDawZ1sPi7Uwimjl0letUSlvxvLPZP9A7ZcT5pETLUV441nBfzTxeueWUuh9MzLx5BmXzDhfHt34zsL6SdoEaH1zugElGveWQFquqTduhI0sCeVFruk147TURQv_02OoQqRCMjI9p0qAENAmlg2DcKCc8RZvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز: حمله به عروسی در ایران ناشی از اصابت مستقیم مهمات آمریکایی بود
🔹
تحلیل کارشناسان تسلیحاتی از تصاویر و ویدئوهایی که رویترز صحت آنها را تأیید کرده، نشان می‌دهد انفجاری که روز سه‌شنبه یک مراسم عروسی را در جنوب ایران به خاک‌وخون کشید احتمالاً ناشی از اصابت مستقیم یک مهمات آمریکایی بوده است.
🔸
رویترز نوشته که این حملۀ مرگبار ناشی از برخورد یا انحراف بمب‌ها پس از اصابت به هدفی دیگر نبوده است.
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/460032" target="_blank">📅 02:56 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

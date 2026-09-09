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
<img src="https://cdn4.telesco.pe/file/hQXQTtxaZn39OTsE2gWjsrksB0nb3hkCUTr3XplKF87D0pjjHeUrvfGTSAF7FlBkYz_5fKk2FHvt58paKcjqeWT0cyIQRDR7avqaOO772Y51aykokwmbruZGJTsJwlbUkaAZkdmGtzra-QwFbfmMGvNm8KwruM3ju1L86Y9ppFtxByx619AGV2I36EvQ8esybWtX1agk5tD_itLezV4FfSNwc-wA0BEvHyxfJCT6VvLj3kFisiaAn9plC_OH6b1JU9HTdYktspX9HfCKzNWzu6yBqAcAWjlCD36DeGhl2VIF4Q-Csq-cURWUt10U812HK_YNr7EvXgxMpC32LWYAKQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 15:07:03</div>
<hr>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=fJpTDFQQRzGVOnXSXSrYg35-ut-hufJU1Zc4yeVn_1sFFwvVFAlUvkJRLlv2XzlT20HUdncTfL66tMNFj7uy0EQ_jmlPby488_rqvGH-L3T3C4c6Cbt4AXKo82MQJepJUijK4O_XwyGW5bdwYwUHzNpyUgP1unI9usijZMegTc05oOk2bL-8UBZnaM-S33p07Ix1jbj4ciu2YZXk4UiGsm0J4vSqBq7s2ksegJaVDKU9GC2M6j-pybjII8JvIbcAEM_ALn7OmW3ObYodP4SS96A7AuopxFJUWIM5We8HfzXd7c-ZxMgIIscbg2ZVnP_6siQHnasaVypG4AVy24pmzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=fJpTDFQQRzGVOnXSXSrYg35-ut-hufJU1Zc4yeVn_1sFFwvVFAlUvkJRLlv2XzlT20HUdncTfL66tMNFj7uy0EQ_jmlPby488_rqvGH-L3T3C4c6Cbt4AXKo82MQJepJUijK4O_XwyGW5bdwYwUHzNpyUgP1unI9usijZMegTc05oOk2bL-8UBZnaM-S33p07Ix1jbj4ciu2YZXk4UiGsm0J4vSqBq7s2ksegJaVDKU9GC2M6j-pybjII8JvIbcAEM_ALn7OmW3ObYodP4SS96A7AuopxFJUWIM5We8HfzXd7c-ZxMgIIscbg2ZVnP_6siQHnasaVypG4AVy24pmzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXykR_ockWfVCgnUbitTuqdF-4M9eKrcZZMtDGlJHUzxduKHaQ5bCBjb3ywS1nJjGbNq9hnqIUTjsyVg_0Lc0pGnu6459sFjBVkH84-a2Bz8Wu6DdrOTKq-0pAmb1n76_cwKVJyJpb79XFGb5_IxNdRIfEt76EzmlippSjBj08QgRImaqyIv4d-H-5Ut4Z-aTuIv76QTLZkJjlijaRUXWC5Vw5SlpvH4vIaQwFIJkmsqga45JAq9hCpys2ja0jD5INw98FskYOeu9uKtQ-ZMKOnnhgaQ0M_Ma7wgdmCPlXLsU7tb3GefI7rfcUazyi7NB_kn5MWkEa51i-J41h7pRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=pwwcRfGld9ze51rCqkCsbO-9rRgJbtr71x42SwKPwBOq-DavQhKHIkhRB2oqTOMC4RZM2-CW6Yoy5WP9_GMtOy5ielVejx4fO7_Myp23u6G03-pPFavvbcM74-7b2qKY0CGdQ9DRkMC7J1PRbrqI8GtjbXk2mABBCDv8Zd23Ih8vz7lP6TEVVHXzjA59saO9TjvhWtBlPhtSIpoRuGd8UtY8tXrZ2_6VRsFKFc78a_k1GPQwd7Stwi6qBa2SGMe-R_1WQL6mlVUNHDUSp6Uwz6KWDsENi5G3b3h9nxPZ-cM7l3m1l5uaEuhEU5BYHR72Xuc6ZuAzyN_Vi2h7Wg2xfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=pwwcRfGld9ze51rCqkCsbO-9rRgJbtr71x42SwKPwBOq-DavQhKHIkhRB2oqTOMC4RZM2-CW6Yoy5WP9_GMtOy5ielVejx4fO7_Myp23u6G03-pPFavvbcM74-7b2qKY0CGdQ9DRkMC7J1PRbrqI8GtjbXk2mABBCDv8Zd23Ih8vz7lP6TEVVHXzjA59saO9TjvhWtBlPhtSIpoRuGd8UtY8tXrZ2_6VRsFKFc78a_k1GPQwd7Stwi6qBa2SGMe-R_1WQL6mlVUNHDUSp6Uwz6KWDsENi5G3b3h9nxPZ-cM7l3m1l5uaEuhEU5BYHR72Xuc6ZuAzyN_Vi2h7Wg2xfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=C0OeUSkebvr9FlQj9gXORzFwBfWyrpFoZm0_7mB1DwaaB0sNGu8ygEGeUg-gmys8N0O-dIpjqmyRfY_1EVNK8KhZxj40b6DwNBZ4loeyyqEBz1HNuJRH4yFaksuJqEb1AVOzWfzluGlJFAGcuQgixhUbFJrtJR-0bvTSihlhJ2Bd8JIkpJ1PPYbvDWTLBdqmY02j0xB--IduGHySJ11UCBZ1bev7SJUMVa58WSu6E9Lnxw4bs-S3w1kM4f_b0ezTy8hlqHONE8oXWtyTk__zYuPwlrFgYeIv_lu8Hcso3Ng-5wJfXwrAmb-I_F0_0tsEgf5WUFaa3Da0hgkSwMdrLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=C0OeUSkebvr9FlQj9gXORzFwBfWyrpFoZm0_7mB1DwaaB0sNGu8ygEGeUg-gmys8N0O-dIpjqmyRfY_1EVNK8KhZxj40b6DwNBZ4loeyyqEBz1HNuJRH4yFaksuJqEb1AVOzWfzluGlJFAGcuQgixhUbFJrtJR-0bvTSihlhJ2Bd8JIkpJ1PPYbvDWTLBdqmY02j0xB--IduGHySJ11UCBZ1bev7SJUMVa58WSu6E9Lnxw4bs-S3w1kM4f_b0ezTy8hlqHONE8oXWtyTk__zYuPwlrFgYeIv_lu8Hcso3Ng-5wJfXwrAmb-I_F0_0tsEgf5WUFaa3Da0hgkSwMdrLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=Envhj-kXOemORarThWuCwny0xP0E_aTfch21alSvVtVudyVzp9Z9ccZQsLkJhIYhmab8lfAsrMi0tN9944xxft2D1qAw4QZBf2p00z264s_1BDP7kak9Nsu50XWHmoeyjqK74jKBu8lQ_THVF6a0OmxB8_R3qDKP5qkg9t3rm86ffJ8VcTINir0HFsayX0ph1TNPyrG9J7SiXTl2T_wiiu82LeVevPbyC30IbWj56r63c5mZQeo_J3trTUw984bSPoaPgdPmlsP4FfEOM06m-rnP9DRCaaCCUjIVVdSjWvbQ9Uk-Rn6kZASOoXPcIzn-5f15DMk4uilmblaue-Q-pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=Envhj-kXOemORarThWuCwny0xP0E_aTfch21alSvVtVudyVzp9Z9ccZQsLkJhIYhmab8lfAsrMi0tN9944xxft2D1qAw4QZBf2p00z264s_1BDP7kak9Nsu50XWHmoeyjqK74jKBu8lQ_THVF6a0OmxB8_R3qDKP5qkg9t3rm86ffJ8VcTINir0HFsayX0ph1TNPyrG9J7SiXTl2T_wiiu82LeVevPbyC30IbWj56r63c5mZQeo_J3trTUw984bSPoaPgdPmlsP4FfEOM06m-rnP9DRCaaCCUjIVVdSjWvbQ9Uk-Rn6kZASOoXPcIzn-5f15DMk4uilmblaue-Q-pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=C0ouaDua6uHvQAXUtRmXfZ5mi2wWFvsApQwAacjucjg6IXmBpCXPLelqio4pPWAKPFl9xqrzR_v9qI9-WVTxzXVQccvLnnQ-EiA60Cro4uX-AbpM3BaQ541Dr4ECozZZsno4JyBbCzuAD8tf1pu9-KMQNfv_HAJDF6FUTfKBivp7RCU-HXNvoUBcfjyJ5_A_dcKzHCUKeeKVwGoWXoj0yUA2NZ0lS_L_W_6apX_Hi_sMH4QzjscyZ8ZXJkymGpD68IyYr8Y6ocTc63dKYrjYzZuye_tnz2fhuULFB0FZqtdeWJ_c1Rvgj_EPuzrkX6ufTh-BbCitf7OVLtedAUTGHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=C0ouaDua6uHvQAXUtRmXfZ5mi2wWFvsApQwAacjucjg6IXmBpCXPLelqio4pPWAKPFl9xqrzR_v9qI9-WVTxzXVQccvLnnQ-EiA60Cro4uX-AbpM3BaQ541Dr4ECozZZsno4JyBbCzuAD8tf1pu9-KMQNfv_HAJDF6FUTfKBivp7RCU-HXNvoUBcfjyJ5_A_dcKzHCUKeeKVwGoWXoj0yUA2NZ0lS_L_W_6apX_Hi_sMH4QzjscyZ8ZXJkymGpD68IyYr8Y6ocTc63dKYrjYzZuye_tnz2fhuULFB0FZqtdeWJ_c1Rvgj_EPuzrkX6ufTh-BbCitf7OVLtedAUTGHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwsjJEBvGR6DETBxRni9hGLj983dwGl5LanuBbyPumc3gkO7Osim33tPfNlxC6Br8Ff7kb7mtRP4JC5qvlDqVfacrkP9w7CwP0XoBPzMt3o40KYO015CNakO2UTEgXEyif1Lp58Bwv-PzKP1ElIPotvFTrzrPNZ5cqlTkBI6ntQItpUgzqErayWnUMCRrtXfmkO0v7aGV3D-Ecj-1QOsLPY6gpvxoEvNYCeeKZ_ASWbuXKU8PthQYmO6vIR0ym7qbTRcK4XQJbpIljnf75ltFjXZTKYMOBUgKNfW7jWlQ8VaX1JWj91yQj-2Nqu19RGbacnX88huzAwcEfL6ZKSUVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=FaRyVhtvrmWg-kGoQBE98YF21PC9ZbMbRxixQtdbMsZqhc7rY-y5Oer2AN11oYbegsWDH5OjDx8YlgyxDk72MahC8I8Ba6F0PucRgi5TpjGfbOlujbhJ5ECMq_Oq_ftjagiJ2V78ThxqJ53dAJSXzGUlR4Vi4O1Osdp8IMC2IfaOVs1NPVkM9wFN39ZAOpMDNVzxseTemd42-EZhaKG6da-QLtWJRsjbyJyT9Ve9kf7AoQCjmAuB2Sq_aQpW2kQsubT07uqB6boEBBYwRh6CRyaM4-AEiqOdWt9fdkb4rT8Csx20s_GfC9dy_Wmyqz1bJoO4TaZhQMC5z5L_zs7FczzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=FaRyVhtvrmWg-kGoQBE98YF21PC9ZbMbRxixQtdbMsZqhc7rY-y5Oer2AN11oYbegsWDH5OjDx8YlgyxDk72MahC8I8Ba6F0PucRgi5TpjGfbOlujbhJ5ECMq_Oq_ftjagiJ2V78ThxqJ53dAJSXzGUlR4Vi4O1Osdp8IMC2IfaOVs1NPVkM9wFN39ZAOpMDNVzxseTemd42-EZhaKG6da-QLtWJRsjbyJyT9Ve9kf7AoQCjmAuB2Sq_aQpW2kQsubT07uqB6boEBBYwRh6CRyaM4-AEiqOdWt9fdkb4rT8Csx20s_GfC9dy_Wmyqz1bJoO4TaZhQMC5z5L_zs7FczzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=VvvUUHiEG6776jFjM_ItS2iBYfweLKLhGSesZyTAcKV3SGkZaqQIZVqjju7iSovccwgY0oTjKz7JL493OnH63fixx7XD7pm9DI489-nLMm5EK5ajyLFl00Nz5h5DK7YpqATjGaUvtgh9-U0pU9ATyCDX5mNTEXleQzlYv74Y10BPBqh4_TSkUp9x0WQPysERJaCZDFmFzrp1Q0Em-hsyNJr3HGs2xDFvj8UXDPxaiMHnXpNWbDfwK3UPVuO7g3ajJ2qxyzv4BndqlHAKUsI1KZc549HGZLx8WxcY9Azn-zuhY_cqEAze4eR6uF86n17eeb_SOkNvagGdAmc53syvVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=VvvUUHiEG6776jFjM_ItS2iBYfweLKLhGSesZyTAcKV3SGkZaqQIZVqjju7iSovccwgY0oTjKz7JL493OnH63fixx7XD7pm9DI489-nLMm5EK5ajyLFl00Nz5h5DK7YpqATjGaUvtgh9-U0pU9ATyCDX5mNTEXleQzlYv74Y10BPBqh4_TSkUp9x0WQPysERJaCZDFmFzrp1Q0Em-hsyNJr3HGs2xDFvj8UXDPxaiMHnXpNWbDfwK3UPVuO7g3ajJ2qxyzv4BndqlHAKUsI1KZc549HGZLx8WxcY9Azn-zuhY_cqEAze4eR6uF86n17eeb_SOkNvagGdAmc53syvVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v1SdukNYvvy9mfr1Agx1dIPBj7R-ysewpmPD9QNZP27PqkU-9oFvEnvLR7Me4VdkCtQVIcjM5Ji58i23rILMtEOpYtM87TS5hDKPM4CX0mmo57WC2uMvQubaSVy8K3mTVoveun0qZ9Ll0nBy4siOQ66kIGYoEDgb6AD00nst0XyitKJzcme3H7QJaLZGkRpPybYsCW953Kea607TKcnHcOpyOQALGXw35WlElvwwLBbgghISuYkYBs8M3jtPTnDw1d8YQYVjOQ5tt7hbQnJMrMVKjbT0E9tZSBOnNQBTkn90pkpw7y7wDMtR58tQFgC8E02CigC7xdOsKPYydNVixw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FVZfXl8lZ58EPhTA_1ve4hs6oGwcTaB3e3lcTsxkh5udB_RDIQqhqdgAoFIiODHvTJ0SPufPUby1guGEV6BjWlJgGemSkscePpmNwzAvyarroXsmwxNVgR0Ou_mK6hTGkvCYrAXZvnqnYBmSgk_VLpwnd8oK_dWiGn-uQmT7raYbD6Mn-jPsV9GbEt8bAcmzDGjJGoFFsXlTSQQorvAfciIa3UwfTZ-H7KwekfT7AWUnSCd9POl60bAEgsi9BgfOG5zC3LVeYlAM4yEUKSkrzkYykW487XMMwOpBbVKYK_4hcgBuGZCC-NAbDbwtyFs8FJPbb9yA8Q-4l_lDJ7dr4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=ZH63c52aGuVDOx5x-Iz6CYAkiqwTYdGeadFizYF_S0QAA1JuHhqjjWFbIUa-oq5r85cyes58JTSFODHMv--zOTySeCn-Fum98Ncuz8ch18FUeKUCyza9qNiEKpm8BC8d0l5pmZxUXOJMfMZZLRR57aSQR4ftqPNbwFSwlMplBPVDNZ-FE_AQhadK7ZuwixMKelBaNohGa821wuRTb-u881WGiGzeCOEqieJMuz5Bu3M9hLNol_DmaUHX0VP4LzEQzHpnoi0DHB6kGbHF9R1CsA8yqMTKi4mjqoQjJ0WLBRR7KNGPpZ4WyGmbJytICpU69jQG8DY6ZTONpWp1TZhizA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=ZH63c52aGuVDOx5x-Iz6CYAkiqwTYdGeadFizYF_S0QAA1JuHhqjjWFbIUa-oq5r85cyes58JTSFODHMv--zOTySeCn-Fum98Ncuz8ch18FUeKUCyza9qNiEKpm8BC8d0l5pmZxUXOJMfMZZLRR57aSQR4ftqPNbwFSwlMplBPVDNZ-FE_AQhadK7ZuwixMKelBaNohGa821wuRTb-u881WGiGzeCOEqieJMuz5Bu3M9hLNol_DmaUHX0VP4LzEQzHpnoi0DHB6kGbHF9R1CsA8yqMTKi4mjqoQjJ0WLBRR7KNGPpZ4WyGmbJytICpU69jQG8DY6ZTONpWp1TZhizA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpaFS7azG7m_KoXwQ4Dg5m-ab3agISpkrYHzd_WFYqU3FH_5iM41bGtakPlHY3Aod00A_wTlVJsAzVUtxgUiXMKu2A73qkxhIUnW-Zi70UdYUldPWvf_7i_v0DoyM3EhNUP5lXGZfnSTWXtk3oQ5nMjqfvXT4ooGkFVFpYVMk08_82cm3JybXXQUu8Djabxno4QkAvqhGmwBDHhrEKPRAwG25oqROS6w30nspa0l-Zp-_YyVvm2iTD8SOgNjnwlelKGJtpn-Y2587QY4W-6K8g2bRMOP6S_5tCWI88Gi-7sGmIcqhauHo8gq8_fYzJvSqZhY-eOjYL7Ucyz7pu-Qvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTVqzs9Ej6i_GGwa-NNUtLoucerIgQkwZmvIVB221IHiUSk3NT3pNXxMsaODZ_c3nRbUEbey8xOXzmF2uWunCFhBA3MrzXR7xFQH0TxJ5J90hWyznQ-5Ph7aGTHMsfLEu_fg6sPTBvcMaFzeLLHFXIx_9PqznJPPtKRrqF3gUvCPCswtfFG7zU_mq-h4NzKJbDXUkAvNrAzEW8V8uVH7Hr4ydJDIYKQUUCFFQa9c_WWaXD7egMh4RQhRridVWzdDlBwCvfdze7EZN_wORuk8LiNnkvMEbJirUqpZVQ8_yFUp8wCEMtMf2stHswsAUnI6VOUr3adQEhSCqAKwD4LLAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IoZgOkSb9nqWZw2YnYqIVQNcrvwY8o9Y3_J7Tw-JUJ975auYwCk_RPWxy4rWkhkGFD0RhJjKXGtmWj3ZMQkkvdS2yJZcYkvDKYQ1ejw8n4KJckfSWxrvwbtdK0tHK0PdozFxonu8Cv3xVpjmNYPzS0alZ_nQxUoYPVLWXrIM5EuzDQif2bSO4_bry2qMUxDeR-xM6mLPGUnpV7li-gFRPF-VzYKY1mt-c5rRgRNC3ijU1149ZSuHwBmtI5o5krOE4JVYHE374uTJQ9eHsX1yAeH0VKMRTeYv3lk6d3I_J3yolAvKYsHdLFMuK4wfY1YSckRvr-lDxFaiLhqmlQ7RuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=dfnYNcCoPGAZX9PhueYTVzuvjUB99a3NJaW9rBDt-tyc8C86SZKV-nFszanz31d_w5ZdGCaTNaX1IU_xnVlfEc2Pm8HRL-6XBxJUDMLb08AG7yaghVeJDqqCPODREzlTDOj3Vq0bmYrOxy2dB7VKjvJJ3D3EixGcUwXz3CclyqwhRbIbVG0W1OWDnbyIfHHpgrb3_SSxxfrfdCkNmmMIKpYgbfNPF3Ud-Rg7lY8XzU7NWQtLFAo3KsI-CgJ5sBh3sDLlENvklS--FoqC8oiQ72Z2zM_dhDOZ_oDG7R-dgs8UY7rJT8zjp6FjbAq93lWXmOqiGgNZrNAY40XRp3Jj0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=dfnYNcCoPGAZX9PhueYTVzuvjUB99a3NJaW9rBDt-tyc8C86SZKV-nFszanz31d_w5ZdGCaTNaX1IU_xnVlfEc2Pm8HRL-6XBxJUDMLb08AG7yaghVeJDqqCPODREzlTDOj3Vq0bmYrOxy2dB7VKjvJJ3D3EixGcUwXz3CclyqwhRbIbVG0W1OWDnbyIfHHpgrb3_SSxxfrfdCkNmmMIKpYgbfNPF3Ud-Rg7lY8XzU7NWQtLFAo3KsI-CgJ5sBh3sDLlENvklS--FoqC8oiQ72Z2zM_dhDOZ_oDG7R-dgs8UY7rJT8zjp6FjbAq93lWXmOqiGgNZrNAY40XRp3Jj0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=Nwi0Tvg0-XzpxJ-mTbLlQs-wyszg3FH0lQiAn-u8OrBijl7URumy3R21O8N6LRGsyx75KladwCh91gD90BQiPlUXlfJxaRZE7dwtuttFU78XCcBdYCzi9ybRxCpC2spl-ngEYdXw4W16pukhDWIXwkGE3LHQkFHURy6Jgri36mOo3DKYVT1iNSbIQ3G6XrT--HTzNXTsQy0JZw4jkZyA5dA4TDk5DpSq5Apyuxgnger6Y1djWX2tPnhvBBS-aqAfN2dFAElp_cg7VFNdnA4kXz3-DvEH_104ldmJaw8N7ju3Kc4ELqf3rX33HKFAmUFtHDZK3U_VNnpMuyt0dZT33w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=Nwi0Tvg0-XzpxJ-mTbLlQs-wyszg3FH0lQiAn-u8OrBijl7URumy3R21O8N6LRGsyx75KladwCh91gD90BQiPlUXlfJxaRZE7dwtuttFU78XCcBdYCzi9ybRxCpC2spl-ngEYdXw4W16pukhDWIXwkGE3LHQkFHURy6Jgri36mOo3DKYVT1iNSbIQ3G6XrT--HTzNXTsQy0JZw4jkZyA5dA4TDk5DpSq5Apyuxgnger6Y1djWX2tPnhvBBS-aqAfN2dFAElp_cg7VFNdnA4kXz3-DvEH_104ldmJaw8N7ju3Kc4ELqf3rX33HKFAmUFtHDZK3U_VNnpMuyt0dZT33w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=h6d03dq2hDAJjXx3DZdiFW3B81E-RgIxIGvyydkAa5Z9EWUezrzIc4y5dkqNNT9hKm2FibvYzrdEUDbGsxnl0iVq--mAPqyiKDUn2N-It-tgXOFsXqjPU8tzVPOncS5yF3iOVmFbO-QcuBKd68IJdQ1fN-2VsYz6htsJSNGlWg3TjDYCAlqpHjTjhoBc6nn2T38HXMKCUDv23bDzuunYdbL1S0n6KMeO30rIXvipMSBs_eIOje5ncj9yw1AmRcPYtpaD1BimVbsJnGrngD-Kd95ugTVZu8SsdywQ6mUsTzdfUK_9PXzRU7KcmGg6qv9mneolhfY5EJGJBzCqfASoLzmnmK_S6YBlwc_Z2k3VNAlAIOlvjvfY8xYwrrl5WlBqw4p9TWaP1D3hArANiN3nkbScyeN-AzwJEy9vTaJUoLFhJBMNFqK74QVqOS3Ws1Z8k38tWbBuuKoxcIzqKPoo44tweWJgXoMsDZiLTc6vDLVmeYBYL-s_xiHY9NQHZX_UTrUBdDLFAh6wwltgRmnFZnWVuykDQ4T0nbis5lLPIMcA7nAlCqrZ2xRfJmS-bsnn-7z7mWUOJJiNtqs0F3FdUsFjjcPvhCqRWxDGqJMsCv9GEDrxxgGbO6beB3AZH5xjkwWQtd0XQq29Ioao1y1SZy_vk0RSUK09UK0Ff58G6kM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=h6d03dq2hDAJjXx3DZdiFW3B81E-RgIxIGvyydkAa5Z9EWUezrzIc4y5dkqNNT9hKm2FibvYzrdEUDbGsxnl0iVq--mAPqyiKDUn2N-It-tgXOFsXqjPU8tzVPOncS5yF3iOVmFbO-QcuBKd68IJdQ1fN-2VsYz6htsJSNGlWg3TjDYCAlqpHjTjhoBc6nn2T38HXMKCUDv23bDzuunYdbL1S0n6KMeO30rIXvipMSBs_eIOje5ncj9yw1AmRcPYtpaD1BimVbsJnGrngD-Kd95ugTVZu8SsdywQ6mUsTzdfUK_9PXzRU7KcmGg6qv9mneolhfY5EJGJBzCqfASoLzmnmK_S6YBlwc_Z2k3VNAlAIOlvjvfY8xYwrrl5WlBqw4p9TWaP1D3hArANiN3nkbScyeN-AzwJEy9vTaJUoLFhJBMNFqK74QVqOS3Ws1Z8k38tWbBuuKoxcIzqKPoo44tweWJgXoMsDZiLTc6vDLVmeYBYL-s_xiHY9NQHZX_UTrUBdDLFAh6wwltgRmnFZnWVuykDQ4T0nbis5lLPIMcA7nAlCqrZ2xRfJmS-bsnn-7z7mWUOJJiNtqs0F3FdUsFjjcPvhCqRWxDGqJMsCv9GEDrxxgGbO6beB3AZH5xjkwWQtd0XQq29Ioao1y1SZy_vk0RSUK09UK0Ff58G6kM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=JVt8X8Jd8z4FhPxLYUPRDt8otjKbl7EBGRoX36PcUfzWqtrzMoBNsEyqpzl6KZlzRbIVl4JE9IauuoXtClFjYsCDoq9nYeclcz6xOP6q1E8NlMHFSzntf8DyxLmp2r369DOuDVvUurQkIQsN24RSMrinSSBhOcKPHx5RdrerCyQ7BRNp21AG_EwpMaKI1756Icq-UrVPD1kJhB88EQwhvKfNou6cyBm6bGtd62jn8obirtB70BPOf8rruSIrON9egkdhOhWOiOr35VQdwrrDwcw6oD4Rsl_tXGRIwh5wqULZEAbIgBYbpfWLKXaK__21pvISN8ocPqg0YgU9L88N6gECMH7O6Via9fq-J29DQUATMCvx0e3qILbV8JTCtY0pK4dyqxyAWbtcoB4wpL0bXZpMkG_7K20J_nebcTgOVNyd501n3MuqsGCISdzuvXMNRqAmlqSnGaVXZ1JbJ139OGAUNWwnc4x0JT88g9J2LneOnwcbkwbfK1tSOmllmnDulCkFqekkTRAz-KZTbZA6elHOUHn6h8BryDyau3QOha1etARSIlvO7dee12A95IsxSFK2DLfMrZQkk0ioLG3ljlbbGukbv-7ydGCyF7YWq80_G5K5Qc12_9JWOpAtLmr-0jd6ex2Ri49hy-lET41AaoQy2S_s2qfy03JvU2EigOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=JVt8X8Jd8z4FhPxLYUPRDt8otjKbl7EBGRoX36PcUfzWqtrzMoBNsEyqpzl6KZlzRbIVl4JE9IauuoXtClFjYsCDoq9nYeclcz6xOP6q1E8NlMHFSzntf8DyxLmp2r369DOuDVvUurQkIQsN24RSMrinSSBhOcKPHx5RdrerCyQ7BRNp21AG_EwpMaKI1756Icq-UrVPD1kJhB88EQwhvKfNou6cyBm6bGtd62jn8obirtB70BPOf8rruSIrON9egkdhOhWOiOr35VQdwrrDwcw6oD4Rsl_tXGRIwh5wqULZEAbIgBYbpfWLKXaK__21pvISN8ocPqg0YgU9L88N6gECMH7O6Via9fq-J29DQUATMCvx0e3qILbV8JTCtY0pK4dyqxyAWbtcoB4wpL0bXZpMkG_7K20J_nebcTgOVNyd501n3MuqsGCISdzuvXMNRqAmlqSnGaVXZ1JbJ139OGAUNWwnc4x0JT88g9J2LneOnwcbkwbfK1tSOmllmnDulCkFqekkTRAz-KZTbZA6elHOUHn6h8BryDyau3QOha1etARSIlvO7dee12A95IsxSFK2DLfMrZQkk0ioLG3ljlbbGukbv-7ydGCyF7YWq80_G5K5Qc12_9JWOpAtLmr-0jd6ex2Ri49hy-lET41AaoQy2S_s2qfy03JvU2EigOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=Mmc5S4VrME3IM69MIuZYKK4I6E-sowZTB7ybLkIu2cpH6okHvTY-w20cSV-SaYQIUZccakmEAEqssFw7EGjG1_NZNWvzRDxespittodvMOnAoGOoQXKhDGeznFtreG3EnYckNIrGMWCYZXuo84K7H0JDfIGswzJ4yOT0cVakJM8-SYeTm0VvJ7ycd2GCu4N9ud2D45ANniEfR_MqmdytitY4lXIgnVtfrr2VVaS8wdeNpOQJqYZUt5lhCrRNknAP7ZqfbWAzWGOasbo5p9sTqxliGDaGnTGExivxVzFb9JHNod6KIRu2-2CzmyT65l7PX9UXCohc4Qzt4L5_LOK-RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=Mmc5S4VrME3IM69MIuZYKK4I6E-sowZTB7ybLkIu2cpH6okHvTY-w20cSV-SaYQIUZccakmEAEqssFw7EGjG1_NZNWvzRDxespittodvMOnAoGOoQXKhDGeznFtreG3EnYckNIrGMWCYZXuo84K7H0JDfIGswzJ4yOT0cVakJM8-SYeTm0VvJ7ycd2GCu4N9ud2D45ANniEfR_MqmdytitY4lXIgnVtfrr2VVaS8wdeNpOQJqYZUt5lhCrRNknAP7ZqfbWAzWGOasbo5p9sTqxliGDaGnTGExivxVzFb9JHNod6KIRu2-2CzmyT65l7PX9UXCohc4Qzt4L5_LOK-RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Idko7lCW7BwGGMZRU1WQfGoxnHEWFkOvI48_ydrbZMTfkHxpJsj6XgeeUA-YFD3PSln5wDV5CBlyWKyb-6c9qHMCnzdOXulwN8DBy3LE9VZN53rsJjAeKAuWSXm2NyasXKceuf7BlVPykRiJ082gZ_D8xSuWpR1w0HOlIOv18hJzLoFRX-HhFdp3mNlTl7lEN-aRhzyv14yW0JrQj26tRjvlbSvuKkvMhMyES15MxeTewV2hVTa4zqjN7KDg3sX6nXfBG1PS8jyVZWDh82dmq3jixu4UhVrDrE0jEn26WkO75djeqqtepPxsqsFxBXP4HmD2BekG--46bWw7nUTV2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=U82NNj8nYsvqISTBVPvqwr5dFiDTPPZqPnoFC3vW7LzZgbad_1XBQphpgqe4wPXjdqmTxctSqnfdHKqvEascvTMID-VGrswPxIubuTYJeiRwr2a4MIoEEXEOL87_UBwHjfbfe5ZhlJhJeddKczkcUl78X9fhlftCC3iiYjzB6CEEBtx8FAtQfEJnM-Obc2nDUBFs1_eLEr7v66daU4j-JsqbHPZ6SfsgEIIze3LuktyZP7vXTE_eqjO9wsikUIWwKoX4cyEX9Cm5SqeBs7ua5XB5oWC2sWchfsYkUL6VaJX3QA03b7kXaFH9DIjQZuoRRCcpMAcG0pPCU-U9xx64HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=U82NNj8nYsvqISTBVPvqwr5dFiDTPPZqPnoFC3vW7LzZgbad_1XBQphpgqe4wPXjdqmTxctSqnfdHKqvEascvTMID-VGrswPxIubuTYJeiRwr2a4MIoEEXEOL87_UBwHjfbfe5ZhlJhJeddKczkcUl78X9fhlftCC3iiYjzB6CEEBtx8FAtQfEJnM-Obc2nDUBFs1_eLEr7v66daU4j-JsqbHPZ6SfsgEIIze3LuktyZP7vXTE_eqjO9wsikUIWwKoX4cyEX9Cm5SqeBs7ua5XB5oWC2sWchfsYkUL6VaJX3QA03b7kXaFH9DIjQZuoRRCcpMAcG0pPCU-U9xx64HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=ey3xo6bh97J2wjfK-MvfKzAWGEeEgAsGqANUQpSbhQubOdfL2gIaKpDnObgvqo5OeNl3vPSxSCOEW3WGpXaTnu7MxajqkLBKizY0hh-SPV16DUXlOEpHnZIEA2rYU_sgb-US2pl1PTR3sqEef9Tkf_16-h8Wv8BoE5akkpwjVLiN23Jgf9BhTAmxzyfe2DW9oQfLTtCe_hWAGj4dXfXJgfMNf4pyHQzybkYUeraNBhiA5uwdcN8p6eIfRjH_FUj5od4OKUPqQUqjbnj7XSAmyKrWShfrdqbW0Xdz1mTWHBwdT7ujFemSDlLSWP8Cs55mMEs1AQGPl-wA_Y92DorGsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=ey3xo6bh97J2wjfK-MvfKzAWGEeEgAsGqANUQpSbhQubOdfL2gIaKpDnObgvqo5OeNl3vPSxSCOEW3WGpXaTnu7MxajqkLBKizY0hh-SPV16DUXlOEpHnZIEA2rYU_sgb-US2pl1PTR3sqEef9Tkf_16-h8Wv8BoE5akkpwjVLiN23Jgf9BhTAmxzyfe2DW9oQfLTtCe_hWAGj4dXfXJgfMNf4pyHQzybkYUeraNBhiA5uwdcN8p6eIfRjH_FUj5od4OKUPqQUqjbnj7XSAmyKrWShfrdqbW0Xdz1mTWHBwdT7ujFemSDlLSWP8Cs55mMEs1AQGPl-wA_Y92DorGsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKWwGQHHs-uUjOp97HoIojT7qd4LEZlQZ_9wDor8ZeP95Bmo6GBGaqkGtBkUcTDmasQZV6eOGxXTRlzVu7eP2Bs7k5xXU6EcADkrYXJdEb6XKYVMJrcPZWuQ75YCHrWqnVRN3Sl2PL2Lrb-qQHGk1lxV8EG5XiClidTxUPaUo4Y2LyAhsUTyR_JUdMoBljCZXE6Jl59BXFZXWPofAm2X8FcgDEQuCbgnsOKcjUUt9Ovyl3753q9V7Pgb_IWin0yxyJDTWKY2QDt2Sl48B_itZOHMaL6cifvVjzqtPjFhZIN7yfiqXrQZe3YAcFZFH-ALSE6rjr_K_Ai8DJZDnf2cig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qsntr1FulISu29asj5Wcyy2uBiZ_XPMkQP8o4uDMxFvnP0lRjWVPaJmWc5ZIWeh536Bvz0o191p7gB9wQC4oFycTqllkGkLUp3JLBv5LuXHeakQJhLNqhgwnRxglfakRC9T37tN05w7eI4WrXWQIuk56j73UJlTT2mpF6496_GdiHy4eumlH8UBIkU056kOxlFkQDpwyQpKPExmqoqBinyJi_HqAkbfq4K34QPHoNJftM54Rfyp7o1bIIu5ICT1HalL_Wso6p8R5k7qNhdOCQEqFRIg363ox6coKyjm-rTM7IvRSDSiMtewKEPKJ12t5eefGBCZOMOOvjj4IyEq6Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2BJVfFAA3-Inm7dZ09nRMwGyqGwcnUcJUAXUqRXhwiyPZfXiEJAsJ6fqJfRf7TNamc0Lmwo-Wv9M0u3HFq7aeahHLoGJg4z4LOxMYdQUTlU4tmR7Vbub53Q6-mJjjiY1k_hAYjPck2ugDvtzyXDZjE7YvGdcm3qZntJKy8qj8LHKuV_4MNkbI0tE-FAJ_sBFr8uofrXkP5KLwd6HgdtHCdOi98w3Wli8uaBnved9XWQ9uyMV05AHwFbBLRgsumUHy8dkBnkR22RysMJRjMC919IrrfrehsYbeJL47E5l0SjmwCpVPSj2N80bfvelMQjQ7lHTyj2QYRd_qRTMt4OsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EeTXafDV5snC9zhhhbVqsnDUUG_UAZYFRES5GpGjuHcPeDzGfjrnXLhN-E4FAawZXvq2tWkX2m04pekkW-5iq32EpB8yr-fBqj7--5AeOEqvXofUW_uM9mHclWHypM6p_CgnDbOZVrsW13QtpfiLBi0x6i1zhXPgkdcaCiXxSsM4MKf9ahyExh4AVodx-auz92NOuMT1dbiVWSKP3cSq21AhHz8u9EhrREun8E8oHVcm8yPg49ayXuLX-TY7uoenI-Rfdzg7g2m2-pXdN0ukRRSt9YlcICUmTnQDVSikqcAmxGXw_byNTHf9kj6qTedZsI2bqlTA4dV07rL9ahwFWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHUhcY_0lJjkNLFEmaEpofMiNPhz_B8nZw6hsle54KSkloD3dtzcwErkCcB8k3J6-oEZ4gu3of-HUsh4onfEXCnbCKofkTpByHBjpo9wbtdZCas3SUY7o8cqCFU1PBrK7049Hdw9NsdrAOJ1eIFcVZ_v-qp-YG6euhIpWibbTUv3m0zXQTfoO4L5cpY94lLvZ8lfK90PiUHIqG8M5xHteegmG459u4hzHiQoUmLosCMNGMw9K6XUStD_6UslvcG_3tNyFr5gRBgLiCN8LLYMFa2DTYFoLihkhFpK_SPXP202h3eo8oJbLsTSuhZMwC56HSwsQAhSdwXVx6KV89T4-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/petzrdAjhh0Qols8iXrs98BtyVtI1CdvZfC-PnhAeUAflILaiR1CB1Y9AmkwJSJT_l2G6ykQI5YgNcYY5Bc33pKrDE2uXz7f-g7l0VaMZhoArJb_j0RR9J6uVPd8nLR4SZ4fUq8IBeXCETld2CcoCnO5O2ZdkIngDSQIACbex7hVW_Ju-pTVFyNu44nqNFmXCOb7R5xG1nbFfHa-Thud70Aad416CEfd7v98nutXyGtiYzI13fj_liO2e_KjjU_8G8E0yPgRt-jGihVJAsvZR72e0r4zcFsdIFHZdhCW14V8XgIFhu_Jpnwkaym6qeeUf2uNU8bnG46cjM-RlUOr9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIS8n9hjUtE-S9tcSxuWK8pFeDkH9Uq3Vlca39NURJIf21TSSywCKASPKLx2Q13uGXFONJtSWNEOVdeCB48iAxeXF6jZ_IH_ILSzaPTkB9ZVudirsFhPazb__IyZqer1zd5N0DiJ6frzjtoFGC9_q07P0Pokux1suePQ4V18w3WA7v7PQKTMSkFHDdZNc6sDB83_OVwFuLhV-2hvSgQlTn6bBDf9ikCYW2iK6XTFtrBucVNLyUXLdUoWo0jVFRwLLJV5NRQdABQfX8g5c4C4laCJ3UBj_I9wuO2G-0WP_t5Xq2gLjT4COpZqOt-msXwfDfRLoWuxXzPjzB_YFIznfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gKsl6BfkBi2DdW0Ba7SWo07aQn660BveADU_De0TxgczNhElvlEsLNsaz-BNUWQeQgHimdl3T5oNaf3HZ4tzzNTNG_vhvvVy4yo61DKn0BcfuAx7rmkSnEmN3ZoqN_wT5GDvxVhlAO5SZcFo1YYUqBifjHDO7KmIcv7Nb0Cr6BLOoAA5CX7Ck9NMqsHhs0-qtm-dvoYxp9XNm9hqAc0jSmtah8Y7a9hSjZBrXIicyZ1DTfoaaZMx9Byu38AEsYm__no4uyg58CCh2QfiDCvlJcmC3XV3XkfRrQiqv7Q6WzLDfdNvPH5NLU_EHA6gan_nW_ZJ9-ZviLJUVazhZOvd3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j9Tf19yNBc2cPWuuFLGAvD-l1TWhsoiiThi4M-Pdz3zySG37EPIVwH-DZHU13WF4myoGc6xZ_7zsJRQIB0qYE3k3c5gl_KF-ivUhLl9dMCEKCAOo-wMU34ppGMXsGU8scovWr8FoYTixDm9XVhuMgeUDnXiDlP-OoP8Uk5QUhpcGN6UNc0DjAQzh-fa4bHewBQhOJkhSl38UYKZm2aLLAMIziityGi1zyioL4kPx1E1fJvmcUcBYzzXNNs0pkInLkMsjKwn7tbljJ_lIADDB2R366AxxnUQNaXTqo5jYZ571iMHmBEWSpdXZzVtwbv_InnsZpkkxrDLFtuKxczNUpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BBbQ24xpOgDiyaNEhja7CmiIawKwKNDHQnpitEsEPTtwHCvsGR2hNdQ5W8emy6fYIr3mxamM0dgq3wucRW16waFMk8DfpZZpq73vd3j6ZFI7JeTxQjptsNoCuWQsnjeq6qAUwuhbktj9-ZYPEKnwa748oijaDNZTraGnxSlloLrOAhDBWCQ8VZAvDgSLbfNjVS00kRiDdWrqJr_NBVubLfDUMNTnjIABtyu4lAjmUqHYQrQCnV5YoNO4mSZMpcyseS5zgUetQ1p18hvY7sekDgO3JzhaIOmRlgOTPji5bt6km_yW0LPWGBX8qRGOylEnGi1GtXXSYhxp4JpwhKYAjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
۷ کشته و ۸ مجروح در پی حملات آمریکا به خوزستان
استانداری خوزستان:
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
🚨
دولت پرو روابط دیپلماتیک خود با جمهوری اسلامی را قطع کرد.
🚨
در جریان حمله آمریکا به کوهستک هرمزگان ۴ تن کشته و ۵۰ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=RV-95MZDXMfP5c9PBo0oIZD99UCaRv380xsfRtsXqwnBqBlW4kJhDoL7Gr93x3_JanKnqlZc_IZr2fuXjgSUPJ5oAEABFbxnJN8u49iPTSASG7QL5qpke1qYOv9NCjYVprqe3QzCowXdUlJB62mCK7VXNSFjUal5u2Tky68PNFoCx89OzxUOQY36_vLtkqr5r82J_LCN1aAATHashrfYVfwVTHvdAkZOJnfdTmMpM3pCcizO99iPQYuYcmhns4yZmlI4wY0BNCfdpyyMBHheCt3EbSeyeGclkvzrjPW1CNtn4iRQ0apD-tNpwLx7rOVsRArLp4IsAjyYjIX8GjbM5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=RV-95MZDXMfP5c9PBo0oIZD99UCaRv380xsfRtsXqwnBqBlW4kJhDoL7Gr93x3_JanKnqlZc_IZr2fuXjgSUPJ5oAEABFbxnJN8u49iPTSASG7QL5qpke1qYOv9NCjYVprqe3QzCowXdUlJB62mCK7VXNSFjUal5u2Tky68PNFoCx89OzxUOQY36_vLtkqr5r82J_LCN1aAATHashrfYVfwVTHvdAkZOJnfdTmMpM3pCcizO99iPQYuYcmhns4yZmlI4wY0BNCfdpyyMBHheCt3EbSeyeGclkvzrjPW1CNtn4iRQ0apD-tNpwLx7rOVsRArLp4IsAjyYjIX8GjbM5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IA_yMqXAHXPqpisO56yVIz5YgfrnvKh0pw81unj5ee52TpJ4TqwBBzEsg2ZS76_YV3TAF95KPaeH86EiS34wIr-6DZZGTw2HTDFxMoMTMJ3QjHRjqzfW4_yQ7Io1lo_JdUU_5WVPnuAJYhyehPjrSXf78wDCHb3AXtrC13Iv_bNlmqIkgxI5XVW8tIutwVXlrwWuz8q4DFmI3h9SkrI4RRneTivbc8aW79h8BNJxIWggkefSYNH4D7OetWPDc-mo2lV7RaqT7ty6li51W8Bls4mLF7jQE2ZYs0S-CkXvEQhtwMTwguyaMihkBk-_FkzlgRvzAGzouTO8DcRYHlY5Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qa_le11bULVdtkXgR29trAHRcljAykDIBnanNaG6G_VqAGOtZVpQZMGdcKziNXh5e0yz9oGYalwjV0X6Sr4aNjh5p5RKZDNK6LSIpl__eMAGOVRz3SN7MSTwmHVBCMx5YqkaVsKzvej50o-wqOjLzYB3WRdXHpMUbYFzsu6kkMaICAD7z7byO6BLcSK-8jJT5A-EzaioIq2pAqVRPl2rqeuOh7a0woG8fFpCeqREKUIXbqaQGoNUfetU_oGsMcyXMfsbLceSm6TgmhUdCyIvJV1-IeHnujOi7NxWTK-jC9Pmap9_zozOzzdnC-jDq6IT_MxNLpX9-QycEeDUvPfrdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=fskQSutcB_zx7h8chMSGoc3WjQNG5REVT-Buk1hZ5RXwVuWx_3GWW7usVTZd1YyUBIDcurXpEtzD6Ri-OkYm8ziq-UP2BfBBWSJ_odA5lMTGrM9g4KR9LQWN_NcY6fR6o3mF-srYZCamp9r-FBQ0mbBVtdjwoF6sE_asavTwMgQt_oC5Gbp-T3pi4kTfgyv6thDpZsypQschD76syBmQdgTCw7MpGITF5_oVuHPszdH4EysJYFtdDg9Zo6JZXbUHGS2Zeza4hIAe94OU6qYHe-ulxkivL19BBvpz8_w3RsJTIIjbGDKV7Ox9g1GLAxlLe97NEeqTiqgG8wl-nc9ugg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=fskQSutcB_zx7h8chMSGoc3WjQNG5REVT-Buk1hZ5RXwVuWx_3GWW7usVTZd1YyUBIDcurXpEtzD6Ri-OkYm8ziq-UP2BfBBWSJ_odA5lMTGrM9g4KR9LQWN_NcY6fR6o3mF-srYZCamp9r-FBQ0mbBVtdjwoF6sE_asavTwMgQt_oC5Gbp-T3pi4kTfgyv6thDpZsypQschD76syBmQdgTCw7MpGITF5_oVuHPszdH4EysJYFtdDg9Zo6JZXbUHGS2Zeza4hIAe94OU6qYHe-ulxkivL19BBvpz8_w3RsJTIIjbGDKV7Ox9g1GLAxlLe97NEeqTiqgG8wl-nc9ugg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=XrPPteTKweLMIQ74m2Bw6_5BSTQiYwXaerOYrVc8FCv6NVa33ug1hVnazdxiJqcspqR2jCMZvoDWWPQBjRWtekqHh-N0ftGqfNbwwhtEfVbAasstZk5tgwXWoBbuCTMnMgdFNOGZIQNLSq0qX1BGTCfskLrlbUYn4QGFApvLqsvRe-6xDoJ_XwhItlHX1URxI2sUflGGVaD1obpUfnvvQlqVEU3-djawJsj8sv_CrNzg2ngdQKuz1RlrlfsOqmNN13LY0btPRCtF3zayZuJb9vdWbTE8XS5QHZtg40HTgrsFvrMmnppZbEwtcGD6U0cS9dYDHp3Eg5JG_8ZVklnRNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=XrPPteTKweLMIQ74m2Bw6_5BSTQiYwXaerOYrVc8FCv6NVa33ug1hVnazdxiJqcspqR2jCMZvoDWWPQBjRWtekqHh-N0ftGqfNbwwhtEfVbAasstZk5tgwXWoBbuCTMnMgdFNOGZIQNLSq0qX1BGTCfskLrlbUYn4QGFApvLqsvRe-6xDoJ_XwhItlHX1URxI2sUflGGVaD1obpUfnvvQlqVEU3-djawJsj8sv_CrNzg2ngdQKuz1RlrlfsOqmNN13LY0btPRCtF3zayZuJb9vdWbTE8XS5QHZtg40HTgrsFvrMmnppZbEwtcGD6U0cS9dYDHp3Eg5JG_8ZVklnRNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuZacFdqglc-RfCnV0D8aoVTjubWkcjHKSw1_NFAwKjbA2uQYcFA-pP1e-w6pRiAkchUBE6EoEMTaHJYdpBB8FkbZaEUU7gQMCyKPo5jlixhlR3nMC086NQCJxCvLoevhdy3pIOBrs3B3iYCOlc_pt0UxOmmm5gcKsJ9ncuXe8eEdJ27clQbGHS6rwpHwoqP5xZRVBxAsodI4hmpK92FbBoaSHPXD-g_YFB75FtzWdgl0oWtqzBfvYGrAYtGK5SEs-4xK2d__k85VZz6Rl-ZVDXWEkNkJMWnTwSTGgW752_oZGmhRRU2jHLr0SdIrwfaA3Y-OkBhzbvvxxepY5wGMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ رو به بهانه خونخواهی خامنه‌ای راه انداختن
۴ هزار لبنانی کشته شدن
از جمله بیش از ۷۰۰ کودک لبنانی را به کشتن دادن!
قالیباف رسما و علنا گفت
«برای جمهوری اسلامی» بود.
بعد دست به دامن دنیا شدن،
با التماس و با تهدید به جنگ با اسرائیل
و با قراردادن «پیش شرط  شماره یک»
برای تفاهم با آمریکا
در پایان دادن جنگ لبنان،
اینها رو از زیر چک و لگد اسرائیل کشیدن بیرون
حالا اومده میگه ما فلان کردیم!!!</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRlhEQ-P7cNFmEW8JpnFdM55Mihv6fKyCJbn5ANjWjqwJ9YK3allbgGMK6uM2UlTK5v-bS2a_Pt8NNubAC_BJV1tMECTO2cx_4Cn6Mr2YwxYLQjQOfm7Ib4C74-4ZmcsUZnJNa7QagnfFy5xTiqQaO5gTGcfHMjBOV4Bx8EXQEnBa_PeQ4xgmPrDzDYOOr-KoYpkLeJN2tKbnITi3DJv8W8EJep_eC3e1Y0Ee2zdVc1UCT9A1xSMjbUhYXikzPe0dQTR_QaRifin1vSqgj08XgMXPT9KGUiTOT-atORBF3zsl6-fVU0SHUHqD4lSWP1MpWnxHPv3Cw34MAFKfGIcxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">داریوش، در لس‌آنجلس روی سن زنجیر میزنه
محسن نامجو در ونکوور کانادا، سینه میزنه
دختر بی‌حجاب ایرانی در کانادا روی
ماشین قیمه عاشورا نذری میده.
ای آخوند فرورفته در مغز استخوان ایرانی!
روزانه چند جوون رو اعدام کنی، ایرانی‌ها بیدار میشن؟ چند تا جنگ و مصیبت و کشتار دیگه باید
سرشون آوار کنی، تا بیدار بشن؟</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQeukGR0MchMQO4iHkGUcfIJq4E00afmAiOcPggfYg4nY8g4XaARxMp-ZbueytUMoo49IRvSbJ7hZh1-C6cQa8zId7fArCqqsKwU59j9ReBILJ97Xi3GLyepIP2eXWpUiWiebYe_Eoi-TxtzcTpfjehUuWTd0SYVzSoJ56ut5XsugkFV0tgZFiLWCGTVhhdKf-AIbzQ5_ex7oDU4VEeYmOyD3j0GcAwu4BPUzaCKwsLq8UExUbJD8SfPzQRk7uys5CDDCDMtCLjpuNLcQ1eA-Bc51jfX109wxx1BtE351mpKjRBjOv6mE_wzDITufIAqHxWDIhSf228NrmTS4LnF3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آتش گرفتن یک فروشگاه فیلم گرفته،
دادگاه گفته این اقدام «مشارکت در آتش‌سوزی»ست و حکم محاربه و اعدام داده!
همون حکومتی که با جنایت سینما رکس آبادان و ترور نخست وزیران و بمب‌گذاری‌ها شروع به کار کرد و قدرت گرفت!
بعد بگید چرا مردم در صبح ۹ اسفند
و شخم زدن بیت رهبری خوشحالی می‌کنید!
هزار بار دیگه هم شادی می‌کنیم
از مرگ و نابودی و تحقیر شماها!
هر جا که تحقیر بشید و نابود بشید؛
از غزه و لبنان و یمن و عراق تا تهران!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2QEjVGFkBCE7PMYklUVc7xvVrGNEchQnS2n5cc8BTmYWNCFloGZykXljfVY3RUyr8n29VYYUwcKCUQRpFZ5Pzz6bxj7R6OG2PCZIYVE15UqfqFayX_UkIl_F-mvfFhUheWcnZkHOI1wVk8ZWwDAbkCWMFnZ3mJvVxCTRhe-hmPVgwZBLQyDvlpbm6FJ8WlDLNjOhejr2OC_lTJUjyJQseK1zVMZcCk3UtrIw0jDGEpCqzZvAtPQ6rpubzI-99Ucg4TADVs4YP79lHkcxPOpG_J4WPa9aJVbdvOPwnoOpHH1QrNzz_P_iqWOdTh9NU9qFLNhhgc9IgwS4_ntg7KfJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CF5yhEcPXaJ7vF-k6EjGIfa5mUq8WVs1OO17g_wFr9bkEuOKa8HSdURWCHGIS4NDhsoy6Y0j39QuGmuCrRWo-lmXVXnbMgEtrGA89pE3lYoA2_k46v6PcfXkePV5x7T6pepjJNmTxnspY8MzSEZzqTPEjzYI0QMvH6bISVNo0l2lVXHWfF8cNcW18G-uGvGrVv_DrpS2wdzNFCwCJqKsx07FX5VyRMcOd6JtZdg_TRZHG-rhkyK2rZrvtBHpFTPDfOSuqJz5ne5e3dSrwXjESeFCYzvFl6rY1ciwR0a682FjQIeBlPUsM3ETeVGsea4bcG-JFwY1Py-zY-xRoTqgAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-KvntIrQMawnJOx2xUT22qDyly_jG1CQINUOai6m6U39Ut80LnZFJWWH5tdFb7lTBv3ao0Qtd7m4URIndkuIA4ulYahzvp52LPrD6qwYqEDa13GBb5qWZaLta8_OtUiE7XFBOiOFHTher8BbMyyn96plfaBNpP30lMmzzNrP3fOsQ5nq0Vo_71zVVoTaFOjuRf_fR0MGvv1p-Za_fd5a1ZEOT5Tp8rMYZpgBxiT-ceo46WJLZTl7xc0R3nTPpuh4NX4jpuGGK1eIsZmN8EZGfOCJ3yaFR0YDUvMwz5_EoKFNCDfgtnSM9wfSoGOEOZNnoq9avCi4Atnu_oLQ3X7DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scKOUYJM5eb4EZ1p8EaEB_gj910H9IbXmptzXsiObihZUKGEGLLwoKjDjgf_7BljHR8gtnvHQu5warHiSoKgb4JAgpsPNrkZQy9wnv1oLToDJ816doox6uz0j1VJ94jh3YevEq72S7W8NeNu3Kh1cIxueytc-o2kK80ckrLuQles4LwqaF84vWC_UdtCXpwOcV4-lhCXuLH6FMeqDZm2Oz3Fe1DSZgaTwRoWCyjLcsgGdlZ5Vuo78mYLKsdQW3deU-kJ3M-dT6WpiKJKw0CncZEyqvIvLnRqigPf2oQTF2h2gpqUzfZU8ogodg3wa-aqnfDrkjiLj0r-YBl0fculRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnskH5YdBBXrksSaiQ_1U-D4CF9dc6mplbSPc7SkYgYsiYvAoIwGVcMQOmGS5NuE7pxp95VHgaoRHzeuLNMld3gnZSr344pHfAVqNXihdzb5R7J85J7NK_ee7rw0lwajH9CGv_2szj-4C-HyTT65PJIULtCJQSz7d3HMg6dzgehuXG0IU1bxVbcVZ4qT-uh7ykF1gqNDXGyBMeOkpACxxVkMAOYyV8j5rnTaIG7Ady2I2qGGnoVlcN3idOMD-pi4cEMFa4Mu6ul-PKf-_Om6qIMA0RkUa0FEX7goXVnoMfqVP0weTUJy9Nzx7_8cTuTWjzlqLUErPRRlhyq5Tk6LlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی،
دیروز به عنوان رئیس هیئت مدیره
دیجی‌کالا منصوب شده!
نام او با واکسن کرونا گره خورده،
او سخنگوی گروهی بود که مخالف واردات واکسن بودند.
رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و برای ماه‌ها
مانع از واردات واکسن شدند.
تحت هدایت رهبرشون خامنه‌ای.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=moAcEXLeiDYjeMTN8IUoBWv-QxCvU7bd11B0cwrq_u8Snc6mJd2vAFjL3oHFdJgujJC0hLFqFJm-QHaCkH9pXnQZ6l_2jORmxfUmfN2LtoEH_Vg4JKvVlcAPUX17S3frQoVcsFHacc2paVZ82GSKWwJFPA9g-4U-aIJYG56SX6VmT-rK9gVHzql7sRrQO2Pd2m2tpmnnmHrImXi2rTseXHLG0VywXCtWhZQT_sg8p-Y8D_K7aZYzeSrzT4aho8jOEEDmOi9q1zZo0Zr5sV-bMWRjXaOlJAuTjDiaFBw6WrqRzKNw3NbbGsJfrC-DV2Cfxiz21iqYvPzVfqN7pmczmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=moAcEXLeiDYjeMTN8IUoBWv-QxCvU7bd11B0cwrq_u8Snc6mJd2vAFjL3oHFdJgujJC0hLFqFJm-QHaCkH9pXnQZ6l_2jORmxfUmfN2LtoEH_Vg4JKvVlcAPUX17S3frQoVcsFHacc2paVZ82GSKWwJFPA9g-4U-aIJYG56SX6VmT-rK9gVHzql7sRrQO2Pd2m2tpmnnmHrImXi2rTseXHLG0VywXCtWhZQT_sg8p-Y8D_K7aZYzeSrzT4aho8jOEEDmOi9q1zZo0Zr5sV-bMWRjXaOlJAuTjDiaFBw6WrqRzKNw3NbbGsJfrC-DV2Cfxiz21iqYvPzVfqN7pmczmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzE10_xOVedu78g19V7t6KAUnlQmzg0LIZZGvuc7ZsjZ8YVySYgHM5spSQgtfU84s5Frt5HC8giRupP2VXnQAWaTBMoJDW9JP1J0YEuqQ8graIrAvmltcoB72NSMAE-MM6rbl_ptIBrn1hFWgPt_vY-TDn-97RpXPeo8np2LpCDrg2NdvJXf5ViGHTZxsGfnzDK1wrfx55wRv8jrE-xiZSFxt1bscb-IwWn3uRNxrhlDUYTeIuiCi3uFYynfPfHRVKBquixzIqbqss2Pa_B2VTByT9UoPRK0wYI4OS6cCFyf4hxFUfICTOwYDHodjHKFKSiFcIu7DAGJ3KP2RnXOpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=T7TOIpW9hRnKq0ffHV9TCc_t43F_mF4VQAI38jrd4W24_CnGnPs3m4ZzdlA-9LpiC_HFhjBvxPPfr5gVF6_wQ60-qvEKGpznD6YyAwD2G5IfI_oNSg_421ooQoS7mDQi96gAQt4MTq1UUw_-QKN4lmuF_qEBsGtxrLsD6UdFJB3L5hQMez8RtMOk35KpU0nAx6G4hCZNaPv6VBeFRJn222muv1wDxz8FSuDGwg3DxRt6F6Y2lFW22y23aAiHMpRvfLo5cgDo6yabja0UbZQ9I_MYjiuqFw31WzPqVQsT4_Zhhm81tFN_gZkkggEe5X6CjQO5w-F85sq_DOzopYb1Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=T7TOIpW9hRnKq0ffHV9TCc_t43F_mF4VQAI38jrd4W24_CnGnPs3m4ZzdlA-9LpiC_HFhjBvxPPfr5gVF6_wQ60-qvEKGpznD6YyAwD2G5IfI_oNSg_421ooQoS7mDQi96gAQt4MTq1UUw_-QKN4lmuF_qEBsGtxrLsD6UdFJB3L5hQMez8RtMOk35KpU0nAx6G4hCZNaPv6VBeFRJn222muv1wDxz8FSuDGwg3DxRt6F6Y2lFW22y23aAiHMpRvfLo5cgDo6yabja0UbZQ9I_MYjiuqFw31WzPqVQsT4_Zhhm81tFN_gZkkggEe5X6CjQO5w-F85sq_DOzopYb1Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=dI0Pd4Adk90ArSB_DKX_m0zcdfPnaDuGIVElAyihr3JDGuFqBdTHv2hclB71XjNeghZBwWtapfy-M10jc9svsK_45RAMDuAV-jNd4UzWxsJVypdn0c2TwoOPnmQtNPxmtZzg2SLcRW-_wQS6NsXAEBziDyNur5FRuHu4NGdIxfBGIbG8SO6pCWlTl41bUbflPtwgD3zM-a1K4ZoKgV5Qgw4YUYIgcrkXdkNngPWd2W7Rga__Hqyhp4CzX1BudluyOm9n2Gxw0P2BEofr_SMuTk5ErSaFE1JZs7wPE-WeKRkSPUKQu3ejbfxViigV64ykVIojyvjuWH-CyH9hXTPABw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=dI0Pd4Adk90ArSB_DKX_m0zcdfPnaDuGIVElAyihr3JDGuFqBdTHv2hclB71XjNeghZBwWtapfy-M10jc9svsK_45RAMDuAV-jNd4UzWxsJVypdn0c2TwoOPnmQtNPxmtZzg2SLcRW-_wQS6NsXAEBziDyNur5FRuHu4NGdIxfBGIbG8SO6pCWlTl41bUbflPtwgD3zM-a1K4ZoKgV5Qgw4YUYIgcrkXdkNngPWd2W7Rga__Hqyhp4CzX1BudluyOm9n2Gxw0P2BEofr_SMuTk5ErSaFE1JZs7wPE-WeKRkSPUKQu3ejbfxViigV64ykVIojyvjuWH-CyH9hXTPABw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1IbqE-dc2LAdlqmDzoixTDaz2UimU8dYNF42_SwvW6jADERB3KGZF_b2Uwlfe-MEJd2OtAWhoUaXSMzDQ9mZVhrEeB0MqfFOQwXl9yVlIJFuvyym_1tV1OpmkimFVKEj5c7SkzBUdEfER7VjQTWt_y-3qkF1NNuUwQsfIlTbOximO9__9CirAj5-3KNSwyMJkboz8rilV4LOisMpMcaPU5vvHVQbTgaJPaPPqy0bu0Vea1Y11KAQ2ICzsr0OZdoxWrLHvIBhv3gnfKj8fV7WOJgwhAQtxzEDi0PSG9eZ5-Zmh3atP8rvB5LbhFvClXqSGyNqOT8yZbS3VdXm0eFoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQiDtIxy4_8AE7bjalc5fQG--yD3bDE3hQVlOjvain-AfRFCEBUaM5rJVekU0IPcJ50u0Z18uOXAbgJqj1E-KeG2BSew180lKEL18IuAzFAHjQGCb6OkPZm4h4S8k7Q7vofO6e0BmGya3ICj6PrJ1N57LMyQpBUzZRchTkXiayrStQT4Mnm5W9Fs4hZSFBFnOp5DPZuCxG89McSXs3rHY2seQPeyhLPOXurpJzPkITJgcFVQJB4u-REbEK-WNj8hT5d4hgBfHKAzalbGJEDFgMeGHKSPAiZyeDWaOG7moE9_GoYpLmfkpBFpFsOxvcFSki7cZ1FjzSjCrzBWFFrkPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با افتخار می‌گفت ما مشت
و سنگ فلسطینی‌ها رو به موشک تبدیل کردیم!
همون موشک‌ها و ۷ اکتبر،
قدس رو که آزاد نکرد هیچ!
غزه رو که نابود کرد هیچ!
مخفیگاه حسن نصرالا رو که تبدیل به یک چاه
با عمق ۱۰۰ متری کرد هیچ!
بیت رهبری رو که شخم زد هیچ!
رهبر فعلی ج‌ا رو که از ترس جان
به غیبت کبری فرستاد هیچ!
حالا بادبادک هم نمی‌تونن دستشون بگیرن!
اینها همه پیروزی‌‌ان!</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
اسکات بسنت، وزیر خزانه‌داری آمریکا :
‏
🔺
امروز «عملیات طرد اقتصادی» علیه جمهوری اسلامی ایران را آغاز می‌کنیم؛ هدف ما قطع تمام شریان‌های مالی و اقتصادی این حکومت و منزوی کردن کامل تهران است.
کشورهایی که به ایران متصل بمانند، باید انتظار انزوای مشترک با این حکومت رو به زوال را داشته باشند.
‏
🔺
خطاب به رهبران جهان می‌گویم؛ امروز زمان انتخاب است، یا آمریکا و یا جمهوری اسلامی.
‏
🔺
هر کشوری که با ایران تجارت کند، خود نیز منزوی خواهد شد. هر کسی که تصمیم بگیرد با ما همکاری کند، سود خواهد برد.
‏
🔺
به عنوان مثال تمام شعب بانک «ملی» باید تعطیل شوند.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=Ldj3EIigd6YCwknmeqTxscx4yrdIJP04mvWl61qMgDBxnheG6iLpQZ0q-iKCQ9tPY_MyDnCIxaULrvHBsk6vKU25Tm86dL7tqX_KoOypW-H8odNyaKuApcVt00bbRHTqUQcMxFk-2k28iwYbxbolrpsnliBq6cJVzft5s_ZzYyTQdm0plIJESYziv86JilVdA79d4yxGKXwyrl7s0sUWT2gOQBQizjI_Ov0E4NvQ443OmD9vWWX6gh9AW6BI3aUVUMcLTUPFpHT4WzghINstjaOxbJHygQUHGDakub1Urg_22PLdlUcRIVXtSjGlz_FiTuRa06Ex0CfTyTkmSg0tBhScFSAjDM9IXWdt-ZarLBSlCp8xAB4b_720NeT6wsbZqp0n2cXS09rv-O3xoq7WnpU_oxABIYjOuCCwRnxE-Dau6ZUa8stcpMCT0hCTGSreUxMRz1V7_mRffmPGTQ33su1nKBS115h2XkEI1UFyonTL71a2uNB5j_NRAdEsDjWO_JibR6G9SSBKqLZf1-Um1d7t7tSQy2a1uC67SMQK4AdjTIZJIADGbO-t_9577Pt5gt2NviJ0VYFDK_s7hzwx5rsf4jZWYVXOfesbUN0-_0QylWXZ6_veKd3haRbunYZTun5BnKMUGbEcnjQJftHUiprHiPlk0OXXBOgUXchJbQs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=Ldj3EIigd6YCwknmeqTxscx4yrdIJP04mvWl61qMgDBxnheG6iLpQZ0q-iKCQ9tPY_MyDnCIxaULrvHBsk6vKU25Tm86dL7tqX_KoOypW-H8odNyaKuApcVt00bbRHTqUQcMxFk-2k28iwYbxbolrpsnliBq6cJVzft5s_ZzYyTQdm0plIJESYziv86JilVdA79d4yxGKXwyrl7s0sUWT2gOQBQizjI_Ov0E4NvQ443OmD9vWWX6gh9AW6BI3aUVUMcLTUPFpHT4WzghINstjaOxbJHygQUHGDakub1Urg_22PLdlUcRIVXtSjGlz_FiTuRa06Ex0CfTyTkmSg0tBhScFSAjDM9IXWdt-ZarLBSlCp8xAB4b_720NeT6wsbZqp0n2cXS09rv-O3xoq7WnpU_oxABIYjOuCCwRnxE-Dau6ZUa8stcpMCT0hCTGSreUxMRz1V7_mRffmPGTQ33su1nKBS115h2XkEI1UFyonTL71a2uNB5j_NRAdEsDjWO_JibR6G9SSBKqLZf1-Um1d7t7tSQy2a1uC67SMQK4AdjTIZJIADGbO-t_9577Pt5gt2NviJ0VYFDK_s7hzwx5rsf4jZWYVXOfesbUN0-_0QylWXZ6_veKd3haRbunYZTun5BnKMUGbEcnjQJftHUiprHiPlk0OXXBOgUXchJbQs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌های دفترم را خرد می‌کنند.»
🔸
در سال‌های گذشته آمارهای متفاوتی از قاچاق روزانه میلیون‌ها لیتر سوخت از ایران در رسانه‌ها منتشر شده است و برخی کارشناسان بیشتر قاچاق سوخت در کشور را سازمان‌یافته می‌دانند و برخی منابع رسمی انگشت اتهام را به سوی بخش‌ها و نهادهای دولتی و «خصولتی» گرفته‌اند.
@RadioFarda</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6638" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfUMswYJrrbH1M84Xys5eDSkNm-PXlHhFM46yVI1zYg4LsrOtaKcFKr4yyVgLWSQdaR1mOst7gh33UUF3Az8i2t65bm5c1btcb33qXhVIYhypYeuYM3hSXpw0a3QMkfLyqiGMtlm6OqlcA0z4kOFesIp782TTLYLw3vOA_LOk8NQjFtLQJd2FPeF3sJh2JzjOeoCk1BMl9_SjIsuXiuQNK8UDD0Ps32H1oh_qTN3s9CaMf9hR0cKYj533jyMRQKa6ot4DnHNoGmhsrfEuE_UjtOQS7Hg3A_PiUptEkb29AV0efknyxuPhzDP5hIaTIraDuEkf2YWul3kwj_b_aN0OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
جایزه ۱۰ میلیون دلاری برای کشتن پسر ترامپ؛ بارون ترامپ هدف تازه تهدیدهای تلویزیون دولتی ایران شد
رسانه‌های حکومتی ایران در ماه‌های اخیر تهدیدهای خود علیه دونالد ترامپ و اعضای خانواده او را تشدید کرده‌اند. این تهدیدها از انتشار محتوایی درباره بارون ترامپ و ادعای دسترسی به اطلاعات رفت‌وآمد او تا طرح انتقام از رئیس‌جمهوری آمریکا را دربرمی‌گیرد.
تلویزیون دولتی ایران در تازه‌ترین تهدیدهای خود در خصوص گرفتن «قصاص خون علی خامنه‌ای و برخی از اعضای خانواه او» از دونالد ترامپ، ویدئویی پخش کرده است که ظاهرا مسیر رفت‌وآمد و فعالیت‌های بارون ترامپ، پسر ۲۰ ساله دونالد ترامپ، را ردیابی می‌کند.
در این ویديو ادعا شده است که جایزه‌ای ۱۰ میلیون دلاری برای سر کوچک‌ترین فرزند رئیس جمهور آمریکا تعیین شده است.
این ویدئو تحت عنوان «بارون ترامپ را کجا و چطور بکشیم؟» در رسانه‌های وابسته به سپاه و همچنین شبکه ۳ تلویزیون دولتی ایران منتشر شد.
جزئیات بیشتر:
https://l.euronews.com/UtiQ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6637" target="_blank">📅 09:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=XpfSmTvTH2lQpNoAi2sdXWgF2xjAeltEWBfSLLLoNgYMDlkNC4Hc0TSOLBP-HDekB9MpP-hKIms2VG_0NjGSLCOYg_ztTPWa7Zb3DygxF7UUIhXiuxFpy3UgNqRST1ObY78kWO0r077HWuQs5dYl7RUTX8dwYCAscl8iknRk0s1FUtBpnP1z25WHAFsiBf1mCnWk0KniXD2aLxW5Ih_8_ZmH1pS5aXwX0W8Jc4HdTLQI6jTO5sP1cxqamXwIgfBu6VK-ruwR0ucmPgtktxZaIm-IRfulIEDVmi56awBl8VvrmEmN10lrB6gBPVsjUeuJ520EXGynXf6LeOvIuv1_b4NqvGsmRv11OxXrI673DOfy9ATfzd1Ni_D9xw8gAdrQiMIFjmyA5ePEt0g6TYP3hRcGbZfBihaGVJcAjGEE_ixDa_LGfak6p23YBCGXTF9HD4MvTpp1xQ434zx8hp_BThlW00dQN_c1b2ZDzSgHnxgIL3jzIdKz0LpSWRKDhXUUMxS4EAKLOq8Z-Wgg_nWWryrGFCIETQ3pMdNyMX2MM82BHFvLm8ayw6WQAb6tVMzKqscMxCO6SJhKqKP7UdcNJzmHiB9j0E5w-qBRlQKNEy600MsJTJ5mjxiFxoBhYSqF4icbZki0uveUwKXYd15FHMTM1B1y-lXUEj1oaQAH29M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=XpfSmTvTH2lQpNoAi2sdXWgF2xjAeltEWBfSLLLoNgYMDlkNC4Hc0TSOLBP-HDekB9MpP-hKIms2VG_0NjGSLCOYg_ztTPWa7Zb3DygxF7UUIhXiuxFpy3UgNqRST1ObY78kWO0r077HWuQs5dYl7RUTX8dwYCAscl8iknRk0s1FUtBpnP1z25WHAFsiBf1mCnWk0KniXD2aLxW5Ih_8_ZmH1pS5aXwX0W8Jc4HdTLQI6jTO5sP1cxqamXwIgfBu6VK-ruwR0ucmPgtktxZaIm-IRfulIEDVmi56awBl8VvrmEmN10lrB6gBPVsjUeuJ520EXGynXf6LeOvIuv1_b4NqvGsmRv11OxXrI673DOfy9ATfzd1Ni_D9xw8gAdrQiMIFjmyA5ePEt0g6TYP3hRcGbZfBihaGVJcAjGEE_ixDa_LGfak6p23YBCGXTF9HD4MvTpp1xQ434zx8hp_BThlW00dQN_c1b2ZDzSgHnxgIL3jzIdKz0LpSWRKDhXUUMxS4EAKLOq8Z-Wgg_nWWryrGFCIETQ3pMdNyMX2MM82BHFvLm8ayw6WQAb6tVMzKqscMxCO6SJhKqKP7UdcNJzmHiB9j0E5w-qBRlQKNEy600MsJTJ5mjxiFxoBhYSqF4icbZki0uveUwKXYd15FHMTM1B1y-lXUEj1oaQAH29M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YxxdRmQAuFB1xQoVO82OYrsdrblgJPw0s-_kEaq21bXYzXrjjAuVL6kY-eU8FOX8x4E0VZ4WaOgb37VAImg7mFJgadixzCbfzebP3XRE6mAf1XaR_IaZ7-pwP9UD30RAHpBJJBBB6PzHUvichaa24T87Wtz3lolLKs976jEnjgb-22Jduqcw76nuAjY-AKO7dFsZEBj5j1CwVugYMH4FDGTHkhVQ2tQMt-kluQJcFv7NSvdMxvSnxT6yP5UYr7foosLtkC6Jjr3ixOFJbJFTiSMZSPn2nMotcVkVLsmggTWNo5ABWHdD_NgS89cjbvAdMdGG1Jagg4EDJxciCsCPhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNqcjhcQoJXTFMjmbigbtOuRpx8kEJTA7do9SppJqojVzgt18f2dcQsWe1e-fr1vVrhQq2aXTY5tK3vryEaL04kFHShp91Y-f8O6Yv4kJKApl6x_livaLSi5zF8kSjSeoP1UPryzEaHe2RsjJd3L-z2sxskEMrfRPXNQIAnfgg_wW3xAWC53Rx80ChR70oNvPmpWXySAJ3deCflD-52jNaoHTISLbtt4_JYhslHtikOlEqh9ErqtNaMoosjROr20xPahTXpyOgsv2pIeUNXU1x4R5Yar2fwhw1jR9v7CtPrI3IX-a8fr3IkTuRsDxpWS_JvcA3YQ3dauTxNzF70Zyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKyK466ZOdLCujk3Wm1pK-axtt7EUNuxTXD83vedA9XhDlFxo5rIEf4fah7Nr6Nt7UNasmGdorC9QydWspcTYy_dJo7oZkujqCeAOdoHMN0afNjxED4TfKeS70jWmkmwmRU-dmEMeuRhRsIbePmUKaxDAXBYdSBPhI4ZJmH0QKjVTq1gjnPLyrk3eBvNzQkecGXKKvZzyMrrA-K4yzymcLDXhAKmOu7z1cCDXowRaoAF6RkZ1_WO-i89wXS1EjofvenPZppMo95Ql8kECzqQZCuvISNzA_r97hGfbtOasAk4aoBjwzl-6DSElF-8bNjYiTVKJjWlpUAQxKJlce3GEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XX6t6gMZT7aEMk1cCa9B9B4Bvno1WUbn7p5HtZTza95aXB3bgT55X_bTo9oyzOineY1qTjvjCsU9dYvZDXcFHfeVWteZTEEuNI0zq4GbUWjBHgf6JAkQNOrGvyIbcdjC4M-hY4psy0xeTOtuf0EpcleQCzicYx7mbRzLJQ9XZ-omnH6Gv74yHF6EMkFpecznwucTwBVwJhwdEOZ04e6DIngDEKKA9-8G-K3r6b14diF5FQFmwHWgab4KYzgyq7SZvsVzVc5ng1tFfxeuqC2ZtFK9f8B_QEVHEHEGZSlmyuO1LuFPsfFox5hWSaGxGi3u10221slOf5gmzmzCS7w5Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpaeUahXrghETQUMzukPqY8_81eIKqc-htvg2q2N5S7_DAbJhN4036iYieUsHD_wbfJ5HzkbuL0JPUexqSMBcMoeIPpZTqnRD0l9THSp0WeA9zGPkIRMCKAtwSXNF7eRGW1Jj2aNOJsfKJnDrIEJ9-cXk-VFpqZZd583muOK8qCVG_Yrw_c31WR33LTZXsTV49sWDZCyH3IwiDUoaR57l7ZtV4boekEXy2CxHV1VZzubekn0Dtr30tvpX7k_-esyCvQ9atpisKJ-L_kt3OYu1ioMwn4gCTK5AjXMwJCZf_ByFWDlg5I_-Dx_fSzsAF9kbQEMMqOy1j6GsWZpXFZogg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lvx6xdVB0w3bw1lF5Xc8qF-ErGxWCoCihSmcJSTZi9xGcQgMgRCSAp-mMIXoYs4GLA45UVpE9-lDZimRRdA90_e_XaBc-OZsY-frKZqEocbBJVz2ZIZxv4q6J8WbDU-vLr8S70umnBBmFCv3EfhsdFVe4doQ87oNdci0teTfeZGL42Tt1Ge27an53wfMMQ4HGulCj1n9iXmOHjy2wjYyz1WmvTshKUVx8lKDZju0HGD_i-DU4lfN1jInk3pD7gjW-R1zgLtOm1M8DlrDHvqLk2WzqEfcAdpr4RZyMEmTtpkEBq3Ud_M5Q7l0n6R5Vb6thH9b6LcrVLVzM82BzH5gRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BelLwg5edn2zQ2fBWk5LhrTCqwShqbMF6XZWMsmXFUhRUIPysStHybCfDT4Q8omR_RPFgkgbe1w1wW-u1VJ2bLCRmEnRe-nleOaXk6mLzWNmD3KbVdjZGzT44kkE_4or_mw3w0-__ki8bbO9pYBduVco6XLGGZt3AFs06nvl6epNCfBoW4NBz0PFwo6ysqfi8XGeHprcoEWgYvm-rHQHBwxAtFTBHLmIJsTTutzMZAJKPXwWEPDdHThI92GjkJGSweCmpZK0ZsMx9RZdGlF0mSGoEzubvAEuPaYzcB4Y4m_0TIQIpvg_IElT1RoDuNzDjuCXos91LNDxzEDnvZ3bVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzNfRZQjhCLdaoxnJ3csD9-YGj6IQuBuudAeiP9ww6qoeJvc3miDy83mRWLn4qtXAmA1NhBpCDxRLi5nxUrmGpRQjUQDgS6JWG0PN2ID9A4lBqfnd4cWb5mQCC-o_Mpcs4rDntpLJE6sfNBvqqWABkw5XINSVeFQeS150JUNA9EnssDYn_0brLKP4fPt7hxXryQac1V-hI0Igc9TbK2taUmkgKTrKO5Q26SvMoYorWncKws-A-7jOvB3-o6UC1t2dmAuEDXe5R9wDe3AJnmfa6s3I4VEEDR9Bp_kTuQxoDR04ph6wUrC4T17vJNhnyeBaWl0yHhzJyui3VSsvwApnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mlxq4Dx2OPREJKD4MyRaF4Gz-NCriWolDtuShdLtVwDMthLEGzbozd6FO9BkSOlhGubCXAhhqGoOsPSyPbkFFAKG-ByRO-NUWFRHT8oTJ7cfAMfkobNEQTEUVh_mhjdbfncH7Z3rwS96axScBK_2EE2kxLbvVipaLvJCrwNvRb5smOAymEvjfv6-_F9K8OpV8iFTo9EHwgp1DHFChRbiiygLMUcVT2KT-PEe4AS3EnhzjSWwibcsyVsJPe4EeD-K_RLciW3kpZFUKI5-lH_BaEOqmgS88dcwnq5_lhytEubE-hpci09hn7JcnLfDWqKClKRJKkGT3R04zPa5HtCNVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/it0ShdSteaJE453icictGdAnInsHNvxwPYnIoABjvElNJsdz7itZapxM0AGotk2OyhaNWj5WvIG2ddRuvxTwOyCxnBP63DPzKEHK6s3k40Y5HtpBKrhqlx_A34Zj2ZTxZCL2b1AJM7a8GXOjLcxN2B3xNslkRv7c_QWH-ABsIJ6rl_lTXlJdDEZjYxPIqE1kRKjdzSw65i9Un0Npihs1fPizPXfijwnFNLh-knU7zivOGMM4kAm2jauomQ7vNOJk0QoM6fm1TLc3a7XmDiwYIpIqsO-zTE6HSrugNmAEZXl_yReM9QDLiW1st0vJQ2YgSd4MpSCw3cApUnsr2wBl8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4bQMwI9l0WuFiDADvfyulAPflHTBzWHn1zaCb-6zpgJYa8FwLMTnI-XXYk21-EVWvt7dE24rJpH2oBTnlPxL_TJ4JmphB8qDYy_d56CsJSKI29U12zgmyAbFH00SVKuyea1GMug0HJLDUMjFg5i4xkcOavHhhDZeeDFPT0QVBXtkN3QZ6lkNk57ckuTvCYSLhZO1zyv7KBRv6u69jyWiPQRpzHhche93O7qIudBTXIz-uEVFa_6bl04im0xfCyaQz29-KFzYdruMir05jjbym2MV2HhFbY2G29WKhYgvIqNZsG0FJUl82tb0kz3XBkKZ49gtI3hdPjzE0mwG4jAzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQNTkqBXaXJVTPkS307DzjBzvhfFGwJ4Aet06GBqLG0ObNOMkKKdC1ezPg2KfMegfpYWzgV5uZqZbhb4SvaLhu-MBgpD1O90SEpRr2JsgddyMi9Quc_6gzspwvylhzBDXsc2ki_FaCWiDDDM8CDw-8wZUZQchyuKoPILAyAI0IPtHmoqm-eMEpdTdZXi7JTsE0t-adFqM_O1MiadKbhABRStaonATRnOYWM66UmDRwZNrYSSmDjDjCmuH8FQsXVyK0OwpuYQW-cNlGwvmdsLmFNqV7NGS63myen2V3frZ9EmFRhrt8TKLKBU6h7_MoHRWrSFXrQoF27r551_Ohtgdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucrEU8QTaOpmJkE97sOe23Wm3O2Tbb__Go3g0Xirh7CkV8gkgxENK1IX--hdpfN9MJZDSBy5UpoFQVNEbbVT0k1BxFIZdTXpagJT8m6eF-st7-Yg4W-vRw6YNGUDvSXpjHbAKEicF8ZiJhLWqjUagU9iFI03QhgLW0ndFQ44GbbQNBA0frgcvGCNRAAZ2pHxbdLp1nFKlKYjDZMA3p5EfhTDoxZ7-X2CM2Y5u4av1r2CKM_oF5gV9HG3xNyd3pOfwm7pYTiL2ja2_7mBx8Kv7EUZu2plwct8dIOHUK18Ay_GF4_cM5i44SSEAp0tHv8x88vQh-D-axQig3fdzoOjHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZovSz3F1nSOpVgeM5MHb9bGpEIfaqaPHT3tuu1mb3kQ7wiSdsY0wrQm2SEgSUngB4z5etwSEQQdhRNx24g8jACyKzXpnej8F6DLovIaLDQkTbyQTMGc-MU5XeOnGwXMmxNiGGylJGpblTk0lelGxeaVCnSxijih6ea0_RHGLaFsmBQk9__ntHFkULqn457dZXJVrrhcgVnCpkZLB20NK8X0UgX5eQZPu0VE_zOkhNC7EiJAIgqrhmXw902kROX4OiNFSCgDDuL07NhOdEzNrI1IwJ9CbfleVzDsXBPC7mYnglmRPNK_LffkcrlG58YfJ9Uy6p-m6wDCkv9r82chBSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند
«مصدق علیه دیکتاتوری شاه بود
و شاه علیه او کودتا کرد.»
ولی یه سوال! قبل از اینکه شاه حکم
عزل مصدق رو صادر کنه،
چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند
و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟
بله! یکی از آنها «حسین مکی» بود!
او نماینده ویژه مصدق در خلع ید انگلیس
در صنعت نفت ایران بود! به او «مرد پولادین» دولت مصدق می‌گفتند
به او «سردار ملی» می‌گفتند!
او دست راست مصدق بود! او مسئول اجرایی  ملی کردن صنعت نفت بود!
اما علیه مصدق شد! چرا؟؟ چه شد؟؟</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6616" target="_blank">📅 15:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6615">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SogacPgbB8Su_xWOl8UYziLqeje9mTEfA4SDBppTBVEbQiWCGf_2-PCpk9otqxeMapXJk2lvcPlI1r_IPg-y9BDTioLV-5m5_uTb8VfyxvRoDRteD43XWErQ8LM7Qzg73Zn86m8gAPv60xrYjppt8VMrYtNE1ATATHf1qyl2rn0a_pAN97Vtw8BLVVdEODUf_aaFhjZx6_sFdhmDENm1tjw-4ljI_KMoBQ-o4nGwn6ZlJaBs54LTNu2tkqccwzqjIYlMjojWOwvRB3AFWs2EggUBmQA_tYEx5rZjyztRCtcGZyxvnFOzcog-838FrtPXykdTYGtR-HpphMPmGZ89GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

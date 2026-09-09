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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-19 02:55:58</div>
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
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=ZsV-x8dtFdl0tZUL99bZo_WSS3dCbcxxuNCIsLJgewXQihuwzsYUh2klvLiHLG6r9Aqkmmb7mIL4p2PNWRHO23OxcPj8oZAa5Wk1PuSpPlI-04ZYmaUzI6FwzTVXWHAuSa42DtoI5LfXNUUSFypFsFwMeqxQYW-QnFH5sl_A4thFF9QWnoszsculWAj_I0FiYblKaoSh2DW7oEsGmw-SRySVjaiKWz8x5sCPQxya4UWA4BdRvnAbJ5wdW6msiZN9tO2-TYkcKkqlWFCQULYAPuj-kx5ddqCatuRm17pE-tspvtaRWMtooTBvhcX3C5FCncsrtkPc3qukPJ3sAgPC1Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=ZsV-x8dtFdl0tZUL99bZo_WSS3dCbcxxuNCIsLJgewXQihuwzsYUh2klvLiHLG6r9Aqkmmb7mIL4p2PNWRHO23OxcPj8oZAa5Wk1PuSpPlI-04ZYmaUzI6FwzTVXWHAuSa42DtoI5LfXNUUSFypFsFwMeqxQYW-QnFH5sl_A4thFF9QWnoszsculWAj_I0FiYblKaoSh2DW7oEsGmw-SRySVjaiKWz8x5sCPQxya4UWA4BdRvnAbJ5wdW6msiZN9tO2-TYkcKkqlWFCQULYAPuj-kx5ddqCatuRm17pE-tspvtaRWMtooTBvhcX3C5FCncsrtkPc3qukPJ3sAgPC1Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=Jy5U_zM3e6dsvbEm3pRtepajwfZhHQkQFgDSD8PXLRaRfVBcrDSLlmylBLBq0VlTF39hSRij_mSm8Fr_8lEhm8pvIdCpvJVoziyysA1lVEzTybptzHVdZzBWblZeiU-R1cknbX_ipDDj5Ty-wBc3pgIZgtjasYXohoRschp9CPJZu9S6amatZU4dV8RtiG4XX0WV7p1XuNJxQXX-i-S-Q8l_Ahrbv0tJQk7e7HrJiU1-ncyyucCX-jboNrUBk_hqqBN1CmJN2fX1xVAI_5wdRWkwhHFnPiH6drUjC6BDUTvh5DXpWoJCRUfEiF0Fo6TtR-bRij5YKqCnyubgWWYPSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=Jy5U_zM3e6dsvbEm3pRtepajwfZhHQkQFgDSD8PXLRaRfVBcrDSLlmylBLBq0VlTF39hSRij_mSm8Fr_8lEhm8pvIdCpvJVoziyysA1lVEzTybptzHVdZzBWblZeiU-R1cknbX_ipDDj5Ty-wBc3pgIZgtjasYXohoRschp9CPJZu9S6amatZU4dV8RtiG4XX0WV7p1XuNJxQXX-i-S-Q8l_Ahrbv0tJQk7e7HrJiU1-ncyyucCX-jboNrUBk_hqqBN1CmJN2fX1xVAI_5wdRWkwhHFnPiH6drUjC6BDUTvh5DXpWoJCRUfEiF0Fo6TtR-bRij5YKqCnyubgWWYPSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KSX6sHMmsNQ2jSbgobDTGaPNeDXf23W63o6VEuVmlWOghL5HuN4rp57O1aDgWTbb06Kb_aM0whgHEjbKpQBg5TK4pVFYrW4qLLUmSgU8shWlp2cIG379sB_uYarFciL1bk7pwmFzvmg9sX-t9RIZuQxbcnknW0-AWVLrnvK1vh4k0XrBvy-vsIQmGqk9pe9tjSo71j6WjWBzGpwP8C28RojsT9El68k6oRN_ZxPtwtlBmddSwQzERb1VV9NzVYhDkHxQlGQgPIICD16xSYt7n99UWnz8DMpVl4DP3Tpout4FFdAKTpI7g6E1S58uVDqapyJ9OIE9oScKqh7u0hLkfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J6PSYkKFL4p8SWHfHrsrp2N65kyMDHHRU-xSQgF57mBe15elnUGC0a5_SthnGAE3D8D0AOG8EXASzNe8U0Pwu0RV0mNkCJFHX3Q26k3-JGBr3dh7tR-qc78RyZnbV2IQkGIjVA3AnAk0FR2ex8FcIr-nxYbRswqgZPvAOO8BcB59e3umgxKSKuiLUk65A5O7SN5BbsSGJeL0inbvx9T1PA5I6Jqo7K-Lym-mCQcmKXvlHfnkz65qWG8LsXELvYw44W8klqOvuLDJMdvvrR_9nkBhtpXarfkkg1a3cePAiZV5HeQ4oSg5FhHLR5Dh0Zg1d0dj87PzeXPUymFc7FtgPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=ku13awIRNLpkHF_1vmBiOnafFYy-Br9FiJ7wuV9sS6mZDCOR-StUVe7GbFnFRjFvWunRASTqLmQuU2ZTKRvcHFkEKwsDpq4qttGWJLPwEnVfDiZV9XO69zkVEV93dCn3T4x5YkY-YRdgPrkbnIYqjnj8I15r6ck2PmECjdaLlXtcX6oCMV75iG31vEbEQIUMcBauxZJtdfZM6GdjtDlgM3okgf96Mr4f3QEwVmUFN8mO6Lauxh7UkNoAjg53gUSwC4cJKk9SPNVHPEzj_s7_m0E1xMNt-DisteS-b3uzmwJkHaT8ThTZxtBNiEy73YUzdyDyROpOOpBOL1tnGccoXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=ku13awIRNLpkHF_1vmBiOnafFYy-Br9FiJ7wuV9sS6mZDCOR-StUVe7GbFnFRjFvWunRASTqLmQuU2ZTKRvcHFkEKwsDpq4qttGWJLPwEnVfDiZV9XO69zkVEV93dCn3T4x5YkY-YRdgPrkbnIYqjnj8I15r6ck2PmECjdaLlXtcX6oCMV75iG31vEbEQIUMcBauxZJtdfZM6GdjtDlgM3okgf96Mr4f3QEwVmUFN8mO6Lauxh7UkNoAjg53gUSwC4cJKk9SPNVHPEzj_s7_m0E1xMNt-DisteS-b3uzmwJkHaT8ThTZxtBNiEy73YUzdyDyROpOOpBOL1tnGccoXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZQH1KY3a2prCdvo_6cIIvqh9UwLCNZvDDE2DF0PIpuKjyo2ppuvDUX764i0DtzS2GrXUhMRhHCrpAfpHVjYnhgb05Rf4ItT0ZJnqzs3V-6BHeuJcIjkL6cDhjjzReXnvNLZZNJGw17X8HAiMlQvJjqPOHAyOkKHFmztvKlfqFdTysEIMcbQFiWJPZIpqwYN8hiMEtindzhKqq5vhu2m6G6oncH8UQICldD_f_DG4Fzxp6H8AQRrv3HoX9s9ltyimM8CaQOEjipSnEhY_fNvckaca2Pi4TjMoEOnKvKCzso8EEqU9vFbTbY1QmXoPCu3wZSp3prrIxWxjeOXnuoRTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQVXfzL3ENxSY6cNy6MqF39oZ7wFPjNQOp2E_0rom4B6o8eCnYeUtL6dnOX8C9EhS4r-YPwdnYchFkJsvre1L5xH9PiqdFU7hlmxk4kiOdnOB0f2XCbu7hqmGx5zxL9dHHePHSQFfcfPbWEuCjhwoT1HE22G_JwRMofqLwzlOna0Hhh-Qaun5ShOkZSm3M9eUm3XqOJNcs4F00RqO63ljnQkk4kjM2U9zHQgDVUJPxx3kUcIvmrC7YAR7erynbrqgrEs_xIkWRlXFRmjbeSPkoINk7ZSbSFmlYBZtZszEAkq1PZynGg3-ck51DB4UpKZos6QX8fz5vgrzbi70KajoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psYYlmUVq7l3IRaWTx4xbzehD-s9Zib3TWy_qc44eoMPil_y8ROtYQtPK88dvlzRN2ySF2OnMQJBtU8FqhqS-kHN3por6k04F9Qs8piwSTg5aDkv3R4mguCBOoCGupdTWn25e8SJg4YSQTgoa0XJP4EvP-shltTaQ7P7LoJEBCQfRGqpmIUSr-eJFH6p7raLQtBvz1IbTL7hDoJ5MkUs2k8Vl1LICEi9iPIddD9bqIN18ZpZlM4Pd-eLxqDcakeYC_6Q7p3suTiWQuYodMla1IzlVcVOu6bWnO88xDHrdA6ujEA0xhqcQglxt74Ru5CjZjBtQjtzayFjmxsg91R0mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=g4tEPOePaZRMfYJKp_hz3xHPSXey2GVi0PxwyD3fr3jJPzYPJTZsT-pN0UA2LS1ivVgkdhsaBSXcJXF8r3WLTseFrRBFtTjM0whHQhnAIdh9wQBIOV7_ikzmnsxG9AWEzkF4pVKZrbfg0pyGdnDvsodKUEvYLVrRz-f6jftP7ErsfDjcGKKJXk5hK_DRrcbpJN_yAGGb7iPDn8F3ssnujx673KQ5PLgyp16H8aYWZ3XzH3-InmxSfKuqWWq1uAQKKkaI360ltCS1okGm1lIpLFZUEM8b_-xrdwadirIz2BzlU3o8EZ1MFUgClnZXS3uwlBLbeLKTaMp0ruzQ1uzGzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=g4tEPOePaZRMfYJKp_hz3xHPSXey2GVi0PxwyD3fr3jJPzYPJTZsT-pN0UA2LS1ivVgkdhsaBSXcJXF8r3WLTseFrRBFtTjM0whHQhnAIdh9wQBIOV7_ikzmnsxG9AWEzkF4pVKZrbfg0pyGdnDvsodKUEvYLVrRz-f6jftP7ErsfDjcGKKJXk5hK_DRrcbpJN_yAGGb7iPDn8F3ssnujx673KQ5PLgyp16H8aYWZ3XzH3-InmxSfKuqWWq1uAQKKkaI360ltCS1okGm1lIpLFZUEM8b_-xrdwadirIz2BzlU3o8EZ1MFUgClnZXS3uwlBLbeLKTaMp0ruzQ1uzGzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=VTSgiX_nK9mzSOl9p-qPdTUqiWnvgS8x0JxmgIO4AO66WRAx251xH55rFXFSgbE1KjwKqZ76F2XPUbcUAjJO8m0UrkyHkrJlOoYW0G7L_IP0_lCtOtZOnV_8NdsnI-G1n9J96v99ZxYcscQMjzNR3JMqlZsKrZDt6tdoBg_zzzfhrGULNbWNCvAt0Wvt9-nFJ1vzPp6d_6IJHDWi4gJA7E2ok26E1XF9KGuudqCgQt6Ve1gj3rVs3PEZe-T14_qClwEfM52eMRSu3stHB-LmNNpvppBnMMKo5kR3-HJXmECwAF95vUVmf25ZVNClfRUfIpKYO6h2hMcG1y1BhazCKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=VTSgiX_nK9mzSOl9p-qPdTUqiWnvgS8x0JxmgIO4AO66WRAx251xH55rFXFSgbE1KjwKqZ76F2XPUbcUAjJO8m0UrkyHkrJlOoYW0G7L_IP0_lCtOtZOnV_8NdsnI-G1n9J96v99ZxYcscQMjzNR3JMqlZsKrZDt6tdoBg_zzzfhrGULNbWNCvAt0Wvt9-nFJ1vzPp6d_6IJHDWi4gJA7E2ok26E1XF9KGuudqCgQt6Ve1gj3rVs3PEZe-T14_qClwEfM52eMRSu3stHB-LmNNpvppBnMMKo5kR3-HJXmECwAF95vUVmf25ZVNClfRUfIpKYO6h2hMcG1y1BhazCKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=Tp60Vok1p8lcWn-2EUvoY4QAzCtwCFWTnsf6C-4hTRRC-7mIK-PHhWq4YHBs2OOnX81RBjcQAqgknOETsKJC5A1BcKn1KS2bdNHh9GSNnVTtMwtuB2fLbTkndDYKGfKIS7bQZNyUSaR52dCbAm-3Agq3IHHgQ4faAAUnzcrq6E8_noAkG6t3M9-H-cTA7nacQUIlQQy3UwHNFP-N-3YgshjwOgqV-ADp7hM7ijYnwfLtIDusd8vm_CtxXUw48DP1eydjyeEA7_qJjFVPT16kLKHOvfH5ODBwla-E1deLaZff0X6zp62dC-4ZYtLF_r_1BEoIZ-W6LdPIzquPZsvrY4hPLlhSp5ol1ZHiNSZzzUwFYDM0A84mhmorXTyqhZy6QqGqYHenBktDcFR2Hre1cjf5M9w3zKRdMUcdNkQS-EndSJ9AzlelZpQ9F9BqcS36fV9i_tsRlQWe_qfMyaCP67hLTXk-tuR3zBri3S0UfedTBqOUTjkwPZSDujBz8vsOGVExyU7PsIJwqD1FLvw43GsWrEhrz5OwAtoQDvUJVLd2jPH7JwTf3HLBjRaildUgFB-MSr2YUgvY7TEpb6kG5JLBSzORK_-JJwo9G2GCmOa1c5FuH-x8hpq_wO5frLCSVn3oJnRUugvoPbIKvBAvS0eSur3VWEiL4qSGLF7ZpL8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=Tp60Vok1p8lcWn-2EUvoY4QAzCtwCFWTnsf6C-4hTRRC-7mIK-PHhWq4YHBs2OOnX81RBjcQAqgknOETsKJC5A1BcKn1KS2bdNHh9GSNnVTtMwtuB2fLbTkndDYKGfKIS7bQZNyUSaR52dCbAm-3Agq3IHHgQ4faAAUnzcrq6E8_noAkG6t3M9-H-cTA7nacQUIlQQy3UwHNFP-N-3YgshjwOgqV-ADp7hM7ijYnwfLtIDusd8vm_CtxXUw48DP1eydjyeEA7_qJjFVPT16kLKHOvfH5ODBwla-E1deLaZff0X6zp62dC-4ZYtLF_r_1BEoIZ-W6LdPIzquPZsvrY4hPLlhSp5ol1ZHiNSZzzUwFYDM0A84mhmorXTyqhZy6QqGqYHenBktDcFR2Hre1cjf5M9w3zKRdMUcdNkQS-EndSJ9AzlelZpQ9F9BqcS36fV9i_tsRlQWe_qfMyaCP67hLTXk-tuR3zBri3S0UfedTBqOUTjkwPZSDujBz8vsOGVExyU7PsIJwqD1FLvw43GsWrEhrz5OwAtoQDvUJVLd2jPH7JwTf3HLBjRaildUgFB-MSr2YUgvY7TEpb6kG5JLBSzORK_-JJwo9G2GCmOa1c5FuH-x8hpq_wO5frLCSVn3oJnRUugvoPbIKvBAvS0eSur3VWEiL4qSGLF7ZpL8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=Bx1H-SdT-xE87DV9v1JcV_g4xQKO-Esuf3gXryynm6-KJPDkHR7d_WTY3rm6g-VcEQtB6XDtmHdxqS2oYT1HqxjgzZ8Wscv1S2IWmyaAPHPuETJ8zeKlNui8yxMP4vtHOzt-bz1fRxkyCv1Iz4VnJ2fkS-y4DGA-1PbqzmVbJ7efiTwuF2rcOeJ2xy-6QOFu9idhQESm_1hoQ7Ook2PlyDJkC1_-B-z-qs_gC2cfodi1xUH7zeBfAXnHGVpJf0N2AAO-Pb1XHng1ycABIwb4ftbwuNKJ3JJMEBWvUyoHG2EdKngOa1zKXMGDrWcEtk6u8Vs3-V2mEN_wTXt6yD8497h35Tj1x-0B9Azm5rAQ-3JjRDQimeYb57CWY9X6C60jcydyaucPw9cor3ekyX8MKH7L1kkXo8yI9ZFho8AuxtNM-g_8ecNAZTXVgvjd-Oy8Wyyt4qEAWIF_84LB4hpbUHRtgUqfBoOHSwe-pZLLVljCEjQka1Fs5Si1HO7Ofj9_OZp1V-MXh-jNsAATVZ8KTGJoDtJ-sq7sgVSaPOn-s6hrub0hZ7uOV4bvF7CrgMOysWfGzs7OV9fYpnmDYox8jZzaDadZH2UOg1YTN8S7qe9tdt_kHpAk7FQ54sT15gLwMW-pQ0a5Dg6j5MB7ON2OeXBuuUAdCJaeYO5up-AyH5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=Bx1H-SdT-xE87DV9v1JcV_g4xQKO-Esuf3gXryynm6-KJPDkHR7d_WTY3rm6g-VcEQtB6XDtmHdxqS2oYT1HqxjgzZ8Wscv1S2IWmyaAPHPuETJ8zeKlNui8yxMP4vtHOzt-bz1fRxkyCv1Iz4VnJ2fkS-y4DGA-1PbqzmVbJ7efiTwuF2rcOeJ2xy-6QOFu9idhQESm_1hoQ7Ook2PlyDJkC1_-B-z-qs_gC2cfodi1xUH7zeBfAXnHGVpJf0N2AAO-Pb1XHng1ycABIwb4ftbwuNKJ3JJMEBWvUyoHG2EdKngOa1zKXMGDrWcEtk6u8Vs3-V2mEN_wTXt6yD8497h35Tj1x-0B9Azm5rAQ-3JjRDQimeYb57CWY9X6C60jcydyaucPw9cor3ekyX8MKH7L1kkXo8yI9ZFho8AuxtNM-g_8ecNAZTXVgvjd-Oy8Wyyt4qEAWIF_84LB4hpbUHRtgUqfBoOHSwe-pZLLVljCEjQka1Fs5Si1HO7Ofj9_OZp1V-MXh-jNsAATVZ8KTGJoDtJ-sq7sgVSaPOn-s6hrub0hZ7uOV4bvF7CrgMOysWfGzs7OV9fYpnmDYox8jZzaDadZH2UOg1YTN8S7qe9tdt_kHpAk7FQ54sT15gLwMW-pQ0a5Dg6j5MB7ON2OeXBuuUAdCJaeYO5up-AyH5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=HvDFj5tTb8AafdqXs-UmuMPxTslmarXTr_7W-aUvlK7XIUW1xQAmOmfy7xj53nelhG7_nIyK7R9Ze57VOWRjDXN1OTLdeg4qxvaajybRDUE9geLxrpg2VwSN2GaUttyqZBWykJhuv3TwLCbuiPlEtR_P7XHpaXW2kicMp0jKuLgy5yxYjoyP1Pk-sNCkAcAIc11ivlPasz2MC57_smuBxaB8clxgmhz82DlZq3aTkVuGR_ufqXk2zj9R6We-hHFP0j4n20vejaTGq3eMBKa8kXdlQVJy9aKy6-3TNMs8lPOcnUdHkMpPLgPmOhplnDnUy2k-KZHSms_7fY3bxzyhOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=HvDFj5tTb8AafdqXs-UmuMPxTslmarXTr_7W-aUvlK7XIUW1xQAmOmfy7xj53nelhG7_nIyK7R9Ze57VOWRjDXN1OTLdeg4qxvaajybRDUE9geLxrpg2VwSN2GaUttyqZBWykJhuv3TwLCbuiPlEtR_P7XHpaXW2kicMp0jKuLgy5yxYjoyP1Pk-sNCkAcAIc11ivlPasz2MC57_smuBxaB8clxgmhz82DlZq3aTkVuGR_ufqXk2zj9R6We-hHFP0j4n20vejaTGq3eMBKa8kXdlQVJy9aKy6-3TNMs8lPOcnUdHkMpPLgPmOhplnDnUy2k-KZHSms_7fY3bxzyhOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ENBOB-sE9aKbvMnS8--DgNHV3CqeOLlpcGBNL-SCThmrbZrJejCsIHVl0BWKPPef6e_m2KhZxqGENg3K4MUgE5uI6ukcUg2fUaERszwe1pv3lvoPm7ntuORvkRgM7Nx-g2Pl4wN2oJwx4crueOi1381gqCdWlvjz1c9qmMMbT-dGFI2WelnyTQa65ZXKER01NIbgtGcDnt6OkiAH1dXW1oqFozCTDapPsHAcdAFnLLp9c1DUCxgK7x122_B8SNgdwYBFchHPUxtobJXUFwm6Qs3Nq0JqEmBaZ3TGSzId0OaxXQy5cczOZRX-InJzZde-qbz2ve9mGqyvCPd2xPCKPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=fdNysDv2Sf4Y9mDokIZOqygCqWu0jq5hOdG2gnsS7di5lAHkUXU3kAJbuZGUL6yvOU5PMLy_gPFI29zEngBD9AYOvIh1xD_aAOtzkcA2-BMaX-Qdu--Ib1LSXXVzSie3SR1SoU_F2rG7R5EJ7MZALYvssQKUr9ujwpkBCxGU3wv6q8DHKl3j2KqiZXUnz6eyvCeyhkbTA7Z4LqoGxweXDty1JTdG_-jmyQdbtdXDVShuosXZmnx4GzeA8CKXRFCHe9cX76kSD0gwzy0wY8Y1h2fd2V0isdxyh7d1FGNaUHd7thgQOZThVPNNKeH6oOGgQbfuGSNZfj5V-y8zSgLamg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=fdNysDv2Sf4Y9mDokIZOqygCqWu0jq5hOdG2gnsS7di5lAHkUXU3kAJbuZGUL6yvOU5PMLy_gPFI29zEngBD9AYOvIh1xD_aAOtzkcA2-BMaX-Qdu--Ib1LSXXVzSie3SR1SoU_F2rG7R5EJ7MZALYvssQKUr9ujwpkBCxGU3wv6q8DHKl3j2KqiZXUnz6eyvCeyhkbTA7Z4LqoGxweXDty1JTdG_-jmyQdbtdXDVShuosXZmnx4GzeA8CKXRFCHe9cX76kSD0gwzy0wY8Y1h2fd2V0isdxyh7d1FGNaUHd7thgQOZThVPNNKeH6oOGgQbfuGSNZfj5V-y8zSgLamg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=oDQtk2bXVdrN3qE1Uc0wJpeS8yMNrYUAWFsd4r2Kg6q8BUzP7jt6fU2f_1YONcCkkyYTfqFJGv76MLz9n-rLSk6P33iUpdgvPT7TaLNpQpl-H-M0DkwdieyM156xTmSKz8trkpzjkFbdCkao_fwKwr11HWMIQZ01ZeQwzvz2euOscgZTjS7bxaFyoT_upKLxJ7xhnu7njDzRIagNdkR0CjGy-UHgzy59ldZbj2wA8aVJB4fyShlhfn0KUk46xcQEjAhdM20bCCA2preMX5601jM80x-hSsGQ9AHDfvVFg4dp7gROfGyaXR1gEyvkgpT-ZnZ4Lr8bLmGC5tZumNVXtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=oDQtk2bXVdrN3qE1Uc0wJpeS8yMNrYUAWFsd4r2Kg6q8BUzP7jt6fU2f_1YONcCkkyYTfqFJGv76MLz9n-rLSk6P33iUpdgvPT7TaLNpQpl-H-M0DkwdieyM156xTmSKz8trkpzjkFbdCkao_fwKwr11HWMIQZ01ZeQwzvz2euOscgZTjS7bxaFyoT_upKLxJ7xhnu7njDzRIagNdkR0CjGy-UHgzy59ldZbj2wA8aVJB4fyShlhfn0KUk46xcQEjAhdM20bCCA2preMX5601jM80x-hSsGQ9AHDfvVFg4dp7gROfGyaXR1gEyvkgpT-ZnZ4Lr8bLmGC5tZumNVXtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYKHlcLJXB9C97XzOVm21KQ4W11B9fn6QvA09uPejtRhkcXiU1ch8Rf4q7ZJQuDsosXNHlnuyBKW9VszpAl5VaOnsomnRUccCdccPXPgmelRteTElJ0wos-ccrEuk9tn0TpDKLxRe66mgfYsoaIWcKbZrNzBV93PNURg082aa9IPx0zysXe0P2NrlWg6crmIlg3rbFaQhlz3kHZ-JYCd7OwlD-9VCwe_VOdeploB3GjYHDq0F0LUQVV96L3kLd3WazK96WTjZf2X_WT1Hrce55Vr0tVzqrQIciWpl1PXJ4Xb8DT8e8zi11MpdV9XRTZuS-lthwnGZEkmjSQ09Wo9QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyviLsr8x-ClFCJZssncujanAAeY12MZZ9Xf1pXW0ULI48A5pK2xi4uoVLyVBIIgF8-ND3rAll8_WEyLdbySWlUVjn0uJ-TO0MTU863femC89JX6sJwnG0ltS9IIZb6hJItDgh55TbreKr6tGT7bkol07hlMGMNuYDlA9VgeosleyIb9teM6DsiV5YMk-ZUQA6Wk407FmmgLJYSmccW3YuhkjFla7_JoFP84lhvXHXcMQgSJ1Fv75FW83J14O-H8S9kiRdqAL7oO-nbmlk0Yobh5VSgZXRjHvmeY3vPTZynPV5Ewxo5t2pvr_hmp9A7PTC-bY2z1Q669TZnic8Y_RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNEksD_QfZW_VPfPoDbMdDpX_niWyOhvW6LliS6ngMQx5P-C8WITbOcAHPNQy57mjo13Mao-T9RD9rXV3AduqSxciVdDDxIp-QPcHt8WDEqPcQnpm0PAWqxSzr_gUrayQoWrJT7PN6oKd5MePHFBY0eAZALxV_ue_sDqSgB_H4pIVyKprBrqb9O-pkdeXypSL45gZwLB-gmJmE5A2oT2gl7Dw1peCbKZwI-9YT14XDQ4m1sKHjMHEvH4RdpXo5Hrd5M1ANZgPs-dNDer3FhuEO8lFpXiPx40IkZ-E8IsyhnTuAM_vSIB6CAMKIZR6txstB7BtGY9F0cIVUMvKHUJFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNO1p5qT5NmGqjCb1Mf_JfQFr9kTZOABk2e9BQGocKMLaTh89MNn59yAC3ygl25NMSzj4j-HLroVba50WqvnBM-QDAHOhEdDcSDmN0OjiqZA--9Wdbth083N3yke352Ju_H0R9QPvDk5l7Mndu-ilI-bvB2855RrPvnU-0PcG0Q9_S00vQsyAebF6vdRyDPDurbYgWOsYrfDjuI8g-prZdXXmiBbcyo4UbfyUIVcsAEaAfB3HYmMdqDz5SfJZtl-dOXwDiwi2NhKH73opp8QKoeL_lbjhmD_Wi6DvI3elPckaL2b_tje6t1QMRwuNnga3itf5RpHkSqw5q68HVAdPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSGQGNbzAiYyXQiy0r7vkz8IzL_jmf2g-V6psYUmOrfDWeYuwB0cd6HVqkmB__oRSOvSpAdA0o82vxeIzQ0fO2HIhY5iuySHe5H4seMjir3ud0FAPjrgPrzhnVllCZ7HN9ev9lJPALBY0gj8dcI46GEssvtdljBfECoiW_VVnLl-9hfLQK8skfJrHMuaA_kQyz3Xfnbs30mDm5aSkfrnHIcgMAFEslozDI3Z7doqDScLxUWXWKPJLkE9tKhd_89zkeY_tZQo0bRltobV3mg75pk5PcjP9hJdtucus5uXyvf7FlT_p7av0GKFrIrDpMXgUBRyJF9MsEFdxIRcPdcDBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XiFCp-X6tZzkjWhp4ueTOuT9lkaSsh3HBPagf-nwbogWnREosZf21dcg5LOsJfLShiXOijv5O93IR0rHasTcjPpZvV4eHtBcKhZowozWrRW8xz1TnvC2u1-dyMyMDLktHfkNr3FNR6shZU_z2J0L2i2U7AQooLLbnEA18tgxfSSe_Edqv8fI1CvL7iiHI-EhN6KyyXrbIuP94vvLrE8txxtS8xOWrjA0V0esoH7aVHGJeD4_FreoHJyDg4ftJ-oNB6q9zHHooK-pKA89uTeQ4Z0Q6HNg0inv7vgKLowezlELKoWsYqiQw2Z9_xfhnmsT6pxa1Hv6PndgaIZUAvgovA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grkx_kJxNAjEWiwM4ZqF1XRcN7PKs9QjJKMPKacrdHqHhd9sKDYgZTXbMtxhWB09a8_nrOl7AaJMgA8RxNZVDiNaxQk2FKfKxhQJ-JN9NAJ1-k5p7UotSuI4jXlS-VUtQtj94UByX-0KyKW9UQ1PZpSTwOC_5TewIGncxkBKi1dX487JAJTidQo4qozWGycSrv6OIU4KoWoU26_SQQ_MUcTas4q5u74TMX2NbWXAn27Da9ZvKpoqAe9VqWjfFYm25_VPVG-j8L6l_qv0YFTO7gOSlm4sOwCN-8-Gjr4Jgk-h1XWlLa-FCWGn2CVLFBAdZV5Y_TA9tsHXCoiXAniudw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M0vffXajMwpuNaMnmq4q6gd-Ym9ou-wV83q7_AR-b8blJH13ONg-UxRN7mLP6TbkG06J4e3Irdt02OrgKCYs0ZBzv7Gp2HA-H3nu9aGOXC4Wy1FEjRWVY6KZLBX7VlSaHjZTNm01sMGLV89Br9Zcy4LpSqTkiMsE9tuwEycbivTH_xH0jl7wYPRdEdrQYZE9J-sgz61dPC3UBfALtfgDj_lR8R9sAultlwBmjjjgOQt3PqZukeaHFMTYdRo96Y-9taUM_Wn29MezGyyCtdNz-61TBkJh7MCsazj2vP_prqzW34pPx8TfP7FczyIW5aA6hyUwRVzN1VMFfnu6jzZdRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P1eCngfPbKP2zRG7of3Fqs7jncvj-nKzOWKzWsIb1_l2ZVOA_uopTSC7lA_IVOrWM7dejcUWPKcCr2Ksdl8Nr9i7Kr0mmuIc_M8rD8YU8am5iWcvUODDivEFJJ8y1cicDWuMeNdYCFStuMtgpLyRmD0xfHbp8IkC2b3OiKtTs6ayvVyCosINhcp_ImxsP391ItCypeXsn3M6xPe7CPKPVLSolU5h6QjxYhIfsg_iMKRDVjGjrCq63bVoZvHyxqvCNDdLKyVs4hGctqXIUA0Hb6IVc_wJ-PmCCyBZM25QNMKJ_xghWH1Wc5rETSGb0f3EKwCJv2sXd64skkRg5Vm-WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jELNro9cw2ybHh_1d5r17CoUvmNFPISMwrhVxmouCkSWnw5VvVh4gSwYC1NYutrhudlP7v_ZGFMdhHaAoC-hhcxL-A6AU1tkdcQiCDFJcaQOyqq-uZHYpcO31mUue3PZX5RoNVdDTSHwM-zTuPSTzQB1DKWOpJcmoK4_EQ9czMDkqJ3sdg_shuZroe4fS6CKdvYr1V2CdaIxSUX7ucZHXoHWemkpPI-uO4GuWcM2OVGGqMOm-fUAEDBngE5Nwne0o4mEeG5EEinEbcQLIBYzjZ4KC4cIZY4ZMbtNh2f06NmEDAyp0t4HbIwhgZTiojUAlmvZAxdcJKl51tqhkfrPvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=K3Yic55MrhB1K15mscwpv5Bb2334gHB9kCbs9JLvRNcevuTWaqYvfAJheSnRTmO93llclZax6MH0_VcP3WGul9_t5esl8nSLuGkTfcRfiPv03RQ4NIHEkloWPtXeSp11YxXSb1nkj7F3rEFo8GaN0dEJiofsT_f2Flrl_O0b2Zi3E4cvWCJ4y5KYIyEMrrYiLRY3DDNabMwLp7DyhMx_UAC-L7XHha-tGxDMzD45XY5CLg3lTMUX0swcDIfRgHR974-1gg7nUPR6ybD-wU_pA7rC9PnEHNyJUa_09xkszN_hcPNipQQYLLv71pOdYYd9jdhekKUiljZn7TqMqch1rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=K3Yic55MrhB1K15mscwpv5Bb2334gHB9kCbs9JLvRNcevuTWaqYvfAJheSnRTmO93llclZax6MH0_VcP3WGul9_t5esl8nSLuGkTfcRfiPv03RQ4NIHEkloWPtXeSp11YxXSb1nkj7F3rEFo8GaN0dEJiofsT_f2Flrl_O0b2Zi3E4cvWCJ4y5KYIyEMrrYiLRY3DDNabMwLp7DyhMx_UAC-L7XHha-tGxDMzD45XY5CLg3lTMUX0swcDIfRgHR974-1gg7nUPR6ybD-wU_pA7rC9PnEHNyJUa_09xkszN_hcPNipQQYLLv71pOdYYd9jdhekKUiljZn7TqMqch1rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daEpH50rYk576vkD1cBqk7hLlazUipH4XYugLRPqNWn9-fVZtEKkMSlurNld9wGGtwYdMGyUtLzj9X_PtDBzJM8mQT6GU_BaW58xRBUOJ7fhSyeVMfT91lMTvMDqA2dVqpgjrVJuLjUdVkWnRBLpIz5Xhs6X4INvsoH36ohGqAyZfuS0p_IwdgOTsMeglaprH1ML5a1yUkJrLf1_Xan3wwwJgPqxLACbzh0Qmds9GoPVh2jVRcV0ty4h42hTNDFoLiWivSDiLmJ8HI3EBX1y7y-lpa7bMk0KAHo2yUkxDWyGs3O2s_eevoG9MS3pNtG-vhZm7sY6FzQAa2zDnEdK2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwDxTkL7cQdvVgLCzHJ871KPCYfLoDgsIxJDrwIUHRznii7HNmsqmoyl4f8uZxfWJ7fwlTxkd-ALW5O1XbooWAPKAhSGPwinGcUR7THuE8wn6VXvpNmVt1iSrXT0dSc8ijXaKNdMoQXewk3xbiBHEriHEESN1ZGA5WnLjyjZZAbVMc189R1TGgjmKrI6DutQ0pF-DnytRw3iCDbmpzOU4gZJ9ZGwS4YP-gVlQitL2w3oSVUUVX8U_pK7w6JcjX0kh0NXkA5Y6BsEjWrRkIaTwG3IdTsVQg9wHfB1YW151QswE_td5iEf-ubaj5J3HVoIMz0KstuD2mtudxUVKoiVEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=OFkAAc0S9NeRsQMXF9ngMi2An7TkUz5e2uw2v3sbRQk0wOw3lmP06TANSPdM94SMNCAefS7uw9ryfWgXP_DX0flOvReEYhZLwPPf4t8B98ZPP1_AlzZ9_AOaeNr8Ql6XyoimfKuqzGj7cO65tgLdfgumTxFXPxOswDdsFdSNYRqNMnxEJqLGYw29j9RSSrXNBbNVutkEV7d6CZHTXPXLgHihNp340fFU5Pf_hNs6k0F3ngD1JQJOeguzwpE_pm8XffEXbMlSm0x90DttmCgZvr8uCVqijViZTadFivWfBEWwn2GpRf5uMeydTvVuGy8yAHVGKbx-faPuo3dHWVrXwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=OFkAAc0S9NeRsQMXF9ngMi2An7TkUz5e2uw2v3sbRQk0wOw3lmP06TANSPdM94SMNCAefS7uw9ryfWgXP_DX0flOvReEYhZLwPPf4t8B98ZPP1_AlzZ9_AOaeNr8Ql6XyoimfKuqzGj7cO65tgLdfgumTxFXPxOswDdsFdSNYRqNMnxEJqLGYw29j9RSSrXNBbNVutkEV7d6CZHTXPXLgHihNp340fFU5Pf_hNs6k0F3ngD1JQJOeguzwpE_pm8XffEXbMlSm0x90DttmCgZvr8uCVqijViZTadFivWfBEWwn2GpRf5uMeydTvVuGy8yAHVGKbx-faPuo3dHWVrXwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=hacjhq1spTqpAVrxWYFKVTgtKchN8skfqlE57vfVNp8gAckfWSZuKIrSSyciPqMRUYAbvUN7AhVgO0QPfuWiP9dOB1kc9CfgsevMYMSpJV6BQVRfm-t3iVK78LzgKvmMLTD0FEfuInbiq0XsV01Rjeoza2oRmMTFuKendrxLBz2ycJMBppjY_KOXIQznKkG5xFKsCemdkfvg7Fd8HnddFqsNa-k3QU3H2xf7xsoHCy0d2Q9-26YB8Gykll1IAzTXj8TMzmcGLNtkikWPU19-02qCbasQCPboK_kl5IJpkYbdi6se8HCPBzb2vh_fAgT4cyDsPEVQX029BF2Tg_61jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=hacjhq1spTqpAVrxWYFKVTgtKchN8skfqlE57vfVNp8gAckfWSZuKIrSSyciPqMRUYAbvUN7AhVgO0QPfuWiP9dOB1kc9CfgsevMYMSpJV6BQVRfm-t3iVK78LzgKvmMLTD0FEfuInbiq0XsV01Rjeoza2oRmMTFuKendrxLBz2ycJMBppjY_KOXIQznKkG5xFKsCemdkfvg7Fd8HnddFqsNa-k3QU3H2xf7xsoHCy0d2Q9-26YB8Gykll1IAzTXj8TMzmcGLNtkikWPU19-02qCbasQCPboK_kl5IJpkYbdi6se8HCPBzb2vh_fAgT4cyDsPEVQX029BF2Tg_61jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEEzjWdrmRIlp-QZ96BbeS70mu3W9UizwHIdHRYgMmtnvgTxrJoWT_X1QRx53ip46BN8EcGarllRSG7a-VtDcYjIuOocWxvEToVTV7ZGObq6wpRuVBRxvdwuPtKTY9Tcya0wAu05CeE24PNE2bIBY3r-GJr4fllywUgfvRMn63iOF1F7tasTJ4Udm94-27HkiCFx9zOn4f-OelLnlLvIxFBZ1ElzVUCb3YhCUJQOwFs4s9X7EO6na0419D-Nc1qtfZRu-pqwUe0G_oo2pOKZY8rPGQOzegbNvKJY8l3mlB2cuWRjUtTCRtFAjNyp4eQkC9CvPhycj6mwHGlUzCdwkg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVJcbwKZNPS8BlNV_-UaX5XA1IVWN2_4uumqYXOcGSyPWgGRp-9UiK3CxXW5llOsMEeuoNCS5WKqq72x3-VJA7lKBcMSy5o8MphsepggE54FxI-rhd6SbHe0dGl6VPeb2jqtfi_srIhSxux4UUlYz5cM3WZbRCay_DFVzXfczyvRriVEStgvSg2CBkWk6fjcKwMLOWOAZFQrgVsZikwt7bP_eyQBKpBfa1UqBqqnqpPo2H5fRgpbEpcAtW24Gd7pQHzK4xx1zJomd_N_U_xeom6JE84jc6Y8N4UQ2dox-BUPrLpHvOHaVmUlRpCMTBrJ9OmonlIEK3rE1rxpWtAOgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آتش گرفتن یک فروشگاه فیلم گرفته،
دادگاه گفته این اقدام «مشارکت در آتش‌سوزی»ست و حکم محاربه و اعدام داده!
همون حکومتی که با جنایت سینما رکس آبادان و ترور نخست وزیران و بمب‌گذاری‌ها شروع به کار کرد و قدرت گرفت!
بعد بگید چرا مردم در صبح ۹ اسفند
و شخم زدن بیت رهبری خوشحالی می‌کنید!
هزار بار دیگه هم شادی می‌کنیم
از مرگ و نابودی و تحقیر شماها!
هر جا که تحقیر بشید و نابود بشید؛
از غزه و لبنان و یمن و عراق تا تهران!</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHxV7LWQn6cNFvqRWoCXsqSDmmkyfiVQuDeftGZprZkp_9KBYR4PSqkN5WfKvbQc2GAXsrJ5dCJYqH9A_xfF-GP7QiHaBkTC8_y8WCCIyzdLu39DhgynSxGk0HcvZ_xmRubdkeGWSpv3J_0U6vNpj5dH5vo2vhtN0um7CiKJBzVwEM5mIyjaz5SWxkw6FfEHhr2GwnTh6t9pJcpDJfBC27MgECweng0E3j32AbSZ6kzqyjs9PONXSXYpBD1RvlyGcKqNV1CThlEcc8TcvvGC7hy1CPji10XTi1sdjkooWWij8sl7k1zSxdc3maKIH6ZNhYFllK5Eo9teoK1d6fs5Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNTJHyAXz_I7XKKhfFzsoLwc2AZVoNQxf0DuLAmgokR9Kz-_uu1dSd0M6wz5Y-w3ca8PyTfBnpmYqN-rezdY2LR5JacfE68CtEvXeOQw-uJfDQ3Lw8uj3F76fd8QBV1wzhqqhcHi4pKNdM0mdAsxQP86KGShocVpDIVK6Lk2hErm9sqDH3IV_c_dok5tcN3O484l9uEXmx1aN75YQbmuGXL4G_pCwWyix_4vRVWyEAtIhvME8cg6cIDHe6Tlr3OVnSemMSS6JWQ911tXrX-2xhD3mWoje_Qklb5VNEX48VMaEB-ls19plSL3B7ZhDWMFiUaam-M5DhJ7svJ29FrZeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/haMk23gxQy2M5vStfClVdt_3hskSdZeOYcjaclS7ggxO0DvlsezarUVDppX3mZbMwH9vOK5MPi_A-IfGt3KhHjPovYP7UeFPpf_yS8Jpb3BAF4yw2r2Rl6nm1ry8NSPm1m0TCLCuvB6kI8yRKZWBE7DPwZyZYvtyJt49AOdTHp-3hXNlR8QszeVCUlkxiffcfj0rz2WCdvqDH9wI3DrCfs3D5RKOaOCSqXzSXbarWz4FFGb8RSKp3sVZUI55c_U2JmK1XkyNjQwDIecDIvXSOHrGdqnOzc-Gaa67x13S6j0FXLbFea6KuuvvFh1yzndAMMiaJ0TzRKFm9puyK6B5pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwrjYsKYYeVRU4DWDUxm_TFf-Fs5yuQ0d8lqkjr37fDOkmmXX2WFCIe15nSE5vOxguCVhGh7Dockj7G6oyNHg2bhcwLowP76IXC8FCSadKKUCO6vsHWLJ0VcP6dsx7m5--uwQR1YjlmIMZl4ygaOyAAGRyeo013-CHp48BaVh3WozcgGnDVgMHca2x4STSl-Uz_Q-u7KLRilXP1JjJ9Y-C6R6A5vZ02qGyueskWDi_OZlyCOr1eM8_4FhxhSd2BFaMx1983EGjuAT4SKF4IfODWNESu_KBT_nSMHXVdEyfhyP96chfoCi7ZNzefuze9NDxDCNgLQzCqqHY-B8Y8wYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1T-AJvLxR7kSqRNLKVqQWYCfMtfL1ZDar8ceAHsBHGSdpEO1o8tEOcv-T_THQ0GQDpnf3W-viMUgr9T4w_huB-5JVKocaUBK-oWK50HEwZUinnldKGeSz-vENNcGSSRcNJtHQPNIpHH-S8Hdx83LCvyZdDV-U6eXOZh_TJxHLXMJjsWP0uXC_oSMAcNSH4cShv-V5kMKO6xIkUP3z6iYxCri--vnvRts9qjISUrCgklfjBymbwFVy_wcSgea3Hx15ZQ-i-sS32Dw6ldQuRUsG9i1wKwCK0htSLsjD6C-lsywbz4tpmk1qPshHKt3umuuPAkDG8Rs89kSotj0p9sbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی،
دیروز به عنوان رئیس هیئت مدیره
دیجی‌کالا منصوب شده!
نام او با واکسن کرونا گره خورده،
او سخنگوی گروهی بود که مخالف واردات واکسن بودند.
رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و برای ماه‌ها
مانع از واردات واکسن شدند.
تحت هدایت رهبرشون خامنه‌ای.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=Hm-Pr1sRiXFMfbfglBh-sTKaYNrxaJ7-zB4Uw_hXP5s2v74K8KlhKTLjdMShwis2rPiJTreT-4vI66Ui0jgGrkCt3oUiruZBE3omVTUsAtFaPmIEHjCcHmmLUDzB7Y9bbshQ2QcaLF4niEGl7mxA6nGwhaHpN_eTr8ufTIN_94Iz7Sdd1jCZjgksm9RXFut0nT__W-B1kQcPteIrc3rgSsBglMM6_42DH8d2C1nIotjTazHLAXFHM038ekxybC85NcjXr0Ftm2-tAq8gcYkZWclaxrGMGGHBgWaepX8Yo6MBI3SttPNraItlZkiScfun0YNch8gRj2s_JHo_dJse-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=Hm-Pr1sRiXFMfbfglBh-sTKaYNrxaJ7-zB4Uw_hXP5s2v74K8KlhKTLjdMShwis2rPiJTreT-4vI66Ui0jgGrkCt3oUiruZBE3omVTUsAtFaPmIEHjCcHmmLUDzB7Y9bbshQ2QcaLF4niEGl7mxA6nGwhaHpN_eTr8ufTIN_94Iz7Sdd1jCZjgksm9RXFut0nT__W-B1kQcPteIrc3rgSsBglMM6_42DH8d2C1nIotjTazHLAXFHM038ekxybC85NcjXr0Ftm2-tAq8gcYkZWclaxrGMGGHBgWaepX8Yo6MBI3SttPNraItlZkiScfun0YNch8gRj2s_JHo_dJse-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qogqKf5j_a4OSN48asKtBr1uvUerY5lre-apMaTNeGL7X2tljzLleCWs6-ob5qCQ9phFm9fyEXL_6n8eJb6oJCW8U9Mp1rf2cA48l8XT2kSzZJnph7sn9c2iBUXArCPf2xfYrEoI-RPI07FXThLrkM75h0p_gAZpLWIe-5K7EckWifSBttkoEGOVuLrSMn8Bu8r2WkNeJ1B4XqJAreQhpK6WiD22dvXEqEyVsyAsEjZpM8469WVNthAfdaYJm5Bk57q8Lcxu3A8rQ4VABZTWEsx8yfZV_Olil-UvSgOHcaaourtHOyqVOeFCI9hAq5Na7xtA0bKNM_yO-NxxQ4tmgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=ShleZkHY_lEsAiklA4vJ8Zca6iT4nqNCm_GN92ZKMYS4C-FMllwWQvCkS3-6gSwZJvB7sl_u1mVfuI1ep7URPX-CarFl-mqNxeLbreIxipDLJ1VfoR1FUbSFx0o_uQl2Pk_tkjXHhqNgrW6pjKltif5hGLjJYESEUlEIzkDWxzuZYPa1NQGI6Ud9qLnsUFXDat6joJ8-415Bg1C6jQRUf7fOmzPGI99jMRWbEgVhxAyEKwhK-zD1DGI1mHye9-oPq9XdHsflXlxejz8Zc3ic3PwZV_HzWdEntnG-rXLoCkJCe5VQJ34VSH-x4JvbZ-7JrC2sAGZNm3qxGo7UW2RoZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=ShleZkHY_lEsAiklA4vJ8Zca6iT4nqNCm_GN92ZKMYS4C-FMllwWQvCkS3-6gSwZJvB7sl_u1mVfuI1ep7URPX-CarFl-mqNxeLbreIxipDLJ1VfoR1FUbSFx0o_uQl2Pk_tkjXHhqNgrW6pjKltif5hGLjJYESEUlEIzkDWxzuZYPa1NQGI6Ud9qLnsUFXDat6joJ8-415Bg1C6jQRUf7fOmzPGI99jMRWbEgVhxAyEKwhK-zD1DGI1mHye9-oPq9XdHsflXlxejz8Zc3ic3PwZV_HzWdEntnG-rXLoCkJCe5VQJ34VSH-x4JvbZ-7JrC2sAGZNm3qxGo7UW2RoZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=Br3Bf3YJg76Pzpn_mQqrrix9ZYn4hZPMZV03w8qtYJhrWlwzwQSEYWPLu-7nQTGpDDX7bKoUdRTacQywqNehpyr0PJbW8v22fDJICD4A5vEphlP5b9RyvXugyQ-PEAOu8AqgufJgNeOdpJJHYTfnYQztxbpv28zQomIWPAvL3qutOt9iHH_udLGO2RMyHa-SYL_3HUJK6FGulx9DGF2Caxgi6XhFZrI9ocAFToGalxZfLYbJioE8AfECHjBBFMmjhf-5fjiBHk5IcFdqh2Em0SU9tuNKZzA8_3wOV4xTjEHXPX7NYXWM96kTwqa-YHyQJPmSOzeM8uyhU73lb2OCxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=Br3Bf3YJg76Pzpn_mQqrrix9ZYn4hZPMZV03w8qtYJhrWlwzwQSEYWPLu-7nQTGpDDX7bKoUdRTacQywqNehpyr0PJbW8v22fDJICD4A5vEphlP5b9RyvXugyQ-PEAOu8AqgufJgNeOdpJJHYTfnYQztxbpv28zQomIWPAvL3qutOt9iHH_udLGO2RMyHa-SYL_3HUJK6FGulx9DGF2Caxgi6XhFZrI9ocAFToGalxZfLYbJioE8AfECHjBBFMmjhf-5fjiBHk5IcFdqh2Em0SU9tuNKZzA8_3wOV4xTjEHXPX7NYXWM96kTwqa-YHyQJPmSOzeM8uyhU73lb2OCxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cphpi0kHAMsmJ6bVHST77zoZb00Xz3AMswfvVmCvz3nJxSB9-SZVwH_Dt79huupvc9fieVSE2CAr6HnWdotXN_MxVMdqxpaaGoZQGQzy9tWjmc9fyu9j20bQ7MNpHK_yYwSeu8TO5J57rf7yOx2Dl5yoUk-6yGs5K-ZFu77Zgwm6gQE_tgiXkV8zJKIOzwx5Ts5Avu31WCcrXLhLmIGqDOz5LxT5lyCIrikN8fU5e6nFQUMueQ-KJ4ZXdWZEOEAe_DAd5zulI3agd0ugm6qC9BgkCe3f1daPYtfsWNKnnBKZ-THUK4W9bHgdlitH_lvbS2M6yrnn19kyq7HWEeL9iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3V_nHo_XkFi7v6ER53B6sb5bU9-VnKpK6_CbhPsrPUZOmlSQYqKqW3NCNh2TTMIFy4aLN2qirjB3XzAEUWPi_W6G4JnvLa1gRhfjdkgmHXJ7QH4ihEZxh-aBFSFtrSqJsIp2bSloxyBPbB8i9kCZ4LlorwGLvdoqhZ_hz-vDmDH9vKIH4GEMp3ep55z-6PwxXgYH84W9lv8tzPHW2LXMJ-kxYtiLrFIwMbqd_qe3yGl5jJ8GRqqWqf2pSs_75665Nm3JbiXXO2P7HIGU1ssxAUdRzwOqv60cISYrAnhHOw2xvsUOcagLI5Cu66w7SMvBsazrAZkSXre-K2LqeX0rQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=dGWx4_6lmfOLBP84tHrbwQHJqbhzawEr79z1w77LTt2h_dI7-OFmQHdQIUFcNk4NmajNw-tfejNQecmXeEONnzt8-ivO9xsfX4pY3ctM-YrOWss8lHKCr1S8tmfmQMePNMPZz3CBfjf8A3v34xN2yyjAFhe6pjSJXY9uJV5Bz73BT39BeLsvi-V1dP78cZDFqmGOW-G_BM-hoyhD7NIVOH7LAwNBOMVkCRPsg3EpQ_lBaQyAGeKFlvq0e_AwFnH9gqYrCTrfoGVDWwBQXabIb21EBBK5KONrb9AqgtJhd1VVcyaXWYrCWeRvMFUZOB0-ZuriDUmhCQus92MBkOwPQ3STU9RHzaJSV53Tgr3kSbK1uPLRTYIV_yH-OgfcS_B0-yYRvMSqlvWi_EjNSlUKx8frZhExh0h7w1eXFy_4AtblOk9jPNTidbGTX-kJZIeYPo4iC419FSxNnnmw3dE9I49no6EeHVeMWeODVylnnaahY-P2Jm89QfX8KtvSvRTKCeqo2eqPNMKSKl0S0cRw64tpSA79d3pUUP5LuxtD2wDdRmDn1_ZTw8DsuECxLr6OmMiP1K3D1LB2ZdJncl1oFBcCfaMI6EZiC-3L1JZdm0vgSFs8OOSq3cSef3Nz-3sSZQVPAI6zzKOzjTgm2aqc1ksPvRYKwS_cpWrOUNPZ_3c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=dGWx4_6lmfOLBP84tHrbwQHJqbhzawEr79z1w77LTt2h_dI7-OFmQHdQIUFcNk4NmajNw-tfejNQecmXeEONnzt8-ivO9xsfX4pY3ctM-YrOWss8lHKCr1S8tmfmQMePNMPZz3CBfjf8A3v34xN2yyjAFhe6pjSJXY9uJV5Bz73BT39BeLsvi-V1dP78cZDFqmGOW-G_BM-hoyhD7NIVOH7LAwNBOMVkCRPsg3EpQ_lBaQyAGeKFlvq0e_AwFnH9gqYrCTrfoGVDWwBQXabIb21EBBK5KONrb9AqgtJhd1VVcyaXWYrCWeRvMFUZOB0-ZuriDUmhCQus92MBkOwPQ3STU9RHzaJSV53Tgr3kSbK1uPLRTYIV_yH-OgfcS_B0-yYRvMSqlvWi_EjNSlUKx8frZhExh0h7w1eXFy_4AtblOk9jPNTidbGTX-kJZIeYPo4iC419FSxNnnmw3dE9I49no6EeHVeMWeODVylnnaahY-P2Jm89QfX8KtvSvRTKCeqo2eqPNMKSKl0S0cRw64tpSA79d3pUUP5LuxtD2wDdRmDn1_ZTw8DsuECxLr6OmMiP1K3D1LB2ZdJncl1oFBcCfaMI6EZiC-3L1JZdm0vgSFs8OOSq3cSef3Nz-3sSZQVPAI6zzKOzjTgm2aqc1ksPvRYKwS_cpWrOUNPZ_3c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌های دفترم را خرد می‌کنند.»
🔸
در سال‌های گذشته آمارهای متفاوتی از قاچاق روزانه میلیون‌ها لیتر سوخت از ایران در رسانه‌ها منتشر شده است و برخی کارشناسان بیشتر قاچاق سوخت در کشور را سازمان‌یافته می‌دانند و برخی منابع رسمی انگشت اتهام را به سوی بخش‌ها و نهادهای دولتی و «خصولتی» گرفته‌اند.
@RadioFarda</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6638" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwtBh5JZ9UsD1LR5sKRaltH4hCldZRirEkctryNWsrzczcxZ_95-au2E__yjolwv93e0uhzA0l9o6HJ0bdpivohEURqYBCidJ5bE3noE4esd9cjmvy95MnSpG9p7rOXgD8ZXudQIsat9lh2GsZOb1hrF94wpdwB0irWjry3WRiEyKPiDnwjmRQfnuInu11r7NzArFhE88jFgnkvHfKsKrwGDgBBeBzQzaakt0Wd05hvRgDP9cH1lpSljg5FoTOPuM4BKYIJOXIaMFip2BJFJx29TLPJNF53k7lbzE0Tj6Kz4sEL6gbf4KNV7PKA0Uaid0C28IVKsliFc5LLKC_ELJQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=PxgwVYdSphoGiUoGrRaeZnjP1rRkkwxL69VIiJU5o1xO8wQc3_8g5Mei4H7GoG5I-3dBGXDE62FR6keMpzRQlxZ8ioEKQc3ez0pWzrAskRWtuVOxkRvHGtTsCOgGW5VsH5gpVJgQ_sv7Sr7z34L_Oj0NWON4Dyof8t6v8jOP5g-6zWei-9CAuCWii-7NQz7pzobp2qs8qOUJ8wPOnIDcHRtRgLN0InXDWJTO1pS5OKRmUdWK0ibUIPHN7r9qcBiBx2vbYcAhMFgOblHsp0PsTAHoqafaLXDowmrdWodF4Ec-xVrZHKU3QgNFSpH4zoYXPKF5fMHHncbzVjzAqE3mvm-JPoOuNaMUPm0m-yHAd8KnECtlHWU1dgxZ_RBOZdx4_UXpcZxjX2B5d8kc3RwQLhkUwDAgGzkdSyOXCYobnGSzhm89LtARxUy1dxT8YyckN2hOX38fB2HVoOE0eYp3GfymvhdVeRNDxa5MIZHgMAY7ZtLXRnMleMZB-1rJWkdPC00k_b0vgSNg7Lzwz9hbq1ZhLxVvGFXC4VGaOPth-mnfDpiACJNH-Wpn6LvYHomB5C9r-7AboBygw_RTLymhfP6bkhFOyK8m1xWIj-6uAU8Hk6dEE1ka5lZJZq6upUjY04VVajBbkj1Vr17sJhfajbuIM6xfON7XfoGwKlzKplw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=PxgwVYdSphoGiUoGrRaeZnjP1rRkkwxL69VIiJU5o1xO8wQc3_8g5Mei4H7GoG5I-3dBGXDE62FR6keMpzRQlxZ8ioEKQc3ez0pWzrAskRWtuVOxkRvHGtTsCOgGW5VsH5gpVJgQ_sv7Sr7z34L_Oj0NWON4Dyof8t6v8jOP5g-6zWei-9CAuCWii-7NQz7pzobp2qs8qOUJ8wPOnIDcHRtRgLN0InXDWJTO1pS5OKRmUdWK0ibUIPHN7r9qcBiBx2vbYcAhMFgOblHsp0PsTAHoqafaLXDowmrdWodF4Ec-xVrZHKU3QgNFSpH4zoYXPKF5fMHHncbzVjzAqE3mvm-JPoOuNaMUPm0m-yHAd8KnECtlHWU1dgxZ_RBOZdx4_UXpcZxjX2B5d8kc3RwQLhkUwDAgGzkdSyOXCYobnGSzhm89LtARxUy1dxT8YyckN2hOX38fB2HVoOE0eYp3GfymvhdVeRNDxa5MIZHgMAY7ZtLXRnMleMZB-1rJWkdPC00k_b0vgSNg7Lzwz9hbq1ZhLxVvGFXC4VGaOPth-mnfDpiACJNH-Wpn6LvYHomB5C9r-7AboBygw_RTLymhfP6bkhFOyK8m1xWIj-6uAU8Hk6dEE1ka5lZJZq6upUjY04VVajBbkj1Vr17sJhfajbuIM6xfON7XfoGwKlzKplw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMDAXRBF-rVWdCXLDohTC3vhx2a672r4SadvglpAHFqPKbuyIn94gicYRJDGGoQnuW7Wu739M6v5h9kbPyQChoALIdQwa_5w86zJD1sQTXmutIAJxMws9YD74FVo0-UrAl1dGWeEUYX227-q_F9t75F6CY6R6qUCGqleyHrpHJun2ue3Y65c3KCno6YEVKkSFPXxZcws9mHXJy61rvcsCHxM9NMSEi7TeHeK1FgHKclFgGQn2dwTLY6ycIc3pJT4r1NvIgTgIslxMnPTmUSlIrbJfSWIWIpWYXvokS1MZCyVLO5aqQrcEytCQaK9T9FqntOMTT0ozY7nyR2vFmE9aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKEMREG51Fh3x-LRLsiVVsfC-auMIzlo-bc-zZDm_eE2omhr78K9gOnlRNrZd_r2NQvghW58mHRXJV0tCTkajvu4ft1eAKhmRUA_xx_vk1e_Pt5etIe5b91q-lWuTtGriEoLSDgXUwpOa71uBoh9GnWWaJBEwMp1P_cqLchM2oZu_DoX7oxXgI7um1SdnKgLC0jZz_ayXZAUIYDgLgQjagh_GsOPuPVxPjmPx-p0pAh1FAdhZVqN9YQ48cfL4vBdtb-A4HE0fQQKK5WlTe1e1uawmfR-l-MP5qOk_nl0oQUc6Hf6f_evssRbj8wRVAryrL3pvVezpbuIVkZnsJdNgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kEwvHj2QG8cRed6pkyYu4ibtPlxFNqpAQ08B3pglwTHkdOdss6Lsf7VgqDssD2nhtCKErjB3WpG54j4UnSxIf5NjGq4Sil1bZ7CU57id8h2t0xKwWlusxfSYCzIjET5F04526ptSosS6TH3T-k_XL-yJKWQT3B4uJqI7LTM_qQ-lKKvRtOiAnsdrfbstxbccOCDqt_WPZrpsFwyPnIRTqw4wAsDKE-_xZzJTcBvxDoAxzjd1qcgIfwmzaidCs7bfoKf-hl_fXZ1V_Kkj6WjKJf6BayJVzbdzigqBaezAhRo72KmIESopK5iNU0jcS1x1hAs2M-R58ZOdrD7N7SKuuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3Th0d2OGtgjKHyAZKTn_hQXEtKwdRLoZON-8j6tQ7LKSY5PQVP2IEjNrWnWoXxBhtXi8gSH9DrKr-yyMGnGiuNcsFYBXECRuu7xkADTaXl6ewh7L_5bmqZE5QJTI05TuGNwQ-5cLNLlOLiavIru46DIKOYDLiGrNTK9NcH1iO15oSv_-zUVjwYwqFh5swqu1MUDMYpf8mBmJhZs7eAahy1uEybIGucohgczXHPahHVYArn0WH7FdN7eNXYrPdxZbF2ZOvcqwEBBDPd3izBbX0begPZ-yn40j8QwoX-WrtworQQXhpEEjlUqNPxbyc_wqJo-qvMUQudz8GncCu_Phw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUD9QgBtg__QFuzkwiRnw9SDrzJWeEgL-8yCgT_T58-_-9K-RxiLSDigs2HBu1SNUSVKa9EVV8P_2FfxGGPylTbJDMexqLAZPcHf114DPKc9P88XOh8MkLSaaFzYX5LZ9ukzd0dc-NM4sQSkI75IvRbNZbk6P60ab1GFSd-G3v02DzH9qW4X2Yur7lpS6ZCYWwoRE8sm6ENKEZkA_wjNZN2-e-CChhm101m9qrYwAipGlHeke948rvjy-47QLRAaXyUmLtiosjFsgwLWkEvu4Co1R8yPQck9E4A2cPWRC7YdtE9WM0a7-ubwQHrHjcbE3ZvPVK9kv6TJ29tt_E5zlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVlDjAoIi9_uTji-B-Tb6yEkaEV6bw2-BFwNMDyOVmnhn6gBkG-pf0oHLAP80KGNn6cfWYpIBD5idVkaqEPSy2YB6VrwjNAsceDAlNCvcgKclOZdG9relpWXwTGR3Qz0iRQPxIlzPCXUJrzofVzaIzSDdITlqvN5c4qdx6naYDLBR4TrYbF-OxBGvmwmEfLEfDXRIa8V4Re7rwTdiVciLNIOeHMrsNpNUTTXIpcCnW9eedBYoWGWQfTq3yKROvorHDwq8ItLmxSggkcSm2hCQkQbR2tjYG2B_DDxbsq5a_BsmCbktDelou0lkWvp7Nc-aBQBoBBo3Qlxbxvze5OVqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJxEXpcWK04M2BrM49i5QoFsqWKiVbhJCuqUM8vcRLIsKspDQfomGuPgvWqCfgjPKfP84Nzrm-0TPYAg5_Sgm3m-sb99VvdLWtkmVGjMecL9CTnU4O_XrecgWzOiJ9zpWG9cA7jY8_QImZVSXb1bdN9S4qs9G6yymgwaSXHWJvGIvVnD5irhDB_pV2andlp3JzGCWicF_YLmaV1CfLkRUEbkBPaAOSEoZavPkPtRJ44j_nKWEQ-5O36uqgWbj6mV-TZaxBhXHWP7oVP_jvS7CGMK9e36Q3RbbKJYhOEn9uUR37y3UqtLRjp1YAukSkoixo7i-QHXUl-AxMRrspP2GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNItaNGvb59g13tf4ZVWgNmivz4xasLUctLZZiRbIX3f49-abK9RKRt9-84DwI3-TK7xedWbTFBeLCwOuiTFyxLyrAbtc4Cd-eI1dvaBclSLcGT82pici_HlfPGux4pmuckEXv6RPX7Ss75ATeMNf-9ChcdGMd69SKRN-zcc-ABr--AZmwLi7TetRHeJ_nf74GcJZZUbNUPMrpH_O0jsyYG_HNHxXvGRriE41CHaEw8F1J5uPfh-hexbfSjKq-VY-HnLTX7Ja3Hdna7LIyW6bFFLxtGJ0ZikvKB2ki6qTSTDSoWs9qdk3xxO8Zlan9YXzKuP3YlkbK1rlWq7NKXukw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUCYBKBmgeeq0LptOF-T62Y0S9pK9BQ2CddzN5EtzxX8B45kmrBExBSfSUUcpx2HUKdZqQpajOSrESwYmHHlN15iBNDlF4jBgJAK5CPTXdqRQPkdEx6isZ3a05W9wfdXCB5LOQulPNQ8DyOfx_V-0l7_x2WdOuIDTU2HjO0Lp6_LR66KXL5wPSDGJ8j53zzwzb3XBP-4jwNimHEpRFQrI2Tco51yHxVO9wj2WcUyGrukh8xjMmj9I2jI2-bwS8xgsqsrLnJkvaCjTNy8gJQp5FigZ47sVW_39-WVXL9q9sKFo-ELgp3jWZI3njdzhc912-Vc1CBy51-egalJg1bbkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prnWkCucmzcqZFR4EfMWnu9sq5dk_dDzOieqY3OjJgDAP6XfwWXo-JraCyyj63PxWfsDJJEju3wDSD_zgGaGE-S0BnMhtVHcy8NmkrCItWs5Xnr797PwYTIxzkWDOXJuMj0UUJDpauVMqy8rUkPwEtmr1G4zW95pm2ZP69FCo8qHU-Ub4yi3fa0SNM4NGg5JC2EGK3BUakl89aK6rjiFq5EStmcjjzUuRtwrgq-a-geoj9ql2mtrOiEn5pZ36EpGgPtQ0pxvPQTGQsF6BYBsHGqTIz3myTmtKZUiSSqSuQSzhaLPGmDoBQXzoSAgepo3kWGTtjVKucXq3aQjE9invw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRGzDXoP45j5Nw9fFcaytFoX8AgrgsbKGzmHOeVZdw80mRY7O03HuULCgoH5YWC5zFw3G3Ni4AKhbChKJQ7axaGtOdyc6kw0H05l5-2rFFERIciZnmJaaw8DBtzh6HCrx0XLDGqWJEEfNCHqTAUUPh0OCzXvNf5A1By2Y1_-xcA3cwPAXi-P4dkrKetPdDoCDgqTnyA7b9DjilXJAltfF4tMnzddJxH0I-Gp-F9qu0AICgSzkP0JeAHFngKEtxIde4NG78ppF-xHveM9jhdgUbxaRGj1mk9mjA_GPJtMhMEfrF-G3pe1ORXCu8SV_e04vTd1QDDi2xeDrDhTs6uTxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXHMWmpBDl-YAKl0MYzXwDUpogEmzY15UD0Cm5zyXu6Z4bRQZGX2IK3DIYHCdhHHot-4VLGotan3pPl0c_z0AOl81WwCu7qNUgatlGjGQJnA2Za4210zHXw7v4PMaoJk-4Jo_O8L9j8cZZxAAYr-EvK15ieQndvdc4uzWWSzW5EUvovmo6PPP--NLyorcR4WqeB63GM3w4E51VjeRNtlL7M8ZYLd7qChmzZ2AbJ7XlLQYN4v2M10BlvE1vXkbo1_1d4qzFAZ_aZgEuOMghVba8aExfWZ2VKDtsO2Q1tj87Z_64uFRQ53_JWHNP4w5hjOFyu0cI5Y_Gl7Kso8Gq8CxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/slLwiB5SKV7AbSdcUowtOJUtlYlzK6DhhtP35IKnSIGlU94AcnphF3Ep2uIrVyUF36fjjD2pVq7mZ8sb0Y_jebzFvIi3ae1H61dcqvzqE_EtO2Q4xkvP5zirFr7MD9Q5rTMdwinsHcspJ1nkvNG2uF_j156ckmAZqrFP6huu8Xsl2914EIkTPIJYjKhX6LXZzRQCijb-Q7lQD8D1W7PyU8O38aw5w7uYaMdBRmyGQm_-sK2UkeLmwt6ovD94-gd-OQaPwrnblhU0jWjcfJ5wRJt13wXHivCyc5hP4AuPaTG-ZRFQSe3oH1O2Y7PVAA8M8fDM5mFWZWXbz7EVkMcHWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1ukTIowEycIbITW2Pq07te4NvKsNVaid3y35G1CmwU2K0P7XA-WKrJ2lJkW3v8JgC1je4NG7shfRRVRbDCNr8iLAz-snP7-9DS8PVHibxWKt_QwVb1ZOqE7TnL-3RfvP59MPFh1hgKz2kb3FpW1X6Uf2kAiUS2JQdjzdMuxQ4ADBLj_ZOMDCWd3przmeQsIPs18muk-vJfT8f8BJ0AO2dPkotTc5QrAkVmb_3GAAH2cpSy6TYocYevt1Roe-uGy3oSY5obaM6570KkuVzIikNAWmFfCt6EkDc58DWxykzwrRsHAkcTXqZEITC9hpSnGGU0Kb75K91VMAumyBwGASQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsnHTvBfSKEjCOUcf-jRoUwvIvaRwtsrg8oVzJ4ZYzvRdjUQlmDELE37GLKKBqSI71pRX8kURORN0ldkOLHWkWRMuTSZOm35t3SNKWBBUvyT0Y4H4ObKei4Ha721zqF4ELoyU1GSBakVJ6FC-qZivUxkOtUvRKNvUbaRgKlE0Wz5wJQ4cEFz1AEhml47VZsT4RyEboETs6UNxomiLhebBlZsCiEXbORlAloDXUjK2fAvU37SNpxZjcazQo10tMqkKZDIH1-icIlEgqXmBNBEHP01zXInnZMdQPmT--62baRR6wPHOfAJ2Gw9k3KaOjjO9-Um8NMeCQVwzosjFmZt3Q.jpg" alt="photo" loading="lazy"/></div>
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

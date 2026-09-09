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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 22:26:57</div>
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
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=LhTrDFVlaKKVNl9muoVlXFiCsOF9CN3V-Xr9NmXVY3WCL9Rygda3NWdSum6mupd8SBX31MBp51mWTHp-6jr0eDAYClH9COY_bJgeins8yLqGjiz53x7NuXBoPcU-2XivznbAOt_I_e3m55mAa3_RyeiyXXIuGwwuTjGWaGseFH0HESrQsLMUQMovDEOzUNWhz2Yq6ldxmZxCmmGwbtG_2egH2KUXF0H0Pdg-fvaQKnEGS0gY4MBsDUSG9cN9-zkzxiw_j0_XcrBEaRF-zSQfT-276l2SMCeV5qn6fGPwt-9kX5Wh-XvLVBoSYPI_SqUb2aPpYlIFg9Un1_uvf_3VoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=LhTrDFVlaKKVNl9muoVlXFiCsOF9CN3V-Xr9NmXVY3WCL9Rygda3NWdSum6mupd8SBX31MBp51mWTHp-6jr0eDAYClH9COY_bJgeins8yLqGjiz53x7NuXBoPcU-2XivznbAOt_I_e3m55mAa3_RyeiyXXIuGwwuTjGWaGseFH0HESrQsLMUQMovDEOzUNWhz2Yq6ldxmZxCmmGwbtG_2egH2KUXF0H0Pdg-fvaQKnEGS0gY4MBsDUSG9cN9-zkzxiw_j0_XcrBEaRF-zSQfT-276l2SMCeV5qn6fGPwt-9kX5Wh-XvLVBoSYPI_SqUb2aPpYlIFg9Un1_uvf_3VoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBMlQR8WpwuxDqB1BLZ48t5KxynpZx9K6sbarhrCTKvWwXG70S8AoZBlTCylRnZKPpQgeUCO9JxhE4XtrC6FkEIzr_a2QCJ19TN7MzNA8Vek2wlt3IMOnE61MlPSKvvOVoAFzRZ7k6xOi1KWY0-lFVuDIdLzZs7IepekobhcjywbkTNnGn-8SiyqandPjAYSwVYIfmnT2Pke0NqdaWfKDjDJCcnNB6KP4MP4ovc1DOvg7L44StJNsuIwBeFXWrax_N1HZz0ix3mRV2c7rObHXG5-On0eikpWBMXiJcSfO10CxTfRT-W-X2_c2tDygkcgRIYsSbcUdOAAMKrsuopDgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nvJtMRqe2p3rWueKjQ7OVsLz4riHUOi3mSHrllTNJnUTptVzbgxdXyonGJHJkE3WELC_uwMG_C_H2KDUOpdTPkAI2mifIW3CZ292HdwANRC4U8osoN1K0kgz6XxECwmgmbZBJ0_XPQPeFvg4WPp_HgG4259d5U3-odhakw-qMXaODa4S2g9WXRPrCOFr-TE1ToLsYUM7x2m3REbgpcTpu9e0k_u0WBfkoIYPmvtWIcSUzPyyIMhBpIwF7p3E2lzMNWrST1V45ClhZoTlQlr6uw9srdXOk3Bbcm1xxH2dORZNb8p-q8rKOUXfVTRS5ap3vTt63btdBE0k5GwSpmXvZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCNT6HsHRuP4v9g4KTXnziNdO0fx63WtyouOeC8NewIEVv6tPROPjcLLw_2D-GnHZtYD-l5t0ZzYuSAUyttRdIPm-U8PdS2zv47M-RuWMKMsj41Rq_XatKNrnlxBnrtuTEaQrX1wQxwF5RBl8mkcYtAT9pcu1cb-JaXHkuHkHYUa5KHoP9JcWdh8msMFQyiak1AtAL2TEA9XYeFnIOvqzXba9YDQ7JHlN0dPqUPOYMFFPznJSyhr_HYv4UWevIEfaktlDlXRLYDC9teM-s9DpRxTk5CWYDm_OrEIiVfDZOvsYUK7EQGeDzTGqqYdyM0xyP4kTNY3pnbHYb7q9hrbeg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=kPKo6ufRMOxXsq7VE9fTlipU-YhMOyBKEMLS2VHEIV7drpVECk_zXIWDLJlOYYK41d4r0B-rWxlLpcmZHLFixyLJHbjtHxaiuT3458YA8u38MCqVeBeVgNBLK9zvqq4nZ0wK83yar3p92j2b1on7rabmW7fyoU1HYH5jjCRbjWKwgI75AXCK5PfbXiBerhQR3q2NpLfcnTMR3PG_D8VfvNqA1Ortuwkuc9kQtKo8FXS5LwC24UMVXDeN5XPsQoe5-07SxLvh-Dg06McgiPVL4zCHUwTpooZu3OE_e9QTKi1E4lLtLJaKIiZn4zsL1nZ6l1bOHHY15aibd6T9ujyOIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=kPKo6ufRMOxXsq7VE9fTlipU-YhMOyBKEMLS2VHEIV7drpVECk_zXIWDLJlOYYK41d4r0B-rWxlLpcmZHLFixyLJHbjtHxaiuT3458YA8u38MCqVeBeVgNBLK9zvqq4nZ0wK83yar3p92j2b1on7rabmW7fyoU1HYH5jjCRbjWKwgI75AXCK5PfbXiBerhQR3q2NpLfcnTMR3PG_D8VfvNqA1Ortuwkuc9kQtKo8FXS5LwC24UMVXDeN5XPsQoe5-07SxLvh-Dg06McgiPVL4zCHUwTpooZu3OE_e9QTKi1E4lLtLJaKIiZn4zsL1nZ6l1bOHHY15aibd6T9ujyOIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=l7jsytz_BySAqBQn-2nFeP35McoPTksuYa8KP1HjDyDDMeJc5D8PZlwBsZGomZbomXuzfKOlZtIivGv294BYbxZrNIABEkqG7p6XGfrQ7lweEAxwxVswnBv5_wNQgWRmxn9pl4g0W8dZ8awaJC3keAAYf834--ak3HONOeKEhn-jw1nWhRrd3HdRwR5M9v-H7n_yYeiuSSPqgvtl1WIGH7Rb1UX5YnzqIVr6PhUsmNcIJahlJhlz965bS5-Tddr2gGbZLczbcNHf_bM3yJCLUHp6U8y27DyZ2ANYRGfkIASmsg4pcIg2Mpuna5STskrD_ggbUcj0RwuHLg-Ug_ON3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=l7jsytz_BySAqBQn-2nFeP35McoPTksuYa8KP1HjDyDDMeJc5D8PZlwBsZGomZbomXuzfKOlZtIivGv294BYbxZrNIABEkqG7p6XGfrQ7lweEAxwxVswnBv5_wNQgWRmxn9pl4g0W8dZ8awaJC3keAAYf834--ak3HONOeKEhn-jw1nWhRrd3HdRwR5M9v-H7n_yYeiuSSPqgvtl1WIGH7Rb1UX5YnzqIVr6PhUsmNcIJahlJhlz965bS5-Tddr2gGbZLczbcNHf_bM3yJCLUHp6U8y27DyZ2ANYRGfkIASmsg4pcIg2Mpuna5STskrD_ggbUcj0RwuHLg-Ug_ON3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=PUgoEfydKQc9EaaOgUDwVhy_L4_hXBhXwcPHfFMSEYBqQEUErD8Zk0yTFDKBsOP4CWQCzzvRSzM7Et_oi21KH90ILQ3hyX3J1N5WQAt-IYyxVTBWgyrqzyk82uAY0ArDubdDrCaXSRiXsucP_GI9UUeXTxxby4l5hUlSO6XSWeD4fnrHIfTTiTf7TdSUjyYhIU4Y8zDfuQ1rLBzCtC1_n5CnbV8KunfjvVMT7Od_iDmQ5L99EZ_GUaIZkXjj2abEs4UYc1k-Uon0JG2_JmC9YfAqguiIJ8JbHjLuIQKCk-HJfQAQEl3LRwor_USpqwC9uNYqVd4AcjG-GHP5UNwkcp7cwqqVPGmwlAtl0B8QhjS0luFieYMNJfHIeZTl70FpqVp__Gz3h61dGXrnlc2u0Bbcv86nQ9CqCOJ2St2a6TjSXYR59zoDyErfAOkb8fm7qe-RiNZ8Wa8z5wsV_akJDLTcjnbZPY1c12UltbQOqARIWGwrGk-OoFBTTKeCX7FQos2feVcGsGaCALIEktLOcPVTEuh7hnR_FBbKLFIHxn_6PazarTeGEiVEZoj2LNKxFBOqYG_UOTaXV4OyqA7UCiFTVTsf8rhopgpPpqHn5AkOEd5KRQ09nyavr9zhCF09bIYg6DaBEGKe51Dr8rq057mqELoHU310ZS-vCHwYKO4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=PUgoEfydKQc9EaaOgUDwVhy_L4_hXBhXwcPHfFMSEYBqQEUErD8Zk0yTFDKBsOP4CWQCzzvRSzM7Et_oi21KH90ILQ3hyX3J1N5WQAt-IYyxVTBWgyrqzyk82uAY0ArDubdDrCaXSRiXsucP_GI9UUeXTxxby4l5hUlSO6XSWeD4fnrHIfTTiTf7TdSUjyYhIU4Y8zDfuQ1rLBzCtC1_n5CnbV8KunfjvVMT7Od_iDmQ5L99EZ_GUaIZkXjj2abEs4UYc1k-Uon0JG2_JmC9YfAqguiIJ8JbHjLuIQKCk-HJfQAQEl3LRwor_USpqwC9uNYqVd4AcjG-GHP5UNwkcp7cwqqVPGmwlAtl0B8QhjS0luFieYMNJfHIeZTl70FpqVp__Gz3h61dGXrnlc2u0Bbcv86nQ9CqCOJ2St2a6TjSXYR59zoDyErfAOkb8fm7qe-RiNZ8Wa8z5wsV_akJDLTcjnbZPY1c12UltbQOqARIWGwrGk-OoFBTTKeCX7FQos2feVcGsGaCALIEktLOcPVTEuh7hnR_FBbKLFIHxn_6PazarTeGEiVEZoj2LNKxFBOqYG_UOTaXV4OyqA7UCiFTVTsf8rhopgpPpqHn5AkOEd5KRQ09nyavr9zhCF09bIYg6DaBEGKe51Dr8rq057mqELoHU310ZS-vCHwYKO4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=RcvBQIk1ibvpM4eQV_z54BPfvLE6OLf8b4-ykQLkZ-hLnflX2iI9177oN_XlzHKMSoLKFmaj5eECrUET6fqPK0h45Kle1jPf_wgBzKHLRJoyfgcXKrgROm3tIhkCjig8_yxNhhQ3JS_z1e4dTWD_vbzpfqtrAv4CoL4C0-Qq2YY6NnZMeY7pajbCnEvOuIIfCU8MhBfO54crgcnZ8FDMmu_cfUEGjC5hyMSX8drjm6HVlQYrIcHmoVbt3KRcnLo8hj-ozDV8XseARBVaElvBADiYg83LY0zc3YvaK949FngHxveQe8e_g4f6hTwwasXpTMh4JmvksU5c5hmHY7isMAPcG5y1y9CMmm0PJU2vUyHtlgyxHBuiyRza72kj9kP4iOYv7ykmqLNZIDUm2sYrfIl5FDeem7rxdT94xNCBP54ENpFO0mWMKOevJPfyVFUqtsS0y4qTDHIjVmnshHAKVWeDiHWV-Ik3NY75cdxIox4qrsIhm10ETboBGsq_BmkYlYoahK2ATW-xy8FKYCOCze1ROZqL8Jr44ug_UqnfttjlHIbiuiKNwv8-V4SDj7kGURO4ihhGhgkkASfp63Gx0or0KdaSkukIq966D9e8ku6Ffj1Shxlg6XiVOcTsGhSxasF5C-BWJM32YzP2TJonbknj0f1jZ69qnQtXx3xqYI8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=RcvBQIk1ibvpM4eQV_z54BPfvLE6OLf8b4-ykQLkZ-hLnflX2iI9177oN_XlzHKMSoLKFmaj5eECrUET6fqPK0h45Kle1jPf_wgBzKHLRJoyfgcXKrgROm3tIhkCjig8_yxNhhQ3JS_z1e4dTWD_vbzpfqtrAv4CoL4C0-Qq2YY6NnZMeY7pajbCnEvOuIIfCU8MhBfO54crgcnZ8FDMmu_cfUEGjC5hyMSX8drjm6HVlQYrIcHmoVbt3KRcnLo8hj-ozDV8XseARBVaElvBADiYg83LY0zc3YvaK949FngHxveQe8e_g4f6hTwwasXpTMh4JmvksU5c5hmHY7isMAPcG5y1y9CMmm0PJU2vUyHtlgyxHBuiyRza72kj9kP4iOYv7ykmqLNZIDUm2sYrfIl5FDeem7rxdT94xNCBP54ENpFO0mWMKOevJPfyVFUqtsS0y4qTDHIjVmnshHAKVWeDiHWV-Ik3NY75cdxIox4qrsIhm10ETboBGsq_BmkYlYoahK2ATW-xy8FKYCOCze1ROZqL8Jr44ug_UqnfttjlHIbiuiKNwv8-V4SDj7kGURO4ihhGhgkkASfp63Gx0or0KdaSkukIq966D9e8ku6Ffj1Shxlg6XiVOcTsGhSxasF5C-BWJM32YzP2TJonbknj0f1jZ69qnQtXx3xqYI8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=l08xnduUaBzfltZsuRw50EWRmLaKsjHamz5v9BNR_uQ1CpFHN41gVW0A3zDWpzQvE4WE7LFXjGJHWo9fqZ5nBslRcu00WJYCM6ipUTQ2e7XBvR3yDV3YFlKlU6nStTZGNI5lv77pTBoEZSBhq_XcD-gTWWb8I4XhjNckwe3JtmPidZvrarJvk0O4vDZCa5DSIkhACsyeAQ2DCorydl8yeMZ152SMAGMOVFKZpb3wqq2F594Z56bRxD19MX11bUKM08CG-QPVTrbvBGwnwRruoHR2vg0Xtm1gHam_os2Uz9jbS3gppLaaQc_yhE4q7HqQBQKj3GxdJGdSgwkAX_4Q6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=l08xnduUaBzfltZsuRw50EWRmLaKsjHamz5v9BNR_uQ1CpFHN41gVW0A3zDWpzQvE4WE7LFXjGJHWo9fqZ5nBslRcu00WJYCM6ipUTQ2e7XBvR3yDV3YFlKlU6nStTZGNI5lv77pTBoEZSBhq_XcD-gTWWb8I4XhjNckwe3JtmPidZvrarJvk0O4vDZCa5DSIkhACsyeAQ2DCorydl8yeMZ152SMAGMOVFKZpb3wqq2F594Z56bRxD19MX11bUKM08CG-QPVTrbvBGwnwRruoHR2vg0Xtm1gHam_os2Uz9jbS3gppLaaQc_yhE4q7HqQBQKj3GxdJGdSgwkAX_4Q6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ecbSZbdLJ2EkuKyVQ3_eOD6nrIJMfBUYJgoqF_TvfbkFP_5ijbJaJ5iJHmlPDBJzpi54nh8cXLQnmMHxXgEFUNK6RzkzQF1BpicK96M4M66sudmb0wGILeT1D7gAKYejGHzRSHiW3CnTTBgvRNz5w2QKbA28BPo5kgBcc_JAX6l4Ezeut6jzszfWuLoVWRjL7LAlqG4wjdSopryXgsENrCnESg5dfGokq50HbzjoiXIxGHmhREE58CmelAIKaU2JiZBWxugJxqVKAuPd8Pjt55SbRVUSrYA8T5_lf-WOIQggRqo1HaJGHUxBOw8U0lKXLUt8FTBlrTrjyoDbqyx4kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=oIei_VORJJw9wJ3vytg503jIJGoIbURZhiOz7seSbu6HHIt1LFHCOsWYZZcPqnl6USMV9Vkj7N1b1YPeZNSVI6RmMKWntEy8ALSIf5QQTe8r3uLi09cGErhCaBmOxk7OxI4e2DLcN-zwjVXtatCxdg_JrXR6tOqF16FNih2CmVluyJjma5K1rMEmdv0NQGmxmgXY9CnF5MRc7iMHgivlLjICOWhmcInUiOKslUm_VHBS9APZuNaL5WMV5b7QVUau5OS8ZPtK7rTDmCOt3mwTa6-MliWlK25RrBgdPOGkUBFIR4ByohNUgxml83fbI8cdyCCfGmZ4pMhCs7abbdPrFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=oIei_VORJJw9wJ3vytg503jIJGoIbURZhiOz7seSbu6HHIt1LFHCOsWYZZcPqnl6USMV9Vkj7N1b1YPeZNSVI6RmMKWntEy8ALSIf5QQTe8r3uLi09cGErhCaBmOxk7OxI4e2DLcN-zwjVXtatCxdg_JrXR6tOqF16FNih2CmVluyJjma5K1rMEmdv0NQGmxmgXY9CnF5MRc7iMHgivlLjICOWhmcInUiOKslUm_VHBS9APZuNaL5WMV5b7QVUau5OS8ZPtK7rTDmCOt3mwTa6-MliWlK25RrBgdPOGkUBFIR4ByohNUgxml83fbI8cdyCCfGmZ4pMhCs7abbdPrFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=nzo0rEqltpQ7CF_XhVfLTccxECk8Th1S73PIJoSHjQghJNnGeeNcolVqC1_Jt2Pwolm5d2o0-k8RsACpTaoaujFp1H6ULAQMlEEYblZNDaj87ufE08PeHzrKtED6et8cnNbI_ne3I6eZQoJhxlIRKV-QyMKj-JSzP7tLQ0754uaUK-fVMGZ-RvJaDn7GZKkCOn6l93xfDb2lYiS4xakqktNOzGajVwz79B1clAcAA9MObjWhFC9Pxi6uiXH3b1JeUrVPlq71bakh_rtn6ZsjVP9FGByAaIIZthJ1lImcYK3YYQ1tAa-c62iM7ugG39vBtjRf3NPbZ7_EapQjOsu0Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=nzo0rEqltpQ7CF_XhVfLTccxECk8Th1S73PIJoSHjQghJNnGeeNcolVqC1_Jt2Pwolm5d2o0-k8RsACpTaoaujFp1H6ULAQMlEEYblZNDaj87ufE08PeHzrKtED6et8cnNbI_ne3I6eZQoJhxlIRKV-QyMKj-JSzP7tLQ0754uaUK-fVMGZ-RvJaDn7GZKkCOn6l93xfDb2lYiS4xakqktNOzGajVwz79B1clAcAA9MObjWhFC9Pxi6uiXH3b1JeUrVPlq71bakh_rtn6ZsjVP9FGByAaIIZthJ1lImcYK3YYQ1tAa-c62iM7ugG39vBtjRf3NPbZ7_EapQjOsu0Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-ud8jiXDoN1gl1u5sCmleps8SNL34rAWqHcf993cVFUlvL54jeuXctxHrzGnOMGInn-EoBpZ0IT5Afe8lZC5ukECt-wQ8H1QC9PojpmXJkZ99rT2G_8CNi5arnM3zwX8pae6F2YlmvxapDfx6FMWN9p5rsTiZGrCu6wiuzCksu9oO_vqhQqPzvSa0nMo11eKAThgPTLpVl1hYvU28pDHFGu3Zvcw_Z3JRkB7KbKZFAio0xVj9jFTnL6A5x7sEydLrEPBOcHM5PZ8VA2YPoRJzGlVrFvFHGr40CVRxpH8OV5RWBGp3gDHQJB2ijTHtOOZRV89_HmduDiD1dWrDpsjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckz35RPzeeyouScVXFgHB2Dj1LYJ7JjfNP4q1lxh8s7RkjboFZkYl1sV904MvAgaoy2fibUY4h1aLmzv2FJT23JdAWzQCrYfRfJz_AEP2EB7DiVRRM4vUHprSVVs0SZ765744RleE5yqmMWIwMcvFerGZ-mfBQo7YbmZVcgFSVGtLSudQF7Qg5Ofo6NkwOCkh0W5sN9ZdVdCdMxEf8E-O70xOjq2TgrIYOZK7PZ8qvZoHOcezxKxaj6PZwDMLZL8r1mL44LFoEYzflUHM-uSLbqJECWtcS6Zt0rX88L9v1NjW_fiebHL5kIqauxnPmDlj7bN1DtMhD5vagOqMlXMCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Opy0z3FFH4wXE3oAE1nE8OzsFGfN3jrQ_SLbVVgOCUT61YHmHtHhmp0r33dvhQOPAaA7CfNc2CL6oQFgh0p-QIQxSD5ajqAtVn5BrkfZ79i1h1iHfJ5lnbzDgj6CqDdiqEpxo4bf8UUQA3koopK1Z3vNfFcYoT_JB7Y31Wn4xPLEpikkTVRz120LMlRdAIQJI2czHoXPnXC_J3hKS9lfAxOipq02I4GhnV3wLmEXs_EDUYH-L57WW6w60eRbrvB2OpkRgCDewO8V9fOjBMU3FGSDmagL-q3ZAbIs7W6y_l5ONiXvfPRswBOPPdfQtxkdY_EK5M6fkfPgKoKDgSPdGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Efmuu425DH1ixSof6I0bSXJygG37ixWzudUAfCPrh61koLDyV4e5CA7TdRCJbYAGGad3hz3jYl5xD_sc-AhR_VZ-bcWwNgCZVo9PmmUehk2EIhhCNl0dg3G2Zhi6UyB-NiJT-athfjFgE4vLsc0k4fBwXfNptW0d_oNT3jakDTiQ2wkAqOLu6TwG-F6JWAv9UqPeeQb1dvNqJo2e7FEzvHlURbBosvAPcdc-1y3kt7XWViXJxdiRbXD4k7IjNZxA1X_MlIkSvTEYXMZUWRGDdRMUtI6-_3Xuy-u-nzBBmGVphe2v4-MfPIh7mlG6jAgvhkzelNRWwZ7ubW0NSAcsDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2ZqRTCSImm2_gfEtRiF_2WfJdnrjIaXuLsa598rd8CXEPehY2UTDGtlK38FfhDmWsXP5XuoWE9NP1XlUjF6KJXFlwiJXKgkS_Uxk3Lfs-sSDMrR4hEF_TFiDY5QHSePRUg8EmzzQIQn_tr6PxDgRkX6yX4kKpLwB9Uda5855f6REkOItAMFeaiFYHZP0vZ6M8aAbGQGV053ScDUAjejWzl7PKvJrj3cwou06UPUJmlykMhk-UZi79_2rFgnJv_jDbgQRjQB88eivFUzjYndTxtjODz5jUW5vfQLUOgLrW4De0cnIS8KPseKw65lAof8radYGOkZ4Ub_ou48YCeHyQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekm8duM6hGKbDL0vWH2JJWHRomR1Iz4nRV98LPI0KiBxdBTaI7SomYA-NRgXSzmtkdLYbZbVM_as8PuqTKs4_BRgv-orx4a47Y-K4GHXtRCyJm4rup4jz4eP2yw0Ax-r9_PqgZNDNCDvriM2uQUZD4lO8dX08IyrhaGgN_d92uR1r7_ZPLuFrmvX-VJ9ACs72Bn-5lPkDG7iXnMdGBwY449ljXyT2i6QyeHOxP_5DoiBTJnH3G-crxcJocnK-zjy571LM1XoKfAqEwqMthjPar827ftBzVzkPVgL7ylyxwt5PprYTlkLk5SiYRFYn9QWKRKaVYMTMiT3xi7yrmNJ1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjWDgH1DBIGLzZmwvdlKwsGjj_S41PC7EgdBt2vAP5XtqGwt6Yq31KB5i5rcCxlRx4tddt1ZlosXVBymR_vXmcwzicSvO9Z-ASx0gNW6t8eI0-L1xsj0CIOLJ12zQdgTbIUl903QlIUeppHGUJMUEhdL_PpAJeTnp-aGJ0LpLPhjzzaN0sewGSSVTwo9nudrfuEfgG45R3FedjMk89Pef3Oye3M17xGxliRDyJT4LvCD4-puhtRGFNLoRT4eFDgvzBflfFPdeGBNTa5BTO_eGxTy2ooBt-I_mmubVr0EM-Gw_GYBJL7MlkV0r6nDnKpYJGQQ8iXNaoVqv95o6zqS6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/epACQLFO510WFdNVLkvcRTCu8roMvKX_adNQD_5_SxAexUrhjVHtX6FQjWsnu0ckcW75DJAFbKynulh-zyZ5oqY4P35aCZy-k3mDmEj0YnUBsmBuos4iJLmRatb0SvHM-d4K75O_gRYS9OnY4aMbanLSousjkvF2jWV_HDbQGJeQ_i6xHz0AgVXLxQrWzLmwBRUaPmCmrKpiCuLDxcAd6rBYdn5wJTwlRijZLUj5halsAxPNp8cxaGCqofeyH6xlDPyo9L6oj33Z4WyRCZKzdwoggUjf9f7BytzxjJA2fzaix14avnKtNejbEv1gsf0dcE1uRDouJc45YOycj-mGYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ffSIF2YAgXJiGDRFrL6lA4ng9Y8infPTL23hsJdovLKxOHrEwhUwXrQOh7cBF4CVc35urOAcm23kPNOTwJ95x9_wnVaS1IDGEuIQCmTLQMmC93UZ_g8Jv1JfITxjuV18LsJc8VqeIGEe_krJqExZjfQrsWX6c4ijX8zGRmw3bSIEvqdJiWeedI8zwkx31tU-EzRNCDA_Zhib0W-QpgjR2BdXbtaJxAdWJ0S9ez98wxN3CWs_Q5WMlG1c8lgn2RixuWlllab0IezUyfklVr_IyPqoVAYNVv6FlhGsY6phMoFqXaiK4qk_GsM7A0dW5Y-0nxPpwmr_GVQdc6f10vkeEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bGA6NU99KQZVrqyhvwMCG0aXahTyO-wkTRjJvEprdJfpl5mjnUM11BvU-ZgOBSM35lmILf4SR748xyFSzXd8JrRXIK5PWv_mri0zO5miEiXOGqjW75Pf-ke2mX3uADXqhrT4lKtFZXMiYUq3KWCjNu1_nnjCdzsrasWLWoVoqTjy-zLe1ySXSkzC0o-24MDoBimX3MH-VUe6XhSTxI3fpNwMMMVs2PsHtrJ8KEp2XqHMTTBYSG5XSsDbV2VArw-9IfQGTo95L8JCvIiHo5EMIJaR8wmvHPu3UHpnN_B1isJ6q3JLJYCoSxSqkmM6dvVnl52LOp1FFjrJ-c9ryudPSQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=GsKnchjmjvTKn3LDlBG2xSSOAGsAj4F-t_lHpMMQUbHmjz0p5Uw1b0ZF8QUQvUCbxCPbcMlnMeJVXPqPD3hSUX-ZlXu5CgfEj_utKdIQDCLYKLq8fo6H2GpzKHfc0OrsLOR81Tq8ZWeywG2uO2t4YY9ujk8p-gMXATcCQJ4HMpncDhTdKS9p5CFl6QDEUj5BanMaOSih4gr2tnOmFWFQq-1DcpusoMBznebobaWb5VpaM0FG73IHN2UX9ndHWKEexsG6-cdBsD7G1M2VddqL-9TbVF6XqGkSMRnE2FAZgehZI3wrgL3Jr6SSE3CjCPXT6cxD4ddy9BRFtQRBpyo5Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=GsKnchjmjvTKn3LDlBG2xSSOAGsAj4F-t_lHpMMQUbHmjz0p5Uw1b0ZF8QUQvUCbxCPbcMlnMeJVXPqPD3hSUX-ZlXu5CgfEj_utKdIQDCLYKLq8fo6H2GpzKHfc0OrsLOR81Tq8ZWeywG2uO2t4YY9ujk8p-gMXATcCQJ4HMpncDhTdKS9p5CFl6QDEUj5BanMaOSih4gr2tnOmFWFQq-1DcpusoMBznebobaWb5VpaM0FG73IHN2UX9ndHWKEexsG6-cdBsD7G1M2VddqL-9TbVF6XqGkSMRnE2FAZgehZI3wrgL3Jr6SSE3CjCPXT6cxD4ddy9BRFtQRBpyo5Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lAfO3RgaCu9XjTQ88nERtkz7SkY11Z__Jfyd57bXLNI-3frvh3QFG-9KuOOjk_ontnAyAmCR0ajPuyA4tiQh7l4cznbJ0f16JFGYfTyB-sTGE1U4XoIq0UONwB6JXUnsYOM0hnwRU-i7MOooYmJxq3ZngRY1YmUcd2WxgoCgdLYNBdtBuFOK3SDih2oyvCohfdVAfsCknkkuDcwh1rkBGD-Kopl95euDgTVdNO_xCZhjtO0_CY9_ayL9CFT0yPuRzpB58fcG2mEwNfqHUtHodUQpXNpvOwoaMLfloBtfILos-dvtDcKz98rLxeNkWh7GNigQL988rdsOBvxGhJ8iJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JA0toWk0kAmalH842Z9F1fsRwVFDS_w0_IYbvi902wLiYP4n5MVHvWiszWP38a7MLPajMYG_TN3DSwya1QuXNFEwq-Y65R5hWGAapFS57KMm38U0LTAq-ncuuumPwr5DsxwP_SbMLdXTnZrZQw-5-G6LGkI2nQggtdPUfEhkmaEEPep_S_aNT7NamUPLgixT3A21F3vpnzQHe2BvNXOqRZQeQqg-RaA6kIavIwTOmRUzRMm7gsni-FXY4jdTTKSzDeLr727uK8XsaYu8Otrz5_OKjVlgGLqz9ESmKhkoqNZYB8_z9ef-MMXVo4gn4L_xw8x8Eqs0cBqN6PqT3JmLcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=JhB_UhBUo19l4fAofjSJ6uYhEtx0_I-tu2nXUlfJEiktIJAz-C7RBW8uJcXAQ-_JtbOumJ12U8ZVSRO81I7ILNHgBjr3CKI9KfgFQQ_G11dUbs1E3qtiuxNTQbvBX5gbqfHpVKOa4AWcbmjM9E9JLXMmxS3WaV-qEpYQXmjbcpBgjdCaQ8EqVnNTaOf_uKl3uy9O9-VvQPcZdOaoSLQE9jef-0Th20m8QM1yp65x2dBBMYi1N8GkbIhZN7e9qxuL2AeF3jTTqDKzvn-91IygkpIuzwqB2deMc58p_bJX2CpVJlWRJQvpoDJNnIq76SUY9cvJzfGgn3GKRaPEyBMZTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=JhB_UhBUo19l4fAofjSJ6uYhEtx0_I-tu2nXUlfJEiktIJAz-C7RBW8uJcXAQ-_JtbOumJ12U8ZVSRO81I7ILNHgBjr3CKI9KfgFQQ_G11dUbs1E3qtiuxNTQbvBX5gbqfHpVKOa4AWcbmjM9E9JLXMmxS3WaV-qEpYQXmjbcpBgjdCaQ8EqVnNTaOf_uKl3uy9O9-VvQPcZdOaoSLQE9jef-0Th20m8QM1yp65x2dBBMYi1N8GkbIhZN7e9qxuL2AeF3jTTqDKzvn-91IygkpIuzwqB2deMc58p_bJX2CpVJlWRJQvpoDJNnIq76SUY9cvJzfGgn3GKRaPEyBMZTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=XrMtn3YYN9fdTfa40BDQNOdTBUUOz3vb17jVRChfaDfdihojOtuiMEpnT-k80tFzesLwwPF3xplmJs1wSBR_PquS1wWWxAkMJ3997MaKJ1BINKG1F6pGibZ12l0KNWnwcWej3MxyNb_Z09dVKnLccvZOB8DVjeGqNBhXDj9vFT4EtrjUNrsXE5ninp12fcjhxCD7nhQrDod9OG6CilRlOkU4b9GAdw_bjAekQgSGpImqgC1cyZXxXOFhFn8pV2xXTnJwMOJPhKA8_gJbs7hu1Zsj6MIju7IHwwE3wlwulaywRrALa2X9qhApzRGP4N5J5W01bSgxSk2TfXrdL7b4UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=XrMtn3YYN9fdTfa40BDQNOdTBUUOz3vb17jVRChfaDfdihojOtuiMEpnT-k80tFzesLwwPF3xplmJs1wSBR_PquS1wWWxAkMJ3997MaKJ1BINKG1F6pGibZ12l0KNWnwcWej3MxyNb_Z09dVKnLccvZOB8DVjeGqNBhXDj9vFT4EtrjUNrsXE5ninp12fcjhxCD7nhQrDod9OG6CilRlOkU4b9GAdw_bjAekQgSGpImqgC1cyZXxXOFhFn8pV2xXTnJwMOJPhKA8_gJbs7hu1Zsj6MIju7IHwwE3wlwulaywRrALa2X9qhApzRGP4N5J5W01bSgxSk2TfXrdL7b4UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGUrSDFYtlniqS0RLOJSNnozvyrEWASq-Hc44yKmpXYTfJK1h0psj58VfjLeoQyjHV-z8mZ7vM-hvwfHh2vgowoomX5MAvc7O4y6FHFmbLk8NbaapTdLoLtGEAuqfDXWEuJGNzdvvMAf-2K00dLV10lzVRke_YG_MByd8m0wBeFMr_fS32bOkyFTgbp0Xb7YNawMlvn8VxpelVWY93RiVIgB6z78JkoRA4iWb5opaLVlDLpNwey-U8n2AL6D4kiK9VDOdRJhr-yTGkhXwZsw3C0868yC7G7jYx5OlHsHKUKIWRt0jxxppLFXMjmQwI2fRyiLob6lCZA9ySQXe1E10g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWiVVwkpQ0Stg3YbMQwfWAKOx5z8hzU4rkQBzdOAbsRuNMji08BlzC0irj5Hvpt9Cbij7F_0PbxoSKAmICrBbljOl4_klPfh8ad1-lNAY4lr_PRAx_E8Xf_nDlqcXE0vQ0cS0XQ9rhYGwLu49d9NfGKBtGdIV8cvm0mnwpVCbtCzRKHJ9oMlLEb09Oc4_hytKYloET9NQCpSg1lAkB5dx2E3Yt7KUWYerBW0EnxFnHSSY-6hpe-H-5MPGrXZfsrHS9wk1i0x63ogevKM9pFK0UTwPSpbhbz6SC_njSPoE4S1mYkUqDsELqmRAo2uOTV5PfrvCEvB-1CwoRL0Sy8OFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awICM2SFH-N_RAHYe2NdpXuBSdvVmMvehOQZS0Lv5m3KkMqkOBkDmtBkuY5gE7l6Mg9c2yrXHsC6rZbEzsfVqlRVYMqoYGFg4p-3uQQlftK5Cez1d53e9qiEGqOixuKBzzoTORHg3FvRxlbc7W6LGOcoecMhe8ECiNN24xigH6lrRq3fp1SAWVq1gDUos3PUqMMpEXGG_9BYLuA25MHTBo6mQ9-jMgxp-od654bm-ef6Os-nPJHVlyZN8aXngUD8441XBM9HD_QtkblTFjHvXkLmuJu25sVD5kGNf9YMLsxQOvGrzIVaIC9_MomauFqqjI2SNkQAVnazPz97aKqDFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOhCiO83Aeu-OnnxnO1b9J-XCaZoUkdShlMxVcG3mioNrGlwX61NebRDTchIqbXaiguH1dIF2dLNswA9Ojxn1Gb9zjbLn5InhXu7_j8LFf4tW4QUMzX2IMcqSNF6DEz4gKYoabtEvQnDcgTSuZQI45g2ouinpNqW5mdnXt2dxGMwWOCqWdrxRYFbnHnpDV9pjpqwpX0Vx1EHpXUjGn6GtMWwSgFwkTquU_EGCEq1h49MqtKy3jXkX4AeB58JZQsHrOO7JVa9n3QxI5vrY04WgJ-vKA_PZWKSPzP0w7YWUs8M1zyhq_v_7W3nBEFYo37RE3z6q1yabRPsqQuw6U6qGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2zyhlZ5SHXE6sbDkoMxo6erN5MDss1EPMwgoMFpz0EUocIVMzIhqpey8PLMT72EbdnjDTE9VTOsVHzUKmYKFHmlpzee_qScrdHaLqXZu0TMbsFyrCLPYFAF61B5Vjw0nIVNFBxqf53YLbpS9dGHxHub_pB28WS4lOKI6lqhiVH41FZ-M-Vpx-CVQF7EYlvqRjE--Q80XVsOvyaiBiiqDHB1_xahjk6FhlxqEyz6a9h6yg0pFzeaVcMtlNpheHz9FDLK2HlyfNXMYtK-b4az1EF89TcJ07ADc6QAs5xCc1sXD1V_to4NpSCzS_CWsq9wWcDk2YYQBZ_rPeb322V4KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PefxfJdKtLboTd-_VktjJXLwFpe2JwPFi-mOIdomYMO4xD4JjtL51UQ8xiMA33Q77PIs8K2V3HH6SbXj946OguXp1DG79TLCcRFARZWnO4oVsQ4wyW67MUVYtM6uuGymjWR6gYOxZK5v42JvHwnTK5S_AO4AtCh0DZFEuDKwMmjgUbAW4fp90TDAbG9VD-FArnMo9BlSs8u4XYlq7VVQEi__6rexsECnm6GCUlJUSRcErn9wZGSmd5xNCVV7ZMrRr7is97UKo6bKtIhCjn2YMe0z5OuOpqe7IzIFUsbBZ-OvE_-r-sm-oqPCtkTuwVLMBqN097g50tu0NTpJOEd0fA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=QoZN5f6cyzbtdqW1IKhKv8hbdwDuowFHXEH2xCf2mvlj9292ogaFJ_11GOk4-au7jWPzD_frJkjCbvnltRo1ozFtaOFuDaiIrKPmlTlEByzyoef84UwN0mSc7oyT0lrfLo1IRXWgE6tocjv8rGVpI76PCxB0yQZWc0C8cgF_Msibxfc6jejibRWW89KRr1J7YjYgsueYYjOcxkQhUWA02kdHYCVo3N6bEDU6JoGmD5No5YpnS9TrElEtZ37pF8-l8LMM9diybGRBXAz2ykm-HSUFrDlIWMnTkebX89lCPyOK9HkweAI5EOlk6ACVVvVXBl-2wuSg5cWuIZSvcxAxTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=QoZN5f6cyzbtdqW1IKhKv8hbdwDuowFHXEH2xCf2mvlj9292ogaFJ_11GOk4-au7jWPzD_frJkjCbvnltRo1ozFtaOFuDaiIrKPmlTlEByzyoef84UwN0mSc7oyT0lrfLo1IRXWgE6tocjv8rGVpI76PCxB0yQZWc0C8cgF_Msibxfc6jejibRWW89KRr1J7YjYgsueYYjOcxkQhUWA02kdHYCVo3N6bEDU6JoGmD5No5YpnS9TrElEtZ37pF8-l8LMM9diybGRBXAz2ykm-HSUFrDlIWMnTkebX89lCPyOK9HkweAI5EOlk6ACVVvVXBl-2wuSg5cWuIZSvcxAxTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4LOgGdvbFLdEf90qhcEKCgp699vjfAsKiCCA9ac9AhtlufYC7ek9553Omm1p70UzV4IZ-TT92--a8h4_0k1-k2eiH9Pa2PCY-OJvh-nbOE5S1fUs55Fr3tEKNm1GUaRlf4uGrLloV8h_bQAOc0P1pQQKXPlgfT-78yfnBXcxa6oIRiDvZvEbHUe_W0K4UXB6OxzOf1g0LWiVWwyzUh-K_d-vJcRV5y_KOGHLHsj8evkA9iZ6R2guS8EDAU3uhTNoH3gpefvXMf5srSBB-miIGWLyCTmHwACNsTeVc08EVyFb9JrSkt1Xld8WILnjYarJ0gX7JDDA194-VBdEFItqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=mU0NrVz_E5zy28onTACDkLFjB8FK9027WZS_a-X6_1VRIjYg2tSdia4dU2TKPW5Rj6f7FalOZek3BQv1xC0yp7KEOAWozwsvxE7Esp6vieQzBvbuBd6lxx4dhZ8M9SaYFoFgcO1LnsmDRmC3SAQTk3EHhrp5oXPXPKXj3dNkdWbhnRI8VEDgffTaEWD66vQ8OnYfn7F5_7I7BMsDkcoA709jTGfNxE8ZMpwzle2E5O2aINU76uC4d5zZlx3Z8bxU6PfUqJoeFXMJAdwF8QIRJ6NqwvM2SZWiTK9fS-te0FonagAUFcZVDtO_6NsJaYX0skZQAo-SDacmPDsswQ-H7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=mU0NrVz_E5zy28onTACDkLFjB8FK9027WZS_a-X6_1VRIjYg2tSdia4dU2TKPW5Rj6f7FalOZek3BQv1xC0yp7KEOAWozwsvxE7Esp6vieQzBvbuBd6lxx4dhZ8M9SaYFoFgcO1LnsmDRmC3SAQTk3EHhrp5oXPXPKXj3dNkdWbhnRI8VEDgffTaEWD66vQ8OnYfn7F5_7I7BMsDkcoA709jTGfNxE8ZMpwzle2E5O2aINU76uC4d5zZlx3Z8bxU6PfUqJoeFXMJAdwF8QIRJ6NqwvM2SZWiTK9fS-te0FonagAUFcZVDtO_6NsJaYX0skZQAo-SDacmPDsswQ-H7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=Sy2WxIy29ReNZuvgs6irbeklYMQMJbzPf3qFxLscw2skImhAFup459JARmmp22pZzVt_gX7ymCYcha4hm2-1PZWgCh4Cc0Ely1RGESxChkY7qRapmrCwgKRiPpGthG4WEFIOR9fmIZtSiMMBaRMJwowj2TdZPKoXzp-XGkjCYevNriJeQf2cE7_nC1eS-Z7PwBmXN-vN7yrMYevd8fjCImAWcwTy6iOrEvfSHCYjXaYEJRlsSvJoQWw0W_KbDyVweeEkMbSs3i-5aaLSpBWAeiQ5Z6RuYyzp1nDZ4JulD_r5WyfkJdVkMsmXgg7sS1cO7fDVvc_oLU7EG2zHXXA7rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=Sy2WxIy29ReNZuvgs6irbeklYMQMJbzPf3qFxLscw2skImhAFup459JARmmp22pZzVt_gX7ymCYcha4hm2-1PZWgCh4Cc0Ely1RGESxChkY7qRapmrCwgKRiPpGthG4WEFIOR9fmIZtSiMMBaRMJwowj2TdZPKoXzp-XGkjCYevNriJeQf2cE7_nC1eS-Z7PwBmXN-vN7yrMYevd8fjCImAWcwTy6iOrEvfSHCYjXaYEJRlsSvJoQWw0W_KbDyVweeEkMbSs3i-5aaLSpBWAeiQ5Z6RuYyzp1nDZ4JulD_r5WyfkJdVkMsmXgg7sS1cO7fDVvc_oLU7EG2zHXXA7rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5LN668GqpNFWax7iKLCOVywPsSnA7Sqtl_Y-s8CRk4Y1V-Y8VtQbwujVBqOyJgqEokqFW00RiSP40GdNTXR-1mbcGMVRUQAw5PB2vHUmX-eu_Tp_HDZAKHV3qY4HgoThNZC5_G38gdgwoSCClKWnRN57uI6kNDFj3Ylzha1zsWNl2isSdRahCKoQHr1tJu4thOCDAgBksT5vtMSAIN-Y-HW7uCK280FVAJAaAlvWDPIhPIaAAM76gKeY4wAWsJXTNFx40KUw8bi5WpUwPSklnWV5feLHntiWTvyGrGA7A0S-Az6KdDidrpfC_OgHFZLkCW-GLcvR3YmV1SaqpdKkA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kl0wpBzHiDdoiTv259y7Ue5jDh_YbcJmdxqPyd8UNEGj0u_tSgVYgaNIvd1NvMnMqzKsd8Am2GRkyf_9Kquq9SHVoAC2NWOCSVG-IK31KGtbwSwQrObOBS4mAaRHtnW7RUokn4lZxL5exb13m33V8yE4jgoDrOCKxqgrDDslmF4IJOU7euVEdGY29bh7fLu6sHiQ4T7oL4LnzIxndasHJQHjXwNrTaTQRXAmRNu4UJb6N83FTT7YkWYcqXW5JH5a68tlq_aLtRfwUom037Mn8INlbTI1GFPVHY8Z-jW1aXnrjuJ2Kl6VAu8CIlgDTxEBqZE0pfdvlQB1OL54WUp30Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=ZhVs9YjEmJvSv2MO2mwl6zQOBl0p0sKyVKd93wXLAx8elFgxo4GbB3S-oxyQsLw25ntigQgxjeSOP8qHuQU9c6j1zGYPdU9FfVq1kZjh0pJ5lybI_g_N0WnOx4ubX5fEVMowIR5FxfR4teZju1VJtvmlHo-gwVcB7dEI-OBC-HaFGjyg70GD3i1SOzG_SkmmtfORUzRcLnsGGzJBnkdhuKncSRWE2Wv-8j268d9ZqQhOJnbxYhJNIGYqfcIqyYxdOofO088qXPFHktOSJpScBfUzhrmquRRIEEvg1xJTPIsDKUp_94OliLJKUTRqpH9Sj720JO2YmDk9yRdQbKiVKQrVhvVBPtWTkSAZbbnM8E4hDZg_X75OuvqGqb_Wkanbguj5uthSKJKTfV9_h15lS-Y0kiTBB0MnZTVXOHpaH-7bJsgeqLKsoBEesEE9tWOh3Ua1YxqYLlfr4PYRfPfJAuklkwQW7CtGdylTGUCoPiI8AiAsv6tdkr2FMs8YL2lhJOsKBtjRsx3SONJmVpiJiyksEeqY8gvi-YnWAM3aRfMfiIt4Md8uZvrhJcEYKM0uvPxBn39JsSQMraa5T2dZZz0p7m1NZ8uSuIhs1GEz02m_vdmyDnrqPj5D_0th7_T2QkRUl6i4XGDCx8XeV1x7YAdUZaWMWfSKhENM73ivvgc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=ZhVs9YjEmJvSv2MO2mwl6zQOBl0p0sKyVKd93wXLAx8elFgxo4GbB3S-oxyQsLw25ntigQgxjeSOP8qHuQU9c6j1zGYPdU9FfVq1kZjh0pJ5lybI_g_N0WnOx4ubX5fEVMowIR5FxfR4teZju1VJtvmlHo-gwVcB7dEI-OBC-HaFGjyg70GD3i1SOzG_SkmmtfORUzRcLnsGGzJBnkdhuKncSRWE2Wv-8j268d9ZqQhOJnbxYhJNIGYqfcIqyYxdOofO088qXPFHktOSJpScBfUzhrmquRRIEEvg1xJTPIsDKUp_94OliLJKUTRqpH9Sj720JO2YmDk9yRdQbKiVKQrVhvVBPtWTkSAZbbnM8E4hDZg_X75OuvqGqb_Wkanbguj5uthSKJKTfV9_h15lS-Y0kiTBB0MnZTVXOHpaH-7bJsgeqLKsoBEesEE9tWOh3Ua1YxqYLlfr4PYRfPfJAuklkwQW7CtGdylTGUCoPiI8AiAsv6tdkr2FMs8YL2lhJOsKBtjRsx3SONJmVpiJiyksEeqY8gvi-YnWAM3aRfMfiIt4Md8uZvrhJcEYKM0uvPxBn39JsSQMraa5T2dZZz0p7m1NZ8uSuIhs1GEz02m_vdmyDnrqPj5D_0th7_T2QkRUl6i4XGDCx8XeV1x7YAdUZaWMWfSKhENM73ivvgc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWp2Yt0225V5_zUwF5-jWvcrAQ_iKjCQpi3P8Kk0R-gkAKQQBUPjEoqNEfXjuFD70fAE0TAi5Mm3px2xdysZPby8zw_pq_q6NlvZzLkdWOYVUSiThLDU0g1iUcWX_lRUH0d0UOru7WJIKLCvZWhD5qbCAgmFAwDt_Y686tjboCiBFS5K8V8fggGmpypAcfXUPHYVhNMZH6chnSwGd5whNXNxAuCLXCwv3ZNT7VC4OFzvtsqaXeWCFCx2MxBZd7iNmYQj0zc7uvU8Yxinm2pyyPknKTB6cpA2am1oytAQl3iOAEI4WayGqmobdpjfTN7H2yHRaBwxz1pUSPhDqe2PJQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=sHtNc-KYn9FDD5c8Ap4Dht2spkds_IghFf-3bo9sXn9-ExyRXafhHiP4O2tIu25UK4BJjomV2Jl6XkWm5sNRlrdmkelmTLKdJU2YwtBWSg_fICuhEm0GENdBNd7fYYnEPAoDH97Sx8ZUDz2JSsPUajlQNuo9uSZN5yqKIkj7b_Cg6czhkmEwAGQmSaW4_BAKj4Hcsr0OFqNrCXlu21QxPInCjVY4a4nboA-I6GLZp5fFCvqI-rQkk6T4pfHQl5z3wnak1N0tYwZ020RI0Q4-Huq273HXFUQgrddNvauiycc0YrT5zexs7eYHw0J5XFAtodCP1wdxsfdxBzIn062qIFQeK_2i2KUfU3xXiOl1o4-_hzT5RRSMe1sRKQtKFRi48s4sVRgZaSHUzPk4OTOdRu7o9IuS6U7Z9udGM0VgZ_L-EsDDTL3R77WYpML_kkj9X_hoKa5aj3FRUEGYBFIVDEWYwyCeYk-bDv2xjkKUsPcvK1Cc6bEbRVHAg67qTrvpCuY6tPmrm35Z2xwMEcPWV2-7fCs2V5ZCL2-k-tJ1UPhERy40zhziV_RRveOESajceaGdFQAjtuZMTMzfxSziF9HSAj4y776RTbK0xQcXK84a2teYqMXQX2JLXhoezd2w0ke3v_Og0iI2HL94fnTmj_95PpuPux-sFJ_ZajQ8SS4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=sHtNc-KYn9FDD5c8Ap4Dht2spkds_IghFf-3bo9sXn9-ExyRXafhHiP4O2tIu25UK4BJjomV2Jl6XkWm5sNRlrdmkelmTLKdJU2YwtBWSg_fICuhEm0GENdBNd7fYYnEPAoDH97Sx8ZUDz2JSsPUajlQNuo9uSZN5yqKIkj7b_Cg6czhkmEwAGQmSaW4_BAKj4Hcsr0OFqNrCXlu21QxPInCjVY4a4nboA-I6GLZp5fFCvqI-rQkk6T4pfHQl5z3wnak1N0tYwZ020RI0Q4-Huq273HXFUQgrddNvauiycc0YrT5zexs7eYHw0J5XFAtodCP1wdxsfdxBzIn062qIFQeK_2i2KUfU3xXiOl1o4-_hzT5RRSMe1sRKQtKFRi48s4sVRgZaSHUzPk4OTOdRu7o9IuS6U7Z9udGM0VgZ_L-EsDDTL3R77WYpML_kkj9X_hoKa5aj3FRUEGYBFIVDEWYwyCeYk-bDv2xjkKUsPcvK1Cc6bEbRVHAg67qTrvpCuY6tPmrm35Z2xwMEcPWV2-7fCs2V5ZCL2-k-tJ1UPhERy40zhziV_RRveOESajceaGdFQAjtuZMTMzfxSziF9HSAj4y776RTbK0xQcXK84a2teYqMXQX2JLXhoezd2w0ke3v_Og0iI2HL94fnTmj_95PpuPux-sFJ_ZajQ8SS4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwFm9LhUS9b2Q9CZDTmLeSXSC_Parnj2IV0KhDLCR1FQ91I6cHZqCACGezKkGPvIobgQy4-ctnAAm_-rdJc5Gzx6sabXHX5GFHDR2v0j36xpg34PEM9ywWWWOBTcYrdfH2Hc_xGjK8W2eCqMlGtR_mbObRWFFnj-yQSTiVU4yKMUl9W8WemFY35CLjNAXoqcVeYFz03OjMn70ph6tgpYcFO-RTq48PobIBzedsVkAAg9cGuW3yF357JdbzdD0HbGixPPdkl8IBpKOLfvshYUMcB6ncWnqoYtfsHwU4581q_-W8enMmUrZmVy8ODxwUVV8uF-59w8GARZsVxoKUbRwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmFZGxxAGSAkvYfamE_B_MOmp8YnsJCmWYy4npUUbEEfpGU1wRQ7eXH6o5K8lSOyPoI39q6dAdfhbZbhsAa4nFhQfEu19ud8BKrFPYou1YB6J0v5YyyT-8_VQWv75d6oa7Sba3WpyWeP5tNjKQjK4bLpBPEYWfIRHtDnoQ513RZfSIBuFK1hmrZwq0JwXmFGe5_pLreX-xCbdraYUSml60id122OfdOstamOgKV7jgZdUT-WM6qSgXeQiH-ON7iyqnZorpMXkso2IIAa-iw8WhQPTBiE6lRPDTsisGAKJFuhh20iN5MfIaEGUUP8j8WM1e7XVvnhZqXXrSyL-rLGjA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lc_m_dsV6VdeJbC4Qmdl6Q0qsKX06hEfDOjDQJUWQV8aGu0gCJUJQ_2-my27JAT7Zjg2XzzRl8LXBhLi2eKHBvCr72pmsz0Gu7evBURFSQtprpG7pegC6_6mZslTQuOJ8o_hHc4GsJ5IKghD-8H97QDxDb_t78X9CuwSd89K6uoOmCA_mD8xCTg0gxUhHvamVEIjDtv2IQFtkqy9fRsPWx3F79dr74lB2TDtebTCYTrW2P6pUr2N52WYLx9XvBIc0OcKPO_AZeHtLLq9DN8p6rN3uD7B6RVP4Ybrev0ZYa1uj1Z-zX3LfeR8Nn7mCr_LyspiXoNNGm_MrI_Ql-O_9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBIMZrJsWaO6y7dQnN1H-M-u_LDK8dT5GdniLRCNOLoSRyt5f1lCj0bcGzEi0o0tj3VsUNGJTXkRDCG2E3eyj5en79CgrF6VzXPzNdBdfn2JwGWhEEuk-c_-HwAugZ9T5dkoxHiDzEEL_66kWXkab4ZzRENr6lNrSne3qtZK3_f27-KkjbRqdP0yj5IJLELo0FgCPV6A7zR0ix_xdhMshSS8DXkakFUvIjXrPQszdSoftg_KqC9kfauC-BBulTRSpqViOSQ0mW5bL0Gw9KaNUtPsnlW3NiurgkRBOg2FC6Bj5oT8P0gwILLQmnmecSDVyaIkg4uI63h-hWepShgMow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6hUZ39NAbTuo_VdACQV69mxMVGmE4g1-j2Vtt4eqDB2LlNau3Y2JVMOJyQumHD3r5GlnahYKCZKImKXVXpfETvqATYuRRdK764fRh34ljxdy5f9g0AJeLG65FsKb8piVGRG6bMBOtd-ufhs2FtXZIFj2lju8mdXC3zSXqtpaBWpUUxfjqL-zS94V4JXvSAKwrBEmzp9XKnfflirPjOQJGaANu76ZpHuR9zryDuzgpAJPOrbtR51HXLrAEJ6eBuZA5Q2wUMDu_vQWec8Q-ubCyKA5eyk3pS5m9Kbup1oMBumBcKds2xlPqQa1NH4_7W575CpMBbfvbtYGvPtoiqDpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbiwnpDLLrn8Wp-x3KlLjO-w460JBljJPeCLQa7vYaeq13a4cZw26z40vHWnvjGWsHbhgiH3ZSJhyEReUFN7F4RH4vfv-QyIHTnZr4WH1KsIWnuX8KDfyM6QwpAhnH3ayoDN9EqnimRSeI3LzrdF0gY9wMpzB9ACqCIZygvCEs65SbPIAkhWC8GMFuRJ_RP3K2jkgzI7L23xct-GpzsKMzywaQcp6Q9xSNNddvhUFxT0swI068CHHOyBZRZiBvpPtPZ-X51S5niU-BstnYy18S7HgCVx16VJAPPzDOII0BvjCR4g0tSUZEl2fvPu__gu9QUVsZI-LK8OwQxrYMkAgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9ObsRDddn8TN7PRa2LZA8ArQmpOvKkUwAIfLx1M3GvkepYpuNNn9aepA7R2itSJdVU6W8A-Nou6aJTndhPZHQ0-nWChWL_7XhdgQn0vVJn5mdgi19loD5tidAWRJ9uljPgGVBzym7kX-2Oewm_51okhu_FL0ADyC2pGe9buwQASh4DaUGklMcQVnxmksWgrDNU-wr4kzv85MtoAFRcaVx4qVabAyv6blHwD3v_QE4w4St4hKi0u88Z-flJ_IVYbxUyAsjwyTAeqjBjc7Q-_GabXIYk-OH81tUzUvaq5n_5u_JmjKrzt6aRFRGbWGP38lo0M-GQeaSP7n9fsdJ-4Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9XC1OEz3NDeZFw3eG88roFDgDhibqg2X11Xvj-FlIdaI1qHCkaftMuBPs1MI-12zy7Y8qEZd7KgxL2bbv1J9j2Y56KzLYDycpyVlXrEzdM4YGF8MWIH2G3_9ifBtiufQO6AZKoQZCVs42nAiIVHVjIYcc39h9iTPlmONW_ItoOxKqljyJrVu6y0dAu2UshQ7Xo8Lt0Q8KP9UJh-3uNarE2um_7HiM_7snWS4GqUlp120JbiArhzW1SNqJLK6MSIfuZqEzZBgZs5e4sPvVEL3_Kltwces0Zft7J_nndTXAHYgiKN_vBpdhmU6BtgcAajvbvFTGb_cBVc_AG53uMYsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLGfu1nn5riQX1NvMXUDUFmcu7iC4WmRarNa4yCt6Dqva1Fqk0MqemE9-xCuiLhzeVJTh5iZ9OWP1kF5fgcNcZd5HAPqXv1GqaZSI2XHfcJFhTfc7zN8168nr4Ueyhh39tXyt8nTze24vudgUDZl4FLGVhMOnJtaAu6Q7KRwYCnNlITPIxNpZ7ylxmsHsNxfHizi-B0-S_o1a068KCDEN0H8ad1cGMhrf1QB-B2zlibwL4zMiythTrlMDPAJ8_0Ff8HjD5YeLqkrLzG4A-VwhdYCw7g-lOSxnYQWdW19q64LhQZGxcW0L_Zi7uhuNyPQmbx6eRxjdsZ_3ygeSwAv4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1a_EGqeeNGE2bEOU7mHQxYAf_rt2YpvCyg2BnxOhA_3DBuNhsmhLhQf2Qj4h7iZKpzGMLFjVFCeQxbeIIYceFpzQEQshCpVv1RkQ-JzvOg-IqG8nmRNd25nlE5KWZy6yNrElPJoLIPhfPjXXYwIskpZqSEtLlF8mdoB8awoeW5UiZLOC8LWECH12OibiL0WRIh_tLnF4hJ7k0K3ninyyhrJPs-kqieWAjnYUnMJNO_mIOAKTWO6zJ4-Z5B7a8O88uDEytgEz0Y_kZQE66baLzi-bHOaXEn_pdYka53lHQhb_Jk0--sBItSUPg_vb0_d92xvdYkYSjYhEzNsmg4A2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEYxEMIFmFlofpcYq_w60heQ--AHnQCbgDEUg6nzPXjXQ4Q9Hr4SOdNnfIyY5A5rYbxDw7fwjCnA-Uh1vVVlWLtPTYCGO5q2_-9ZYfQ1QLK39qk5kD-9sl7Z0LD1Hp9a9IA-eUref3lXHzA44f9mJuJ3H0F5a38TiUIoVVpTo4cUbAs4aYH9ZxyPYn31jIgXX365L0mWmdLh_pUpbQX0P5v0mzEnpCkdSFvRAtmT-u0346AWvWOyiz2BCrc8ytM1EZWm2Zi23BBzTMy8AUYlOZyEzbsVu7EQ65DbbTjaJjES826Vsu_9aXzqDsRF3HN0bcNdA2u9A3TirisTxaZmig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ur-MB7-ZyBt8Rdx_X3PJG-tX88tNjauTYd59pSxPOPjcxsNIkiJ_e8eWSnfKSp78Zctv_tewXhk9et2K_uAMfGrkKFSxyUxnCiXVoI_ErSo79vJT1FB0NKYcPTSS0IXNAyDHyBQy8BUiYiMMfBiIKzjjrTQbqT-DQiEe0zN_iv_yP6htYtdX_tlsbnv1wTjzQYGuB8ZPEj6kMvTpZ8j6RrpkoGqxoSp3JavY_W9Ja7dNFBCM75XRwfGuMe7sR2-jWgwGLRQ6jFCQtJVF37235yeQbLRKtzGimvJaCU0iBwEi4gTLwTyf5LFYONIo9phEq0PLv3wfssUYZMtR2aQYuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HD4nPm9zUzrrTNAPRltyeuE31vQMkvdK3nuDTHDSLfybZwA12-UOnIem-Z6OgVI0GR7-mXhIKe2vk12NREfvGFFAtDNUQjl5grbd2OXQeZb2Z_JAujNOjfuVy6lcVAvd8aQo3UEFI5ubYsy_sCm6dlIg4XaIQ2vjUMSTt2e31aGBvuEsJ3uG-tNAOq-_2gpQGqlqwLRXfyk01BeHmI3csnfrG0b0LtqITQLP1jWRxMh5QYMtCCDYd-jZIsJ8PWs8AdK5_bm3DediIXeKbaaVo7hBA-NykagHUMu2c3hByUwpppIAqz3ZIh7fXtYwEqgvSgdHCqkxXMT5IttRJziJFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGRtTgR9uRR351DjKu8N14fXPJuUKTIfSCRXXwVfgfjm2nHu5tuCAO7QL7Lc4_TS7TE0JDCw4OzxXqjqYh0OjfdXsiVjuHGnebwDnI3Pi9lGO8jDbGA1VGVgQ4wypkxLHvS_Ip_o2tjrlr9t0HUlcRfmuSN64WSrpQrep0m5EKI_62Aj9bqxeHTMaR63rqzqiMzmQ2E5hFQKh0QSTqG7crlRxrIElJ709fpe95ra7jtPe5ZDnFjDuOVVpnq3IBzggaOfY6N7hMSDNKz2p3JjqzQQjtJ93dw6i5NutRUVa2x8xImbSKqRCcNjN-tNxP3fUI7--qSWv_obvyH-HhXWFg.jpg" alt="photo" loading="lazy"/></div>
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

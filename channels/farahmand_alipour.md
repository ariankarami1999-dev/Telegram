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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 19:06:53</div>
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
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=C8EpFNLNNzL6UFDJoakqjQXI47V96hFJc9T0fWhAOV2mcT76GAJkLk8X70yBjYyIu6J9VlYNi1Y1_ZjYNkVyRtVF9UTJYZCAP5-hmKPci9FUGzbvM2RVio5u84H84XCPXIKuKVwfVpy-He8Y86Mh56MiUm0vRDrLehzs65sYLAVSzgyNRhoyy_eLjAI2mCHDDrKVUW2fZntuR7tVRbFWeeNkoh3hdA4ACcQzoB5n3Y2nvrDQRwS7VW0-EdFxSrfv3jRor_99uon3nndgvGgGFPBNMn-hItg9T1fNfrscy2ln4WIVHHSNIQ22Fb6YAdVUxqPX97u1LCNgmmEUG-3E9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=C8EpFNLNNzL6UFDJoakqjQXI47V96hFJc9T0fWhAOV2mcT76GAJkLk8X70yBjYyIu6J9VlYNi1Y1_ZjYNkVyRtVF9UTJYZCAP5-hmKPci9FUGzbvM2RVio5u84H84XCPXIKuKVwfVpy-He8Y86Mh56MiUm0vRDrLehzs65sYLAVSzgyNRhoyy_eLjAI2mCHDDrKVUW2fZntuR7tVRbFWeeNkoh3hdA4ACcQzoB5n3Y2nvrDQRwS7VW0-EdFxSrfv3jRor_99uon3nndgvGgGFPBNMn-hItg9T1fNfrscy2ln4WIVHHSNIQ22Fb6YAdVUxqPX97u1LCNgmmEUG-3E9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8ZtRouOuJ44FCRmsCpq_X5oiMfXEZklEpqvjTgy2paSsAcAMjRipHUBD1UKc-FEzxOCotkO0QOogsu8q235ljeHcmwh4oHQ17wFIhji5W7NOvMP_k55xBF7qjRpHqMM2AEo7w6agxvLe0Ee46zjFmt2oiCAC-GRGmIjg1n8Gc3Fu5AvVBwPlijRkAgatTu629ir1o9gNAr9KXhGxHqJWs9VSy2uE2zH76HutpRFdVBG8GWlvOhPI7T6NcJwMiXCaSLNHZu_R--gOxNfpcdH82w28D2e1LjbdzARpTWXNYikgR7QGxDQMOTiqBHpeRkLJN1VBH7nAEnTzHzX8BMgMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUBiBIF2tUOO0wQnqsillOfd4Vyq1mjAe60V1V_5uUEXwLm7DCsYggXFH2sfuxUXpl7rXPQyPyq15WOcFNB0aBwl7nXSuXJzc9X2lLhR6RJwOBpXJcoMlrA1cDhQrxWvR0QVoSUlcXHzH1CPldIkeeS0vDzyqIw55-i8kXeAxh9PzkqcGrzrebKXlw6BUXm3eeKpIfZgNzyzn2eqh3XZ-0ky8MfraCvQ66n1jgkOmXG_0bbfvDaHar3ovpmAK3FafMD_2hLHOdUgy9FfWD2V-cKh-mfwWlMyvxVIIbou_F3IzrIiHbHxuCstpolYP0K2KO6Oy71fq56S5lBXqRnlpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHgsIzpkcF1wvi1aadaibqSh2fGz9M2SJzmUyWCw-b4BG3IteOMDRNm_JlzSA1Pn12cRFv6Ad0JjXl7t5jTXi0wRc7CjHGNPPd7gHPseR5XtlS4gSK0-mF_ML6zkTb7qFnvdM2hTYcK6qKvBv66xAEji7AMXXoWk20pjqCmOaf_SE9eqCGa9bqDqKv9qSi1ZTG3U0veQlmdHP6fMduTZ35QZ4a0u8ZlsGM56P0muwwHVoLPxMVdf8nJJxLTWLdkSfFvHkqbfd-rUoUUFxq6q8ZkddE_UgK5tgDFi7b12jY4mcAsaif8U5Pq4axViUm8W7GgiLcGwNlVEfshQXH1NXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=MeCWThCZYV_MV5P00ngi7hKW95R3DudnaWfbdC7OamS1rG0rDO1d244ntDoATCcqDwXJNXmUiD2tZqH1BPYF5Ckov6afNrEPaS8-AFWKLhaji8RE3qU9vhKAwUgXg3DcjxYV8tebxr4sfoEL0X6Z8xJzMe9VZ_dd4rE2VnH6_eCd5DWYkHFgGSN8MJ0U8GnLoEfHizqUrulSSLJqX0ZEknDdMQL3smJEWpF9bMnn6aclvojU3zANBgwtVp33i7dherrHGIfFIr2Iba-xRfN7vkQ-lHyW7HjMvXXsL0CRHEBKyWh-Iy-GYfajloUDJNNfdEWBr2_M4j8895_PiIKrlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=MeCWThCZYV_MV5P00ngi7hKW95R3DudnaWfbdC7OamS1rG0rDO1d244ntDoATCcqDwXJNXmUiD2tZqH1BPYF5Ckov6afNrEPaS8-AFWKLhaji8RE3qU9vhKAwUgXg3DcjxYV8tebxr4sfoEL0X6Z8xJzMe9VZ_dd4rE2VnH6_eCd5DWYkHFgGSN8MJ0U8GnLoEfHizqUrulSSLJqX0ZEknDdMQL3smJEWpF9bMnn6aclvojU3zANBgwtVp33i7dherrHGIfFIr2Iba-xRfN7vkQ-lHyW7HjMvXXsL0CRHEBKyWh-Iy-GYfajloUDJNNfdEWBr2_M4j8895_PiIKrlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=pFp0NCRlVZ3UVuWZ2EHe4x4fIISxD5uJPgUPAbXU08dkVb1rDiu7qIdREFlAVNscMzLlafd4pCamQhJjoz2giv3IMIe2XsghT0VA9ThgIWlIoVDwzwIm241lQPpnuSVq9tKs9UgusQPTcWYjgbG1hDHPgzkWgAx7oRWzVGAu7cbVGcEtbhLadfFqCfIn0g6ugG-yEuCf1hjv0qA3x-f5f3FMQcedZ9kb0yB9fxOL1mUUR4NZFuvarb3545b0o5wdWT2CG8mFDGSjE29iIRRlQ1YMwA94A_AVXSM4eVYCIUvYdZ2hsI_D1GaZUjNrTEyeX2LO8uz3pAwgwl8JBzjQbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=pFp0NCRlVZ3UVuWZ2EHe4x4fIISxD5uJPgUPAbXU08dkVb1rDiu7qIdREFlAVNscMzLlafd4pCamQhJjoz2giv3IMIe2XsghT0VA9ThgIWlIoVDwzwIm241lQPpnuSVq9tKs9UgusQPTcWYjgbG1hDHPgzkWgAx7oRWzVGAu7cbVGcEtbhLadfFqCfIn0g6ugG-yEuCf1hjv0qA3x-f5f3FMQcedZ9kb0yB9fxOL1mUUR4NZFuvarb3545b0o5wdWT2CG8mFDGSjE29iIRRlQ1YMwA94A_AVXSM4eVYCIUvYdZ2hsI_D1GaZUjNrTEyeX2LO8uz3pAwgwl8JBzjQbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=N-vUkgDh2Jp0wcl6NJjGaHW2gKfgdvW23aVaefMxgZ9bnuUB8ABVxBdcl6cg47BcV7bJwEz6f0L4MA2i0NXXv6vMY2a9xmEESF024tXufXfEl60lSp8h9-CCJoheos4oCHwdDeSO7t6ZXESbJgjCbaghnID7WHrb3GMm9ufJO_q5FSKMKgAVFTml_ZVTq-0pI2VPxF7RnmsectZpkIlIkOOQfrxclKG9NYsH4ggvxRw1FBToOQrrpif2OMToMKUQ4f4tID2hauCCvZWFO4-ApnhCHoc3VRa1mUkxwb9SrXPWbB9fhs0pxdrWBDiN6qTSt6nAoOnAORjVsXrbR4AzZV3Sz3zVJfdw2rXzHN8FZJAv52vafYDO03s_0XbuQf0WfuWr3mCZ7EVuInjlZpO9GHS5ua3Kvvzc432up8ngdagRSzjDgfwcCqy0-v7h7-7EL7QKm9lBn0LcMs2qEPNGkJm4GVQkgq9FHoitpwXwQRm1fX4J7eHzX0kfBkQtA40GZc-I0yXGAT4Z0DzLrscLOpyu0jSap38bjVWDmgrwkYR7vosW78NgijMtvP5Q23nXp7i3XUjUH7MqjXtFlph4bfrDBi8MSx8YZWBPHHZUN554i3oQEwKoo6pyW1FR9hQCgsasdD2tGSyVxom_fACloXl5nk3CZr4L8g0hQVRwIto" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=N-vUkgDh2Jp0wcl6NJjGaHW2gKfgdvW23aVaefMxgZ9bnuUB8ABVxBdcl6cg47BcV7bJwEz6f0L4MA2i0NXXv6vMY2a9xmEESF024tXufXfEl60lSp8h9-CCJoheos4oCHwdDeSO7t6ZXESbJgjCbaghnID7WHrb3GMm9ufJO_q5FSKMKgAVFTml_ZVTq-0pI2VPxF7RnmsectZpkIlIkOOQfrxclKG9NYsH4ggvxRw1FBToOQrrpif2OMToMKUQ4f4tID2hauCCvZWFO4-ApnhCHoc3VRa1mUkxwb9SrXPWbB9fhs0pxdrWBDiN6qTSt6nAoOnAORjVsXrbR4AzZV3Sz3zVJfdw2rXzHN8FZJAv52vafYDO03s_0XbuQf0WfuWr3mCZ7EVuInjlZpO9GHS5ua3Kvvzc432up8ngdagRSzjDgfwcCqy0-v7h7-7EL7QKm9lBn0LcMs2qEPNGkJm4GVQkgq9FHoitpwXwQRm1fX4J7eHzX0kfBkQtA40GZc-I0yXGAT4Z0DzLrscLOpyu0jSap38bjVWDmgrwkYR7vosW78NgijMtvP5Q23nXp7i3XUjUH7MqjXtFlph4bfrDBi8MSx8YZWBPHHZUN554i3oQEwKoo6pyW1FR9hQCgsasdD2tGSyVxom_fACloXl5nk3CZr4L8g0hQVRwIto" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=Hgj1l0kf9_nIrODyUOjl9fzpfFomdwikMJ0iB9nK7qJxbq7yRC90PLdsFWxyZoTERURqF92lphfwdHHncDOljEUw7lx-h43rPGiVxAPmY6Yw84gF8rkrbgbWussDUyBYG2Ud6kMUAC9TRJhP-O5tDvH6R1evcP1uYoc8TwD_Getdz7BB58K-QSItaOdy9V5Nda1bzIGCzbyZa5VJDZV49OGXCvSwqHZUWQlCAA4-KjKDeReUKQD570Z7FIkQOFWUlbRYSihLW7yqUpO3hYE0ohUAEEfFS1Eb0eSg0JQWP7b-XTon1Cd3II3w5MdecS57rgWKHTNHU7P1dt-SnbsG9ralL0SRv78tys5jFdAT0fccRc7g92pnjJm7qv6W0MixXDd5UHyZBsdgrqqm6M3yiaRqZVShz-M-d84OQ9DR-dYZ1kd3inlG9fp1PN3-PLeGe3RvlxmissB7vWArc8rni8QSnNortojYtEWPUvYfjpIm6BV6Rmtc0AQxnKHUhTkKtMJN5xkUMydmEQsjw3PMZ0FYiALiKk-OR2l28NAE6vnoCPQtz2Q-mLs5ulFdysZ5WaMVPQGhPDY23eJuaX5fnzQIMWszKT36n_GP-M0KB4OTioJp3ZEf4lfxnr4LT-lF3720nuxH60B6eVvQawudLg41DyQMi2DVgAtYuK2iGjM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=Hgj1l0kf9_nIrODyUOjl9fzpfFomdwikMJ0iB9nK7qJxbq7yRC90PLdsFWxyZoTERURqF92lphfwdHHncDOljEUw7lx-h43rPGiVxAPmY6Yw84gF8rkrbgbWussDUyBYG2Ud6kMUAC9TRJhP-O5tDvH6R1evcP1uYoc8TwD_Getdz7BB58K-QSItaOdy9V5Nda1bzIGCzbyZa5VJDZV49OGXCvSwqHZUWQlCAA4-KjKDeReUKQD570Z7FIkQOFWUlbRYSihLW7yqUpO3hYE0ohUAEEfFS1Eb0eSg0JQWP7b-XTon1Cd3II3w5MdecS57rgWKHTNHU7P1dt-SnbsG9ralL0SRv78tys5jFdAT0fccRc7g92pnjJm7qv6W0MixXDd5UHyZBsdgrqqm6M3yiaRqZVShz-M-d84OQ9DR-dYZ1kd3inlG9fp1PN3-PLeGe3RvlxmissB7vWArc8rni8QSnNortojYtEWPUvYfjpIm6BV6Rmtc0AQxnKHUhTkKtMJN5xkUMydmEQsjw3PMZ0FYiALiKk-OR2l28NAE6vnoCPQtz2Q-mLs5ulFdysZ5WaMVPQGhPDY23eJuaX5fnzQIMWszKT36n_GP-M0KB4OTioJp3ZEf4lfxnr4LT-lF3720nuxH60B6eVvQawudLg41DyQMi2DVgAtYuK2iGjM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=jV6al4t8PUhEz8Lpt5XR0l5Zh0h1jPqKpCwYM2LaDu0DDWEVXZB8GfkuH95KJLkr5_7-mr-ec1Co7uLLWhfaNh6RHeeKK2cR76ORRvaN57ZHDfyOafJLt3YpnK2uWrIai6HEK0JHDHkkPv7t8vlFEF1xx2SyUPr1CDs0WvB4ZTf6cNx5L01gBcrYaOSRdXzetrwxy8zbdiLzlDBLH6FBAPuoTnH9GQ-KpZz8OQGEPHEzvdoolEYGitPnDclNKZ9ZPIF11aoqM4kYlccA8rglfw29Lg7bINA6IuqXR-NsmZoVq6eVGX_451nKHSyPVtppLDQ2T37Vi5pqx-YxgEaBXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=jV6al4t8PUhEz8Lpt5XR0l5Zh0h1jPqKpCwYM2LaDu0DDWEVXZB8GfkuH95KJLkr5_7-mr-ec1Co7uLLWhfaNh6RHeeKK2cR76ORRvaN57ZHDfyOafJLt3YpnK2uWrIai6HEK0JHDHkkPv7t8vlFEF1xx2SyUPr1CDs0WvB4ZTf6cNx5L01gBcrYaOSRdXzetrwxy8zbdiLzlDBLH6FBAPuoTnH9GQ-KpZz8OQGEPHEzvdoolEYGitPnDclNKZ9ZPIF11aoqM4kYlccA8rglfw29Lg7bINA6IuqXR-NsmZoVq6eVGX_451nKHSyPVtppLDQ2T37Vi5pqx-YxgEaBXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfI8Ywr_D61dKQZJR3km8WOM1bL4Ek2E6SzKds85Vv-2_uzXBLLUnCcjuRQqgWzVz0KKbzfJfLfLyC22SYtYouM1tVsZP_XLlGIutdwnttCWsOUb1iTIDXjFTFJhr5P2cDHwwP58OoRqPjhR5E4L7K1Ejs37qDTzSOlhl3dNrmmqOb87F7m4RT7gem6nNS3mJfps4-KbQkEO-zamyKO4dguFuhuUbURGVYCV5lpbtZ-o0sARq2_oyuvznyCPzfbSPlyIA9ncJlnO6EtuUeXJ7fjDPybzlmE2nrmQGEoC-V9azGRUO3buMEQPcTWaQORFIkreA190g9SSfzuhPgcaJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=ME4AMN4LXAGo3omu-OYN4OTY7ezh-jnsHPpNXMVKWbHoY1259QIHAAPqhN5D7zVs9Fmsece6o5UUhu16GuAGB4HOxaCR6mBhw3qkOIh3WehHmAkskPSsvDJ5gPJkpeHaprp6hCPLMoq9KdhkGNUzM08_9BXSjIvY6mYcKD6HFf5m-FLOtSB33uvMzsRZuyr2nrMgfaKhOu2fzVXoUUg_h1ej0YDpcUtkdxbGYOJZ67jP67s24mnNlUD1GZtGOviSWZ4PfJVr3soAOdFOLV6yfHObnoaiy_y6rEjC9RE_yvSYFnHZHJwzwA-gyDgGcXqATG71yGtKJD_2wAUxjVVYJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=ME4AMN4LXAGo3omu-OYN4OTY7ezh-jnsHPpNXMVKWbHoY1259QIHAAPqhN5D7zVs9Fmsece6o5UUhu16GuAGB4HOxaCR6mBhw3qkOIh3WehHmAkskPSsvDJ5gPJkpeHaprp6hCPLMoq9KdhkGNUzM08_9BXSjIvY6mYcKD6HFf5m-FLOtSB33uvMzsRZuyr2nrMgfaKhOu2fzVXoUUg_h1ej0YDpcUtkdxbGYOJZ67jP67s24mnNlUD1GZtGOviSWZ4PfJVr3soAOdFOLV6yfHObnoaiy_y6rEjC9RE_yvSYFnHZHJwzwA-gyDgGcXqATG71yGtKJD_2wAUxjVVYJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=Z69azdcnhnEvP0f8tyQVihKyN0PFmG6kMv0YQyD8JRMdLmfrAj6oTeil1mhPZ0FTQgHS8PCYTZvei33ihRypAQz9wiXXa9Ify-4rYFQQBMNyPnL5CyHp3OPToXs2YhZPwB8KPeyDMi9cL3UmDOfEcBsJXbpwbwYUijQVBC25sX6O2E9ka_IYgl_3xeFufhej6VqZX09XZQl-O0bdsNV8WsMMtD6oDmGAmmsjFrsIK41t4fKEzKohcGDncWHEu2XcLYOnNsHgjUi_43QpQls3GRb3d_wFzuYePRFl09J37EeAjG-VgSQiybDnMJSknRe_OIpu46rSoSGIw-QW71ppcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=Z69azdcnhnEvP0f8tyQVihKyN0PFmG6kMv0YQyD8JRMdLmfrAj6oTeil1mhPZ0FTQgHS8PCYTZvei33ihRypAQz9wiXXa9Ify-4rYFQQBMNyPnL5CyHp3OPToXs2YhZPwB8KPeyDMi9cL3UmDOfEcBsJXbpwbwYUijQVBC25sX6O2E9ka_IYgl_3xeFufhej6VqZX09XZQl-O0bdsNV8WsMMtD6oDmGAmmsjFrsIK41t4fKEzKohcGDncWHEu2XcLYOnNsHgjUi_43QpQls3GRb3d_wFzuYePRFl09J37EeAjG-VgSQiybDnMJSknRe_OIpu46rSoSGIw-QW71ppcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIQRVxRSUQ5ySONCbpxDHxdKMCwcvH7dqtriOVh3ehNkdmbNCWLdn-Wf03aIDUT8cB4_5bQMo3byUjUpXd-ixk1Lrv4ICFu4m0jkgbsbOoReTRZDsqMuqbWeGkE4NM_5qodqvzClcf4RZ-1c_ISTs72kwqvpLrDsLnk_6BENXOHMOIaxFIQGDFQMeUigph_iOEdqNDdN4fayi7NxwjzZPycaB8OEhc1xOiXF4hKqI_wkbmili-z53JH7bv05KI2GGou56uqUms3mesadFl9DCRduA3AH789f36oP7Toh6nwnS0YgMM9LB5AJ0evFxBjBrR1wcsJ6Uh68Jv2d_1iPIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHqjwcBum2U5tXc1sCxQArCPGYn1B3TQSfD_qWM7G3U4CMrsth29mt0PXSb2U57kzNKKlFrovHs2mzoRHvNArO_ilKlBdT3jq5lC7TtGXyXD6XC8w8UBAT707-6qzHuW-4P-9SqAl21OpQwsSlm2g04K4B5Amumj9V1xZfx4nEAnWTqVCMbtO9XrP71q0kpsEpLqg4v8BrAtif7nk5mw6X22SvVRaI82LXq9zHlQGulQIkDeVHrHCRyGPUao8Qu3xwW_MKVcAUdOJ0var0yHaMJYHTacwMa8EOQe8hP21leGu0Pf4in-WNgAtyriEdB0QzHpsFe5CHCqUOyTgpIHwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLXM5y1cWP9rUhHynYyCXoKc3zZZ26TcMQPVw1gI4X2u8O3Ty4Z4MMkPSbsUblv1iir7a6vn8LjkbAsjOBHjLK5r3gfmgsq_YhaHK6GpBrV_GgrRqRZf04y64F6UyYzu5D4dLamuU90xNd8-XL86v8nUtYIpXjXhCMrvjhyO261QMPL6zb11iyFwr6dZ6Yoy_o0xlCxjocuy0LkXcMDZLELnqaYFk5FI6bd29K6eEGYww_b5qkjXhmMl1IAwtrDc3Yr-GFz5JfyDcXsstNNgJuXZ2S-9JbD0zsRht_YxhK77aiUqdC_LAjQoKshuI4XI574RZmwjbkFd0OvQielkeg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QD_rmymAo_zcfAQeBXURmCRkUEkUcIe5OCSPDNOgnERk-UeN0kmruq3GoBx-_-SN12qCAdqpJKeln6cPfsAw_Vaya5JIH4wQlRZJVqB7fYBgrj4cdZGVH_Nc5SofozJ64e3g4n4FdAzyj-9QPw_uMetYbxd5Yh7bXLs3DfZqreyxPOkeU_KTZ7yF4ksIoPn0fEki-kIwv0DUB-884rZnFReAe6bW7LbQYkSD5tWmAlE7nmoatOt6MUekFqruvtiJ9hETmkhE4apUFFifYahaT8w74eX39uKQoxNf9xRJne7_uOejcZO4_-AMGn2dsvkqEmkQyTucz0711RlEPkHbug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNImv6yYIODwJMr38aPxBVdS9iUkD2nO7vjsyAwrJuBi3WrqMXlVAtEGkx0AW_6ylqlfmWkxO8iHbgCw9vuucn6L808GRAf7LTZRZ71sKEDmx2z990XLLXkL7Mf3MLWz9stRh_M79_JLiGubimcqOKnsnOY5EUxoKuzhvPfSvdW3gEPx5nW48JDedRRty6mxxbApur4wLdX9uSoel8-Wb0lHIYyJmEL2ZobHE0kWg6XRXN0xYttWjJpkFi4z9l_--3zl58hb6qDokQVqEC6FIYUA85UgvDRxzKeUarNb8Olx_XbHFuHFESDY0tRiRvzYinIfzL4VqHpTmMq7F5vfLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MInm77AJCcPF-Y5XshkTF45QqJ30advwq94xBARSDyw04Jqgzvi4PMzsAIhZjlU2m73GfuyyKBjqcXk0faG3xZhLezYF9OJftD4uEmLTWuM7ZrxRTLenxPhoOVcajy8dhCLsKrzxLTIilLdgzRNphbZ9OzP3h4584DNnfWcDmdzyhEEGOi4rcf_3vtH4eA-n8HWDJ0Pl4g4sDDnSlPRQtwekm_SuPLi1GEDpw6-BSc-WQfK6cKIXIdlKBdEi7cTLazIAEhg75eP4eYRXHZLb0swIr9X-S4G7PyNWe1De_IN7eY-V7WQWO9PuCqTDrB-urWZG_1NMczMnqDkoNVQAaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TifvyDUDTjV-NgJf4pnYsEi0KS2xU1h6ImCRUuu4UsYjjV2bonI51RAtfZH5qlXWXExKNAMqMi51UHPKhWaPMqFwdeKdoAbzmLbM4wJSNEDpHoEBksC-5j_oxZxz-N0mPjaF4uAwg-fhRVwmX99Tfsh1dMLEFetvfgF9dcJd01rkN5VvJrA7n9ftumdidO6r5guWUpg-JABvgApndHVkkq3sDLbeI3XlLXeBfZy5QaIg-r8j2Ys7W4oCPlqXXMd1WcOfFzytZ0T1m5Xfi37iydXT0L-ym6_dN0q9PJfR72XFC6BoPqzI_3aP2Hj1XTNFn3oMqqkguF6zbEvScSbK5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DQy5SnXLEYdA6HcP7RKFbeglDfY99WDsI_tSoQ3Z_poa9uyNIsQnQfaxK_3JzHycq0gnU8CXzRoPU1UpI24zZI91hsLnE4GZS-Sm2lXPA1_Qj7VyoBgJe3NQIbx54Tl_3hljHITKC7FNh5lCzhtulTRlDe2bZn-oiFe49uV9ri5M8HqFsub3qyTJcmqv0KGU2OJtd-YuyLz2lBe7-ZuEdwlSFZ5uGuPAnaLeqHWyw8pynRieFOIhLM5UsDWYty62NkkLyFlcbg4CAjcZWAMPzbveLzxgDJ7I2iB7znWBXY-M9kUvvU6aGs1Za0BmaLg3ADMLhU2HakwZ7lwj5skXZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tIE99YfxxzSKdbJer2c_XYwWCw37qGlpJDgYqE7vfHEyYAUW3ioEzZug2mIcgQsWE3LMddbivijUKXKZAkAGHIrzzCwJqFWfN2HwlOOKPYHKFs6HAR6O2tHJlPorYq2xLPg2Av0oH3TQhKMPaRYu5gtUKAZFk-i6MFj5-e3nEdwn_gYlNB50-8p0iYfXVu6M2xiDsSn_at5yJAqeQnlmC-FgoeMP-5jMaObxiyP4O93P9uhrW_IlBKaP0T1zhKrcTtf5CkyE_Yel2u4B41DjqFCDroxVsnI0Qi2jxLLm4mVvFcEYVdzOhgnxELhdqyU5_Y5myW0bDAqWWF7Joe20Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lIGSKu8zR-DMKk6qCPDiMFi32yQ0MFFN4qCK8mT77Do9GOd8TsaTzc9p3wNVicYcSwP5OaBno9_OgPY1qan9FHtTyRXb2kkn7-ptXZEyvBXlfr-0EQISH9tJZ6TAsyvA82lmbzf-840fy0j0FkTFIw_LPiXBZQQJKVlDSvDMNKc9azLG8Z6Gf8kbVKi3FRv-UKpQ-ruAYo9PLDujiDUiEQcqZeK51CatqUIsUBRGdY8GXpqq65hKpf6b68fvzmKU0tBT0h0k1rs59vtVP0C8p2UHW8Lgpj0MSekg-aDKuyEPKUBMcKMWZxUrcucbUOm3UlGu_2H26cRQQnc7Vi51aQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=T83NJRXW5JnidHwt871mFL2TKcTzgBRuzMklHQh3DlvOlZBidQX7kPWVwhJJV_Zmo9FkAxgkrNK__AOgGPUzgvtNVdYI74YNBpRJwXKaj9w-oqt8DIhsEC97oEubu2218mCWMfFHZ4bvqSoD-ai7Z69BurOVQh3-P0S5GPiyKrApwMhX__HKuleoZAlCbG4RPZG3IUT-cg796mHZMJQjwM14XuIXUDu50tW88BOZMgDzHaARe2Lm6rxqkRP3yHC8jIzEfyuOK_I6hoGhb4-kNb5rn0L_PLlHH52Wmqj9czZjdVEGcUd7CGkmIwKaWhaqa012HBaNI8skm8IuI1MM2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=T83NJRXW5JnidHwt871mFL2TKcTzgBRuzMklHQh3DlvOlZBidQX7kPWVwhJJV_Zmo9FkAxgkrNK__AOgGPUzgvtNVdYI74YNBpRJwXKaj9w-oqt8DIhsEC97oEubu2218mCWMfFHZ4bvqSoD-ai7Z69BurOVQh3-P0S5GPiyKrApwMhX__HKuleoZAlCbG4RPZG3IUT-cg796mHZMJQjwM14XuIXUDu50tW88BOZMgDzHaARe2Lm6rxqkRP3yHC8jIzEfyuOK_I6hoGhb4-kNb5rn0L_PLlHH52Wmqj9czZjdVEGcUd7CGkmIwKaWhaqa012HBaNI8skm8IuI1MM2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6GrSyf6OCT4k9-uNFhtH4hd4LS2fLpJA2b21hhnaWR5Ey266U6o5KdjZpxWzGXQUHsQ44QaLzkcoHMoqskDdKVGsDgdaO1RQMQ_YyEl3SIZTOEXVmlAT7OoMq-EMlgDjYIDaBswDxQF45dKG8BBh6kWPwm8YgqAzv_TQtjn-xVmF-hRSQtuwbZeDDCDOoiZDV7yK_5y2W5sbJmZkd1WYiOQpQ8n6aUxqZq6ckPWsN-djvquPnAmDhSTfI1eNBDKR-B3YS7AZG5MHeIrhkjnHUqQchr8o-D6PVq1YZanmRzSusaniZ_b1_XaQjVPJ5FPVxmk29m82mvvmE5_qwpdIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqHqdU1luFJudD2lLW4Ajd2dY-HhzEwXykKjM6RchB53h39ocnzTQSdp4GtvGMiC-lKd8iPoxtck28Jnrgc6466X6ecWrOYX6nuC7uiZ3rhxMIiK4ByYb6CpPeF9ZcjV1ow7bPVw5b5PadYs1X6KvEnR2_5Efob1h25C9PQlOw4KcQPJMAGjklI0YV8WYWd5X5hpzbE-B0ihmwPTtb6jQeG77srjKWBcgPV4nwkxotbOjq3HEzgr2u5V2Ct6NNBWHay0XzskrViEBXuYxfg-PnZWuNzFVzZe_k7iMmMAI9bxg_6CG0Gha7gJMpZzzeubpKsVkoLa4U7wFl2xPNX3Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=lDPqf7qRE-xttE7x5bDhTAtUE7Sj72Qk1XVafF3jU3LRrFeR9ZUI9XLGuWYRVsSSZiT8UHJ7pRoe17w9He8R3b0rtix4LBT0oVXnAdn9AS-17Ok8J0sTfGghFzsCsc3QYjXzYkOVYOB41dN9NJrlDjvyTh24OPKKFM5b_w8-aTuynhqtmDp7GvqZ0_2B1zyNxl32vH3Ehz24KP2pjkCNxZlSrayRSw4K1vJry1tbxFf7dMt-RQEuhDI4Dgsak-F_wlXVXMY34n_MB9S9WeeNkgKuz1EcK6sbsyigi9g8Wxav4tSD-6m944TReP_a3C8slPPRWwGdaoiqmKjYfV3q_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=lDPqf7qRE-xttE7x5bDhTAtUE7Sj72Qk1XVafF3jU3LRrFeR9ZUI9XLGuWYRVsSSZiT8UHJ7pRoe17w9He8R3b0rtix4LBT0oVXnAdn9AS-17Ok8J0sTfGghFzsCsc3QYjXzYkOVYOB41dN9NJrlDjvyTh24OPKKFM5b_w8-aTuynhqtmDp7GvqZ0_2B1zyNxl32vH3Ehz24KP2pjkCNxZlSrayRSw4K1vJry1tbxFf7dMt-RQEuhDI4Dgsak-F_wlXVXMY34n_MB9S9WeeNkgKuz1EcK6sbsyigi9g8Wxav4tSD-6m944TReP_a3C8slPPRWwGdaoiqmKjYfV3q_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=dr18voLT8673rZr7gBtMXMifKz0QNGX0hHmELB6dXnjpLRmT0TyLcdCR1oFLTAF1cBDYb6h64vG4AMvJtaLqV6Y7lp-MCaJb10Y4OqAdSZ1bJblnZlJECAx_HcMrO5l0IGEioMCm6DUQ6gn6uwNdHdQi8OZ0W-iVDwvH4RzYsg8gn3c7NEGeYf2DaER41E8SSkzJ6UV0PjLmFgZlkZLLr-vJbR2l1cG5B8cE6nQFvdRC2YJrSNvOdZ3C7ndKyQOGKSG8Ww5NJSnC21XcrrzgqYRv0qeEJRpVbxNllmYbRQzzmEUy42lPrp59kiaOHbV6z3ewz17wvJeyn3NyCUzZ7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=dr18voLT8673rZr7gBtMXMifKz0QNGX0hHmELB6dXnjpLRmT0TyLcdCR1oFLTAF1cBDYb6h64vG4AMvJtaLqV6Y7lp-MCaJb10Y4OqAdSZ1bJblnZlJECAx_HcMrO5l0IGEioMCm6DUQ6gn6uwNdHdQi8OZ0W-iVDwvH4RzYsg8gn3c7NEGeYf2DaER41E8SSkzJ6UV0PjLmFgZlkZLLr-vJbR2l1cG5B8cE6nQFvdRC2YJrSNvOdZ3C7ndKyQOGKSG8Ww5NJSnC21XcrrzgqYRv0qeEJRpVbxNllmYbRQzzmEUy42lPrp59kiaOHbV6z3ewz17wvJeyn3NyCUzZ7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5e8CCfnOjgxhIC_wYLYyy7uZL_OCCyawZnE-shrvbV0gfRTDzrTeO5SmkKFtwuXqANmDRFYuSObzWuPUO7p8ADK3J1IKh8PJgCXLTfauyPZQfUgp22rWW84N1C2Kk1w4aBBHgvVQGPZ8aHdGT6t4OikNpY25Do4sSxxH5CmzwnMWWftipcGT5AsOsd2dzwlzOCPUfoqMaTJ-DGtC8TwpQ1OiksCv1pEJzI1E0HNjUykh7AILZZnqdK8F0pNydA-UbhYLwjyPNuMvhbJuVwpM4Mjw5fe3ZUs3Ism14mYmI2k1zRVtJa6D8UL4w5WzxvUJrx9h63RB1DJ6owN2K7mcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_cWeqfMj13mVz3lmUjswAooAICROlCe8XlU9yPJ6OBR0rrmzgq1j6VcxB5ULiPiwcaz9AHF5RETtApbWAZqE4v0-eSLi1hX7148tLMn_KxQyprXZGBaJ8u2U98jIY9BZqUD5AHzrpZCKL5l7hhk4_OpziYf2Te9Q6tHjjcdm2AH-64gF0i0nyCLOuwELEvju84pwr35tF-W8S7k02JI8LrzE83RDpRX7KfzGPmEztnYw5JMD6FfJawMr2ouYbU_EeHuVdgtSkaLJMtEUhVRTfyAeYFWbTUHShnp-Ko3X0JchdaZezdhiYapwG7qMjbNYUfEFRUrwsdGdqMyBLCc6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJymelPmff8-yemtMRLbX5iFhwva64CQaekxyiUPOYPRN22IfFk7XYzL5_m3D-Mn78RmN0xtBiDXAFB9Y5FPtFOkFbM8rcy2Zb8qIY-fnupLndHkpEqy7QZhCRRWZ4Qkzg88Nsi7LkBz08VXhpSkQZqQTEbIPWcZIHhl7fX_La6-LX0GoQvxi3lJ5EyIOlYt6TbDhYB-kEjle8b3K_kBW0ZzNlfqTQzVdiwyq8mTU927wS6LHoITzYGXpUT0M2AItZzAjTLE0cHJJ1Ie_uYqsyrjk3lhkm5nFSLrOBV5Y10uXe-bmvaL74dsE5wAaABuzh8RsFjfkKA8nkE5mAbv1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDKoMIV43p7U1mHrf1rOC1YejiTIccmVCPGvxFk3aRDCDEmW2ZYFX4SZGA099wBoWPTUyHR6O9nBIAYr0hIYXN5MDWWrRCpD90y7huRIijs49FebhDq0VtvABOgmJSpmLXRu07azTJ9cJ3Cx1O7ECO_mWve4P7Nq2h0tWgb7EsyLS3O-Ao6fjJ3NhLe4xcMjrTn-TI8j7wkfjInnP78SSg-YkRJvp1fEjGcI-iuewhxwvpqdQ7b17urSlmfnPLiQE30q4VsHRuX1MrlMDTFMC_rR_j5BBpzn6gnuh9WcgTUXwByZx4B2d6uqMhRuGoHMZa-_fixKhXiKRrEZDaWIIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TeV12g8pLyHUcvgqZL218-IQFyk2pS2tPXQMs1xmiuM1dC5kEe4S560Br1hQFneGl7tBUMu4Ro6CZ39YYZYqkO2M6nzL3nV-tw5KwSfcldpmP3YCBks9HINUoHTN-eV0ngC3JzaMkJbjPbFg6Ze3L2vgpAZXcYG94CdDBELsb8pqgY_Wg34IH_uElSDHCx00JC5qfwJsxdPTOL8Z-GF-g2DMV5g9iszdSJNElbJASMIAPp6lP_Sh6laZsmyKyyF5smPAeQP6X6ksS6j11XT4vY4pXSAQBw9u0SOTsWz_hBHiqJdZEOCmJiL1s9f-rcjvgcyrtohh273G2tdHrTVASA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alvxKWiMJqEu9kobNBZOud59BKS8dWOng1tlwoXwqe8YDWVub4ho1DqCPncDZQu4RiOGAEgqZwR2RLBDhuAzC4UqhTrODup3zvAMCz2hYL8p4cbijUc0GCpF-kH5ydhinPw3DEIULEPjrphgk50WdfowM_4UZWldun4uQXFGWJ-aqdyvJyRAxL3S7vDZpHGGmV0UGedmKSrzNDn_Yw0bW_D0F35TZAsisJsWFxS3PaC6v8bMeOy0um0DB6yq9QBETbI1Lgz6swHpW0i156iCufkIdPdT8XPhECLmqODDgky8m7JQAfSktpMIl0QFiA67SVt3McAmHjir4zKmudCPLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3vaKGPq-zu4GR2zYViz2GTxTdvZa53gRbQQPHbPY6pKv6Pwgnl-Aaz36bl4oLSqSqjkS6nPYOZ-33GPY_YgOfoNm-UJNuPlLCfXr-hRaIna93EUW8VXlj0-SnO4tvdn8dkXiaW2agQGnG2ngPLqlTBqZJZTCgw4KkHp35-SmzA5lvg1gArg7yJH-Q2aHXQJ3P5g5RhSBWj8vZPm4YMBblOoyEZe4_2-7Rj157KHKRMjol0uthEptroGd7ezkYHpOoB0dqZ8dktv0GusTkyCLnzf8ys5aqF95HQbbjmhQ4vmBdkp6RMgmMa671DfNzFZ8M1Nlxd62_O_uQDiHEgZpQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=RRlKHtLjq3nF1e3jEo3cjYb1gIDGyjod0nC2WnRG0uFUWwSXwV426JVRHjcvFKXhjRl8TfaeJ4HvegdEC0dz3e5QQlracEK0PK33Mne7A1Ytw_VsgKpG18qPGnxnH3LnTZz_YGx6Jr3kUxThSgqVm-Tk1ZMh0L-QfZtp5hXlm3CLtlM6G_jow3sx6JlHI9uaK9KdcN-ZNUxs9JHt45SCniFfGRvB0eY-vyYGhiE9X0bErXoDbmwnC1cXFuJnC7Y-rWfd8u8cOm0r5bZqmLWt-w93oeD8pV1ojrOjFgC4jj0OEPltGKhOXJjjuiLUI6beV1B92GOczrrjHY0Xh3U0_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=RRlKHtLjq3nF1e3jEo3cjYb1gIDGyjod0nC2WnRG0uFUWwSXwV426JVRHjcvFKXhjRl8TfaeJ4HvegdEC0dz3e5QQlracEK0PK33Mne7A1Ytw_VsgKpG18qPGnxnH3LnTZz_YGx6Jr3kUxThSgqVm-Tk1ZMh0L-QfZtp5hXlm3CLtlM6G_jow3sx6JlHI9uaK9KdcN-ZNUxs9JHt45SCniFfGRvB0eY-vyYGhiE9X0bErXoDbmwnC1cXFuJnC7Y-rWfd8u8cOm0r5bZqmLWt-w93oeD8pV1ojrOjFgC4jj0OEPltGKhOXJjjuiLUI6beV1B92GOczrrjHY0Xh3U0_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUtAd_Gw7EKcf1PiQdWltkpRmPB4UZyYgjMQ4AfbHNQle-PmhJTvk3wKZLi0cV0nBbWwU6Z3p5rJJqulC3PQd9Aj2BIBzWv5_sEhhZUH1vjGkqa306nEhjHUw8VNiI6fmzjDGvBbrm7gZvzaowk5kMfLn3SVO2Ja3CUM57BCmDbFFrQPep_lMzBFJqlziTo0B3XWbjuOsqF8zPOCh_NbP1QndPLuGw83zB3N_JecyX0MfWBOQh0oV60ncCUX4RhD-udDvGaVone4W8KW1bgnUykkUc0Nkapcfel6DMirqtiA2Owun3lNKFf2jSiNhKu4EZtHlfDPInkTMIj2YAhJ9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=bt3mj4jdVKO-useawuPjwMo3tVyDdW6k0Tty2UW9vEntp7sHK-vrFredFbTZc10gPj7Ipt-69EBOtxuw_LTq9aZNU8UI7_kvGbOjqWsXI4oYnfaqGpySq4EJDLNb4Zi8l6RuiiiHsHCsGmJ2p_BGX9851_7F9pt5VvcJ9J9KrS32-GOMOslRlnCgsohXbvq2ydthnRs7oEvPTNe5UoCGUCKIfe50FLQMeS3_Vl1WSjnqQ-iCvOKvys46JlNU7pJnG7pfeTXdcbcphp7e4JxM-sQ6WADfx--aJjFrRMkauF2YlHyUd3eMYxu4grngagv16iRlAM-lIDWYPlFr-wZ6WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=bt3mj4jdVKO-useawuPjwMo3tVyDdW6k0Tty2UW9vEntp7sHK-vrFredFbTZc10gPj7Ipt-69EBOtxuw_LTq9aZNU8UI7_kvGbOjqWsXI4oYnfaqGpySq4EJDLNb4Zi8l6RuiiiHsHCsGmJ2p_BGX9851_7F9pt5VvcJ9J9KrS32-GOMOslRlnCgsohXbvq2ydthnRs7oEvPTNe5UoCGUCKIfe50FLQMeS3_Vl1WSjnqQ-iCvOKvys46JlNU7pJnG7pfeTXdcbcphp7e4JxM-sQ6WADfx--aJjFrRMkauF2YlHyUd3eMYxu4grngagv16iRlAM-lIDWYPlFr-wZ6WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=EkSly9P6UzL-NpjDG5bDk1q7hlit0b5Ewlp1msGUcC_knUFn2BnfJKrWWqC-w137-wRTAr4ZfdhWvWhSLnkKFw66WFpnSyv-sA-Ym1blkMs4wL2hoVnUUL-LUAOi877XI5INyDXSfbTtQh9fL7jWO1ryOxF0IGmkfFP2W_JkA7jdawgEhUt86rEXksuhA7zm4FpDmkbKFm9ji-49U8q05WwXCiHPbBsYnhMaY0Wmv5XiVHHn8FTpwLDJGdDt6jbPX0XnwMh-OATpOtsR67eLs1Fb2VUwgu7qg3H1b38GUYHnBnTcgvbYSOnDxxxip4Bi3yWvXv8KyOnxPBKOMfwe9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=EkSly9P6UzL-NpjDG5bDk1q7hlit0b5Ewlp1msGUcC_knUFn2BnfJKrWWqC-w137-wRTAr4ZfdhWvWhSLnkKFw66WFpnSyv-sA-Ym1blkMs4wL2hoVnUUL-LUAOi877XI5INyDXSfbTtQh9fL7jWO1ryOxF0IGmkfFP2W_JkA7jdawgEhUt86rEXksuhA7zm4FpDmkbKFm9ji-49U8q05WwXCiHPbBsYnhMaY0Wmv5XiVHHn8FTpwLDJGdDt6jbPX0XnwMh-OATpOtsR67eLs1Fb2VUwgu7qg3H1b38GUYHnBnTcgvbYSOnDxxxip4Bi3yWvXv8KyOnxPBKOMfwe9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDDjYToh3k1zEKFf-K9wIQzfU9CIS7qgrBRnyLj7vRwrm39dE3m6wsbhesgDishIJ5NEB7aXNrGYzk__yskjQ1aY6NBjLuK0wMeC5EAgOt97kmfuY39VfRsFfKpOYtPyqowE0a24tp5-OGEDo07wkehJTxUDsmeeOXqGE2rezdVAL02L7W73txt-E-zG8i2t5E0K7hFHhLlvK01DfvBR5zn4YKGbrVg7KKPgZT2lRvdM2mX-DYgNwMSu8LC3CdJpwyRm9kkkJM7V8FLPaQAU8XQxcAuQdzJtyUAI2xgolTEaRTv1T1ObR5jOOCRi_km4etlSxWbnpmBaiHq6i9P--g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKL1UoMSslqO2P5MEYNef-tXGl2-gYEQGlU30uxXethS_Bzramc2Gl_qZkENwuWOU9h6IZdhiVxmGGQALLNl97hxQzG9WKBncZzHiMfGaNVV-NlCzIufnYzeNYRMCU-qqG3M3VRNOJcwJ3kudMJqogUh5-_zqr-2r4aIZnOtXmmk8OJnuA_S2VbSrVMIpacGa_-mQJzs5NcArhR-UwRjg8_lY2wIC7Sbcoa25WT_CXJFsM6ODtV5CNpTxNfgO585v7fByHjRcm1J-dw7ZqSjL07NpttCS-Ie5hY5HBPRZFtGnrZGLvs-uRFHNxsr5-b6swgJ4V9a5RUMg87_2ycfgg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=pNOKjaCsF7f-GoK6AJdwkt66gJm5yscCwqBC3KDnBwHW-A6KpOOwCSrmvMziQMctODnXKOGZ6ANftOVNLh1ta_hLpXCw5wAqQlngzh1fHf_fkp5OxXobxpLApfNwfrm4hw7H7THGOUZfhXjNZ3m_9zoHmgAdH4Jl06KTG8jJEeGl8hH15c7Pp0jsQYHFcSo3Mn1LahUUJKbecdvdJ037rTJrVfHZvPmZF6JbobdaHWL_ksIPSvXnHFNt7RRKzAo5rZc_WNITk-UV0IFLkg34IllAyWJa6SIMMpSDgDesynP93kZ_tIcvDIXv3r8z8ZKP1iWGHdIhTQqkHIeaJIsFT1ViBpzqGD6ZctJnTRaAtM9u1MxFQ5HNc_JWg0TR28sRpyl_6ko6SNgcUOp69aGJzVmsPkTFCyYLgkoIJfKD8R88AuFeSwgGk7zBs-ZSYJqqQgMKnUHNPbGDVkGVjaVU-g7EV4oqcKVDOxAmWXKpne4ML6Z663Er5S3-EkTdwS7BdDwWXtX2cXYUom8dcCMHulEzj7lMubNT7C0PKYhUtG7-HvnBTiOsWsnEX0azoD8tnTpR3d-S4_pJM8gv3UV2O2XnLajHkhLIEkBa4LOeo001ob_hV07bqibQarAA7Sugs7UsaCzP1yoLISRn_6tL7YaM0FUN24N_jZ4LtMLmLcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=pNOKjaCsF7f-GoK6AJdwkt66gJm5yscCwqBC3KDnBwHW-A6KpOOwCSrmvMziQMctODnXKOGZ6ANftOVNLh1ta_hLpXCw5wAqQlngzh1fHf_fkp5OxXobxpLApfNwfrm4hw7H7THGOUZfhXjNZ3m_9zoHmgAdH4Jl06KTG8jJEeGl8hH15c7Pp0jsQYHFcSo3Mn1LahUUJKbecdvdJ037rTJrVfHZvPmZF6JbobdaHWL_ksIPSvXnHFNt7RRKzAo5rZc_WNITk-UV0IFLkg34IllAyWJa6SIMMpSDgDesynP93kZ_tIcvDIXv3r8z8ZKP1iWGHdIhTQqkHIeaJIsFT1ViBpzqGD6ZctJnTRaAtM9u1MxFQ5HNc_JWg0TR28sRpyl_6ko6SNgcUOp69aGJzVmsPkTFCyYLgkoIJfKD8R88AuFeSwgGk7zBs-ZSYJqqQgMKnUHNPbGDVkGVjaVU-g7EV4oqcKVDOxAmWXKpne4ML6Z663Er5S3-EkTdwS7BdDwWXtX2cXYUom8dcCMHulEzj7lMubNT7C0PKYhUtG7-HvnBTiOsWsnEX0azoD8tnTpR3d-S4_pJM8gv3UV2O2XnLajHkhLIEkBa4LOeo001ob_hV07bqibQarAA7Sugs7UsaCzP1yoLISRn_6tL7YaM0FUN24N_jZ4LtMLmLcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ia23bB6qDsWVDpSaDXle-W73cLV1Hjc_p17FFuGfgfcl-QaA-2cOfwCMzy7UA4gIlgtCekP6Zrd7fUjOMih0FGXOgV8q1PUg8RwTA9-vglgAt5-chOMjTdASPRfR2UU3iFo1DfQAkiAi2EBxnhuWDLw8UD7uYMm6rSiekdJ1HMCvNRqCoJ5m1Kpj-7X7e2lLuns4grESuKQDBvA6u3gC8Dy--PmC5QX6d32Yq9hHuVdDLgBD2jtqtJGwYyCeeGZjoGKnB60ud8SypU91lXTSGvv1Ww5ruAm2vWN_-Zz9r60hhyt2Uk-8rnpkgK8mvY9s7UCbfyW52BnD2XKSpTJttQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=nCDYiRuG1AJ9BYghlSkClxFQeBRJ8JoNaOLat23f0_rdbBFIFad442gFqq2NNUdxXGnyjVq0UUb2rvrLjO8GLdkhhM6y1iWH607XhWfW5nFFVXTZvna-RvIsKLETfLLFY7-ya1orIFzxCH1ZaQyK-RkFnBTWfNo-DaBKSHAIWJE1ZnAm2ZVpkKbdlZmRa_BEOu5LmIil3kA6JDW6g7nNUFQ5jB4l1ZbWR0P37YWxpx7Ml75jrPhH3cxFXERAEXuJOMXunw0H6gIyejRmfo_5LnL-TOX4vL6hM-MvO1qZ7-ODTw_TedIxcXglHvXLHpEPhOBKAjma7GdkylUJAMfYXyNjhu8vXD7qZGxzUkhJ7bgR7ufaO110gZXbfWKGMeSlP0UDA2ykprXlqIWRS33WMc_RPoDFEfs7pJhcmjz1e3E6Mo1qZKxajAAHanvFEuESFdoZ1aq7rN0ZaWwIE30Ki9vH9lX46g6H1WJHlY6_Zl3eRCRPe9_vcq_L8WSoKSpDAPq3eBlxoLv6aJpyYhNbJjBbv0JAewwDHzrFvwiE8AV3NJlw39vCVDVwXvcogG0j2PYWf_wifIinDimCg_jNGbQdBTgrq11hhZdzWkHYp3_7uyaWcLmDQb3x7Sf9WMSDUejaTC_klGiJlzkN3YT8bZ5k4BNha6GxSg2_2axPmII" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=nCDYiRuG1AJ9BYghlSkClxFQeBRJ8JoNaOLat23f0_rdbBFIFad442gFqq2NNUdxXGnyjVq0UUb2rvrLjO8GLdkhhM6y1iWH607XhWfW5nFFVXTZvna-RvIsKLETfLLFY7-ya1orIFzxCH1ZaQyK-RkFnBTWfNo-DaBKSHAIWJE1ZnAm2ZVpkKbdlZmRa_BEOu5LmIil3kA6JDW6g7nNUFQ5jB4l1ZbWR0P37YWxpx7Ml75jrPhH3cxFXERAEXuJOMXunw0H6gIyejRmfo_5LnL-TOX4vL6hM-MvO1qZ7-ODTw_TedIxcXglHvXLHpEPhOBKAjma7GdkylUJAMfYXyNjhu8vXD7qZGxzUkhJ7bgR7ufaO110gZXbfWKGMeSlP0UDA2ykprXlqIWRS33WMc_RPoDFEfs7pJhcmjz1e3E6Mo1qZKxajAAHanvFEuESFdoZ1aq7rN0ZaWwIE30Ki9vH9lX46g6H1WJHlY6_Zl3eRCRPe9_vcq_L8WSoKSpDAPq3eBlxoLv6aJpyYhNbJjBbv0JAewwDHzrFvwiE8AV3NJlw39vCVDVwXvcogG0j2PYWf_wifIinDimCg_jNGbQdBTgrq11hhZdzWkHYp3_7uyaWcLmDQb3x7Sf9WMSDUejaTC_klGiJlzkN3YT8bZ5k4BNha6GxSg2_2axPmII" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0j-F7TVpkOX7d72W-cIEX1D0a3wV8MYAPAxz0jzcuqbKNE4gLlHnRr4Cs_CXwiDuPD7Lm4Oo03RwTOL7vlinC22TVPCKnLRQVjc3PbQwq6gwWT73mLOSjvhHuv8-IBR-vNsPXXoAzqQxk2gasTrmkd-r2z9SbYIMhwv8_RxoP606ABEtZKTwwLb-TkuUeOl5rshodW1VKVKpiriqEUGPpmcbTC84q4Dvj7Ji33n1UuJqxxCNKq6i_xIVniY-rKbOVCFewfoT4xDut9BFEYyAS8sLpdzE1YJcYt3nVigGRuC1JPDJ1BcpcFob2mEMK1PnLKCBBNExJP_Qxo97mxF6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPD8lKeOQCzLLIR-zcp4O05O4cU9IX-BG2M_ZMjxeiuy6pDHmVydnw_w2cMkOOQTEAFMxnGlAbEVURt8tBp5_kCnQ6YfQKnxbVj3SzQ2CwZRw5UPtss-YLGk-Kjm5nYQHQ4gUOGIg2T2A5-fMmCzKWVUl75QW65sb37q8cIrUgqalXGkJm1wtPNmt97iKDEdIsuBj0UEZ6057xeKzHc8gMTV_Lcfv-FyjZmfIhWy1IhZP74bZFPSV6jMibfUml5o4jcga9D8KcowuXvQCPEybJuk2odCGExZMQsKSGnpRUIQPoXPPjgXYZDapBa075dvQN9zVVynihkzrPefctHlyg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKP7lQDVp3506rT-VBpBTo8hEl4hQOWTJoJ_iPRxtLuT_vpJTkSmgb3AnKBAG3XNuYjc1S44EpXVvFJrg4GHtZD8rBaUctEIVUSm45ZtV1a8uIgSP-2ytCptcPrffZgW0GcGkwYTpkWt8dnxp2VGuOowZnmDt5IhVjqsq_UohRKMjV-Saho8HX96KSGuESrpT-7XN_3__eRYDlWEoPBdbMHiwFU7sw1tkZ8hAp1BCd--vT_P7hTiOZSAKFcoconwHEWNw02zPV87yFLOmTtO3iWSmARdzoEDhNe_zDQn_ofQlfqS9mdh43s7irYMM2Ved_B4avptGw62aqjAkQQyew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPj570bie5IZXIPch4JV5KkVDguA5ZASg7lCu8dzgfVlCC10J8E49UJKFFcx3ke7qk1UJeG5TGIWqoUoAuYZNMffSVmNCbQEbCxghBNL6Bq0swn_HxUSIIVApDzyKGKyS-MRnySgIO_HyxRxJP-0B_AkOvSixWkykCYanx-S1ef2wOGjrg8u9dS-RuyjqyxiVgL-0GaCDSCYwzcpsAc7y65ib_AmiOI3S6Qg3dftqset9hO9dqozBFt4Cr_3TbHUeeANuKO9EcQZ3pIc5alrYeslAcuezQGhOt8obKN0LtClG1-HvSDEiOWHtro1fTndNUSr_LoreMnJvt658hpfcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctSquA_duSum2Zgpq1XMQpKj4qnV0GuZfFUPaTHIyTx0W2XZP6F0moqQp4TmrbNr9JtW0R5GhHcRsbvZZk5D7P8YWb1Jab5gpaXnmC6MKVhUNqSY8c_J367bTAMjkBNaA_EgR6f6AoV5tT8-ySiy26GHucPLjP-9HcchB5Tz1IgML0GrPTn5tr643SO7-LfoqN6QZC3xivndAieewcqv7yTgiDe_7GowJKe34nQXEGaSXUiRMGk6-2ACstJ8Lg1KPQYlFR70uuJd9dY5CaL9Khr9qAKgJzpepItTIz5QB1tWXLJj69UaMOKGv3lAjBj_o4CAXhln_TIHadsYw7T0DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3AW3aHp8WnAKvMNpE1YjvkpV5dtG1XcS7bFKt5rxPJQHSxWj9xCYKerqd0wLwIOzgtpPibDMohVmInzYgmXk7X5cBTXfdDJ3I5GcWqlk1nX__hJ0sIpWKlAKij7XwLcJSNSI9C0CbeyPgV2arvRrEQf6ulnsTGhToZfkYUyqEoxyrgpUcO8VBuiN4FGv4HuZoKUjMschbj-xDScnNT3ySkqCGB-oUDhMXOY1-lVvZlxOSQC7DXrwETLFDIu0fPp3boU1pUnASlQW1yTbN8V74hEHuM57GuFvZPWo1FtUZpinOK6j08vM5EBZCzGZKSD0jElKGJfxuFsKlK7AJYoLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1QOdXyAxNA25s3KMI4F3sf9YqUHcSZ8j2c2RnkJfr7oiQDL6lSYJFIVAP_UG9Qh9Nuhc3s6S_mMyYVFSOsV2mCBRTs3AJyHjjEamqPrpDuvk4gFsMEMadUuCxZ-PfrHPN0A2-JI-6_2l8yfqA6j46g-dol42f7o7z-tGpU22oDXAppBVdqnY0HBff93OUNjnb5u6k_XkPBf3uPAW3Ro2u1phY3RR0_HDSQ1pRtGRH5L7NrT_trl4aj41wW9HAOAmCYgeR8KmNViSECsMueqEgKroKqSeadUjpBYsH4fC8jVTI42f_dO1LwPK-Ahnzu0HOOjWi47GFsyIZhuCYBfkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEoWGh2W_hxa8gnZyGaNK9V1Ox489lbvBamAK2oRy35Ewb-f3LqqQmiV_C1n3G4g2GrDq7kRpos49GC6TJw3-UL6kiu2QSZgPTjQqc0y2IbOU-gUCB0_S73Bx0Iw9G9Fd2HBlT3YZm59v71hYDV3Q_2EZqq-5snLa5RKludLDPEfD2-bk_DDKYS9egBSrekpUY0r5QO_88W6yaNRYk3ZygyqwLK8HKh-FVFsLRlNg54hOjDpw2_Rpuh6KEiu5eF8rCTvK2L5TwbPF56k5h6I9YXNcuKhXCI2IOdTipULzJdnBggOg94L5fC04hs9AKWYASrUX-x0xRfbtBFRTANmUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HixNULODzJAPOxDMT-SgUzd2Ct48VgwLAN8xHVcnxnWOlG_hbkB1nTwvIAdVPhC1KuvVGAEjtzcElAXR9hqLS0A39wadUGNJ3fYZVjkD-v8kabyL0TBxUL0CKT4vkSCwHMD_pAWsGC7cBoyvAyr2ceuAxH6TXpRnwUmw1Be59SJOMYLcxokxZ1u-JbFXgZ3rQv6mNcQhJTiMtIsrl93-G54Kks-3iwGln2vK2uWlMTaTftu3orgout-iGcL_t3KH7Zq9UKuGMurW8YWx9jN_-haWjWRlUYs_l4MtfUTUe37qXqe94U4bIdRoyGb5DX8kSkI1G44iklSS25KCGJ7b4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCexAgbXUo2EhYiPE1j8iaYrS17MBSL7E66DFiFHQg6c3TKn9pGWOqyBGXAcEwIsFgDwrBUFuwJEKHxXkp5-jIqySYTC3SR4yYzfVtfBz1VrVqpwtApuKru48u9FfSdkUslC_voLRMf2uT0n8bwJY4uUu7j6UYEgPmrwfPa2lSieSixN8hgr-grLIAdw4KBr7bVOehlgGT6TTH0upZfd1JGet11dlxCeGyIBpmQVwCMpqUc7OEuVkB-LSNss71z2yuzJLqYyaZQMa-r2lJ6Hr7GeImmvs-zsun2SbxTK6ppWETJ9v58Dkbg6CpMXyXt3aU12gtFDm09DCJoEyg__KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGu23JgV7h6k7knPY-9TeWTgG5uVuAOhNgGSSU1iozzm9BgWLKHfUdN-oIfl5jsxkojsOjZ240Slczp3bbsheohx9qMhHdzqjmb6yHXP2_c-ASUeKCl4m8ujlF9xDAmH86Rxxy-lRU5JokX4-nQF7YGSEXMPMPRceJbqYK7WHZI867mWHDwyXnpi1SXUna7HqaiPhlSbSZb-EF6r64i0_TiPzG_aG_dRlgdW7Jo3ZBqmnwfISxncI-HST0fxdOPeASkh4G6f01mRsckfRLwKcjVJKTufAwEM4O2BcWLohSCO_0pTolInXttCol_Ir5FBUmsLmn11YCLz7qLXLKydyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ualLceo2GtKZZAMxqOYA4mjiYaCaJ8CHdd6A3G4Uj4lkU3hcU9vgNwYgkIrpifvPjfxzffDRVjxrAK94-xHUNs_3UDNvgIz-dlh1D4PRtpVUkV8z80fmoUN_K-7aB8HFKY3eIrFutIzR0uazk6O0-SpMnJkrRtWfQVK8PWZbL4JJXJOj7UT2UqFgXWVkuPpjwzxSFAAxj55bvVUPNNkdXvq4KDStVwFBeT-qNEwEL1YCWQjNMfcu6cypPktG5ijXuJu8XEHXxjnsVupLfmdSkpdpnUee5fU5OUJXPZA1PvCJzLtYDFM4xznpgwUXhKEi1v4K30qACqz7JudzB4jnsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCg1i9TTd7BhNAMaJCV9KCQApm2hX2NGWjq3Au_T1neBASh_A3_W4riKvIKiFwj77ovLGGsLX0enyccAjguOvQX-yEYnKRFdHdHw7eCgfdKKjPKdmhSVPA4xVVGdc-POQdpAsKp8TSb00WW8na_t1xqoYymY204VwcFB0nkMVg8mNwippcl6RQPslLH0onPFvX1qpO_IzFaog4cra1BxoCe08HDparMcGS0jD_KrNhe6VDgfCN3v0eu_OyFVE_t4Vqosr9E1nJDWNsTDKAfbMAjpxi7VSvPpOqCuI0X0B_5PaVD_a8swwZQb8h1A37LVTJpd5GhUI87hCXBEb3keaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UubvzmVw-z9AwacUxawRXGq5HusU6CCrwJJRdNP0jNx7E1LZsDsMdMU6krTn0kjm5uklkjJ6a1R_ibRnAkpBEkHaEd0ccu0zbu0ozPeZO6UoQkTRIjgUS0jqYXYbwezzDwNaj6CQevgw3JzLVZShze0setBchiMzVDDfkq_OnJtCf7hDWjftehRRJBoQoCtRa5LSZSRoxOo3z82YkA6rHhkeBryGkDM_24NiwFZaD1B9xZnrMbj0FwsHDiM6oFkrm_4AqyFtR-WYz9ROEME12Re92znR7AURMn5GZiAsTg7jfh5Vj83cfMVmd9gZeHW3eY1mioqp41V2T1J10ugL_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SilUltIAXVilZg1tO_xwt2iIUggw1XOl0jToLVyepRZb_gSYV5mrz8KBi04ETP4QHtIvT1hX5J9f3dvox3eWpo6SEFgla2as6ohNp53DVhnv32pNAffFobw0uBQAXJ1mQ_StHhu0FJh2fRMt4WK9wGjzsTYaeNui-ZjFxOCj5ZVp4eDDGss2ykxZ9pqNwCba6IFHethN7Vn_jp5mrms98NBbnQzQ_lsczWHIF0kpjlAH6zsse_zo1CkDE9lI7EAxmswnbN5-zBj1HC_r6hsYdeRiMOUYcTDazjwUb7QL648NgjVJjAP2hpVNDlS7cr3Qi1Zo9EzDTrcNrHtNu2toKQ.jpg" alt="photo" loading="lazy"/></div>
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

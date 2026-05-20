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
<img src="https://cdn4.telesco.pe/file/gKmQdUj6gXJnq02NxBNx0GUGkkOVC6Mtof2ecxXSjv7XZ9fLRQoKKMbziou0g5499tXBhLY1jos78Vyal1dZyStECim_5GzGdtqpGDHM8lazeV3vXIA-L0i3oHIQQMFWEkQvbYqyPHaNY1abb7oaz6DRQlWfkX5zHS2tAweiLxTbi_mSPtTZf2iYJnlbiwB6si9E-LMt0Pbr4Nb5TbCUVRKiwxg9jPkRqmaf2cQFObAJqw6BmaLw4D8i0C5qluh7I4NnCLIxvuw3iKvImJwG-XPNdfbTPtit2P8CeznP2aHHEnyZsfnKCBr44N1LVsbhsoMngqACNczChFnXDT3B7g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 253K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-30 21:07:19</div>
<hr>

<div class="tg-post" id="msg-75769">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🏴‍☠️
‏هيئة البث الإسرائيلية: نتنياهو يحاول إقناع ترمب بمنح الضوء الأخضر لاستئناف الحرب على إيران.  ‏نتنياهو لم يكن على توافق مع رأي ترامب بشأن التفاوض مع إيران.   ترامب يميل لدعم توجيه ضربة عسكرية لكنه لا يزال يترك نافذة ضيقة للمفاوضات مع إيران.   إسرائيل تتخذ…</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/naya_foriraq/75769" target="_blank">📅 20:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75768">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‏ترامب: رئيس الوزراء الإسرائيلي نتنياهو سيفعل كل ما أريده منه  متأكد؟ جا وفيديوات ابستين؟
😄</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/naya_foriraq/75768" target="_blank">📅 20:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75767">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ff7f595ec.mp4?token=CBLGrAYuw89kmkvQXu-daj7rRXgwVes_JHMhAnlXjEjl4oEopEVfbk0tB1d9P_WGzwSXu-V5FhWOM2_SFkSsGurhRczkMQY7lqE7hPxZTv8Tj-hE5c0fn3WfM00oat8iaSH-QJMhMyZf7F93oHOqEvrJMu1xmnLU1peOjz9289g3likzSXn5ynmUiu1o3YPKHWNIB5jcE42_De72U4-ifEj4gfxr47xf1UbCG8dSUFc4-rV55yajLICI3eg3soKNGpeu7kMFYAT3hVlbYKwVW8UkhBdoVm1p2QcpdCN317OQXuQHmAZ--3CfP-0ZFKOTyjjlHN90xhvP0vSczKP3_1jy_m0Xlwr4iqlzDRZSYoKoSew-lOacv62hyAL8IiFlOTU-NL1l9OqYsjcl-K9Wm_1k3kpWuCk4B5-oC6URhITgyFXudtsA3hD71YHnwZv_cp1XTa-3U436dknjQ2mL_ySvw6Z6XIHUqW5nPQvDp9r07wI8CyRoH5kvpTXTb6Lm_9teJtuaBnEUNxBnt6_dtHFVOGJahzTAhkNoZW5NAfRpj5qflpUvmJbWFmFBAqfBn3t0hCeVBs5JEQyBqLrBQLl97aSfvbUZyenXIEpaaN9IWd8LzFaqYbDXug2sWkHAVsUu4TRY2QEMIm1hNzSJ13RU4Q5d23uMIYLcWFsAPlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ff7f595ec.mp4?token=CBLGrAYuw89kmkvQXu-daj7rRXgwVes_JHMhAnlXjEjl4oEopEVfbk0tB1d9P_WGzwSXu-V5FhWOM2_SFkSsGurhRczkMQY7lqE7hPxZTv8Tj-hE5c0fn3WfM00oat8iaSH-QJMhMyZf7F93oHOqEvrJMu1xmnLU1peOjz9289g3likzSXn5ynmUiu1o3YPKHWNIB5jcE42_De72U4-ifEj4gfxr47xf1UbCG8dSUFc4-rV55yajLICI3eg3soKNGpeu7kMFYAT3hVlbYKwVW8UkhBdoVm1p2QcpdCN317OQXuQHmAZ--3CfP-0ZFKOTyjjlHN90xhvP0vSczKP3_1jy_m0Xlwr4iqlzDRZSYoKoSew-lOacv62hyAL8IiFlOTU-NL1l9OqYsjcl-K9Wm_1k3kpWuCk4B5-oC6URhITgyFXudtsA3hD71YHnwZv_cp1XTa-3U436dknjQ2mL_ySvw6Z6XIHUqW5nPQvDp9r07wI8CyRoH5kvpTXTb6Lm_9teJtuaBnEUNxBnt6_dtHFVOGJahzTAhkNoZW5NAfRpj5qflpUvmJbWFmFBAqfBn3t0hCeVBs5JEQyBqLrBQLl97aSfvbUZyenXIEpaaN9IWd8LzFaqYbDXug2sWkHAVsUu4TRY2QEMIm1hNzSJ13RU4Q5d23uMIYLcWFsAPlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
17-05-2026
تموضع لوجستي تابع لجيش العدو الإسرائيلي في اسكندرونة ببلدة البيّاضة جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/naya_foriraq/75767" target="_blank">📅 20:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75766">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73f31002da.mp4?token=f9GtIQDJrrZWSuTAQz4QJqBUnqVYI2Mh45tLojbcSZEs2H6C_723QOp6_YDsr5pChjUTFvgec1RKoSTeOYb_pm4hPTNDaNEgjuE_GGEFSIluYn0qMDaMfE9zztCRIoTPTsCvgUvKAfvKKsLxZuiOsg2ioYn9SAiyJfJB61--YH1ESNhtKIfgllMYt3qzvFEmx_5Nr0GHE5FvvOjmqBY3-sh3MK58jkaes7fmjDxSFUIRGhNiIiWVbSiKD2P4Llu04olN8nv4AkQPm9bdBFGkXIDqe_Xvpm1sGVoIdV-4MERFwkEKZrtlyozkBMeIA2KEzhzmCdmU966VNA9sLatwAzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73f31002da.mp4?token=f9GtIQDJrrZWSuTAQz4QJqBUnqVYI2Mh45tLojbcSZEs2H6C_723QOp6_YDsr5pChjUTFvgec1RKoSTeOYb_pm4hPTNDaNEgjuE_GGEFSIluYn0qMDaMfE9zztCRIoTPTsCvgUvKAfvKKsLxZuiOsg2ioYn9SAiyJfJB61--YH1ESNhtKIfgllMYt3qzvFEmx_5Nr0GHE5FvvOjmqBY3-sh3MK58jkaes7fmjDxSFUIRGhNiIiWVbSiKD2P4Llu04olN8nv4AkQPm9bdBFGkXIDqe_Xvpm1sGVoIdV-4MERFwkEKZrtlyozkBMeIA2KEzhzmCdmU966VNA9sLatwAzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
القيادة المركزية الأمريكية تزعم:
في وقت سابق اليوم في خليج عمان، استولى مشاة البحرية الأمريكية من الوحدة البحرية الاستكشافية الـ 31 على سفينة النفط التجارية M/T Celestial Sea، التي ترفع العلم الإيراني، والتي يشتبه في أنها حاولت انتهاك الحصار الأمريكي من خلال العبور نحو ميناء إيراني.
أطلقت القوات الأمريكية سراح السفينة بعد تفتيشها وإصدار الأوامر لطاقم السفينة بتغيير مسارها.</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/naya_foriraq/75766" target="_blank">📅 20:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75765">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية:
نركز حاليا على إنهاء الحرب في جميع الجبهات لا سيما لبنان.
إذا أصر الطرف المقابل على مطالبه المفرطة فإنه يمكن القول إن الدبلوماسية لم تحقق نتائجها.
الحديث عن الإنذارات والمواعيد النهائية بشأن إيران أمرٌ سخيف.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/naya_foriraq/75765" target="_blank">📅 20:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75764">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">⭐️
رويترز:
بعض السفن تدفع لإيران ما يزيد عن 150 ألف دولار لضمان مرور مضيق هرمز.
‏رسوم عبور السفن لمضيق هرمز لا تفرض على كافة الدول.
‏الآلية الإيرانية الجديدة في مضيق هرمز تعطي الأفضلية للسفن المرتبطة بروسيا والصين.
‏"وثيقة الانتماء" التي تقدم للسفن مقابل عبور هرمز تؤكد عدم ارتباطها بأميركا أو تل أبيب.
‏الدول التي ترغب في عبور سفنها مضيق هرمز يجب أن تتصل بوزير الخارجية الإيراني.</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/naya_foriraq/75764" target="_blank">📅 20:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75763">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">⭐️
إستمرار موجة الإنسحابات..
النائب "حسن قاسم الخفاجي" يعلن إنسحابه عن تحالف الإعمار والتنمية.</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/naya_foriraq/75763" target="_blank">📅 20:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75762">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84c2e4689c.mp4?token=X8YDH7K9w0Jcz0C-3viUmFioKJtwNRdDTV2-2b60HrzSQ-Hbxb3QuWakbfrxCpx77b1gT66IaPCSxJPyzdy9Dtv2NvDaXV70PgSNFRaeOh53WifRKLHGzYG94IIFMTkrcTfBr_ZsnMcp3JuEJn2G8ccXMQ2UtIEKl7swN4gKh1i8W1rs2V1ExgSx01fxUVVQ8lwYXliSXwal_heTGsd0AXIM0hq1hpiOHIoA5BWdihma-TkUxeo9v32Ff1LJza7fLj2xvzXK0wtl-rU6MPRgfc58rdkbkm-F3JIid-B79C7jnIExIlzrijbpNrPh97qrfRNH3gE-EEfG7i9zbHSDDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84c2e4689c.mp4?token=X8YDH7K9w0Jcz0C-3viUmFioKJtwNRdDTV2-2b60HrzSQ-Hbxb3QuWakbfrxCpx77b1gT66IaPCSxJPyzdy9Dtv2NvDaXV70PgSNFRaeOh53WifRKLHGzYG94IIFMTkrcTfBr_ZsnMcp3JuEJn2G8ccXMQ2UtIEKl7swN4gKh1i8W1rs2V1ExgSx01fxUVVQ8lwYXliSXwal_heTGsd0AXIM0hq1hpiOHIoA5BWdihma-TkUxeo9v32Ff1LJza7fLj2xvzXK0wtl-rU6MPRgfc58rdkbkm-F3JIid-B79C7jnIExIlzrijbpNrPh97qrfRNH3gE-EEfG7i9zbHSDDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب: سنمنح ايران فرصة واحدة، أنا لست في عجلة من أمري.  إما أن نتوصل إلى اتفاق مع إيران أو سنقوم بأمور قاسية ونأمل ألا يحدث ذلك.</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/naya_foriraq/75762" target="_blank">📅 19:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75761">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇮🇷
هجوم مسلح من قبل عناصر إرهابية يطال عجلة تابعة للقوات الأمنية في مدينة سراوان بمحافظة بلوشستان جنوب شرق إيران ؛ إستشهاد أحد أفراد الأمن الإيراني كحصيلة أولية.</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/naya_foriraq/75761" target="_blank">📅 19:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75760">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
استهداف دبابة ميركافا وإعطابها بواسطة صاروخ موجه في جنوب لبنان.</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/naya_foriraq/75760" target="_blank">📅 19:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75759">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f93dd2e141.mp4?token=s8x8AYc_ektokuN8ahN-pPE8vyQw3lHfgIeV0iNL21GY0Wkwdl7J9WfPJeUoKTTTC12vi8hx3fR0vN07NralTFcRE985Tf7Er13hfFM688B8Yy43PK4CGGuDHqC7At-XgVXuzzDjMcU8YDGVkd4BOycstXXKAsTKTLM3xRWQ2kO64XaP0Xuzi3G6qRKkW8eDwree04tfp5Xv0UJi-5VaBZJdLtC4Ix69_HTc9d-SeGY-DF2EOUoCVuF6j_u1JhwpmAwtkypECkHZDojq2yxCua8BkypYv4BYpsQ-prXKnNdJlSAVIFl45qEpixXVfgQvIY7w6Qi9vtiLfoqdMqW7cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f93dd2e141.mp4?token=s8x8AYc_ektokuN8ahN-pPE8vyQw3lHfgIeV0iNL21GY0Wkwdl7J9WfPJeUoKTTTC12vi8hx3fR0vN07NralTFcRE985Tf7Er13hfFM688B8Yy43PK4CGGuDHqC7At-XgVXuzzDjMcU8YDGVkd4BOycstXXKAsTKTLM3xRWQ2kO64XaP0Xuzi3G6qRKkW8eDwree04tfp5Xv0UJi-5VaBZJdLtC4Ix69_HTc9d-SeGY-DF2EOUoCVuF6j_u1JhwpmAwtkypECkHZDojq2yxCua8BkypYv4BYpsQ-prXKnNdJlSAVIFl45qEpixXVfgQvIY7w6Qi9vtiLfoqdMqW7cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🏴‍☠️
ضمن الإستعدادات العسكرية للعدو الصهيوأمريكي..
مشاهد تظهر العديد من طائرات التزود بالوقود الأمريكية في مطار بن غوريون الصهيوني.</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/naya_foriraq/75759" target="_blank">📅 18:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75758">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nA9Pe9ESzTXJL989fzb5YPX12t5np8oybqZS6VOnsKi6o9gXlb5SLpb-C2dSzYS4ScbRIdagFzHJ5qOe7Oe8EvEyRc7XAV37S7vl4nP52t6IBvlgxV_OKmwZ6I9rJWYCVK23EdHCwxxDegbL4a5021WOhNekKyW0YgttKo7b97TIDi1nfFXf_oQ7zIJEZ34sQXda0RdnyVFliBpebUVgExM8zUh_YCb2QqbFyarmlSsAodNax1Bhm_bNYR7wvqC3zS-_x59w_ByPNg9rGsGS1MzabnqzEBV2QWfXyhn-KqYIUFsMA_w15NCH-7BKOFmzPLXJCDtptX6sZ-ePJR4ubw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
من المثير للصدمة أن الجمهوريين احتفظوا بالموقف المهم جدا "البرلماني" في أيدي امرأة، إليزابيث ماكدونو، التي عينها، منذ فترة طويلة، من قبل باراك حسين أوباما والمجنون الشرير المعروف باسم السيناتور هاري ريد، الذي أدار مجلس الشيوخ للدوموقراطيين ب "قبضة حديدية". على مر السنين، كانت وحشية للجمهوريين، ولكن ليس كذلك بالنسبة للدومقراطيين - فلماذا لم يتم استبدالها؟ هناك العديد من الأشخاص العادلين الذين سيكونون مؤهلين لتلك الوظيفة الحيوية.
يلعب الجمهوريون لعبة ناعمة للغاية مقارنة بالدوموقراطيين. إنه أكبر عيب في السياسة. يغش الدوموقراطيون ويكذبون ويسرقون، خاصة عندما يتعلق الأمر بالأصوات في الانتخابات، ولكنهم يلتزمون ببعضهم البعض، في حين يسمح الجمهوريون لإليزابيث ماكدونوز في العالم بالبقاء في السلطة، ووحشيتنا. نحن بحاجة إلى تمرير قانون إنقاذ أمريكا، والآن - وبالمثل، قتل المماطلة، التي من شأنها أن تعطينا كل شيء! إذا لم نمرر واحدا على الأقل من هذين الحكمين بسرعة، فلن ترى رئيسا جمهوريا آخر مرة أخرى. سينتهي الأمر بالدوموقراطيين بولايتين إضافيتين، العاصمة وبورتوريكو، وكل ما يترتب على ذلك، بما في ذلك
4 أعضاء في مجلس الشيوخ، والعديد من أعضاء الكونغرس، والعديد من الأصوات الانتخابية الإضافية، وسيحصلون أيضا على حلمهم في محكمة عليا للولايات المتحدة معبأة برقمهم المفضل - 21 قاضيا.
سيقضي الدوموقراطيون على المماطلة في اليوم الأول الذي يحصلون فيه على فرصة للقيام بذلك.
الجمهوريون لا يفعلون ذلك لأنهم يقولون إن الدوموقراطيين لن يفعلوا ذلك أبدا، لكن الجمهوريين مخطئون. كن جمهوريين أذكياء وصعبين، وإلا ستبحثون جميعا عن وظيفة في وقت أقرب بكثير مما كنتم تعتقدون أنه ممكن!</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/naya_foriraq/75758" target="_blank">📅 18:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75757">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4d89ae9e5.mp4?token=CdwpqpDDeG6FwEEeTTZwHcPlP2LZ7kWZP53Hc38R6P5KeB-GIc9iMZRYMNH9h5h1lVqXO80OA0iv2L8ZkQPG1ar6h2w1xfnoURURraRgQPFBEC8HYd0p9OaeahYH1f8UNFWhkJzCugYkpOSnSrxw4HBznJaRdxoKKTXrXVD6uHXQ3UNpvabDjgbSdpzbe9-v9-ILywEpacXCSFDAQwVquTym_Ay-jVKr0Kew27duXfRo_STs2TB-dNiOfbJT2TeWpexvsnprmg06giJKM9ICqjidPMTaVO6mRh7LkXTNQS3u1QgS8w2jdxjpmcsIiQwr4oAnktDbx4NE_CZFKgwlU5_IQlPtBAfRSBKaMTrzMfl0gRBOQjpEeJGXlufP5zEAGisduCLxqRr_bh-iG3Jfi_h9eB_4MuWq-OcNFRe4FEKemWLw5TVuYCulBtCUKB7MB_dDDrdjRLHCs98Sl0kRkcwAmYlXrF8WMColFWGepl_hBT1IL_tbUXxlCRLWB4Aw7YYK842hts6arH2P4ZcFwDMjmbRkkBbPTvaah15J2u7TugX1eKL_ZSXNPDVFO5aLdQEjDrE6S9n6uRXmtsGPyVtwOWoCoF_kMJIPYplvwcWCXwrMEYUFZ6yPiefUGX4WTI9plk_J0FAHppCSQjTUqJwwfYAHKT3-SpAz7Df2Kow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4d89ae9e5.mp4?token=CdwpqpDDeG6FwEEeTTZwHcPlP2LZ7kWZP53Hc38R6P5KeB-GIc9iMZRYMNH9h5h1lVqXO80OA0iv2L8ZkQPG1ar6h2w1xfnoURURraRgQPFBEC8HYd0p9OaeahYH1f8UNFWhkJzCugYkpOSnSrxw4HBznJaRdxoKKTXrXVD6uHXQ3UNpvabDjgbSdpzbe9-v9-ILywEpacXCSFDAQwVquTym_Ay-jVKr0Kew27duXfRo_STs2TB-dNiOfbJT2TeWpexvsnprmg06giJKM9ICqjidPMTaVO6mRh7LkXTNQS3u1QgS8w2jdxjpmcsIiQwr4oAnktDbx4NE_CZFKgwlU5_IQlPtBAfRSBKaMTrzMfl0gRBOQjpEeJGXlufP5zEAGisduCLxqRr_bh-iG3Jfi_h9eB_4MuWq-OcNFRe4FEKemWLw5TVuYCulBtCUKB7MB_dDDrdjRLHCs98Sl0kRkcwAmYlXrF8WMColFWGepl_hBT1IL_tbUXxlCRLWB4Aw7YYK842hts6arH2P4ZcFwDMjmbRkkBbPTvaah15J2u7TugX1eKL_ZSXNPDVFO5aLdQEjDrE6S9n6uRXmtsGPyVtwOWoCoF_kMJIPYplvwcWCXwrMEYUFZ6yPiefUGX4WTI9plk_J0FAHppCSQjTUqJwwfYAHKT3-SpAz7Df2Kow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
اعلام العدو تحت بند سمح بالنشر: اصيب قائد اللواء 401، بجروح خطيرة إثر انفجار طائرة مسيّرة مفخخة اخترقت المنزل الذي كان متواجدًا فيه في جنوب لبنان. كما أُصيب معه أيضًا ضابط برتبة مقدم.</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/naya_foriraq/75757" target="_blank">📅 18:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75756">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇮🇷
المتحدث باسم وزارة الخارجية الايرانية:
المفاوضات مستمرة عبر وسطاء باكستانيين. ما نريده في الأساس ليس مطالب، بل حقوقنا. قدمت الولايات المتحدة مطالب عديدة، لكن السؤال هو: لماذا ينبغي لإيران نقل يورانيومها المخصب إلى دولة أخرى؟ لم يكن أحد قلقًا بشأن برنامجنا النووي، والجميع يعلم أن برنامجنا النووي سلمي تمامًا.</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/naya_foriraq/75756" target="_blank">📅 18:27 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75755">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇺🇸
‏
ترامب بشأن كوبا:
لن تتسامح أمريكا مع دولة مارقة تمارس عمليات عسكرية واستخباراتية وإرهابية أجنبية معادية على بعد تسعين ميلاً فقط منا.</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/naya_foriraq/75755" target="_blank">📅 18:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75754">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🌟
نت بلوكس:
تُظهر المقاييس انقطاع خدمة الإنترنت في معظم أنحاء ‌العراق باستثناء الشمال لمدة ساعتين تقريبًا هذا الصباح. تُقدَّم هذه السياسة، المطبقة منذ سنوات، كوسيلة لوقف التسريب والغش في الامتحانات المدرسية، لكنها تؤثر بشكل غير متناسب على المستخدمين والشركات.</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/naya_foriraq/75754" target="_blank">📅 18:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75753">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jeh9_ABjZohB7Zh7zY01h2ySNkw7h64tQNHfNLWQ0x0yaQHaShGmDk-6IgL_BHHPEXyFRNbjkfgNi9o6ht-Vmln-A9OQSFmdY-Gwvzu5K1XGdZDHkrk3g0te14FcTev68rVn4V-jc2E8kI26LOYcDklXbPDPPiG7Tak_7L4anD29sY_6p-mPgPkR6lyqb5rGYnJZCDRSDkINngzmpAuzqUHj1MekcbN51-LoDnL7aac98Jzq1pBeiyaj7-3Um5qMp9LK1aNiQqUomPVUibGuNSA0aKGVuXMDFZDFfOmMh_sF5dXdSJB9BTAp0jcj5o_iBOYThFaa5acyKQwf7YZKaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسالة من مجاهدي المقاومة الإسلامية إلى سماحة الأمين العام لحزب الله الشيخ نعيم قاسم (حفظه الله):
بسم الله الرحمن الرحيم
سماحة الأمين العام حجة الإسلام والمسلمين المجاهد الشيخ نعيم قاسم حفظكم المولى
السلام عليكم ورحمة الله وبركاته
تلقّينا رسالتكم العزيزة وفيها أثر الوالد على أبنائه والقائد على جنوده والشيخ على مريديه.
نشكر لكم يا شيخنا الحبيب مشاعركم الصادقة ومودتكم الخالصة وعاطفتكم الصافية.
ونرد لكم التحية، بتحيّةٍ ملؤها إيمان وسنامها جهاد ومآلها نصر وشهادة.
كما نتوجّه بإجلالٍ وتعظيمٍ إلى أرواح الشهداء من إخوتنا المجاهدين وأهلنا الأوفياء، الذين أدهشوا العالم بصبرهم وثباتهم وصمودهم، وكانوا وما زالوا الحصن المنيع على الفتن والسند المتين في ذورة المحن، ظهر المقاومة في ميدان الدّفاع عن الوطن ضدّ الاحتلال الصّهيونيّ الغادر والهمجي.
أيها الأمين المفدى، إن أبناءك المجاهدين في المقاومة الإسلامية قد راهنوا على الله تعالى قبل حمل البنادق، وامتثلوا لأمره وتوكّلوا عليه ونزلوا سوح الوغى مسدّدين بالصّبر ومؤيّدين بالمدد من عنده، وهم في كل يوم يسطرون ملاحم التصدي الكربلائي ويلاحقون العدو بكافة أنواع أسلحتهم، يدمّرون دبّاباته ويحرّقون آلياته ويرعبون جنوده ويلقّنون جيشه دروساً ستُحفر في ذاكرته المصطنعة، ويبقون الوطن عصياً على القهر والإحتلال.
يا شيخنا، لقد فتحت قيادتكم الشّجاعة الطّريق أمام سلسلة من العمليات التي جعلت العدوّ منهكاً، يتهيّب الاستقرار فوق التّراب الجنوبيّ، قد أدمن النظر إلى السّماء، مترقّبا صلياتنا ومسيراتنا، واعتاد تنكيس رأسه في الأرض، مذعورًا من عبواتنا وكمائننا. عهدنا ما عهدتم إلينا به: سنبقيه على هذه الحال ولدينا مزيد؛ لن نهدأ ولن نستكين ولن تقر لنا عين حتى يرحل الاحتلال عن أرضنا مهزوماً خائباً، وبيننا وبينه أيامٌ لن يصبر على مدتها وسنصبر، لأننا أهل الأرض، وليالٍ مظلمة في عين المحتل أضأناها بذكر الله، وميدانٌ سيحصد منه أشلاء القتلى والجرحى، بعد أن زرعناه بالبارود والنار.
باسم حبات التّراب، باسم كل شهيد، وكل مجاهد في تشكيلات المقاومة المتأهبة على امتداد جبهة المواجهة، نجدد لكم الولاية والقسم والبيعة، بالاستمرار على هذا النّهج حفاظًا على العزّة والحرية والكرامة والإستقلال؛ فحياة الأوطان لا تُكتسب إلا بالتضحيات الحمراء، وشرف الجنوب يأبى أن يتحرّر إلاّ على أيدي المقاومين، ولن يخيب عليهم رهان إن شاء الله تعالى.
والسّلام عليكم ونصر الله وبركاته
أبناؤك مجاهدو المقاومة الاسلامية
الأربعاء 20-05-2026 م
03 ذو الحجّة 1447 هـ</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/naya_foriraq/75753" target="_blank">📅 18:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75752">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">الاعلام السعودي يزعم: العمل جار بجدية على وضع اللمسات النهائية على نص اتفاق بين واشنطن وطهران</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/naya_foriraq/75752" target="_blank">📅 17:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75751">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">الاعلام السعودي يزعم:
العمل جار بجدية على وضع اللمسات النهائية على نص اتفاق بين واشنطن وطهران</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/naya_foriraq/75751" target="_blank">📅 17:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75750">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🏴‍☠️
اعلام العدو تحت بند
سمح بالنشر:
اصيب قائد اللواء 401، بجروح خطيرة إثر انفجار طائرة مسيّرة مفخخة اخترقت المنزل الذي كان متواجدًا فيه في جنوب لبنان. كما أُصيب معه أيضًا ضابط برتبة مقدم.</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/naya_foriraq/75750" target="_blank">📅 17:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75749">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🤺
🏴‍☠️
اعلام العدو:
حدث أمني في جنوب لبنان.. التفاصيل لاحقًا.</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/naya_foriraq/75749" target="_blank">📅 17:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75748">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/352ed3da2b.mp4?token=sGpYxHMErIDWhGIajMHBDqruRiyL_dCejwEsC-SNR3qEg3xZTdgwVJ13eMAtiSJXBXX0gTN4vbKGmKOOtgefjNU3VNBYl49HR0wm7-ugYVOI2LvWYZHozr1cqadV0TTFKsdCj_ezApFsOJHXVh7wgSMVpDmfwVdCx5DJ7fMA5ed2DPGFKNVVDmwb4t59eY2xjljIYbx1ecDJkKqnE33IZ3krIB6axNB8rJLtK91iob817PvvgsMc9uHghAHMVl76c-JgT5vgoZkgRLLYqxUUbZaz2yAbj4Fob2IZH_PmcGd807msGG2-CKFHRGZ_R4Wm4mSxO0gNh8PdY3C_CRympw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/352ed3da2b.mp4?token=sGpYxHMErIDWhGIajMHBDqruRiyL_dCejwEsC-SNR3qEg3xZTdgwVJ13eMAtiSJXBXX0gTN4vbKGmKOOtgefjNU3VNBYl49HR0wm7-ugYVOI2LvWYZHozr1cqadV0TTFKsdCj_ezApFsOJHXVh7wgSMVpDmfwVdCx5DJ7fMA5ed2DPGFKNVVDmwb4t59eY2xjljIYbx1ecDJkKqnE33IZ3krIB6axNB8rJLtK91iob817PvvgsMc9uHghAHMVl76c-JgT5vgoZkgRLLYqxUUbZaz2yAbj4Fob2IZH_PmcGd807msGG2-CKFHRGZ_R4Wm4mSxO0gNh8PdY3C_CRympw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: أوباما انسحب من أفغانستان.  علما ان بايدن من انسحب</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/naya_foriraq/75748" target="_blank">📅 17:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75747">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f240d29220.mp4?token=f7apRT7z71Ghwx-naj7qz9a2iXjqZJZKKLMw6Sau30BlzQJu5y-iOVZdPbZOrO89Hlm3x3EalRGKhTWVxe1XALk8WyEzJm27qM2WMCYqQ23wIzrP_jKDtkdNwG4i-soVFu8_dPFT8DpEPpgd4FsNFNx0zs95TaYjzirCI6CypiuZxyWjNETEKM4npn39Bj659GmyaLTlg_ofeBn1wmanDCLFA8UMIgSOtp6Tq4jXaL1ARZdD4yLbJwJPBw3yPzOTv86ZinPMHvSNDghVR4O-ivwPi0hpa4e20hAJY2egtAbfzyA1QMez-3np_XrKxfYzPYzCQeMT5jKR4VS7dQqmgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f240d29220.mp4?token=f7apRT7z71Ghwx-naj7qz9a2iXjqZJZKKLMw6Sau30BlzQJu5y-iOVZdPbZOrO89Hlm3x3EalRGKhTWVxe1XALk8WyEzJm27qM2WMCYqQ23wIzrP_jKDtkdNwG4i-soVFu8_dPFT8DpEPpgd4FsNFNx0zs95TaYjzirCI6CypiuZxyWjNETEKM4npn39Bj659GmyaLTlg_ofeBn1wmanDCLFA8UMIgSOtp6Tq4jXaL1ARZdD4yLbJwJPBw3yPzOTv86ZinPMHvSNDghVR4O-ivwPi0hpa4e20hAJY2egtAbfzyA1QMez-3np_XrKxfYzPYzCQeMT5jKR4VS7dQqmgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: لو أن يسوع المسيح نزل وأحصى الأصوات، لكنت فزت في كاليفورنيا. لكنها انتخابات مزورة.</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/naya_foriraq/75747" target="_blank">📅 17:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75746">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lqxc8EmeKy8rHxW1hc-ijySJrxu-9vmtSoIoDBRRm2FsbXNqP2dAYOJUqvkeNoC3VF8DOLLVlV1rj-FjBZvTpcPYeuubpLjNgE621Zx2NzZo26cY5CPgYlgdhJHSLbRVgNf_b1iSVixuPa1-R4OmeCBprPP7RjpV3AbkvWpTtSOyQVLJVVeOGe2X-SAkw8bUs89wVgk13hcwS0jp0J_ZLVXUDAf1LpkTW-4CobfJyx5Ozewd0S-kBoSKkiCTxzNalcZYqcY_HF9qxCZwtN3IQsdDifQSNfHL8kEePX9gDqVfqGls9qqk9BilwD28dSpKEjdmwGKu8XzbgFhaqa3eug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
وزير الخارجية السعودي:
نقدّر تجاوب ترامب بمنح المفاوضات فرصة للتوصل لاتفاق ونتطلع لأن تغتنم إيران الفرصة لتجنب التداعيات الخطيرة للتصعيد.</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/naya_foriraq/75746" target="_blank">📅 17:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75745">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترامب: لسنا على عجلة من امرنا لفتح مضيق هرمز.</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/naya_foriraq/75745" target="_blank">📅 17:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75744">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب: سنمنح ايران فرصة واحدة، أنا لست في عجلة من أمري.  إما أن نتوصل إلى اتفاق مع إيران أو سنقوم بأمور قاسية ونأمل ألا يحدث ذلك.</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/naya_foriraq/75744" target="_blank">📅 17:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75743">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‏ترامب: رئيس الوزراء الإسرائيلي نتنياهو سيفعل كل ما أريده منه  متأكد؟ جا وفيديوات ابستين؟
😄</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/naya_foriraq/75743" target="_blank">📅 17:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75742">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5677620f9.mp4?token=bW8npgvoEjPDLwGwWPdZYcbZ6bxLx-YIFwlSt-IXkZznKD4BWBKAeK1hxAuMS0U0X8bijW569dScHLCaNTV5NdeOG6BeYH0TnsZ2YnEdyASFnNJz0TEjTYTZ3wB-jIkgupvkGZiJZz0DWjNfFDXeA7Th_FBwYrr1u8-rgMe1Zl0yoKuu6RgClKvNetMW7FuYOjUpdnn7ZP6lNmK3bxAgQdCHEwAGAJVhRJDdXebR5Zcs6HGln7LaVo8ZXjA8rWOpfThueIS6iuCMoN_io_PtbUdj5TmBlAaHQd11-vgrBtzB3FPLASnXFnGfAx4pD8Esg_uFhLltYtpWG5Yu0613jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5677620f9.mp4?token=bW8npgvoEjPDLwGwWPdZYcbZ6bxLx-YIFwlSt-IXkZznKD4BWBKAeK1hxAuMS0U0X8bijW569dScHLCaNTV5NdeOG6BeYH0TnsZ2YnEdyASFnNJz0TEjTYTZ3wB-jIkgupvkGZiJZz0DWjNfFDXeA7Th_FBwYrr1u8-rgMe1Zl0yoKuu6RgClKvNetMW7FuYOjUpdnn7ZP6lNmK3bxAgQdCHEwAGAJVhRJDdXebR5Zcs6HGln7LaVo8ZXjA8rWOpfThueIS6iuCMoN_io_PtbUdj5TmBlAaHQd11-vgrBtzB3FPLASnXFnGfAx4pD8Esg_uFhLltYtpWG5Yu0613jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
ترامب:
رئيس الوزراء الإسرائيلي نتنياهو سيفعل كل ما أريده منه
متأكد؟ جا وفيديوات ابستين؟
😄</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/naya_foriraq/75742" target="_blank">📅 17:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75741">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">رئيس المعارضة في الكيان يائير لابيد: الهجوم الذي حدث اليوم قام به بن غفير لكن المسؤول عن هذا الهجوم الخطير هو رئيس الوزراء نتن ياهو الذي أدخل مجرماً مداناً إلى الحكومة، وكل من وافق على أن يكون شريكاً لشخص غير مسؤول بهذا الشكل</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/naya_foriraq/75741" target="_blank">📅 17:03 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75740">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">محمد باقر قاليباف: لا يزال العدو يأمل في استسلام الشعب الإيراني، ويعتقد خطأً أنه يستطيع إقناع إيران بالاستجابة بشكل إيجابي لجشع أمريكا من خلال مواصلة الحصار واستئناف الحرب. إن الضغوط الاقتصادية المتزايدة والحصار لن يجبرا إيران على الاستسلام</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/naya_foriraq/75740" target="_blank">📅 17:02 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75739">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇷
‏رئيس البرلمان الإيراني محمد باقر قاليباف: التحركات الواضحة والخفية لـ"العدو" تُظهر أنهم يسعون إلى جولة جديدة من الحرب</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/naya_foriraq/75739" target="_blank">📅 17:01 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75738">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇷
‏
رئيس البرلمان الإيراني محمد باقر قاليباف:
التحركات الواضحة والخفية لـ"العدو" تُظهر أنهم يسعون إلى جولة جديدة من الحرب</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/naya_foriraq/75738" target="_blank">📅 16:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75737">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFkgOnDCTAQlTnClq4POSBFXg5CBkoFqo0WdIbxsVusStAa32z6c9qFMDnde_AKuNAP6_ONOsy4hYidP0f468G6tnzwTla4pk05kz5tKQ-c2S6-AlLPghu2r-pJEZRXBrk-q1HFUzfP3vSGwULfbV99FNF7xnVm-_DzYJmjnXr3A5p6VIhCVMHYvuPvLdlSFSBgqnDHkBM2R-DruYzWPkCDLPO9oiJAr4UqIwO0Th2vdL0TE1RHe0CkxJTuuLeu-75nGY_fgszyEPzsunm0_2-99bS9vB9vs-0lISf6G0pjY6qtUJLCl2MTgZftRyi8fPsFpZQe1JgU5PUJeoSHXsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بن غفير يهاجم وزير الخارجية الصهيوني: هناك من في الحكومة لم يستوعبوا بعد كيفية التعامل مع مؤيدي الإرهاب. من المتوقع أن يدرك وزير الخارجية الإسرائيلي أن إسرائيل لم تعد دولةً تُعتمد عليها. أي شخص يأتي إلى أراضينا لدعم الإرهاب والتضامن مع حماس سيُختطف، ولن نتسامح…</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/naya_foriraq/75737" target="_blank">📅 16:51 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75736">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9PNHKUegQv9IkEWX4UyT5tZkgi6Uoy77T-D8Pyvo9oxE-q64PZ08YS0pmpFBreBK3mzJ0RwkIE3vF3VWBUrryhNU5elsJMi4vtkDj1F50go0aKyDIKm9Rwfnn7Wma34t3oMu6OQWVcwjVjIZJwKy7fInWvXVD2nqRPY7EvsVETrkR234anvslW9X6LZGUS2oVBW9-76Fm2W0A1yqWpKMzzY064UZ2lz5A74CotDyw0AMRJ_QPsVRwLAeXq9EV2KBtMINN1dbbX62Qmdm1snvDjFnbJO95aNuhqNllJOgVaW8anPQDot0-AbIwjzn5CbvkoFYa8dfIqjGTsiJjpKHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الاعلان عن تشكيل تحالف سياسي في العراق تحت عنوان (تحالف البيان الوطني) يضم تحالف العقد وحركة سومريون ونواب اخرين.</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/naya_foriraq/75736" target="_blank">📅 16:29 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75735">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQOSfA6HDHZqlLmwukJsNjQWHz-Qe-nox2GsxDJdK_Z3oqMglYCIjbGvKHMp4trlfCyd1BHRiOQdRoQaIUYbFwv8clblBBeYEleB9RnzYhOXEk3d9fUOVmLtjpKWFrQ07eyZWAXh7KgZLoJcsMu5V71mFUdMA_LxMqBBoTqrpieevr2wB9ogCoqVDHs0K7d682evtfrW96khtgND6dqOVYNso4E_wq6dVFRCBMGMhhkltRjzb6_ktqMkg9g0V8CCvlgFqb4YJ9u8p8v7737_2p1f7Lqru1pvp2ouzCItSE2EVE79cT9csj-86tqF_xyFH5VwHYHHqyErxLa2Gv_P-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
وزير الخارجية الصهيوني يهاجم بن غفير بعد ان كشف الوجه الحقيقي للكيان: لقد تسببتم عن علم في إلحاق الأذى بدولتنا في هذا العرض المشين - وليس للمرة الأولى. لقد أزلتم جهودا هائلة ومهنية وناجحة بذلها الكثير من الناس من جنود الجيش الإسرائيلي إلى موظفي وزارة الخارجية…</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/naya_foriraq/75735" target="_blank">📅 16:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75734">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJiRU6BtXoXzl9coe9s_jRT63ojy4wrITMAJ0MSt3GWy0wUglqAXF8_QIlmjZ2wi7B8fwNR8ECcyJI-URC4xSRRinrVFWmhKzLahrL5MfJbkKWxm-bTWijSy4ZyKm5XZQANXTPd-McsoZfAQhn2bTyBYw2FzlQXEQStg__eFF0r_zw-z15qZ6qpTCa88lfIasQdWNaZ0xZ0T5CFe5hGd6ZhKEDgIJxpS7-8jqcssRCfJwZPdgT5fvmrH-jq7cXsDOpKiH8Z9PQKvL5XozqCSQYwqYil4Gfm-W_L76WM8sD7GpXfGGC4X-43LrJn_ehZxna923vZq5-lJ0Q--uxRqjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بن غفير يقوم بجولة في ميناء أسدود ويشرف على اعتقال نشطاء أسطول الصمود ويقول: "أدعو نتنياهو أن يعطيني إياهم لفترة داخل السجون".</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/naya_foriraq/75734" target="_blank">📅 16:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75733">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">رئيسة وزراء إيطاليا ووزير خارجيتها: معاملة إسرائيل لنشطاء قافلة كسر الحصار غير مقبولة. نتوقع اعتذارا من إسرائيل بشأن معاملة نشطاء الأسطول</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/75733" target="_blank">📅 15:29 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75732">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">رئيسة وزراء إيطاليا ووزير خارجيتها: معاملة إسرائيل لنشطاء قافلة كسر الحصار غير مقبولة. نتوقع اعتذارا من إسرائيل بشأن معاملة نشطاء الأسطول</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/75732" target="_blank">📅 15:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75731">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🤺
حزب الله:
شاهد من عملية استهداف المقاومة الإسلامية بتاريخ 19-05-2026 منصّة قبّة حديديّة تابعة لجيش العدو الإسرائيلي في موقع جل العلام على الحدود اللبنانيّة الجنوبيّة بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/75731" target="_blank">📅 15:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75730">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سوالف الگهوة
من منزل العامري ، طرح مبادرة اليوم تتضمن صلح وبناء الجدار المتصدع داخل الإطار التنسيقي في العراق..</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/75730" target="_blank">📅 15:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75729">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7c36a9108.mp4?token=EIw77dctHTr2syk4wmQDudVa-cfnr5OLV5jq4EcNGZ4QKQllIO6m_HPXFSr3IpfqApb0rmFEa_bWKDWQQ9ZRO66kJuyY5VkqXoW2zvzQ8ngW5fUzC5enQyieIm6NToGNqz-FlH3gIiovT7Wt-lv9JLJ7n8zfRmlVLvvk2s8hXWqof7c0i1gdcJ1nq9fukEJQBMS3n1DHlt7UcA1TZWTRi-g3f63vOP8-ZTmDH6q4rEodWgBqD_NxTDH4jpTvxMUp76jqUm8ivM9CfMJmfUk_7zhxMipK_jt9Mw9O4N_QUVhk7Ti7Ago9RYxPnvtwzCO2XLKWyX1EYXsYVW_2oDldjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7c36a9108.mp4?token=EIw77dctHTr2syk4wmQDudVa-cfnr5OLV5jq4EcNGZ4QKQllIO6m_HPXFSr3IpfqApb0rmFEa_bWKDWQQ9ZRO66kJuyY5VkqXoW2zvzQ8ngW5fUzC5enQyieIm6NToGNqz-FlH3gIiovT7Wt-lv9JLJ7n8zfRmlVLvvk2s8hXWqof7c0i1gdcJ1nq9fukEJQBMS3n1DHlt7UcA1TZWTRi-g3f63vOP8-ZTmDH6q4rEodWgBqD_NxTDH4jpTvxMUp76jqUm8ivM9CfMJmfUk_7zhxMipK_jt9Mw9O4N_QUVhk7Ti7Ago9RYxPnvtwzCO2XLKWyX1EYXsYVW_2oDldjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
جيش الكيان:
رصدت قواتنا أجهزة مراقبة تابعة لحزب الله في جنوب لبنان داخل مبنى كان حزب الله يستخدمها لمراقبة قواتنا وتوجيه العمليات.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/75729" target="_blank">📅 15:03 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75727">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">وزارة خارجية دويلة الامارات:
نشدد على ضرورة التزام حكومة جمهورية العراق بمنع كافة الأعمال العدائية الصادرة من أراضيها بشكل عاجل دون قيد أو شرط وضرورة التعامل مع تلك التهديدات بشكل عاجل وفوري ومسؤول بما ينسجم مع القوانين والمواثيق الدولية والإقليمية ذات الصلة. كما نؤكد على أهمية اضطلاع العراق بدوره في ترسيخ الأمن والاستقرار في المنطقة، بما يحفظ سيادته ويعزز مكانته كشريك فاعل ومسؤول في محيطة الإقليمي.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/75727" target="_blank">📅 14:41 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75726">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b6bfe77ce.mp4?token=lpKNUYFZksAyi85CYvJl-K8pIsqLNzkQnDilaAGnv4CXFLZrVkiL2uOPIdUL3sPJ_AQhZRRuYCxVjTTgKxnun4vSH7grHs4AkNkvBkEtHyyPH5ie8TnAoJJhRpoio5hQ42XoBQbjpxJFQRzApMNMGe5S06_RxYu0qd5ZfAN0aSR7pv0PRmEn7-Iwc5_Zd6A0ZNJvHptfQGIFRYqU-NWavSQZcbCvptIIDmaZiXOFCcvNBZAZymsjmctX9BADaW6a523wph6eknIbG768hCuAXCOD6ngFSZpuecyzm6Q3Y9XnNa58FFPJOr-daWmFKMDyFRw1_r1TRnDom3tx6yCkSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b6bfe77ce.mp4?token=lpKNUYFZksAyi85CYvJl-K8pIsqLNzkQnDilaAGnv4CXFLZrVkiL2uOPIdUL3sPJ_AQhZRRuYCxVjTTgKxnun4vSH7grHs4AkNkvBkEtHyyPH5ie8TnAoJJhRpoio5hQ42XoBQbjpxJFQRzApMNMGe5S06_RxYu0qd5ZfAN0aSR7pv0PRmEn7-Iwc5_Zd6A0ZNJvHptfQGIFRYqU-NWavSQZcbCvptIIDmaZiXOFCcvNBZAZymsjmctX9BADaW6a523wph6eknIbG768hCuAXCOD6ngFSZpuecyzm6Q3Y9XnNa58FFPJOr-daWmFKMDyFRw1_r1TRnDom3tx6yCkSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بن غفير يقوم بجولة في ميناء أسدود ويشرف على اعتقال نشطاء أسطول الصمود ويقول: "أدعو نتنياهو أن يعطيني إياهم لفترة داخل السجون".</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/75726" target="_blank">📅 14:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75725">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇮🇷
رسالة قائد الثورة الإسلامية السيد مجتبى الخامنئي بمناسبة الذكرى الثانية لاستشهاد الشهيد رئیسي وتكريم شهداء الخدمة
بسم الله الرحمن الرحيم،
إنّ إحياء ذكرى شهداء «رحلة أيّار» (حادثة تحطّم المروحيّة) وفي مقدّمتهم رئيس الجمهورية الشهيد حجّة الإسلام والمسلمين رئيسي، يُعيد إلى الذاكرة استشهاد قوافل خدّام الشعب في جمهورية إيران الإسلامية، من مطهري وبهشتي ورجائي وباهنر، إلى رئيسي وآل هاشم وأمير عبداللهيان ولاريجاني؛ مئات الشخصيات البارزة من الذين تربّوا في مدرسة الخميني الكبير والخامنئي العزيز (أعلى الله مقامهما الشريف)،  وزيّنوا سجلّ الخدمة المخلصة والجهادية لمسؤولي الجمهورية الإسلامية بتوقيعهم المضمخ بالدماء.
ويمكن للمرء أن يعدّ  من الميزات البارزة للشهيد رئيسي: تحمّل المسؤولية، وإفساح المجال للشباب، والاهتمام بالعدالة، والدبلوماسية الفاعلة والنافعة، ولا سيما الطابع الشعبي الذي اتّسم به؛ وقد كانت هذه الخصائص تبعث الطمأنينة في نفوس أصدقاء إيران، ومنهم مجاهدو جبهة المقاومة القوية وكثير من الحريصين على النظام. وكلّ ذلك كان ممتزجًا، بالطبع، بنفحة روحانية متجذّرة في أعماق نفسه.
وأما بشأن العلاقة بين المسؤولين والشعب، فإنّ الخصائص الإيجابية المؤثّرة كانت تؤدي إلى تقدير متبادل. وهكذا جرت مراسم تشييعه إلى جوار مولاه ومخدومه الإمام أبي الحسن الرضا صلوات الله وسلامه عليه، بمشهد مهيب قلّ نظيره. وقد شكّلت الفترة غير المكتملة من رئاسته للجمهورية معيارًا لقياس حجم الجهد والحرص على الشعب والبلاد، مع الحفاظ على استقلالها.
واليوم نقف أمام الملاحم التي سطّرها الشعب الإيراني في مقاومته التاريخية الفريدة بوجه جيشين إرهابيين عالميين. وهذا الأمر يزيد من أعباء التكليف الملقى على عاتق مسؤولي الجمهورية الإسلامية - من القيادة ورؤساء السلطات إلى جميع مستويات الإدارية ـ أكثر من أيّ وقت مضى. واليوم، فإنّ شكر نعمة الانسجام بين الشعب والحكومة وسائر أجهزة الجمهورية الإسلامية، يكمن في تعزيز دوافع المسؤولين ومضاعفة خدمتهم وجهادهم، والعمل على حلّ مشكلات البلاد ، ولا سيّما في المجالين الاقتصادي والمعيشي، والحضور الميداني والمباشر، وتعريف دور جادّ للشعب الناهض بمسار تقدّم البلاد والتحرك بأمل نحو المستقبل المشرق.
رحمة الله ورضوانه على شهداء طريق الخدمة، ولتكن النصرة الإلهية ودعاء سيّدنا عجل الله تعالى فرجه الشريف سندًا لخدّام الشعب الإيراني المسلم.
السيد مجتبى الحسيني الخامنئي
20 أيار/مايو 2026</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/75725" target="_blank">📅 14:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75724">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دوي انفجارات في محافظة السويداء جنوب سوريا</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/75724" target="_blank">📅 13:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75723">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">إعلام إيراني عن مصدر بإسلام آباد: وزير الداخلية الباكستاني توجه إلى طهران للقاء مسؤولين هناك</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/75723" target="_blank">📅 12:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75722">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‏الجيش الأردني يدعي إسقاط مسيرة في جرش دخلت الأجواء الأردنية</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/75722" target="_blank">📅 12:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75721">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">إعلام خليجي عن ‏مصدر دبلوماسي: تضارب المواقف بين إيران وباكستان حول قنوات التفاوض ومكان المحادثات</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/75721" target="_blank">📅 12:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75720">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇮🇹
إيطاليا الدولة الـ19 التي تشغل طائرة التزود بالوقود A330.
وقعت إيطاليا صفقة بقيمة 1.4 مليار يورو مع شركة "إيرباص" لشراء ست طائرات تزود بالوقود من طراز A330 MRTT - مما يؤدي إلى إلغاء طلبية شركة "بوينج" لطائرة KC-46 Pegasus، التي اختارتها روما في الأصل في عام 2022 قبل إلغائها فجأة في عام 2024.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/75720" target="_blank">📅 12:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75719">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا احتياط</strong></div>
<div class="tg-text">🇮🇶
إلغاء القرار المتعلق بفرض مبالغ تحت مسمى "أجور خدمة" على شركات الهاتف النقال</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/75719" target="_blank">📅 11:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75718">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇱🇹
أ ف ب: إغلاق مطار فيلنيوس في ليتوانيا بعد الاشتباه بطائرة مسيرة</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/75718" target="_blank">📅 11:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75717">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db7a1d74fb.mp4?token=n4o39UIQdML4xUx7FCS7n--BHjzrX12jtyN9X8PuVFlm0F2hqCSch4R_JJoGwS03ITmfZJboPEEZsTFV2Yn4h0pzPjXqUVFqIuTm1YKRANzzPNc3HVFGv-9WOpTEn2K1UGu_145Ov00Xk-OjEpTaiVx8Xh09R2BmCTBdTKDK_xQaMTlfzHp0HSh1DB45xnz9LTVjcrUkD8fhfjaQFPt2286Aa8LH39mFx7NoUg51xSJOLpaDKPY6lHhdyQaPWuhuQv9-QjRwgR7SwJV1emWBpztVP5Knre3xYGbwvxhf0VLyOGh_TR6VClcE4hqhMKCIrVT_eVb9V7UvxaZUDc1uwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db7a1d74fb.mp4?token=n4o39UIQdML4xUx7FCS7n--BHjzrX12jtyN9X8PuVFlm0F2hqCSch4R_JJoGwS03ITmfZJboPEEZsTFV2Yn4h0pzPjXqUVFqIuTm1YKRANzzPNc3HVFGv-9WOpTEn2K1UGu_145Ov00Xk-OjEpTaiVx8Xh09R2BmCTBdTKDK_xQaMTlfzHp0HSh1DB45xnz9LTVjcrUkD8fhfjaQFPt2286Aa8LH39mFx7NoUg51xSJOLpaDKPY6lHhdyQaPWuhuQv9-QjRwgR7SwJV1emWBpztVP5Knre3xYGbwvxhf0VLyOGh_TR6VClcE4hqhMKCIrVT_eVb9V7UvxaZUDc1uwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
هبوط مروحية عسكرية في مستشفى رمبام على متنها عدد من الإصابات في صفوف جيش الاحتلال جراء إصابتهم جنوب لبنان</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/75717" target="_blank">📅 10:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75716">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vP84Skl6i928H4vDc3DfLLDMjPzDMOYtKTxH4ex4hhVuEtiBPvQ0CyD-_DXfliTqsPnECgwbQCDihRje8ow-SlCq6kzPQJMC-lExf1KlsPgwUMD0KW0kJpgIWRbrU_Ntr4NzU7naKnUlfWpmA4leelvmgIbnU8POc24u-TfgBP69eWuXcOIlVGT1J8_S8XXNgn8i7agtheDIQZxMEezDFXwguTE6jym1UVIalAlv3a55z9ErJ0ls3khU0ODJ-yd9sE1ToRgwCbkDn2wjpEMk4Mh3vzgo2BcO_LdHpS-ST0F1bMTPv-22hoJkuTWbFG8nS9vhKKKLqLh9OmWqP8QN-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
🇸🇾
الدفاعات الإسرائيلية تعترض مسيرات في سماء محافظة درعا جنوب سوريا.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/75716" target="_blank">📅 09:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75715">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">زلزال بقوة 5.6 يضرب شمال سوريا وتركيا.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/75715" target="_blank">📅 09:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75714">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKoy1UntyaBdw2d8vgl0OIpipZY5bSzC-D6XcmCAu1d7cONUyQtnbloNETX3kLSTM5G6JL9NbndAixX0iYeWpUTmqmsu5F0Ck6-gjYe47WN8zsp1gUp7H36Uiz8v4zPkbJYnCvNqdCcYyDvyxdibd8TD4iWo4zOJbpkUfTgJzF7X4oeUWrzL5frdta8c6Lr1EFrybEL2MluyvPmYG2E6qEouDKO7sP13Tyty6kxlWSAlD56V9EPoXkaHvl8JGyBdxNQ8s6Nd3z5Ewtrx4EVHqrLGR8K_sRT8uN7lY2Ffcq--ZJ3HPtx6FdlXWa3iO5bFnXbORm-XwSL7EOgzzSqOqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نيوورك تايمز: يخطط الاتحاد الدولي لكرة القدم (FIFA) لحظر المشجعين مرة أخرى من إحضار علم "الأسد والشمس" قبل الثورة الإيرانية والملابس ذات الصلة إلى ملاعب كأس العالم خلال بطولة 2026.  تم أيضًا تقييد العلم في كأس العالم قطر 2022.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/75714" target="_blank">📅 01:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75713">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLahdOJ-mNArpLLsce7g98tALbqNoD2LVY0Jron_qgQuUgI98S56aw-QxXAwy2ble05zyfrafRXriVMPn7_3t-DrS1g6tB8tStQgPi8-Prd80xBLFTMt1-5wZBuG9eoO1tcwDuw0lToXhedbTb3wr944iiIixPzUOYEo-FFTxjbNaXzbv2f70kMSnfG5gpH7MeY0HAA46b4OHrK7uZDXWMjnWV0hiZ4ADeXNzoI6IsJGXEQh3ju_lCQD0pq3nsmyMbaQoUcGcvLIYTvMR-FsR3B6w6qBqCYsj_qb13FqVx3Fu1cKE4hbN8YqJ1ETdcs6cORSjWJt9UDw6sYuKmHXJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجولاني يشكر دونالد ترامب على “كرمه الزايد حيل” بعد إهدائه شيشتين عطر، ويعتبرهن “الأساس المتين” للعلاقات السورية الأميركية، وسط ترقب شعبي لمعرفة إذا المرحلة الجاية تشمل بخاخ جسم لو مزيل عرق دبلوماسي.
القدس تنتظرنا يا اخوة
😄</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/75713" target="_blank">📅 00:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75712">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFTZ0krJ6fwyJ3FWftT414Gev9VrodS0TWLcBhpdN3Bj8SrNcfG-AnRaYeqwcCSC9Fpnkyom0wKnTPWLPo45tF_4k-hAJ73Mu7HU__cuK0Odh5_J-8qOXvkCrRljC3EsMqANNT3gp2_r_i4frrgJlkWMcMxLvj8B3KpEH0zFR99O5CkaEx-ErDanVoMNeh9YNzCBGoUY7VpJwFRVot9fzVWRWArvBlWPdicA8Y1j9jZmqFJK25IYN1-iyALvcFJ4M4woin3jWITBDcJW27H2qsHByCGXveSTlio416DqJgVO-XWMmgtUNJCIyu7fO0ckg4Vz3ufzBZxpc8i3JOYyUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقجي:
بعد أشهر من بدء الحرب على إيران، يعترف الكونغرس الأمريكي بفقدان عشرات الطائرات التي تبلغ قيمتها مليارات الدولارات.
تم تأكيد قواتنا المسلحة القوية كأول من يضرب طائرة F-35 التي توصف.
مع الدروس المستفادة والمعرفة التي اكتسبناها، ستضم العودة إلى الحرب العديد من المفاجآت.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/75712" target="_blank">📅 00:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75711">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🌟
🏴‍☠️
قوات حزب الله البطلة تشتبك مع عناصر جيش العدو في بلدة حداثا بجنوب لبنان وتتمكن من إستهداف وإحراق دبابة ميركافا وإصابة عدد من الصهاينة والمعارك مستمرة حتى اللحظة.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/75711" target="_blank">📅 00:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75710">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🌟
🏴‍☠️
قوات حزب الله البطلة تشتبك مع عناصر جيش العدو في بلدة حداثا بجنوب لبنان وتتمكن من إستهداف وإحراق دبابة ميركافا وإصابة عدد من الصهاينة والمعارك مستمرة حتى اللحظة.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/75710" target="_blank">📅 00:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75709">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cbad0422a.mp4?token=FN8CLgsKuAMRwDllRhCm-MfogZ2IvjxATLEGwB8g52epIV_ndx881EhAZ2_7CweT7vHukzaLzrJcKSs7e8Usf9Eu6mE5UrahOHQZKfBHsZGO5XT86y3Z_a_Zh_U7osmg_adIFcCHLcTO-1SkJNqkIMpgeB-P_qbOCXnh41BLQcPdV8rLeiA0caToR2UZAF4QP-ylRKNT6gJb--FPJNdNs6z9TjsFW8iwyquy-um3nrTUwOuWFrNHB3yCGYWWhd_TDN6qt9SLuaeiFFoazgu51aR5-P8CQGM42EJaTsygfO8cGaoe--8L4xTXd1TABE6c-zZlgaZca2gAXCqjDXO-nJV7NP5Yr3Wq6M5PdGbEkgCqqc5sgR2rwbDxAR4GTUB_BVgcO7G8x2sa0qI6HyjhuLo1GCR1URRapyaANdvj8RKvzEt0DYgq48VEerag_8yiyrZtt31cxRYVHFp5WqOZzaMxkEhBPFY-fZAm0FIehsFO5kVgmpbVGe9gNrBgLF-DTv9DqrpICL9T1je1yl82nvM4utrwm6tICtqUGWVuISDHv5zVVsHp6BScqKQLZ9082gB7w_HnjLr9oKfDXdBCHuikrLxwPMN-mvI8a7v9WTgr03pZZoLeUD5vU1qxUmHZxCbP9gi0f5cyGjnf3V3NbKZnC1MQTtrBEeqOMtxC19o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cbad0422a.mp4?token=FN8CLgsKuAMRwDllRhCm-MfogZ2IvjxATLEGwB8g52epIV_ndx881EhAZ2_7CweT7vHukzaLzrJcKSs7e8Usf9Eu6mE5UrahOHQZKfBHsZGO5XT86y3Z_a_Zh_U7osmg_adIFcCHLcTO-1SkJNqkIMpgeB-P_qbOCXnh41BLQcPdV8rLeiA0caToR2UZAF4QP-ylRKNT6gJb--FPJNdNs6z9TjsFW8iwyquy-um3nrTUwOuWFrNHB3yCGYWWhd_TDN6qt9SLuaeiFFoazgu51aR5-P8CQGM42EJaTsygfO8cGaoe--8L4xTXd1TABE6c-zZlgaZca2gAXCqjDXO-nJV7NP5Yr3Wq6M5PdGbEkgCqqc5sgR2rwbDxAR4GTUB_BVgcO7G8x2sa0qI6HyjhuLo1GCR1URRapyaANdvj8RKvzEt0DYgq48VEerag_8yiyrZtt31cxRYVHFp5WqOZzaMxkEhBPFY-fZAm0FIehsFO5kVgmpbVGe9gNrBgLF-DTv9DqrpICL9T1je1yl82nvM4utrwm6tICtqUGWVuISDHv5zVVsHp6BScqKQLZ9082gB7w_HnjLr9oKfDXdBCHuikrLxwPMN-mvI8a7v9WTgr03pZZoLeUD5vU1qxUmHZxCbP9gi0f5cyGjnf3V3NbKZnC1MQTtrBEeqOMtxC19o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انيميشن بأسلوب الليغو يوثّق المسار الذي خاضه رئيسٌ شعبيّ للجمهورية الإسلامية الإيرانية
نُشر بمناسبة ذكرى استشهاد الشهيد رئيسي ورفاقه الشهداء</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/75709" target="_blank">📅 23:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75708">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇺🇸
حاكم كاليفورنيا:
إنهم يحاولون تزوير الانتخابات. دونالد ترامب يعلم أنه سيُهزم بشدة في شهر تشرين الثاني.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/75708" target="_blank">📅 22:22 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75707">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
انتحار جندي من الجيش الإسرائيلي داخل دورة مياه في "الكرياه" بتل أبيب.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/75707" target="_blank">📅 22:13 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75706">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🌟
🏴‍☠️
مراسم تنكيس علم العدو الإسرائيلي الغاصب في مقر اللواء 226 التابع لجيش العدو في بلدة البياضة جنوبيّ لبنان بتاريخ 17-05-2026</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/75706" target="_blank">📅 22:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75705">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">⭐️
وول ستريت جورنال:
‏احتجزت الولايات المتحدة ناقلة نفط مرتبطة بإيران في المحيط الهندي ليلاً، في الوقت الذي يهدد فيه ترامب باستئناف الضربات العسكرية على إيران.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/75705" target="_blank">📅 21:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75704">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇺🇸
‏
جي دي فانس:
خياران أمام إيران إما الاتفاق أو استئناف الحرب.
نعتقد أن الإيرانيين يريدون إبرام اتفاق لكن نؤكد أنه لدينا دائما خطة بديلة.
‏لا أحد يريد عودة الحرب والفرصة متاحة أمام إيران.
إيران بلد معقد للغاية ونرى مواقف متشددة من جانب فريقها المفاوض.
أوضحنا للإيرانيين خطوطنا الحمراء.
لا أعتقد أن الإيرانيين سيكونون متحمسين لنقل ما لديهم من يورانيوم مخصب لأمريكا أو روسيا.
مخططنا ليس نقل اليورانيوم الإيراني المخصب إلى روسيا ولم يكن ذلك أبدا ما نخطط له.
لا نريد فقط التزاما من الإيرانيين بعدم امتلاك سلاح نووي بل بألا يعيدوا بناء قدراتهم النووية مستقبلا.
هذه ليست حربًا أبدية. سنتولى الأمور ونعود إلى ديارنا. هذا ما تعهد به ترامب، وهذا ما سيحققه.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/75704" target="_blank">📅 21:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75703">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🏴‍☠️
‏
هيئة البث الإسرائيلية:
الاستعدادات الأميركية – الإسرائيلية لاستئناف الحرب ضد إيران اكتملت.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/75703" target="_blank">📅 20:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75702">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QxupKaMIzjUwkIl9yh1wMmT5MJ7_1bwpleL1Uc4mRk1hqZg-kW1WUnVDj1iUeAuDmbMiO2lWhTUXYcYbfAKbkid9B0JMQBovTLBySIZ5_lkFFMVAyIeobrY9E0NyrMZV4JsqHApbjQQ_q6EHM8ftr9oUAogP_rEJP2ng19GFYs4tp_CNDt4M-34XxcodWQUDwFllrnM9v8seBBcv0YlxIzJpuU8phHwweMvimtfxU9BmZsqzI0gIzjMnlo4vjXdfodbKNS7DB1U4qWJi097mInVMzebq6ue4JwX81va_rQgRP14Ygrc8UTDFinco66Ku4MX-_0cITNHPXZIfR6p9yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
وزير السيد مقتدى الصدر ينشر عبر حسابه الشخصي.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/75702" target="_blank">📅 20:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75701">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‏ اعتقال موظفة في السفارة الأمريكية في بغداد تدعى قند محمد فرج ذياب الجنابي بتهمة الرشوة والفساد !!!!
‏</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/75701" target="_blank">📅 20:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75700">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">حدث امني خطير في بغداد</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/75700" target="_blank">📅 20:23 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75699">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZeQZydF8395p5OhQDOIWw9XLPrU9-zsKbToK4HZgSXEEj-MmlILrdxTzrmA3BBpsrv22V3qnRjO5nrTp4excIElZqojt7nZZhbzAH2PmyMXlcoIoSeNJgWS8vzdfgW7AA9Sd-G1YxvpuMeyPwAACHWWqTMYYySzoImnkn2PWTCUTycTAYDAODoNk8fiQLHobeEl9Z_p11rOhNYv_bAbVPh6eZ_Cd1E4UGg83z2D8zi6-tz0hcze_HUtqOXGoYBLEyQIiQkDF0rob1tmzqawE5bPiUwG-3BnQomSt7QLcF5uVguICZAaZedIuxHkJqkMi1WRg_44itaGTN65P9mqxzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
مقتل جندي إسرائيلي في جنوب لبنان.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/75699" target="_blank">📅 20:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75698">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🌟
حزب الله ينشر:
ترقبوا... مراسم تنكيس علم العدو الإسرائيلي الغاصب في مقر اللواء 226 في البياضة.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/75698" target="_blank">📅 19:14 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75697">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">⭐️
ذا أتلانتيك:
اصطدمت طائرتان لإعادة التزود بالوقود من طراز KC-135 Stratotanker فوق غرب العراق في 12 آذار خلال الحرب الأمريكية-الإسرائيلية ضد إيران، مما أدى إلى مقتل ستة من أفراد الخدمة الأمريكية بعد تحطم إحدى الطائرتين بينما تمكنت الأخرى من الهبوط مع أضرار شديدة في الذيل.
صرحت قيادة مركز القيادة المشتركة (CENTCOM) علنًا أن التصادم وقع في "مجال جوي صديق" ولم يكن بسبب نيران معادية. ومع ذلك، تظهر تقارير المخابرات الأولية أن نشاطًا مضادًا للطائرات تم اكتشافه من ميليشيات مدعومة من إيران في المنطقة في وقت تحطم الطائرة، مما يثير احتمال أن يكون الطيارون قد اتخذوا إجراءات تفادية قبل التصادم.
رفضت قيادة مركز القيادة المشتركة (CENTCOM) لاحقًا هذه التقارير، مستنتجة أن الإطلاقات المكتشفة كانت على الأرجح صواريخ موجهة إلى أهداف أرضية وليس طائرات.
من المتوقع أن يحدد تحقيق مستمر لسلاح الجو الأمريكي ما إذا كان الحادث كان خطأً يمكن تجنبه من قبل الطيارين بسبب ازدحام المجال الجوي بدلاً من عمل العدو.
شمل الأفراد الستة الذين قُتلوا ثلاثة طيارين في الخدمة الفعلية من السرب السادس لإعادة التزود بالوقود في فلوريدا وثلاثة من أفراد الحرس الوطني للطيران في أوهايو من السرب 121 لإعادة التزود بالوقود.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/75697" target="_blank">📅 19:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75696">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c6863208b.mp4?token=pONWCkF4j6-ZqBxdz4O1rLUsqr-m8BjBE9pUhxAEFwjMXYaq831OsZlvUPooJNlJP4E0sXzoWDunXZ3cmqCbaXbX_2sWxcsRLCamDjJ2vX22CzXqZMtTWZOjgHwy_ufTi_dw6QNZwVV9_2loBlqcn7M2Yts1O666IXOx_ZjUNABR-J1aqujt3OfkAIb98kXUM_pUnem03WR5KM3FEgTCysPvfPBiH1R8X_df3RdDrlIjISyZpmwb6ps8dguhMaoiUJahdVhqfQxaT5EttvDamVsnlmfuQdPnmeCFh3yapQMUQgPuikPxQ6BnXLHylprYLkOjzYAEG9Y2pEuFMX6fi6nAv-T_SgOwLNXMxidaFirY7-W8RJ4mwv6Hq3csdPDvHxKRBky-tYpfEvjIARUe2S_0fXTeDrHw8Ocy4l2p4tEGSjRM4vGdA-GvaiNeV4f1zgg-lWI2GVLtUhdNYcmc4-dKfqaDyJvfhR39yI0r8Hr54x4VXO1ZC4RGB_1FbZN1WLOqU1QBtxgxZRqWASvaX8EzSEVpY9VULq2iCZCDnFLqt8dMpsx6Ny5bmQvgkYOebMD6hvMBAVM0EJXLdDpXkYI8gCzK9UQBb3cACG5HyPl4AI3becBTHlrLYM84DVHc7C0B6O8exlKPrHpzP0ri-feWnibr2PpewIPcb8FUbX0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c6863208b.mp4?token=pONWCkF4j6-ZqBxdz4O1rLUsqr-m8BjBE9pUhxAEFwjMXYaq831OsZlvUPooJNlJP4E0sXzoWDunXZ3cmqCbaXbX_2sWxcsRLCamDjJ2vX22CzXqZMtTWZOjgHwy_ufTi_dw6QNZwVV9_2loBlqcn7M2Yts1O666IXOx_ZjUNABR-J1aqujt3OfkAIb98kXUM_pUnem03WR5KM3FEgTCysPvfPBiH1R8X_df3RdDrlIjISyZpmwb6ps8dguhMaoiUJahdVhqfQxaT5EttvDamVsnlmfuQdPnmeCFh3yapQMUQgPuikPxQ6BnXLHylprYLkOjzYAEG9Y2pEuFMX6fi6nAv-T_SgOwLNXMxidaFirY7-W8RJ4mwv6Hq3csdPDvHxKRBky-tYpfEvjIARUe2S_0fXTeDrHw8Ocy4l2p4tEGSjRM4vGdA-GvaiNeV4f1zgg-lWI2GVLtUhdNYcmc4-dKfqaDyJvfhR39yI0r8Hr54x4VXO1ZC4RGB_1FbZN1WLOqU1QBtxgxZRqWASvaX8EzSEVpY9VULq2iCZCDnFLqt8dMpsx6Ny5bmQvgkYOebMD6hvMBAVM0EJXLdDpXkYI8gCzK9UQBb3cACG5HyPl4AI3becBTHlrLYM84DVHc7C0B6O8exlKPrHpzP0ri-feWnibr2PpewIPcb8FUbX0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇨🇳
لحظة وصول الرئيس الروسي فلاديمير بوتين إلى بكين، واستقباله من قبل وزير الخارجية الصيني وانغ يي.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/75696" target="_blank">📅 19:09 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75695">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzkgkW1KOAeLWZoDLhyuX76mPcECS6sPcPhh81Qy16YnX0oogh9Und8FtKTHFFfubC4z12zS4LHEbMiKrLHH5BMmeQOsB8P6wRSj_JkX3SUELL2PKfchTXFfj6dy_NOXuL15lGvt0Rab0Y3qiLcZxLG2ladtlRHOStQRngsQ0ZrRlfmKStsxd_n56vdncltDWYJym4ioYpjH5b82FsdCGCmYYCkZlvRqCPmtiIgt_WP6Luf6depB21scd6B8KfobLucc--EIEGtblzO7YMyvE2l4wUS-YdNKCNMYtWRKiLEnvTflXp81Rdh09vIoWaeODdaPUqliaDKX8yPaoEJ8qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
رد قائد الثورة الإسلامية على رسالة جمعٍ من الناشطين الشعبيين في مجال السكّان:
أشار قائد الثورة الإسلامية، آية الله السيد مجتبى الخامنئي،  في معرض رده على رسالة الإعراب عن المحبة والتعزية المرفوعة من قِبل جمعٍ من الناشطين الشعبيين في مجال السكان بمناسبة استشهاد قائد الثورة (قدّس الله نفسه الزكية)، إلى مسألة زيادة السكان وارتباطها بقوة إيران الإسلامية وحضارتها، مؤكدًا على تكثيف الجهود المتزايدة للناشطين الشعبيين في هذا الحقل وضرورة ترويج ثقافة الإنجاب.
🔻
وجاء نص رد قائد الثورة الإسلاميّة، الذي نُشِر بمناسبة اليوم الوطني للسكان، على النحو الآتي:
📖
بسم الله الرحمن الرحيم
بعد توجيه التحيّة والشّكر على إعرابكم عن المحبة والشعور بالمسؤولية، أيها الناشطون المُخلصون في مجال السكان؛ فإنّ من بين الإنجازات القيّمة للدفاع المقدس الثالث، والنعمة العظيمة لبعثة الشعب الفريدة التي تجلّت للجميع، صعود إيران إلى مستوى قوة كُبرى ومؤثرة. ولا شكّ في أن استمرار هذا الوضع وبلوغ مستوى أفضل منه، يرتبط ارتباطًا مباشرًا بقضيّة السكان.
▪️
إنّ قضية وجوب زيادة عدد السكان يُنظر إليها من منظار تعويض النقص الناجم عن بعض سياسات الماضي؛ ولكن إضافة إلى ذلك، فإنه من خلال المتابعة الجادة للسياسة الصحيحة والحتمية لزيادة عدد السكان، سيكون الشعب الإيراني العظيم قادرًا في المستقبل على خوض غمار أدوار كبرى وطفرات استراتيجية، وقطع خطوات واسعة في اتجاه إرساء الحضارة الحديثة في إيران الإسلامية. ومن هذا المنطلق، فإن الجهود المتزايدة للناشطين الشعبيين في مجال السكان وترويج ثقافة الإنجاب، يمكن أن يكون لها أثر بالغ الأهمية في سبيل تأمين هذا المستقبل المشرق.
⏺️
ومن جهة أخرى، فقد كان هذا الأمر أحد أهم هواجس قائدنا العظيم الشهيد (أعلى الله مقامه الشريف)، الذي طالما أكد عليه في الكثير من اللقاءات، والمداولات، والاجتماعات العامة والخاصة، ولا يزال يُعدّ من أهم القضايا الاستراتيجية للنظام. يُؤمل أن تؤدي جهودكم المخلصة، أيها الأعزاء، في ظل الدعاء المستجاب لسيدنا (عجل الله تعالى فرجه الشريف) إلى نتائج مثمرة، إن شاء الله.
✍
السيد مجتبى الحسيني الخامنئي
🗓
19 أيار/ مايو 2026</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/75695" target="_blank">📅 19:02 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75694">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60e2efce8f.mp4?token=reKCLrxjvBwhVc2PdKA2Cx2CAUdFgCjvRsWK9GLYQ1VuJjbFY7zbG_pBS0FF5DrjTsQjZMA-SxV-EZF5cJvFOpA87m88QBAfQ1YNfBtfKJskSjwRMnVtdBj3em1ilU3378L9fe0PoCuTHKaOKkDhrH909flotfqLFpTnduvlQfp4Y0nwYX5Toa9WomW8IjyOrJBjLEq_m_dkrmodNwGdCxjetksHXxATyLC-4gm7KyD84d649WA7j4EFcA86f6ZWnxOZ-HPL58BcJ-zX7EN9K03TWwvxkpb3PSscmfmVdTrC6ohYEhXc0pMCVbj7oPEn-bJiZ6lUVacMopHg2Uk_ngUJl35RwVb_N_uVs-RawvOh_qz2rWLM6KIk7jvkUQEhpfuzW-orRt2thDEZ8ecm0h6t57yC97eR0bUh5hIujsto4QTgOfZLcjlWby5EYuRmEEYZRUg0VfeCR2OT1TsZen7xPDfsmCoE1zjujaG8x5N85489DwHHBzCmmYCtVYKVNrD918iDpV-uXEEZKVi3TtaZaSXBqMmiwmAT03zpCEWaUhMIq2Looc7_zpSG-qfzWMmfdF4FHXreLMIdRKjiH-yYK6g1OO5Ne5S8XJPDazxqo7ZFpSiLrC6q_47b_5D03ucUkwkHMQyIehJPZMw2s9T8AukJ74OBNUo8W_mmNno" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60e2efce8f.mp4?token=reKCLrxjvBwhVc2PdKA2Cx2CAUdFgCjvRsWK9GLYQ1VuJjbFY7zbG_pBS0FF5DrjTsQjZMA-SxV-EZF5cJvFOpA87m88QBAfQ1YNfBtfKJskSjwRMnVtdBj3em1ilU3378L9fe0PoCuTHKaOKkDhrH909flotfqLFpTnduvlQfp4Y0nwYX5Toa9WomW8IjyOrJBjLEq_m_dkrmodNwGdCxjetksHXxATyLC-4gm7KyD84d649WA7j4EFcA86f6ZWnxOZ-HPL58BcJ-zX7EN9K03TWwvxkpb3PSscmfmVdTrC6ohYEhXc0pMCVbj7oPEn-bJiZ6lUVacMopHg2Uk_ngUJl35RwVb_N_uVs-RawvOh_qz2rWLM6KIk7jvkUQEhpfuzW-orRt2thDEZ8ecm0h6t57yC97eR0bUh5hIujsto4QTgOfZLcjlWby5EYuRmEEYZRUg0VfeCR2OT1TsZen7xPDfsmCoE1zjujaG8x5N85489DwHHBzCmmYCtVYKVNrD918iDpV-uXEEZKVi3TtaZaSXBqMmiwmAT03zpCEWaUhMIq2Looc7_zpSG-qfzWMmfdF4FHXreLMIdRKjiH-yYK6g1OO5Ne5S8XJPDazxqo7ZFpSiLrC6q_47b_5D03ucUkwkHMQyIehJPZMw2s9T8AukJ74OBNUo8W_mmNno" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
12-05-2026
دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في بلدة البيّاضة جنوبيّ لبنان بصاروخٍ موجّه.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/75694" target="_blank">📅 19:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75693">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇺🇸
🇮🇷
قائد القيادة المركزية الأمريكية:
القوات الأمريكية تعرضت في 7 إبريل لإطلاق نار من إيران وقمنا بالرد.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/75693" target="_blank">📅 18:46 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75692">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇺🇸
ترامب: ‏الجميع يقول لي ان الحرب على ايران غير شعبية، لكنني أعتقد أنها تحظى بشعبية كبيرة. عندما يسمعون أنها تتعلق بأسلحة نووية قادرة على تدمير لوس أنجلوس، عندما نشرح الأمر للناس - ليس لديّ الوقت الكافي لشرحه لهم.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/75692" target="_blank">📅 18:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75691">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc14bff42.mp4?token=J71TU5xmyN672tMq7ieFnaOWG64bshpOe7brPZKw-97qqbGQl1M6vTTx1Za5lSdNEMKUmSENUavTKhX6zLLAKyL_9YydgC6-allyi5y136oVvFEVVUG-CzTToo1r1o8G14kruuyAwphsKh3X2ipp_yVxxXkTA16Jl156scQEJssGe37aVg1jASu_wQUi_xqQjs_zbDf26oDNi42GyhEXFmrkqHnp9Zq8_6UGnA9RJht-D1peXZbBP4QmRxSCglj36CHsUdPnhQU089NtdFc0z-SZJ4882Q6cLNZrcJQnoYa_MNynR7FWlf8cktIeSGywsxZgBVG8eeTZjLY8aCQrSIhsQbVjdApInVhLt89IswaqVj2n7sqImR_Js2ucmE4RwkJq3QPt4qfJ5_iXywqZztFfTYNwpWiOe6XGxhQW4OX0b1-S5g2w39kEauPuXyWk0DXIxm9WprpyFh8clgFHsRdlhAql4KFlrSn64maEitQLmMSP5C3OmvyvGZsTidRultiqPYx1G2xJUfrX9p5XRrHM129NrAq-A-tRPopDXR_JJVSbeEAo-sT236DRHLCepzOg7bqzHYxDEfKncZ0jm6vadRXKIuLJmfhnlA0IgSO785NRjjx0DjfyOFIuqc3Qz7cWdZ_Q65uR6hUvYdPSTqd_Vj7-Rlp3lZ06yuYBHO4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc14bff42.mp4?token=J71TU5xmyN672tMq7ieFnaOWG64bshpOe7brPZKw-97qqbGQl1M6vTTx1Za5lSdNEMKUmSENUavTKhX6zLLAKyL_9YydgC6-allyi5y136oVvFEVVUG-CzTToo1r1o8G14kruuyAwphsKh3X2ipp_yVxxXkTA16Jl156scQEJssGe37aVg1jASu_wQUi_xqQjs_zbDf26oDNi42GyhEXFmrkqHnp9Zq8_6UGnA9RJht-D1peXZbBP4QmRxSCglj36CHsUdPnhQU089NtdFc0z-SZJ4882Q6cLNZrcJQnoYa_MNynR7FWlf8cktIeSGywsxZgBVG8eeTZjLY8aCQrSIhsQbVjdApInVhLt89IswaqVj2n7sqImR_Js2ucmE4RwkJq3QPt4qfJ5_iXywqZztFfTYNwpWiOe6XGxhQW4OX0b1-S5g2w39kEauPuXyWk0DXIxm9WprpyFh8clgFHsRdlhAql4KFlrSn64maEitQLmMSP5C3OmvyvGZsTidRultiqPYx1G2xJUfrX9p5XRrHM129NrAq-A-tRPopDXR_JJVSbeEAo-sT236DRHLCepzOg7bqzHYxDEfKncZ0jm6vadRXKIuLJmfhnlA0IgSO785NRjjx0DjfyOFIuqc3Qz7cWdZ_Q65uR6hUvYdPSTqd_Vj7-Rlp3lZ06yuYBHO4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: تلقيت مكالمة يوم امس وقالوا لي "سيدي هل يمكنك الانتظار؟ نحن قريبين من صفقة"  سأمنح إيران مهلة يومين أو ثلاثة ربما حتى الجمعة أو السبت. فترة زمنية محدودة.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/75691" target="_blank">📅 18:16 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75690">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3bf75e59c.mp4?token=J83SwYY9YIkUQGmSejsBWWu6YhxW17PPG6PL9WX8oDiBqYiR0DWa0398PPsvlY0y68m-mPrj2siKf_hpQD82kCbFxr7HZx_ZmHesFeW4bXB_4aimFZs3NTkCqXSPuyfYK2D0az91OGdOtbEgU-oyWb9uWIeKSNBlL0IAW220mVio2n7JzeL7NrNp02ui6N0_OO8HzREpFD7iOb2XZ4BNXKfVWe5I1BlMCj9B_i-dRhwUAbHCHvsYqMI9I54qxvhEjpkW5GFmu_IEEKgrHTYWxAYtm47DeUv9JKqyvaHXJQmsplfqN6yJnfB-m48YvENY5QPniPa1jRfmt_gz8bbYwa_VKGKkKwi_eED8vD5_udL-dIVzoei8v3Z4betnn8yXERwd0YQ0hGj9-H0pM29cXlovuKf_31-IrP5zajNzV9dRWy5sgr6pPpzeGfLSEHL11zWt2Fv_ywQefJ4eS3HyFERRx9LwCk2v7hpU6t6p4-jcjynfLI7b_awaTnZ4yrdYRh_0ddc2D8iL1fSLkEI_2VqDWv1DWG8CdT4mF1KHop9aAiGxYO30CibrWu5tgggI4NAiEDLASrI8OOP-bFWJH21M9DBaRxqUnRwlk2ofT3gNbcEzTo0vd0VPqyR7Sp1wCKCiA2Iyv1mHESqXyKJarP4AsqgdS_zTW4laaFe1uec" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3bf75e59c.mp4?token=J83SwYY9YIkUQGmSejsBWWu6YhxW17PPG6PL9WX8oDiBqYiR0DWa0398PPsvlY0y68m-mPrj2siKf_hpQD82kCbFxr7HZx_ZmHesFeW4bXB_4aimFZs3NTkCqXSPuyfYK2D0az91OGdOtbEgU-oyWb9uWIeKSNBlL0IAW220mVio2n7JzeL7NrNp02ui6N0_OO8HzREpFD7iOb2XZ4BNXKfVWe5I1BlMCj9B_i-dRhwUAbHCHvsYqMI9I54qxvhEjpkW5GFmu_IEEKgrHTYWxAYtm47DeUv9JKqyvaHXJQmsplfqN6yJnfB-m48YvENY5QPniPa1jRfmt_gz8bbYwa_VKGKkKwi_eED8vD5_udL-dIVzoei8v3Z4betnn8yXERwd0YQ0hGj9-H0pM29cXlovuKf_31-IrP5zajNzV9dRWy5sgr6pPpzeGfLSEHL11zWt2Fv_ywQefJ4eS3HyFERRx9LwCk2v7hpU6t6p4-jcjynfLI7b_awaTnZ4yrdYRh_0ddc2D8iL1fSLkEI_2VqDWv1DWG8CdT4mF1KHop9aAiGxYO30CibrWu5tgggI4NAiEDLASrI8OOP-bFWJH21M9DBaRxqUnRwlk2ofT3gNbcEzTo0vd0VPqyR7Sp1wCKCiA2Iyv1mHESqXyKJarP4AsqgdS_zTW4laaFe1uec" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب: دول الخليج تتفاوض وإسرائيل أيضاً.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/75690" target="_blank">📅 18:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75689">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇺🇸
‏ترامب: كنت على بُعد ساعة من توجيه ضربة لإيران، وكان ذلك سيحدث الآن. القوارب والسفن مُحمّلة ونحن على أهبة الاستعداد للبدء.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/75689" target="_blank">📅 18:13 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75688">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27acce6b15.mp4?token=L1V99CeHsqdSUw8QUBJYRrHbEe2vKySOxsHgAO8xMkaKE8OPJXYiCPd6vnbxFaWBPYbd5jobH1-W038yotSZCsOVB2C3_p81mKkWDnKUk2wVsodi2v8l5LyWsAaa5d7xyi03DBdVUpXXPeqnmLGa95Kkmw-sTfTKjbWDeOQuCiozW-ih7Ew2qEqthhEZO6DtHSRYNcROAWaJDasZMKF4gvT12FAR9Vy5njZd-PVLDW_xWOCIh95LT4XVcmXEcsQw7S90VGBqVMJr6SDQjjjhrn_uWV2e2OYQS9OUQTQ96DcL2lldGUXzlynmtMp6EKvqMVHP-w2aTuG5M_Bfvjys3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27acce6b15.mp4?token=L1V99CeHsqdSUw8QUBJYRrHbEe2vKySOxsHgAO8xMkaKE8OPJXYiCPd6vnbxFaWBPYbd5jobH1-W038yotSZCsOVB2C3_p81mKkWDnKUk2wVsodi2v8l5LyWsAaa5d7xyi03DBdVUpXXPeqnmLGa95Kkmw-sTfTKjbWDeOQuCiozW-ih7Ew2qEqthhEZO6DtHSRYNcROAWaJDasZMKF4gvT12FAR9Vy5njZd-PVLDW_xWOCIh95LT4XVcmXEcsQw7S90VGBqVMJr6SDQjjjhrn_uWV2e2OYQS9OUQTQ96DcL2lldGUXzlynmtMp6EKvqMVHP-w2aTuG5M_Bfvjys3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: ستعرفون قريبًا جدًا ما إذا كنا بحاجة لضربة كبيرة أخرى.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/75688" target="_blank">📅 18:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75687">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‏ترامب: قد نضطر إلى توجيه ضربة أخرى لإيران، لست متأكداً.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/75687" target="_blank">📅 18:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75686">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‏ترامب: قد نضطر إلى توجيه ضربة أخرى لإيران، لست متأكداً.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/75686" target="_blank">📅 18:09 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75685">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🌟
‏
مجلس الوزراء العراقي يقرر ما يأتي:
‏
تعطيل الدوام الرسمي في الوزارات ومؤسسات الدولة كافة، ابتداءً من يوم الثلاثاء الموافق 26 أيار ولغاية يوم السبت الموافق 30 أيار بمناسبة عيد الأضحى، على أن يُستأنف الدوام الرسمي يوم الأحد الموافق 31 أيار.
‏تعطيل الدوام الرسمي يوم الخميس الموافق 4 حزيران في الوزارات والمؤسسات الحكومية كافة، بمناسبة عيد الغدير.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/75685" target="_blank">📅 18:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75684">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامب من موقع بناء قاعة الرقص في البيت الابيض: "إنها مقاومة للطائرات المسيّرة".
يبدو ان المسيرات مصدر قلق لترامب
😄</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/75684" target="_blank">📅 18:02 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75683">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇺🇸
وزارة الخزانة الأمريكية تفرض عقوبات على أربعة أشخاص في أسطول الصمود الانساني الذي يحاول كسر الحصار عن قطاع غزة.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/75683" target="_blank">📅 18:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75682">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇮🇷
نائب وزير الخارجية الايراني:
- تقول الولايات المتحدة إنها أوقفت الهجوم على إيران "مؤقتًا" لإتاحة الوقت للمفاوضات؛ لكنها في الوقت نفسه تتحدث عن استعدادها لشن هجوم واسع النطاق في أي لحظة. هذا يعني اعتبار التهديد فرصة للسلام!
- إيران موحدة ومستعدة بحزم لمواجهة أي عدوان عسكري.
- بالنسبة لنا، الاستسلام لا يعني شيئًا؛ إما أن ننتصر أو نصبح شهداء. وكما قال الشهيد رجب بيجي: نحن أمة عظيمة، فلنسجل اسمنا في التاريخ؛ من بين كل الألوان، اخترنا الأحمر، ومن بين كل أنواع الموت، اخترنا الشهادة.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/75682" target="_blank">📅 17:49 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75681">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‏
قائد حلف الناتو:
سيتم سحب 5000 جندي أمريكي من أوروبا.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/75681" target="_blank">📅 17:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75680">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دويلة الامارات تزعم ان الهجمات التي طالتها قادمة من الاراضي العراقية.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/75680" target="_blank">📅 17:43 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75679">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‏الولايات المتحدة تفرض عقوبات جديدة على إيران</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/75679" target="_blank">📅 17:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75678">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">📰
مجلة
فورين بوليسي الامريكية:
إيران تتفوق في معركة الرأي العام. قبل مئة يوم كانت إيران "دولة منبوذة" أما اليوم فهي الشخصية الرئيسية على الإنترنت</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/75678" target="_blank">📅 17:22 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75677">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcdfd32e5e.mp4?token=KS6iOyxpnJexvWfF_EQqZ0qcFlrlNtrsvPiXpx1BFg7Zjz4SVNNujvRDOxXIVJsmo7ajMoosH0RprkWQPpc-f6PSbjvXbXoJ_kom6bS4hCeqQrdMBma48YG0TFS3Q8j0axNG3puB23mWNHhNpfQ7C9KffCIOV8prXl1pU0WDJ1Ucrf2AmRUnumHFJ1v8EdipPcRxnbqPmnf19gfB-ruosfAHufEtsmCFSUiCZdy0sXzoTAokTr_3rE5TaeqKKwCO9oUWq7hjqK1NY65752WM0vZF7Zru0C4xVsv2ItLWcAPQGvRA0ZEx1WOkoaJkZbU5kyRterAV011KVswMko91Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcdfd32e5e.mp4?token=KS6iOyxpnJexvWfF_EQqZ0qcFlrlNtrsvPiXpx1BFg7Zjz4SVNNujvRDOxXIVJsmo7ajMoosH0RprkWQPpc-f6PSbjvXbXoJ_kom6bS4hCeqQrdMBma48YG0TFS3Q8j0axNG3puB23mWNHhNpfQ7C9KffCIOV8prXl1pU0WDJ1Ucrf2AmRUnumHFJ1v8EdipPcRxnbqPmnf19gfB-ruosfAHufEtsmCFSUiCZdy0sXzoTAokTr_3rE5TaeqKKwCO9oUWq7hjqK1NY65752WM0vZF7Zru0C4xVsv2ItLWcAPQGvRA0ZEx1WOkoaJkZbU5kyRterAV011KVswMko91Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#متداول
نفاذ الوقود يتسبب في توقف سيارة إسعاف تنقل مريضاً وسط احد شوارع محافظة ميسان</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/75677" target="_blank">📅 17:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75675">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ERMNQCozKTmmLDD0NgTIPdInUNigPRWSRA8qtJ5orWPskyWCjg9Ni1lBHjj7eN3UCjMqHSU9nazr8BrsLO0UmE-7N8T_edvmEX4mO26m1gE_Ia8p-Sjo1PqKXxjKc4YCUy17ZuMPUjE1OJwnI3uoZTBnLWxoPBfUlS-PRxtaxhi1tplZkGG0MvDt2V_EabJN7pwMAtZ2nzmG7YkpA-tnMkvIIk5Zs6NDBed3V4qMonX0unvKyFZcgB8UPWVdUUBWGOT9DiM-e5ajfUy9ms4s8C7GibY4AWbB1rC71Aq_c5EHM5GBbIhIcm6bSMVcvi-LDnyrdiDFoKMbY0zaq4kOPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G4PCqbx2UVBVKMarbdgniQ5s2pgCXxiNxMkJuMNO1UUdKHbr51BnRRDrVFySCIFnjxHjvuKvyHTw-QNrXq9GNNNUzfJZDcbIKek8txYuA7fMfXx0Q_ty_1ZGqgcRwxTngM6vgWVyTVwPO24l7c_3uHIPE6M5lZMOZ4Io8wqETIz14ykefoG2fwxGDtrhYXK2bLEB75g-qYq2EEFbfPbDCc6rJwd0_lLJ7EU9wWrdrlpRro2xwWyzpzGNqk5E903-OO-9ckBJnGp8TysDX73XFDGtuISDndCCLn-0Ry91ARn75628_uPaHjvfY6gs8lWvWSN8Id7vo--fHKhzIiyfwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">النائب سعود الساعدي يكشف عن هدر مالي بقيمة (4) ترليون دينار في هيئة الإعلام والاتصالات كمبالغ ضريبية بذمة شركة كورك لم يتم استيفاؤها للخزينة العامة مطالبا بتحديد المسؤول عن توقيع عقد التسوية مع الشركة دون استكمال إجراءات التحقق الضريبي، ملوّحاً باتخاذ إجراءات قانونية وقضائية بحق المقصرين في حال عدم الإجابة خلال المدة القانونية المحددة.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/75675" target="_blank">📅 17:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75673">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇺🇸
‏
وزير الخزانة الأمريكي متوسلا:
من المتوقع أن يدعم الشركاء الأوروبيون العقوبات المفروضة على إيران من خلال منع مموليها، وإغلاق فروعها المصرفية، وكشف شركاتها الوهمية.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/75673" target="_blank">📅 16:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75672">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">#رياضة
⚽️
قرعة كأس الخليج
مجموعة A:
السعودية
العراق
الكويت
عمان
مجموعة B :
الامارات
اليمن
البحرين
قطر</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/75672" target="_blank">📅 16:49 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75671">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🤺
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 16-05-2026 دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في بلدة البيّاضة جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/75671" target="_blank">📅 16:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75670">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‏وزارة دفاع الجولاني تزعم تفكيك عبوة كانت مزروعة بسيارة ثانية في "باب شرقي" بدمشق وتعلن مقتل احد عناصرها واصابة اخرين</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/75670" target="_blank">📅 16:02 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75669">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEtmDpAXJSUwjkBC_q1tHOSFTNQVJ90TQvs3G4chqtrxXSdFZPZ9qSTdxoJvwQtVwkXMJP2YbhH7_Xht8FuGhP5bFf8caoFUYjKlFYzjhCloqBepFC49dapFVzuD-8uNk7O4JCnbUXWEQYukoxbUXtrDKUdN5D5jWLTwzu-juq293k1nJyHXgiWe0Ox4pqZq2AiN3WOgqcDLdqEmDGkBIxN0aWDFdAH82mxNwQjs6jv9ue9_C4PxUPF_x44lTV39xGFNrAWRVWyOrWzLx2C1fntQYj3UuNw9hUtPEHobHreM5OHO3ATFmvRPTQUCItmVa6_56E4yydfcHozIXuG-4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظة الانفجار في دمشق واطلاق النار العشوائي من قبل عصابات الجولاني بعد الانفجار</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/75669" target="_blank">📅 15:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75668">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufhOeLBJ8DzeFcL2_gtW7BqhcGmLSM6Eja_cSDWYnq53RrEAGZPQFPU-zFHVMbA7uMYHyix6Oa0OQaWBFAyzvPDB8Me53Q0Mq_Yn1IVhrWCLI4c-vZq-ZtVOfNd3T5jZNYuN-odYXsvQ4zXPM82af72rs0X73bXbJOHY5kFcG-JxGI458CJBhIRv3GPxJAjlPUr3KR4iYA_hPymc2iV9bWZekaDqO_OOiqk7bP3dQUCbo48HWVGPSUyS6Eu-qgVxGESqxmx08_qwsNjbVNd4aK9Kp5-kiRmZ5rr-kx4ZKYFTWk40GhJxDE0EZ4_LmOxVEfYpPP5SD5jbm4MmPBW8NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">السيد مقتدى الصدر:
لن أغفر لمن يتهمني بالعمالة للثالوث المشؤوم او اني عدو لآل البيت عليهم السلام لا في الدنيا ولا في الآخرة وسأقاضيهم وإن لم يأخذ القضاء مجراه فسأتعامل معهم وفق الشرع ولن أسكت عنهم</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/75668" target="_blank">📅 15:48 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75667">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇬🇧
‏
بريطانيا:
العالم يسير بسرعة نحو أزمة غذاء عالمية بسبب إغلاق إيران لمضيق هرمز وعشرات الملايين مهددون بالمجاعة.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/75667" target="_blank">📅 15:39 · 29 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

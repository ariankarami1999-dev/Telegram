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
<img src="https://cdn4.telesco.pe/file/vFJQ9jo6At1ZzyS0zrx35sX-8blejeIcyDNn3wkcUMbh_1lUo-D3GDCXLV0qKea1dX8Sd3W7Bpo2vAvAUa8X3rzjf4NHx9WUv6siJqpA3SuZlhUsOHC_jJSWylgRxztuC6qMNtuzQzec6OCw-ADZ6sio_NV_xlG7i8jZ4UclXnPX7QFG-e74k--QLr_vTmjX4BkL_1vFeYUpBYJGj8q_sli4DNS7FmXfOoJHqZOgg48CNudOMoGvTClmIW7ETq90wy79_s8Y8mvcNM86wQ2PuoiQWTlXJgBHoYfn94WTsEAPU83bqEyVtldk1KngFbrUPLtVad_hk6fjcx48leD7tg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 256K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 17:41:53</div>
<hr>

<div class="tg-post" id="msg-80496">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇷🇺
🇮🇷
نائب رئيس مجلس الأمن الروسي دميتري مدفيديف سيشارك في مراسم تشييع جثمان الشهيد السيد علي خامنئي في طهران بصفته مبعوثاً خاصاً للرئيس الروسي.</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/naya_foriraq/80496" target="_blank">📅 17:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80495">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41542b706d.mp4?token=SabYGCs1w-cubntTIMRMie-IhfqafeiWlz8RkcAIOfFELoXxOZxeumLZNktrgAgyITAcMkyfrjpO94yZTIEsH74JS5xYcAlKb3W-B5kFAjUEhbmkMr6gCZZOpd5UYhfeMRwixoRKqq4RcxRc8lAebKJtnApGHW1BtFaLKdw6c74ktafD9FWQ3-TftM-TjvespDI9GVuiKA4ABSKGwpJFJFsfBnU9WIRYe6XZzBY-WUxbqEhNOXbqdCLtM_gotJ3O_o5iwJ-EifJu8Wqn_Gyrgy4WbAzxGak1j5BA3EXl-XF5G14d5dx0f4sJ1rBThDxA57bfZpQPQmGRanLT2zAJaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41542b706d.mp4?token=SabYGCs1w-cubntTIMRMie-IhfqafeiWlz8RkcAIOfFELoXxOZxeumLZNktrgAgyITAcMkyfrjpO94yZTIEsH74JS5xYcAlKb3W-B5kFAjUEhbmkMr6gCZZOpd5UYhfeMRwixoRKqq4RcxRc8lAebKJtnApGHW1BtFaLKdw6c74ktafD9FWQ3-TftM-TjvespDI9GVuiKA4ABSKGwpJFJFsfBnU9WIRYe6XZzBY-WUxbqEhNOXbqdCLtM_gotJ3O_o5iwJ-EifJu8Wqn_Gyrgy4WbAzxGak1j5BA3EXl-XF5G14d5dx0f4sJ1rBThDxA57bfZpQPQmGRanLT2zAJaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
🇺🇸
الكيان الصهيوني يمنح الولايات المتحدة استئجار موقع ما يسمى بـ"السفارة الامريكية في القدس" مقابل دولار واحد ولمدة 99 سنة في حال بقاء الكيان.</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/naya_foriraq/80495" target="_blank">📅 17:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80492">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PKg3pXJzl1CVNzsYh7x7ORT_mOIDiwzwONUz6bn1vNmhdv7hNCVovsOM4j1g7wJenQtxUJp-u5_seOy-t4Pk93pSHGDnXL2dRBw9knAs-cuEirQvWeXqjuoojho-kL870QD6e2L5QNjJYnhonoN3VHI00JVonEAXBdXPr23cHLJ6FccPmN_fg96bfRvwWkzay3EK6PH7MXRCZ8uKxt7Hksa9DlOtqB3CZC_9zEWycu04fJlJO3dEEkUPe8AoLHaCnm3AGh0ujGDm3uz-oVNobcAORnlNr54MrpiQKEmA9t9cLtQG83Ow9IR4pE7XFNUE6EPHnEHqPp1bIUe3YC3bSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RpD0inhHnRMxM7CoKHa-hbo6hGzZR3x3zdzkZiUfSAmDbN2J2sTPWG4L0tmhPgf4WjVt4_roBs55kUyCyDBdTkf6cRlQmpjbjNirsZFbRbnCZU2b_i69tjXTtYpfn9Uj6VGoah-0pDay9wFTZ9c4CeWOvxu4K2cbyFI6IRNOwsJCSgWm7e00Lzc7P90Qo2LN93Aqv3x5Yk6YiI94wzBwDoKccaj3IH8BgHEV6ujL-MZtzlLawcdzSDP0C0IPpVciRWOT1Nk01OrWvP3lFVkWz3ZCoqOc2GMuT3bqRxk-BGpVeI_RjOPdjyVxVc2cGFN8JNHhyLO0ySgskd6c8c6Zzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L-Bybrt3DRMaxlC0v9s6GPFv0MCjM_he4-34xfxMX7FLu0CE7I9q-2y7wUlMi23tOmvoM-6vVGUinbcj9wJ6jXot2diSn2Y-obhhnkm0jWQnHCSF1XOkqoNXfdEtI9_FoY74sZAls5qtubE3RLQTkj1vvhPuQ2hKsTweyRZBn0_bsArEZ9onqHENXbxbE5-sVibvEXxKOJNfpO78JgNxmKqXwKbpb-IlvzrUUkPI8I5LneUpG-2QgndiF9nBtS2AeMp5MZ-3xXzwFTLvkdtc53Wcaq3j4Rr53rO3yrST5SyJvgV80suS2sCyjf64XYZ83AdJ4AZ50gvqKsZbzAG8mw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#بالوثائق
🌟
سحب يد مدير عام شركة تصنيع الحبوب في وزارة التجارة العراقية بسب وجود مواد غير صالحة للاستهلاك البشري.</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/naya_foriraq/80492" target="_blank">📅 17:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80491">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🌟
المتحدث الرسمي لائتلاف الأعمار والتنمية يتحدث عن استثناء وانتقائية:
سبق لحكومة السيد السوداني أن طرحت تعديلاً وزارياً شمل ستة وزراء ورفض التعديل من قبل الكتل السياسية في حينها، وبنفس الوقت أحالت خمسة وزراء إلى القضاء ، إلا أن ظروفها  لم تكن توفر الغطاء السياسي الكافي لاستكمال مسار الإصلاح.. أما اليوم فإن حكومة السيد الزيدي تمتلك تفويضاً سياسياً أوسع ، ونؤكد في ائتلاف الإعمار والتنمية دعمنا الكامل لاستثمار هذا التفويض بفتح جميع ملفات الفساد دون استثناء أو انتقائية ، وترك الفصل فيها للقضاء العراقي.</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/naya_foriraq/80491" target="_blank">📅 17:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80490">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">هجوم مسلح على طريق 17 الزراعي في قضاء سفوان ضمن محافظة البصرة جنوبي العراق يسفر عن مقتل طالب جامعي</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/naya_foriraq/80490" target="_blank">📅 16:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80489">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1cec442b3.mp4?token=Z4Y3wBLrRo1FEKFusVCTcOK-YYB_ttXIQIZaLhJUygTVAA59cmKmSVmh94GY5HIX49MZsCjcoGYsS_fKcsf_etL6v_5PFKjUkyvoC5jEaoMB5_ajFMY1xrLBBJdBP2sjZQGU7piJgINck4cgip0Xm3Gdpf6991Z4-lz8BbkZYt9EBbevEJu2Mdwu19H1j79i39S79cvPOCWYiQUI2WisRq3hVOopYbi3WAJ1UXsDHpRQ3AxgltKrCGqleyoRZH5TTVgb_Uh9lX0eypZoIZrYUqdZkI_Dz4ho5Mrn2OoPz852SdStrmOxY1hhJk5L0GiItpbZcgX6tNOEeGjdVDGJYWMIMp9RcIttJDvMa43izuKcOCcM033Jxxm469-qYG69mbWmIf72jl3eqmAXwvrgo4pR8NfVmg_fN7NwWjBnZ_wF-Y_fooTKpqVcpWc4frNJnSBnmpirLcUpv76jGkoSH9bVRwaTQxvyk43jy4ZV5-yYpH4rKAZwLHH5ADBNe3tO7ArISfl0PJfPjBFN9qCw-GwmLjvtEwhe4gdNo5o6TB1frgl3O97PWi4tKbf6Bh7ohHW2CQ_r0KbQjFYqZhMHXa3IV4UGL8yFD_F2txBIOKCA3MjogXbuf7EPQ2vbicGOqZQiJwOjKk97CO8pLY56HuBPSzKPGT0CavcmZCqT9f8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1cec442b3.mp4?token=Z4Y3wBLrRo1FEKFusVCTcOK-YYB_ttXIQIZaLhJUygTVAA59cmKmSVmh94GY5HIX49MZsCjcoGYsS_fKcsf_etL6v_5PFKjUkyvoC5jEaoMB5_ajFMY1xrLBBJdBP2sjZQGU7piJgINck4cgip0Xm3Gdpf6991Z4-lz8BbkZYt9EBbevEJu2Mdwu19H1j79i39S79cvPOCWYiQUI2WisRq3hVOopYbi3WAJ1UXsDHpRQ3AxgltKrCGqleyoRZH5TTVgb_Uh9lX0eypZoIZrYUqdZkI_Dz4ho5Mrn2OoPz852SdStrmOxY1hhJk5L0GiItpbZcgX6tNOEeGjdVDGJYWMIMp9RcIttJDvMa43izuKcOCcM033Jxxm469-qYG69mbWmIf72jl3eqmAXwvrgo4pR8NfVmg_fN7NwWjBnZ_wF-Y_fooTKpqVcpWc4frNJnSBnmpirLcUpv76jGkoSH9bVRwaTQxvyk43jy4ZV5-yYpH4rKAZwLHH5ADBNe3tO7ArISfl0PJfPjBFN9qCw-GwmLjvtEwhe4gdNo5o6TB1frgl3O97PWi4tKbf6Bh7ohHW2CQ_r0KbQjFYqZhMHXa3IV4UGL8yFD_F2txBIOKCA3MjogXbuf7EPQ2vbicGOqZQiJwOjKk97CO8pLY56HuBPSzKPGT0CavcmZCqT9f8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سؤال: يقول النقاد إنك تستغل منصب الرئاسة لتحقيق مكاسب شخصية
‏ترامب: أنا أربح لأن سوق الأسهم يرتفع. الجميع يربح. أموالي تُدار من قبل صناديق. لا أتحدث مع الأشخاص الذين يديرون أموالي.</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/naya_foriraq/80489" target="_blank">📅 16:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80488">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0a98fb201.mp4?token=ksoqftA4T7a2i2A2g4bk29C3Mknt9HBYIapPzQMB_QNnVCdEPEyKlGQ2wwZfPQsEEpia8BQH1s901b1LCSf_5TMpLcz9Q6qWxVEb4b2S5QWxN1AvxjrsSGMiKZN5hczqFn1cDAm6HmuF_IqWkg5FFf8CvQYlrOtgDaOOH5mHUCNjSrhQHUaOS89iBtGSyQjQ71-Ad13UADr_KcNMcn39HdWJ-4RXxXwT7krlk3ZTgGyK17ewRCdoB-Up0nBt3AZVQ0Wx3EJ3AeHBgII39qZyTywp0J4O-Mie74ts2qzx-_X2zNSoJENvlI9lS2N5ihxqIKTCw0ctwi19Pebj8n_OHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0a98fb201.mp4?token=ksoqftA4T7a2i2A2g4bk29C3Mknt9HBYIapPzQMB_QNnVCdEPEyKlGQ2wwZfPQsEEpia8BQH1s901b1LCSf_5TMpLcz9Q6qWxVEb4b2S5QWxN1AvxjrsSGMiKZN5hczqFn1cDAm6HmuF_IqWkg5FFf8CvQYlrOtgDaOOH5mHUCNjSrhQHUaOS89iBtGSyQjQ71-Ad13UADr_KcNMcn39HdWJ-4RXxXwT7krlk3ZTgGyK17ewRCdoB-Up0nBt3AZVQ0Wx3EJ3AeHBgII39qZyTywp0J4O-Mie74ts2qzx-_X2zNSoJENvlI9lS2N5ihxqIKTCw0ctwi19Pebj8n_OHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب عن الطائرة الفاخرة التي اهدتها قطر له: ‏إنّ البلاد فخورة بها للغاية. يمكنك فعل أمرين -- إما أن تتباهى بها بهدوء، أو أن تُظهرها. وأعتقد أن على البلاد أن تفخر بها للغاية.</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/naya_foriraq/80488" target="_blank">📅 16:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80487">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efe48f538b.mp4?token=CVqEHlzb0LJLMIY1on2JNKUlT8XilMZbEYsvPrGRwIRDZV829F-ZuZkUG4dJ5HSZ_l4xAq4p7ukl9zTIpC_rjxKR5qihBkwKTbb3xvO9DEW-7yKTbb4Dk19iZIG8RfAAk5k_PdW7SvDtbMtmHqxhsNQP07tK6lVMWtwKhdzV3tFB9WR9EybzfZbuj0qZHxRq1sVBsxt-DRmfvCuSLF2QfQmlaxzXkmJIt5ZxohKavkVjVqzpyfwmBUJuPrjjU4STjpJt4GrOpDnjruorj3ciDvek0togs5WfsU5XdMMiOQHXnbRdHR43-hT0JrsgVOzReVF4GlIWWHKxmdaD9tuX0bofjVpCfL3HPZvAjn0bhJVYELlU5okJ59NVW6HRgADC3mcOaJ15O_X45wARnaOUDf67vuda2aYcGR8L41XsomL5uX9wmluNd7RLKJMsWx-hprVORK7wsz34ugwEz-b_OBMUjLwl8Sb2mRx63ksKmkI0IWQqdhMA7CUCYkJrxcpeeM_HvkYan_EpvVRp58VddqNGkQv_s-fNgZMluB4MlYj9MTC3R06njD7CMHsZTdmV-JqJa-TVzwjmdmmMMzRXvfcR0IC3lgvGLYyCWq-HLbWE6TovzMEP8jKnnfjmHhl-MaZxHoW-EtPPF3UcZMZMOVug_T3aOArOg5d4fsnGlbU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efe48f538b.mp4?token=CVqEHlzb0LJLMIY1on2JNKUlT8XilMZbEYsvPrGRwIRDZV829F-ZuZkUG4dJ5HSZ_l4xAq4p7ukl9zTIpC_rjxKR5qihBkwKTbb3xvO9DEW-7yKTbb4Dk19iZIG8RfAAk5k_PdW7SvDtbMtmHqxhsNQP07tK6lVMWtwKhdzV3tFB9WR9EybzfZbuj0qZHxRq1sVBsxt-DRmfvCuSLF2QfQmlaxzXkmJIt5ZxohKavkVjVqzpyfwmBUJuPrjjU4STjpJt4GrOpDnjruorj3ciDvek0togs5WfsU5XdMMiOQHXnbRdHR43-hT0JrsgVOzReVF4GlIWWHKxmdaD9tuX0bofjVpCfL3HPZvAjn0bhJVYELlU5okJ59NVW6HRgADC3mcOaJ15O_X45wARnaOUDf67vuda2aYcGR8L41XsomL5uX9wmluNd7RLKJMsWx-hprVORK7wsz34ugwEz-b_OBMUjLwl8Sb2mRx63ksKmkI0IWQqdhMA7CUCYkJrxcpeeM_HvkYan_EpvVRp58VddqNGkQv_s-fNgZMluB4MlYj9MTC3R06njD7CMHsZTdmV-JqJa-TVzwjmdmmMMzRXvfcR0IC3lgvGLYyCWq-HLbWE6TovzMEP8jKnnfjmHhl-MaZxHoW-EtPPF3UcZMZMOVug_T3aOArOg5d4fsnGlbU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب عن الطائرة الفاخرة التي اهدتها قطر له: ‏إنّ البلاد فخورة بها للغاية. يمكنك فعل أمرين -- إما أن تتباهى بها بهدوء، أو أن تُظهرها. وأعتقد أن على البلاد أن تفخر بها للغاية.</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/naya_foriraq/80487" target="_blank">📅 16:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80486">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62dbeeea8c.mp4?token=ttsQy5hyzKxeLeLyU_xisR2fWVtGZZ-Zwqq-ibrFTsHiNr-PCYNYh-a1sGoqHx1OQdfLgSOKcLBZ5FPH5vqHS7cPu0g6SprgXflQKuvbps2KcmI5G9uEuTaQJaDRWD4DDExol3p0dh4y2fbB-Th69eznojXYHBg2XlG_T5Wi2AL8V3Zui7zlRX0XHYBpvuk_HxyDzrEtnE_bBNzMrZQldfF9sQYGxw7SYHljQ395Rfc5VbSmuZQORQJQxgD8tK5IafkK_DdFHPIivoHwY1ujhjpFkoUENa9L29l3gSbPWWZvqb_6qx3VgZL1rs-r7r0tKu9CpaD7p30Cb_7RC4X_Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62dbeeea8c.mp4?token=ttsQy5hyzKxeLeLyU_xisR2fWVtGZZ-Zwqq-ibrFTsHiNr-PCYNYh-a1sGoqHx1OQdfLgSOKcLBZ5FPH5vqHS7cPu0g6SprgXflQKuvbps2KcmI5G9uEuTaQJaDRWD4DDExol3p0dh4y2fbB-Th69eznojXYHBg2XlG_T5Wi2AL8V3Zui7zlRX0XHYBpvuk_HxyDzrEtnE_bBNzMrZQldfF9sQYGxw7SYHljQ395Rfc5VbSmuZQORQJQxgD8tK5IafkK_DdFHPIivoHwY1ujhjpFkoUENa9L29l3gSbPWWZvqb_6qx3VgZL1rs-r7r0tKu9CpaD7p30Cb_7RC4X_Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اندلاع حريق كبير في ياستار شقق حي السلام ضمن العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/naya_foriraq/80486" target="_blank">📅 15:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80485">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bec1bb2f89.mp4?token=Vd6Uet_l0yq89r_YqYPOB2TNaoIfDgzGjOfelKdp8iTbpOJPKMQ2AJWgTdj6Okc-8-OQrdKdnY9pmYCAaoPG8NzzaPMV7aYCJJtt-fqN-2qCQ6LMyXNvc3J-NheStAXqWVfMqu41CGiTkfzZoaSfcjPq7AIQvEWWBIRj3nsv7YCYhEndqwUezPcSyYy-S2tfw5XnfUHI9DgiZ0sa8ClRTYZn3j-977b3YG13C6Ifzmo-TyuRcZFYkDSP-bhPL-H-XptT9-FOXp8KXy5YK7sOvelRUNrcxyrTH-KoNWoP8b4CiRR1B7H2RkqJIPTWqLpwd0Q-TCHmWrxdX-t2aN5kTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bec1bb2f89.mp4?token=Vd6Uet_l0yq89r_YqYPOB2TNaoIfDgzGjOfelKdp8iTbpOJPKMQ2AJWgTdj6Okc-8-OQrdKdnY9pmYCAaoPG8NzzaPMV7aYCJJtt-fqN-2qCQ6LMyXNvc3J-NheStAXqWVfMqu41CGiTkfzZoaSfcjPq7AIQvEWWBIRj3nsv7YCYhEndqwUezPcSyYy-S2tfw5XnfUHI9DgiZ0sa8ClRTYZn3j-977b3YG13C6Ifzmo-TyuRcZFYkDSP-bhPL-H-XptT9-FOXp8KXy5YK7sOvelRUNrcxyrTH-KoNWoP8b4CiRR1B7H2RkqJIPTWqLpwd0Q-TCHmWrxdX-t2aN5kTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اندلاع حريق كببر على طريق أربيل-مخمور شمالي العراق</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/naya_foriraq/80485" target="_blank">📅 15:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80484">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇮🇶
الحشد الشعبي:
ضبط 20 ألف حبة كبتاغون في ناحية السجر بقضاء الفلوجة شرقي محافظة الأنبار داخل أحد هياكل البناء في ناحية السجر، كما ضُبطت بندقية كلاشنكوف، وسلاح من نوع M4، ومسدسان، ورمانتان هجوميتان.</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/naya_foriraq/80484" target="_blank">📅 15:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80483">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🏴‍☠️
حزب شاس الصهيوني يعلن أنه سيصوت لصالح قانون حظر الأذان.</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/naya_foriraq/80483" target="_blank">📅 15:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80481">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اندلاع حريق كبير بالقرب من الطائرات الجاثمة والمتوقفة التابعة للخطوط الجوية العراقية داخل مطار بغداد الدولي</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/naya_foriraq/80481" target="_blank">📅 14:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80480">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">حدث امني قرب سواحل اليمن</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/naya_foriraq/80480" target="_blank">📅 14:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80479">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">حدث امني قرب سواحل اليمن</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/naya_foriraq/80479" target="_blank">📅 14:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80478">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔻
هيئة بريطانية: زوارق صغيرة على متنها مسلحون اقتربت من سفينة قبالة اليمن</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/naya_foriraq/80478" target="_blank">📅 14:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80477">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1302294625.mp4?token=HSSY2zp2daqO0HNsSXMK0kWY-G1jPQPs753O46h2VdV53R_GRzb5qi1A_wjTQaPpaU-6IJbyZOzdSB_w3n3eGa0b3U6cpJhYrIBXizQ_HkjqhmzjkPmf7FOX4F9sFbZR3x3DgN_EmsJzOy-VGWr9VrLYGxbj3hX-Tr6Xxd6uEiY4RioVBncoX3EX437X04phdJ5K7MHVusvlmlZK7jj4yh7nSwokgyF6knLL_NynYzxNF5b8_-fem7bC9KbeHPdEkEImb_0_ZPrilVEShj-g0R_HQKpPiwhT6HVVzynLHAOG3jpw7ZP1JErEiBu3jM3KQQqeMMMX1uBbCWbVtjNu44i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1302294625.mp4?token=HSSY2zp2daqO0HNsSXMK0kWY-G1jPQPs753O46h2VdV53R_GRzb5qi1A_wjTQaPpaU-6IJbyZOzdSB_w3n3eGa0b3U6cpJhYrIBXizQ_HkjqhmzjkPmf7FOX4F9sFbZR3x3DgN_EmsJzOy-VGWr9VrLYGxbj3hX-Tr6Xxd6uEiY4RioVBncoX3EX437X04phdJ5K7MHVusvlmlZK7jj4yh7nSwokgyF6knLL_NynYzxNF5b8_-fem7bC9KbeHPdEkEImb_0_ZPrilVEShj-g0R_HQKpPiwhT6HVVzynLHAOG3jpw7ZP1JErEiBu3jM3KQQqeMMMX1uBbCWbVtjNu44i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتداء مسلح يطال السائقين العراقيين في بانياس السورية من قبل عصابات الجولاني</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/naya_foriraq/80477" target="_blank">📅 14:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80476">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اعتداء مسلح يطال السائقين العراقيين في بانياس السورية من قبل عصابات الجولاني</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/naya_foriraq/80476" target="_blank">📅 14:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80475">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99f98398fd.mp4?token=G1gnIUfFJuVv6T3vU_IrpQn4UCcU8WYmsCc99g0738P9-o4CfLx8yeRZEExtEJBKCbGyplZ2MkfZHYt9gHcgILugTR8_vjKi1x0JsRfyxVLqsBZxzowqrAM6Z8jAvTfv4DMJupbMX3AG1hBjlnbf3Y2-RpLSIKbeXrJhsvy4pRnRV5LFiFdUMqyq6Bsz8J2Dfa3Un40pM4p31oiUxNhS7l1JfbsTEc2dpJ4BMxuSZuirmytF-1ZlYTASpWepGiTtM6pRncajhbakoZju_Xm-gcyxrVI5IEBOEdrr6YTAzAOanFy-UA57tsC1EleJYwGd_xS4_ePYgzHaDGsgQm44ERnvAUEnAZSl_-QoDs_qN0934soyl3DJzvtKY_kKhjAkt52lAnn7p5SlcWvI30iOHVWr3KLt0o8lPK7QvQVucho_l-UvM8GXG9GUEjydKyVrUQccrK6gmY54ZzKoirL3za90tjVzSRlmD4xIkli9OWPgdFKqr7yen-4lUytwmNS1UwZ9Lfu9eMeWK77h-jY9cPmR-9qhPoU_9sLNYU7E15el9e1sj-ZBDysNdgQ_2HCXui_uidekvDzz8eO_WhbhSE78YTUZG-laVyHBjlcXWGqricPxSefnFKF9xYf8rZ9A3mxCqPlxPSostoavut5JfjTik--hIYgliyoaDgMFYzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99f98398fd.mp4?token=G1gnIUfFJuVv6T3vU_IrpQn4UCcU8WYmsCc99g0738P9-o4CfLx8yeRZEExtEJBKCbGyplZ2MkfZHYt9gHcgILugTR8_vjKi1x0JsRfyxVLqsBZxzowqrAM6Z8jAvTfv4DMJupbMX3AG1hBjlnbf3Y2-RpLSIKbeXrJhsvy4pRnRV5LFiFdUMqyq6Bsz8J2Dfa3Un40pM4p31oiUxNhS7l1JfbsTEc2dpJ4BMxuSZuirmytF-1ZlYTASpWepGiTtM6pRncajhbakoZju_Xm-gcyxrVI5IEBOEdrr6YTAzAOanFy-UA57tsC1EleJYwGd_xS4_ePYgzHaDGsgQm44ERnvAUEnAZSl_-QoDs_qN0934soyl3DJzvtKY_kKhjAkt52lAnn7p5SlcWvI30iOHVWr3KLt0o8lPK7QvQVucho_l-UvM8GXG9GUEjydKyVrUQccrK6gmY54ZzKoirL3za90tjVzSRlmD4xIkli9OWPgdFKqr7yen-4lUytwmNS1UwZ9Lfu9eMeWK77h-jY9cPmR-9qhPoU_9sLNYU7E15el9e1sj-ZBDysNdgQ_2HCXui_uidekvDzz8eO_WhbhSE78YTUZG-laVyHBjlcXWGqricPxSefnFKF9xYf8rZ9A3mxCqPlxPSostoavut5JfjTik--hIYgliyoaDgMFYzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
عمليات إبادة وتنكيل واعتقالات واسعة من قبل عصابات الجولاني الإرهابية تطال أبناء الطائفة الشيعية في قرية المزرعة بريف حمص مع توجيه شتائم للإمام الحسين عليه السلام.</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/naya_foriraq/80475" target="_blank">📅 14:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80474">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">رئيس مجلس محافظة كربلاء يوجّه بإبلاغ شيوخ ووجهاء العشائر للاستعداد للمشاركة الفاعلة في مراسم تشييع الشهيد سماحة آية الله العظمى السيد علي الخامنئي المقرر إقامتها في كربلاء المقدسة يوم 8 تموز الجاري.</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/naya_foriraq/80474" target="_blank">📅 14:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80473">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">القضاء العراقي: السجن 10 سنوات بحق المدير العام الأسبق للهيئة العامة للضرائب وزوجته عن جريمة غسل الأموال حيث أقدم المدانان على حيازة أموال واكتسابها بصورة غير قانونية واستخدامها في شراء عقارات</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/naya_foriraq/80473" target="_blank">📅 14:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80472">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🌟
لمعرفة نتائج الصف الثالث المتوسط:
اضغط هنا
الناجح مبروك
والراسب بيك بخت بمحرم النتائج
مواكب المبيت هواي
😄</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/naya_foriraq/80472" target="_blank">📅 14:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80471">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u30jsCVQtnw5gd92BVv4EERyLWyyJ-eFOh85pIz5F4T6zHXj9LkWFE9sbGunUxXeLQd3GJyj0TmOAh4Jpffd8qWfJZ28SVpW5Jw1b-RAvJwppTKkquq6ipk_YFr3_7COEIIgr9LBJivgY6jJyX2mxyVhitilX3nlhB2y60jti_eOwn2k_U9M4-UK_6uJWidVZ-0mtGP_cWYMvMqaKB2gVQ4RJC9egzVp1k_7Okzx3jlt5R0Ff9lqN0HWvAJrA4VTRn3SPv6uloGaunxYku-9jnWvAhXiuQn0ce8jYsu0a3bQK6pDnfY1tpeNVEAUMvmY5YyWv_0j-ZIavgr2AIzuWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
وزير الخارجية الايراني عباس عراقجي:
‌‏مذكرة التفاهم واضحة ومتاحة للجميع وتلزم الرئيس الأمريكي بلجم حلفائه في تل أبيب. وإذا تجاهلوا أوامره، فسوف تؤدبهم إيران. ‏أي تهديد ضد شعبنا وقيادتنا سيواجه رداً فورياً وقوياً.</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/naya_foriraq/80471" target="_blank">📅 14:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80470">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d63ab9e22.mp4?token=fcOc6tmDkbAPoGRS3eg1S5BU-xXRZZ-UosdWZsGw5bkw2n3zxOSd6GyXYbnM4QKObor5pI1xidnsftjJ3BXskymveA4vFQxYpHNYh2OIVMkvxpbp32YahKKB8ZVliDNmIZieV2EHV3-AP0i-wwgFct_r8ODHTCwK7l4l3G0FrSl_navZ1v8A-UG6Pc4j-N_6wkgrkh17KWU9MDfhnNIFaM94B-qSmD7QYgLqVkFbYxBFwQe9-wy44-PjYR3YSIbUp5nlzMiTy1rzzK3wRjgjo7fAUVqza_J4HHQstK6g3eFv74iDQwUmNGOkqiJtudQ3zvhld5MIvKJFGXbBP5vVfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d63ab9e22.mp4?token=fcOc6tmDkbAPoGRS3eg1S5BU-xXRZZ-UosdWZsGw5bkw2n3zxOSd6GyXYbnM4QKObor5pI1xidnsftjJ3BXskymveA4vFQxYpHNYh2OIVMkvxpbp32YahKKB8ZVliDNmIZieV2EHV3-AP0i-wwgFct_r8ODHTCwK7l4l3G0FrSl_navZ1v8A-UG6Pc4j-N_6wkgrkh17KWU9MDfhnNIFaM94B-qSmD7QYgLqVkFbYxBFwQe9-wy44-PjYR3YSIbUp5nlzMiTy1rzzK3wRjgjo7fAUVqza_J4HHQstK6g3eFv74iDQwUmNGOkqiJtudQ3zvhld5MIvKJFGXbBP5vVfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد اضافية من الحريق المندلع داخل مطار بغداد الدولي لاسباب غير معروفة</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/naya_foriraq/80470" target="_blank">📅 14:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80469">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCP8PXmYv2GLgRMqlaFoMVV2j0xAgQzdJCt4pr58fGVWbAMNVgsyMNmOVcsqclA45Mk1LWDj16qa2XglQJUl6i8onWHRsL9DZ3_MUC2o72FuZ-9M54QVhFKv6S9RrFOKn6QEvX0fBYy3CgrDF_SFXlb1VfB_7E5Hn7c6tdReajgA5svBjQL6o0FMGEHzY_jPZbqy_fjlOE935ogWZfofcRpq7hqpPwHiefhXisIcnT-Y5VIKuUojqZv87uw0oKE3OUdAizEs9WbCU8peE4YZv3S5dYeIo_5T8PlP9KSr2ytsYJ63RtHd5-EA-RR_Y-vqax9tLVaTIl2He0SjnnKFHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد من الحريق داخل مطار بغداد الدولي</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/naya_foriraq/80469" target="_blank">📅 14:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80468">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اندلاع حريق كبير بالقرب من الطائرات الجاثمة والمتوقفة التابعة للخطوط الجوية العراقية داخل مطار بغداد الدولي</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/naya_foriraq/80468" target="_blank">📅 14:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80467">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gq1DQzLr2PyyNWJkT8Wti-4NFzDpu0YuuiomujyY9idiNKeWRUg6nsEgNYsU25cmXYvuuShs7o5oC_6gGRkgd2yMTG44_G5ZIz-ER5_U530sToJLDMoz2aCARZmK4bATmEMzjf4srBPhgNsfwBd4R8xJbKx7zvIWItOw30JCeAw3Kt8A3Zba5YXQV2fSUYsl9Mx_Uq4Y3PjqVaWhCp1ZC5WttimqDJQMOpkV7T6j08djUiqgplqG4mlRyfGXmY3vOJ1IVIC6pxXnaqw8Nkbykrcah9yXy7bCTf8PcSPX7_7aNaGAr8ohsTcgkPs4wLoQrlYoVtjXxXTy4OPrx_PORQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندلاع حريق كبير بالقرب من الطائرات الجاثمة والمتوقفة التابعة للخطوط الجوية العراقية داخل مطار بغداد الدولي</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/80467" target="_blank">📅 13:41 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80466">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">وزارة الصناعة والمعادن العراقية:
صدور أمر وزاري بتدوير وإعفاء عددٍ من مديري الدوائر والتشكيلات.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/80466" target="_blank">📅 13:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80465">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZWBs07yoBi0xwbPvYPWH21TK3fyrEP3BWfLMCFJ9FRuYLs6oAAnyRrLwG87w1TlsYeIjHEM-_-Re83Qn4sZqTlNbpMaQkLEM31MuWzyX2JHeMi2bJjfr6uQJH5_2gtO6HuOWXE6FhYgsMSort7czNfaYd-f1cm1EZT2NTIN8DnN6sC-Nel-sWUbScF6uLDIqv77VzhMvNoJ_anzPLZKcPrNROyaJQO5vG5wX4aITKUrtUSi4ikMdFNBi5aaRbt5fxM32-A0ad7HOh5HJlx16LQB_as98JkZMuPMDl5WE9vB33w8uNT0rrs98bz0DbVhKeD1OVaO0eIQxR92vamqhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قيادة عمليات حزام بغداد بالحشد الشعبي تعقد اجتماعاً لمناقشة استعدادات تشييع السيد الشهيد الخامنئي ودعوة أبناء الشعب العراقي للنفير العام</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/80465" target="_blank">📅 13:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80464">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOX7NqxNVyH4jdaYG0OFP75EbBYQa6bEd9ekUjqgsLbNb9TRjsy6Zchn3z_bxGXQaOKvEteSW3YvsOd7HVzEMNsdBhM8fMlRPXd8YJZJQc7v39nLX7uMJ1Unwpy-QhOXgPUsYNh1zy9ORJlXkitPymC5kcR4t_uBAe5Wz_raf539lFnm0QluaSKy9RYMuWKIEF7E862jOvuotJbbKfYSc8G3rg6knzYu4KqAQiGWed1lY78fe9v-BvFQUn653pDzciLklVp6J_KTw4x4uIakXsw4RsDwrrbVGkdnlU5ZVQTBpfCjbfkYYQodLArDW4L07X_u_vvrV48gE3MvXv_W_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
حدث أمني على بعد 76 ميلا بحريا جنوبي بلحاف في اليمن.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/80464" target="_blank">📅 12:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80463">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔻
حدث أمني على بعد 76 ميلا بحريا جنوبي بلحاف في اليمن.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/80463" target="_blank">📅 12:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80462">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالعراق يودّع إمام المستضعفين</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfAV27JHmz08ZwLNxDdrU5-Lj0nzlg5okVgHOFY7tKXQq1WzOLfdXmCPkA-Nu6HdMSFUE4H0eEwKgIWwoirUGxVwgAK2kJ0cXSEtSHxB7XOknYGGm_0UYDjUQxIQE196oi2sm6glfGt2SU8_lLbWTf6wpkdbQ_UUH5R8et44WhVgL2CV7VMS5EtRdn0lt-hwvQOCtw2Y7U1R16kUdwpcNp-dhOBXU10-LLBqwPAs31V9k0WBds6p1x2AH9MZELAgY8ww9-aGdOIvP-kRgagitzljEuCIgs7yloYxM4fzvlthPU51uWYi7jdJh1EzmvWJCDdq5Lf4oHMt4Y6SZFHZTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
يُنشر لأول مرة
|
🔸
المتحدث باسم لجنة تشييع قائد الثورة الإسلامية الشهيد: الجثمان الطاهر لإمامنا الشهيد لم يُوارَ الثرى حتى الآن، ولم يُدفن «وديعة»
إيمان عطار زاده
:
نعلن وللمرة الأولى، أن الجثمان الطاهر لإمامنا الشهيد وأفراد عائلته الشهداء، قد جرى حفظهم حتى الآن في كمال الإجلال والرعاية، ومع مراعاة الضوابط الشرعية والقانونية كافّة؛ فالجثامين لم تُوارَ الثرى ولم تُدفن «وديعة».
▪️
#قوموا_لله
#تشييع_إمام_المستضعفين
➕
t.me/Wadaa_imam_iraq</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/80462" target="_blank">📅 12:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80461">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TFp9P8EAdvcOB18LI-RptrMUiS1v24Y90HZ4QDAFHu9Unh8hJfONhLiNsX9ctbV2ya6-I-r36jVmLZPF2SFiKcmNcR0iNtdJga9Qx74-3USbWsNh7e2ghu46Bbwmoxk2LlnDaujkM_Tr8yL8YS9zkLbyvhEm5P_O8iGTu6ifkhx3fGN2ayi73lMT2Sw_TVh0AstGNk2KfCLlg8gpvgJ_oUDI1Wz0j0Gb4D_SvJNrMi_1hq0foGOlcgPpYiI9PsdFrf0NhKfZzqihfaXgtLVJKpxVIlSRfIElWKqWZD0z6raStc9MWBD52kvTyC016FylgCuRC7e7mLMpJGaQG_lcTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
الجيش الأمريكي: تم التعرف على هوية جندي مشاة البحرية الأمريكية الذي فُقد في البحر من متن السفينة USS Anchorage وهو العريف لانس أرماندو أورتيز كانسيكو، البالغ من العمر 21 عامًا، وكان يخدم ضمن قوة مشاة البحرية الاستكشافية الأولى (I Marine Expeditionary Force) في معسكر بندلتون بولاية كاليفورنيا.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/80461" target="_blank">📅 12:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80460">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔻
تابعوا إطلاق نتائج مرحلة الثالث المتوسط بعد قليل على الرابط أدناه:
https://t.me/nayaforiraq2</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/80460" target="_blank">📅 12:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80459">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">📰
رويترز: محادثات فنية غير مباشرة بين واشنطن وطهران جارية في الدوحة بوساطة قطر وباكستان</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/80459" target="_blank">📅 12:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80456">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rioexIhOp9iPiQOSGnBXq6QmUCp28EvGeJhlzxzfD_As40lry-4fW5DgoqeRzz3U9oA1wLErWfD8YLvyVvmlCYCdQoiXHZehSaSGwb7tKv0f7RZuD5g_iQRpen1eH7zr0vicX-tf6itLqZcw-b0u5JcL3JpLdEEihTCK2KBrHvjJb6Lr-R8xWgqryH6ACNjZZDmTLaZCGbQ8PCTe9WaKB8gEaWy3yd031CHWpZfa1FRzaFiadUNjMm-6WvypyVtCYlMLwBD_06XWXrBLjqqA7WsWZbH1nPODl5Lg5TOgKn2oDWs77dS19VPAunQuUgcHp3dO8EjU1NsEx0jUbY-hnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EtnyZm32HewSARfIJ6oTqGurLiRAJcAddsEH48f1bEGGLCyF5doYodaGNkHKIbsaaKNxglF5mBMLwuXc8zqEWPCIZh9fbk_vzuqNsX3XLnBgZ6wVyO-pWowWPICeYGWQaxSKhc6ZEAKUhXrHtI5bmx9BuAJeEUn8Eq-DtPT0-dHC4EPmyBSm9zXh3dFsoCeGE9rl2g77eAknkAwdHUs7BNMQ4h-OQvis6NShkCydHzvFzuFEKK_g-fU8ZOkMCcH5DSxp0whKS_U0PjhM33cR59jtQb_cR4DoAOua9MK5j4uiiCNDOcZEbYIw4fVLUi1oc130S4lNXyIgRZ1vZd_TtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k51lO3ifcMQ8Y4UaZT2JMklpyP6GECPqoPG_4th8HiRWuDnLgKcEnSqYHU0cvTl0CHC_kWesNwltn_L7jKwHKNNYlI1JOpk6lqfeGiFo4hNEn15hwjdVzKA0zkbbJSNcvqO0QOE9dyMmdgloLYpzDd1pY06ad0nLVHeWfv_BtFfClatW8u_mHdAYxU9yzH1MHciOuLjmg0shXaHsEcXxi__1UhE56FFjqQkN-BoCc2QOhhmjbN2lkkYxYbwHOgJSGcyGzQIpA4cYcFsD_GnHp6ItvcXRtmveLMTXa6yKCfPPxjK2f_KZ54uK4EHKyi1LGMw6eY0R7YAobr_qso39Lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
استمرار الانتشار الواسع للقوات الأمنية في شوارع العاصمة بغداد.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/80456" target="_blank">📅 11:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80455">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7b2a11221.mp4?token=H0Cy0VkTNKtwP_kMCc6TZ6gzRiEnrwG9howVs-r2rEDt2y2_VIqbagRcXSzyLGJbCdcoxOL3tUG3ciMKJF69ZTBY-7eOEzVMIjWm0aX3vvlNKVPQh-hI6UQHuAUUHzRohySIa2YOl4jU_zuhCU5xsitQRTeXxGzSrj-Q9gP0NVSqzEH7J5aBVD1UbuP8r8JDNTLlliAE_uKA9vAYBwqlPgCmko3IAuqjSc8MMqx_njn9Rldc_Lqf41PN5Nvnc5Eb-bYxhsOnYD3axkUeymwa2TfWmw04uH_7I4KBnBCVNqtlViNmiyKNI_Els3BpdqdgftAWTNzwIKGaTX7678QBkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7b2a11221.mp4?token=H0Cy0VkTNKtwP_kMCc6TZ6gzRiEnrwG9howVs-r2rEDt2y2_VIqbagRcXSzyLGJbCdcoxOL3tUG3ciMKJF69ZTBY-7eOEzVMIjWm0aX3vvlNKVPQh-hI6UQHuAUUHzRohySIa2YOl4jU_zuhCU5xsitQRTeXxGzSrj-Q9gP0NVSqzEH7J5aBVD1UbuP8r8JDNTLlliAE_uKA9vAYBwqlPgCmko3IAuqjSc8MMqx_njn9Rldc_Lqf41PN5Nvnc5Eb-bYxhsOnYD3axkUeymwa2TfWmw04uH_7I4KBnBCVNqtlViNmiyKNI_Els3BpdqdgftAWTNzwIKGaTX7678QBkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مرقد السيدة المعصومة عليها السلام يستعد لاستقبال الزوار لحضور تشييع الشهيد السيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/80455" target="_blank">📅 11:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80454">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a10c2fa70.mp4?token=YkY7V2AhLncQGMXGFQYyqv_gEbuiYLM2VJ6EI9X9o3ypnVbWvEJDHWcUS97t6L0vRc1VK0Z_OS3EfpYanBb8MujTyG6BY6t74XZMG8zfKN6cVtIONfTSv18eRipWAmb7zBD6WZQ15Dw0diCEiO886lc_CogPyLkeBt4Jg1fcREmGkPcMEpEbDjiGXlGV7R_U61go4Q6-Sw-nyuUMAQboysc2RpP_Fw0I7_5MXK8x1ZefO3Vh6VQ1V_ElInxIAAwQz-tm4yS_fM9COf0ztSOrgL9jPVCz7TgwucRk1tW0Ngt_inMc6yR6RJQP9cqkGZVNXEQjlkYKU9ssEpxzOLsUKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a10c2fa70.mp4?token=YkY7V2AhLncQGMXGFQYyqv_gEbuiYLM2VJ6EI9X9o3ypnVbWvEJDHWcUS97t6L0vRc1VK0Z_OS3EfpYanBb8MujTyG6BY6t74XZMG8zfKN6cVtIONfTSv18eRipWAmb7zBD6WZQ15Dw0diCEiO886lc_CogPyLkeBt4Jg1fcREmGkPcMEpEbDjiGXlGV7R_U61go4Q6-Sw-nyuUMAQboysc2RpP_Fw0I7_5MXK8x1ZefO3Vh6VQ1V_ElInxIAAwQz-tm4yS_fM9COf0ztSOrgL9jPVCz7TgwucRk1tW0Ngt_inMc6yR6RJQP9cqkGZVNXEQjlkYKU9ssEpxzOLsUKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
صهاريج النفط العراقية التي تنقل النفط إلى سوريا تتعرض لحوادث وانفجارات خطيرة في شوارعها بسبب سوء البنى التحتية والإصلاحات الوهمية التي غنّى وتوعد بها الجولاني.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/80454" target="_blank">📅 10:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80453">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔻
سيُغلق مطار مهرآباد اعتبارًا من الساعة الخامسة صباحًا يوم الجمعة وستُعلق رحلات طهران بالكامل يوم الاثنين.
▫️
سيستأنف مطار مهرآباد عملياته يوم الثلاثاء بينما سيبقى مطار الإمام الخميني الدولي مغلقًا لنقل جثمان القائد الشهيد إلى العراق.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/80453" target="_blank">📅 10:41 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80452">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxXmPp-lpGF26CvdhnCuj1v_kvgCgpETEanujVNZT7czOVjePYDzqjmT0KXUzasR3FnZCaM6ZkLvvlCeBTX2DZVXSbgoi60OfQZUzIIqTHcJgAW-PmBiTYw2l7hnxONqgAtU_WVB0T1YBAHgZEbZZmKxjDiCzRLy7u4pqkFe9dXFScWM0TP1tH0gxvV42UqWYTxKFawgvzN1vxO7Fom80rTU6W5IEGb2gAJLiNajBT_9avohSxB82TUUSCQF15S_RpVIj-K81ju7GgCmhobldGQShNQEfbAbdU4JVkhzODNaa2QyZ8rjx8KmdfQHz8R05CJUGXz6sMkBDpAjcLK5fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
في أجواء توديع ووداع قائد الثورة الشهيد السيد علي الحسيني الخامنئي (رضوان الله عليه)، تم الكشف عن أحدث جدارية في ميدان ولي عصر (عج) بعنوان الوداع الأخير (آخرین دیدار).</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/80452" target="_blank">📅 10:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80451">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfd7746698.mp4?token=J-942dFWuHboBHNJVhSBPTMxciC5TnVwkKNq5DbmrYVGS44FVVZeyR9hmwQ0Y_ZKxmeZklh6PjUrfXADMIynzgCkxzGsagkinAeUAb3czIQPpadSQndb9zyqGHB7XJ3_WBox4hzzQeRNYtceI3awX3p4jGtdOYeKx552Gn2vVPd3rHQOjeKCnLkbTiQNWOxE1WA85YexVVuTmaF3S_Jr_aIIG-vHAmzjhJtFpy6QE-5Od-3xrV8EXtcZdcZey5xgvuvHRsYiEwjHfaXNwXp7kwVei9t7KCajXBXLbz6jFFi9ubO5LZWG-NOCu6t3OrHa0RV_krTExtiNlEBXdJ8v-7rzeAP23KE1CeUx_suFuUVu8Ob3pJq2p2Ry_1bCGHxrfZ6RQNgGBTO2DQxn9igsqCGdy4r_VO9HhAtUganvmPDy9TNTuJml-_cXBTvb8Ty8O_eWR6qMNuREcWDiFjscVp5cMHVxjRkY0pBXJRoedriLbP6e2vXX4hIPai8OxBQW9C9xQLbyFiMNLh9JSp_CF1hJdPbJScgEZXE4nrHLwqFJRarMyCy866br4bV8YU2UZxTQ322VXvtrg-U7tZRdBwB1YKhaSUyFhFqMY4xTfbQglp8GxGsUY4Qy2F0PA7VXzXZAnhMhwHDIqit0JgF_KbRKR83CTV0n8MxS-6jiyVc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfd7746698.mp4?token=J-942dFWuHboBHNJVhSBPTMxciC5TnVwkKNq5DbmrYVGS44FVVZeyR9hmwQ0Y_ZKxmeZklh6PjUrfXADMIynzgCkxzGsagkinAeUAb3czIQPpadSQndb9zyqGHB7XJ3_WBox4hzzQeRNYtceI3awX3p4jGtdOYeKx552Gn2vVPd3rHQOjeKCnLkbTiQNWOxE1WA85YexVVuTmaF3S_Jr_aIIG-vHAmzjhJtFpy6QE-5Od-3xrV8EXtcZdcZey5xgvuvHRsYiEwjHfaXNwXp7kwVei9t7KCajXBXLbz6jFFi9ubO5LZWG-NOCu6t3OrHa0RV_krTExtiNlEBXdJ8v-7rzeAP23KE1CeUx_suFuUVu8Ob3pJq2p2Ry_1bCGHxrfZ6RQNgGBTO2DQxn9igsqCGdy4r_VO9HhAtUganvmPDy9TNTuJml-_cXBTvb8Ty8O_eWR6qMNuREcWDiFjscVp5cMHVxjRkY0pBXJRoedriLbP6e2vXX4hIPai8OxBQW9C9xQLbyFiMNLh9JSp_CF1hJdPbJScgEZXE4nrHLwqFJRarMyCy866br4bV8YU2UZxTQ322VXvtrg-U7tZRdBwB1YKhaSUyFhFqMY4xTfbQglp8GxGsUY4Qy2F0PA7VXzXZAnhMhwHDIqit0JgF_KbRKR83CTV0n8MxS-6jiyVc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
المتحدث باسم لجنة مراسم تشييع جثمان المرشد الإيراني: جثمان قائد الثورة الشهيد وأفراد عائلته يتم الاحتفاظ بهم حتى الآن بأعلى درجات التكريم، مع الالتزام الكامل بالمعايير الشرعية والقانونية.
▫️
لم يتم إجراء أي عملية دفن أو مواراة للثرى حتى اللحظة.
▫️
الشائعات…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/80451" target="_blank">📅 10:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80450">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15cb98fdc3.mp4?token=aafOdeBHP6PQ1HbBR7-IvEBVaxN5ctUW6Ft9uxGNm3AuIbUJnjxPyYaGbvYP5FpDvWEerzDICQC0Wdlq2YAh6SymQosfgg3uynds6iRHBKUtX78uGEZBLWN2TUnrKRcKP3jAeaPfq2FGS2inQT1kUxNA9Bm2EgajsrU2EH9m3XOYgH_RvmRo-vj_Ne5QJOKnatZSsf87AnQneT7INnniDqNsYO-EkkV5KTwIxoIH617tkY4RyxIKq83C93tv2l3mO2MmHXK2nT_92pVTMypUGPiyfjBVdg7cwBH9gu23CuA0zG2BBIXWf9koN886LvgbDgkMRRatuT-HZyfoIN7oJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15cb98fdc3.mp4?token=aafOdeBHP6PQ1HbBR7-IvEBVaxN5ctUW6Ft9uxGNm3AuIbUJnjxPyYaGbvYP5FpDvWEerzDICQC0Wdlq2YAh6SymQosfgg3uynds6iRHBKUtX78uGEZBLWN2TUnrKRcKP3jAeaPfq2FGS2inQT1kUxNA9Bm2EgajsrU2EH9m3XOYgH_RvmRo-vj_Ne5QJOKnatZSsf87AnQneT7INnniDqNsYO-EkkV5KTwIxoIH617tkY4RyxIKq83C93tv2l3mO2MmHXK2nT_92pVTMypUGPiyfjBVdg7cwBH9gu23CuA0zG2BBIXWf9koN886LvgbDgkMRRatuT-HZyfoIN7oJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
المتحدث باسم لجنة مراسم تشييع جثمان السيد علي الخامنئي: سيحضر مسؤولون ورؤساء ٤٠ دولة في مراسم الوداع والتشييع لقائد الثورة الشهيد.
▫️
سيتم الإعلان قريبًا من قبل مسؤولي وزارة الخارجية عن تفاصيل مستوى الوفود المرسلة، والدول المشاركة، وأسماء الشخصيات الحاضرة</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/80450" target="_blank">📅 10:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80449">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20c0d32e61.mp4?token=AvX8FIpgJncUH5VtnNOoV_WUAZr0Xiw61Df2Q4yQ1CrDlFEcLkFEv95o5OBEuU0WXpdguT0u5D-QKw9p3KNLzlBGzeG0qROx-LADP7-avsbcoCXQS5Yfusd7RXUvNcjX236CVQVCypu5PB6YdxNxZi1RZvETaa036XbKo9c1yPmuzwl4q2CSO1v-vYUlSt2j4NMuQ-nlX-tWdcCJ4XK8bJxdsfJYXumdXhwdh-_BsLFjrLW_lax2nERCI89cJlrVzpG2h6Jp6U2oVZ4easCA2IgWvnxscygM0VLz7viSRy0LWWlsNNciVUi7ojtVs_95YFTtXc8SeNmdHd4DX_xj6C2cTWHq3YPDWLJGrf-zZ2wAA8FIsSLgfH2fTpMyYE2AzNuUt6BxkGZZgQ5D98wlMFo3FeJSPgB8houh97gIp9JGhjRbPQKc-yHC4MIma9sBGCfhomlfERYj4ulCrBjmZmTk952d0wb6HFC0PNriwemJ6Po2RZZ1tnKM67VIByMbHLAcYz18KfNTIe1tFMYwL3jtneVCdAgHnb-irJgbKhdRgRLVaga5w5boJY0ce6TnP7i9Cf0gUE1d7x9ez39EpqIKua9ArFb27RVnGvCLc76V-etTSLO_XN1-xCrKU09z9x7qPWz84k2g4HtBhp1CeNIMjapoTxhz36PqSfTH9hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20c0d32e61.mp4?token=AvX8FIpgJncUH5VtnNOoV_WUAZr0Xiw61Df2Q4yQ1CrDlFEcLkFEv95o5OBEuU0WXpdguT0u5D-QKw9p3KNLzlBGzeG0qROx-LADP7-avsbcoCXQS5Yfusd7RXUvNcjX236CVQVCypu5PB6YdxNxZi1RZvETaa036XbKo9c1yPmuzwl4q2CSO1v-vYUlSt2j4NMuQ-nlX-tWdcCJ4XK8bJxdsfJYXumdXhwdh-_BsLFjrLW_lax2nERCI89cJlrVzpG2h6Jp6U2oVZ4easCA2IgWvnxscygM0VLz7viSRy0LWWlsNNciVUi7ojtVs_95YFTtXc8SeNmdHd4DX_xj6C2cTWHq3YPDWLJGrf-zZ2wAA8FIsSLgfH2fTpMyYE2AzNuUt6BxkGZZgQ5D98wlMFo3FeJSPgB8houh97gIp9JGhjRbPQKc-yHC4MIma9sBGCfhomlfERYj4ulCrBjmZmTk952d0wb6HFC0PNriwemJ6Po2RZZ1tnKM67VIByMbHLAcYz18KfNTIe1tFMYwL3jtneVCdAgHnb-irJgbKhdRgRLVaga5w5boJY0ce6TnP7i9Cf0gUE1d7x9ez39EpqIKua9ArFb27RVnGvCLc76V-etTSLO_XN1-xCrKU09z9x7qPWz84k2g4HtBhp1CeNIMjapoTxhz36PqSfTH9hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
المتحدث باسم لجنة مراسم تشييع جثمان السيد علي الخامنئي: سيحضر مسؤولون ورؤساء ٤٠ دولة في مراسم الوداع والتشييع لقائد الثورة الشهيد.
▫️
سيتم الإعلان قريبًا من قبل مسؤولي وزارة الخارجية عن تفاصيل مستوى الوفود المرسلة، والدول المشاركة، وأسماء الشخصيات الحاضرة</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/80449" target="_blank">📅 10:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80448">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔻
الحرس الثوري: أصوات الانفجارات التي سُمعت في بندر عباس من الصباح ناجمة عن تدمير ذخائر متبقية من الحرب</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/80448" target="_blank">📅 09:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80447">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a71a250766.mp4?token=d2nLDz02gGRr04QpyDxq4m8HEP26hjTuVtg_OsBE-_MT9qF-8q2UXYnd1ofhAlW1rqDcgSWFEj38zCRg_w3X_AxlkUqcgFwRXfj1JaB2VxC-0AyB3K4BmKNa-4-lgg1-epaHJsRoTZmjLbHsjyRK4cr5AX3mlGQcSi_UzYIeUIcMeilFuYJmXyzxRLh5uGq0m93Rb6wxkESZjLdgBrepHpdr1mqZLvBUB7jZqMQWrmfwLD4rXlYcbo1S0-tPviaKapgXHtS8xMZs9k8xHgyHm3KKJBfPydu6oyBtwDlbx1pDlIciSZUuyBv_7QieNTgTSKD6klkamVByeb8NmDSWQIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a71a250766.mp4?token=d2nLDz02gGRr04QpyDxq4m8HEP26hjTuVtg_OsBE-_MT9qF-8q2UXYnd1ofhAlW1rqDcgSWFEj38zCRg_w3X_AxlkUqcgFwRXfj1JaB2VxC-0AyB3K4BmKNa-4-lgg1-epaHJsRoTZmjLbHsjyRK4cr5AX3mlGQcSi_UzYIeUIcMeilFuYJmXyzxRLh5uGq0m93Rb6wxkESZjLdgBrepHpdr1mqZLvBUB7jZqMQWrmfwLD4rXlYcbo1S0-tPviaKapgXHtS8xMZs9k8xHgyHm3KKJBfPydu6oyBtwDlbx1pDlIciSZUuyBv_7QieNTgTSKD6klkamVByeb8NmDSWQIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
المتحدث باسم جمعية الهلال الأحمر: سيتم نشر ٢٥ ألف متطوع، و٣٥٨ سيارة إسعاف، و٢٨٠ مركبة إنقاذ، وأربع مروحيات إنقاذ، وأكثر من ٣٠٠٠ دراجة نارية إنقاذ في طهران لإقامة مراسم تشييع الشهيد السيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/80447" target="_blank">📅 09:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80446">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔻
الطائرة المسيرة استهدفت منطقة الخضراء ومن الممكن كانت تستطلع سفارة الاحتلال الاميركي في العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/80446" target="_blank">📅 03:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80444">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59de911ab6.mp4?token=DK1i0X4rHdf9tnFVwUbO89f6ln7kj77MRqkxFRkeS-OSbxfOkUPtAmTiiEP2D3Lo2_OdqTFD7c9ifrwNYMIFPQVXwjJj9Loj1WYu8qdyo5Y6IKPZAFLlrCy5Rh3YxFl58ZhtK9JIFi372aC1YopI6QXiO9M8g6N4cjsGu0YP6FEPQMH7hnMnZZs2Ol7mcWRnx8qQx1MhieVB_vlStrIPbimhFCgpA5wZkm37LZkHHsr8gykBLww8teO-daQobkHVMqUWi-wfqGEnEsNhgRZKnryoQWEg2yeTsHEDK8I1GFEC0nESoUHBlUW5le4WDkhzAwqEs7MNRgA3FdHfSR8bDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59de911ab6.mp4?token=DK1i0X4rHdf9tnFVwUbO89f6ln7kj77MRqkxFRkeS-OSbxfOkUPtAmTiiEP2D3Lo2_OdqTFD7c9ifrwNYMIFPQVXwjJj9Loj1WYu8qdyo5Y6IKPZAFLlrCy5Rh3YxFl58ZhtK9JIFi372aC1YopI6QXiO9M8g6N4cjsGu0YP6FEPQMH7hnMnZZs2Ol7mcWRnx8qQx1MhieVB_vlStrIPbimhFCgpA5wZkm37LZkHHsr8gykBLww8teO-daQobkHVMqUWi-wfqGEnEsNhgRZKnryoQWEg2yeTsHEDK8I1GFEC0nESoUHBlUW5le4WDkhzAwqEs7MNRgA3FdHfSR8bDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
الطائرة المسيرة استهدفت منطقة الخضراء ومن الممكن كانت تستطلع سفارة الاحتلال الاميركي في العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/80444" target="_blank">📅 03:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80443">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">هجوم بطائرة مسيرة على منطقة الخضراء</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/80443" target="_blank">📅 03:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80442">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4c7bc3f30.mp4?token=lwxrUSsEr7-uJflralDFtveApoTKPK7z6dwgtzVR3dXuFsqkdkEtqXu_0Lh4ES8uxaW09JHSW1BRkulGNSG1Fg9Vm6HJkQ_wvZXsYmIdUhEb6u8frMbB7cCXQMStIbxT87_x2MY8ByT3tVWhxHVvJjCxKg3DPi9avrJPa0NiJE0Kx_bu6YdvHMU7NpDqbOzn_vWgHmeknuActfTDsEwj4r9wnXsZ7qna3gKw5yYFl7cF50z-j8QJ-hT1VJo0a4IWra55gb7GXHH9NmFK3d3aCBxwuhKLQkO21RgRdSAUfe0R6D7AsKCEEvjlJyuPknyZhbGDl_L9ZoCu5o1L6VlOaYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4c7bc3f30.mp4?token=lwxrUSsEr7-uJflralDFtveApoTKPK7z6dwgtzVR3dXuFsqkdkEtqXu_0Lh4ES8uxaW09JHSW1BRkulGNSG1Fg9Vm6HJkQ_wvZXsYmIdUhEb6u8frMbB7cCXQMStIbxT87_x2MY8ByT3tVWhxHVvJjCxKg3DPi9avrJPa0NiJE0Kx_bu6YdvHMU7NpDqbOzn_vWgHmeknuActfTDsEwj4r9wnXsZ7qna3gKw5yYFl7cF50z-j8QJ-hT1VJo0a4IWra55gb7GXHH9NmFK3d3aCBxwuhKLQkO21RgRdSAUfe0R6D7AsKCEEvjlJyuPknyZhbGDl_L9ZoCu5o1L6VlOaYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم بطائرة مسيرة على منطقة الخضراء</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/80442" target="_blank">📅 03:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80441">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">انفجارات في سماء العاصمة بغداد</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/80441" target="_blank">📅 03:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80440">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اصوات قوية تسمع في بغداد</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/80440" target="_blank">📅 03:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80439">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اصوات قوية تسمع في بغداد</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/80439" target="_blank">📅 02:57 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80438">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4747a2157b.mp4?token=osIvQ5Xg2PixHduTW2ko3AnXnfw3ylyQou4b6B0l_LvQ5m4lGjdelpS6MXakxdvvLKN-fjzM6K9Z97WW6VlddY13yqU6wQks77gnZ1vPUYRXzIJBgYglxcCSE9T1fuJLUb9A_aFL0WNtH5Yu5vk_ORHf3cwUKPYvbDRlK9QG_zv4LbM9F7NMJHjJ-6cDF_XlXcBV0FpTbQPoN5VGzbvXZQeKaPOzef8PAG72bQlExHTyDsoscZpeAsZ4KUsQngGEVADUnflKCpZan_bPqQVcE80eW1an2QBtBczRLhl_mluRUL-LUEaBCaxb7UXw1bhXkHTBlnp9oenOeq4FZFgIjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4747a2157b.mp4?token=osIvQ5Xg2PixHduTW2ko3AnXnfw3ylyQou4b6B0l_LvQ5m4lGjdelpS6MXakxdvvLKN-fjzM6K9Z97WW6VlddY13yqU6wQks77gnZ1vPUYRXzIJBgYglxcCSE9T1fuJLUb9A_aFL0WNtH5Yu5vk_ORHf3cwUKPYvbDRlK9QG_zv4LbM9F7NMJHjJ-6cDF_XlXcBV0FpTbQPoN5VGzbvXZQeKaPOzef8PAG72bQlExHTyDsoscZpeAsZ4KUsQngGEVADUnflKCpZan_bPqQVcE80eW1an2QBtBczRLhl_mluRUL-LUEaBCaxb7UXw1bhXkHTBlnp9oenOeq4FZFgIjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
تعزيزات امنية كبيرة تتجه صوب قضاء قره تبة في محافظة ديالى.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/80438" target="_blank">📅 02:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80436">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/prcO7wSCA2EtK--aNuIb6eSRngd9ettmjf86SNAPJfIscwsgBWpVPdZxMCbCMuoi0A0sDAYli42oxiNBvDpgu1TZILovsbzCBztKD97ntpTeHsBufX1L-LiqjjxpYZ1Rl6Q_c9RAwcHAZkcj3bOvsVnUEKQENWGrS5AYvEoB25e_lBU1cnM6umbrFbSxEs9sgN1iQT_YRWnaBDfr2MsxVO3KXJUNei54kGp0l0ezQ3c80Rs1wRlLAarGe3nPHYN7FpNcxCg3m4mQ2RRmd5LiPglJ-gMctG7SY_cRaDFdXwe6MAW5Z5Pqt1VYxVIf3bih8N1G6KOSlYKirxrf5Gkocw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mU9lGa5NhMyRiFONoiWc-B1ZAp1HOHeSFAYNOMZokJJI6IYZNNUrhbNYNlQORuMfWG3qrtZ6cL4vtxj_8zaIyJb7O9kWqkK4OSul6YADVbauXzDyGIunYchhNcL6H_ASgFjBPQEkWXmWtevvfSUDlvQRSLAwUBkNy30DmTIZl-DcwVZ-V-vpAqZQc86iG2a5IohPrkfFqUuxiCbWiF1zWyQwsFxvFO1KzCEj-CCEPlimgvH_kuJdf5qPPKaSqwsTwmhJc52ujJryV21aF8uWP1mSn2W8-VHdOdXFptMxKPB2pGp2KZGovBkxhUgN-EZrh3S4HE1RXTnjlt8NszbEhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
متداول
: اشتباكات وإطلاق نار عند سيطرة امنية في قضاء قره تبة في محافظة ديالى بعد رفض شقيق النائب عن حزب تقدم أحمد مظهر الجبوري الامتثال لأوامر التوقف ما أدى إلى إصابة طفلة كانت داخل المركبة وفراره من المكان بدراجة نارية.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/80436" target="_blank">📅 02:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80435">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔻
رئيس البرلمان الإيراني قالبياف: لن ندخل بمفاوضات جديدة مع واشنطن حتى تنفيذ شروط مذكرة التفاهم، وهناك التزام أمريكي وفق مذكرة التفاهم بوقف الحرب على لبنان وضمان سيادته و صدرنا أكثر من 40 مليون برميل نفط منذ توقيع مذكرة التفاهم.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/80435" target="_blank">📅 01:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80434">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UH9qJ_HcB9e-mJA4UhngVO-LSQIAoJTQrSeqyJUVCs3gWmc-sJ-j-Blg7r73ci9rTeBKhc_5hd_3iQJ-woyjckGcXbm1L4GpefG70pT9J-rKss7lb0UJNpS-M8xE4zmWreqO7sLFtpQ2fTZ9fCDMWhzTDJEYCv54qeXnUziLQS9VWHZ4leTgAnVdrgwF81qZhkb-GANvrRniM1Pn7BTLmd0x2BRo_yVC9XHpjrWeVNlIAiIXgslNz0Pv0dd1hdWykx8ADjYBNPAtOpIac7iUlBYjx6yzChDLTW39IttCeMHQQi2cd9oxg3LcCiKH2EdyD_DnXDYP-WJschT75mKOAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
اعتقال الطفل عباس إبراهيم نصر القلاف في البحرين على خلفية حضوره في المجالس الحسينية.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/80434" target="_blank">📅 00:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80432">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/577a8900f6.mp4?token=XqqEpoDFqlwOY4O1wSopvevoEttpC6RGKYW7AeJ3gn3udempuhUw-oDsyweOXLNVlYhVAUyVbH-dvPGfnXGQrT_soYegpl2FiBOb3A9MJrvGmWj0SqazWt3P67oP0tv47_uU9NaHUgoMcQ926KmuULAOEnCyehmB67mByA05DzKhRqfgGAadv11l3uPfx6mGkAKDTTTR-Ad73ZCfQiPxHd2LliLJ707OhbwrjAb1M6x5Lld258bdRI-m27UJuJXHKZmt8kG_a_Q7f3WkFoW3A6JrVktrCZKK8lbd-QtG9r0iuUOzTrD105LcIrzNJ5YXgyEly9UgZbhpIXIibpfCWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/577a8900f6.mp4?token=XqqEpoDFqlwOY4O1wSopvevoEttpC6RGKYW7AeJ3gn3udempuhUw-oDsyweOXLNVlYhVAUyVbH-dvPGfnXGQrT_soYegpl2FiBOb3A9MJrvGmWj0SqazWt3P67oP0tv47_uU9NaHUgoMcQ926KmuULAOEnCyehmB67mByA05DzKhRqfgGAadv11l3uPfx6mGkAKDTTTR-Ad73ZCfQiPxHd2LliLJ707OhbwrjAb1M6x5Lld258bdRI-m27UJuJXHKZmt8kG_a_Q7f3WkFoW3A6JrVktrCZKK8lbd-QtG9r0iuUOzTrD105LcIrzNJ5YXgyEly9UgZbhpIXIibpfCWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
انسحاب جميع الحفارات، مع بدء انسحاب أغلب القوات الأمنية المتواجدة في الموقع بمحافظة بابل.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/80432" target="_blank">📅 23:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80430">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/plZD1ZOIvFs3MjUGpyLpbM53ZK8s7sHNl-EyAtRHSnWN0zpO30c4Jqw8TwdMr24Mbx61LV5JOAWRP2flHLZ9-BiKVTCZh5jokT0N719hbRcBZ2wNsLSYWaKHXKnDsRcP4o5oAH2H3x-3DW8x2LmxUVTId0K6vXugfp-UG0tMf1VLwWW0XXxQ4ACQzAY7WymXh5uCspp_3t74Gvw36HGvkMHMLYFitgj6TFckysxojvARTPGEPYFT0gtDhLjYUviehdvIMfn4jLJ7zNd7jPf0ssmHMFIZAKnyBbAkF0AqNRz47-wa76MUUZehvja25hNsZdyiNyKpkzpXeoxRdj_DSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KI2UIGnQosIEmMiCGCoRXD5bRGgqINtGLBWaH2p0zc_pdRPXW0LHgdw6Cw9Ds7LI7ruyxXUlj0Gb_m88TWRnjv9-qkqCEVCsObuck7AGj5-ulyI63ZzM6e7DL52eHA1gQmRwpCFZBuaARq6NHVCHq0H7aNnOjAB93HJwNLDddl_ZzuAFQI1726VYHXZtBQoKuLO-NwQPihVdSt-mSTpUbenXvK4Stydo15q75UJ3RM5vf-xSHcO2xV4YWboB_FAOv3BsqXp9-2cLRYudpmP_BKhHllwnZ9bUJK_8sp79nCkIk8Dh3CTCfdNwCC7_hYGIsCdk3X0F96SRy1T9McTd0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
بحسب تصريح عضو مجلس محافظة بابل حسين عليوي، تُجرى أعمال بحث وحفر في ناحية الشوملي بمحافظة بابل بحثًا عن مبلغ يُقدّر بـ32 مليار دينار عراقي.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/80430" target="_blank">📅 23:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80428">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0addd9e39.mp4?token=MVZ3mk7sGwI9xY8cTiRI9HlTSKbRCHkGRvUhxoEBoU4fx0sPtvFJtY6vB8C6E_BbJz1-oprLzvSN-uU6Xn48XjyQrwo5hNMYFUNERmENlSET2Tc4O3TcdQXcoxokTCBLYliWd4Jiax0vwUoQBBS7D1QJZNgGj86bZdYHxZunb23MLBPiIRFLXWAEAnCMdGF_pwSbSfZmPCH-ZHLcS2XGRoKZlZLcfFDtmXviUSkpsig5Gv7KqG_X3SbIhGKCybnItJifEbthlz4nFHOhd51zpdlaIKBMo94LFu8U8wFBCXLc8CsvWoBw2c3x2kdKBjM-arMFxNLFLdvgXLdOzIs21A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0addd9e39.mp4?token=MVZ3mk7sGwI9xY8cTiRI9HlTSKbRCHkGRvUhxoEBoU4fx0sPtvFJtY6vB8C6E_BbJz1-oprLzvSN-uU6Xn48XjyQrwo5hNMYFUNERmENlSET2Tc4O3TcdQXcoxokTCBLYliWd4Jiax0vwUoQBBS7D1QJZNgGj86bZdYHxZunb23MLBPiIRFLXWAEAnCMdGF_pwSbSfZmPCH-ZHLcS2XGRoKZlZLcfFDtmXviUSkpsig5Gv7KqG_X3SbIhGKCybnItJifEbthlz4nFHOhd51zpdlaIKBMo94LFu8U8wFBCXLc8CsvWoBw2c3x2kdKBjM-arMFxNLFLdvgXLdOzIs21A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
وزارة الداخلية العراقية:
تكرّم منتسبين أحبطوا محاولة تهريب أربعة ملايين دولار في إحدى السيطرات، بعد رفضهم الرشوة تثمينًا لجهودهم في إنجاح العملية.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/80428" target="_blank">📅 23:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80427">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔻
وزارة التربية العراقية تقر شمول طلبة الثالث المتوسط والسادس الإعدادي غير المؤهلين بأداء امتحانات الدور الثاني</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/80427" target="_blank">📅 22:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80426">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔻
رئيس البرلمان الإيراني قالبياف:
لن ندخل بمفاوضات جديدة مع واشنطن حتى تنفيذ شروط مذكرة التفاهم، وهناك التزام أمريكي وفق مذكرة التفاهم بوقف الحرب على لبنان وضمان سيادته و صدرنا أكثر من 40 مليون برميل نفط منذ توقيع مذكرة التفاهم.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/80426" target="_blank">📅 22:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80425">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقوموا لله</strong></div>
<div class="tg-text">لنستقبل أكبر تشييع في التأريخ
#قوموا_لله
#باید_برخاست
#KHAMENEI
https://t.me/in_front_of_the_martyr</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/80425" target="_blank">📅 22:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80424">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCIKS_floG13kuUQ-6AOsSKUJvzA5Ge2cxjykGI4VHaBUGgTtPOXJi-C7O_rzHpyLKc1iFLdTdYRm5Ynldzd0WJtPqxsdcY8ven4kjWFDK5UlUbg9g2FcFuh4ieMhMNIGKOfSqliSAAdDac6aKOPeeiMAPyRLEbmM4LXB_eAfjOeFsCVoR4_1BPblwlrJwBeBLyWZJ7TfXEVt7lDvLyDuYdTZPF8OJTeNJCYat07aHJ6_bHKwiuQtt7q2N8qSA1IX-RroLyMBNZiwl6xXAGuw-GfVnnCCWydknzzXgghcleXlKEyKgmjft4SXOYJ4Rj6Mhk536yj3ZVTambFcG-3Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇶
عراقجي:
خلال زيارتي لبغداد، التقيت بالرئيس ورئيس الوزراء ورئيس مجلس النواب ووزير الخارجية وغيرهم من الشخصيات البارزة في العراق. ‏على غرار إيران، يستعد العراق لمراسيم جنازة جماعية للشهيد القائد السيد علي الخامنئي، وهو حدث سيخلده التاريخ بلا شك وسيعزز الروابط بين بلدينا.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/80424" target="_blank">📅 21:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80423">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
عملية دهس في إحدى المستوطنات.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/80423" target="_blank">📅 21:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80422">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع:
خبر دفن جثمان القائد الشهيد "وديعة" في مرقد السيدة معصومة (عليها السلام) عاري تماماً عن الصحة.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/80422" target="_blank">📅 21:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80421">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVSmH5n56rFBb5erZ0ZL9ahyy9X7XlYtr1W-g-XHLNYC1iiYhI_7EP4Qw60-CYW_vV2WW-IgcjdmBexwk6AvjDCwytxV918t5ZesCIJYSQDNGwtF0yVn7TfhsDw37oUNiS1QVNVPSBD9jhHgrmOsO87J_i-QfiMS5Kdd3Xpvoo2R93RDBzXtSX02eDl2EFCUNXRf1IdiY4xkg1dAqazsvx3AEKSZimopEUw45dtcPXPPEeAlUYbgjwoPx4tqHwBrVsr4xD2FWeJ3wtHkl_I2ktNkW5ggUptTugMJOb1x2GqE7B9H3mG8459Gor9tlIZerfGIKVBtr2mgpqIYjQXOww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
وزير الخارجية الإيراني عباس عراقجي:
تم إنجاز المهمة"، السيد مولين.
‏لقد أنجزتَ شيئًا آخر أيضًا: إثباتك للعالم أنك لا تملك أي حق في استضافة بطولة دولية. لقد كان سلوكك مثالًا صارخًا على كيفية إهدار الكرامة التي تأتي مع كونك مضيفًا.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/80421" target="_blank">📅 21:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80420">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇶
هيئة الحشد الشعبي:
بسم الله الرحمن الرحيم
﴿وَمَن يُعَظِّمْ شَعَائِرَ اللَّهِ فَإِنَّهَا مِن تَقْوَى الْقُلُوبِ﴾
وتحت شعار: (قوموا لله)
تدعو المديرية العامة للإعلام في هيئة الحشد الشعبي جميع وسائل الإعلام المحلية والأجنبية، والقنوات الفضائية، والوكالات الإخبارية، والإذاعات، والصحف، والمواقع الإلكترونية، والمصورين الصحفيين، وصنّاع المحتوى، والراغبين في تغطية مراسم تشييع قائد الثورة الإسلامية السيد الشهيد علي الخامنئي (قدست روحه الزكية) في محافظات بغداد والنجف الأشرف وكربلاء المقدسة، إلى ملء الاستمارة الخاصة بالتسجيل، لغرض إصدار الهوية التعريفية الإعلامية التي تخوّل حاملها الدخول إلى مواقع التغطية الإعلامية وممارسة مهامه خلال المراسم.
الاستمارة الإعلامية
للاستفسار والتنسيق:
القنوات الفضائية والوكالات المحلية وصنّاع المحتوى:
* 07713513822
* 07737599025
* 07713282065
الوكالات ووسائل الإعلام الأجنبية:
* 07710066020
المصورون الصحفيون:
07807172059
ملاحظة:
لن يُسمح بممارسة أي نشاط إعلامي داخل مواقع التغطية إلا بعد إكمال إجراءات التسجيل واستحصال الهوية التعريفية الخاصة بالمراسم.
اللجنة الإعلامية الخاصة بمراسم تشييع قائد الثورة الإسلامية، آية الله العظمى السيد علي الخامنئي (قدست روحة الزكية)
٣٠ حزيران ٢٠٢٦</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/80420" target="_blank">📅 21:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80419">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVMjM_NnZIMoeycMjy0j63jh2kfrfzjy03_7FA7O7cEYwpxVMYRKWHoEFgthMXXfAd13EUi3-kEjqcgXq6O6BWFB5hQssdROLRdLuFedUyvIAuwDGQ_aWN4cR8M7ybxYRp7C7TIrQ2w6fXDJbcbBjfSvEnwHnlsy0-74fC---AGIoEtgoC6ToSX-rXiL_Mbq0OG-4cgOpy0qv-JVqnW4UN8lkjf8XtZ2A2i4vjHcpyZn0FJ5dnJnnLqI8ZGIqaErHS0ybuPm8Ws-m55LyIXNkPiJrxUz8etuoE7Eteth8p9yxh4H0zVJiK_c9s3qvunaUqqHUJRQZ8RBjEfREP9Gtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نعش الشهيد القائد الإمام الخامنئي رضوان الله عليه وعائلته الذين نالوا الشهادة على يد العدو الغادر الصهيوأمريكي.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/80419" target="_blank">📅 21:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80418">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">⭐️
تانكر تراكرز:
صدرت إيران 50 مليون برميل من النفط الخام منذ رفع الحصار الأمريكي المفروض عليها قبل أسبوعين. وهذا يعادل 1.66 مليون برميل يومياً حتى يونيو 2026. أما معظم دول المنطقة الأخرى فلا تزال بعيدة كل البعد عن مستويات ما قبل الحرب.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/80418" target="_blank">📅 21:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80417">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXU1IuSrzGe9UNfxXiChypbvKMGC29Mk2-20GAT_vkz9gzF6Z3cIxCOuL0pda7TOU8hoIoKGVrl5BKVvyUGoMRxQJo8WJK-5rmAxevkfWWeHFL8CK5lTmsqwHyMLnqjz19PGWiNYHf6pZuGxXK9HeudTsSm3ZFLLpe3y0t4QEKxPEOHHIJfzGax_OG5dmJUEl2aqk18rISuBjgZQkpRl8xF11a7Cy5Bk_Mt8v2wJuoX4w66v-iW_593lhKHVchYliPapJ0OdL9NeW3a6b_0ceN_MQ8IoYqBt525Pzx_VyuJdp0hIs7yHnbNtj7Cu7L4jKsLeQkLQJumiEr7yOu2vuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب ساخراً:
أود أن أهنئ الرئيس شي، والدولة العظيمة للصين، على فوزهم الضخم في مسألة "المواطنة بالولادة".</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/80417" target="_blank">📅 21:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80416">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3r6frViEseLVzDQ8SGu6um9qso1OyTGlWXJhUhe8XRT4gna63Nssb8O5bjeIGfpoeR60ZgWxkum0g7JJQ4-fJS56rIe8dVCnYVTthXVLbXQClKO0StpUxb5lWofWFn3sgTCRXdkH1rSckzcI8_NYudT6R6wzFXzm_hqYA4rp3xrwQhfR9NcMYnclC3-sGznVNk6VfCvCtiEDrf4Dv4f5EotCbs20VHSWPQ0xCJ6LMpFE91kqcndQOMr8yeBS8DqUY5tc6ccBhAFIKum4maAKlNq4eu193aisBbjVAOoM2HJ9Mo-r5nHyl8zm-9-cDkN2ckzyE_golg7HeMUd6x1NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو ينشر صورة يزعم أنها لفلسطيني تم إعتقاله وتعذيبه على يد جنود جيش الإحتلال الإسرائيلي.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/80416" target="_blank">📅 20:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80415">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">⭐️
المنظمة البحرية الدولية:
تم إبلاغنا أن الممرات التي قدمناها ليست آمنة.
علقنا إخراج السفن العالقة في مضيق هرمز بعد الهجوم على ناقلة نفط.
ننتظر موقفا إيرانيا بعد الهجوم للسماح لنا بإخراج السفن من هرمز.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/80415" target="_blank">📅 20:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80414">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية:
اجتماع الغد الذي سنشارك فيه في الدوحة سيركز على موضوع الإفراج عن أموالنا المجمدة وإيقاف الحرب في لبنان.
البند 13 واضح بأن بدء مفاوضات الاتفاق النهائي رهن بتنفيذ بنود أهمها وقف الحرب على لبنان.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/80414" target="_blank">📅 20:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80413">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇮🇶
🇮🇷
اللجنة العليا المعنية بتنظيم مراسم تشييع جثمان الشهيد القائد السيد الخامنئي في العراق:
تؤكد اللجنة العليا المعنية بتنظيم مراسم تشييع جثمان الشهيد القائد السيد الخامنئي، رضوان الله تعالى عليه، أن جميع المواقع والمنصات والوكالات التي تدّعي تمثيل اللجنة المكلفة بالمراسم هي جهات غير رسمية، وما يصدر عنها لا يتعدى كونه توقعات أو اجتهادات أو معلومات مسرّبة غير معتمدة.
وتوضح أن الجهة الوحيدة المكلفة بهذا الملف هي هذه اللجنة، وأن الناطق الرسمي المخوّل بالتصريح بشأن هذه المناسبة هو الفريق سعد معن حصرا.
وسيصدر بيان تفصيلي عن توقيتات ومراسيم واماكن التشيع (في النجف الأشرف وكربلاء المقدسة) من اللجنة الإعلامية المشكلة رسميا برئاسته.
اللجنة العليا لمراسم تشيع جثمان الشهيد القائد السيد الخامئني رضوان الله عليه
٣٠ حزيران ٢٠٢٦</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/80413" target="_blank">📅 19:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80410">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a935b97b50.mp4?token=KBCiFy3MPli4ciWD7cUxmbUhbzAMIZRQNMeRlyALVYn-O8cgXSxpsQY8jqTBBLbgEQlaAqv83aCALbaMPY8d8c_lhsVmIyzMVyHF-SiMRPNtLae7vmwZOQ5sbpbcQXk46KeyRZVGf1JfVtcOdKWnbrcAUaXK64igT7nsu-o2ngWy4qQ549JIRI7iaFN_hQLi9Oaoi0MUw0uNCnFelVy8pUazOoQjYrrc1qo9UrTDAykmJt_k-CzqXm-U7bzyXGAygR0KR7YppH-S7bwzuGGsqbuxvZo9FODRQZpCSmGXjVSSe2MeYTRi_U8H1ayur-osveqvchmH-_FoMNcAHHsqpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a935b97b50.mp4?token=KBCiFy3MPli4ciWD7cUxmbUhbzAMIZRQNMeRlyALVYn-O8cgXSxpsQY8jqTBBLbgEQlaAqv83aCALbaMPY8d8c_lhsVmIyzMVyHF-SiMRPNtLae7vmwZOQ5sbpbcQXk46KeyRZVGf1JfVtcOdKWnbrcAUaXK64igT7nsu-o2ngWy4qQ549JIRI7iaFN_hQLi9Oaoi0MUw0uNCnFelVy8pUazOoQjYrrc1qo9UrTDAykmJt_k-CzqXm-U7bzyXGAygR0KR7YppH-S7bwzuGGsqbuxvZo9FODRQZpCSmGXjVSSe2MeYTRi_U8H1ayur-osveqvchmH-_FoMNcAHHsqpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
استمرار عملية تجهيز مصلى طهران لإستقبال الجثمان الطاهر لقائد الثورة الشهيد السيد علي الخامنئي (رضوان الله عليه).</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/80410" target="_blank">📅 19:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80409">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">قوة امنية تطوق منزل معاون مدير عام مصافي الجنوب في منطقة الجمعيات بمحافظة البصرة جنوبي العراق.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/80409" target="_blank">📅 19:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80408">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">⭐️
‏رئيس البرلمان العراقي "هيبت الحلبوسي": لن ندخل في توترات مع محيطنا العربي من أجل إيران.  ‏أكدنا في السعودية أن العراق جزء لا يتجزأ من العمق العربي.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/80408" target="_blank">📅 18:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80407">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKi-2TsS-hI-H1C0Qb3FblflH-kPKLDDjVZSdnIIKaBNIFX8w9Gn2ooGbihMqGywqrtsKInJrWtjO3xrIb4Aci1QIq7WXl5sJVuC4yjU_20pGCHXIVO_xEBhGVypl7eQmrlGqM2QegskOdZj8xpI-Dd-adFad997OCET0fe4ApexX5rxPVxYUei9mY9DeTT9lp2AIwI8ADhSHeJS1BzYRdXrxv_SW5ZKiaTW67kPD4pMW3fCU0N7QFgJ2G2MFAuqcLi6p_-K5wGV4_cYGFQFoEVEK-1jD4tltB2IwGTfFxqVIwaHBSjlmjh8k39PFCVAwjuUC3JolgOP-eXCRf4VmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏
ترامب:
«انتصار كبير: المحكمة العليا الأمريكية أصدرت حكمًا ضد مشاركة الرجال في الرياضات النسائية. يا للعجب! هذا ينهي هذا الوضع السخيف تمامًا!»</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/80407" target="_blank">📅 18:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80406">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">⭐️
‏
رئيس البرلمان العراقي "هيبت الحلبوسي":
لن ندخل في توترات مع محيطنا العربي من أجل إيران.
‏أكدنا في السعودية أن العراق جزء لا يتجزأ من العمق العربي.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/80406" target="_blank">📅 18:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80405">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🌟
إعلام العدو:
"ألقت الشرطة وجهاز الأمن العام الإسرائيلي (الشاباك) القبض على مواطن أمريكي للاشتباه في تجسسه لصالح إيران".</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/80405" target="_blank">📅 17:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80404">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">من عملية تجهيز مكان وضع الجثمان الطاهر لقائد الثورة الشهيد السيد علي الحسيني الخامنئي في مصلى طهران.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/80404" target="_blank">📅 17:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80403">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">⭐️
نيويورك تايمز:
بعد الحرب الأمريكية الإيرانية، اقترحت عُمان نظامًا جديدًا تدفع بموجبه السفن التي تستخدم مضيق هرمز رسوم خدمة، حيث تدير إيران وعُمان هذا الترتيب.
تقول عُمان إن الدفعات ستكون طوعية وستساعد في تمويل خدمات الملاحة والأمن والبيئة، بينما أشارت إيران إلى أن الرسوم يجب أن تكون إلزامية.
تعارض الولايات المتحدة أي رسوم على المرور، مشيرة إلى أن المضيق يجب أن يظل حرًا كما كان قبل النزاع.
أصبح الاقتراح قضية رئيسية في محادثات السلام الجارية بين الولايات المتحدة وإيران.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/80403" target="_blank">📅 17:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80402">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYxA0foo1LaLy7w_i3b7kbFFRbqEoMYQfHz-PipUE33y9gvsxneqcN3ZbYR4tWfoK8JeeFOEW9xllMUQki9OlQ5AB0G2aS0anPvzvziA_1FG4wybkSSKSngJBJu5P9td32xvHNI70Sfjqda6PuAhYllAbqMN645bfY6rxFNc--N2J4Tc1EKkhkUz7Ebv1u164TQDdFwiIfeZyn00RpNTtfm4gjx2TPgI7GftVWnLjebPQl6hJvd0B_0Ztvt6MIHF9BkPr7QheNdyX0NRl-ZEbIzsVGAVI--zh6c-wb42COhAXEbDTnqNawfcZUOvdthxqq7SlQFOA1F7ftG8o89flQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
نتنياهو ووزير الحرب كاتس زارا اليوم "الحزام الأمني" في جنوب لبنان بعد توقيع اتفاقية التفاهمات.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/80402" target="_blank">📅 17:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80401">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKvoOORkgGKOuBZ5UJWljZWBobDVQyfs-As2vcLgRC32KNc0jaHpIIe-BNrMyxDUpNjkghDFqBIdzKDWOuxh-jecMeCOQsYAl2vkPVfm1c8gu9UH5CZhDOHnlbGQc_fFJ1n6ya9WBt02A_reKQDR2w-f-VFC70SQdIQZYcjx5Oc6URisNgzYdp4U0P-H9436rMdyX1HjMJfM6FOqhDjekMR8ICo8fJD0C-T_WXC_N3U1wpxAy3tWucPjYwgrY19egh38fAML7ATo5Uggj--AHNFDRhXKQw-v0_TRPG7tLR4f4rA0vIvvexFyY_eR_6TnsUr_maVu0Gm5nQ3VQlKoQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوة امنية تطوق منزل معاون مدير عام مصافي الجنوب في منطقة الجمعيات بمحافظة البصرة جنوبي العراق.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/80401" target="_blank">📅 17:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80400">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVtnQyCiY3WV4mXzLkiy3a99a5KF5wQ5WhlQI5nFqELkFaEEJG-I6joTZ0AIxt7TfHOlIfTw9hmC0MIsYNAWYYt66OxMPhEkDZYWYVl7WynCpv-gjRTUxu0SUH6hJy96bD2uwbsK85Uq8k1AnbzWGky7AA6U7lu61eRmOePj6hIVg4vb06HsOdWXnv5C2AjFSsBk_4NtWzAaEwOIFyBa70yVXyQZTS7b4PMRCvR_9dlCQPpV3kPP223P0Dpjb7JqMRaD4mGYCt7uUDjVhYzUqEZIWzvcmj7c1ZijXezxAO5u4CBJImCBoIDqyP9Lo92jzi8gBdcLMj3BAT9L81HNIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوة من بغداد تداهم مديرية بلدية محافظة الديوانية وتعتقل مسؤولين بارزين فيها</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/80400" target="_blank">📅 17:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80399">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">وزارة التعليم العالي العراقية توافق على منح خمس درجات لمعالجة حالات طلبة المراحل الدراسية المنتهية</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/80399" target="_blank">📅 17:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80398">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc24e9d2ba.mp4?token=ZRPIYzkHtfX22kKNrh7HDRxe5P4aD6XwWJrQ1QiY1t3lKbW3MZJiNljmjnFE0rWXYSaZzlidXaUcWtNSJHKeA3Sjb6PBWi780g8xx4_YwI1hvgcm6ne-Gs0xZwZPdJCyuO5vP4hREpiDof8pgQOFEdVdpq7fib4BUNzIRdT16pbtfrzsJvbmb6I1mN0Kbzd6tFtJdUBKZTLjDItX9M51uNQCnDUXgwVQmh3vEWq627bB1fg7mT9mppQ2Ltk8tt46Bd1K93pwiomqp6DLF5X7exWeB4-FgArVoLI_wB4mTuXlEhBgsCKeRi9Aiq1B9IGpRJ0PKv_QxeOUcOmg1GxQOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc24e9d2ba.mp4?token=ZRPIYzkHtfX22kKNrh7HDRxe5P4aD6XwWJrQ1QiY1t3lKbW3MZJiNljmjnFE0rWXYSaZzlidXaUcWtNSJHKeA3Sjb6PBWi780g8xx4_YwI1hvgcm6ne-Gs0xZwZPdJCyuO5vP4hREpiDof8pgQOFEdVdpq7fib4BUNzIRdT16pbtfrzsJvbmb6I1mN0Kbzd6tFtJdUBKZTLjDItX9M51uNQCnDUXgwVQmh3vEWq627bB1fg7mT9mppQ2Ltk8tt46Bd1K93pwiomqp6DLF5X7exWeB4-FgArVoLI_wB4mTuXlEhBgsCKeRi9Aiq1B9IGpRJ0PKv_QxeOUcOmg1GxQOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات الامنية في محافظة البصرة جنوبي العراق تلقي القبض على (مرتضى زوير) برفقة أربعة من أبنائه على خلفية تهم تتعلق بالتزوير وتم ضبط بحوزته على 30 ختم يُستخدم في عمليات التزوير إضافة إلى كميات من الاموال</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/80398" target="_blank">📅 17:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80397">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">جيش العدو الصهيوني: تم إرسال طائرتين مقاتلتين تابعتين لسلاح الجو قبل قليل باتجاه طائرة مدنية في البحر الأبيض المتوسط ​​بعد ورود بلاغ عن فقدان الاتصال بها.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/80397" target="_blank">📅 16:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80396">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اعلام العدو: عقب الحادث، لم يُسمح لطاقم الطائرة بالهبوط في إسرائيل، ومن المحتمل أن يعودوا أدراجهم ويهبطوا في بلغاريا.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/80396" target="_blank">📅 16:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80395">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اعلام العدو: طائرة كانت في طريقها إلى إسرائيل في الجو ضغط الطيار على زر الاختطاف ثم ألغاه، الطائرة غيرت مسارها من وارسو إلى قبرص وتم ارسال طائرات مقاتلة</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/80395" target="_blank">📅 16:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80394">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اعلام العدو: انباء عن اختطاف طائرة</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/80394" target="_blank">📅 16:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80393">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اعلام العدو:
انباء عن اختطاف طائرة</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/80393" target="_blank">📅 16:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80392">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73908e4ec3.mp4?token=fI4mED4dxX2sS1aLaqqjpR6Rwt8TJmk0eMAljZi01DCy7BAgLPNi5jz1KTZM-cUcVcW_wUp1xY2voiz3CVWunhQy0Kk-NfgpkdHklXSpKOLBRzTw736iQ8h8t9OR5NQMe5hd5nLHRmSxtxfk84XLuYRKVApm4S3kKQj0UaPHEKIrcgYIEm-jyiwx9Wczezo-dzMMI9-tC5uESBig5t9OtXhle60kAF_zuM4sXO602LdY4I2nJHzpW1aC6jwrUsXiiFOIe8O_hDKIOw_yzUpn5cuJbRWvh282wqwGFFbOGdmYLwRLJc-iu8n22HZvVMM7xmcp_s1ffycJSBx6BQzZXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73908e4ec3.mp4?token=fI4mED4dxX2sS1aLaqqjpR6Rwt8TJmk0eMAljZi01DCy7BAgLPNi5jz1KTZM-cUcVcW_wUp1xY2voiz3CVWunhQy0Kk-NfgpkdHklXSpKOLBRzTw736iQ8h8t9OR5NQMe5hd5nLHRmSxtxfk84XLuYRKVApm4S3kKQj0UaPHEKIrcgYIEm-jyiwx9Wczezo-dzMMI9-tC5uESBig5t9OtXhle60kAF_zuM4sXO602LdY4I2nJHzpW1aC6jwrUsXiiFOIe8O_hDKIOw_yzUpn5cuJbRWvh282wqwGFFbOGdmYLwRLJc-iu8n22HZvVMM7xmcp_s1ffycJSBx6BQzZXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مشاهد من عمليات هدم بيوت الشيعة وتهجيرهم التي قامت بها عصابات الجولاني في قرية المزرعة بريف حمص السورية.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/80392" target="_blank">📅 16:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80391">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇮🇶
وزارة الداخلية العراقية:
عرّاب تهريب المخدرات يقع في قبضة مفارز مديرية شؤون المخدرات، وبحوزته 32 كغم من مادة الكبتاغون قرب منفذ عرعر الحدودي ضمن محافظة الأنبار، كان يحاول تهريبها إلى إحدى دول الجوار.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/80391" target="_blank">📅 16:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80390">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">متداول  الافراج عن النائب السابق محمد الصيهود السوداني لأسباب صحية بعد ان تم اعتقاله بتهم فساد</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/80390" target="_blank">📅 16:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80389">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🌟
هيئة المنافذ الحدودية العراقية:
إلزام الشركة العامة لموانئ العراق بعدم السماح بمرور أي شخص غير مخول، ومحاسبة المتواجدين في البوابات في حال حدوث أي خرق أمني أو حالات سرقة.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/80389" target="_blank">📅 16:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80388">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🌟
وزارة التعليم العالي العراقية توجه بالإيقاف الفوري لتسلم جميع الطلبات المتعلقة باستحداث الجامعات والكليات الأهلية فضلا عن إيقاف طلبات فتح الأقسام العلمية الجديدة فيها اعتباراً من اليوم الثلاثاء.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/80388" target="_blank">📅 16:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80387">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🌟
مديرية المرور العامة العراقية:
منع سير المركبات الكبيرة على الطريق السريع (محمد القاسم) ابتداءً من مطلع وزارة المالية ولغاية منحدر قرطبة/ الباب الشرقي ذهابا وإيابا، وذلك بسبب الأضرار التي لحقت بالطريق نتيجة الحريق الذي اندلع صباح هذا اليوم في منطقة النهضة.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/80387" target="_blank">📅 15:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80386">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nm7f-p1jZUqZ-wgoashyqgn8IHkV_6UAltUDGGIvOfcOFpC38OZGmM8Cm0feGCrMlQPkaoMr4tmoBXqmtHV2ymwcNNe-522EiSLzDwXE9eUAGz5yjbUWMXRU9xgHnqhDq7zw7LX3qeYarkqltkWNWeJZu9LNHjjRgWZ-ChtgKT_uPndywWKJCl4CqlNk3wv4bGHPNL6ynwMT0M5EHNxw37CBnQtqq3tfqEgjK2NBiXW42LfjSh7rMHzz8yxip5Nrg_vWkv7HmYr3O5cHQVY6y-QRVbnGNYZW4MujlleEF2dCGlrlFgAIUI7Ob3WctdHtIlKYYHHcARGNCJaBoJHBwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متداول
الافراج عن النائب السابق محمد الصيهود السوداني لأسباب صحية بعد ان تم اعتقاله بتهم فساد</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/80386" target="_blank">📅 15:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80385">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🌟
قوة أمنية عراقية تلقي القبض على زوج أحد أعضاء مجلس محافظة الديوانية بتهمة التلاعب والتزوير بوثائق.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/80385" target="_blank">📅 15:33 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

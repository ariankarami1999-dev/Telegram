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
<img src="https://cdn4.telesco.pe/file/N_2p63R1q3m-48b1e8m6_qd8DexEp9sLSvmHbwYn9WC-8Ifg3MHm4dZZjVdAMjhT7Yd68iK6p-ictP8BTrzt9cqQ70D4CsHWbPSY0WWmL1b3qol-4S0SDdxQPvoXEa7FgVNI7XQB550MWNozg9Z4vqEIE-P_oSDMD0GZsrhmxLnoZ18ZQuzuFeoBaPsqQd08a40Er-NoRASyqY2OiVDGK5buVB5Cjt6UuH-eRg14fdQtWcMNwpB3Yp1yFbAPI8VusO0cj_AA8lg-bOE0uCfeAT6UAWoUGhnObmohjxUK73KLm5F6DNcdUXvaTv75m0ucxoPpA0Zmm9OAaw6kYRZgNg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 267K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 09:03:26</div>
<hr>

<div class="tg-post" id="msg-91036">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aee2088fd1.mp4?token=SwHe6PC_p5FweqQq-CdEgyZWkWsRD-rbD-jPvC8PE3pJXEmxDhtilxyAxNnNKw9QEWGYr1p_DUXU7K_RAQGJH_djNb-l33OdxBGZBK3LRNmuVIz6IH6ucQCgq-6GLIb6CZBTh4sie9-ItHUR0hcKROA0h2ySA5_J7XmDPciIa055oM0DwfjCTKO4UfFgRC-TJKPOt_ILNDSq5Qcj4eCjALtUgqgzF-mZ7iZCtYbBTfB2QKjIR2dtab7Drhh70A8RO7zPN7Uf2ee13hn6gpRysqc3oBheadl1n9PkvaMVsO2wFXYJHSOm9HJcmysf2fb1Ev7mfoj4Hl1Xe-SCoHGr4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aee2088fd1.mp4?token=SwHe6PC_p5FweqQq-CdEgyZWkWsRD-rbD-jPvC8PE3pJXEmxDhtilxyAxNnNKw9QEWGYr1p_DUXU7K_RAQGJH_djNb-l33OdxBGZBK3LRNmuVIz6IH6ucQCgq-6GLIb6CZBTh4sie9-ItHUR0hcKROA0h2ySA5_J7XmDPciIa055oM0DwfjCTKO4UfFgRC-TJKPOt_ILNDSq5Qcj4eCjALtUgqgzF-mZ7iZCtYbBTfB2QKjIR2dtab7Drhh70A8RO7zPN7Uf2ee13hn6gpRysqc3oBheadl1n9PkvaMVsO2wFXYJHSOm9HJcmysf2fb1Ev7mfoj4Hl1Xe-SCoHGr4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
انباء متداولة عن تفعيل الدفاعات الجوية في قاعدة خراب جير بالحسكة السورية.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/91036" target="_blank">📅 03:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91035">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔻
مصدر امني لنايا   التنبيهات للسفارات الأمريكية والأجنبية يأتي بسبب مخاوف من نية تنسيق هجوم مشترك بين أنصار الله وجبهات المقاومة الأخرى بالهجوم البري على السعودية .</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/91035" target="_blank">📅 01:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91034">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">انتخابات كنيست في " اسرائيل " فلسطين المحتلة
خطاب لترامب في الجمعية العامة للأمم المتحدة
هل سوف نشهد جولة جديدة مع ايران ؟!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/91034" target="_blank">📅 01:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91032">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gc4py_TtCB0f9rxafpGYpuCMdLZOrxoTMAix7a55sSep_xJQLM8BrQiesasTmNUBNtD8tSyrekpfV-XT76AVrSMnJJZxEfUiuCq7Z_ejKkZ0NdWgLDAjl1KXnIPzHNh5kb8CyTpqwLi4wDzA2leQ6dHpV3m0D9saPPZS9R9cT-gMrn7n17vZcVefeBAsNPlbBYzuxV7DGTAkrRqEAANuJB9k-AGMuAYDEgFObjJxpNzT7DjCF-AgLvkXwfqH1aOTY-0OveaaHl61f7n4m6RIngovbAJwhLnOtwvb2t4GNzIwmCll7raADyImAlqnFpz957dddNf7wkcxLnnQK7rb6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
USA situation in Middle East now</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/91032" target="_blank">📅 01:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91031">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇺🇸
التحذيرات وصلت لكل السفارات الأمريكية في الشرق الأوسط كما وصلت تحذيرات لكل السفارات الأجنبية في السعودية مماثلة عن تطور الأحداث في العمق السعودي</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/91031" target="_blank">📅 01:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91030">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">السفارة الأمريكية في بغداد تحذر رعاياها من إمكانية إلغاء الرحلات الجوية وتوخي الحذر والحيطة</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/91030" target="_blank">📅 01:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91029">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2sibiSly52U9YTZV3ZY4BScglZFQ6R09YTq-bfD9vH4ShxEWFj_bhZSXEYlSfkat9BjHWucgvi3r6A-M3USs4nR2kDqzBKMEm1zhppbXeYcN506AD132gOzHtKfZ7M8PQpDMF9JpiqExUjqOi4RZ2_nVew1xEH-QMlHu7yF00WvHFchzT9GX5kRotkpGIh0V15ho8nnYjZDlmqLmj1iB5D9nULV7vkJQWaei1uV4q-bMAOCebpzmtU-GSpY62UNJoJnfrvqndGPKOWx-1ls90AexfgKJsdb_0PCrk1Aivw0uVLmGHVcOfz5P_kLoZQBe84QZG44B976aRpMC6vWWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدر امني لنايا
🔻
المجلس الجهادي لكتائب سيد الشهداء ناقش اليوم إمكانية الالتحام البري و المواجهة مع النظام السعودي في حال تطورت وتسارعت الأحداث بالمنطقة .</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/91029" target="_blank">📅 01:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91028">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔻
مصدر امني لنايا
التنبيهات للسفارات الأمريكية والأجنبية يأتي بسبب مخاوف من نية تنسيق هجوم مشترك بين أنصار الله وجبهات المقاومة الأخرى بالهجوم البري على السعودية .</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/91028" target="_blank">📅 01:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91027">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U26WA20ZRfdsEicuijj6bBssJC4qvdYuf65CSaxZGDX708KAS0aDag_pS3t3Vj8L77bzvm8T--XjHVs9nXkZWDiw3x1ljggtPceuJcyidO1MHRNff3hW160Ca6l6hL6wfr2OTwGpyYHZjHmKiwVwmFs7aq7I4Oc1jjbOQcAZzrVFSkLBXDAlA55V-aKy5eEOBmSkmc6Rbmw56lvI-8_cruIArv9exPdh0e5hMIlLBBjtxdDVm2ksLBLe5XFN6bFjsVuU60OubyrMVtu2lkudaOGR3x_HzgnG1k5loXAViuC3-ExzcqEUg-osccoMRg9C1brl9LXViUcPkWjN8e4IJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">السفارة الأمريكية في بغداد تحذر رعاياها من إمكانية إلغاء الرحلات الجوية وتوخي الحذر والحيطة</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/91027" target="_blank">📅 01:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91026">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huTDRkbG_JyunyqMNHXDKCHD3ycfNgUuGiRgy_O83KIZLuWpzYo4BOLizcjEuTvpU_SkmjhtlccIjmpb-1TtF1UJxdcXBabrjCQ4p4ie9LfQ_N9DQIv2n68xRxnl6MRKaAgYv7xQoEulh-_QnTrpNGcuRYHADhk7wbA8z0IsoqlsmCL1uB-VdEEr080kPgqfy-zjSaHOJOcuF1Hl3FwGdUw_0Qh0d3DMxiA-osLoTVXBXlErfJQv93rtC8xx18zI19REjQR_h1AumOXIRNXzjmvjjjCTUyMkcgx5NptCY-2w29wW-agVx5afUzeVx5wUEc-WKtnVtcdAQGAI33Gsgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توقف الحركة الجوية في مطار الطائف السعودي</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/91026" target="_blank">📅 01:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91025">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">انفجارات عنيفة تهز سماء مدينة الطائف السعودية</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/91025" target="_blank">📅 01:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91024">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">السفارة الأمريكية في بيروت تدعو رعايا لتوخي الحذر !</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/91024" target="_blank">📅 01:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91023">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">انفجارات عنيفة تهز سماء مدينة الطائف السعودية</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/91023" target="_blank">📅 01:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91022">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">انفجارات عنيفة تهز سماء مدينة الطائف السعودية</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/91022" target="_blank">📅 01:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91021">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/91021" target="_blank">📅 01:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91020">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUcKTUpnxBHkbzJLvXicaAg1yCHY6ywzQweZTCPzu0D71d3_7RTaSEgl2rw90lLkd6ij0PQiIA9yStPFYPh2K8ujwhFhOMBn62g6N7vs-gNT0qdD4w2NgHgnhmuCRBXk3INgjEJqjjNVswIu2_PsO64lATqN_y0f_hhhQ49isKdl2AGBnmSY5D616RaGgBQ4KQ4LRWR7UejNQCIziN0ELGfh5ymu9dc9Ha12qM2PLy2QhQRvcMdEfsuZlrRplpyX1PxVQagfLtqbcQaqBAX3CVWVizEjJbvj-_AKhUTBsR2mLnUHusDbCazzAmdxXawTD1btwn5Ajt1ZEarfhuDjrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إيطاليا تحذر رعاياها في السعودية بعدم التقرب على المنشاءات العسكرية السعودية
لا تسافروا إلى جازان خميس مشيط ونجران</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/91020" target="_blank">📅 01:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91019">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‏أصدرت السفارة الأمريكية في مسقط تنبيهاً أمنياً عاجلاً للأمريكيين المقيمين في سلطنة عُمان، تحثهم فيه على توخي مزيد من الحذر في ظل التوترات المستمرة في الشرق الأوسط. وتنصح السفارة الأمريكيين بالبقاء متيقظين والاستعداد لاحتمال إلغاء الرحلات الجوية، وإغلاق المجال…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/91019" target="_blank">📅 00:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91018">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‏أصدرت السفارة الأمريكية في مسقط تنبيهاً أمنياً عاجلاً للأمريكيين المقيمين في سلطنة عُمان، تحثهم فيه على توخي مزيد من الحذر في ظل التوترات المستمرة في الشرق الأوسط. وتنصح السفارة الأمريكيين بالبقاء متيقظين والاستعداد لاحتمال إلغاء الرحلات الجوية، وإغلاق المجال الجوي، واضطرابات السفر.
‏يأتي هذا التحذير بعد ساعات من إصدار السفارة الأمريكية في إسرائيل تحذيراً أمنياً مماثلاً للأمريكيين الموجودين في البلاد.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/91018" target="_blank">📅 00:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91017">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇷
🔻
🇮🇱
محسن رضائي عن علي الطاهر: تم إخلاؤه مسبقًا ولم يكون أحدا فيه كما تم إخلاؤه من المعدات أصلا</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/91017" target="_blank">📅 00:44 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91016">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇸🇦
🇾🇪
‏
التحالف السعودي يعترف بتعرض الرياض بصواريخ
القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/91016" target="_blank">📅 23:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91015">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6CtzWdZ_WXUIciXTqcUZdFiUTGnzLdx-opJ22rtSbYyTzmHsn7S8CY-NXmr4QqzUL9SJf5wr2_sOZ1ncRNmBUZaZ_l4npLDEhfKQPnJAm_tviGVrzei8f_1tjraxiCei48OIUZ_lIdWnCJUCipzvAYR9zAQZ8vhfjCQ47GYa7eHN0t--3qXt9MaQVzyMuvsGjTNAuJgJboZoC7TVLBFUeHrJKrnPJQ4HM3piXhF1kKGBucJRzuqzj5a0vjGdN5HpprpV_BwA72viEncL5hbNCt8oYGqsFyAlTQiuatVqi3LmfyrHrLsQ5L1DgItiOnP1wCF5PITPMaiDZC0odayZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفذت القوات المسلحة اليمنية عمليتين عسكريتين نوعيتين بعدد كبير من الصواريخ الباليستية والمجنحة والطائرات المسيرة
- الأولى استهدفت أهدافاً حساسة في عاصمة العدو السعودي الرياض
- الثانية استهدفت شركة أرامكو في ينبع</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/91015" target="_blank">📅 22:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91014">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇹🇷
‏
وزير الخارجية التركي:
تم تقديم مقترحات إلى جميع الأطراف لإنهاء القتال السعودي الحوثي ...</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/91014" target="_blank">📅 21:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91013">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3e6c9d1b7.mp4?token=RdluNoVV8FIKL6c_jItcKi4XrLYOeN9BZoBDU3hj-Ck-IOoZyXgv_GYcVXuwdjJEYuCrxL4JoW20cooFuR6woFc29StUltNEJiLO9MEYr3nA7Sh8DEMJJSr38QWNPx5SKJUJzXR9JSTImqOBzWVOsqJWHBEqJq_sn1qwISp0Z00utN43ZXK82ZR-kqALJE6No6u5q60QjK1gcqtcXpQqYEonuJ3o0ITObiqN38CedhAtba8ca7GZvfDH_zfM4n4VKPctm-6BTT-senvE466l8xBD9qflyAoiL9BGyWiQOZHeb4Z2tRgnKRGoLXK9JZr8ju9Skbywuw0c1IXTDXARsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3e6c9d1b7.mp4?token=RdluNoVV8FIKL6c_jItcKi4XrLYOeN9BZoBDU3hj-Ck-IOoZyXgv_GYcVXuwdjJEYuCrxL4JoW20cooFuR6woFc29StUltNEJiLO9MEYr3nA7Sh8DEMJJSr38QWNPx5SKJUJzXR9JSTImqOBzWVOsqJWHBEqJq_sn1qwISp0Z00utN43ZXK82ZR-kqALJE6No6u5q60QjK1gcqtcXpQqYEonuJ3o0ITObiqN38CedhAtba8ca7GZvfDH_zfM4n4VKPctm-6BTT-senvE466l8xBD9qflyAoiL9BGyWiQOZHeb4Z2tRgnKRGoLXK9JZr8ju9Skbywuw0c1IXTDXARsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
بيان القوات المسلحة اليمنية بشأن استهداف أهدافاً حساسة في عاصمة العدو السعودي الرياض واستهداف شركة أرامكو في ينبع بعدد كبير من الصواريخ الباليستية والمجنحة والطائرات المسيرة - 19 سبتمبر 2026م بيان صادرٌ عن القواتِ المسلحة اليمنيةِ  بسمِ اللهِ الرحمنِ الرحيمِ…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/91013" target="_blank">📅 21:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91012">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇾🇪
سماع دوي انفجار في محافظة عمران اليمنية.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/91012" target="_blank">📅 21:36 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91011">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇷
المتحدث الرسمي باسم القوات المسلحة الايرانية:
إن إسقاطات قائد القيادة المركزية الأمريكية وادعاءاته الكاذبة والسخيفة بشأن مرافقة ناقلات النفط وسحب مليار برميل من النفط في الشهرين الماضيين ليست مجرد حقيقة، بل هي عملية نفسية فاشلة لرفع معنويات القوات المنهكة والمتعبة للجيش الإرهابي الأمريكي في المنطقة، ولتبرير التكاليف المالية والبشرية الباهظة للولايات المتحدة في المنطقة، ولن تغير هذه العملية حقيقة انسحاب جيش ذلك البلد المعتدي من المنطقة.
لا تزال زمام المبادرة في مضيق هرمز في أيدي القوات المسلحة الإيرانية القوية.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/91011" target="_blank">📅 20:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91010">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtttE6eWC7uFBaIOFWxTmimIc2R7N6iCrbqYKhI7NS9TqkhEJytncdNc93HULoXakYgfVSOJ3r1BBrJHfD06DuUhZnEL4_izny2HsnKyvi3uwgdVloCt762aDdM7yXxiQJBDDTGTnHX4ZmSfI_8MtOZeDzsG1E4TrGwR7UrC5olcxiSjZWkdxFkhXzlZWfo8DvyXnuhmkm8A5F1q3usAbBeoew4ii5Y7lLyWkRPQ07vdqpvAnXmL8Gb5qLXOgPejM0NNdqXSTSiOt97etmF3zNuDXVftIEsckUnEGZ5c-z8qR1SRRlW_MVBYQ-awTsAuu5a66ua8k9f7R8cj1afXPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
: أنا بصدد تشكيل "قوة الذكاء الاصطناعي"، على غرار "قوة الفضاء" التي حققت نجاحاً هائلاً خلال ولايتي الأولى.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/91010" target="_blank">📅 20:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91009">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/91009" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قولو له الرياض اقرب</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/91009" target="_blank">📅 20:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91008">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇾🇪
‏بيان مهم للقوات المسلحة اليمنية للإعلان عن عمليات عسكرية واسعة في العمق السعودي،  في تمام الساعة الثامنة مساءً.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/91008" target="_blank">📅 20:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91007">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇷
الخارجية الايرانية:
من الظلم للشعوب أن تقوم بعض الشخصيات الإعلامية بتحميل إيران مسؤولية انهيار التفاهم.
نحن نتحدث عن الولايات المتحدة؛ وهي دولة دأبت مراراً وتكراراً على التنصل من التزاماتها على مر السنين.
إن لوم الذات يُعد إحدى سمات الحرب الإدراكية التي يشنها العدو؛ فهناك حقائق واضحة لدرجة أنها لا تحتاج إلى تفسير.
ستركز زيارة وزير الداخلية الباكستاني على العلاقات الثنائية بين إيران وباكستان؛ ولا توجد خطط لتبادل رسائل محددة تتعلق بالوساطة.إيران وعُمان توصّلتا إلى تفاهم بشأن تحديد مسار آمن لحركة الملاحة في مضيق هرمز.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/91007" target="_blank">📅 20:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91006">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇶
ضبط 200 كيلوجرام من لحم الخنزير خلال مداهمة مطعم في محافظة ذي قار جنوبي العراق.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/91006" target="_blank">📅 20:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91005">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇱
صافرات الانذار في المستوطنات قرب الضفة الغربية بفلسطين المحتلة خشية تسلل مقاوميين.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/91005" target="_blank">📅 19:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91004">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gujV-lfnpcYSXebrGrlM4GaXQa_We-It7W8WBrKyQBZp2FAEr6Rnjw-Hr5zH_oCrtxqBUapdg92Qje-nyfFdM_mCpvTYzxheLVVkXZSRYra5b5JtXVWVuHhfeBX5HNuq25s522kiKITR0nSvFwCHvYPl9q7quf6J27cLpz7roXaqPGO-_PF-Qq7xsba1pxGwqX_Ig37CFi1RFSuDj5bQjrNWl29kcqI_-H8M_IiBgL5Ab6gGTImUm6Vf9WNA-Thib4Qc5cyMABZiPxfLSaSZ_ohaNfDCX73sSPgmR1a_fbH7Ukoj0zywnU9Iw0vsQB3wBD6JGyVvsritNgl8RSrODQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
🇾🇪
عرض عسكري سعودي في سماء جدة.
جدة تستعرض والرياض وجيزان وابها وخميس مشيط تقصف
😆</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/91004" target="_blank">📅 19:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91003">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇾🇪
‏بيان مهم للقوات المسلحة اليمنية للإعلان عن عمليات عسكرية واسعة في العمق السعودي،  في تمام الساعة الثامنة مساءً.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/91003" target="_blank">📅 19:08 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91002">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYBW_Tf5RKpvCEgM2ZZxLoXmqDgNX9u59tGG2QJksqWB22MtS4UOzMrwKe1bOH7lNRbO0ED5gV3KiGrfwBjFzMMSo0o3zI0ohDrFz3nhHrJe95ZUIucbB6KxJ_nLmGXyMQ040Wq3YqV8vgfqVVHYZCdp0t293bpfniCtZ0m8ih1KjvLaF2QC7jVcbc0MyQHttPfVIdFTm5yWXau8qqKxGnNkzFp16tur0PFB0tsk_3YtSJNAuFBQsN6H-s57uQoSTXBwpYM6PR9ael3OSGfzsPk6cNoBZekwBUp8M-OwrovR77MXEKV9aMOzCoEsbkkYz-BvXK5p91zGLadYswX4Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
يبحث ترامب عن اسم جديد للذكاء الاصطناعي.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/91002" target="_blank">📅 19:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91001">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇮🇷
رضائي:
من صالح واشنطن القبول بشروطنا للخروج من الحرب وتهديدات ترمب لن تحقق أي نتيجة ومستعدون لحرب حاسمة، يجب إنهاء الحرب على جميع الجبهات، وفك تجميد الأموال الإيرانية، ورفع الحصار البحري.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/91001" target="_blank">📅 18:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91000">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48bd90ce61.mp4?token=azdVWF4byNvR18GbD4UBqhajkm_HyLY0Xmv-h-j0PhP_z90D8xbVQHmhGz_PWEAsFyBxdnr6SsmWloFzcjEkAkhZymkiluQxknDHdcZ3t-7W1819DEvmDZExicSR_VlVP0PhoLxHQpF0KliYOyI2uVmSkSoNAitdrJRe61qeQvEtKm1ZBBSAehdmmcdcgQhpZ9hBy0qiaF4MKg-01YuuhFG4S9iD4wkteHNZiMziOV44jIybQyfWowiz7CoN7O4cIuZVvNE0iDc_aPbUE8kUQnzUlr8zRuvSj0U19f6_R7Sdl1h1vNeZsF3g-0JTSm-BK5pOMwp_EfgYdHXVy8y4NG55AZtL7CpmnUZH-k6Cv1qzjiNUtUJrz691K0oAhj6oYHVZGuLzALFGtN0k8prGq6JNaOXBnFo6c-igZRz6qfmxIsoL0V_HOo--0Slpm8dr3iIa5mlpSNrTDtIY_h5RSlFo6TW3xPksV-6NIx6njeM_ZWBX3ziZdQLVi_yxXikvGHe_k0g33QzIxFMrxAEleNBWHP76WxOnoMJtZIe7_jy6iztPjWcXrzCCkw6v3jnZtLWR2wWiKtusdfhA-K6-ogGPilzYW2av_czKMdj2hGLPLGqrGpR89vmaaMNXVS8Plpts7HGHdTxJuRZWgFDGjRx3ojo9jwm4vCEQQo3CfzI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48bd90ce61.mp4?token=azdVWF4byNvR18GbD4UBqhajkm_HyLY0Xmv-h-j0PhP_z90D8xbVQHmhGz_PWEAsFyBxdnr6SsmWloFzcjEkAkhZymkiluQxknDHdcZ3t-7W1819DEvmDZExicSR_VlVP0PhoLxHQpF0KliYOyI2uVmSkSoNAitdrJRe61qeQvEtKm1ZBBSAehdmmcdcgQhpZ9hBy0qiaF4MKg-01YuuhFG4S9iD4wkteHNZiMziOV44jIybQyfWowiz7CoN7O4cIuZVvNE0iDc_aPbUE8kUQnzUlr8zRuvSj0U19f6_R7Sdl1h1vNeZsF3g-0JTSm-BK5pOMwp_EfgYdHXVy8y4NG55AZtL7CpmnUZH-k6Cv1qzjiNUtUJrz691K0oAhj6oYHVZGuLzALFGtN0k8prGq6JNaOXBnFo6c-igZRz6qfmxIsoL0V_HOo--0Slpm8dr3iIa5mlpSNrTDtIY_h5RSlFo6TW3xPksV-6NIx6njeM_ZWBX3ziZdQLVi_yxXikvGHe_k0g33QzIxFMrxAEleNBWHP76WxOnoMJtZIe7_jy6iztPjWcXrzCCkw6v3jnZtLWR2wWiKtusdfhA-K6-ogGPilzYW2av_czKMdj2hGLPLGqrGpR89vmaaMNXVS8Plpts7HGHdTxJuRZWgFDGjRx3ojo9jwm4vCEQQo3CfzI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أصوات طائرات حربية كثيفة تسمع في سماء مدينة الطائف السعودية</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/91000" target="_blank">📅 18:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90999">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇨🇳
السفارة الصينية في الرياض:
نحث المواطنين الصينيين والمنظمات الممولة من الصين في السعودية على تعزيز إجراءات السلامة والبحث عن مأوى فور تلقيهم تنبيهات أمنية من السلطات المحلية.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/90999" target="_blank">📅 17:40 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90998">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEcIz3dCC0H0OZEDBI_yPiRM9mwKn6Jn0eQ7lVvq88xyZI2BCgmdZM5V06GJQsT1gA1YEbvwQdG01iXQ_Op4pW5AzFVOsrZ0iloQLLvBnv1poIlIXiAG-TAvoREmrfQmFcJOMddqwSb-u2rv1pQXEUHYQfRmqyl_E8xmfyu9ZRfmfnb2inkXSMZEgf3FYNLl4elM_Q2p1TGxkJjTF0h3NJSPpKd5w6iTLtcpWXSxvToWe6xHhiC6AZBfbgTENvVXMBZQZ-1bJuroexISkIelJ6QqDaQd2S8HWq0XGyOAzKTkkVuteHv72oPazz_yDsqEfyMCi2C_Mf9gZApW5q2cPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الرياض لحظة هجوم القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/90998" target="_blank">📅 17:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90997">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇶
البنك المركزي العراقي:
الارتفاع في سعر الصرف في الأسواق المحلية يعود إلى المضاربات في الأسواق والتوقعات وسوء استخدام الظروف الجيوسياسية في المنطقة لإرباك الأوضاع الاقتصادية والمالية من قبل بعض المستفيدين من هذه الحالة.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/90997" target="_blank">📅 16:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90996">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/922e790775.mp4?token=iXPT0PIw7DOkM-yX3BG9T8ew9PBTnYlpsu3qdQnOKefQc2dlOtx-fNQWipfcXfIw9wyVIHCgczE7cSJKxOBPnU-LtlqqK5p4cwXTWolcrBFfkqZKP1_PfoHChhXp-PZqeSFOBX98UiLNzltkq9clOHwB_8KAKO2yFCbcGhFU1wgqn5IapIcId6Q0JZbIDgTnnVreGVMMikSnG4W5MlPLXcgWCTpYFqnDFMxCbz3-p2M2tvAGg6vflxwFembT-SyxHOiNzDPa2t2wNeOfHluLM8wL-v4-LGRIvqrdj8C2oXFfiG8MWDQJeDegOYL2D9NLJGQCWkERQSNxr8TGp8vVmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/922e790775.mp4?token=iXPT0PIw7DOkM-yX3BG9T8ew9PBTnYlpsu3qdQnOKefQc2dlOtx-fNQWipfcXfIw9wyVIHCgczE7cSJKxOBPnU-LtlqqK5p4cwXTWolcrBFfkqZKP1_PfoHChhXp-PZqeSFOBX98UiLNzltkq9clOHwB_8KAKO2yFCbcGhFU1wgqn5IapIcId6Q0JZbIDgTnnVreGVMMikSnG4W5MlPLXcgWCTpYFqnDFMxCbz3-p2M2tvAGg6vflxwFembT-SyxHOiNzDPa2t2wNeOfHluLM8wL-v4-LGRIvqrdj8C2oXFfiG8MWDQJeDegOYL2D9NLJGQCWkERQSNxr8TGp8vVmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظة هجوم القوات المسلحة اليمنية على العاصمة السعودية الرياض</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/90996" target="_blank">📅 16:36 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90994">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3773ef6e7c.mp4?token=PWTwqLMHmlFq1W_5IQu7Njps0c3L4iH48IFG6XC9XElW9corgN0-OkuUF3cC7oRHIy4JsK51CumpvgphvK4JDYXFCvPGq9Dm-xOH8IUc7543OT2pPP_fMMFu3cxIzdbkMCHMDW01rhe7Jzcj0adEotnRkm-gGrFdCr5YzH1sCu85VtXkNUQEf32Y47GeQq-vUINptj3aF9A4m8fSYKxqMbH9EvYzeWRh_OL-JTjDjOnbQqaYM9l9jqgyJ8toEg_qbPsn96tUWD9ClnvQBbg4LdhC7v3d0MyvGz_7cG6FlcLG3gVhENC0aCRpCjCFRhmUALGqhDZUEdyegb2-95Ighg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3773ef6e7c.mp4?token=PWTwqLMHmlFq1W_5IQu7Njps0c3L4iH48IFG6XC9XElW9corgN0-OkuUF3cC7oRHIy4JsK51CumpvgphvK4JDYXFCvPGq9Dm-xOH8IUc7543OT2pPP_fMMFu3cxIzdbkMCHMDW01rhe7Jzcj0adEotnRkm-gGrFdCr5YzH1sCu85VtXkNUQEf32Y47GeQq-vUINptj3aF9A4m8fSYKxqMbH9EvYzeWRh_OL-JTjDjOnbQqaYM9l9jqgyJ8toEg_qbPsn96tUWD9ClnvQBbg4LdhC7v3d0MyvGz_7cG6FlcLG3gVhENC0aCRpCjCFRhmUALGqhDZUEdyegb2-95Ighg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد اضافية لتصاعدة اعمدة الدخان من مطار الرياض الدولي بعد الهجوم اليمني</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/90994" target="_blank">📅 16:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90993">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/234fc6665a.mp4?token=MG-XI84sKV2H0IlICoe7yHq-hsqm-1-9gZG-tCudhOicZIe2fg4MLuViXhsjLYcR4NCqGdj_W0aF2ftvVjHSBgU0Ar9ebvlTsHBMEmXvqC89TZ01O5glJgMGlqhx5aoJuhZ7wXlSF5R04Fi4CUMmTUZSqmEfFGNMlEopoGQn1PYZxHRxVZyQKce_2z2-sdTZhBYzHDfZQzXWjsZ5gTk3gM2DU2dNd1CFsd4K6TPu4jQPoi6tQVoT3OCDOcCcPaVTTLB2GADKSIWzFY18V_INPXoiSO4H04x9bvrF6HovjAANFpDK5LH-wK-vE--VaLkM6F0FPXurgdw5NJOnY405ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/234fc6665a.mp4?token=MG-XI84sKV2H0IlICoe7yHq-hsqm-1-9gZG-tCudhOicZIe2fg4MLuViXhsjLYcR4NCqGdj_W0aF2ftvVjHSBgU0Ar9ebvlTsHBMEmXvqC89TZ01O5glJgMGlqhx5aoJuhZ7wXlSF5R04Fi4CUMmTUZSqmEfFGNMlEopoGQn1PYZxHRxVZyQKce_2z2-sdTZhBYzHDfZQzXWjsZ5gTk3gM2DU2dNd1CFsd4K6TPu4jQPoi6tQVoT3OCDOcCcPaVTTLB2GADKSIWzFY18V_INPXoiSO4H04x9bvrF6HovjAANFpDK5LH-wK-vE--VaLkM6F0FPXurgdw5NJOnY405ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الاعلام الفرنسي عن مصادر: اشتعال خزان وقود تابع لأرامكو قرب مطار الرياض.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/90993" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90992">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">وزارة الخارجية اليمنية:
- الأعمال الإجرامية الداعشية التي اتجه النظام السعودي إلى ممارستها في اليمن، توجب على المجتمع الدولي تحمل مسؤوليته حيال ذلك
- هذه الأعمال تُعيد للذاكرة ما قام به النظام السعودي في الفترة الماضية في كثير من دول المنطقة وفي مقدمتها اليمن والعراق وسوريا
- اليمن يمتلك الحق المشروع للرد على أي نشاط سعودي داعشي يستهدف أمنه واستقراره، وسيتخذ التدابير اللازمة
- حالة الضجيج التي تظهر بعد أي رد يمني مشروع من قبل بعض الأنظمة تشكل غطاء وشرعنة للأنشطة السعودية الداعشية</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/90992" target="_blank">📅 16:12 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90991">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">مشاهد قريبة من موقع الهدف المستهدف توضح حجم الاستهداف والدخان الناجم عنه  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/90991" target="_blank">📅 16:10 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90990">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‏
زيلينسكي:
وافقت على تنفيذ عمليات بعيدة المدى ردا على الضربات الروسية</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/90990" target="_blank">📅 16:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90989">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bA-lBIF8w7qba9P9mx9u44q8KdFOjNYY7y7ATRdivCnWPY2Rbc-UiV2GlQbHO21NAAkjsH70Lom-moWduJVO07dbKtUtnmYIzuEPPw-vb-dc1L_878Ycp2J0j24XKEJ9lypIxX9L1rtRzAHuW5ZFUZ4DBV53xiFWjCdyCNE5rtFuD8X_xWIPpxzwWHlHDfvIAdj5BA5_His5gBQJKzjGGiq6ga2DMqxAlYPD3QgNSxOfSh3tueXy8nDp89MHuTFLTUoRhpUEeBffsCxAQkFtN_Ap_KJjyalVz1shxP8vi11KmtfkFgFTB-G3g8bO0HyHHGN84MwNOEuRT9UEzrW_wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انصار الله يدكون عاصمة ال سعود
النظام السعودي:</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/90989" target="_blank">📅 15:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90988">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/702bac9acb.mp4?token=jSeVKY46kTxcl-yzy-qQfZxQlAyudAf8fHxrLlEXyXkU2yeAFAKGiFCHLPye62lUF_WxiV_9LgK1pWXIQQRC8GABCDKDaycw-pcemfmL_s4GoGkF311-B8ge5xlvUnC3in2lguqJn8Jz8uuJqvI4Nb_ctMV7hr0gArrZHkM44688JrWSfgNIV7cWKct6RAtk7OQl6ek6i-lCndMYl7tx5cVLv0eTQxJ5-_x_F5FjtHRC4GLsPkaY8XvvCK_BPHwBwcA4n35Kvh-8OISU6IeJbQJpu1rBjg87kaqn3sFGVX7K5KiwFr6csKedGFOSayqzEm4R1O84UwwAy_YxlG8RnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/702bac9acb.mp4?token=jSeVKY46kTxcl-yzy-qQfZxQlAyudAf8fHxrLlEXyXkU2yeAFAKGiFCHLPye62lUF_WxiV_9LgK1pWXIQQRC8GABCDKDaycw-pcemfmL_s4GoGkF311-B8ge5xlvUnC3in2lguqJn8Jz8uuJqvI4Nb_ctMV7hr0gArrZHkM44688JrWSfgNIV7cWKct6RAtk7OQl6ek6i-lCndMYl7tx5cVLv0eTQxJ5-_x_F5FjtHRC4GLsPkaY8XvvCK_BPHwBwcA4n35Kvh-8OISU6IeJbQJpu1rBjg87kaqn3sFGVX7K5KiwFr6csKedGFOSayqzEm4R1O84UwwAy_YxlG8RnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدخان يملئ الرياض منذ ساعات والدفاع المدني للنظام السعودي يعجز بمكافحته  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/90988" target="_blank">📅 15:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90987">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5e8fb5d2c.mp4?token=rVyX_xPu7dnw3fKC2kOb-ottmY2KWni02peOWAxmI5vCkPYWKj3q33jeBG0YNqhosrxNcl8yXQXf_1nK87CDu4dxcfZE0GRtHarCNZsuTlu6xSvNJNno4P6JsM_GMe5BxXVK-N3h4S8C3rI1ho3qT4rTTxjivfpaDkikHGbCoEhItSM1o-fb61QngrvVP874wVvM3X_LW-TRQ2nDbZ83ezNIGyh4kRCfy2G10U2uvUmF3dw5P9-CmtuqtfeNSqWfYt5lTYrbyLvw2IZHjjYu4NbFpp9WkvEjk3XLYlHGZY7a3Ph8rjOMPliPJ08lyxVorJiSZxzu1dyAQRiN7-e_dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5e8fb5d2c.mp4?token=rVyX_xPu7dnw3fKC2kOb-ottmY2KWni02peOWAxmI5vCkPYWKj3q33jeBG0YNqhosrxNcl8yXQXf_1nK87CDu4dxcfZE0GRtHarCNZsuTlu6xSvNJNno4P6JsM_GMe5BxXVK-N3h4S8C3rI1ho3qT4rTTxjivfpaDkikHGbCoEhItSM1o-fb61QngrvVP874wVvM3X_LW-TRQ2nDbZ83ezNIGyh4kRCfy2G10U2uvUmF3dw5P9-CmtuqtfeNSqWfYt5lTYrbyLvw2IZHjjYu4NbFpp9WkvEjk3XLYlHGZY7a3Ph8rjOMPliPJ08lyxVorJiSZxzu1dyAQRiN7-e_dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هندي حزين على قصف النظام السعودي وسط دعوات لارساله لتربية الماعز ليعود لصوابه.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/90987" target="_blank">📅 15:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90986">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/90986" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇾🇪
نقسم برب العرش
#شاركها</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/90986" target="_blank">📅 15:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90985">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f64ee0cf27.mp4?token=p0q8r9x63_TrRgTf3DolIyKqK2GXGGjxJMo4rqKVGeCX1UGXgfiaZa2eP2ulbY6p_qhtwTIINiIG0FhxgK-2IoMufuoRPXU-HS1HW8N5PbcGLnZgC9vzvPbJAGe51c985nv_Ueu2SluCU3r0fr3iFnW94D9Cu_d0TxubNSSaSIFJQpNNpIJHb11oklA66FhLjpJ6CvjPcqxDmHGPfVJZLWl_mfYl6POYDHRXachq-6j-1508_FkxAKELl0KFApkWkqE2ViRVcBi2vQa8kV22wz1B8ppKNC1qBQG6HlwyTJSW6hh9GDvfALj3jtj0uyH0QUblhF1ok9hQmAPmP3GMgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f64ee0cf27.mp4?token=p0q8r9x63_TrRgTf3DolIyKqK2GXGGjxJMo4rqKVGeCX1UGXgfiaZa2eP2ulbY6p_qhtwTIINiIG0FhxgK-2IoMufuoRPXU-HS1HW8N5PbcGLnZgC9vzvPbJAGe51c985nv_Ueu2SluCU3r0fr3iFnW94D9Cu_d0TxubNSSaSIFJQpNNpIJHb11oklA66FhLjpJ6CvjPcqxDmHGPfVJZLWl_mfYl6POYDHRXachq-6j-1508_FkxAKELl0KFApkWkqE2ViRVcBi2vQa8kV22wz1B8ppKNC1qBQG6HlwyTJSW6hh9GDvfALj3jtj0uyH0QUblhF1ok9hQmAPmP3GMgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صنعاء مقابل الرياض  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/90985" target="_blank">📅 15:40 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90984">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">الإعلام الأمريكي :
انها المرة الأولى منذ عام ٢٠٢٢ يتم استهداف مطار الرياض منذ وقف إطلاق للنار بين اليمن والسعودية..
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/90984" target="_blank">📅 15:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90983">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42f7d44463.mp4?token=EjSP0pzjJL65WJo1l2jcGsYGwChVlHthboHLIHUXONooLc_a4Z_D07ggPuYg_hI9fFts4xiPwJviTYSN-LncuHodHsQCmLtEg6s5YFaZhLg04Uhm8-91-MYyUHFg0z5h7qMRgqh7gZhPb8KqQygz_l0RfnQDUwny1CdEbhGhtjqxSjheQtDkj_H8IAvnyV71dOSFHGmeAsdAh1O9iPuaHq-fIZo6VOv5l8CNyJrXgCmbyD529FEF8-3Tij469EzY74mUz9INiHrgiRfRpaqtp8hDQp7q0PxdhWZ4-pUJVkGObat1OMaEz6ry1q4G6vnaCHgQLTHUUntRP-kTQ7dfAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42f7d44463.mp4?token=EjSP0pzjJL65WJo1l2jcGsYGwChVlHthboHLIHUXONooLc_a4Z_D07ggPuYg_hI9fFts4xiPwJviTYSN-LncuHodHsQCmLtEg6s5YFaZhLg04Uhm8-91-MYyUHFg0z5h7qMRgqh7gZhPb8KqQygz_l0RfnQDUwny1CdEbhGhtjqxSjheQtDkj_H8IAvnyV71dOSFHGmeAsdAh1O9iPuaHq-fIZo6VOv5l8CNyJrXgCmbyD529FEF8-3Tij469EzY74mUz9INiHrgiRfRpaqtp8hDQp7q0PxdhWZ4-pUJVkGObat1OMaEz6ry1q4G6vnaCHgQLTHUUntRP-kTQ7dfAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الاخوة الهنود يوثقون لحظات انهيار النظام السعودي العنصري باغاني سعيدة  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/90983" target="_blank">📅 15:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90982">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f2127ef7c.mp4?token=RBryijZqnAL2fMPyJY4k0PT2aunC4sljHxg5ECaC4YX0iCGBjJAgMPjEvs-pD1FkOZomqaJ1ZFUkA0LKhLFQ4-wKCkYIVvUka62lwi7zhBd8Q_BhA5CdroZ9NqBJ8jblk1zkLNkH7Tusfv4bHoXORhyihnjSyQXoK6lw5kQ5KieoR-1vuCXoZCVqvAzUn2c2pqoUiTDFNEbI487-di05j3gzaTrI3R-qwKCxOAcW7R2P1kx7PS4wmKEIuuW3KJxu5cqEH0XxmQi1us6FrR1MZCgM5OxcE8E5PejeOtzPxQu9k0ItSNBLZhWs2_jVNfzIj5Nq7Ia4c-BNOVWWfhGTIjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f2127ef7c.mp4?token=RBryijZqnAL2fMPyJY4k0PT2aunC4sljHxg5ECaC4YX0iCGBjJAgMPjEvs-pD1FkOZomqaJ1ZFUkA0LKhLFQ4-wKCkYIVvUka62lwi7zhBd8Q_BhA5CdroZ9NqBJ8jblk1zkLNkH7Tusfv4bHoXORhyihnjSyQXoK6lw5kQ5KieoR-1vuCXoZCVqvAzUn2c2pqoUiTDFNEbI487-di05j3gzaTrI3R-qwKCxOAcW7R2P1kx7PS4wmKEIuuW3KJxu5cqEH0XxmQi1us6FrR1MZCgM5OxcE8E5PejeOtzPxQu9k0ItSNBLZhWs2_jVNfzIj5Nq7Ia4c-BNOVWWfhGTIjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من الهجوم اليمني على الرياض ردا على المحاولة الارهابية التي طالت صنعاء  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/90982" target="_blank">📅 15:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90981">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fba06ffa5.mp4?token=DfuPykBjh2zy7tlU2A0_VD_acykzNjbuBRgWoSw-phcGIovtJCWv7qBvibEIyj15PirTDtbd7vG648GK4jagYHIMzv6Kot7W41CZXk9L1uTkXb-Z2r5-cx1H81d4JWlyPyEhOEhxUURS6rfoAfZ19INecKAQ4TuCEqWvX7QN7zRD4XOMaHckCU5cT90dnYCAY8loj7cGeqxr0l0eqRfuF_CqnfDZR1uJmBQeuwVGPwZDse6i6qf6P7H4B1-4nAp78sn-K6cmt4FGGJs6J46_E9hboTpLbQLuLD8ESCOyQG2ieDiHTYDD9JPRVCE4MfrS5k6RCYQkyNTtlwD1Dr620w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fba06ffa5.mp4?token=DfuPykBjh2zy7tlU2A0_VD_acykzNjbuBRgWoSw-phcGIovtJCWv7qBvibEIyj15PirTDtbd7vG648GK4jagYHIMzv6Kot7W41CZXk9L1uTkXb-Z2r5-cx1H81d4JWlyPyEhOEhxUURS6rfoAfZ19INecKAQ4TuCEqWvX7QN7zRD4XOMaHckCU5cT90dnYCAY8loj7cGeqxr0l0eqRfuF_CqnfDZR1uJmBQeuwVGPwZDse6i6qf6P7H4B1-4nAp78sn-K6cmt4FGGJs6J46_E9hboTpLbQLuLD8ESCOyQG2ieDiHTYDD9JPRVCE4MfrS5k6RCYQkyNTtlwD1Dr620w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد توثق لحظة الهجوم اليمني على الرياض  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/90981" target="_blank">📅 15:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90980">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53c7108005.mp4?token=iY1SMPI9UgEUB9SdAPVKD9gQR3IPmK0osn0Zg9grBG2dsmq1RNdjQbeIn_mL8-6rMt8VvHeAabHKalv9o8Cfy7HF-CpHpYhAiaV6AlPiZoIzjpa83IW2G7zMfu2bFqXyeFGMpC2PK_PPPIXByIY3FnXTaeH4VPIfax10wDxTuVcTTaeCjlDkhQZMhpP_Iu16Xxtj8d-70wR1-GuATJFwKKD15sSWWS60bBjGl2WO5Q1mihy3GOWiUmiECILa-rWwpGEEFnAxdss9VnVq96zDElWGVHOqh73AwbhCL7twBVe31fd4pQqdrhOWLIbsVhTkmLcK-XRGBFCnJhNpcE2VmD4voNm7eriD2TmwiSERNDcaBFRbWIxD8QUAsPbe7WY1ilDoSZqCEb9Ij_fZkFeg9RnMLQszlQlZPnlrwhAZvuduuqrQWz85WnAR14ob0o5o6lw4vB41zo7X15JvxjHRS-TX--bX3mxZuOwqiBcOBOdk-5NVcOHyUdGF87hcrskFfWIgRv28jwjAY-pfa-iXi9P4qAYQGpBC9A_HlWGho7GP_3U7ouKh5YSmxOJowD6WzqRdSIQqVrGljPkFyiKpMTzHBfNns5Ovi30zRUbq8CGLHCbshrDlkicLUDVw5PXoomdDY2cQFoI8n3wXwMFefOGwJHdJNChawaE8SVfhxFE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53c7108005.mp4?token=iY1SMPI9UgEUB9SdAPVKD9gQR3IPmK0osn0Zg9grBG2dsmq1RNdjQbeIn_mL8-6rMt8VvHeAabHKalv9o8Cfy7HF-CpHpYhAiaV6AlPiZoIzjpa83IW2G7zMfu2bFqXyeFGMpC2PK_PPPIXByIY3FnXTaeH4VPIfax10wDxTuVcTTaeCjlDkhQZMhpP_Iu16Xxtj8d-70wR1-GuATJFwKKD15sSWWS60bBjGl2WO5Q1mihy3GOWiUmiECILa-rWwpGEEFnAxdss9VnVq96zDElWGVHOqh73AwbhCL7twBVe31fd4pQqdrhOWLIbsVhTkmLcK-XRGBFCnJhNpcE2VmD4voNm7eriD2TmwiSERNDcaBFRbWIxD8QUAsPbe7WY1ilDoSZqCEb9Ij_fZkFeg9RnMLQszlQlZPnlrwhAZvuduuqrQWz85WnAR14ob0o5o6lw4vB41zo7X15JvxjHRS-TX--bX3mxZuOwqiBcOBOdk-5NVcOHyUdGF87hcrskFfWIgRv28jwjAY-pfa-iXi9P4qAYQGpBC9A_HlWGho7GP_3U7ouKh5YSmxOJowD6WzqRdSIQqVrGljPkFyiKpMTzHBfNns5Ovi30zRUbq8CGLHCbshrDlkicLUDVw5PXoomdDY2cQFoI8n3wXwMFefOGwJHdJNChawaE8SVfhxFE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لوحة يرسمها السيد القائد عبدالملك الحوثي في الرياض والهندي يصورها.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/90980" target="_blank">📅 15:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90979">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">لوحة يرسمها السيد القائد عبدالملك الحوثي في الرياض والهندي يصورها.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/90979" target="_blank">📅 15:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90978">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6156c7481a.mp4?token=XahQ46tRNFFBorUSFFMQq_urknabEapHlJtUWlbFbRQ5cYouTRkg7yv32ByAJ8q4MLs0vWGjwLVK9ybj0ih7RxwbY9GbRHftc3ptZDCstYcr0fF3Fvb8NKqYuuXra4ZfF2jftxbPM5Y0_N85VC3tY4h8iwJxiDnehqKsLnan41EG04DdWGuovsbZUzho-cdhaJsYAHuTbQ2pyawNEM8WVlWsnJ0s6w2RcWOCK9TH__q7ymvDh8Kv_1Dtl0BAP8flUA70f86p4Bd1rCHr3GT0tb7PNiUrXmKzI1hPNNplnlPs3atbOrc0itYPS8O4lselfAbxWiGe_XHmlknSB9we2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6156c7481a.mp4?token=XahQ46tRNFFBorUSFFMQq_urknabEapHlJtUWlbFbRQ5cYouTRkg7yv32ByAJ8q4MLs0vWGjwLVK9ybj0ih7RxwbY9GbRHftc3ptZDCstYcr0fF3Fvb8NKqYuuXra4ZfF2jftxbPM5Y0_N85VC3tY4h8iwJxiDnehqKsLnan41EG04DdWGuovsbZUzho-cdhaJsYAHuTbQ2pyawNEM8WVlWsnJ0s6w2RcWOCK9TH__q7ymvDh8Kv_1Dtl0BAP8flUA70f86p4Bd1rCHr3GT0tb7PNiUrXmKzI1hPNNplnlPs3atbOrc0itYPS8O4lselfAbxWiGe_XHmlknSB9we2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد متداولة للحرائق في العاصمة السعودية الرياض على خلفية الهجوم اليمني  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/90978" target="_blank">📅 15:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90977">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">مشاهد من اثار الهجوم اليمني على الرياض  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/90977" target="_blank">📅 15:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90976">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">جيش العدو: اصابة جنديين في جنوب لبنان بعد تفجير حزب الله عبوة ناسفة بآلية إسرائيلية</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/90976" target="_blank">📅 15:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90975">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5af67e77ee.mp4?token=E0xXR1_pfVt4_ETYK42NF8bweh9JIfbYUdzHB0h0zyibuKTTz3bPyRODa9XSJsgzUaHRPDcjaMMkSMNJTBePoCV98OwbRQ77phpADO-xs8LyruAvypMx2Lo0OCn30OrJfrPjXG6UgT71RpaOhnsV1yL84A4OoywAd2Pj_clRmKRZFGr83sBTkC0U2FIlnP8njCL_hP2emBW3k53tMXkvoJXUCo8IIdmt-Y30QhA0JhMYkbCSaVeLmee_y0W-2zP-nhB1ZF_oIONIyUDY3pEFutkNzow8WFb5w3robQ7Jvwh8WQYPWxnwqSUWueG9XuhAYrDCn5OiQ6QXi7m6aJqJJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5af67e77ee.mp4?token=E0xXR1_pfVt4_ETYK42NF8bweh9JIfbYUdzHB0h0zyibuKTTz3bPyRODa9XSJsgzUaHRPDcjaMMkSMNJTBePoCV98OwbRQ77phpADO-xs8LyruAvypMx2Lo0OCn30OrJfrPjXG6UgT71RpaOhnsV1yL84A4OoywAd2Pj_clRmKRZFGr83sBTkC0U2FIlnP8njCL_hP2emBW3k53tMXkvoJXUCo8IIdmt-Y30QhA0JhMYkbCSaVeLmee_y0W-2zP-nhB1ZF_oIONIyUDY3pEFutkNzow8WFb5w3robQ7Jvwh8WQYPWxnwqSUWueG9XuhAYrDCn5OiQ6QXi7m6aJqJJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من اثار الهجوم اليمني على الرياض  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/90975" target="_blank">📅 15:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90974">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3327b4315b.mp4?token=uJDUFKCL58NGMN_DnvuJCw7GanGVjUIjaS6L6lVm1KVpYqM2nrIJ15QVXKqLqNRv8QPRQhHYfMIBj0KCiP6Ocfea18aprQN8BMOiJirRm73xySVi36DSwTB_NkjYzA5hgI-ELAbrieYT2oo775ZCJHIrLHfwRj-UO7-mlpTBOzgCbwpL9jq5b1J9DNOFDq4KQp4qMcR8wLK7K76dA3atNxyD2mfJGpsw_Vgbn2u4wrRTqIgY-9-PZOQHH_JkwYq1pzIO5eOdlo3pyZ27jwfLze7vhg1QgzdjGDX4u4zj6JK3Te8ne-dT1IHuVdp847-jGVGzE2gyjUfgmX8qR7zcvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3327b4315b.mp4?token=uJDUFKCL58NGMN_DnvuJCw7GanGVjUIjaS6L6lVm1KVpYqM2nrIJ15QVXKqLqNRv8QPRQhHYfMIBj0KCiP6Ocfea18aprQN8BMOiJirRm73xySVi36DSwTB_NkjYzA5hgI-ELAbrieYT2oo775ZCJHIrLHfwRj-UO7-mlpTBOzgCbwpL9jq5b1J9DNOFDq4KQp4qMcR8wLK7K76dA3atNxyD2mfJGpsw_Vgbn2u4wrRTqIgY-9-PZOQHH_JkwYq1pzIO5eOdlo3pyZ27jwfLze7vhg1QgzdjGDX4u4zj6JK3Te8ne-dT1IHuVdp847-jGVGzE2gyjUfgmX8qR7zcvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من اثار الهجوم اليمني على الرياض  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/90974" target="_blank">📅 15:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90973">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc0c282f20.mp4?token=Li5CDY5We3kF6NofE0RFo_Njx7kBZ9O71HGcNdDdyp9UXDJVVVK_03R6yAzcEVwh30LeEWpkB8AzToHZHN3kxTZcOCP8kyl8lLpN8OfcG0PEkv7w6G2cbHpbDO-rKfWEBumfE807WinxrgRLYsIZRH8A0_26I81AOReOkdnSTs3AaKixGYWsI-dCx2GpyXnoYHj52Gh4dm1nkEYTa7XbeHn9jLGCwv5jiSKzaal1CtUmZLwKV7UVx4Hi5JilRdmN94F978j2yQoClRrZbJrGraCkqnIiRYsLHo9t0QhGEF719lpysRXapPYIUQ527U_VEMEHQePY1k2ZqbSGkh_T6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc0c282f20.mp4?token=Li5CDY5We3kF6NofE0RFo_Njx7kBZ9O71HGcNdDdyp9UXDJVVVK_03R6yAzcEVwh30LeEWpkB8AzToHZHN3kxTZcOCP8kyl8lLpN8OfcG0PEkv7w6G2cbHpbDO-rKfWEBumfE807WinxrgRLYsIZRH8A0_26I81AOReOkdnSTs3AaKixGYWsI-dCx2GpyXnoYHj52Gh4dm1nkEYTa7XbeHn9jLGCwv5jiSKzaal1CtUmZLwKV7UVx4Hi5JilRdmN94F978j2yQoClRrZbJrGraCkqnIiRYsLHo9t0QhGEF719lpysRXapPYIUQ527U_VEMEHQePY1k2ZqbSGkh_T6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من اثار الهجوم اليمني على الرياض  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/90973" target="_blank">📅 15:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90972">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02deb34747.mp4?token=kvrbWAfMRiXDYLx-Hs573uqLA9PaxUkjdFnlV0vuqbm5ockhSPcpjdfRo8-w3o1gFI2LXMI-OilPvCvLy_ATIpkC58iInGkrNV1vgUYP1qRlJpnWotBFih1tdL4z-4gkd_q6C0gH5eUNEbY0LHPSnCUtFhf1qvvShxruvh69wKStjFU8Q14KBls0Do3CgeE6mxUOL4ymugLsOGeLEBZKZUQ-VaipiSUefgLVnzsaotYpGrmTltmzqKPTfl96SwXFsPo1DfrR-RWhCm8XH8lOfdmV3zNcdZnM9UVDkJO0qI8mBn1CIX5Sjxf4n6mKRIJR763BkkqvBUCnqqthKJMaDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02deb34747.mp4?token=kvrbWAfMRiXDYLx-Hs573uqLA9PaxUkjdFnlV0vuqbm5ockhSPcpjdfRo8-w3o1gFI2LXMI-OilPvCvLy_ATIpkC58iInGkrNV1vgUYP1qRlJpnWotBFih1tdL4z-4gkd_q6C0gH5eUNEbY0LHPSnCUtFhf1qvvShxruvh69wKStjFU8Q14KBls0Do3CgeE6mxUOL4ymugLsOGeLEBZKZUQ-VaipiSUefgLVnzsaotYpGrmTltmzqKPTfl96SwXFsPo1DfrR-RWhCm8XH8lOfdmV3zNcdZnM9UVDkJO0qI8mBn1CIX5Sjxf4n6mKRIJR763BkkqvBUCnqqthKJMaDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من اثار الهجوم اليمني على الرياض  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/90972" target="_blank">📅 15:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90971">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7e0763727.mp4?token=b85uRXcnVnHnI3-rgtj1UMLe0B-s0uOTxF1MzPUxq9j8FW9v-FvVhJwoS5rp-D4-ymDbBfLRG5kNhideKj8WbDK4_TPdhHsHn2N7PTXYcZtPRHr8LZ0950ZyZLLyMbkoG7TYMzTBOYsnZlnen3yefIbpRWM8lrZDO7THuAE2G1paKKVBfT-1Vpuj3kzaSb7G1_4oMFtA_gJ9aYWOMYTUWGc-aFrpSOSGcmQG2_CwCfUTCFTvMO2yKraYsjFHS_bLxQKrClv5fZefheVne-A08fxPl0TK86Ebg6Gq0kJMi_QCNHQHmZ-woMCMLzhxQ5o3UPvCBCHz6yzzM1yD1x9M0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7e0763727.mp4?token=b85uRXcnVnHnI3-rgtj1UMLe0B-s0uOTxF1MzPUxq9j8FW9v-FvVhJwoS5rp-D4-ymDbBfLRG5kNhideKj8WbDK4_TPdhHsHn2N7PTXYcZtPRHr8LZ0950ZyZLLyMbkoG7TYMzTBOYsnZlnen3yefIbpRWM8lrZDO7THuAE2G1paKKVBfT-1Vpuj3kzaSb7G1_4oMFtA_gJ9aYWOMYTUWGc-aFrpSOSGcmQG2_CwCfUTCFTvMO2yKraYsjFHS_bLxQKrClv5fZefheVne-A08fxPl0TK86Ebg6Gq0kJMi_QCNHQHmZ-woMCMLzhxQ5o3UPvCBCHz6yzzM1yD1x9M0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خروج المدرجين 15L و15R في مطار الرياض الدولي عن الخدمة  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/90971" target="_blank">📅 15:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90970">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مشاهد حصرية لنايا من الرياض   حرائق وأعمدة الدخان مستمرة من مطار الرياض الدولي …   https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/90970" target="_blank">📅 15:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90969">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c84e1ee9a7.mp4?token=WcLbhej9tv6Hk-zmnn5GQCKzIfEiLgXcwSCTry5Xaw8ckieZ50zJ3XxAULi7QWhUM10zdnBt9t_DamHmZc2uoyVrxame779GuM2CFmem76O0hHUTDi1ab8YnqHD3NotGr8fOSFI772iFk6QrTDBSnm7ss8T385VD5HuI1nf31aB7Mz-BGET0MZtD-UB_UbyloZmlA_9AdIZq2j9IUXWtkGSv-tHec_jRiCJn-2RH_1AlMxAcj4kyZmofmWHg6iH2ca2wq_8JLDcQOIYbC4vkL76KCC89RZog3ipU5zOL_B2oOI7-bcacovtEppFYQGnKZSTJGu3AHTdPBYimmMy1QgE_9HPpvj_S3wa7Ktp83bYBDNrL63rj9fttEDW9u25F4rs8Ix2ulY-NVXDTL4JuBz4xTy1HgagM9FQ672PIPYeVghfmxS8giiChUMIEhvP4qesNfa4XqfYQufcM9ApLFBLMjBoV_zGZt8WvWsAP67BTecZPlEAGEkNtTINWUZtzbEo41hUzBuemAUe54Awo5mtAF2M5_cevcIFxILIat9jFXa714qZVQTTYl2jyrlF2nX40YGGv5yCn4R6_F9NZNTFYcZH8F6p-Ki8hx-WWFdBZnC6K8s7cXKjBsEGUloT5_zGJoA1z5bZ1fAHCBLY1ekdlnh8RBbCU8ehNgoL4GRM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c84e1ee9a7.mp4?token=WcLbhej9tv6Hk-zmnn5GQCKzIfEiLgXcwSCTry5Xaw8ckieZ50zJ3XxAULi7QWhUM10zdnBt9t_DamHmZc2uoyVrxame779GuM2CFmem76O0hHUTDi1ab8YnqHD3NotGr8fOSFI772iFk6QrTDBSnm7ss8T385VD5HuI1nf31aB7Mz-BGET0MZtD-UB_UbyloZmlA_9AdIZq2j9IUXWtkGSv-tHec_jRiCJn-2RH_1AlMxAcj4kyZmofmWHg6iH2ca2wq_8JLDcQOIYbC4vkL76KCC89RZog3ipU5zOL_B2oOI7-bcacovtEppFYQGnKZSTJGu3AHTdPBYimmMy1QgE_9HPpvj_S3wa7Ktp83bYBDNrL63rj9fttEDW9u25F4rs8Ix2ulY-NVXDTL4JuBz4xTy1HgagM9FQ672PIPYeVghfmxS8giiChUMIEhvP4qesNfa4XqfYQufcM9ApLFBLMjBoV_zGZt8WvWsAP67BTecZPlEAGEkNtTINWUZtzbEo41hUzBuemAUe54Awo5mtAF2M5_cevcIFxILIat9jFXa714qZVQTTYl2jyrlF2nX40YGGv5yCn4R6_F9NZNTFYcZH8F6p-Ki8hx-WWFdBZnC6K8s7cXKjBsEGUloT5_zGJoA1z5bZ1fAHCBLY1ekdlnh8RBbCU8ehNgoL4GRM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد توثق فشل الدفاعات السعودية بالتصدي للهجمات اليمنية في العاصمة الرياض   https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/90969" target="_blank">📅 15:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90968">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">توقف حركة الطيران قرب مطار الرياض الدولي قبل لحظات   https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/90968" target="_blank">📅 14:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90967">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14d4220bd.mp4?token=RWe9Lq1CqbXaMOZ80zdhoUnVh5oqcJ1GUFuG7cFgILU6tMy20-7fGsL2L6D0wjv4YgKVOg5_3wbXe4hz2xszbQBrg9yymE9CjIBM3REO5ebO4OiFL8j4BjQSJBdosan2KFZDS1_PUxLlm6tRaEJt3B01-oK4ouzj-_8OLwV5rtQf5j9cSe_-R_w9GQwbm5ZakYlwk0TH7DZHc8fkE3GVHQBa8oMbWsPOJpKQpoPJbh-Ir-y9b36c3yBoq7D2MwlqxjZTt8rgWiuJEuZnvFJkjPT_xQuWDArYSw0m8NNNBJnYBdK-x6d4bBO4sFLdOptwj_UNnz_1ZZmqZw1KOBW7Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14d4220bd.mp4?token=RWe9Lq1CqbXaMOZ80zdhoUnVh5oqcJ1GUFuG7cFgILU6tMy20-7fGsL2L6D0wjv4YgKVOg5_3wbXe4hz2xszbQBrg9yymE9CjIBM3REO5ebO4OiFL8j4BjQSJBdosan2KFZDS1_PUxLlm6tRaEJt3B01-oK4ouzj-_8OLwV5rtQf5j9cSe_-R_w9GQwbm5ZakYlwk0TH7DZHc8fkE3GVHQBa8oMbWsPOJpKQpoPJbh-Ir-y9b36c3yBoq7D2MwlqxjZTt8rgWiuJEuZnvFJkjPT_xQuWDArYSw0m8NNNBJnYBdK-x6d4bBO4sFLdOptwj_UNnz_1ZZmqZw1KOBW7Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مواطن سعودي يوثق لحظة الهجوم اليمني وفشل الدفاعات السعودية بالتصدي له  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/90967" target="_blank">📅 14:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90966">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdf1563a0f.mp4?token=TamK7rDFRi5fQ88lIOJY86STqP_NamqGF2Tj1dVfHaQEeJzO1jVhzav517W3LXf-zgHYged4VBKqOB8VMEI19d5yaEVdInWoU0pj09CMHUg76xJhY-FZA5qQ9s2je4asT7bf1945oNLmqAUyqtSuaQV3IrQOjePKZ0YUHyn6v4zgv_g8kKmNQU8meoj9YMAQ-fr7aYe43a0KqCmjvxY8v1fjHQBWH_Ka3ziqmgCto42cSjyyMPRW1VryIR_Uf1JebL7mKv6ZyAmhQGDqSlWXnkZNG_thzaGQhCbRvLQ_hvwgonBToerh8ehhcOZkBoD47kjCq4NEx39ZP593PEzGlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdf1563a0f.mp4?token=TamK7rDFRi5fQ88lIOJY86STqP_NamqGF2Tj1dVfHaQEeJzO1jVhzav517W3LXf-zgHYged4VBKqOB8VMEI19d5yaEVdInWoU0pj09CMHUg76xJhY-FZA5qQ9s2je4asT7bf1945oNLmqAUyqtSuaQV3IrQOjePKZ0YUHyn6v4zgv_g8kKmNQU8meoj9YMAQ-fr7aYe43a0KqCmjvxY8v1fjHQBWH_Ka3ziqmgCto42cSjyyMPRW1VryIR_Uf1JebL7mKv6ZyAmhQGDqSlWXnkZNG_thzaGQhCbRvLQ_hvwgonBToerh8ehhcOZkBoD47kjCq4NEx39ZP593PEzGlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرائق و انفجارات قرب مخزن شركة سفاري الان داخل مطار الرياض  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/90966" target="_blank">📅 14:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90965">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AsmcGh38qzZ64VumrtmA71w3nXrbnHW1kFAHkeOwVFRN04ZCu9eOfhwYQXQArKId7ytiv_YCa2t_-xZVFjLIAIQmpCfWBLol7hN60Hslzo1is-vlXosOvITo3-qNIGNxiPT_8-lC48l6fmx98jjHJVzAXYtp7Jz4Z5G4gX8RZLUAQmw7h1sJelAdREgZwFSVyXi9OVS1u8MrT1KSae3FFdNby22sNjwFcBz5-FcC9YVqhxfaUxm-eXOqK1rE4PC29e150Wdt30MVWVTpC5HMevGB_NL0Ufu77hsUO_Whv0PCYKK8uEJNIk4vDFsA9eo7COqKIWPNSnmcfwEzfbNvqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الرياض تحترق  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/90965" target="_blank">📅 14:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90964">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bef5be52b2.mp4?token=og3OxcTRmM3jm3TelwjLJmWk6OymBoGJZrCcL_wFAdP0J87Ml2g0yvE9FarzcJwlwzQO1zGHzBOZLVdc04Di-fG8_0KZiwuNXun4jryHp54tRslB4PG0sNCEy_uz4N9X-rvyji8F-byWsVwiasGK24fp9NT7Dz8LeWVztbuVCtrs-f0HSd8oBTfsqyW27QF3wS8VQVH81LR0duZnjm1TU6NQv5Zlc2R83s2ThZH0u0yWDgPR1Lj4gx0Bw8CjglZkSkGGfeBEyZ1vLtvqRa78WOzmFWJujYU3W30KJsb1x3cK64XXM2A9ZygVyiVssRN-vFETK5Qexl_-fQaOwUK9amvEKI2Z58lWFJ3OHyuArkhF8k75PKfN3B3fPiMNCjIe7W7mDPD7W0FAjupggJhnGOs8gU2GGPoU1UBmgexB18mPBiYb9fZD05Dx8gvfD_Tnd6oc8Bd1Zow-Nzls-5RTvCIvqM7a7K6_XYnLbHyLTAyCf81lw-5rdKkkB-aMHpzQ8nVrOx5wkQ3mYEay4tfLn0YdEoTGpwFHIKgX2MMRpZzPweklkrdTBLw03vwQHDTLFy8RSToZ0BqP1FsrMWImqYcbnsNrLPLgTWWVAjnh0fI79rjPmq7MAxd-q6uQyqde2pmE7vqsjFkKD4JhpFdvzVVZNAuJt5XvcQsrfIxZ4oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bef5be52b2.mp4?token=og3OxcTRmM3jm3TelwjLJmWk6OymBoGJZrCcL_wFAdP0J87Ml2g0yvE9FarzcJwlwzQO1zGHzBOZLVdc04Di-fG8_0KZiwuNXun4jryHp54tRslB4PG0sNCEy_uz4N9X-rvyji8F-byWsVwiasGK24fp9NT7Dz8LeWVztbuVCtrs-f0HSd8oBTfsqyW27QF3wS8VQVH81LR0duZnjm1TU6NQv5Zlc2R83s2ThZH0u0yWDgPR1Lj4gx0Bw8CjglZkSkGGfeBEyZ1vLtvqRa78WOzmFWJujYU3W30KJsb1x3cK64XXM2A9ZygVyiVssRN-vFETK5Qexl_-fQaOwUK9amvEKI2Z58lWFJ3OHyuArkhF8k75PKfN3B3fPiMNCjIe7W7mDPD7W0FAjupggJhnGOs8gU2GGPoU1UBmgexB18mPBiYb9fZD05Dx8gvfD_Tnd6oc8Bd1Zow-Nzls-5RTvCIvqM7a7K6_XYnLbHyLTAyCf81lw-5rdKkkB-aMHpzQ8nVrOx5wkQ3mYEay4tfLn0YdEoTGpwFHIKgX2MMRpZzPweklkrdTBLw03vwQHDTLFy8RSToZ0BqP1FsrMWImqYcbnsNrLPLgTWWVAjnh0fI79rjPmq7MAxd-q6uQyqde2pmE7vqsjFkKD4JhpFdvzVVZNAuJt5XvcQsrfIxZ4oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعمدة الدخان تتصاعد من العاصمة السعودية الرياض بعد هجوم للقوات المسلحة اليمنية  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/90964" target="_blank">📅 14:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90962">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مصدر محلي سعودي لنايا
بناية تابعة لشركات النقل اللوجستية قرب DHL ؛ تعرضت لدمار شامل داخل مطار الرياض
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/90962" target="_blank">📅 14:40 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90961">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اعمدة الدخان تتصاعد من العاصمة السعودية الرياض بعد هجوم للقوات المسلحة اليمنية  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/90961" target="_blank">📅 14:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90960">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12ce0ef0c5.mp4?token=I3RI3rPl3UOzM6U9O1EzI5SclhByY4OT6uBEsBYusYceFJsfqhAVZ-lOF4P_kFo_ClSunYDFjcUswpNxdRtCjp2GK1inXSjubDt6oURd92TF7vp6TGrZNtpeTcZ_JAa6u-m2AQ7eEFRTjUl4Vqu5kYnUe2x33EKQ4C3HoTusmPhcP0GogSVIgORrvDZLDNYvuyGoBGaCGcPdaoaBeBa_mZHafC54zpyjh35PTvtt0vRlxUwq0Wfl1J5w2GD046SoY8K4Zxv2D9aO5OzYRQqCv-1-lfjgbIiykE7XxxtZtUMdlJwE7zlV5pJMj9MLa021L75pDzS_gCSDr5mD9WDNoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12ce0ef0c5.mp4?token=I3RI3rPl3UOzM6U9O1EzI5SclhByY4OT6uBEsBYusYceFJsfqhAVZ-lOF4P_kFo_ClSunYDFjcUswpNxdRtCjp2GK1inXSjubDt6oURd92TF7vp6TGrZNtpeTcZ_JAa6u-m2AQ7eEFRTjUl4Vqu5kYnUe2x33EKQ4C3HoTusmPhcP0GogSVIgORrvDZLDNYvuyGoBGaCGcPdaoaBeBa_mZHafC54zpyjh35PTvtt0vRlxUwq0Wfl1J5w2GD046SoY8K4Zxv2D9aO5OzYRQqCv-1-lfjgbIiykE7XxxtZtUMdlJwE7zlV5pJMj9MLa021L75pDzS_gCSDr5mD9WDNoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الرياض تشتعل   https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/90960" target="_blank">📅 14:36 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90959">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EnrX0APqH_YIoBnA2W2s3m5hfpI0Ep8yJolpA4AoIyUxULwyVC3x9ZcD5yFT-O7_Dc0NP9b_0SrCmmH3vI0gZJ0h5GhbuuqUOO0WG4vRVEqWC_gegFO9xPiemF8-HtntWH4n2u5GQ0Rtf6nfIZzkdH02mp6yqz5cysIzCEGcttQaGmhDohPAzh2xOQdZoh2vtsFsy92UE8Juh2o7kYFBKYz43s-MJK7wn_S3Mvm9KVLipE2RLxVn3QkW9rTwmt6tB17fHjk-xZFdszW9jYhVVupfPrUfE4cIYQSMZH8qrWfemnHlrc17G9I9JYwzt5q1DwnHob3EDL1DBtBRNQJ0Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توقف حركة الطيران قرب مطار الرياض الدولي قبل لحظات   https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/90959" target="_blank">📅 14:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90958">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qy_1zw2NyyLR7wiFITVfnAl-1B7HafVVFdi4SijKTC09bhBve9vCm72ih7EAF5MYF1w_jDDkYZ29BCtHSDpwYJ05t5APvgX_0IuouYW6TkQDFWMNjHhhQYG07z7EB8TfVFBpE_dpYNSi4qoMTPh3gMfQELUCkS-A_Bgjds3AI1GmAsluIrjDEpvRTB5SCvWrz8O9Re_j6e2JAR3aqmFqm-TWyNVwUjZhkvwPUtwo7bACtMC5JyDrY6PiY1Uvm8TI_wXCGBY9ofPSKJVpdY9TIEjKmr1E9AeRnIxMT_n9sKrzMPRtX01LrpGoVVqT4YlyQPztZ2R8z-oasPm1enRoJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توقف حركة الطيران قرب مطار الرياض الدولي قبل لحظات   https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/90958" target="_blank">📅 14:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90957">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWIWTCvEwemqCQm7ulh-mz3LzlCB-b6Ey9wEOsWwKr5G6EH_mOhedZPeupxvLIxsWWGKcEuHKOcm89H386QQLjNaw2vNbxUbZod05N60HfjYXLAqSgYWsSguSKIl0dGa1jqeSDQBvJLyYRpvgkPW8kGcFDKETwRQawijvk4t1uDUzAwTQMdgqrWiLelJ5bisTiEgqQBChsQtIIX-Khinz976dTvYDNcrpJqZM9aA62RQ0vrBMq_CgOBa3hUfanFQG-CcPrMoS6SAIUsjyjnHJdU7bSK6WaqvoG2_zadOMhocBV4A3fR-2gkjSrlMZvzBPYjModY7pIF1fxkJ2AF1dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توقف حركة الطيران قرب مطار الرياض الدولي قبل لحظات   https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/90957" target="_blank">📅 14:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90956">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HE-UOckmuFghY_BphlgvQIn_WvnIJkHp3kv1wFWDRDlrr2ILvMBERzFSBex55RIhT3cV2KrUJT2p3JqnwzlmVE-S22QkZXZ0ABsb9D-AgFy-LdB-08Gk7LyQRKfmFVKbaj_SyH4W35GQ4qQ-krV0oEUGeAY57EOHSVnx_NfpECdz-5rE4I2szUNlrKS0KKo-fYWS9VoY3qucrigmYQVV72onndTojKdNV3J7Js_AiQub0iztI77cY8dMs57OPWzdGSz_eXY2pdR7v0o2fNB2SDhWuTJ3Vizu9tsLOIMqUKGOoPSJoAZWkt5GjAW7e5YqyyHwMOdWJfkKbprnSlOzUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان تجدد الانفجارات قرب مطار الرياض</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/90956" target="_blank">📅 14:19 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90955">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFqdMUfjuWErc8j8CzrLoF26vXJL4UYWTvJeL1IP1IjKefAb3H965OKXHPnZY6oR0HShQKQjmA0wYINWw3vUqNhDWSHMYvs5Kl3c3sdjR2KIv_P8NlyHWO2V4-LSJ5e3n_-l0mQHaONu0x30Iz5vrmO-Qll-pdNby8xqU5rCsryxJttmNUr36dhyjaxbCNGQ84Yqm1lU4Nu21lXkR8Scr_DznHtcQreF7XH8krgRd6ekOLh9mgL5h3T6zLMeZA-WzbM4u4pTQTHszbi8DxpkpZowylXljLCdKR-bfEC9jpDE7HbQHyWL4HtP1zBoPunft-KV8InBvRjugHPOzuiSMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رويترز : رصد ألسنة لهب وسحابة كبيرة من الدخان الأسود ترتفع بالقرب من مطار الملك خالد الدولي في الرياض ..</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/90955" target="_blank">📅 14:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90954">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">رويترز : رصد ألسنة لهب وسحابة كبيرة من الدخان الأسود ترتفع بالقرب من مطار الملك خالد الدولي في الرياض ..</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/90954" target="_blank">📅 14:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90953">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">رويترز : رصد ألسنة لهب وسحابة كبيرة من الدخان الأسود ترتفع بالقرب من مطار الملك خالد الدولي في الرياض ..</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/90953" target="_blank">📅 14:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90952">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">وزير الخارجية الباكستاني ييحث مع نظيره الإيراني عباس عراقجي حماية منشأت الطاقة السعودية</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/90952" target="_blank">📅 13:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90951">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇮🇱
السفير الأميركي لدى الكيان مايك هاكابي:
يوجد علاقات عسكرية واستخباراتية ممتازة بين السعودية وإسرائيل وهذا سيكون مفيدا في تقارب أكبر وصولا لدخول السعودية باتفاقات أبراهام.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/90951" target="_blank">📅 13:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90948">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IylQJ-WLaVAZcWKjM9Yad13U36s-py55228ma5lWFNGLDPVSLOIWkePEUQggOTcAzV2gdIREfNymioYRIGYmA89SDLjzgSybh3UiYvC852twRiJfPa4Ik0Gn-uJppKJswQDWC2akfwzYM4mjB_rTCsmGwJcjzsrmwM__Rwl64X0FhXkxUIjOvGm-Ue9mcFKNp8zoAs4oAzqMXsjhtAHPVW-so1Gjx5FLH4-o1QDuJMf0DulBd2vgyCjpG6elkF-EZp6n4AdH45uIzDldDazcHumZHt1z60iDrIUPjGcSSF3rV6cnyG5Jlhg-pUqjzFADwAF971OnHtfl3R919W4Jeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BcIq1xS0TD848Q482lRFiykL9eEwX6k4dTDPtoSAzI_7nKk4LVtLI_tyr7D2e2KAeIv0V3HT4OoNIvIFGupmANu5ws9bExbmtb7LTWq_SsxyJ6MNKGF3FWS8x_Xouy2onz6V8WFE8Van0yo-NNmORmxxvYPrCimiohEh3L0QD57tRdCsDqmSkcmFyGKJCqcbRoN-im-QgybyXu7ZgW00rPfKswoAFtdTRinrv_onXIUKIk7frep1wFxhp0LA2qXZuIlQHvvXuTge2sjSevsFwJM7vYOHHiRtUiMb-bBcPQ_2ehEzmjiC7WXhEhpXRSQlrPBnrModRaM8Nb6qHGMRIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K5jo2fffGevFdBbu6TD-qZopahxQbF4HYfgZ2HuPxrIWOFTI6lLe99uqVVcA5mwDvVZE-LiTvA986-GAo1Y-UqcK2QIt_HDFFXDVYiqc0r_5eK8h8_ypXBnxr31jXU49jvgCrjhqOwBn8mkZ9ABVdoVBjU2fiqLl0sPJrbIQ-LjiNsKBJV5mVjP5OijuuS9vyn0XnoXjtyXlnIfePEqpdnWT1tNDs948AzKeNZSgesNrhsNNjvqmYT02JBYHqddh3bFJ8oG8tLxpaU8l555tU-lTKteeS7vmFGbKXMFJvFDCmuaRfo4G_-hyPJrGgdalrqKodaZkqpxJFTACjU8KDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇷🇺
🇮🇶
موسكو تنتخب من بغداد
شاركت السفارة الروسية بالعاصمة العراقية بغداد في عملية اقتراع وانتخاب أعضاء مجلس الدوما الروسي ؛ كما وجّهت روسيا لأول مرة لجمهورية العراق المشاركة بصفة مراقب دولي من خلال تواجد المفوضية العليا للانتخابات  العراقية وعدد من الشخصيات الرسمية ..</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/90948" target="_blank">📅 13:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90947">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇺🇸
🇮🇶
مسؤول أمريكي:
واشنطن لن تترك أي سلاح خلفها بالعراق بعد الانسحاب.
‏ترامب وجّه بعدم تكرار ما حدث في أفغانستان خلال الانسحاب من العراق.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/90947" target="_blank">📅 12:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90945">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K77xayuQqFD-f979994q4DquWl4BoXHvMOKTkLuAmcQsaQyNnv442qDI_zy4m4lQViIs7pZtohfKJmmyOWlvFWaatfWTAPHXr2U9A2lUUy5_yDnFJdlqv9AZVjK-biQ-vWCC2gWv5VUnvtu8ajZWXPUh2sctEFcU_qURbgQHqdp_LlTHOAIArPuQg_4LZkEblByHqNw_A_IoeGr-R8B3JRTLmUZeQazEh1HibxV-uJlHc6HmdWZ3q0t2XMjGDwMGX2DR5jfdhBG5iNq1mtdTID51tVuisdGm5NClrkvKXjNQ7MQmw1Pq4eCKsENRrwPapI8widyBvSM3t3aZo8VmsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
توقف العمليات الجوية في مطار الملك خالد الدولي بالعاصمة السعودية الرياض.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/90945" target="_blank">📅 12:19 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90944">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇮🇷
🇮🇶
وزارة الداخلية الإيرانية:
نقيم علاقات ممتازة مع جميع الدول المجاورة، بما في ذلك جارتنا الشقيقة والصديقة العراق؛ فقد توصلنا إلى تفاهمات بشأن قضايا الحدود ونشهد تفاعلاً إيجابياً مع الحكومة الجديدة، ولذا ليس لدينا أي مخاوف في هذا الصدد.
العراق دولة مستقلة. ويسعى خصومنا باستمرار لاختلاق الذرائع؛ فتارةً يزعمون أن إيران تقوم بأفعال معينة داخل العراق، وتارةً أخرى يركزون على الانتصارات الباهرة التي يحققها الشعب اليمني.
إن تعاملنا مع العراق إيجابي للغاية؛ حيث تعقد وزارة الداخلية ومحافظو المناطق الحدودية اجتماعات دورية، ولا يساورنا أي قلق بشأن تهديدات قد تنطلق من الأراضي العراقية.
كما أننا نحافظ على علاقات ودية وتعاون جيد مع إقليم كردستان، رغم أن إيران لا تتهاون أبداً عندما يتعلق الأمر بضمان أمنها أو الرد على أي تهديد يستهدفها.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/90944" target="_blank">📅 11:58 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90943">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a3fefb345.mp4?token=WRL6WvAIq_MMA3Xd9Rpl8ow6goyhP-YQyiH1FGFRroN9toygM0wpCi2HEBRwgRVpW3jB4lVRajD8jdu3mXyZ_EKDwWy4CvmVC-HrOXFjKP31zePkJ2aHnb5HKtZFZAb18v_FPqGupnHWN_nAWo1hMwEbx2cu_X2Vi_KB8XleJ4NqNt_Ek9wCS-jkMSzN0Ax0I5tGl8PmMu0VMqcGvBY8zpvErDXAOxjcic2IqslHv4MF4sTJ38tOHD_7t0w7e2F0tANMByQVt0z3N_1BCBC3qBl9loBg22LWX3utD9fppC1jS0T3OJKPKMNTkqaXUhOmPtuJ21QzqF-reFsP2wD4Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a3fefb345.mp4?token=WRL6WvAIq_MMA3Xd9Rpl8ow6goyhP-YQyiH1FGFRroN9toygM0wpCi2HEBRwgRVpW3jB4lVRajD8jdu3mXyZ_EKDwWy4CvmVC-HrOXFjKP31zePkJ2aHnb5HKtZFZAb18v_FPqGupnHWN_nAWo1hMwEbx2cu_X2Vi_KB8XleJ4NqNt_Ek9wCS-jkMSzN0Ax0I5tGl8PmMu0VMqcGvBY8zpvErDXAOxjcic2IqslHv4MF4sTJ38tOHD_7t0w7e2F0tANMByQVt0z3N_1BCBC3qBl9loBg22LWX3utD9fppC1jS0T3OJKPKMNTkqaXUhOmPtuJ21QzqF-reFsP2wD4Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
أعمدة الدخان التي رصدت شمال العاصمة الإيرانية طهران ناتجة عن حريق داخل أحد المطاعم ولايوجد أي حدث أمني.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/90943" target="_blank">📅 10:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90942">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔻
🇷🇺
مسؤول بالناتو:
روسيا شنت هجمات سيبرانية وانتهاكات للمجال الجوي طالت العديد من حلفاء الحلف.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/90942" target="_blank">📅 10:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90941">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇷🇺
الدب الروسي يداعب اوروبا
أوقفت مطار لوكسمبورغ الرحلات الجوية في وقت متأخر من يوم الجمعة بعد ورود تقارير عن نشاط طائرات بدون طيار غير معروفة بالقرب من المطار، مما اضطرت الطائرات القادمة إلى التوقف أو تغيير مسارها.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/naya_foriraq/90941" target="_blank">📅 01:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90940">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEQRegVNTEEV-38BoK8iDmmq7V8qLhJwBuHcbpjnAHQoMAITYYrUYzMlIF-oSo9SDEYg7fyMf-WXLT0t6zUzxG_LihHH-l5uZ01CDBN2cy7roMl2ffEFI-caKX-cGZxZGa2r_BFjfpwBfkdPje3A6T9dHfIFq425paEBLY1XqfzwCFcG1BeaifFVNPS28yE1gy1nI68Xel9tk4izRlTWpSoqNlIM1VezNiAMWL_u6V5ju-e5KTI04WYFZ3ZkDQkAKgJLeSMLlK0YWGiA5I7gPHHXu48G1Q127fnxNcZCeRp0Efxf1MyVxbHDJ0zUilTLd_QfiIIBcNF6CDkpN6qS7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محافظة فرسان تحت القصف</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/naya_foriraq/90940" target="_blank">📅 01:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90939">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/naya_foriraq/90939" target="_blank">📅 01:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90938">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/naya_foriraq/90938" target="_blank">📅 01:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90937">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇺🇸
🇷🇺
ترامب يوقع قانون العقوبات على روسيا.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/90937" target="_blank">📅 01:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90936">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEXowYV7i2GJvglNhZzMokhUtdHnQ8sNooRr2CoRvhaUktM8USoulPI1o-1FXGY1bIypkxlUe4TtgawzWzSO4xivRy8ejaz05lfBglel2jLwY1nY55zAJGC3jTWAOVjGMwrK4Z7Ev3DBnsvwEooP_QjNoe6qm0_NPghN-PuO_sf8tElWJOWr8UchIJv3A9ndGwUv0cJqG9u0ZNnUUZCwTWrWbD8vgaN3vP9xUkWP8VhcNBGEJzWtoo37mGg6f_5-XCOtnNhHbxhMKgTYzAHWT4SHLM-ZuSy3xNV7rCkKmTltNlNMD9UIIHEC8b-g3RTxYsMVolM0Oki1CunIF5dhxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏
ترامب:
يسعدني أن أعلن أن الولايات المتحدة الأمريكية قد أبرمت اتفاقية مع مملكة الدنمارك وغرينلاند، تمنح الولايات المتحدة سيطرة دائمة على الأمن وجميع الاحتياجات الأخرى في غرينلاند، مما يعالج بشكل كامل جميع مخاوفنا العديدة في الولايات المتحدة.
لن تكون هناك أي تكلفة للولايات المتحدة. بناءً على توجيهاتي، عملنا مع ممثلين عن الدنمارك وغرينلاند لضمان أن الولايات المتحدة ستحظى إلى الأبد بالقدرة الكاملة على فعل ما هو ضروري في غرينلاند من أجل تأمين وحماية أمن غرينلاند والولايات المتحدة الأمريكية.
بالإضافة إلى ذلك، اعتبارًا من الآن فصاعدًا، لا يمكن لأي خصم للولايات المتحدة أن يمتلك أبدًا قاعدة في غرينلاند، أو أن يكون له وجود عسكري في غرينلاند، أو أن يقوم باستثمارات حساسة في غرينلاند، دون موافقتنا الكتابية الصريحة.
هذه "اتفاقية مدى الحياة"، ولا يوجد لها نهاية. نحن فخورون ومسرورون بما حدث للتو، وكل ما تم الاتفاق عليه اليوم سيحظى بتقدير الشعب الأمريكي. سنبدأ على الفور عملية تطوير وجود عسكري كبير في الجزء المناسب من غرينلاند، وهناك العديد من هذه الأجزاء.
سنعمل مع شعب غرينلاند في تطويرها وبنائها. هذا الحل هو حل رائع للولايات المتحدة الأمريكية والدنمارك وغرينلاند وجميع حلفائنا. نتطلع إلى العمل مع الشعب الرائع في الدنمارك وغرينلاند نحو مستقبل عظيم فيما يتعلق بهذه المنطقة الكبيرة والاستراتيجية للغاية.
سنحرص عليها بشدة. هذا حلم يتحقق للولايات المتحدة الأمريكية، وهو حلم مهم وتاريخي وخصوصي. شكرًا لكم على اهتمامكم بهذا الأمر.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/naya_foriraq/90936" target="_blank">📅 00:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90935">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇮🇷
🇺🇸
إعلام أمريكي:  ستة مسؤولين أمريكيين مطلعين على بيانات الخسائر الداخلية، فإن عدد أفراد الخدمة الأمريكية الذين لقوا حتفهم خلال الحرب الإيرانية يفوق ما كشف عنه البنتاغون علنًا.  ‏أفاد خمسة من المسؤولين بمقتل ما لا يقل عن 22 عسكريًا أمريكيًا منذ بدء النزاع…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/90935" target="_blank">📅 00:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90930">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WGipKwnuMD4lx7YmtFYxsTEbYNXvVaBrJTP8sCz3zVymzJ6Y19yE97YVLcetXaFx3SQax3nVenyS4Bp5wTllYNS5v6aMWkXkWfR71J6MoWviseuy1q3U8F2Jb1QhzsdS86ClvVvQu7Kkj7kGL6nT5VQUz-IQeZxiJFJy-1_NqQVYL-vcuvE9Jx7NnlYHb7mETgxmoxp5jeplNOeryOVx0jsl8esSkVLf7brze2Ipcn088KXWMqJrT4Z5PMDW3m6ywI5CbXyCR1Yb-jq1bxYgAkl4bAul6nw2dOnnP0HfFnItGUq0byAmvcEmx0hBnOZnjpd8wfDBtllOXux1E3gU9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GaWpWwUB3iZZx2T_UtGjJN0XcJ9ndkCOp-YHZmDWxISr3BqbStZhxATgY1udy-NCsm7jTNYj9bihQK6frmFoSjKI_Fcwn6X1jkKrwzzddNFcjGjVB1QFIzNSNEUoaVeVVfnGqMtf-Jh0aRvSfpjkgXKiz39hQ0hE7yX7jV1JJVTkBVbpIhy9QifwO5tIYKC0DSnsO_EAr0ck_vU7K8ynx7NKo27W_BuGK9iAkZ_vDsimapwHmAvu39g-1BCmFzTMF1T7fD3QQ7zhwINUZ_Jr8Mcgk_r2C3e5k_HQdN7BfEwsYLTvSazKqcS6sKk5EkezAs7CjC5jSGI71rMlc9Yjhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XR3cTaFbd9ibROltqBGwIi3J4BE81d65R6GfrgQzs2bgQedWL0a6nmYYSeGzCSAULzoI8L7SiXHj461RpFbxgGq10O_cpr__FpJMguFREWJKspcSPEkHol83HZbMfd7EXHoxJs2kfDkuDNBBuNIa4F3XSjAgrQUY2zXKZLrDlUD4yEzYv_od0kiLObyiNloNDr8M9rF_oGLOks4piiJb6E1YLBu0zIKyhULwvihhSMS2EEwvRDb__y3Y27HOJWtlMFboCcPBhycaterjHdYmesU7KB5eR_DCRixxEBWZ20ocHWbfG6WlxRcrkZD0NRQvLfc-E39ANpbxWdx7qEU94A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YZub5PC6UoLWiPTpKel8GdZNoXGKnK1DoxTxUPiTUmMvEbE7sUlVhoqI3UjrPScO_UAMjDDP7Q5D1FaemVvOUbUD5TF8-B1suBSIcmXAwPsYoxqKIUCPLkNqaqEz7rUS_rl5zfzqJ1Z2OLeXM6F9gTWONuLIiZqYM5uV2nXw0zsk0apr9_amjedKHRR-xT1Mpi-g2yfm9-Taj1xpG-O9hDbImur3nKKS0ja0JCE-Y5VckSKQp1tf3hh1kY_FevMBrrnH8cKc0X_J8c44IT10waN5wGzvlsolFQaJ7Kem2fZDP-ONfw0-Ro3QB91TUtJoGgG6uB9iqI-x5sqSQSXbbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/etCGR8DYnPnQyzdAzY4Af63vtx8Nn3XWpwfvtWI6z7OHJinkR5vHJYFsuUX8Y4iJMIDwUHMuU8YaY2dU-QOQA8A_urVvFoQb3H_6tXZzRqsr5TZovwkXtfkM3O0JXJELL4S83aWUnRbLjVSiY8wY92cxZwq72Ee49IJIqEQBmv-p-4-Pg2wm1WrpH0_734lN-FGIaslPBQvf17WJd0EaDz6XbQk3jW8YNWBn27g7UeEd57srLzI4mY0BhjVL1c9ZKQiT-7oa67Giv4nh1nLhA_tTWIrdDb5TV9Vcb3pFOJW9z0HDPjrj3QAgoCHMPL26ekfFx_JDffnanpIqOM-dCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
🇺🇸
مشاهد جديدة تظهر الدمار الكبير في إحدى القواعد الأمريكية بالكويت جراء الهجمات الصاروخية والطيران المسير الإنتحاري الإيراني.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/90930" target="_blank">📅 00:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90929">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">السعودية تفعل منظومة لا تصور " تكفة ، امسح الفديو بسرعة " بعد فشل منظومات الباترويت التي تديرها اليونان و إيطاليا داخل السعودية</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/90929" target="_blank">📅 00:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90928">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇷
🇺🇸
إعلام أمريكي:
ستة مسؤولين أمريكيين مطلعين على بيانات الخسائر الداخلية، فإن عدد أفراد الخدمة الأمريكية الذين لقوا حتفهم خلال الحرب الإيرانية يفوق ما كشف عنه البنتاغون علنًا.
‏أفاد خمسة من المسؤولين بمقتل ما لا يقل عن 22 عسكريًا أمريكيًا منذ بدء النزاع في 28 فبراير/شباط، أي بزيادة أربعة قتلى عن العدد المسجل حاليًا في قاعدة بيانات الخسائر العامة التابعة لوزارة الدفاع الأمريكية (البنتاغون). وقال مسؤول آخر إن العدد الفعلي قد يصل إلى 23 قتيلاً. كما لقي ثلاثة متعاقدين عسكريين أمريكيين في المنطقة حتفهم.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/90928" target="_blank">📅 00:12 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90927">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مصدر من الحكومة اليمنية لنايا
رصدنا عمليات هروب جماعي لمرتزقة العدوان السعودي في جبل حبشي بمدينة تعز .</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/90927" target="_blank">📅 00:01 · 28 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/ClMgDAwcwIDs63KMp_3H8KfFmE7yoLtxxWy_04Z-o-i7lc77JT_-cKdLm5BK9fz1s7Q9XIm-rcXzs5tWVOQSBPYuw4gGgTkrZzgB1DApQL1aB4mfoQWYWkKuNxlVymBS-BcljUsldLrBQShGnaq03KYnUoy8HzJjTaOxZ3flRhOsdsN_o5yayyOnkwEaBCDNDgeq7XMcuVBArDeILqoFI3Zsghs__SND9oKInhfa5ZDjrSDEOmNEyY9XGqIwN3Lhu-1YeQkJEfSHSz13oeGyeBeNPISYWdX8rIEo-dT2x6buBALNjLyoSeHAl9ZPdWTukVIh8MOdQ4wK1biUFsiTvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 274K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 05:11:23</div>
<hr>

<div class="tg-post" id="msg-86311">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l031nLDHOvd79HiAppHn4DU9vQIHQq5VfHqjXPrcN_YyG9FHc8fsmEqOH3hdE7gyw_b2xyVzlkqVdDxxiyhdsHHWFudBi5IzT4ZdAKp5UMLJ1c_lNYccyElWEJ-8eYDw9VmQv7dlSZSiZshP5ssQdl4pDSDRjWTBplehPoGvGQC9R6eJZsl5tEaTkEQDw4IG_TXxxbr-9gny5W93xp3k0sQgm2Xmimu5HiEHigu-oZXzWbQPrdlXVdK4Y4Fs76-TWOQISsLjTCLTFtAMTJ_PqnPH4_-oki4t4n73NMhvKzlKAS2lEARqmf5U-I3jNew1nymkkV7iQrOY-j4w7Yt5uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات في مدينة الاهواز جنوبي إيران</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/naya_foriraq/86311" target="_blank">📅 05:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86310">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e286db0489.mp4?token=upJjjfVXijuuhCtYC8a-h06ExdskmEk8KcBhdEEDUTilkKL7QAyU9jEa_WzA7TdYYywNwekSLYau0ieCgZvGsTr-Vm4FjMfPyO3qzYqrMopknGIx6WWo0gnuUPXPmKbLO8A8LLk-PJOyFanZ_J8sIgABpmXMA8loDqYnZ26IEJBovTFfAELL3cxvhHH7gn4dahjXzNqARHIPgaoFk2F2wiE0irf9U-fIuP57S97eQoCS4RiEvusHnArvjecWdRKH2VoNgzd8YQZP3jh6vtAOLw3SlQvCYoWGXdsUHKdMEH2CUYkMJ-d6BCSbel2u28ISts3kh8pG_l10kHG_jITqqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e286db0489.mp4?token=upJjjfVXijuuhCtYC8a-h06ExdskmEk8KcBhdEEDUTilkKL7QAyU9jEa_WzA7TdYYywNwekSLYau0ieCgZvGsTr-Vm4FjMfPyO3qzYqrMopknGIx6WWo0gnuUPXPmKbLO8A8LLk-PJOyFanZ_J8sIgABpmXMA8loDqYnZ26IEJBovTFfAELL3cxvhHH7gn4dahjXzNqARHIPgaoFk2F2wiE0irf9U-fIuP57S97eQoCS4RiEvusHnArvjecWdRKH2VoNgzd8YQZP3jh6vtAOLw3SlQvCYoWGXdsUHKdMEH2CUYkMJ-d6BCSbel2u28ISts3kh8pG_l10kHG_jITqqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمليات البحث عن عالقين تحت الانقاض في جزيرة قشم عقب عدوان أمريكي على منطقة سكنية.</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/naya_foriraq/86310" target="_blank">📅 05:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86309">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5fb69b02b.mp4?token=E-s09R7zKU2hWKKlNtl99rE5ygoYWHLMBdYGEjCsfH3U8_K-Jvmv98fWAGpOocjeIAsxFETIK35dDxK0m9xplQjsuE9r1f6iMApM5SnJEFMiEQ9qt-UVns6t9mKz9R8B6EYiY-e0qjlBgftzMizWmK0LSyM07xe8Ike92vQMpY7KxCHcJScmoe2ribluShru0gZ0BOOpvrTFZ-gnHFRtC4I5YneVws9ntTtrgT6BGFjxiTstYMwrfeMPmqQ3pOmSENun2Otfl0R2mlWciUZrh4VoZWD1-G2oTuhr1nibm5pr0C6IQJiDdfD7OG51X162SOQBtVjtVVjssyrprfKqHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5fb69b02b.mp4?token=E-s09R7zKU2hWKKlNtl99rE5ygoYWHLMBdYGEjCsfH3U8_K-Jvmv98fWAGpOocjeIAsxFETIK35dDxK0m9xplQjsuE9r1f6iMApM5SnJEFMiEQ9qt-UVns6t9mKz9R8B6EYiY-e0qjlBgftzMizWmK0LSyM07xe8Ike92vQMpY7KxCHcJScmoe2ribluShru0gZ0BOOpvrTFZ-gnHFRtC4I5YneVws9ntTtrgT6BGFjxiTstYMwrfeMPmqQ3pOmSENun2Otfl0R2mlWciUZrh4VoZWD1-G2oTuhr1nibm5pr0C6IQJiDdfD7OG51X162SOQBtVjtVVjssyrprfKqHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تعرض منطقة سكنية في قشم الى عدوان أمريكي غاشم.</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/naya_foriraq/86309" target="_blank">📅 04:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86308">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تصاویری دیگر از حمله موشکی کویت به شهر آبادان در استان خوزستان ایران.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/naya_foriraq/86308" target="_blank">📅 04:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86307">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb907f6861.mp4?token=toZzNDGwUlG9gnYIL6-NYgDUTKWzezypgpWQKNhvxgri8c-0ixNe31j7NPndKUN-EirLIQj6gCbdh6zic2l7UtqZqfDbMj06984pUpcPZOQG1ksbJ9oVf6aAq9cc1ENOPODGmPVYOkJuLfAh75wurTLsAzxBW01zylElKzzIeWKe2IY5xDxSSQ-vvKKqgaN-rimhaQ2lyz0q1gyIsadBgYcdR9EgYWYAmFf7deQr-jLQxo27YnzO01cLPC9MKS2ZsizSuuaCzQvnjRwdCxjb1_4ZGTFF5ZHP6ulMjhq8Cx5l-mkLeRQPbgQ7BfHkH6RwbsFHAuJX6GZQVUvtPSs9Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb907f6861.mp4?token=toZzNDGwUlG9gnYIL6-NYgDUTKWzezypgpWQKNhvxgri8c-0ixNe31j7NPndKUN-EirLIQj6gCbdh6zic2l7UtqZqfDbMj06984pUpcPZOQG1ksbJ9oVf6aAq9cc1ENOPODGmPVYOkJuLfAh75wurTLsAzxBW01zylElKzzIeWKe2IY5xDxSSQ-vvKKqgaN-rimhaQ2lyz0q1gyIsadBgYcdR9EgYWYAmFf7deQr-jLQxo27YnzO01cLPC9MKS2ZsizSuuaCzQvnjRwdCxjb1_4ZGTFF5ZHP6ulMjhq8Cx5l-mkLeRQPbgQ7BfHkH6RwbsFHAuJX6GZQVUvtPSs9Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران حربي أمريكي في سماء البحرين.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/naya_foriraq/86307" target="_blank">📅 04:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86306">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">انفجارات في مدينة الاهواز جنوبي إيران</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/naya_foriraq/86306" target="_blank">📅 04:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86305">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92e5b35879.mp4?token=VwAcTlGBIiZfatSmMPvKaUouDpF8WE-oRgBLWAnEwMdGtk74z00ObvxriSQzrgOh3yKpiHZom-14wxaIcNzEjiuqlWfw_FYY5LerwjHzbVQCN6qvGPusRKKcf1NkGza-qyKd_09GYVIanwYcP4IcREHN2dVRW7TcPUaQlGENEdL18vP5L3p3TmMLkxGF5odSUK_8JAcsJuw57sYR1Wf-VDJ3jL9taFE-GaJ0f7r0zKDZXOkBJi6RsClBcD0YpOadbIEyWLzJWl6-x-Qj7CQNSvV7FuFZuCveUkz075ku83Kua2AAcUQOeQFUDVmimGeqPS4T4R22PZk-6FVcTNzAQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92e5b35879.mp4?token=VwAcTlGBIiZfatSmMPvKaUouDpF8WE-oRgBLWAnEwMdGtk74z00ObvxriSQzrgOh3yKpiHZom-14wxaIcNzEjiuqlWfw_FYY5LerwjHzbVQCN6qvGPusRKKcf1NkGza-qyKd_09GYVIanwYcP4IcREHN2dVRW7TcPUaQlGENEdL18vP5L3p3TmMLkxGF5odSUK_8JAcsJuw57sYR1Wf-VDJ3jL9taFE-GaJ0f7r0zKDZXOkBJi6RsClBcD0YpOadbIEyWLzJWl6-x-Qj7CQNSvV7FuFZuCveUkz075ku83Kua2AAcUQOeQFUDVmimGeqPS4T4R22PZk-6FVcTNzAQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادامه حملات موشكی از کویت به آبادان</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/naya_foriraq/86305" target="_blank">📅 04:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86304">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇺🇸
مسؤول أميركي:
الهجمات على إيران مستمرة وتستهدف مجموعة واسعة جدا من الأهداف.</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/naya_foriraq/86304" target="_blank">📅 04:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86303">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇺🇸
🇮🇷
عدوان أمريكي على محيط مدينة شادكان جنوبي إيران.</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/naya_foriraq/86303" target="_blank">📅 04:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86302">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad77c0e383.mp4?token=WlmvJuDRR2KHoLke0uSf7B0WmU_QcXiQS9q3Em8G-1Yz0u2QzMUGLjwr_TjROeMNoY6U-aXbZkDwZW9QMD5gbf3hZI0BO4Yhj5ByA65LP7QWJMKdWJ-Vh6cz29REiW672lPCQ73KYwhzUiISApvkmHUPRFWwLL1-qgquQBjFe6ImWxQU1nzMrkt_WewnPuMrthBelSpxwtphHsheofRUVZhiJYu1wUJDvnyG08uA0WHLj0FpREBUKnzeHS6ONBHxQzwQPMTHRQgIycQ1mz5n96D-cnIs-4PmN0O4mGFkF_a43heAn4J6gQRmuFprPxNr39CxaaKiamZdxXiCtd0ycw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad77c0e383.mp4?token=WlmvJuDRR2KHoLke0uSf7B0WmU_QcXiQS9q3Em8G-1Yz0u2QzMUGLjwr_TjROeMNoY6U-aXbZkDwZW9QMD5gbf3hZI0BO4Yhj5ByA65LP7QWJMKdWJ-Vh6cz29REiW672lPCQ73KYwhzUiISApvkmHUPRFWwLL1-qgquQBjFe6ImWxQU1nzMrkt_WewnPuMrthBelSpxwtphHsheofRUVZhiJYu1wUJDvnyG08uA0WHLj0FpREBUKnzeHS6ONBHxQzwQPMTHRQgIycQ1mz5n96D-cnIs-4PmN0O4mGFkF_a43heAn4J6gQRmuFprPxNr39CxaaKiamZdxXiCtd0ycw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تعرض منطقة سكنية في قشم الى عدوان أمريكي غاشم.</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/naya_foriraq/86302" target="_blank">📅 04:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86301">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">انفجارات في جزيرة قشم ومدينة بندرعباس مجدداً</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/naya_foriraq/86301" target="_blank">📅 04:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86300">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">عدوان أمريكي غاشم على مدينة كازرون بمحافظة فارس الإيرانية.</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/naya_foriraq/86300" target="_blank">📅 04:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86298">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ادامه حملات موشكی از کویت به آبادان</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/naya_foriraq/86298" target="_blank">📅 04:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86297">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">نائب محافظ خوزستان: مناطق في محيط مدينة آبادان تعرضت لهجوم صاروخي من قبل العدو الإرهابي الأمريكي.</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/naya_foriraq/86297" target="_blank">📅 04:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86296">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">الانفجارات مجدداً في آبادان</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/naya_foriraq/86296" target="_blank">📅 04:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86295">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">مجددا صواريخ من الكويت تنطلق نحو الاراضي الإيرانية</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/naya_foriraq/86295" target="_blank">📅 04:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86294">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مجددا صواريخ من الكويت تنطلق نحو الاراضي الإيرانية</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/naya_foriraq/86294" target="_blank">📅 04:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86293">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7f237080a.mp4?token=A3nwWtKMiaKxU-cmlGVAjCP-bhA35qlmwQ5J9peatj6dMrW1O6ohvu6k1Fm4QFiSmUDVwGIs9KlcibCR67085vWn0WSRFB2mZywq1u8rCIWXO7AbSbK4wNNVhW4N9rTswvbV0B5K6IGTey-gh6_Du89frveN4JtOf7KxcEOlkcyw3iKh2y6Agzg6QP2Dl8xw8-rl3hBFNCI3eMm8Go3toZS6ABmyIgmlmg2q4GpLVkpxwR_5cQ2bVQsmbSc8BPQn-W50hWFJaFCSVw7dByDewC8722IPbfwhNhHZM4AcqocFxUmsFr4H16ycFShS_EgGOMh_H0EkOOatjK-H_2omfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7f237080a.mp4?token=A3nwWtKMiaKxU-cmlGVAjCP-bhA35qlmwQ5J9peatj6dMrW1O6ohvu6k1Fm4QFiSmUDVwGIs9KlcibCR67085vWn0WSRFB2mZywq1u8rCIWXO7AbSbK4wNNVhW4N9rTswvbV0B5K6IGTey-gh6_Du89frveN4JtOf7KxcEOlkcyw3iKh2y6Agzg6QP2Dl8xw8-rl3hBFNCI3eMm8Go3toZS6ABmyIgmlmg2q4GpLVkpxwR_5cQ2bVQsmbSc8BPQn-W50hWFJaFCSVw7dByDewC8722IPbfwhNhHZM4AcqocFxUmsFr4H16ycFShS_EgGOMh_H0EkOOatjK-H_2omfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موجة صاروخية جديدة أطلقت من الكويت نحو مدينة آبادان جنوبي إيران.</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/naya_foriraq/86293" target="_blank">📅 04:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86292">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69adeaa37e.mp4?token=bxqLgOHSCdWHC_-2ZW76uLcu5u373nrEtTNMNqyUzpEVuUZMZhHZZygWHDexyK90zB_Z7XD8jHzsKhhuQzFrUHQHaNUYQWnE2fS7LrsV_PTzFWY9NzR_GtMKI7qzyksXna73D9X-SpgGJKEcCp-j8dy1APOHgufGAL4DrLRf0g57mxB8rJVS2kZhEFNAKkeXPe9lR-HuIUCPNDX8tnhUxdfBb8-ZTOxMKpbW5DktAF8SCIT0xa86GcjRekjOpbkiUPHOM1sXB5Ep2xZj1PUpjBljH1FducjaeB6XFQHxswcVhTN3DDXae3KHk8SYgbiBELoFc6Z9OSPzsBOKsHWNOaeFlX4-W5lediYH829RO-CN5h4-4KMtXG_LHduiixBH8yufKQHKv2AhMYE5jlLk5zYFcZiIeMFKIxdN_EhHEQXaNVrbbCGMgRyZYNa4SKl2fL6UtdTECW1xIri6KXywollbVXyM4QBsU-5t-zH2uDtmLbHXRwWp1nFBrZHOKixwFVg0GwnLPPrmychb9mQ8FFTEGt7im2HJhnsADn7GwmKn0Xj_kpaNu4Ol2wO4rH3NSMqYcZkkrmDJh6n9w6n94_Uznww2YHOaE7eBqdtiSp9Gce1QciSGEFE7cIR-s49GK4Inui5vONYw8isP-xVangVAkc9B9u6ibtJFOgmWmnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69adeaa37e.mp4?token=bxqLgOHSCdWHC_-2ZW76uLcu5u373nrEtTNMNqyUzpEVuUZMZhHZZygWHDexyK90zB_Z7XD8jHzsKhhuQzFrUHQHaNUYQWnE2fS7LrsV_PTzFWY9NzR_GtMKI7qzyksXna73D9X-SpgGJKEcCp-j8dy1APOHgufGAL4DrLRf0g57mxB8rJVS2kZhEFNAKkeXPe9lR-HuIUCPNDX8tnhUxdfBb8-ZTOxMKpbW5DktAF8SCIT0xa86GcjRekjOpbkiUPHOM1sXB5Ep2xZj1PUpjBljH1FducjaeB6XFQHxswcVhTN3DDXae3KHk8SYgbiBELoFc6Z9OSPzsBOKsHWNOaeFlX4-W5lediYH829RO-CN5h4-4KMtXG_LHduiixBH8yufKQHKv2AhMYE5jlLk5zYFcZiIeMFKIxdN_EhHEQXaNVrbbCGMgRyZYNa4SKl2fL6UtdTECW1xIri6KXywollbVXyM4QBsU-5t-zH2uDtmLbHXRwWp1nFBrZHOKixwFVg0GwnLPPrmychb9mQ8FFTEGt7im2HJhnsADn7GwmKn0Xj_kpaNu4Ol2wO4rH3NSMqYcZkkrmDJh6n9w6n94_Uznww2YHOaE7eBqdtiSp9Gce1QciSGEFE7cIR-s49GK4Inui5vONYw8isP-xVangVAkc9B9u6ibtJFOgmWmnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صواريخ جديدة من الكويت تنطلق نحو أراضي الجمهورية الإسلامية الإيرانية</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/naya_foriraq/86292" target="_blank">📅 04:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86291">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">صواريخ جديدة من الكويت تنطلق نحو أراضي الجمهورية الإسلامية الإيرانية</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/naya_foriraq/86291" target="_blank">📅 04:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86290">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">صواريخ جديدة من الكويت تنطلق نحو أراضي الجمهورية الإسلامية الإيرانية</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/naya_foriraq/86290" target="_blank">📅 04:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86289">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇺🇸
🇸🇦
مسؤول أمريكي:
ترامب التقى يوم الأربعاء بوزير الدفاع السعودي الأمير خالد بن سلمان؛ نقل الوزير السعودي إلى ترامب رسالة من ولي -العهد السعودي محمد بن سلمان بشأن الحرب مع إيران والتصعيد الإقليمي.</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/naya_foriraq/86289" target="_blank">📅 04:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86288">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">الله أكبر
إطلاق صواريخ نحو منطقة كيلو 20 مضيق هرمز.</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/naya_foriraq/86288" target="_blank">📅 04:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86286">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0f16e8514.mp4?token=p5KvRQrOWm6rDE4cDOGYXTWLqcAwU7dMrrsQXFsDw3S-Dya4g6BxCX15sdNU5iV5EIzkcqjbb9MkLHFAmLERnLtxBvwQpjaM7GsHPwAJFnfb5-aUJtUZSXtEJdxuL7yYE62VfyzBoPjX3BV3ExpRBVzLh3dFaqYccD6Abqa-aJ970UYkEBJN4oRXBrXv8kBep1VLVraxXPRSp9QLxj4GErU7mXucu1AfpV0RYTJ8-4-sv2Thn6vTa0koqQE9Nk6ltWGix8LCUGmYBPlHJQeFB72zB46tu6h23iQRZc4NJssOgENLufW1s401rSfdVQ0KplxTq5aQ-Ft_K87I0xvuJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0f16e8514.mp4?token=p5KvRQrOWm6rDE4cDOGYXTWLqcAwU7dMrrsQXFsDw3S-Dya4g6BxCX15sdNU5iV5EIzkcqjbb9MkLHFAmLERnLtxBvwQpjaM7GsHPwAJFnfb5-aUJtUZSXtEJdxuL7yYE62VfyzBoPjX3BV3ExpRBVzLh3dFaqYccD6Abqa-aJ970UYkEBJN4oRXBrXv8kBep1VLVraxXPRSp9QLxj4GErU7mXucu1AfpV0RYTJ8-4-sv2Thn6vTa0koqQE9Nk6ltWGix8LCUGmYBPlHJQeFB72zB46tu6h23iQRZc4NJssOgENLufW1s401rSfdVQ0KplxTq5aQ-Ft_K87I0xvuJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مشاهد حصرية لنايا
🇰🇼
🇮🇷
موجة صاروخية كبيرة أطلقت من الجانب الكويتي تجاه مدينة آبادان الإيرانية.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/86286" target="_blank">📅 04:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86285">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇺🇸
الجيش الامريكي:
‏بدأت القوات الأمريكية شن ضربات ضد إيران في الساعة الثامنة مساءً بتوقيت شرق الولايات المتحدة اليوم، رداً على محاولات إيران شن هجمات أمس على القوات الأمريكية في الشرق الأوسط.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/86285" target="_blank">📅 03:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86284">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44b08911d5.mp4?token=OYN22ZhNxOamuzdiHbBK_emCP2pKNc9n5PNyHALWixOE_VRXhVGqU2Rzoh6IJwyFh6gu5t4WgXwklsa5SEEp1qbWN_eYbT2BYYEYF8H5_NT0hhh587AEgaKUbsJXK5sN9xuNfVnvDj5BWJ3BMKdYjMy3UdN_e3GN5DeCxbxoJFyMol2rXGfGLrFtpWl9sII_RsQUUVA0elIBU7x6mJAHMQg2rV0jnyu00jeBMCnxsSD1PQ7gQmf8HryMhgDEEFSzDiznMSvHZgeGJXVZUN0qLThWYv6mCEx10aS-NP0l_2G7Ak4iA9lbjqinksWE5d_h8gQiMmnm2K8WUSKU-Eyjkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44b08911d5.mp4?token=OYN22ZhNxOamuzdiHbBK_emCP2pKNc9n5PNyHALWixOE_VRXhVGqU2Rzoh6IJwyFh6gu5t4WgXwklsa5SEEp1qbWN_eYbT2BYYEYF8H5_NT0hhh587AEgaKUbsJXK5sN9xuNfVnvDj5BWJ3BMKdYjMy3UdN_e3GN5DeCxbxoJFyMol2rXGfGLrFtpWl9sII_RsQUUVA0elIBU7x6mJAHMQg2rV0jnyu00jeBMCnxsSD1PQ7gQmf8HryMhgDEEFSzDiznMSvHZgeGJXVZUN0qLThWYv6mCEx10aS-NP0l_2G7Ak4iA9lbjqinksWE5d_h8gQiMmnm2K8WUSKU-Eyjkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از شلیک چندین موشک از کویت به سمت ایران.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/86284" target="_blank">📅 03:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86283">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70000377da.mp4?token=oeldmQqRHM5Q-WTF8xkN-h-sdM8wwD7uG7Eib-FKbHCwU6XZbADCvLypOFOhqyCrHipBucQQo_mGPClfteH-CwNIOtNPvcQzHpUEpdZouqM3p4CVCiZOxzumT_H74zviGoUcAOd4VlvtS6vMP9Ix1sE5kyjj2ZXqLM1VX4zBRJOWwSUaddB_uTL2FVsF7Krn04r4sxsQ8GwnbypULRdRVcf4xSkCfgrYlbc0F2UcP8_TSmVQD854yP81tmO4fxPHmXVwsmGzJcqGcihMMAZxZ_AhvXVmIfpXZoxyaxo2QxksFUp7PBp27R1lqYtYIui1y6Vbt7UKPq6TMA8nMZmxvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70000377da.mp4?token=oeldmQqRHM5Q-WTF8xkN-h-sdM8wwD7uG7Eib-FKbHCwU6XZbADCvLypOFOhqyCrHipBucQQo_mGPClfteH-CwNIOtNPvcQzHpUEpdZouqM3p4CVCiZOxzumT_H74zviGoUcAOd4VlvtS6vMP9Ix1sE5kyjj2ZXqLM1VX4zBRJOWwSUaddB_uTL2FVsF7Krn04r4sxsQ8GwnbypULRdRVcf4xSkCfgrYlbc0F2UcP8_TSmVQD854yP81tmO4fxPHmXVwsmGzJcqGcihMMAZxZ_AhvXVmIfpXZoxyaxo2QxksFUp7PBp27R1lqYtYIui1y6Vbt7UKPq6TMA8nMZmxvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد تظهر لحظة إطلاق الصواريخ من الكويت تجاه الجمهورية الإسلامية الإيرانية.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/86283" target="_blank">📅 03:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86282">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09e2d8b313.mp4?token=o1AlTRTVs_XvP_KsJjQZrfHvGKExXadphEY8AF8JwFqaPA_GpFZ2KgXCCU9IbapDtvS-8Xk1FKnBEzwkpo69RO-PkkyOVr3PAbuZSDeWfNy3HkJV5QjOMKYZIRpcc9ELG0OvYTNN53Du-2qOLsJ7So_5bBgqtxiE6Cf38uX4YstODHfWSy79V6D4dyY30KHa1M1mZcAC8wR2o7x7YLJB8U3joSSZXDGKL9_2FTjRav5_l99-ujwK2GwOX_W2FE7s_LZmn29UiaEZsZWv4UnE7_S84tqWhjmUFXRUwkk9BVt-czjgXK5DpUJbf7yhyExjQrykiQzRYoej1Q-Q4yngoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09e2d8b313.mp4?token=o1AlTRTVs_XvP_KsJjQZrfHvGKExXadphEY8AF8JwFqaPA_GpFZ2KgXCCU9IbapDtvS-8Xk1FKnBEzwkpo69RO-PkkyOVr3PAbuZSDeWfNy3HkJV5QjOMKYZIRpcc9ELG0OvYTNN53Du-2qOLsJ7So_5bBgqtxiE6Cf38uX4YstODHfWSy79V6D4dyY30KHa1M1mZcAC8wR2o7x7YLJB8U3joSSZXDGKL9_2FTjRav5_l99-ujwK2GwOX_W2FE7s_LZmn29UiaEZsZWv4UnE7_S84tqWhjmUFXRUwkk9BVt-czjgXK5DpUJbf7yhyExjQrykiQzRYoej1Q-Q4yngoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اطلاق صواريخ من الكويت</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/86282" target="_blank">📅 03:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86281">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">عدوان أمريكي على بوشهر وبرازجان وبندرعباس وقشم جنوبي إيران</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/86281" target="_blank">📅 03:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86280">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">عدوان يستهدف مدينة آبادان جنوبي إيران</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/86280" target="_blank">📅 03:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86279">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">انفجارات في جزيرة كيش جنوبي إيران</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/86279" target="_blank">📅 03:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86278">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اطلاق صواريخ من الكويت</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/86278" target="_blank">📅 03:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86277">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اطلاق صواريخ من الكويت</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/86277" target="_blank">📅 03:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86276">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6ff8e3964.mp4?token=qgqiQANAplImRqupy1F4IeODFeG2AnhMk15v4A-2oRGbLDallbAOrnsmLaulXtPDM6D-8Y6G9t96WOCq-7o6gcInRM-0Qtyz7AuO9WO6zQOao35NlXanii6trbBToAd71L14eGu3VUaRAjSeI9AZjDTSnfrKqCyAle6NgSvTZ92PJoJbv2sdJw-mDkfxzPwLH_hjpJI7A5GHL7lf1XnUCvUczE9h3q7zPd7sgzEOSWIN_n6VigoeT1k51BEYwgG1mJbDKIp792oEDAsdsj3nnaXz91XYUxVNBO8LF4ezYue1jseDU5zfJ0tIzseLNlCvxhdTc9t5j1O0do4f0DM6eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6ff8e3964.mp4?token=qgqiQANAplImRqupy1F4IeODFeG2AnhMk15v4A-2oRGbLDallbAOrnsmLaulXtPDM6D-8Y6G9t96WOCq-7o6gcInRM-0Qtyz7AuO9WO6zQOao35NlXanii6trbBToAd71L14eGu3VUaRAjSeI9AZjDTSnfrKqCyAle6NgSvTZ92PJoJbv2sdJw-mDkfxzPwLH_hjpJI7A5GHL7lf1XnUCvUczE9h3q7zPd7sgzEOSWIN_n6VigoeT1k51BEYwgG1mJbDKIp792oEDAsdsj3nnaXz91XYUxVNBO8LF4ezYue1jseDU5zfJ0tIzseLNlCvxhdTc9t5j1O0do4f0DM6eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
طيران حربي يجوب سماء محافظة ذي قار جنوبي العراق.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/86276" target="_blank">📅 03:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86275">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇸🇦
لازال الطيران المدني يعاني في سماء السعودية.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/86275" target="_blank">📅 03:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86273">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwoau0UJpj1ejDp0WPHrGNOyNGwnyLcJ03-M6TDPx5HgmZyovUf2Act_n8MNlyOd2AnqgCZUwuVzccdD9kE72ry4hn1OAGaYqCYvqNtiGHOeJzRvWZ6jJERv-TWSvRloHIBW-RYtyVgrHbtBuvTuDg_N-ffHnUnuzmxq-MW-BDpeQbr26_Duy3G_gchlsJYhSJ36yfUVKsMnpTKy9OnYD5lMpKr2XF9H7_bRe9il9BdHXs1523UYAXFGc4R7TB5_UpjxDRp_tD4pG0t4utNj545HWkmkX-Fgsgdrb__KhfaV0uRgw8NGaugTSY8Ym4yZPYIfhNO0l4NYuhsPR9o03A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الطيران المدني يتجنب الدخول في أجواء الرياض.  ثلاثة طائرات قادمة من نيودلهي ؛ جدة وتركيا لا تستطيع الهبوط في مطار الرياض</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/86273" target="_blank">📅 03:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86272">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">إنفجارات في مدينة نورآباد بمحافظة فارس الإيرانية.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/86272" target="_blank">📅 02:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86271">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6f9d903b2.mp4?token=Dzs9YKOCMRAQRTwIH3D6CvHVbtK6MkeylgrgcUn5u6wlpm5VMlYLO_XDNoNNyvfeSjYWFOPhyc2gYBan99ic8UD-Cd5waFJs9g5rd4WBw_olTz4HQOEbbZ4HskKuA3400CRUgXW-N1XcdVjk7eyu397bbksETY7sDRzpAketED9C7ZgHoWhQi-igVDjeXXBeL1ZLn_UXE5GY6lFe9GlK--oPMmUjOKHQkwC8OMSxNfEGx-2-6ms6k83HtPvQjIJ8IOY23jWDe2ZeMRb0zOdKu0Q2UB6kolj0m0mH1S5oElndica5XCX4swPjMaCU7sUnBpgxdI_MnAqOZoHOKjZIdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6f9d903b2.mp4?token=Dzs9YKOCMRAQRTwIH3D6CvHVbtK6MkeylgrgcUn5u6wlpm5VMlYLO_XDNoNNyvfeSjYWFOPhyc2gYBan99ic8UD-Cd5waFJs9g5rd4WBw_olTz4HQOEbbZ4HskKuA3400CRUgXW-N1XcdVjk7eyu397bbksETY7sDRzpAketED9C7ZgHoWhQi-igVDjeXXBeL1ZLn_UXE5GY6lFe9GlK--oPMmUjOKHQkwC8OMSxNfEGx-2-6ms6k83HtPvQjIJ8IOY23jWDe2ZeMRb0zOdKu0Q2UB6kolj0m0mH1S5oElndica5XCX4swPjMaCU7sUnBpgxdI_MnAqOZoHOKjZIdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇺🇦
ضربات صاروخية روسية مستمرة تطال العاصمة كييف ومدن أوكرانية أخرى.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/86271" target="_blank">📅 02:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86270">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">إنفجارات في مدينة نورآباد بمحافظة فارس الإيرانية.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/86270" target="_blank">📅 02:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86269">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">الطيران المدني يتجنب الدخول في أجواء الرياض.  ثلاثة طائرات قادمة من نيودلهي ؛ جدة وتركيا لا تستطيع الهبوط في مطار الرياض</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/86269" target="_blank">📅 02:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86267">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5f91bebb6.mp4?token=g1G1kPZS_R9dSLWaLRTX9IU7HgvSzYJ7J3-jXp8aqNBE-KRJsNORdUjRXryui_TkMj9SMlvHxnOczy1ZXgHaWZTXGSFnK6Lpr0bTtwCnLCAgAaxqTuDrT7NPN1tFHwgSiMyFquM7ZpsnE-B-Epc7DCr0TcohhHxIhNMxveQGFZpc2UOE5iJaNzENQEvqi20_wXHE3L49N3B-3mK1glqnme_vU3zjsBoBCapAu5ChnsRMaAcopysdLYUg2F4yBsNHdZ9toZR612_PuG9HYyNr7WKIawwaeJkKbN37GMoDajMv3yEBgQXjmFVi4-S1Uk7T7p0oi-LyW2DlE0e-vqDVoDf16MDOjAYgMaFACdEKFc0n32f58FaSFBBoxLilPxEFvBo1MEokckx-6fIY4zdKzxgPQKQci8kLy-K7-xIxEFjCTPCafW9hmvAWHrthZCat0KV4tgDQyTA-cPqHh-BCYXLhUNmr131KfUzBl3lfAiPZEce45T-SSBIiGSh8lJ7t9N5186O4TGq6igNe4zAHM11aGQI2IFjytoMxV5txY9szM5GkclwSXDufHdBhO_g8kdmJNE62bikDoaAK0CCStuyojJDXxJK1F4eLzsxT0oixOpdsmWCc1RqzQ604QihgOWkxNTYQyoTgEFzNCAbbuJgyMO81U-mb9OSVKYMyVMU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5f91bebb6.mp4?token=g1G1kPZS_R9dSLWaLRTX9IU7HgvSzYJ7J3-jXp8aqNBE-KRJsNORdUjRXryui_TkMj9SMlvHxnOczy1ZXgHaWZTXGSFnK6Lpr0bTtwCnLCAgAaxqTuDrT7NPN1tFHwgSiMyFquM7ZpsnE-B-Epc7DCr0TcohhHxIhNMxveQGFZpc2UOE5iJaNzENQEvqi20_wXHE3L49N3B-3mK1glqnme_vU3zjsBoBCapAu5ChnsRMaAcopysdLYUg2F4yBsNHdZ9toZR612_PuG9HYyNr7WKIawwaeJkKbN37GMoDajMv3yEBgQXjmFVi4-S1Uk7T7p0oi-LyW2DlE0e-vqDVoDf16MDOjAYgMaFACdEKFc0n32f58FaSFBBoxLilPxEFvBo1MEokckx-6fIY4zdKzxgPQKQci8kLy-K7-xIxEFjCTPCafW9hmvAWHrthZCat0KV4tgDQyTA-cPqHh-BCYXLhUNmr131KfUzBl3lfAiPZEce45T-SSBIiGSh8lJ7t9N5186O4TGq6igNe4zAHM11aGQI2IFjytoMxV5txY9szM5GkclwSXDufHdBhO_g8kdmJNE62bikDoaAK0CCStuyojJDXxJK1F4eLzsxT0oixOpdsmWCc1RqzQ604QihgOWkxNTYQyoTgEFzNCAbbuJgyMO81U-mb9OSVKYMyVMU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇺🇦
هجوم صاروخي روسي ودوي انفجارات كبيرة في العاصمة الأوكرانية كييف.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/86267" target="_blank">📅 02:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86266">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇮🇶
حشود من المشيعين تتوافد إلى مدخل محافظة البصرة جنوبي العراق لإستقبال جثمان الشهيد "حيدر منصور السكيني" الذي إرتقى خلال العدوان السعودي الأمريكي.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/86266" target="_blank">📅 02:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86265">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">⭐️
وول ستريت جورنال: ‏
أعدّ الأدميرال براد كوبر، قائد القيادة المركزية الأمريكية، خيارًا لشنّ حملة جوية قاسية ضد إيران قد تستمر لمدة تصل إلى أسبوعين، بهدف شلّ قدراتها الصاروخية، في الوقت الذي يدرس فيه ترامب مدى التصعيد الذي سيتخذه بعد الهجوم الصاروخي الإيراني المفاجئ.
‏يقول مسؤولون إن القوات الإسرائيلية قد تُضمّن إذا عادت الولايات المتحدة إلى عمليات قتالية واسعة النطاق ضد إيران.‏
على الرغم من ادعاء هيغسيث السابق بأن برنامج الصواريخ الإيراني قد "دُمر فعلياً"، قال ترامب في مقابلة إن إيران قد لا تزال تمتلك ما بين 21 و22% من صواريخها؛ بينما يُقدّر بعض المحللين النسبة بأكثر من ذلك.‏
اعتقد الأدميرال براد كوبر، قائد القيادة المركزية الأمريكية، في البداية أن الحرب قد تستغرق ستة أسابيع أو أكثر عند اندلاعها؛ وقد ساهم إسقاط طائرة أمريكية من طراز إف-15إي فوق إيران خلال الحملة الانتخابية في قرار ترامب بالسعي إلى وقف إطلاق النار بعد ذلك بوقت قصير.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/86265" target="_blank">📅 02:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86264">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇷🇺
🇺🇦
‏زيلينسكي: روسيا تستعد منذ أيام لتنفيذ ضربة واسعة وهناك احتمال كبير بأن تنفذ الليلة.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/86264" target="_blank">📅 01:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86263">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇺🇸
مسؤول أمريكي رفيع:
الإدارة لا تسعى إلى استئناف المحادثات مع إيران في الوقت الراهن.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/86263" target="_blank">📅 01:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86262">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">أنباء غير مؤكدة عن دوي انفجار في مدينة تبريز شمال غرب إيران.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/naya_foriraq/86262" target="_blank">📅 01:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86261">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">أنباء غير مؤكدة عن دوي انفجار في مدينة تبريز شمال غرب إيران.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/naya_foriraq/86261" target="_blank">📅 01:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86260">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V76AYy64q_5D8Od248IhcKuigXN6C0u8RBcax-tiI_R3aHardcro5z4X5uNk9blOpoVXDtD8Jur0c2cKZuxHK3oF3cg-k2FMAKZ6p5hrhBYaG7QoC4PmOAYytWZoPCduq58edrTvqXB8EUY_ZaCHKHZ_Jrr-BO2iuDw1rFjC5BZh3nCpbTpY9wDD0bOE64l8rwwfoE2YP6WctGFH1leuf90BjsThXVFUiN4epk5cAKSx56is9crzm7MmcXvBfrIoQm-2oc7BDIGGr2BYb1Ke4b0XVYzHm9ozQTa8wghADz2T9AC1MKh0P49bzerT2IAsoEm8YLSjX-v-_l-E8FE2hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خروج مطار الملك خالد الدولي عن العمل بعد سماع اصوات انفجارات</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/naya_foriraq/86260" target="_blank">📅 01:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86258">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rup51WkmqogsF4t-ZGCJN-d0lXmvXh287d7La8ZVZmtLn2odCdP5dsHm27Qq9CIe9f2IV29NPZAe8jvWX80ve1OqE4-bRwXUkQSnmDs60ze_YuJ_XIl_LYZy26t-t-Mc9HwDpd-lY8ITRWX2GwoVjvcKJOFxYd8udNcjKccOcNN6P0zpsE5cui-ZFHqbSSrlQyoKk7ylR26HAzR-Dy22s82xJfSAj1nK5mweiiiku1002TkJ6Fp_ppcj-vSvpu4w-Zm0gnt-DnYyqyAeEsrgQ4JsiblOklNjaAnnPDKygvhNCZ0e7PA99tbdS34PFkY8H0-6HJgP2h8Lo48x2Eni-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصوات انفجارات مجهولة بمعدل ضربتين سمعت بوضوح في العاصمة السعودية الرياض</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/86258" target="_blank">📅 01:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86257">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اصوات انفجارات مجهولة بمعدل ضربتين سمعت بوضوح في العاصمة السعودية الرياض</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/86257" target="_blank">📅 01:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86256">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اصوات انفجارات مجهولة بمعدل ضربتين سمعت بوضوح في العاصمة السعودية الرياض</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/86256" target="_blank">📅 01:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86255">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f18ec7b09f.mp4?token=OMyNWfqPQMf2EsijYXkONM0ztdmfj0EWZAcB5wDHsUqtmQUsAS9byOUUedUJf6B7mFZOAzwagZ2lL9Zq-gqSbmm_mfCtbg8jPehSzjNuPnfHCggBrGW1wZSREhtX6923avox_8P9GPP_cKLTm8-r5wLQ5SQMKd7WUiHLNQ3TDSYHCitGyOTxUx_u3QSxaesk9RqlHt4w4aQyq_feaFKM63U-yZG8GphrE4f_JAZyp-mV1m-AgMfREFQXsE2sZYOtneRt7UgY_5awnl02iZWEHj7_Premy1Cw1AHz-CRLrGFwJuQOUgB6ZsqEhd9kh5bSOmAb9PERWsSfCorwPNbJbGJkK1zDrpS1r9cp8402xwU2L9a7nBFg8NxD2D2w3SacO5rz60CT1xyywFqPj1jcOy29pWj8EsUuBzbwgwDIpJYVIdqMSb8dqr7Up_n45qW-xz4s3odRZLl_FcLHX0wF_QlmGJ0l3qFzl2l7RuuEBDs6mcNnANT9iZmY82e8p1NUeHL-x1RgHaIhkRQ_El1d0Hi52Utj6aeY7YnRiU3S_N7hm9q2ng9T9OUMdy0jURllngV-KtpOOFrVTuWftxGpRwFzEVd9Crmzl4xxML56g1L-5fyfQGPi0VO35PJoSKeDLIGjV12hcQ5uXtUYu3BCMhRkqVnyxqSD0bnljVLVbB0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f18ec7b09f.mp4?token=OMyNWfqPQMf2EsijYXkONM0ztdmfj0EWZAcB5wDHsUqtmQUsAS9byOUUedUJf6B7mFZOAzwagZ2lL9Zq-gqSbmm_mfCtbg8jPehSzjNuPnfHCggBrGW1wZSREhtX6923avox_8P9GPP_cKLTm8-r5wLQ5SQMKd7WUiHLNQ3TDSYHCitGyOTxUx_u3QSxaesk9RqlHt4w4aQyq_feaFKM63U-yZG8GphrE4f_JAZyp-mV1m-AgMfREFQXsE2sZYOtneRt7UgY_5awnl02iZWEHj7_Premy1Cw1AHz-CRLrGFwJuQOUgB6ZsqEhd9kh5bSOmAb9PERWsSfCorwPNbJbGJkK1zDrpS1r9cp8402xwU2L9a7nBFg8NxD2D2w3SacO5rz60CT1xyywFqPj1jcOy29pWj8EsUuBzbwgwDIpJYVIdqMSb8dqr7Up_n45qW-xz4s3odRZLl_FcLHX0wF_QlmGJ0l3qFzl2l7RuuEBDs6mcNnANT9iZmY82e8p1NUeHL-x1RgHaIhkRQ_El1d0Hi52Utj6aeY7YnRiU3S_N7hm9q2ng9T9OUMdy0jURllngV-KtpOOFrVTuWftxGpRwFzEVd9Crmzl4xxML56g1L-5fyfQGPi0VO35PJoSKeDLIGjV12hcQ5uXtUYu3BCMhRkqVnyxqSD0bnljVLVbB0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
غضب عارم في الشارع العراقي.. تشييع شهداء العدوان السعودي الأمريكي الغاشم في محافظة نينوى شمالي العراق وسط صيحات كلا كلا آل سعود ونعم نعم للمقاومة.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/86255" target="_blank">📅 01:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86254">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اصوات انفجارات مجهولة بمعدل ضربتين سمعت بوضوح في العاصمة السعودية الرياض</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/86254" target="_blank">📅 01:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86253">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEt-e-5mAvatqM3MwuzJ8vg3monoL5TEsEXMKzoDfE-kZH1KHN_U-8bnjbSKbMg12pEakoyiQvtnFh0UWWCWgZKcl_-AI_hpD4_uxg3Mj4HbzU4hLp3eUY7Bm4X-HWTPh7mt1L-5YH01SLdTlWhPf6AIyDBzH8gPPutnCzBh2k5OTHGLPCj31X0PW7_x7vBd8JKFha3A-C0_noqJtGl_N-QlSiVwmWGq1BvIJ3ZYO2bHkGpLbYuOac2VoizdBYxmuwAbswS6EKM6N2qy-_AZIcVqNb803ox6GsiNJqk-YEN-lx4Ij5L7qURGj0d8bfPPizoh3czIqMZV4o9icd3G5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إيلون ماسك يحضر حساب وكالة تسنيم الإيرانية على تطبيق تويتر " اكس "</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/86253" target="_blank">📅 00:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86252">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c11fe0a58.mp4?token=SJRTF_5aYogQBeSqVy65vu70PAVib3ppIuxcjRSNCVMQUfTyY02vw8PhujHTel2jqkE6AH4eKEhkMHOz3mq1Jv868LsAtl7xO5uAd_XDe3iONaIFBJSvpUeN4zLvJO5MeOvE4-W1EvuVVgVrWqfngShfAZ6uq-k8trSpcBOvVtMloPJEi62JjjneNYhzkyHhyq3kv_qHEUySzJ7aiToHsiGZp68iBNLr7iLetgWhZBDRQKTmxnslW4FGE8rMRFURFCRmCTLQYClB7oevN1TfaQt44Yq_vtgGUiv1ROrXXpdwzpoXPk26qINpDcJc56P1HRXcCHrUccvIZCfh1V9FnL2EY6tEk5GrOTuFomldCd39cV_QV6hsclrcjPpLN4hRBeQ44BLPkMdd8iOIn2NWwsgIfEaVodr337VEXJOLW-Df_TXcEUSnf3WXNd3TCY8zWz1NivRYSAc5iF5g_TzsqkjeXwL1Az5wD5rr1ECOAoTn_rzAQcTA_RweyOi56AXRoWRFQV7nIIsizpT46M8eg8tVHK0NXC_7jhX7hTK3PFmcMrfPNIZBaHKtR_z_GeYGlpWTmhwJEqhV1n7r_ZyUz5145uB2RJ5UadpfpFkUmqfOcGC0fBw6yTpiRNMyrQUIUA72QWnAhqmf5pLBLA51RU2qGyePcirgBCFis5CQ-g4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c11fe0a58.mp4?token=SJRTF_5aYogQBeSqVy65vu70PAVib3ppIuxcjRSNCVMQUfTyY02vw8PhujHTel2jqkE6AH4eKEhkMHOz3mq1Jv868LsAtl7xO5uAd_XDe3iONaIFBJSvpUeN4zLvJO5MeOvE4-W1EvuVVgVrWqfngShfAZ6uq-k8trSpcBOvVtMloPJEi62JjjneNYhzkyHhyq3kv_qHEUySzJ7aiToHsiGZp68iBNLr7iLetgWhZBDRQKTmxnslW4FGE8rMRFURFCRmCTLQYClB7oevN1TfaQt44Yq_vtgGUiv1ROrXXpdwzpoXPk26qINpDcJc56P1HRXcCHrUccvIZCfh1V9FnL2EY6tEk5GrOTuFomldCd39cV_QV6hsclrcjPpLN4hRBeQ44BLPkMdd8iOIn2NWwsgIfEaVodr337VEXJOLW-Df_TXcEUSnf3WXNd3TCY8zWz1NivRYSAc5iF5g_TzsqkjeXwL1Az5wD5rr1ECOAoTn_rzAQcTA_RweyOi56AXRoWRFQV7nIIsizpT46M8eg8tVHK0NXC_7jhX7hTK3PFmcMrfPNIZBaHKtR_z_GeYGlpWTmhwJEqhV1n7r_ZyUz5145uB2RJ5UadpfpFkUmqfOcGC0fBw6yTpiRNMyrQUIUA72QWnAhqmf5pLBLA51RU2qGyePcirgBCFis5CQ-g4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
غضب عارم في الشارع العراقي..
تشييع شهداء العدوان السعودي الأمريكي الغاشم في محافظة نينوى شمالي العراق وسط صيحات
كلا كلا آل سعود
و
نعم نعم للمقاومة
.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/86252" target="_blank">📅 00:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86251">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">طيران حربي في سماء محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/86251" target="_blank">📅 00:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86250">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇺🇸
مسؤول بالإدارة الأمريكية:
الرئيس لا يزال يدرس خياراته ولما يحدد مكان أو قوة الضربة لإيران.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/86250" target="_blank">📅 00:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86249">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇮🇷
هجوم مسلح من قبل عناصر إرهابية في مدينة ايرانشهر بمحافظة بلوشستان جنوب شرق إيران؛ استشهاد منتسب كحصيلة أولية.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/86249" target="_blank">📅 00:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86248">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">الإطار التنسيقي:
استضاف رئيس مجلس الوزراء السيد علي فالح الزيدي، اليوم الأربعاء، 29- تموز- 2026، بالقصر الحكومي، اجتماعاً طارئاً للإطار التنسيقي لبحث الاعتداءات الأمريكية - السعودية على سيادة العراق.
وأدان الإطار التنسيقي العدوان الذي استهدف الأراضي العراقية، وأدى إلى استشهاد عدد من منتسبي هيئة الحشد الشعبي وإصابة آخرين، في انتهاكٍ صارخ لسيادة العراق وحرمة أراضيه، وبما يخالف مبادئ القانون الدولي وميثاق الأمم المتحدة.
واستغرب الإطار التنسيقي هذا الاعتداء في الوقت الذي تتبنى الحكومة فيه سياسة خارجية متوازنة تقوم على بناء علاقات التعاون والشراكة مع محيطه الإقليمي والمجتمع الدولي.
وتقدم الإطار التنسيقي بخالص العزاء والمواساة إلى ذوي الشهداء، وتمنى الشفاء العاجل للجرحى، وأكد الإطار التنسيقي أن أمن العراق وسيادته لا يمكن القبول بتجاوزه أو المساس به تحت أي ظرف، مع رفض تحويله إلى ساحة للصراعات الإقليمية والدولية.
كما يؤكد أن الهجمات التي استهدفت العراق وانتهكت سيادته لا تخدم الجهود الإقليمية والدولية الرامية إلى احتواء الأزمة وخفض التصعيد، بل تسهم في تعقيد المشهد وتهدد الأمن والاستقرار في المنطقة بأسرها.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/86248" target="_blank">📅 00:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86247">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bbcf1f5b1.mp4?token=QfmvkUGGkWlCWXFOVsjc7B3hZy4b9ZK3y81jV6Jna8M08bq2YanbvAgXUF8EgMSi4YNGhcTjkA1a6_AXYWlH_6a9OdPabyBhcpAYmlRI7VvCe_EA5YVZb1AxtdPjHNWN5JVZd_4n78MmIYHcjYU1HVMfqpxmX3qHckANeyU8xBAtc_eUCogXOme4oDH_ilKMpurvexly0xSWeIlvNhxhG62QFSsQYhmIEjxJ21j_QATN6pwB0Rg3LKwQWpYv2AZLVpG8lkz0F4uXfAXDXuXdann_EB-pNcpQHD6Chl2eEmnAD2QxP0Gn7lRbkUOx6YQotI1hyjCCwF4Jjb7lKIJUAqdXE6nzICodshs9XgYFto6b2IU7qIegQBKkFbJ_nFmlodHdTQxqJeQMsu2i2g7Xe3-Cq5ypuhl9HQhl0_ITMVaVKtmSjiUKkqYu9Y_ux-mbFE9T8FT54puCPVkLN0CmoOlbToV2NZ1WxhiuIOr-43Zt6NqCnFYA0ag95GcG_N0PCtjotAk8-QDJHCS4QwEMkWNmIk-THLcwYoOA820otey1rK7TGECnycb_VjaYhr7cedVDjS5ClaCFDKurpGSYcj8v5G3-xkLDjM9j9E8JKAQg8UTep6ubnrr0HAyMrH9vcA6UbwEdCphw33gOqGUq3ku_gbgLXCc3u-QAZK88tV8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bbcf1f5b1.mp4?token=QfmvkUGGkWlCWXFOVsjc7B3hZy4b9ZK3y81jV6Jna8M08bq2YanbvAgXUF8EgMSi4YNGhcTjkA1a6_AXYWlH_6a9OdPabyBhcpAYmlRI7VvCe_EA5YVZb1AxtdPjHNWN5JVZd_4n78MmIYHcjYU1HVMfqpxmX3qHckANeyU8xBAtc_eUCogXOme4oDH_ilKMpurvexly0xSWeIlvNhxhG62QFSsQYhmIEjxJ21j_QATN6pwB0Rg3LKwQWpYv2AZLVpG8lkz0F4uXfAXDXuXdann_EB-pNcpQHD6Chl2eEmnAD2QxP0Gn7lRbkUOx6YQotI1hyjCCwF4Jjb7lKIJUAqdXE6nzICodshs9XgYFto6b2IU7qIegQBKkFbJ_nFmlodHdTQxqJeQMsu2i2g7Xe3-Cq5ypuhl9HQhl0_ITMVaVKtmSjiUKkqYu9Y_ux-mbFE9T8FT54puCPVkLN0CmoOlbToV2NZ1WxhiuIOr-43Zt6NqCnFYA0ag95GcG_N0PCtjotAk8-QDJHCS4QwEMkWNmIk-THLcwYoOA820otey1rK7TGECnycb_VjaYhr7cedVDjS5ClaCFDKurpGSYcj8v5G3-xkLDjM9j9E8JKAQg8UTep6ubnrr0HAyMrH9vcA6UbwEdCphw33gOqGUq3ku_gbgLXCc3u-QAZK88tV8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
فيديو من الذاكرة للاعلامي القطري عبد العزيز آل إسحاق، الحشد الشعبي العراقي قادر على احتلال السعودية من خلال تطبيق أوبر.
﴿أَلَيْسَ الصُّبْحُ بِقَرِيبٍ﴾</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/86247" target="_blank">📅 00:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86246">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇮🇷
الحرس الثوري في محافظة مازندران:
الخبر المتعلق بهجوم على سفينة شحن في منطقة خزرشهر، فریدونکنار، غير صحيح، ولم يحدث أي حادث أمني في هذه المنطقة.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/86246" target="_blank">📅 23:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86245">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">إعلام غربي : تعمل السعودية على تشكيل تحالف دولي يهدف إلى حماية طرق الشحن في البحر الأحمر من هجمات الحوثيين، وفقًا لمصادر مطلعة على المناقشات.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/naya_foriraq/86245" target="_blank">📅 23:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86243">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇷
إغلاق حساب العلاقات العامة للحرس الثوري الإيراني دليل على خوف جبهة الغطرسة من البيانات الدقيقة والتنسيق بين شعوب المنطقة المحبة للحرية.
بيان العلاقات العامة للحرس الثوري الإيراني:
يا أمة المنطقة النبيلة الواعية، يا أمة الإسلام العظيمة، يا شعوب العالم المحبة للحرية!
بعد أن قام شعوب دول المنطقة الغيورة الشريفة، وخاصة إخواننا وأخواتنا الأعزاء في الأردن والكويت، بدافع من المسؤولية التاريخية والغيرة الإسلامية، بإرسال معلومات قيّمة ودقيقة حول تحركات وقواعد النظام الأمريكي إلى الحساب الذي أعلنه الحرس الثوري الإيراني على تطبيق تيليجرام، لم يستطع الأعداء المتعجرفون تحمل هذه الظروف والروابط بين الشعوب، فأظهروا، بإغلاقهم حساب العلاقات العامة للحرس الثوري الإيراني، خوفهم مجدداً من البيانات الدقيقة والقيّمة للأمة الإسلامية العزيزة والتنسيق بين شعوب المنطقة المحبة للحرية.
...هذا العمل المشين والجبان، شأنه شأن سائر أفعالهم الدنيئة، مدانٌ بشدة، وهو دليلٌ واضحٌ على انحدار جبهة الغطرسة ويأسها.
🔹
لن يُسكت إغلاق الحساب صوت الحق وإرادة شعوب المنطقة الصلبة.
يُعلن قسم العلاقات العامة بالحرس الثوري الإسلامي عن إطلاق بوابة إلكترونية جديدة آمنة وموثوقة للتواصل المباشر مع شعوب العالم المحبة للحرية، وذلك لضمان استمرار تبادل المعلومات والتوعية بشكلٍ أقوى من ذي قبل.
نؤكد أن درب المقاومة والنصر سيستمر بلا هوادة، بعون الله تعالى وجهود الأمة الإسلامية.
قسم العلاقات العامة بالحرس الثوري الإسلامي</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/naya_foriraq/86243" target="_blank">📅 23:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86242">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1df8c6c9a.mp4?token=b4TuOJXWPmJLu-WPXB1NDpAoWgNMEeEsUhb4kQe_gWfSMgmY5Xjun6dFjvEwQFmBwpY-027D5WY-rjLa-D1H-54u1kcl-ZUwIyFbIiq9dE0maNa0uE9CynyW_7jph3Qq0t9zvtU-5SVOE3C1v7GuEROara3PnySc0IJxJSxzbjR2usSDFaLVoaT7NUEdIOX2EcasV0s8Dsf5KZ-6bGyBx4Q5L7i4g7Cxwr3HgYFABqC63WpRWzMQtmATFLPJ8A3-mWtajR6s6JfxN6mmNsOn6Ap1BadznuYAj0OhEW4cxKOOyAIEyQcUudYfX3-JzSJDx0vIBZVTmWXUo1J-lXRZTqmMREXY1ZfLKVbHxDFgC4xcmA0fYFBlw7pzj1XpRzq6ckDx8Dd83VOudhPZ5y0-oZpa2VJNQABMb-EDovGz0dZjWu__gUcrNsoyD6uPW24qmCRFdtPt3fRyAUFBo1B5XtNJrtyGIYlVIGoRyji_HekCHBvL5koivIW29dZN2H8BnMvZ0_31uDamKA3JpDANYtToga486suReKSwUFEhn4J7GGOivxjsecHiRBpfkT3kXXif_FjXSusGzcefWwYpPCglzHRdGS9Tw4d7NJCfeDrrUS_4ER_rR7WmQPMkhd88UcALLcpc9izF5PchVJAIlotNzMxcB5XgcYoxJZuq1CI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1df8c6c9a.mp4?token=b4TuOJXWPmJLu-WPXB1NDpAoWgNMEeEsUhb4kQe_gWfSMgmY5Xjun6dFjvEwQFmBwpY-027D5WY-rjLa-D1H-54u1kcl-ZUwIyFbIiq9dE0maNa0uE9CynyW_7jph3Qq0t9zvtU-5SVOE3C1v7GuEROara3PnySc0IJxJSxzbjR2usSDFaLVoaT7NUEdIOX2EcasV0s8Dsf5KZ-6bGyBx4Q5L7i4g7Cxwr3HgYFABqC63WpRWzMQtmATFLPJ8A3-mWtajR6s6JfxN6mmNsOn6Ap1BadznuYAj0OhEW4cxKOOyAIEyQcUudYfX3-JzSJDx0vIBZVTmWXUo1J-lXRZTqmMREXY1ZfLKVbHxDFgC4xcmA0fYFBlw7pzj1XpRzq6ckDx8Dd83VOudhPZ5y0-oZpa2VJNQABMb-EDovGz0dZjWu__gUcrNsoyD6uPW24qmCRFdtPt3fRyAUFBo1B5XtNJrtyGIYlVIGoRyji_HekCHBvL5koivIW29dZN2H8BnMvZ0_31uDamKA3JpDANYtToga486suReKSwUFEhn4J7GGOivxjsecHiRBpfkT3kXXif_FjXSusGzcefWwYpPCglzHRdGS9Tw4d7NJCfeDrrUS_4ER_rR7WmQPMkhd88UcALLcpc9izF5PchVJAIlotNzMxcB5XgcYoxJZuq1CI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇺🇸
ترامب عن إيران: سنضربهم بقوة، لقد حان دورنا، أُطلقت علينا 5 صواريخ الليلة الماضية، وتم إسقاطها جميعاً. حان دورنا.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/naya_foriraq/86242" target="_blank">📅 23:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86241">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇷🇺
🇺🇦
‏
زيلينسكي
: روسيا تستعد منذ أيام لتنفيذ ضربة واسعة وهناك احتمال كبير بأن تنفذ الليلة.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/86241" target="_blank">📅 23:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86240">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بعد مضيق هرمز وباب المندب تتجه انظار المحور إلى قناة السويس.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/naya_foriraq/86240" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86239">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇪🇬
🇺🇸
ترمب بخصوص حادثة مصر: جرى إطلاعي على ما حدث في مصر</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/naya_foriraq/86239" target="_blank">📅 22:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86238">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇪🇬
شركة أمبري للأمن: تعرضت ناقلة غاز طبيعي مسال يونانية، ترفع علم برمودا، لهجوم من طائرة مسيرة واحدة على الأقل أثناء رسوها في ميناء دمياط التابع للشركة المصرية القابضة للغاز الطبيعي في مصر.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/naya_foriraq/86238" target="_blank">📅 22:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86237">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇷
🇺🇸
ترامب عن إيران:
سنضربهم بقوة، لقد حان دورنا، أُطلقت علينا 5 صواريخ الليلة الماضية، وتم إسقاطها جميعاً. حان دورنا.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/naya_foriraq/86237" target="_blank">📅 22:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86236">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34f901ff18.mp4?token=jNTS1cRWRitJpORWdQNocvPIO6n9RgygDJsqSQepVU9CBOoncckAbImQ0e3drS9w4P7UgqB3mfUjq4sqvQtIXoU9QE29wqDICyWp18n5byJiz2oMpTKrX8niBykOS4bkggBUBXOIjEJvUQx5_KBj62ZsYb-oGV-5iMhq8hzrPC_QtjGf4ABKougBFzqbNddD7JtaYLVgtwu5O7syuxyAA3RaJcoW0fkVd1gA6KBwSB0IQ62gACKAU5CNpwcvDde4g3r1DpQfwB3NkrrvAu_sVevx0Y113B6fo0JBSoOpCYFdpCUj6aHDe6ADKGtrRaf0u9A67hElXbPj08Z9ndsXsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34f901ff18.mp4?token=jNTS1cRWRitJpORWdQNocvPIO6n9RgygDJsqSQepVU9CBOoncckAbImQ0e3drS9w4P7UgqB3mfUjq4sqvQtIXoU9QE29wqDICyWp18n5byJiz2oMpTKrX8niBykOS4bkggBUBXOIjEJvUQx5_KBj62ZsYb-oGV-5iMhq8hzrPC_QtjGf4ABKougBFzqbNddD7JtaYLVgtwu5O7syuxyAA3RaJcoW0fkVd1gA6KBwSB0IQ62gACKAU5CNpwcvDde4g3r1DpQfwB3NkrrvAu_sVevx0Y113B6fo0JBSoOpCYFdpCUj6aHDe6ADKGtrRaf0u9A67hElXbPj08Z9ndsXsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انفجارات قوية مجددا في قضاء رانية بمحافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/86236" target="_blank">📅 22:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86235">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPVnpnAZhqvHvOM5dqIxbotzxQ1K54Ry8O85OcFbsUaK9i9LeT8OtUYThFZXQK41o6xJaeucQGJVPBduK-Q7j6TM1_fhTS2Bz06fEqlSAGsEQQYnf3EUv6DD-Cx9Zp51EL_7npGi1Zv6MFmvpBOHRrCCa6dhMxY71kVD5bGJDQliKnrq90o4XtbqIsSnKAEqANx8Z8_ci9i7k3FLy3CQvQCUrrtFT0rRDb1uYLwlVaaEzX-MhDzcD0v9BVccM7Ux63KfAcHPXkM5Uh9hjSymUjPJXBDfbdOaBay9T2hfxSU6zysFKLCyse_z9nI5AN4L_mR_hcmM52PGsEWDVT3A_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">يوماً ما ستنقلب الموازين يا ابن سلمان فلا تظن أن بلد العم سام سيبقى إلى جانبك حتى نهاية الطريق راجع صفحات التاريخ وسترى كيف تخلّت الولايات المتحدة عن حلفائها عندما اقتضت مصالحها ذلك.  ﴿أَلَيْسَ الصُّبْحُ بِقَرِيبٍ﴾</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/86235" target="_blank">📅 22:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86234">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇶
مشاهد مصورة توثق آثار الدمار الذي طال أحد مقار الحشد الشعبي ضمن قاطع قيادة عمليات البصرة عقب العدوان الأمريكي - السعودي حيث أظهرت اللقطات حجم الأضرار التي لحقت بالموقع نتيجة الاستهداف.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/86234" target="_blank">📅 22:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86233">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇮🇶
انفجارات قوية مجددا في قضاء رانية بمحافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/naya_foriraq/86233" target="_blank">📅 21:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86232">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇮🇶
انفجارات قوية مجددا في قضاء رانية بمحافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/naya_foriraq/86232" target="_blank">📅 21:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86231">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">توقف تطبيق التلغرام مجددا في العراق !</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/naya_foriraq/86231" target="_blank">📅 21:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86230">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">تشيع شهداء الحشد الشعبي نتيجة اجرام ال سعود</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/naya_foriraq/86230" target="_blank">📅 21:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86229">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">انفجارات تهز سليمانية</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/naya_foriraq/86229" target="_blank">📅 21:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86228">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇪🇬
شركة أمبري للأمن:
تعرضت ناقلة غاز طبيعي مسال يونانية، ترفع علم برمودا، لهجوم من طائرة مسيرة واحدة على الأقل أثناء رسوها في ميناء دمياط التابع للشركة المصرية القابضة للغاز الطبيعي في مصر.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/naya_foriraq/86228" target="_blank">📅 21:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86227">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇶
رئاسة هيئة الحشد الشعبي:
الحشد الشعبي جاهز لتنفيذ جميع توجيهات القائد العام لمواجهة أي اعتداءات تستهدف العراق ومؤسساته الأمنية.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/naya_foriraq/86227" target="_blank">📅 21:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86226">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇷
هزة أرضية بقوة 3.4 درجة ضربت منطقة قريبة من مدينة كوزران في محافظة كرمانشاه.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/86226" target="_blank">📅 20:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86225">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">رضا بهلوي:
سنجد أفضل مكان لسفارة إسرائيلية لائقة في طهران بمجرد سقوط النظام الايراني.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/86225" target="_blank">📅 20:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86224">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇮🇶
الناطق باسم القائد العام للقوات المسلحة العراقية:
الاعتداء السعودي – الأمريكي عرقل جهود التحقيق فيما أثير بشأن استهداف السعودية، ونطالب بتقديم الدلائل والبراهين بشأن انطلاق الاعتداءات من العراق ولم تقدم أية جهة أية أدلة، والحكومة لن تسمح بأي انتهاك من خارج العراق او تصرفات فردية.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/86224" target="_blank">📅 20:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86223">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jznnNgGITLwcwL82V2QsdvG9fEDsX0lOzYT0LCgnalKph1hG750pyCmpxekuDujVp_uUNA4TVYZC9NtiXq6F2oNl0urfm5C8RVLVpQY8oy4QlAZ_9MsVjgFeuah1jVBaSa6WfS5g8pj6ZvkswNatUwYK_iVEvmMqTUkWLtaT5J_38zL7Nm_zqr41x41SrnDbefEo7GPXCZSTS_QWUiGQakDurQ0eFKWteiS-5i_A0JLR4OQtabXma4ipqc97YIZwuvav_BJFTTPLsVG40a_MSPmNSzQVmhCj-x_KDTMAByIkg41WeDACxhFoAmqvH6bTmrcqZ_TB7kg84PPSCvLyhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
حركة انصار الله الاوفياء
أن مراجعة العلاقات مع النظام السعودي أصبحت ضرورة وطنية، في ظل ما يحمله تاريخها من ارتباطات بمرحلة دامية دفع فيها العراقيون أثماناً باهظة نتيجة الإرهاب والتطرف والفكر التكفيري الذي استهدف أبناء هذا الوطن على مدى سنوات.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/86223" target="_blank">📅 20:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86219">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RGgyfLUt3IZkn_w8mUD2wZsr3ZzziF63xQbCDQsTkfZvBJYDs79lGoV8HDFEZEg6rhbsEmIacdT0DGI7e-tt4saigux8rEUuhpkhdAMkcvmoURHdOofaEZSkFrqNhVgSe7Urz7LLE48wf_ch5vsdii3CVC223T9eyBT5YkbwlgXfhhI61mkTRqpAu41NUt5zDBprkmIc5lDyNGJBnzlTIKA-RcnipoEB4k7d96ZLEVf_A1_4wuP4Awhc19bgFk1OKDD-tHBrn5Q19bpgO0jRaerY95qxxKHZdQIBIad48zQowFvi_mwmscyhMlG-La16zHU4MQwWFOgQjSIkpRLc_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uHcHzGJobrxoZ7THfVvwg2W9gMiwnhg2Arc-32VNZpzk8GGcKCeMH4u2yVObiKFrbe-GyT08O1Fc2V25Nza7gfUS7OnC_gEbLVN3RYaK-r0Qgszy-Ed-2-khvDZLSXSn4i9wOCci2AZhKOy3n0PHEomC0w59G22xt-dRDMMDxadg8SMvDGYU5AueHys9hz33Rvsm3NLwJ6CMuT7V4asz0dJBBWdcFpFjoHPYe-akpJfu0TIec_manjfVB50WOyqLnqUXaiNRbIoHws6HaaP54ob-liHn5OWM9PeixygfYXfXvzVQwDoc0_XhSZNPUkmy4D3g846dRQJPTLJMBFlaeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vT2XsbqeQbfnd1Ax2utFmKYsDONfIyYxirZtPtV65IwAZkAJD1sRqQpnz_hmZOSTWnBZmFKRmjhFmsBsxBa9ZQk3d63Gn7Iy3DaBdXh7rlXLCmFLt3xFrbjpz0idLRufuqxevffZV6MPQKcs4Mwjr5W9tWwKwnaVHxvux7lDnDfd6i6jofdQltZtauq34Q0759Je2Uedq2Un6LqEyYzWsWbHE8ikcEzZi1z5ssycMLHQwHDIf_AzKzIUWqu8fgBe9S5uf6h_sNcIiEBg-948uuFtQ6QtGtlacZ5-JGGHpDOC-BE1T1yoSyvZDyjB9fBbejrEZGYyQhnlsSlrkuQh9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WnmHJxmvnUiLGgmXPtPA-AAytW02gs2BLhrWfKSpUVOiV6gJ55s4UaWykAj1JIaCtV4941s0-_cdV6LrilfaTKJDOUGYXjITsTlf1u6HjbJNxnr7H3DZmD-3uZObrebKOQc46VTkyQkyO4g-GfJRFkpmGgVhjZgRrmMTob3xvYBGIn8J_wbPSZDm0M3GkOj9j9-jNO6xeiXfRpNVSYnBOhp4fiMB3rYq5FMoBUeDtR-CDpwk7859gc1ACjzUVks-gCfkagoM1lVhjJsCgDfjYptqrLhDwMrAgQF-a_U8Clw2IgBbQUT36otQZCUJX-NfsDE5K7xQFLE0C1stfIFvpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">استُشهد أربعة من مقاتلي حرس الثورة إثر العدوان الامريكي السعودي على مقرات الحشد الشعبي، وذلك أثناء قيامهم بمهامهم بصفة مستشارين قانونيين إلى جانب مقاتلي الحشد الشعبي.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/86219" target="_blank">📅 20:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86216">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mBFEv9xZBbS6bIwFwU3abEXHPOi_HcMJFvPkm1wd9UOy7qCKlM-oymWQrjWRlAKle0KgkqHy6oc0KYizqDJXZ6dwWi-sF9uw80U0RnLxuP0_MJmBL-K5RDKeOVLhjZGZ06YUGFAEQSoBHk9xn08MzfV0AY6AD8mebCSHNdSD7HQIHgtJy-5XsYA96-6Aww597cVXfo0wS-6-Tb5tRkVy_7WBalckOJa1Uf9spCRrk32afIFvlrqQfcw22klu7u13-Y2xbIDCjHyoPaX1NudmmGraEzJzenHyxe8osnEoapUAQ4E1k49Crpu_E557z9iy9cR3HbQOx10Y0WgzY-aOcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fpMR3UHnW6G5alHmHgdRwsTeNgfQzUku8Y_A0Fel4OHAgVyAI3HIIiOytciBrp2PQUZ-wpp0M7ncwLNzCAuVchIw754kejerOZ5BrmVbXyyxS4pljk-OJAt-Q6YNK47reR1ex7Q6ycTDW_VSggV68pd7q2SwyzKWbQKe217E9lbcW9WzpvfoOjgLBHzjdJOA5SRUHpRxuwvcypXpPG_lLKZKF5b9DAWr-8lzSkZ6CsmAkqhsxCMSBnphjCZcBdOqg3W5ToBTHAqeuN4tVl_q74JOJ0_mEpXKS3iugzpXlZwdqFC2lZan8dMOyv-2X2HaR0mlWJLGXdoHpZ6a9ULcMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lqr6L1c4RG4MiTAZMU8J5OMtJxKsIDW4xfyxHFwC6IHOhtSgaqQyc9hBofEmh0qiGadG_OvZzoW9o52DIkjXtPDmwW4463V6z3Mb56XsxdUGqYlz7XOGMxRhx2lkU8wVKSLilrb5rgwKFUSc0hFY6GdfrZUws9zjkhnsxAEHJJE_6M6apuhR_PxVb9XMPsJ6rSidHo4ZoBRMnyQSGnXp93FlSuoGV3ZNZ_sIQiOKPJKpQ511M0899ccuwgU7SmHupPUxolyY1M02zBT0zbfNVr80ySrhl3EiiSaoNIfsi16g8YAbZaNI9PC-JRYOb6RjWpfdk-hAJJiZ5gHab_9VZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
النجف الأشرف...
تشييع شهيدين ارتقيا جراء العدوان الأميركي السعودي.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/86216" target="_blank">📅 20:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86215">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ameyfbnkZk5Q2eea15MXMZMnszCGEEYAPxEnQMlEjrDczLmn3d0T6yEBNqjOtDFoF2QIFWh4NzuTqqBdKXDhO2g7PrYW4Axyj8BBxQOI_9CP9xhXk1hm8OOSffxQvpV05PidScpHc06BIvsB-iGqXTVyychxh2XtR5dG_GTssM6uv8RlymKSsZ8SfaVw3NQy4_5gQt8WzS6VC2yHqCRDY1V72sOglzPsJEF6qmavLal5c-ts77RHy0cgsF4fSwZr5vTwGV5zXeWZd0bzriE3-nGw6WE8F_Dz0g7zadpPjcguLMU-JsS6jdXBGgD_erpTyCQ3or02cA1Mk5iVWqUpiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">يوماً ما ستنقلب الموازين يا ابن سلمان فلا تظن أن بلد العم سام سيبقى إلى جانبك حتى نهاية الطريق راجع صفحات التاريخ وسترى كيف تخلّت الولايات المتحدة عن حلفائها عندما اقتضت مصالحها ذلك.
﴿أَلَيْسَ الصُّبْحُ بِقَرِيبٍ﴾</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/86215" target="_blank">📅 20:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86214">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a7529a921.mp4?token=p_HfIhOPXW4FygDGQ2Az5dECUD5HI93QsiWrv9Qe8GM3FZo7oSTVaeZim1jpM1Hzosyg99aM8Z4DLdi4PcIz3GbaztrTEDDmnh1d0wSFrPhIlutye4cIdHU0FVtEjE-VyrZZx-r9HvUdmJScRA5ZvFcc0VOy4W3unLEQt2uzSjqY1CZP8X8AIQXZTpQ-zi1-gjD8MQINWMAuOPiZkrtgobWbsDV-ZqIzqYU9aboCTcqGkrwokb_qEvDxpCvb2Ln61yGYDHaTALd2ptSMMUkqlb0TZeMK-7EfSGNOYLY9fKF62RHmO8eHsP9LZA81RPONU5NghLKMdBZsOadq-RZbww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a7529a921.mp4?token=p_HfIhOPXW4FygDGQ2Az5dECUD5HI93QsiWrv9Qe8GM3FZo7oSTVaeZim1jpM1Hzosyg99aM8Z4DLdi4PcIz3GbaztrTEDDmnh1d0wSFrPhIlutye4cIdHU0FVtEjE-VyrZZx-r9HvUdmJScRA5ZvFcc0VOy4W3unLEQt2uzSjqY1CZP8X8AIQXZTpQ-zi1-gjD8MQINWMAuOPiZkrtgobWbsDV-ZqIzqYU9aboCTcqGkrwokb_qEvDxpCvb2Ln61yGYDHaTALd2ptSMMUkqlb0TZeMK-7EfSGNOYLY9fKF62RHmO8eHsP9LZA81RPONU5NghLKMdBZsOadq-RZbww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
تشييع مهيب في محافظة واسط للشهيد منتظر عيدان العتبي الذي استشهد على اثر العدوان السعودي على الاراضي العراقية.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/86214" target="_blank">📅 20:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86213">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1BGq2AkNveAPr30r0queokoIUj_5bxW-g4-A0A4bfldDOC4fr5GuplcGRSPA3I0u5HY_ZUW_l-DDoD74najwxqE6BEIwoPG55SD0uF0vZG3eZ-d7iOveJ1MYSCKP4TX6drzuhLlTyuJ5j3bMRw7vsfFaloKuTqF7BD6G9C9oBcB6lyTbX-fycDikUUEwlf6ObWSO6GAi39REbwVsJ1XFXHlcUAR-8a_OMCidc2Quih3rqHkmLFIOoGS2W9p3jbI_Qnobyz5AcoqcDhM-wAg9d8n4udPdJxIrLYpCTyFkcxQ2CZerwgMEAW7f_k8-X5ZbZznDGk5nVVZDwTiEsX2HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇱🇧
🇮🇱
رئيس أركان جيش الصهيوني في جنوب لبنان:
"إذا لزم الأمر، سنتوجه إلى مناطق إضافية. نحن مستعدون لمجموعة واسعة من السيناريوهات.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/86213" target="_blank">📅 20:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86211">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/286802a563.mp4?token=e58F1ylmrwWi4Ay9z3b67nnhJDAT3ECmr13jM-jrj3ScyBBN_gn7YrZgHq2QIRrJAGwJTyKgG11w4rOqO3b88AaNX_FjQwAVXa-Xpfxdy2q6eiik-hFRAWq-JIWpF7U8HwHTXzrNxit031KmsdEDmFtoncGKx_S7ONFqYZ_BPhNsG9tfBQkltdP2S-YMjcz-ZZLggU1Xz69GAZmmHrFvd-x3MEHfTZ4psqM8BEMpUVioUJoVGdJj0CpFf_KZfv5p25JtGtomxsMwTTDvP5oDGEkgquHqvZ_baRaJJoBKU3ET9PbLXGcclgnb46rWa7TnPgJFJXt8tYikje53Jwx0QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/286802a563.mp4?token=e58F1ylmrwWi4Ay9z3b67nnhJDAT3ECmr13jM-jrj3ScyBBN_gn7YrZgHq2QIRrJAGwJTyKgG11w4rOqO3b88AaNX_FjQwAVXa-Xpfxdy2q6eiik-hFRAWq-JIWpF7U8HwHTXzrNxit031KmsdEDmFtoncGKx_S7ONFqYZ_BPhNsG9tfBQkltdP2S-YMjcz-ZZLggU1Xz69GAZmmHrFvd-x3MEHfTZ4psqM8BEMpUVioUJoVGdJj0CpFf_KZfv5p25JtGtomxsMwTTDvP5oDGEkgquHqvZ_baRaJJoBKU3ET9PbLXGcclgnb46rWa7TnPgJFJXt8tYikje53Jwx0QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇬
الله اكبر السلطات المصرية تعترف: تم اخماد الحريق.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/86211" target="_blank">📅 19:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86210">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/801f3d5794.mp4?token=Ve-ahyrGkRwCu9RucGswDhnuTHMewrXN8J71ZW1drHggcGzgPFWCkarznQhbVMEtbFB6e0dpNcEqq96yAELQudOLiERdpfl6qkIOGZ5r6legcixAWzgBElxQwcdBgeqWRldDeZz3HjiYWjRZY-wH5pcda6PxqO8HPk_Y90Zm_UAOc2GF7tL2iKDgNIkPHBvP0o-BYkIp7Nr5A3ANINvx1pbMCRN5b6ottuiTN82zQJMIlKMLXlYyT3T6FVntyOtcRROJQUAFFxyA6hyCw15q6-eS5kuFQ8K5lHKVGoO6kbIjKLZzppoo0uRjg3BSX-tgPMguWsz7f-MOa3R_YKTbLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/801f3d5794.mp4?token=Ve-ahyrGkRwCu9RucGswDhnuTHMewrXN8J71ZW1drHggcGzgPFWCkarznQhbVMEtbFB6e0dpNcEqq96yAELQudOLiERdpfl6qkIOGZ5r6legcixAWzgBElxQwcdBgeqWRldDeZz3HjiYWjRZY-wH5pcda6PxqO8HPk_Y90Zm_UAOc2GF7tL2iKDgNIkPHBvP0o-BYkIp7Nr5A3ANINvx1pbMCRN5b6ottuiTN82zQJMIlKMLXlYyT3T6FVntyOtcRROJQUAFFxyA6hyCw15q6-eS5kuFQ8K5lHKVGoO6kbIjKLZzppoo0uRjg3BSX-tgPMguWsz7f-MOa3R_YKTbLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منو ياخذ السلاح يا زلمة، الحاج ابو فدك المحمداوي</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/86210" target="_blank">📅 19:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86209">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇪🇬
رويترز: ‏تعرض مرفق عائم لتخزين الغاز الطبيعي المسال مملوك ومدار من الولايات المتحدة لهجوم بطائرة مسيّرة أثناء وجوده في دمياط المصرية.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/86209" target="_blank">📅 19:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86208">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇪🇬
انفجار بمحطة الغاز الطبيعي المسال في ميناء دمياط بمصر أثناء تفريغ شحنة</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/86208" target="_blank">📅 19:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86207">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇪🇬
انفجار بمحطة الغاز الطبيعي المسال في ميناء دمياط بمصر أثناء تفريغ شحنة</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/86207" target="_blank">📅 19:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86206">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">الجبان ابن الوطن سموه
واخوي استشهد يسمونة هسة الذيل؟
مشاهد من تشييع الشهداء في العاصمة بغداد</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/naya_foriraq/86206" target="_blank">📅 18:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86205">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالإعلام الحربي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dyNjhqZ80AGHN_mvgycpMIbsEcN3X4v4i34Bo0rZVOhby0zJxlZf3OnnCgDuH3KlVImORtBknwxWHl6mDV_wD36FZ63gn_TLT7WDhFTCx01IpINQ5XscQWE_U0PiWVYdhWUe-1ylQzeul5RzrTU8SgKmcUozyM1uqgyE0MfJUELrkVW0X2zg-ogvmJGYkrYkMnEsTBbLl6ncjObiGoTukKyN06mqw5Mct0dxZK9_tJBxjDdGzCd3wX9SSOj8hSfRbX9VlfV7H3V5DpLH5FgQi2sKhm6E45A7rfFOwYYut6UMMcK6wr3ISvHQeHlCQfhhE-q-Olreb-kT80dQiUbFRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم الله الرحمن الرحيم
(وَقَاتِلُوا فِي سَبِيلِ اللَّهِ الَّذِينَ يُقَاتِلُونَكُمْ وَلَا تَعْتَدُوا ۚ إِنَّ اللَّهَ لَا يُحِبُّ الْمُعْتَدِينَ)
بعد أن أكدت المقاومة الإسلامية نفيها القاطع لأي استهداف طال الكيان السعودي ومنشآته، اقترف العدو الأمريكي جريمة جديدة، استهدف فيها رجال الحشد الشعبي وموكباً لخدمة زوار الإمام الحسين (عليه السلام) في كربلاء المقدسة، راح ضحيتها عشرات الشهداء والجرحى.
إننا نؤكد بلا ريب أن النظام السعودي لم يكن ولن يكون إلا خنجراً غادراً أو أداةً قذرةً تُدار من البيت الأبيض وأجهزته الاستخبارية المشبوهة؛ فكما سخّر إمكانياته بالأمس لتفويج الانتحاريين لسفك دماء العراقيين، ها هو اليوم يجدّد مرغماً عقد العمالة لتنفيذ جرائم سادته وإملاءاتهم الإجرامية، للنيل من إرادة شعبنا الأبي.
ولو سلّمنا جدلاً بصحة ادعائهم: أن مصدر ضرب منشآتهم النفطية جاء من العراق. فهل يعقل أن يُرد على محاولة (غير ناجحة) لاستهداف حقل نفطيّ بقتل وجرح العشرات من الأبرياء؟!
ولو افترضنا في هذه المرحلة المفصلية أننا سلّمنا سلاحنا وصواريخنا إلى السلطة الحكومية، كي تتولى هي زمام الدفاع عن سيادة العراق وحرمة أراضيه وشعبه؛ فما الذي ستتخذه من مواقف حازمة أمام هذا الاختبار الميدانيّ الحقيقي، لتثبت للجميع قدرتها على ردع المعتدين، والاقتصاص ممّن سفك دماء الشهداء الزكية، بدلا من رجال المقاومة، وكما فعل المجاهدون ذلك مراراً في العراق؟
وبناءً على ذلك، نعلن الآتي:
أولاً: نمهل الجهات الحكومية التي طالبت المقاومة بنزع سلاحها مهلةً أقصاها حتى الثالث والعشرين من شهر صفر؛ لنرى ما هم فاعلون.
ثانياً: حرصاً منا على حفظ أمن زوار أبي عبد الله الحسين (عليه السلام) وأرباب المواكب الكرام، ومنعاً لأي إرباك لزيارة الأربعين المباركة قبل إتمام مراسمها؛ فإن ردّنا على العدو الأمريكي قادم لا محالة، وقد ينال أدواته في السعودية متى ما استدعت المقتضيات ذلك.
الرحمة والرضوان لشهداءنا الأبرار، والشفاء العاجل للجرحى الكرام.
المقاومة الإسلامية في العراق
29 تموز 2026</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/86205" target="_blank">📅 18:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86204">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8c2INJNL6IPvNwNeEgH2dETgXhVcwctqGWm8MZ_Pe71sEJRALquxoIxyZHnXx2gPdkugTm40tX7TzpYoLlK9-Wmkk0S2vs4AsvUbvaZVzNRQl_DzgHhr7vBUOoMWs2joS2-a9nnS8iJmdGOzSwpj82QqlxsIu6qZXFWJqrxX-_sRNYTk9Jdb9QZ8c1SFnuJPFJXE_xMDbgSbWHcn4lxPGsWfSKjbdvjY_DtGFg-wPLdtgFwheu2RQ5boY2Zx42ZyTbQmmWaxXDfLtbOZtIvY_BPf9kac_n9l6NN5bYBxR9RlI42W4Sy5vRmk8MvzmsG-MBSnuI9RsA1YyZvnMBj3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سعر برميل النفط يتجاوز الـ90 دولارا</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/86204" target="_blank">📅 18:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86203">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">عوائل الشهداء توجه رسالة إلى امين عام حركة النجباء الشيخ أكرم الكعبي: ثأر ولدنا ما يبات هاي الليلة</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/naya_foriraq/86203" target="_blank">📅 17:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86202">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4eLQ5mJvXDwj7l3Bss9rtEbNj5_1WnocxEx6LeVzNyUpmF8joGZwzeTe93MjIeUSo7T6bMZ6BYzNKVXmIvrKEVs-7Xi-E2PfDThQAkTwYDbltP058TWrGTCwpRI58cvBxyBZFq9qoIXl7CVVSnIj4gvGQFtJAzFCDPkseJlZsiq1lbDzOKyiHkfpt55OFiJeAcy27gPcDaXkYgnxNXFD_rYCUknBIq67IUz5tpuRMOignAA_axGw4JZtTq3400lFAJVwQEjNRK7mjUmFl62uhLsltNKFwQo2gYbPxXmDcBAJdUzm-kobEBXage_qUWQmjIU6ZnXss6wbiE7CbGcZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استُشهد أربعة من مقاتلي حرس الثورة إثر العدوان الامريكي السعودي على مقرات الحشد الشعبي، وذلك أثناء قيامهم بمهامهم بصفة مستشارين قانونيين إلى جانب مقاتلي الحشد الشعبي.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/86202" target="_blank">📅 17:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86201">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">صحيفة التيليغراف: الصين سترسل صواريخ إلى إيران.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/86201" target="_blank">📅 17:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86200">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">استُشهد أربعة من مقاتلي حرس الثورة إثر العدوان الامريكي السعودي على مقرات الحشد الشعبي، وذلك أثناء قيامهم بمهامهم بصفة مستشارين قانونيين إلى جانب مقاتلي الحشد الشعبي.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/86200" target="_blank">📅 17:48 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

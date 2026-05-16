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
<img src="https://cdn4.telesco.pe/file/B1ax5EJ6nftW-rH02cU1Px4Mbt9z8fquS7eNgFiNFHTMGe6nTE3gl5GLEqRA6kDyJOrB9YWnyCXYbMgFBVutk4VjAQ8qNi0UvEHDhW0WKoAXh2qiOwpBtrCKk7yOR1uqH5CmONrQIUBma3QS8UVSI_PARNihCtjo7PVqY2P_9sLeVVqlJgOGSS9foYFy02pyUUJ12n_gtlgIMyl3cZHjt-ZB_oxZ8VoZl8Yz1yrf-et8wuMn2ehF9cKLO-DwA9kuQWHUYvZWKdsW5ad5peKwgDjF9lNFYvaqwMeYMwt0oEzwf0mZJQvNo9nBP0rWw6VzT_ezSr8Xbfv5jf__DAAk3g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 254K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-26 15:13:52</div>
<hr>

<div class="tg-post" id="msg-75488">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🌟
🇮🇷
وكالة الأنباء الإيرانية:
زيارة غير معلنة لوزير الداخلية الباكستاني لطهران للقاء المسؤولين الإيرانيين</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/naya_foriraq/75488" target="_blank">📅 14:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75487">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">صافرات الانذار تدوي في المستوطنات الشمالية بعد هجوم صاروخي لحزب الله</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/naya_foriraq/75487" target="_blank">📅 14:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75486">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">صافرات الانذار تدوي في المستوطنات الشمالية بعد هجوم صاروخي لحزب الله</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/naya_foriraq/75486" target="_blank">📅 13:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75485">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQOdqneUFQiMak_y13WXYxtirrfelpRbS-oNo-PVpVEbzmvQi8EGfNXZhJyqKs493Q3ZhTzFgPuG3pZ7nMDps1hdr9h2sWg0cFnOjQmCBa9v67m6Ynh13X0VlT9ijnaH80eDAZqUoaY5KJbfefK2RfEQhDblwm4YW9LihGsh5F7lFOIW1pbxwNs_vQ4UNteKH-1oGenjg8t6ydRGjE5uN4nU23WeD_2tLQvzqcU-4UFkZB3srKA1GJSdnuQvTSzYFITLdbSLekNcrfEWdZb_8vo4iOT-46bJ_0dKNLIYpPLDtqmx9p3yfeQ8UOMR_qon8Fo2eJxsrxtVVvQ3Zf3hFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
رئيس لجنة الامن القومي الايرانية:
أعدت إيران ، في إطار سيادتها الوطنية وضمان أمن التجارة الدولية ، آلية مهنية لإدارة حركة المرور في مضيق هرمز على طول طريق محدد ، سيتم الكشف عنه قريبا. في هذه العملية، لن تستفيد منها سوى السفن التجارية والأطراف المتعاونة مع إيران. وسيتم تحصيل الرسوم اللازمة للخدمات المتخصصة المقدمة في إطار هذه الآلية. وسيظل هذا الطريق مغلقا أمام مشغلي ما يسمى "مشروع الحرية".</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/naya_foriraq/75485" target="_blank">📅 13:51 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75484">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EuWmFb8RHwlb0s6Ooadsp_xJh0Utbx7QZkxyz0MfgwQqA9lu8tG8_mcJVU8EatcsNTpZcUqtwHlCHr14oxsf28gzDR7sCWkXUgx-irtBvNbH-D_cfRi3okvJrWDJZCC3Ya_D87rphvxurFq_iVkbJ_VkDsd1HcwO1qxc7LVK1YAxTdyRDfyBKaiq4VXBdP_26SNVkPQhSdzL5y1cylpZ0AjhUZfm3BfzkQQuFx3h1FLsoSpHVKFHjISH-a17SoFSyH-AA6ifaiSblBHlrTjmk9bCxStjx7pJQFGLgSfjpIBUlnb3iSrpZR2BfoVkV2N1Q3pNaYWyqLTqsuZNNJIwAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهاز ال FBI الأمريكي : ألقت عناصر مكتب التحقيقات الفيدرالي القبض على محمد السعدي، وهو هدف آخر ذو قيمة عالية مسؤول عن الإرهاب العالمي الجماعي، وأعادته إلى البلاد - في أحدث نجاح في العمل التاريخي لإدارة ترامب لتقديم الإرهابيين إلى العدالة. يُزعم أن السعدي وشركائه…</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/naya_foriraq/75484" target="_blank">📅 13:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75483">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df110dc480.mp4?token=Jbq7sobiDCUkzMlcZV_TEQeCt6bNBTmdKUIfV2PlxN2W0HoDWCvKN_3qwWOzbZSje__oNiR8rWjV2QHkRb6tEnQMK67KTLw8zeZIvG9p9A7NAGzCBOBYSWCFpPTfxXTIpOY7gWFV2ZsazqLKuSCHlrk0MZpILFEUiMPPm7FDWaEbS9oGR_lBpmmSnmUVnEGhNITM1-2ls5TI4Fpg3hBinRttU5sDZ7vZzPBbzvzHUatSG0tmPmkwjPLl7gMWXkBsct5sBcZe9ehyu9eu9Fado1m_zs2gGCLS8OO-qEbNZCohv6pufyTt0XpZ2-AKv31s_bbTtZ6rZDw3VKTkhJaIeRW9L4ILyyayx6EXnDg8JLqaKi5s4l4N0knd6XOZmZ8TZqPjbkQqs_ceYP_1HEjDQwAfGt8AwUb4H2R55qSVY1ZdPNIe4QD64o4UeYNkdY8ykcfrQ57IFZrdiKbhSY_I4BXG3Ap2jSq7XsFYY5Wwy3byTBZXNTGBsxklWpj0JRSiJuTzg_NHZV25QotKQctrmBNXakX2FIYOHv0YP6FHy2Cb4RSGD46cByt3z-6sCvuxoIVaV0n1d8xP3kGnSJa_kpzEySQnJGMUItUt232D__wFsZo06P4_PlUPlraXHZAsbfp7GFDp0XWYOWO1_M0FE8J3DKbFIJuJrddU9g8OzEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df110dc480.mp4?token=Jbq7sobiDCUkzMlcZV_TEQeCt6bNBTmdKUIfV2PlxN2W0HoDWCvKN_3qwWOzbZSje__oNiR8rWjV2QHkRb6tEnQMK67KTLw8zeZIvG9p9A7NAGzCBOBYSWCFpPTfxXTIpOY7gWFV2ZsazqLKuSCHlrk0MZpILFEUiMPPm7FDWaEbS9oGR_lBpmmSnmUVnEGhNITM1-2ls5TI4Fpg3hBinRttU5sDZ7vZzPBbzvzHUatSG0tmPmkwjPLl7gMWXkBsct5sBcZe9ehyu9eu9Fado1m_zs2gGCLS8OO-qEbNZCohv6pufyTt0XpZ2-AKv31s_bbTtZ6rZDw3VKTkhJaIeRW9L4ILyyayx6EXnDg8JLqaKi5s4l4N0knd6XOZmZ8TZqPjbkQqs_ceYP_1HEjDQwAfGt8AwUb4H2R55qSVY1ZdPNIe4QD64o4UeYNkdY8ykcfrQ57IFZrdiKbhSY_I4BXG3Ap2jSq7XsFYY5Wwy3byTBZXNTGBsxklWpj0JRSiJuTzg_NHZV25QotKQctrmBNXakX2FIYOHv0YP6FHy2Cb4RSGD46cByt3z-6sCvuxoIVaV0n1d8xP3kGnSJa_kpzEySQnJGMUItUt232D__wFsZo06P4_PlUPlraXHZAsbfp7GFDp0XWYOWO1_M0FE8J3DKbFIJuJrddU9g8OzEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
06-05-2026
آلية "نميرا" تابعة لجيش العدو الإسرائيلي في مدينة بنت جبيل جنوبي لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/naya_foriraq/75483" target="_blank">📅 13:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75482">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_w9DteB6-Twbx5cVZkTDxAJQmQZo4kiXnZZBdQxC23ZDUliqlYHZRnv9LQeKfYBNlqQe42C_uQjetfAvhqRL3KZdsx1zANNx65CpzHZaYcV0UPJgGQ0T9bx9TPJ2RPmgO-UM0SwjsL3EHMJcU27wRT2XK5VkMQbHlAZOiAvQppqZovMXWTZbeVtSj6EfrFsZgXpCVWKIcqrx7iKskti-1Bwlwc0juk6Ir40Wl1DUXNJ-Di70ww2I4okNEWc7Izeh2Ko7YhqrKMpQbnGAY57nqrL50F9tzr7Zs6VQxuqmHU0gGziK3sBm0jtNR8d9kjxdfzKhnvopBTMK28R5r6WGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▫️
رئيس الوزراء الروسي ميخائيل ميشوستين يوجه برقية تهنئة إلى الزيدي</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/naya_foriraq/75482" target="_blank">📅 13:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75481">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ناقلة غاز مسال قطرية - هي الثالثة خلال الأسابيع الماضية - ترسي في ميناء كراتشي قادمة عبر مضيق هرمز</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/naya_foriraq/75481" target="_blank">📅 12:49 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75480">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇮🇶
تعطيل الدوام الرسمي يوم الأحد لموظفي مجلس محافظة بغداد بذكرى استشهاد الإمام محمد الجواد (عليه السلام)</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/naya_foriraq/75480" target="_blank">📅 12:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75479">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3f924a615.mp4?token=ShZ3thKPPETwXj-x4MjDeKtd6ExmvY2elcDAJ6SW4l_RMl1M7izow3oO43RVXOS45jEUuspOA-R9G3rwiFJmM5dZTW95dwqwxLY_SjMK2WGVM4QXG3BecOFMGDWqp3OK1TYz5A-gL8LKw2HGybY361K8pevGNl9X4KbXZIONnYnfk55uqL0qXcpcAa7fH87a5Kr-pRItLsKRZZ0a_ah3qflZtqU5IcyUhdv75WkbooLXi3a96MUdAZklcEOf6FZLE8xCxinccs62y7Hl7LLsRkeIOWlMC7z9S2lRD2G6zkinfBSs5g6yzmrlHHhAyxoqtbNDe1i5n3LJvNn8WASLQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3f924a615.mp4?token=ShZ3thKPPETwXj-x4MjDeKtd6ExmvY2elcDAJ6SW4l_RMl1M7izow3oO43RVXOS45jEUuspOA-R9G3rwiFJmM5dZTW95dwqwxLY_SjMK2WGVM4QXG3BecOFMGDWqp3OK1TYz5A-gL8LKw2HGybY361K8pevGNl9X4KbXZIONnYnfk55uqL0qXcpcAa7fH87a5Kr-pRItLsKRZZ0a_ah3qflZtqU5IcyUhdv75WkbooLXi3a96MUdAZklcEOf6FZLE8xCxinccs62y7Hl7LLsRkeIOWlMC7z9S2lRD2G6zkinfBSs5g6yzmrlHHhAyxoqtbNDe1i5n3LJvNn8WASLQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوات الاحتلال الصهيوني تتوغل في محافظة القنيطرة جنوبي سوريا وتنفذ عمليات مداهمة للمنازل في المنطقة.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/75479" target="_blank">📅 10:34 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75478">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">انفجار يهز المنطقة الخضراء وسط العاصمة بغداد</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/75478" target="_blank">📅 09:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75477">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">انفجار يهز المنطقة الخضراء وسط العاصمة بغداد</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/75477" target="_blank">📅 09:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75476">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">تسلل طيران مسير من حزب الله باتجاه شمال الكيان المحتل</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/75476" target="_blank">📅 09:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75475">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">إعلام أمريكي: تمكنا من إحباط مساعي هذا الرجل في زرع الفوضى وتصدير الرعب، ليس إلى الولايات المتحدة وحدها، بل إلى كندا وأوروبا أيضا.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/75475" target="_blank">📅 01:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75474">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">📰
وول ستريت جورنال:
لا يزال أكثر من 100 منصب سفير أمريكي شاغراً بعد مرور 18 شهراً على ولاية ترامب الثانية - وهو معدل غير مسبوق يحذر الدبلوماسيون من أنه يضعف النفوذ الأمريكي في الخارج.
تشمل الفجوات الرئيسية المملكة العربية السعودية، والإمارات العربية المتحدة، وقطر، والعراق، والكويت، وأوكرانيا، وروسيا. وفي أفريقيا، تفتقر 37 سفارة من أصل 51 سفارة إلى سفراء.
يمكن للدبلوماسيين المهنيين الذين يعملون كمبعوثين مؤقتين إدارة العمليات اليومية، لكنهم غالباً ما يفتقرون إلى إمكانية الوصول والنفوذ الذي يتمتع به السفراء الذين تم تأكيدهم من قبل مجلس الشيوخ.
وفقاً للجمعية الأمريكية للخدمة الخارجية، هناك حالياً 115 منصباً سفيرياً شاغراً من أصل 195 منصباً - مقارنة بـ 45 شاغراً في نفس الفترة من الولاية الأولى لترامب و 12 شاغراً خلال الولاية الثانية لأوباما.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/75474" target="_blank">📅 01:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75473">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61bb464b53.mp4?token=v852EOfTS01Z2I4bgliPpVULqrpUjes2G4YGyx7vyLCthX3AoNXc8iNsXjOSED5fzb7kfFuMjcfUuDx6oF4KZCMCrrupZJXMlc3Qn0BHCBBLY2dbP80p-1CqI7cQafXRO55xKdO8vGFF5dJnovyjoMgwVQ53tYRBl9VhJ4hdUBmmfiskohamfkxJ_YsTbaPdGCQT8vqmrPR1w11FZefIG7GhRh7Iidfw8l7vgAh7nNjMJYOjemFwfV6TcwxQkx7BI-w6fwbrJ2tQoOZoraWY5muKQJZUD5PT-Ddw8oJV7J2R3I6CkzD7eg4a6mrVaCHoLPLtLr4edUI_0fEt3xRt7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61bb464b53.mp4?token=v852EOfTS01Z2I4bgliPpVULqrpUjes2G4YGyx7vyLCthX3AoNXc8iNsXjOSED5fzb7kfFuMjcfUuDx6oF4KZCMCrrupZJXMlc3Qn0BHCBBLY2dbP80p-1CqI7cQafXRO55xKdO8vGFF5dJnovyjoMgwVQ53tYRBl9VhJ4hdUBmmfiskohamfkxJ_YsTbaPdGCQT8vqmrPR1w11FZefIG7GhRh7Iidfw8l7vgAh7nNjMJYOjemFwfV6TcwxQkx7BI-w6fwbrJ2tQoOZoraWY5muKQJZUD5PT-Ddw8oJV7J2R3I6CkzD7eg4a6mrVaCHoLPLtLr4edUI_0fEt3xRt7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جهاز ال FBI الأمريكي : ألقت عناصر مكتب التحقيقات الفيدرالي القبض على محمد السعدي، وهو هدف آخر ذو قيمة عالية مسؤول عن الإرهاب العالمي الجماعي، وأعادته إلى البلاد - في أحدث نجاح في العمل التاريخي لإدارة ترامب لتقديم الإرهابيين إلى العدالة. يُزعم أن السعدي وشركائه…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/75473" target="_blank">📅 01:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75472">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسرايا اولياء الدم</strong></div>
<div class="tg-text">«من أراد العزَّ فالعزُّ هنا شامخُ ما بينَ حدٍّ وزناد، لا ينال الذلُّ من عبدٍ مضى يسحق الذلَّ بساحات الجهاد»
#سرایا_اولياء_الدم</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/75472" target="_blank">📅 00:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75471">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">جهاز ال FBI الأمريكي : ألقت عناصر مكتب التحقيقات الفيدرالي القبض على محمد السعدي، وهو هدف آخر ذو قيمة عالية مسؤول عن الإرهاب العالمي الجماعي، وأعادته إلى البلاد - في أحدث نجاح في العمل التاريخي لإدارة ترامب لتقديم الإرهابيين إلى العدالة. يُزعم أن السعدي وشركائه…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/75471" target="_blank">📅 00:23 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75470">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">جهاز ال FBI الأمريكي : ألقت عناصر مكتب التحقيقات الفيدرالي القبض على محمد السعدي، وهو هدف آخر ذو قيمة عالية مسؤول عن الإرهاب العالمي الجماعي، وأعادته إلى البلاد - في أحدث نجاح في العمل التاريخي لإدارة ترامب لتقديم الإرهابيين إلى العدالة. يُزعم أن السعدي وشركائه…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/75470" target="_blank">📅 00:20 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75469">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">⚔️
Animation Grafik
Simulation Harakat al-Nujaba attacks on U.S. military bases in Iraq and the region</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/75469" target="_blank">📅 23:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75468">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">مشاهد اولية لاعتقال العراقي محمد باقر السعدي من قبل جهاز ال FBI الأمريكي</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/75468" target="_blank">📅 23:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75467">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZ1-Si_miPEDKvVGhFm_QbquEdN6ecFx4VEkpn7zIG0Rd6A6LgP2JmrnMTRIYBhc4DK33i5RFnuUU9ys6o_Yab5uNjG4Ke09aTUJS0oVC1LslzPnFfqelO_L8rPaa6HeEWIAEk4EeYWC_Y6Yrf50JlV8LfYmmEI55y0EreIxyKJZd6L96vyGyGr82myIpnuCp_BTNvgyLzrsSToC5K_6tidFw3Xgii7tFJ8h3KxRTfYA3LLiqXg8lNBYwkddviApmPp2mipl76MadxJu54PTQkrcUyVITmmA80pq_jlplSzKXQwNo6mt6UWhKO72Gg4AcUyLuDyWQHTGFzDXnZCIFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهاز ال FBI الأمريكي : ألقت عناصر مكتب التحقيقات الفيدرالي القبض على محمد السعدي، وهو هدف آخر ذو قيمة عالية مسؤول عن الإرهاب العالمي الجماعي، وأعادته إلى البلاد - في أحدث نجاح في العمل التاريخي لإدارة ترامب لتقديم الإرهابيين إلى العدالة. يُزعم أن السعدي وشركائه…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/75467" target="_blank">📅 23:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75466">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇺🇸
سي إن إن:
قراصنة يخترقون أجهزة قراءة خزانات الوقود في محطات الوقود الأمريكية؛ ويشتبه المسؤولون في أن إيران هي المسؤولة.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/75466" target="_blank">📅 23:24 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75465">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">جهاز ال FBI الأمريكي :
ألقت عناصر مكتب التحقيقات الفيدرالي القبض على محمد السعدي، وهو هدف آخر ذو قيمة عالية مسؤول عن الإرهاب العالمي الجماعي، وأعادته إلى البلاد - في أحدث نجاح في العمل التاريخي لإدارة ترامب لتقديم الإرهابيين إلى العدالة. يُزعم أن السعدي وشركائه خططوا ونسقوا وأعلنوا مسؤوليتهم عن ما لا يقل عن 20 هجومًا إرهابيًا في جميع أنحاء أوروبا وكندا - وكان يُعتقد أنهم يستهدفون الولايات المتحدة بهجمات قادمة بما في ذلك المؤسسات اليهودية في نيويورك وكاليفورنيا وأريزونا.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/75465" target="_blank">📅 22:48 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75464">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5186ce786e.mp4?token=ppLfVoymS0XkWAZP_q8my3LsG63Eo26r-8SkCejOBb7Y5CUShS9gj6hvn9yd5z0uNtAHl5TEg95TQ6HI1bwcZUhiSjA9JQvs_UWbsB_3YuKUVBJUVLBBpFCSmetOsy-Raz2SWKAKfwABTUWpIerxs8Haov_CxDme32SF__lE16ROxnK91yzxUzLawRwTK8aQFqLaL59Ex-pnbPNtyDw1MPM5hz3SC6DdZjBllawqsR3N_8SMEkwlk19dvJ63YP74iO7wrwgKKdp1WigWzxrKdrF6Gyaa8gGNI1jsL5o0KWYxf-WWiYtBOOBVIe3X_4g5jYR4Olf0kRDkyBehlsXa_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5186ce786e.mp4?token=ppLfVoymS0XkWAZP_q8my3LsG63Eo26r-8SkCejOBb7Y5CUShS9gj6hvn9yd5z0uNtAHl5TEg95TQ6HI1bwcZUhiSjA9JQvs_UWbsB_3YuKUVBJUVLBBpFCSmetOsy-Raz2SWKAKfwABTUWpIerxs8Haov_CxDme32SF__lE16ROxnK91yzxUzLawRwTK8aQFqLaL59Ex-pnbPNtyDw1MPM5hz3SC6DdZjBllawqsR3N_8SMEkwlk19dvJ63YP74iO7wrwgKKdp1WigWzxrKdrF6Gyaa8gGNI1jsL5o0KWYxf-WWiYtBOOBVIe3X_4g5jYR4Olf0kRDkyBehlsXa_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: لم أقلل من تقدير قدرة إيران على التحمل.  أبقينا على جسور إيران ومحطات توليد الكهرباء وبإمكاننا تدمير كل ذلك بالكامل خلال يومين فقط.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/75464" target="_blank">📅 21:49 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75463">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇺🇸
وزارة الخارجية الأمريكية:
سيتم تمديد وقف إطلاق النار بين إسرائيل ولبنان لمدة 45 يومًا للسماح بمزيد من التقدم.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/75463" target="_blank">📅 21:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75462">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
11-05-2026
آلية هندسيّة تابعة لجيش العدو الإسرائيلي في بلدة البيّاضة جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/75462" target="_blank">📅 21:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75461">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e93bc4d06.mp4?token=EDLxD6NIWyzv0S79s9yo2GDO_bH_P538TYw-eTtnzrAjD7C6J3i8s17zxTW7le5aqFlKbWkmQb30WYlHDmISLzgkmjnzjCqYDvOGcnGWwdNbwyFH4ZeYp--QwXIpWTKVOpo6EgFRBj3zK6pV7pi6kRrr-yOMagwgRSQDoZwDiOIasxk0A9O3hdBnB4pyu0-6aiqAx07iH28_a0HJ29AQ-QhK54FZju3nUeh5TmW9XHJQ96NsbKl5pdjhPHzH4fut7AgLszir_K8m5mt00kGYR48p4S5F8tx_fjGQ5Z1pdmgYmY63T4FiC1u-EWqkdf9R0Ou9GXPI4WBrHNvtXPJgcLG-VIIP2FHtX1_7oJAGMRJ7PXlSGVeDM3XCfLqfFDEQ-HMJIjqkBKWu88QwkqEz5JRcSaY5KMH1JWKv6Jr6w3aQzV_Qd0E6n546Z4q5ttwx7_eALXn53gxRq-xKdgQ742CwYoZqoIvt6r5luBiw4dhCU1JblRy2SkiIlyRpW-MOrV995CYfMCkCevtj9bGBYgofLxrmGwAT00fAzoJ6JewpYTGuC8DD2DmMcqtrNybCj-ridico8gR329bp2WFIFhwDF7av1cTGL8z4mIaPVXx-zcklgal6UrW3yxuWGBqbI1gVrWg5WvGlqs5yRKxz9ZZ1dJLl0zQAekeFeeKLAJ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e93bc4d06.mp4?token=EDLxD6NIWyzv0S79s9yo2GDO_bH_P538TYw-eTtnzrAjD7C6J3i8s17zxTW7le5aqFlKbWkmQb30WYlHDmISLzgkmjnzjCqYDvOGcnGWwdNbwyFH4ZeYp--QwXIpWTKVOpo6EgFRBj3zK6pV7pi6kRrr-yOMagwgRSQDoZwDiOIasxk0A9O3hdBnB4pyu0-6aiqAx07iH28_a0HJ29AQ-QhK54FZju3nUeh5TmW9XHJQ96NsbKl5pdjhPHzH4fut7AgLszir_K8m5mt00kGYR48p4S5F8tx_fjGQ5Z1pdmgYmY63T4FiC1u-EWqkdf9R0Ou9GXPI4WBrHNvtXPJgcLG-VIIP2FHtX1_7oJAGMRJ7PXlSGVeDM3XCfLqfFDEQ-HMJIjqkBKWu88QwkqEz5JRcSaY5KMH1JWKv6Jr6w3aQzV_Qd0E6n546Z4q5ttwx7_eALXn53gxRq-xKdgQ742CwYoZqoIvt6r5luBiw4dhCU1JblRy2SkiIlyRpW-MOrV995CYfMCkCevtj9bGBYgofLxrmGwAT00fAzoJ6JewpYTGuC8DD2DmMcqtrNybCj-ridico8gR329bp2WFIFhwDF7av1cTGL8z4mIaPVXx-zcklgal6UrW3yxuWGBqbI1gVrWg5WvGlqs5yRKxz9ZZ1dJLl0zQAekeFeeKLAJ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
‏نتنياهو يزعم: استهدفنا بغارة قائد الجناح العسكري لحماس عز الدين الحداد.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/75461" target="_blank">📅 20:54 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75460">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
12-05-2026
تجمّع لجنود جيش العدو الإسرائيلي قرب مرفأ الناقورة في جنوب لبنان بسربٍ من المسيّرات الانقضاضيّة.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/75460" target="_blank">📅 20:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75459">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbbff97235.mp4?token=KAqa5zyfRYgyVOrar-IOnqJl05PICwVZDjblnWCoBNtfefhGGJt4AL7EFZfo1dfANO7vBSmghoWxkDW9IiU5H6qpakcE29dHV124wNU7tF6_IDNsBnvQthIV3rVU-Uoza47gkpHeBycZoU9cQH1BqkbtuqkxOUu3teiwc2giZpgcOe3xFSQR-KpEyCAR3uE7KirmW7TB3uPEA9j3aU-HBlzJay6ISl5HZl6JZic6O0kem6NjvQlDa6wUEnSGpM_71MpKDf7sJaVD4qm9cyX1_MKtxQzm8lkFXO3Nufqk1vpNDpzlh8WmRIhw4Fl1e_mAD9KGueROOWKZTaQ0pIOAjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbbff97235.mp4?token=KAqa5zyfRYgyVOrar-IOnqJl05PICwVZDjblnWCoBNtfefhGGJt4AL7EFZfo1dfANO7vBSmghoWxkDW9IiU5H6qpakcE29dHV124wNU7tF6_IDNsBnvQthIV3rVU-Uoza47gkpHeBycZoU9cQH1BqkbtuqkxOUu3teiwc2giZpgcOe3xFSQR-KpEyCAR3uE7KirmW7TB3uPEA9j3aU-HBlzJay6ISl5HZl6JZic6O0kem6NjvQlDa6wUEnSGpM_71MpKDf7sJaVD4qm9cyX1_MKtxQzm8lkFXO3Nufqk1vpNDpzlh8WmRIhw4Fl1e_mAD9KGueROOWKZTaQ0pIOAjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
‏
نتنياهو يزعم:
استهدفنا بغارة قائد الجناح العسكري لحماس عز الدين الحداد.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/75459" target="_blank">📅 20:41 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75458">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سوالف الگهوة
الأساس وتصميم سيلتحقون بالمالكي و الفياض والأسدي والغراوي ويلحقهم المجلس الأعلى وأبو الاء الولائي ..</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/75458" target="_blank">📅 20:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75457">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DThSDFDgN3U1dGNH7hWZKaYD0SVVtHOqLWJKz4SqrkMXr8gGrTtdznF9Ir8RtZmgo-uwJy2YF74x8j1xYR3cOaMq7YGKXYbZLMrEP_MNgwa2QTbt7eino2eUhZqZKHrp1emeSoYhhQyBI-NNadaWSkzlbcnrqFWZF7kjAqfPY-JS3n_CuspkmMIHnk9Je4ChSE6QDMPQ1UUFZDD_U9VZifoBFdh6g0aCo2TVkSBOSi4pcBOHJ1kMIZyZ5XGXQnnQQ8F4nGJ8bJ8v0Moanr3_ZtTseydRxh87CoO7IXwMoTkTUHoEByGXmm2_9BTj900khb3Wrqu5I2XaenQD_mxgAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">السياسي العراقي حامد السيد يؤشر بخلل بموقع رئاسة الجمهورية !</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/75457" target="_blank">📅 20:36 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75455">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb51233478.mp4?token=YuQhY0zbEcuPbfUOAAem1BH6LUNbAZcep7fNC8uY7VKXpwrXHagddLpLXs9XsW19WbnJ5L_rPDk4rIz2Fls3xMb2Z5ivGi-bRpVfVi5MPf4ofFSBOkUPH_0Xh0WCmH07-VWAU45q8DE93ejuKD8xk_veB7VvYWTME3p3W_BjLjZWjZeFZcaQx1M9kNl1uQbPJ5vTevGonpmWnUYHI8zW90Kiq53kFT95TUaPIP6TQLT-b2--T5tfUgkvpzRsHGl2vwSuEUtXpmYvqFKyezqa3ZGzfjBSDEmqDIKgejuPhqT9DXhqMT81-NmqxHGXkn6NJUTKjXi6-v9VIcThVAh5JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb51233478.mp4?token=YuQhY0zbEcuPbfUOAAem1BH6LUNbAZcep7fNC8uY7VKXpwrXHagddLpLXs9XsW19WbnJ5L_rPDk4rIz2Fls3xMb2Z5ivGi-bRpVfVi5MPf4ofFSBOkUPH_0Xh0WCmH07-VWAU45q8DE93ejuKD8xk_veB7VvYWTME3p3W_BjLjZWjZeFZcaQx1M9kNl1uQbPJ5vTevGonpmWnUYHI8zW90Kiq53kFT95TUaPIP6TQLT-b2--T5tfUgkvpzRsHGl2vwSuEUtXpmYvqFKyezqa3ZGzfjBSDEmqDIKgejuPhqT9DXhqMT81-NmqxHGXkn6NJUTKjXi6-v9VIcThVAh5JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
إنفجار كبير في محطة للغاز بمدينة زوليا الفنزويلية.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/75455" target="_blank">📅 20:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75454">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
حدث أمني غير عادي جنوب لبنان ويصنّف على أنه خطير جدًا.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/75454" target="_blank">📅 20:04 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75453">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/defed828a2.mp4?token=W5uOjUbFlhvTOn1V4oAunYzCljOJbasgtMlDGRf0oi6Wdn1gsVJFw1NkJqmdt4RzBxVnYEEaXCIDt-L_UUFiYvDV8X5LckLwniGIvhdO6emShtMG-Y4LEsWVSsm5kmng2cAh59ytYZAeS0I7isBjfaRNun-3xvQn-YRtJ66kouLN-oyDtkMtuzBXhFkD47Whj1PwFh13Ps9vkGDfb8b7l4zec9hqlOIZa6KXgWj5c9y0GUcKBK9rhjrUj3jgnOogK_LNG-M3vKpuhrh7RUaB0wA-50rgIq0KPRweMDo412y_9Y6VQwp6ttPpCxQ9Lj3tLm8St1aIJYHpGvvK_rZfkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/defed828a2.mp4?token=W5uOjUbFlhvTOn1V4oAunYzCljOJbasgtMlDGRf0oi6Wdn1gsVJFw1NkJqmdt4RzBxVnYEEaXCIDt-L_UUFiYvDV8X5LckLwniGIvhdO6emShtMG-Y4LEsWVSsm5kmng2cAh59ytYZAeS0I7isBjfaRNun-3xvQn-YRtJ66kouLN-oyDtkMtuzBXhFkD47Whj1PwFh13Ps9vkGDfb8b7l4zec9hqlOIZa6KXgWj5c9y0GUcKBK9rhjrUj3jgnOogK_LNG-M3vKpuhrh7RUaB0wA-50rgIq0KPRweMDo412y_9Y6VQwp6ttPpCxQ9Lj3tLm8St1aIJYHpGvvK_rZfkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
على الرغم من محاولات الإعتراض.. مسيرة أطلقت من لبنان تصيب هدفها في كريات شمونة واعمدة الدخان ترتفع.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/75453" target="_blank">📅 19:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75452">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eee05b77d.mp4?token=O6caa6aoRz7Tns73ElRESXL6S4CdgECuqwIL_mikrhRBX8Exi9ooE6XGR5iI70poaWexTNXhtVZmijb0CrCs-tfGDEqfRRVgnFBDthxmJWKMG1vlmcilU5oItjk1IKFci4kljfSvAu1amWwkJA4Bx8-QzKImndF005YBxyjqPWbrHa97smtHquAC98k6vDTbspw1nOuTneP1f9acktmf8BUDgSrQBMwPvaGGzBcUBIgHgDM1gyDr-06nxQIaZ2yN7XFkzmiD6dxmuoA8JZe0h4ni11ipg_P9VwNlno013f0hM8CGcawUfESzF9kO2zF--_cuTLTujH7kRP2-_mUr6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eee05b77d.mp4?token=O6caa6aoRz7Tns73ElRESXL6S4CdgECuqwIL_mikrhRBX8Exi9ooE6XGR5iI70poaWexTNXhtVZmijb0CrCs-tfGDEqfRRVgnFBDthxmJWKMG1vlmcilU5oItjk1IKFci4kljfSvAu1amWwkJA4Bx8-QzKImndF005YBxyjqPWbrHa97smtHquAC98k6vDTbspw1nOuTneP1f9acktmf8BUDgSrQBMwPvaGGzBcUBIgHgDM1gyDr-06nxQIaZ2yN7XFkzmiD6dxmuoA8JZe0h4ni11ipg_P9VwNlno013f0hM8CGcawUfESzF9kO2zF--_cuTLTujH7kRP2-_mUr6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
هجوم مركب جديد.. إطلاق طيران مسير ورشقات صاروخية من لبنان نحو مستوطنة المطلة بالشمال الفلسطيني المحتل.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/75452" target="_blank">📅 19:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75451">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇺🇸
ترامب:
لم أقلل من تقدير قدرة إيران على التحمل.
أبقينا على جسور إيران ومحطات توليد الكهرباء وبإمكاننا تدمير كل ذلك بالكامل خلال يومين فقط.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/75451" target="_blank">📅 19:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75450">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50710e6d35.mp4?token=nuDhARdT5eZ5g_BwC7c6AZQE-uPStVWsmgJqpnakCghCRiBldmbuhBECgXhS7PtgeJRNZsWq9_NpCMZilz6oELHk-hBc3TABeR4SJApjX9e6JuD3OCo568E6alfD4eGwWyx2v_4FeNttw-dF9mpMn9_VvSbROJ5XIF26cKx5XPwRHu_HsqWSfvxF3PCERvZ73u2gkM8UzHjy28Db9FWKtBO0qdDevvF-CcAbtwDSvVKksnzeIWTOTyjAHHBSBTqQBgIJQX6l5zgZ08CKdV2hTBtbKijBPk3a90hI92LLfUJM4djJNSjRIP2Tdt4DkNTIjX3X5Z8GZcT6cVicgYkhXSXgzQ4r5pz3d0C_7eSIjtMh7Q5kUpzk-3aLNytoLSTDJq44Cnoxos7sgMWJvy1oBaUq44MtvtoqeZMrnvoa80wlD-bND6IZ6GiCKZnzqK_Vx62y9B7qSElznRzkR-xaDHWg_oQF4Ih9cyr4d6TFsZELzEGrGbKWVJ4k9ebGO2Vslcpn4owVmOWtcxAR_f-xMO8AMJuKHWEPeuOrSlAvz9mTSRYs--BxcZir74RtWE1ebtXNWKpPvwRJxAKl6Sda_h9-CKTr-ACtGA6AznJNs7nQY3ivMfr1eIcjKSBASypQFfJYQ5_SO_bdQKEjZ0LSPNVcWK6K0g2rfiX7eHtMMGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50710e6d35.mp4?token=nuDhARdT5eZ5g_BwC7c6AZQE-uPStVWsmgJqpnakCghCRiBldmbuhBECgXhS7PtgeJRNZsWq9_NpCMZilz6oELHk-hBc3TABeR4SJApjX9e6JuD3OCo568E6alfD4eGwWyx2v_4FeNttw-dF9mpMn9_VvSbROJ5XIF26cKx5XPwRHu_HsqWSfvxF3PCERvZ73u2gkM8UzHjy28Db9FWKtBO0qdDevvF-CcAbtwDSvVKksnzeIWTOTyjAHHBSBTqQBgIJQX6l5zgZ08CKdV2hTBtbKijBPk3a90hI92LLfUJM4djJNSjRIP2Tdt4DkNTIjX3X5Z8GZcT6cVicgYkhXSXgzQ4r5pz3d0C_7eSIjtMh7Q5kUpzk-3aLNytoLSTDJq44Cnoxos7sgMWJvy1oBaUq44MtvtoqeZMrnvoa80wlD-bND6IZ6GiCKZnzqK_Vx62y9B7qSElznRzkR-xaDHWg_oQF4Ih9cyr4d6TFsZELzEGrGbKWVJ4k9ebGO2Vslcpn4owVmOWtcxAR_f-xMO8AMJuKHWEPeuOrSlAvz9mTSRYs--BxcZir74RtWE1ebtXNWKpPvwRJxAKl6Sda_h9-CKTr-ACtGA6AznJNs7nQY3ivMfr1eIcjKSBASypQFfJYQ5_SO_bdQKEjZ0LSPNVcWK6K0g2rfiX7eHtMMGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
06-05-2026
نقطة تموضع تابعة لجيش العدو الإسرائيلي في بلدة الطيبة جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/75450" target="_blank">📅 19:30 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75449">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🌟
🏴‍☠️
هجوم مركب جديد..
إطلاق طيران مسير ورشقات صاروخية من لبنان نحو مستوطنة المطلة بالشمال الفلسطيني المحتل.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/75449" target="_blank">📅 19:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75448">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/274d153e34.mp4?token=Mbf0URayl2pi4nEwByopOFjbiZqNw-O6LSzVZaGxXA5moTdHRLvINTwlNe63l571lj-xKUU5ADB2H3iZpQj8re-L_Bl5wKWSAfMQyRMeWq-xc9ZyOPx-w3Bzscx5f0W4OpVj35As2sTHvmY61zC50bhHVmoQVOi7b6X6O_NAxk6_dNa_34F0ipl7HFSugbj5y9c2MYXGIq1_XJhd0LvSYHb9nabIrv-og5CDcD9ukDZWOMEvEUP-4CvtqfgOq-W_Z1hSJ9MZJd1-WrYxTqrmmXBsH0eDmOMEUTdvs4cH5su4ApOWisdrxi97ZIxyguRX8hppjYU-lDOaqDXkIDWbBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/274d153e34.mp4?token=Mbf0URayl2pi4nEwByopOFjbiZqNw-O6LSzVZaGxXA5moTdHRLvINTwlNe63l571lj-xKUU5ADB2H3iZpQj8re-L_Bl5wKWSAfMQyRMeWq-xc9ZyOPx-w3Bzscx5f0W4OpVj35As2sTHvmY61zC50bhHVmoQVOi7b6X6O_NAxk6_dNa_34F0ipl7HFSugbj5y9c2MYXGIq1_XJhd0LvSYHb9nabIrv-og5CDcD9ukDZWOMEvEUP-4CvtqfgOq-W_Z1hSJ9MZJd1-WrYxTqrmmXBsH0eDmOMEUTdvs4cH5su4ApOWisdrxi97ZIxyguRX8hppjYU-lDOaqDXkIDWbBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
اندلاع حريق كبير في منطقة بتاح تكفا شرقي تل أبيب المحتلة.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/75448" target="_blank">📅 19:04 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75447">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzAYJq8iSwuUgppeOeM2RQeVabqyPwuqmCmIwh8KswmI1Bw-M9rnAHIjnzKOhJuBme6wkgcPdaV4nC6E9Dv0fPpLuHK5sXQidscTAzT6fslz5m3doPNZvBw5CjNmHbQq_mgpH7RPiaeCWd8wreaUfeFhMp3eWgHmsUiLWwY1S1Q5GRQybDgUD-yWpsRsSIJAnDUEqA51RL5V6pQIqYVRdOnSu7gkXgRUSdahMQTiydHDx__waHXv06JHm2iuhFKsFNNWgvSFSCXugcVa4_FAE2sHdQ1Ha3vIttuSaXIoGFFk4fDmgDXkSUwzlTqt51EDSvW-Dgk7V8cpSDg3-iDjEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
أسعار النفط العالمي تلامس 109 دولاراً للبرميل الواحد.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/75447" target="_blank">📅 19:01 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75446">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🏴‍☠️
هجوم مركب..
إطلاق أسراب من المسيرات ورشقات صاروخية نحو الشمال الفلسطيني المحتل وصافرات الرعب تدوي من رأس الناقورة إلى نهاريا.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/75446" target="_blank">📅 18:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75445">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XkHGwHlGcawFtQ8zJeVLkvVEMqtvTD06AbxIP_BxHnq8_3PQqbFXc4YeA45CvlIdQ8BX38FUnZh7uTQ_zgzmQoH3QIjfcHJY3LAvOeJE8RbP_jR9KyQaZUYPo8MWdCIGJ0EK9cIxe1L0GEjuizxLJR4OrSRd_NRWaK1JgNC-ASRA0r38OcNEqu4SrWlOIpEHmS4u2Qz3hVHfjyWLLqxbnRaKurNA9vDj_LDiSx6qoGzdJh2F8VLB3FljcNSlNXm2ewUNVKOxUcPAKsxM0trI0GX-HssqIdUMqnDR8GvTxdQWGIoNIJDxf6TUaZ3q_WtqfGkoU3OYYgkYHnaiAt3-FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود بزشكيان:
إذا ذهبَتْ إيرانُ فليذهبْ معها رُوحي وبدني،
ولا تبقَ في هذي الربوع نَسَمةُ حيٍّ أو نَفَسٌ لأحدِ.
‏خلّد الفردوسي، من خلال الشاهنامة، الهوية التاريخية والثقافية لإيران، ومنح البطولة معنىً مرتبطاً بالعدالة. واليوم، يُعدّ أبناء إيران حماة أمن هذا الوطن وعزته في وجه الظالمين.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/75445" target="_blank">📅 18:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75444">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22069c906f.mp4?token=czpDn4lY-HuaXDIriNdLUpTU4TqJpup0jLFgNqJIQS3ZZYXswF9uQFxMlXBku16yh0c5nyTUPinf-JGy4UzGZNQuZJa788VmLtoAd7bqEBz_mbGxNeTzp0n2-qMVtHtegI70U8E1BGaIqrHrMk-_Kued8EYH9tGpS1jDQf1HkvAFFdBaAdEw2a9gL4NvHn_wc_UlP-mlc-qvmg3xFpsu-anTLiibsqaLbdL2qE8dVZyiTNzAga0Zi7gwsggP9j8fn4HWpRAxJJM9em9icHcGHauGXqL8z2uTihdBQqdMZzkAeeB9iRV5qebOps6RdmCx0G5jcQ6g38Ls3lRr7IloNZiwtGiyJ4IOTl7nhj78uFOYd-zpNlc7sELUNlGvYsONsB92qEA6Evvj8e2lfUb_ICDG48XCqKpbOTEKtAxzVMrPw5lSbzM-sGcEBK8OGepgFDzo4FOVY2ccze55l_0tOfgS9CLFWMczfMoQcZVzt59v_iox3INUC4sR43vghqdYf1srBESaqkMGDduFRmBjm7JgJVI7kguYHBV8QL2zp2egQJpLwFfAP9seW4J78CQYR7jvHM03yOIcvUfZNmJ2eOA5gBUaOx5HD26252Qjy4nam12M6yuBAgij0bxlCW3aVsT_sVXVGZINFiv706kyhmzHp_mKNHfYr394pyHB5Ok" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22069c906f.mp4?token=czpDn4lY-HuaXDIriNdLUpTU4TqJpup0jLFgNqJIQS3ZZYXswF9uQFxMlXBku16yh0c5nyTUPinf-JGy4UzGZNQuZJa788VmLtoAd7bqEBz_mbGxNeTzp0n2-qMVtHtegI70U8E1BGaIqrHrMk-_Kued8EYH9tGpS1jDQf1HkvAFFdBaAdEw2a9gL4NvHn_wc_UlP-mlc-qvmg3xFpsu-anTLiibsqaLbdL2qE8dVZyiTNzAga0Zi7gwsggP9j8fn4HWpRAxJJM9em9icHcGHauGXqL8z2uTihdBQqdMZzkAeeB9iRV5qebOps6RdmCx0G5jcQ6g38Ls3lRr7IloNZiwtGiyJ4IOTl7nhj78uFOYd-zpNlc7sELUNlGvYsONsB92qEA6Evvj8e2lfUb_ICDG48XCqKpbOTEKtAxzVMrPw5lSbzM-sGcEBK8OGepgFDzo4FOVY2ccze55l_0tOfgS9CLFWMczfMoQcZVzt59v_iox3INUC4sR43vghqdYf1srBESaqkMGDduFRmBjm7JgJVI7kguYHBV8QL2zp2egQJpLwFfAP9seW4J78CQYR7jvHM03yOIcvUfZNmJ2eOA5gBUaOx5HD26252Qjy4nam12M6yuBAgij0bxlCW3aVsT_sVXVGZINFiv706kyhmzHp_mKNHfYr394pyHB5Ok" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بالفيديو | مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
10-05-2026
آلية هندسية (D9) تابعة لجيش العدو الإسرائيلي عند خلّة الراج في بلدة دير سريان جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/75444" target="_blank">📅 18:01 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75443">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">وزير الخارجية الباكستاني:
إعادة 11 باكستانيا و20 إيرانيا اختطفوا على متن سفن سيطرت عليها قوات ألامريكية.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/75443" target="_blank">📅 17:54 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75442">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pM4ZQ71gdm5QTUWTMFmx_Z4WRKuNArPrBCRUDv2bg38NWvKCXa05RDgBumZvBO9eBWUABFXEcuNHL16wOd7x2YgaDHbZE1P92CkRO7pqtbFj3TbfuKPsTwyVXJE2venbRhcuD-eVNb1dkZS8UDo2GDJd04uVcgVzCnEL_a44hCreDXFwvxo7co5RugNhJX9R-kRFmLtAo3Bebkx8YMHV8wP8BKPd-6N1WCinIx9s6-uMadMYBlUvlNNOqv3Dva6u8-C9Uq5d1EaTl8an-WdBsH7qslLToeIZMoLl57d1fyh6S9ldmQYZBs5dCQFP9u9tfEhwRUDkhy9NLZ99x9LKLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفعيل الدفاعات الصهيونية بالقرب من طبريا</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/75442" target="_blank">📅 17:00 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75441">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🤺
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 12-05-2026 آلية هندسيّة تابعة لجيش العدو الإسرائيلي في بلدة طيرحرفا جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/75441" target="_blank">📅 16:54 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75440">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">وزير الطاقة الأمريكي رايت: أعتقد أن الصين ستكون أكبر مشتر للنفط الخام الأمريكي</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/75440" target="_blank">📅 16:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75439">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‏ترامب: لم أرغب في وقف النار مع إيران وفعلت ذلك كخدمة لباكستان
اشرب جايك لا يبرد
😄</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/75439" target="_blank">📅 16:04 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75438">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">📰
مراسل صحيفة نيويورك بوست:
‏قبل صعودهم على متن طائرة الرئاسة الأمريكية "إير فورس وان" لمغادرة بكين، قام الوفد الأمريكي بأكمله بإلقاء كل ما قدمه لهم المضيفون الصينيون - من هدايا وشارات ودبابيس وأشياء تذكارية - في سلة المهملات الموجودة في الموقع. ‏لم يصعد على متن الطائرة أي شيء من أصل صيني. ‏كان الوفد قد ترك أجهزته الشخصية في المنزل واستخدم هواتف محمولة نظيفة طوال الرحلة.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/75438" target="_blank">📅 15:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75437">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سوالف الگهوة
وزير ادّعوا " انه لم يصوت عليه البارحة سوف يعود بقوة القضاء العراقي المستقل ، العامري الزيدي ورجل معهم حكيم اجتمعوا البارحة عند المالكي ليلاً …</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/75437" target="_blank">📅 15:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75436">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe5ac0cea1.mp4?token=s7D13QZDotFZ0b6cNolg1yQri5ViEg6HL0qZQE0sWk53aANV7wB6t6x5esFOzd0YfQYovPHIeKFRvmr2_YEyW6G1AsniLPW0nlvmJKEO03_m4u3Be0_N9jO5-VD3Fs5uSlb8aPWrY-JDglUm06TBOnO7n5iBq6ipaoST4MT_fLyRwpuXBNyBbk464QkuKSIL0m_IBx1bHa5cZg85887FBxt3BUuahGZKYruh_DuRjHzvRccHF9AGnx9fC5fvEnJ1eUvX3V1LTAvk3pLtboPX3ia9rb231AJyjnq_h3v6O9fDhCYQ18pn_ljey2oYjs1DVCdSHvCH2zyldHIt_C94Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe5ac0cea1.mp4?token=s7D13QZDotFZ0b6cNolg1yQri5ViEg6HL0qZQE0sWk53aANV7wB6t6x5esFOzd0YfQYovPHIeKFRvmr2_YEyW6G1AsniLPW0nlvmJKEO03_m4u3Be0_N9jO5-VD3Fs5uSlb8aPWrY-JDglUm06TBOnO7n5iBq6ipaoST4MT_fLyRwpuXBNyBbk464QkuKSIL0m_IBx1bHa5cZg85887FBxt3BUuahGZKYruh_DuRjHzvRccHF9AGnx9fC5fvEnJ1eUvX3V1LTAvk3pLtboPX3ia9rb231AJyjnq_h3v6O9fDhCYQ18pn_ljey2oYjs1DVCdSHvCH2zyldHIt_C94Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب يهاجم ‏مراسل بي بي سي بعد ان سأله عن القصف الامريكي الذي استهدف مدرسة ميناب الايرانية
‏
س: سُئل الأدميرال كوبر أمس عن الإضراب الذي استهدف مدرسة البنات--
‏ترامب: حسناً، الأمر قيد التحقيق
‏س: هل يمكنك تأكيد أنه صاروخ أمريكي؟
‏ترامب: مع من أنت؟
‏س: بي بي سي
‏ترامب: بي بي سي مزيفة. هل تقصد أولئك الذين وضعوا الذكاء الاصطناعي في فمي؟</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/75436" target="_blank">📅 15:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75435">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">انسحاب الاسدي والغراوي رسميا من السوداني</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/75435" target="_blank">📅 15:18 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75434">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2Lh4ZXcE4PGSl6L3n6TI6M3YmZez93iMTWBADyPjYL7ZQO6Py7bobJT8cGmN3pAKxfmzhCDZAmWNA4MsC95ZY7blAwZgHFIVV4O9WMAuZ2VOMaU7zbpAXHkMlt3EGNhz3Mnd1vLNMlVUrVHSN1zuf97HeovzUztcCR8HKxakmpniqygRrjmdPrZkeJeecZv2z7HYJWUoNfSYv9hfrBRvp7YdKKAeIfFzE5OTN1pY8JXPo2fow6KXVeP28edNnh-UEZlq9kOU4_HdOFpqxHlKSGRCqub79gSN0KDp-UBX3MIThdHK2f3f39VbAL1JzLkMpQ4JIndtVATJ2t0FEooUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوالف الگهوة   رسالة من ابو علي بوتين للعراق …</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/75434" target="_blank">📅 15:14 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75433">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5Jx9Semr0b_7nMl7u2BBB07gYCQ4aZSDVyQqd1_NjnxkiN-5XO9QpNiNvpiIaTMafLGWssT4MU64Syz9167KZh5p2BBKKjUYriCeM-zSp6JQUC18EXJfnUrZpZc8Hx-jHWuPZybSveNopNGHah8JKo6K7QrowPCJNNosV9Dw7UZPWlOtioko_ixFLmZvc6rye6ekqbrbHjie7HnA9Yr93pkxcgVvu-FYDVl7P3o2MLkEIh7yLzRX4b5hmdzl5GEmOuviXSohcwYk_t0N5jTzbPitMNOkazLsG-mSQhAsFGkTVVp28nUCBIdl1q8B5evYjzkwF4oaIWRFYfzVPFUaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
وزير الخارجية الايراني:
إن مقاومة إيران للتنمر الأمريكي ليست معركة غريبة. فكثير منا يواجه أشكالاً مختلفة من نفس الإكراه البغيض. لقد آن الأوان لنا أن نتكاتف ونعمل معاً على توضيح أن هذه الممارسات يجب أن تُطوى صفحتها إلى الأبد.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/75433" target="_blank">📅 15:11 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75432">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">سوالف الگهوة
رسالة من ابو علي بوتين للعراق …</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/75432" target="_blank">📅 15:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75431">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‏ترامب: لقد أجريت اتصالات مع كيم جونغ أون، زعيم كوريا الشمالية</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/75431" target="_blank">📅 14:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75430">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‏ترامب: سأتخذ قراراً خلال الأيام القليلة المقبلة بشأن رفع العقوبات المفروضة على شركات النفط الصينية التي تشتري النفط الإيراني.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/75430" target="_blank">📅 14:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75429">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‏ترامب: "الغبار النووي" الإيراني قد يُسلّم إلى الصين أو الولايات المتحدة</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/75429" target="_blank">📅 14:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75428">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامب: آخر ما نحتاجه الآن هو الحرب.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/75428" target="_blank">📅 14:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75427">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‏ترامب: لا امانع في تعليق إيران لبرنامجها النووي لمدة 20 عاماً، لكن يجب أن يكون ذلك التزاماً حقيقياً</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/75427" target="_blank">📅 14:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75426">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">مصدر لنايا  يتحدث عن خروج كتلة العقد الوطني من ائتلاف الاعمار والتنمية بسبب ما حصل من ممارسات سيئة في جلسة منح الثقة للحكومة الجديدة  اليوم</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/75426" target="_blank">📅 14:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75425">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dH_jGStcrkrc76eUbilV0zBUgiG-faQ5taxZoNjK9igu8Mbh93mmtmM4OmeNcAzRWigIGP7IzTwr0jhaf1d3Ic5sXnlZNImjoq5WcWJb1VFgbKrWYOIsEy8hIJMMoRJnZSD297UG7TQQFvOOXbjcLYRPAZh5l8ZE-hWTs0neHiEEH3BHPedzACyMvNm1ONANZQxlLN8oZJRNhiMZpG-wJ-421ZI9mHZrFDihC8EgdQ4qguj6jMKKcAdHgdgjhRCFllQXuc7XvrbYTxWoD2pxAp9bsPFtCGv7Lb9jHzzzsoqNDHOaJycX01oLVteNisZcsfxn8sXzvB8qapo4q3p-RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدر لنايا  يتحدث عن خروج كتلة العقد الوطني من ائتلاف الاعمار والتنمية بسبب ما حصل من ممارسات سيئة في جلسة منح الثقة للحكومة الجديدة  اليوم</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/75425" target="_blank">📅 14:19 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75424">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ترامب: لم أقدم أي تعهد بشأن تايوان.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/75424" target="_blank">📅 14:16 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75423">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامب للصحفيين: لا أعتقد أن هناك خلافًا مع الصين بشأن تايوان</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/75423" target="_blank">📅 14:11 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75422">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامب بعد اختتام زيارته للصين يقول لفوكس نيوز حول تايوان: لا نتطلع إلى خوض حروب</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/75422" target="_blank">📅 14:11 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75421">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامب بعد اختتام زيارته للصين يقول لفوكس نيوز حول تايوان: لا نتطلع إلى خوض حروب</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/75421" target="_blank">📅 14:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75420">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‏بيان لقائد الثورة الاسلامية آية الله السيد مجتبى خامنئي بعد قليل</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/75420" target="_blank">📅 14:03 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75419">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVyPvKDQfzb8eRi8J9ZaBYPK5-9n3yhP8R-ACFHHkifQ-31a8h7zdyyAW5lo-TtwnzmC3mWAqZGwz3yPR5SD58ih_pJcJ4YTu8QEM-Yuc06_8bRRapi02dfxiV2VZE_oidEenus9JTHjsHoUtOoZNENAqn4qztTxD5iuQ7bCay0xWgoPtqqikzyXYIYP2ubYrd0DwqQkSGBuvFcqhNO4uAJewdSBIKUpzrqvuwQ1n9Jbe2Si8lMZCgmN8SiHeumnqJKe7jX7hBD1gUgPN9R5YZJcsv55-hxrzKz7bnoHsFafKYvI3CyK3ArK04wHEIzTqyJYCzTnC2-j_eG7-6IfVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامب: ‏الصين لديها قاعة رقص، ويجب أن يكون لدى الولايات المتحدة الأمريكية قاعة مماثلة! إنها قيد الإنشاء، وتسير بوتيرة أسرع من المخطط لها، ‏من المقرر افتتاحها في سبتمبر من عام 2028 تقريباً. الرجل الذي أسير معه هو الرئيس شي جين بينغ، رئيس الصين، أحد أعظم قادة العالم!</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/75419" target="_blank">📅 13:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75418">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏بيان لقائد الثورة الاسلامية آية الله السيد مجتبى خامنئي بعد قليل</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/75418" target="_blank">📅 13:41 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75417">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j73EmlqNkRy5Pe-5CPweRPLnl64-lk-_k0cLzHExTXBVqkSLH4zEkDz0BMPK1XJfMaIB7pWwH6yVgOcpFaCYRqbuQkh-yhOuXf6GoslFzDpDB1XGY7-JEcRxu21RHJlb7-88smqpo9VafwZkpJvk4GZAKEkA-HR3lNEr41UQi1ea7NPXVjhhX_ChLXUv47Cl90VNVvC0IArc8tGaFyyTRcdPBDQwtdRfKg-k25pU2IKAp31eaIeUz2E8iaaOEmOM2BaQLp5Hhts39s4i8CJ63-3Gu1TY-dWQ_Dg6TuVh3fcutAmGL50sZU0zizxl9Nan7HI8D6lP8Z3fz1ZTRSWWKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
الرئيس الايراني مسعود بزشكيان يهنئ رئيس الوزراء العراقي بمناسبة نيل الحكومة ثقة البرلمان</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/75417" target="_blank">📅 13:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75416">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇷
وزير الخارجية الإيراني:
- وقف إطلاق النار هش للغاية
- لا يوجد حل عسكري فيما يتعلق بأي شيء له علاقة بإيران
‏- نحن مهتمون بالتفاوض فقط إذا كان الطرف الآخر جاداً
- لا‏ نثق بالأمريكيين
- نحن لا نريد أسلحة نووية، وهذه ليست سياستنا، لدينا برنامج نووي سلمي
‏- يُسمح لجميع السفن بالمرور عبر مضيق هرمز باستثناء السفن التي تخوض حربًا مع الولايات المتحدة
‏- إيران مهتمة بمواصلة أعمال الطاقة والنفط مع الهند
‏- اتفق مع الولايات المتحدة على تأجيل المفاوضات بشأن المواد المخصبة
- الرسائل المتناقضة جعلتنا مترددين بشأن النوايا الحقيقية للأمريكيين في المفاوضات</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/75416" target="_blank">📅 13:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75415">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">استهداف دبابة صهيونية في بلدة رشاف جنوب لبنان بمسيرات حزب الله</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/75415" target="_blank">📅 13:00 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75414">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بلومبرغ:
الإمارات حاولت عبثاً حثّ السعوديين على تنسيق الرد على إيران لكنها شعرت بالإحباط عندما قوبل طلبها بالرفض
في حين سارع محمد بن زايد إلى التعاون مع إدارة ترامب والإسرائيليين أبلغه نظراؤه الخليجيون أن هذه ليست حربهم
الإمارات نفذت هجمات محدودة ضد إيران من دون دعم من دول الخليج بدءاً من أوائل مارس ومرة أخرى في أبريل</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/75414" target="_blank">📅 12:55 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75413">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🌟
حزب الله: مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 12-05-2026 تجمّعات لجنود جيش العدو الإسرائيلي في جنوب لبنان بالصواريخ والمسيّرات الانقضاضيّة.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/75413" target="_blank">📅 12:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75411">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/971b1df4d5.mp4?token=jUStYAvvLH6-Clp3KPCHqWU8mw88kt7EZ9f3o_6iIPI3IMQtDulZXyWet-RBmL3w7FXNA17Brh4p_gA8N3YXX1rkA_z6FUG4W74xLD3zE6XmOwVeim7y8PIm5KInPxXwjOgW12lc735q1qWB-OFU75NPXl7IF6WM3Nf9178pQYKA90sPWuIiyfF_NhbwXAui3rdXbQgHtw6f6M54F1yf6__QgnPK3Z-jCzejmCCF5bgO--H6OX4jpBlm6trL1yoHcYT_l-c_UbGsBz70CMbAjeV9lk_GJQOYgSWkfruxvy0sMlWXmGhyQmoySs9vnn7ugwhU9Uq1WnUeYPaPrLhvcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/971b1df4d5.mp4?token=jUStYAvvLH6-Clp3KPCHqWU8mw88kt7EZ9f3o_6iIPI3IMQtDulZXyWet-RBmL3w7FXNA17Brh4p_gA8N3YXX1rkA_z6FUG4W74xLD3zE6XmOwVeim7y8PIm5KInPxXwjOgW12lc735q1qWB-OFU75NPXl7IF6WM3Nf9178pQYKA90sPWuIiyfF_NhbwXAui3rdXbQgHtw6f6M54F1yf6__QgnPK3Z-jCzejmCCF5bgO--H6OX4jpBlm6trL1yoHcYT_l-c_UbGsBz70CMbAjeV9lk_GJQOYgSWkfruxvy0sMlWXmGhyQmoySs9vnn7ugwhU9Uq1WnUeYPaPrLhvcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم بالمسيرات يستهدف مقرات حزب الحرية الإرهابي في محافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/75411" target="_blank">📅 11:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75410">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f7e67fea4.mp4?token=LDKiS9g8FHMMB1UPxnw805Wpa7DaJnuCcJbmYMGKftr4ug4zeUQ_h5jIv8m_zyA-vdaXnaZt3iHPr2sHiD7OMrWEzUd3VxIhcH5jESE3oWdhKDEgLczEPu7TMGrs_zzR8wPHg8T8CsxDmjCmcc5kTBYoXDRZ_B78Z8Zd5sJtMmlMNuqoGvJp3J6Huq3EzOupvDdggiQno_tueMHdHFyNBXf_IxfL0ATrrFVpaDeYTUrFwiQFOX-OEQooLNIIiisPio-SOMcSZ8R3Js3p2R9FaV2-0k2xNdwaOGJlfcn5PSZIZBdS1ls1HYhwoUy2YViiQ5zIW9-mt6oeudNDy4DWYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f7e67fea4.mp4?token=LDKiS9g8FHMMB1UPxnw805Wpa7DaJnuCcJbmYMGKftr4ug4zeUQ_h5jIv8m_zyA-vdaXnaZt3iHPr2sHiD7OMrWEzUd3VxIhcH5jESE3oWdhKDEgLczEPu7TMGrs_zzR8wPHg8T8CsxDmjCmcc5kTBYoXDRZ_B78Z8Zd5sJtMmlMNuqoGvJp3J6Huq3EzOupvDdggiQno_tueMHdHFyNBXf_IxfL0ATrrFVpaDeYTUrFwiQFOX-OEQooLNIIiisPio-SOMcSZ8R3Js3p2R9FaV2-0k2xNdwaOGJlfcn5PSZIZBdS1ls1HYhwoUy2YViiQ5zIW9-mt6oeudNDy4DWYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم بالمسيرات يستهدف مقرات حزب الحرية الإرهابي في محافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/75410" target="_blank">📅 11:14 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75409">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇮🇷
وزير الخارجية الإيراني: هذا هو الوقت الذي يجب فيه على إيران أن تثبت موقعها وتبرز دورها الإقليمي أكثر من أي وقت مضى</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/75409" target="_blank">📅 10:19 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75408">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8ecb192c7.mp4?token=vFJ4_aPR2MZkeEDpCaCny3zbpLOW7o8ENMxn6SfDrDY2uJQThvgD9BeaweeEK94PlqGDAzmdEdiQsasgHMAWKNx5xdAnBnigJHi6ec3TVc3OBTuNTfr_2iJlO3x5F_k1o6uHfblQppnv23jmb21li2cgeDaiaMMpz_pl2i4pbG871PEtPiPyTb1r9GFKgV1QWdLNZWI977_FmB1CkSsXtF2ivsCNfacXHJdfpRcnPPanIvgXNSnLYaqVg7Q9Kygp81-tgh5hrDYCUsRMBM_Ir19q9eTu8SSwkS-6r4qG9cA3rk1SjSB1uDnf3D1WdPUMDow7OCwhXYLf9dxKc6MexA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8ecb192c7.mp4?token=vFJ4_aPR2MZkeEDpCaCny3zbpLOW7o8ENMxn6SfDrDY2uJQThvgD9BeaweeEK94PlqGDAzmdEdiQsasgHMAWKNx5xdAnBnigJHi6ec3TVc3OBTuNTfr_2iJlO3x5F_k1o6uHfblQppnv23jmb21li2cgeDaiaMMpz_pl2i4pbG871PEtPiPyTb1r9GFKgV1QWdLNZWI977_FmB1CkSsXtF2ivsCNfacXHJdfpRcnPPanIvgXNSnLYaqVg7Q9Kygp81-tgh5hrDYCUsRMBM_Ir19q9eTu8SSwkS-6r4qG9cA3rk1SjSB1uDnf3D1WdPUMDow7OCwhXYLf9dxKc6MexA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇶
🇮🇷
قائد القيادة المركزية الأمريكية
قال امس في مجلس الشيوخ " رئيس الوزراء العراقي الجديد تعهد لنا بإبعاد نفسه عنّ ايران "</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/75408" target="_blank">📅 10:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75406">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7lFrjcfah00MyrXRvvHgPISCaYnL6l6eMNKA17y8WA9PD8zMXatTPXRkfDC1-7mNPaFqdih_hlsX2fpOcvRgDQlt_nUm8jfc6zDmjQm0WYdvuSU5Fku2ulHE1Xw1d6PFawcbeIF_UxMfHPl1YpwMzJr04iEqiVDhn24JGeuaUybMDcCF8GtFKbcNRYPrIpyGNrM1a4HYxfEIEjnbPqSn3lGhFdIcJhPNNwzKDtnsJfJmCMryrl9zv7fk2-FV21ajDZeLhbuDgX1SYT5FEccpwB4mKyQNNfLYwuIVJ0kr1SVtQ9wiovVgzLHf221MbZus4GuBunwZYRSKJDYzFLRWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترمب
عندما أشار الرئيس شي بأناقة شديدة إلى الولايات المتحدة على أنها ربما تكون دولة متراجعة، كان يشير إلى الضرر الهائل الذي عانى منه بلدنا خلال السنوات الأربع لجو بايدن النائم وإدارة بايدن، وعلى هذا الصعيد، كان على حق 100٪. عانى بلدنا بشكل لا يُقاس من حدود مفتوحة، وضرائب مرتفعة، والجنسانية للجميع، والرجال في الرياضات النسائية، وDEI، وصفقات تجارية فظيعة، وجريمة متفشية، وأكثر من ذلك بكثير!
لم يكن يشير الرئيس شي إلى الارتفاع المذهل الذي أظهرته الولايات المتحدة للعالم خلال 16 شهرًا مذهلة من إدارة ترامب، والتي تشمل أسواق الأسهم والـ 401K في أعلى مستوياتها على الإطلاق، والانتصار العسكري في فنزويلا، والتدمير العسكري لإيران (سيستمر!) - أقوى جيش على الأرض إلى حد بعيد، وقوة اقتصادية كبيرة مرة أخرى، مع استثمار 18 تريليون دولارًا أمريكيًا في الولايات المتحدة من قبل الآخرين، وأفضل سوق عمل في التاريخ الأمريكي، مع عدد أكبر من الأشخاص الذين يعملون في الولايات المتحدة الآن من أي وقت مضى، وإنهاء DEI المدمر للبلاد، وأشياء أخرى كثيرة سيكون من المستحيل سردها بسهولة. في الواقع، هنأني الرئيس شي على العديد من النجاحات الهائلة في مثل هذه الفترة القصيرة.
قبل عامين، كنا في الواقع دولةً متراجعة. وعلى هذا، أنا أتفق تمامًا مع الرئيس شي! لكن الآن، الولايات المتحدة هي الدولة الأكثر سخونة في أي مكان في العالم، ونأمل أن تكون علاقتنا مع الصين أقوى وأفضل من أي وقت مضى!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/75406" target="_blank">📅 01:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75405">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c66844eb9.mp4?token=obcV4jN2N7T51bTauV35NIV0U8TabJF3-xOmmwrrfq4oDnRXSZXOjLb-f1VdaqD56ip3e-Ih9VwV4jzapx1czSRljFN6kBVy3yAHI0OdSH-P6frqYYEMivKlZDpYUPgfs6QgfsNN61_V4WW9m-PHlblCDzESsSANF8nxBSv7jlh7fbP05r1xCe-21ESliF2UEZT8NYmJFtGkB_4b0DIh__3p3P4WkwoSky6qIbenlwzO6m8K9aMmEGVdLnqCF2qxjWAAmt2HvNL8DvBnXtvGtFCsbGp4BYTBMTrynzebP5aWnfz5QZYWwQdnvLXzS-_ml5DoDUNVj3J923HKStW3Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c66844eb9.mp4?token=obcV4jN2N7T51bTauV35NIV0U8TabJF3-xOmmwrrfq4oDnRXSZXOjLb-f1VdaqD56ip3e-Ih9VwV4jzapx1czSRljFN6kBVy3yAHI0OdSH-P6frqYYEMivKlZDpYUPgfs6QgfsNN61_V4WW9m-PHlblCDzESsSANF8nxBSv7jlh7fbP05r1xCe-21ESliF2UEZT8NYmJFtGkB_4b0DIh__3p3P4WkwoSky6qIbenlwzO6m8K9aMmEGVdLnqCF2qxjWAAmt2HvNL8DvBnXtvGtFCsbGp4BYTBMTrynzebP5aWnfz5QZYWwQdnvLXzS-_ml5DoDUNVj3J923HKStW3Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتفاع أعمدة الدخان من داخل مقر رئاسة الوزراء في ليبيا، عقب اشتباكات عنيفة بين مشجعي أحد الأندية الرياضية امتدت إلى محيط المقر الحكومي.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/75405" target="_blank">📅 01:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75404">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">مصدر لنايا  يتحدث عن خروج كتلة العقد الوطني من ائتلاف الاعمار والتنمية بسبب ما حصل من ممارسات سيئة في جلسة منح الثقة للحكومة الجديدة  اليوم</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/75404" target="_blank">📅 00:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75403">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇮🇷
🇮🇶
عراقجي يهنئ بتشكيل الحكومة العراقية الجديدة.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/75403" target="_blank">📅 00:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75402">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">مصدر لنايا  يتحدث عن خروج كتلة العقد الوطني من ائتلاف الاعمار والتنمية بسبب ما حصل من ممارسات سيئة في جلسة منح الثقة للحكومة الجديدة  اليوم</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/75402" target="_blank">📅 23:48 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75401">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWAavsH_3S5dUKdrPumS3-px2cGL-onB28kP1FPlUJyjcWTpc8KnputTHzL2AEcwDUlvOrkV4VvmQdLgcadSMefrzEBOLdQWYbArraPdCkTANTT8klsELKzf4V1VV9g5EYWmKjgCZCcf08UiQ9jSvkfPjDEfo-NRCMFW1EOotigIwrK0Fhxdaa6D6DWlK5zUwtMbcUvVjVMt_5DuAeokmLeR1JV1-NN0RXOLZRovv1468AicspNYIfocwA_edpNtTt7GLzEact_FlGtwdgVYVQKv5WCAgXblRPSC9_73w5muwRahKjv2sZshsMW7K1tCpHuJB6wOOLyOoFFdO0chVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدر لنايا  يتحدث عن خروج كتلة العقد الوطني من ائتلاف الاعمار والتنمية بسبب ما حصل من ممارسات سيئة في جلسة منح الثقة للحكومة الجديدة  اليوم</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/75401" target="_blank">📅 23:37 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75400">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مصدر لنايا  يتحدث عن خروج كتلة العقد الوطني من ائتلاف الاعمار والتنمية بسبب ما حصل من ممارسات سيئة في جلسة منح الثقة للحكومة الجديدة  اليوم</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/75400" target="_blank">📅 23:31 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75399">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ViKqHmS5mpi30p8Li3KzyMA2hS5ZclExrbYvExUBU8ZoCxI-vpPnipS41ozpw-73-zaYLhneVhNWOC3VqNWMMXM7qZ8JemzFz_rNJS7x_3MFZUAaL0fqRAh3orQNRXLyHyAFsGlGPOtD3U3ru68gYnMqRQsyrEYkFtCnkwtY8WWqA9K8DHKOXkTPKrGXp_ABr6RGOZSjMKoc7GrY_D0TFpgYUU1keDaurPtnKseSzw7xzBoqc6p3X-6ZUn-EvI2wkf8VArWmeWe3jcb8Y1t-fimdsbF6D832mukz4mdxcUThImptbgQJUXCIlC23stj13MfJXB_w0cu5hNVSPwYrjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف:
إذن أنت تمول هيغسيث مقدم البرامج التلفزيونية الفاشل، بمعدلات لم يسمع بها أحد منذ عام 2007، حتى يتمكن من تقمص دور وزير الحرب في فناء منزلنا الخلفي في هرمز؟
هل تعلم ما هو أكثر جنوناً من 39 تريليون دولار من الديون ؟ دفع علاوة ما قبل الأزمة المالية العالمية لتمويل لعبة تقمص أدوار حية، وكل ما ستحصل عليه هو أزمة مالية عالمية جديدة تماماً</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/75399" target="_blank">📅 23:29 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75398">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">#سمح_بالنشر
.. مشاهد من إستهداف أبطال المقاومة الإسلامية في العراق
#رجال_البأس_الشديد
أهداف حساسة في عمق
الكيان الصهيوني
الغاصب
بعدد من الطائرات المسيرة حيث حققت إصابات دقيقة ومباشرة .</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/75398" target="_blank">📅 23:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75396">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc00397ad.mp4?token=QPIrdHQSwMM3_5UzoVCEWgjaStT6xwQEZYZvKqcdN509AuDqhtf5hBomJ-IMUMXjs_j0r81rQNLB3N7TwS-69cvatZDGvSBh6jscRnxqv3kyBjwClBSrc4zmZffPJJkrd4R8V7eMd2MwlNBbJm9AJ909tnbz4l7CCigqYjs7qd3g379esmuc8aEpH0L1RcPkhX3Scze11Y3olkvr18DGNW-Y8-5F9BtMR40OEIokopvSq55GqXEuoxPyVs8bO_O2zw4Unv3CXVYEtyfyyRdJUXzMJjEdSLklUb5nP3L3EUks5wnzbJHdIQK9Pm786GcKjFPV3nwTtJB3ovoNgY3rcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc00397ad.mp4?token=QPIrdHQSwMM3_5UzoVCEWgjaStT6xwQEZYZvKqcdN509AuDqhtf5hBomJ-IMUMXjs_j0r81rQNLB3N7TwS-69cvatZDGvSBh6jscRnxqv3kyBjwClBSrc4zmZffPJJkrd4R8V7eMd2MwlNBbJm9AJ909tnbz4l7CCigqYjs7qd3g379esmuc8aEpH0L1RcPkhX3Scze11Y3olkvr18DGNW-Y8-5F9BtMR40OEIokopvSq55GqXEuoxPyVs8bO_O2zw4Unv3CXVYEtyfyyRdJUXzMJjEdSLklUb5nP3L3EUks5wnzbJHdIQK9Pm786GcKjFPV3nwTtJB3ovoNgY3rcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إطلاق رشقات صاروخية من لبنان نحو كريات شمونة ومحيطها في الشمال الفلسطيني المحتل والدفاعات الصهيونية تحاول الإعتراض.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/75396" target="_blank">📅 22:53 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75395">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87449a5631.mp4?token=b7aiGB72O8TupF3BEDlMutbCgn57_O6ZU_sdD50r0l0QjUaAJcdroJY1W98adm-JbJin38_0-7FwFwlcp8IC1ks2D11tbCwIXX3dhCN7aWO6ATMaaIOvvn635xXEpPybMQam7M8sOqY24y89l4b8h3JCcoUmcAFU_VD50Q6SHJhUzPqDHaVJm5lQljwPd_hVUnwoh3g5-V7djPEb02gll1AknWnTo1FwajZ2VGAHR9x6jB93OYdwkzrRLznVSMpph_Fo4U5p47jL83Bx77kyghC7MwDhiYywGAbHAPY5TzB-FAzVukbNIMc8KR2p1OCRICVaLQrBBlof4ff-5iN-gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87449a5631.mp4?token=b7aiGB72O8TupF3BEDlMutbCgn57_O6ZU_sdD50r0l0QjUaAJcdroJY1W98adm-JbJin38_0-7FwFwlcp8IC1ks2D11tbCwIXX3dhCN7aWO6ATMaaIOvvn635xXEpPybMQam7M8sOqY24y89l4b8h3JCcoUmcAFU_VD50Q6SHJhUzPqDHaVJm5lQljwPd_hVUnwoh3g5-V7djPEb02gll1AknWnTo1FwajZ2VGAHR9x6jB93OYdwkzrRLznVSMpph_Fo4U5p47jL83Bx77kyghC7MwDhiYywGAbHAPY5TzB-FAzVukbNIMc8KR2p1OCRICVaLQrBBlof4ff-5iN-gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
قصف صهيوني بالقنابل الفسفورية على بلدة على الطاهر في جنوب لبنان.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/75395" target="_blank">📅 22:49 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75394">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">مصدر لنايا
يتحدث عن خروج كتلة العقد الوطني من ائتلاف الاعمار والتنمية بسبب ما حصل من ممارسات سيئة في جلسة منح الثقة للحكومة الجديدة  اليوم</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/75394" target="_blank">📅 22:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75393">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇮🇷
عضو لجنة الأمن القومي في البرلمان الإيراني "خضريان":
لا ينبغي للكويت أن تنسى أنها سقطت في يد صدام حسين في غضون 90 دقيقة فقط، وعليها أن تدرك حدودها اليوم، وأن الجمهورية الإسلامية قوية للغاية.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/75393" target="_blank">📅 22:28 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75392">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ceda60f73b.mp4?token=fgw5va5h4kuzylv9jc0ljsoHVdoaJmoCecJotwX6r_FrCmG2UmQDyGF8dzCc8ru0Pbm69vnR-VViC8BkHovA9bMQF7eE3uaWAsQWDbBg_mzSm1lCfLQosOL8mNUq1NQ3AtpkiOEm-6azpSOIN0XnxbtXk66el8qKZAeO1r-R1K4U4jHLWEZRo6EoEd4SwKt9X7ZxNJW2uiFrmuSPAqu28xfBPAsTLCrmFQIXMt5Ej-VNo6KWqfdNDfiJYEyrlUsKzuF2TmzMaGtN_zVtYSUFHK0p_ZjMEiCh_Zm3zG_HX_CQiQMmfQWigXqawj6tPvB6U-kCi2X3WK_roCvka2ZYXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ceda60f73b.mp4?token=fgw5va5h4kuzylv9jc0ljsoHVdoaJmoCecJotwX6r_FrCmG2UmQDyGF8dzCc8ru0Pbm69vnR-VViC8BkHovA9bMQF7eE3uaWAsQWDbBg_mzSm1lCfLQosOL8mNUq1NQ3AtpkiOEm-6azpSOIN0XnxbtXk66el8qKZAeO1r-R1K4U4jHLWEZRo6EoEd4SwKt9X7ZxNJW2uiFrmuSPAqu28xfBPAsTLCrmFQIXMt5Ej-VNo6KWqfdNDfiJYEyrlUsKzuF2TmzMaGtN_zVtYSUFHK0p_ZjMEiCh_Zm3zG_HX_CQiQMmfQWigXqawj6tPvB6U-kCi2X3WK_roCvka2ZYXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
قيادة العمليات المشتركة:
تم رصد تحركات لعنصر إرهابي خطر ضمن قاطع المسؤولية. و​بعد تحديد الهدف بدقة متناهية، نفذت قيادة طيران الجيش ضربة جوية ناجحة بواسطة الطائرة المسيرة المسلحة (CH5)، مستهدفةً الموقع المرصود في وادي الشاي ضمن قاطع قيادة عمليات كركوك ، إذ تم ​تدمير الوكر الإرهابي بالكامل وقتل العنصر الإرهابي المستهدف.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/75392" target="_blank">📅 22:08 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75391">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">يسقط حمد
دعوة لنصرة الشعب البحريني المجاهد .</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/75391" target="_blank">📅 22:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75390">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">سوالف الگهوة   العامري منزعج جدا ؛ ويفكر جديا بسحب وزرائه من الحكومة بسبب مهزلة اليوم في البرلمان …</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/75390" target="_blank">📅 21:54 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75389">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سوالف الگهوة
العامري منزعج جدا ؛ ويفكر جديا بسحب وزرائه من الحكومة بسبب مهزلة اليوم في البرلمان …</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/75389" target="_blank">📅 21:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75388">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/287f8d0310.mp4?token=Eb7qDU0HP5J7N4AGc9OqlyX4A3jQSblhUzKyEYxvLpYaxvmPKiXC9kGQEMOXPd2AKWiQ0FBlX7YLfXGsE8K4I-cIV-Lw-LpmbUaAO7ElG7-FX-w5LcfH6_oemcP4xI4b--bqe1gY3I3kOcQmOYoocXdNDvV0ijGLOYktPJaj_B3fd_eggDqXNxZAWhy4DRfrWNKizb8ccd8mvJvmV2S0zHHNFhc01itCgSI_4YLZvrnFM3XbHyEZ18miMdk3CRGL6gz06j8xfDTDg49h0jZ93MFMNWNTduM_IM3hhX2NdKjdShhMi9Qo1M3P7XQia7wkSYyyYTktkDJXMmCs69g43g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/287f8d0310.mp4?token=Eb7qDU0HP5J7N4AGc9OqlyX4A3jQSblhUzKyEYxvLpYaxvmPKiXC9kGQEMOXPd2AKWiQ0FBlX7YLfXGsE8K4I-cIV-Lw-LpmbUaAO7ElG7-FX-w5LcfH6_oemcP4xI4b--bqe1gY3I3kOcQmOYoocXdNDvV0ijGLOYktPJaj_B3fd_eggDqXNxZAWhy4DRfrWNKizb8ccd8mvJvmV2S0zHHNFhc01itCgSI_4YLZvrnFM3XbHyEZ18miMdk3CRGL6gz06j8xfDTDg49h0jZ93MFMNWNTduM_IM3hhX2NdKjdShhMi9Qo1M3P7XQia7wkSYyyYTktkDJXMmCs69g43g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
القناة 12 العبرية عن مصدر: إسرائيل ترفع حالة التأهب إلى الذروة استعدادا لاحتمال تجدد حرب إيران بعد عودة ترمب من الصين.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/75388" target="_blank">📅 21:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75387">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">بولندا تعلن عن تسجيل أول زواج مثلي لها يوم الخميس، بعد أحكام المحاكم الأوروبية والبولندية التي تتطلب الاعتراف بالزواجات المثلية التي تتم في الخارج.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/75387" target="_blank">📅 21:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75386">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🏴‍☠️
النتن ياهو: نقول للعالم أجمع إن القدس ستظل عاصمتنا الأبدية والتاريخية.
‏أبعدنا خطرا وجوديا يتمثل في القنابل النووية والصواريخ الباليستية الإيرانية.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/75386" target="_blank">📅 21:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75385">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdAyX0f1UYt2k2RPL6CKSQ2dDkpdb9srWb8jL-gPdY1CjzlHIFdjQx16uhakrxakh_SSExo5U15Rzsj18fh5NH4jznRDoiSl-WrVe2UAva-cMJqKobP9mzoBUtoXyCReRAYBbIfnD8so86wNEJ68gkYpzF-_kBh5ojr2-2siV5S4rZENd-cmUIdlfU0UFl_IEy63c6mVqxe8-QOBPIFWyoaNeHg36gnHz6K5DRPIqiLJmhJNqFbGiRL7-FnoziTS316U3-4kCe7QDpaypqY23uPTKPHWkMuRvmmDq01e6q1aP5NE09NfFTOjovqVqS-uTf-Z8Hm2cfSQwGD0GCpSpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇶
عراقجي يهنئ بتشكيل الحكومة العراقية الجديدة.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/75385" target="_blank">📅 21:02 · 24 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

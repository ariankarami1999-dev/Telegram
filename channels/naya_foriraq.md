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
<img src="https://cdn4.telesco.pe/file/tg_mPLQs5jvAKboZj2KAGsX0XKNrXdxJJ5rwtdF765P5ody7Jsk2JQ8sVqs-2Ny531ejAWbc0r3ehez5GZiCKoTeuvmvM2q2MZS8R66NocSWzUZp6KFVKi2z0QvjiVHGlDxSyQimYiXNMuiNWX445gHVHK4GazhVeQzBns8-7oV4a9D1aFXORT4k6TvjzfVIOVBHBlzO_k02R8MKAiamgigxkbSVl00LhR9V3fhQParndoOkk5MHdym4nykL1O_P1u6lpXFxD7TVFg5q-gwDODeWaynXZD1cxpTkHTUrQPGIf54tq-BLD1_f3b-rYw2AgP8AMjNj4Kr0zPotaNUxXA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 274K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 09:26:41</div>
<hr>

<div class="tg-post" id="msg-86491">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81cba719d5.mp4?token=KMTt0FIBlnrwWgg3qulApoZpvkHsSXGW9ilx676sqVGWtzevN7mPLiedTZTYekjGkdfdwXUd_YmlRGpF5CSeb3-z75tHZEu8PA8vqJSK23lB57zlQ1C1Vg7lYKRlcZEymgNENtOxNtwv_pciH969bVyYl0qtq5vm8FW26GehFmJDLPGTKAwTqU5qfB3JRPw1h-cVQfAnIMUDi5iByivQUHp19tGXrBe_pn8XYIx2kJ9XJGWO7nRFxfmdr_yeoxEWOHljmQZA4kMMp9IfP-tDnjb9mFeAuvxxIfHc1JmRJYWMu0PfJArfrxNEqC-6fEAiSpr8cyVt-fF401JQ1MKIAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81cba719d5.mp4?token=KMTt0FIBlnrwWgg3qulApoZpvkHsSXGW9ilx676sqVGWtzevN7mPLiedTZTYekjGkdfdwXUd_YmlRGpF5CSeb3-z75tHZEu8PA8vqJSK23lB57zlQ1C1Vg7lYKRlcZEymgNENtOxNtwv_pciH969bVyYl0qtq5vm8FW26GehFmJDLPGTKAwTqU5qfB3JRPw1h-cVQfAnIMUDi5iByivQUHp19tGXrBe_pn8XYIx2kJ9XJGWO7nRFxfmdr_yeoxEWOHljmQZA4kMMp9IfP-tDnjb9mFeAuvxxIfHc1JmRJYWMu0PfJArfrxNEqC-6fEAiSpr8cyVt-fF401JQ1MKIAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الجيش الإيراني:
في المرحلة السابعة والعشرين من عملية "صاعقة"، وردًا على التعديات الأخيرة التي ارتكبها الجيش الأمريكي الإرهابي ضد بلدنا، والهجوم الوحشي على منزل سكني في جزيرة قشم، استهدفت، قبل ساعات، "مواقع طائرات مقاتلة"، و"أنظمة اتصالات الأقمار الصناعية"، و"مخازن المعدات" لهذا الجيش القاتل، في قاعدة أحمد الجابر في الكويت، بواسطة طائرات مسيرة تابعة للجيش.
تلعب قاعدة أحمد الجابر في الكويت دورًا رئيسيًا في العمليات الجوية والمراقبة الأمريكية، وتعتبر، بالإضافة إلى دورها العملياتي، مركزًا حيويًا للدعم الجوي للجيش الأمريكي الإرهابي.
الجرائم والعقوبات والتهديدات تجعل إيران أكثر تماسكًا وتوحدًا في دفاعها المقدس.
الهجمات الحاسمة والواسعة والنادرة التي يشنها الجيش والحرس الثوري الإيراني تجعل اعتراض طائرات مسيرة وصواريخ إيران مكلفًا وصعبًا للغاية بالنسبة للعدو، على الرغم من استخدام أحدث أنظمة الدفاع وتطويرها، ويضطر العدو الخبيث إلى استخدام الرقابة الشديدة لمنع نشر أخبار الأضرار والقتلى والجرحى.
﻿</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/naya_foriraq/86491" target="_blank">📅 07:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86490">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f829242f02.mp4?token=Qyo7GhCJ8sFYElBG-1xspgRlA2sm2DTfOy38hyRvR79cKy24TxHI1Qfyfm6eohpm2SRXdgSu5cJbza8KZ10N6dTPKQjVeFtyT6qgxD60WLovtQf8zMP5F8KGrGY-Zos5qYaetQGHHfnrI6OlUc7ujW6smCU5iLlEj8VXMGlxcdWkULyWar75PkLw5e_Lx67I-dbJSvzpYy2AgUQYndJR7VfyxUO21_K1_RhklFG1hZayYYCkNEaub4tSAqzNxEo3kj5wk0vt8ex2R3sghNBjBAXqZP-5SCzjf3tnwzGFTiXVzVMTWIR-fGubzXT2MgXAJAieZeATnnmvFTcn46AB6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f829242f02.mp4?token=Qyo7GhCJ8sFYElBG-1xspgRlA2sm2DTfOy38hyRvR79cKy24TxHI1Qfyfm6eohpm2SRXdgSu5cJbza8KZ10N6dTPKQjVeFtyT6qgxD60WLovtQf8zMP5F8KGrGY-Zos5qYaetQGHHfnrI6OlUc7ujW6smCU5iLlEj8VXMGlxcdWkULyWar75PkLw5e_Lx67I-dbJSvzpYy2AgUQYndJR7VfyxUO21_K1_RhklFG1hZayYYCkNEaub4tSAqzNxEo3kj5wk0vt8ex2R3sghNBjBAXqZP-5SCzjf3tnwzGFTiXVzVMTWIR-fGubzXT2MgXAJAieZeATnnmvFTcn46AB6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران مسير انتحاري يدك مقرات الانفصاليين في محافظة دهوك شمالي العراق.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/86490" target="_blank">📅 05:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86489">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/933e01f5b0.mp4?token=gb-Tl-cIVoGHIKt56F-S0geKjihbYHo3PRkc6jLQzSrgPsmOUTmXV0e_w3Bh5_IERWTi_X2XdcHQ065gAGaGK8Kr8ILhHlaUAU2LbIV3y76bvrS8d8bEEDbxCVfdJUWels6NJwHTTtNw4LEPHaNsMNWSCZB-IzzFXKhI9VD08V26mFu2el4VmijcM6YTqemPSf0BLNPPmEu-L98LrCe2mqgSmSjsf6_zkErvDjhITkptLW0GyjIKYSnp4j8xbi52P6HRoyj1IPBwktCi58dM3gQq6MX3DrHICoIXnQ2a-LG3eT_3gGJYsDyEyuHp5jb4NKzQp8nT5dMscyV8bA4VTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/933e01f5b0.mp4?token=gb-Tl-cIVoGHIKt56F-S0geKjihbYHo3PRkc6jLQzSrgPsmOUTmXV0e_w3Bh5_IERWTi_X2XdcHQ065gAGaGK8Kr8ILhHlaUAU2LbIV3y76bvrS8d8bEEDbxCVfdJUWels6NJwHTTtNw4LEPHaNsMNWSCZB-IzzFXKhI9VD08V26mFu2el4VmijcM6YTqemPSf0BLNPPmEu-L98LrCe2mqgSmSjsf6_zkErvDjhITkptLW0GyjIKYSnp4j8xbi52P6HRoyj1IPBwktCi58dM3gQq6MX3DrHICoIXnQ2a-LG3eT_3gGJYsDyEyuHp5jb4NKzQp8nT5dMscyV8bA4VTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز محافظة دهوك</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/86489" target="_blank">📅 05:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86488">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">انفجارات تهز محافظة دهوك</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/86488" target="_blank">📅 05:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86487">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fbe150fb6.mp4?token=U8o6ruMeRpWMNKSb2DTcWJM9SbR4HitamQWELgVun6GJCBDBFIx6WG-15XUKIIFu5DkkcyA3LEN-9HmBM9Eo53NVQ3Q2kBnA67v807fx_9qFvZ4WkpGiqkhh5fMoVzAhqyv_zgI7FyWyrbDSIt9LOETDbnoGpf6zWVdi98JIK_WFHb5PYMyPwsuE2NofSE4qGeoe-5cB5_4xTqIcxWrhcD8yspJy-O_K-GS2D8Rlh5ZGiuUDw8eNzrm3PcqMcNCWM80Gpbd7gjXuZ1JHg7UPBDysrGC30T-_qOlOWqa0dwGsjbGlk-q61LSQKv2RuxdFeHnuXg9IeekJgKmfadekHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fbe150fb6.mp4?token=U8o6ruMeRpWMNKSb2DTcWJM9SbR4HitamQWELgVun6GJCBDBFIx6WG-15XUKIIFu5DkkcyA3LEN-9HmBM9Eo53NVQ3Q2kBnA67v807fx_9qFvZ4WkpGiqkhh5fMoVzAhqyv_zgI7FyWyrbDSIt9LOETDbnoGpf6zWVdi98JIK_WFHb5PYMyPwsuE2NofSE4qGeoe-5cB5_4xTqIcxWrhcD8yspJy-O_K-GS2D8Rlh5ZGiuUDw8eNzrm3PcqMcNCWM80Gpbd7gjXuZ1JHg7UPBDysrGC30T-_qOlOWqa0dwGsjbGlk-q61LSQKv2RuxdFeHnuXg9IeekJgKmfadekHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيق أخر للهجوم الواسع بواسطة المسيرات الإنقضاضية على مقرات الإنفصاليين في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/86487" target="_blank">📅 04:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86486">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10c6755af0.mp4?token=JqsR05wexa1WwingdTlIfKc2ppQnOQ2JUXWjJCwJzQphJSJCYIENuGDk2uI4GzAuFot-XHk5do-HnWPYmvjYP9k0Hc5h-vBxv1HBR6Q8LEixqwzgkcLLQ5o3nPjqXL4a6W2g56pwzLXmsgT5h8TJOYh1pFl13LBezaQr17kcMpgHxPegFVLh_sgr1ZLkb_EqURiERC88aj6RO2Ic86bEeBf9q4S9rwXPg-LSKY4dNunJ7Go0FoICxItlJXl7QY6OgIhycXKraIoJiduv0EkDXXyOLzKdO7T5JugWkNbMPDPm5lZbVUNNxFBXCTO9RbK77hrYrB_8JrAaaG5r6tx4KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10c6755af0.mp4?token=JqsR05wexa1WwingdTlIfKc2ppQnOQ2JUXWjJCwJzQphJSJCYIENuGDk2uI4GzAuFot-XHk5do-HnWPYmvjYP9k0Hc5h-vBxv1HBR6Q8LEixqwzgkcLLQ5o3nPjqXL4a6W2g56pwzLXmsgT5h8TJOYh1pFl13LBezaQr17kcMpgHxPegFVLh_sgr1ZLkb_EqURiERC88aj6RO2Ic86bEeBf9q4S9rwXPg-LSKY4dNunJ7Go0FoICxItlJXl7QY6OgIhycXKraIoJiduv0EkDXXyOLzKdO7T5JugWkNbMPDPm5lZbVUNNxFBXCTO9RbK77hrYrB_8JrAaaG5r6tx4KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
مسؤولين أمريكيين: البنتاغون قلص وجوده بالكويت ردا على هجمات إيران على قواعد أمريكية للحد من المخاطر.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/86486" target="_blank">📅 04:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86485">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇺🇸
مسؤولين أمريكيين: البنتاغون قلص وجوده بالكويت ردا على هجمات إيران على قواعد أمريكية للحد من المخاطر.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/86485" target="_blank">📅 04:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86484">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/86484" target="_blank">📅 04:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86483">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">آمریکا باید منطقه را ترک کند</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/86483" target="_blank">📅 04:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86482">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇺🇸
الأمريكان يهربون من الضربات الإيرانية.. مسؤولين أمريكيين: الولايات المتحدة تعيد حاليا النظر في نطاق وجودها العسكري في الكويت.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/86482" target="_blank">📅 04:23 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86481">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/86481" target="_blank">📅 04:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86480">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/86480" target="_blank">📅 04:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86479">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامب: لم أتخذ قرارا بعد بشأن السماح لأوكرانيا بإنتاج صواريخ باتريوت الاعتراضية أرض جو.  متفائل بإتمام الولايات المتحدة الاتفاقية التاريخية للطاقة النووية المدنية مع السعودية.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/86479" target="_blank">📅 04:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86478">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامب: لم أتخذ قرارا بعد بشأن السماح لأوكرانيا بإنتاج صواريخ باتريوت الاعتراضية أرض جو.
متفائل بإتمام الولايات المتحدة الاتفاقية التاريخية للطاقة النووية المدنية مع السعودية.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/86478" target="_blank">📅 04:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86477">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b953c0da1.mp4?token=R8EKjfH7XtpBNoaxfSAjXDU8K7_ea1AvLyor9Dt6mPtxtI-Gxlc8EP3ye8FsTaK2WNhPJb7MbpiEcMvS15HlVvpi1i5YGzZVHhleFjXmNuwVZtaKz4cxMYWuE3oy7NwlQ7LoTMZEMSK60kOk_-4WQhCeusbrJC7zEm86onMBR2LhCaVLCLBmsiqqJ7Lr6nJ8sNrvsMA4gwjjCJj8VLwa_he1fV6Hn1AorOhAopC7ZhLD_j7Wacyqtn5OaDWbkSpuJfxsE7_If15e6nfBiQQrHzRodfp0-Az7NmUSGiKqpB2F1kgzN0PWLsa1-2TJ5wFUNBOCEL2EPgpJmtfUhvjDuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b953c0da1.mp4?token=R8EKjfH7XtpBNoaxfSAjXDU8K7_ea1AvLyor9Dt6mPtxtI-Gxlc8EP3ye8FsTaK2WNhPJb7MbpiEcMvS15HlVvpi1i5YGzZVHhleFjXmNuwVZtaKz4cxMYWuE3oy7NwlQ7LoTMZEMSK60kOk_-4WQhCeusbrJC7zEm86onMBR2LhCaVLCLBmsiqqJ7Lr6nJ8sNrvsMA4gwjjCJj8VLwa_he1fV6Hn1AorOhAopC7ZhLD_j7Wacyqtn5OaDWbkSpuJfxsE7_If15e6nfBiQQrHzRodfp0-Az7NmUSGiKqpB2F1kgzN0PWLsa1-2TJ5wFUNBOCEL2EPgpJmtfUhvjDuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرائق واسعة في مقرات المعارضة الكردية بأربيل</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/86477" target="_blank">📅 04:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86476">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/852dc2afce.mp4?token=AlrLsNTeMRrP0_SIdHcQ8_O1Ga_U-vlsJP4yvvRMwPfOTmYPZSOhhEluQwlqIpiY8ocUoSghnAflwGFu_6XvohmnuLYIbUUxpKAKGhp70DAHKrUWYlutKXhx8adip-5IsLB08OYy3ha7Zw356ei10XpXB7x1puaQ_sIh06u0JpmrlbAbSWxt4_HPi3kt-3ADC9ki6dRglj8CjDbnEJLDg10O7gwn2rDbUTx8Mg1Vb_tuCnp1oqt04EZalxO2zEzL2iRZiHz_-nH-WAECzD6SEAIkq3TIS0fgTENR9SDTHRaRemn7D6hTicVU36tc5QsGJ1odTXNckmumo4RP-WHl_jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/852dc2afce.mp4?token=AlrLsNTeMRrP0_SIdHcQ8_O1Ga_U-vlsJP4yvvRMwPfOTmYPZSOhhEluQwlqIpiY8ocUoSghnAflwGFu_6XvohmnuLYIbUUxpKAKGhp70DAHKrUWYlutKXhx8adip-5IsLB08OYy3ha7Zw356ei10XpXB7x1puaQ_sIh06u0JpmrlbAbSWxt4_HPi3kt-3ADC9ki6dRglj8CjDbnEJLDg10O7gwn2rDbUTx8Mg1Vb_tuCnp1oqt04EZalxO2zEzL2iRZiHz_-nH-WAECzD6SEAIkq3TIS0fgTENR9SDTHRaRemn7D6hTicVU36tc5QsGJ1odTXNckmumo4RP-WHl_jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دفاعات الإنفصاليين تتمكن من مشاهدة لحظة وصول وإصابة المسيرات الإنتحارية.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/86476" target="_blank">📅 04:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86475">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a9e70da68.mp4?token=QMyl0LY7-IDbwQK6vzWprjxrPG8u_Qt_WwJYqO4oujmihKrXPDL5IqDGLQZtrAqvDyjE04Py9xicBkM3qnn_KWP39A9Ah8XZogBMd58B1vi2JtOSQnM7DhdYsuNhZf97Q9V2J-a4QSX0Dr9K2Nuu1TWRfelcUHx8tcqiN_M89BUPl6Gu_iVgsfzvSzKOQuAfliDJR8fc2ShMIraGIP2okNQTzY3lGVyn70QHHmzchq_tQM315_-_rmfEln1g9ghPv54BMxqipPftQE5tFVZqd80VSuh1mVWpfEbYhxhQg76BTcOr4kIVCQ5uMODDevaCR1tieI9nLm-gi9kbCJx9Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a9e70da68.mp4?token=QMyl0LY7-IDbwQK6vzWprjxrPG8u_Qt_WwJYqO4oujmihKrXPDL5IqDGLQZtrAqvDyjE04Py9xicBkM3qnn_KWP39A9Ah8XZogBMd58B1vi2JtOSQnM7DhdYsuNhZf97Q9V2J-a4QSX0Dr9K2Nuu1TWRfelcUHx8tcqiN_M89BUPl6Gu_iVgsfzvSzKOQuAfliDJR8fc2ShMIraGIP2okNQTzY3lGVyn70QHHmzchq_tQM315_-_rmfEln1g9ghPv54BMxqipPftQE5tFVZqd80VSuh1mVWpfEbYhxhQg76BTcOr4kIVCQ5uMODDevaCR1tieI9nLm-gi9kbCJx9Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز قضاء خبات بمحافظة أربيل</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/naya_foriraq/86475" target="_blank">📅 04:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86474">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd8c976939.mp4?token=EPEiUhe6vBt7S3WOMYG97XXFWwzuINRdFYZ3Bwc7DMSYx7wk1zdOfC_IilKR0lLJ_akUP_O9l4OWRGLxzenGQu7h2w-YXi1r6MLJBDwKX9FkF3t-j7syDjmlzimeakLx5_3h5MFQgIPe4j6Fc-L2x_axevvlrvIQanhUV2pcBM9d92kQBQ0V42WuIMEhNAUJ3iXW289N2ZmGlsf0zwhGtLIlL-CwOhH3_22YkU1mbaVj5WuLJAaV54NDHzElt7oyxXqvfJ7aKdWX6m9Zp1t3ytFNXeGg2opGwuZrwhY3wN9rMTlitvqPLteFhetIrOLKdvtxuw2d3Md9oyYnZ7ks3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd8c976939.mp4?token=EPEiUhe6vBt7S3WOMYG97XXFWwzuINRdFYZ3Bwc7DMSYx7wk1zdOfC_IilKR0lLJ_akUP_O9l4OWRGLxzenGQu7h2w-YXi1r6MLJBDwKX9FkF3t-j7syDjmlzimeakLx5_3h5MFQgIPe4j6Fc-L2x_axevvlrvIQanhUV2pcBM9d92kQBQ0V42WuIMEhNAUJ3iXW289N2ZmGlsf0zwhGtLIlL-CwOhH3_22YkU1mbaVj5WuLJAaV54NDHzElt7oyxXqvfJ7aKdWX6m9Zp1t3ytFNXeGg2opGwuZrwhY3wN9rMTlitvqPLteFhetIrOLKdvtxuw2d3Md9oyYnZ7ks3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدفاعات تجلس على الأرض والدخان يتصاعد
😄</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/naya_foriraq/86474" target="_blank">📅 04:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86473">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1ccfcba4a.mp4?token=Me2CaOvZdCC559_1vpHSoqdxEiMy3Tgs5vWRBunDxkp6OJbzvs9RZW3YsM-9hGJMPSn2qA59ffG2fcP1yTxgO-Ve2g1RjAEguBtt3rJsDPaSwsWvqu8bKwKjAxQUEtpaBPj68eVA7ZVVvIrGsDAT08lr5uyqvQPNZbtg3aZPa4KPE5j2KG6y3sh4Ykg1lBP4ASHxvTZ5wznyOoe6pspnS3UC4Fdw2PLQiPOxP06WW1Nim9S8is8a3lREo61hM_B25HYrrneWQTDAissmBGxnEi5MC3YbNtnnJ31hAyFVwTJGPxKtL8zR9d5v2ikbbS0w3BrtOI7bnbLboiAMHdZa7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1ccfcba4a.mp4?token=Me2CaOvZdCC559_1vpHSoqdxEiMy3Tgs5vWRBunDxkp6OJbzvs9RZW3YsM-9hGJMPSn2qA59ffG2fcP1yTxgO-Ve2g1RjAEguBtt3rJsDPaSwsWvqu8bKwKjAxQUEtpaBPj68eVA7ZVVvIrGsDAT08lr5uyqvQPNZbtg3aZPa4KPE5j2KG6y3sh4Ykg1lBP4ASHxvTZ5wznyOoe6pspnS3UC4Fdw2PLQiPOxP06WW1Nim9S8is8a3lREo61hM_B25HYrrneWQTDAissmBGxnEi5MC3YbNtnnJ31hAyFVwTJGPxKtL8zR9d5v2ikbbS0w3BrtOI7bnbLboiAMHdZa7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدفاعات تجلس على الأرض والدخان يتصاعد
😄</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/naya_foriraq/86473" target="_blank">📅 04:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86472">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1a34c1a19.mp4?token=K4E03W_kPe3cnrX8qpLJZYu5emqjAk2MssX3RY75kET5Gdj73QetudhaYUAzkyhVOmDrCH2KWqrvWbYpdBIji-XWhB5whWoyFuxZP0WGVH2IUeyzIclcSg4YFrdPtKqWncbcCIeCjAK8L05ro5YFA0wzT69zNDwXYIwQjYg3AotW9InMY-nN47852i34JNyD8QcBbTOEzw_kv8aeFnfoioSZKH4hnKy7A9wuVUnnfTx4yccZVkP5yg7z7FAneL1Gt99ku0QJSEbKZvHYWcxJlZl02DxoSB6mSdxWjkctjVj8XdYOci3h12fPdTTmaX5p6A6CH4-Z434VjfXZDw9FFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1a34c1a19.mp4?token=K4E03W_kPe3cnrX8qpLJZYu5emqjAk2MssX3RY75kET5Gdj73QetudhaYUAzkyhVOmDrCH2KWqrvWbYpdBIji-XWhB5whWoyFuxZP0WGVH2IUeyzIclcSg4YFrdPtKqWncbcCIeCjAK8L05ro5YFA0wzT69zNDwXYIwQjYg3AotW9InMY-nN47852i34JNyD8QcBbTOEzw_kv8aeFnfoioSZKH4hnKy7A9wuVUnnfTx4yccZVkP5yg7z7FAneL1Gt99ku0QJSEbKZvHYWcxJlZl02DxoSB6mSdxWjkctjVj8XdYOci3h12fPdTTmaX5p6A6CH4-Z434VjfXZDw9FFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفعيل المنظومات الدفاعية للمعارضة الكردية الإرهابية في السليمانية
😄</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/naya_foriraq/86472" target="_blank">📅 04:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86471">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3788fea65c.mp4?token=ApxnIeJKQETeFg_-V7JbZxfwqM4hFKOsO7hJB8tPLBtV5VAqqRz2Gk0iLh04UhRIklo-iFs26eWx2Ak9vV_ic-42yqahicrE02iVLqP5zvBeX6wMZykteIs_gzdQYqM4w7L1gXrMLqrvOj3JBhNpqmccjus_s-5RqS5mN0OkyUMIeGBM_-H2zb9H5c9lzWxXXtPUEs-VZDv7cYfb5o4opGl-EgK1_PUfyTiZQLP_sXe1qmgcrH5lFyfSWcULB3dnoi7spoaYF_KoQBq9dGjcpxxcoNDUBcNaSrRkCeu9N-sUklVls1tSQHQE-nYOQuhC55gMn8U7FJIUi5JUpxqX1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3788fea65c.mp4?token=ApxnIeJKQETeFg_-V7JbZxfwqM4hFKOsO7hJB8tPLBtV5VAqqRz2Gk0iLh04UhRIklo-iFs26eWx2Ak9vV_ic-42yqahicrE02iVLqP5zvBeX6wMZykteIs_gzdQYqM4w7L1gXrMLqrvOj3JBhNpqmccjus_s-5RqS5mN0OkyUMIeGBM_-H2zb9H5c9lzWxXXtPUEs-VZDv7cYfb5o4opGl-EgK1_PUfyTiZQLP_sXe1qmgcrH5lFyfSWcULB3dnoi7spoaYF_KoQBq9dGjcpxxcoNDUBcNaSrRkCeu9N-sUklVls1tSQHQE-nYOQuhC55gMn8U7FJIUi5JUpxqX1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار دك معاقل المعارضة الإرهابية في السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/86471" target="_blank">📅 03:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86470">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ae6cef071.mp4?token=HtE0z2We7ThTGEpPxnlYA6ZvNwpmG26_OG4J5X7lSLYkgI39W4TqVNvFXuhMXqLpogwqu2QhmAQAEvyUXxZolRqsTvoAEs-Cfet7l5DA4VNzfhBE51Vr1ePpQ0VnkJqdTraDvh7QnLJ_s_-ECulHfkVanZr-D4xxYIHjm_r-PlXkP5S8j1HskDGHX51v7i8dMZuG8PUfZpMQtPi14F82w37cH2-jev3lJwfCo9ZnmHrI2lmqyPlg6JUMHX5XR-q29keTLy5ZkcQ7aGardCLyoou4Vd3sga9_uIMl8gxrtUYZGnoqjWoJh6BvQrnVHf7q1x54-sOocb5WMAqF7D0Isw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ae6cef071.mp4?token=HtE0z2We7ThTGEpPxnlYA6ZvNwpmG26_OG4J5X7lSLYkgI39W4TqVNvFXuhMXqLpogwqu2QhmAQAEvyUXxZolRqsTvoAEs-Cfet7l5DA4VNzfhBE51Vr1ePpQ0VnkJqdTraDvh7QnLJ_s_-ECulHfkVanZr-D4xxYIHjm_r-PlXkP5S8j1HskDGHX51v7i8dMZuG8PUfZpMQtPi14F82w37cH2-jev3lJwfCo9ZnmHrI2lmqyPlg6JUMHX5XR-q29keTLy5ZkcQ7aGardCLyoou4Vd3sga9_uIMl8gxrtUYZGnoqjWoJh6BvQrnVHf7q1x54-sOocb5WMAqF7D0Isw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیر مردان ایران زمین خواب را از چشمان تروریست‌های هم پیمان با آمریکا خواهند گرفت.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/86470" target="_blank">📅 03:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86469">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b76b77632e.mp4?token=u4odVlwfFa_k8rHYepQbB6eQOqaeElGh1Ef3oYFXzcEJDJg1Un17EXDh4z07Gxuk-T0tbLTP7a1o3Nb88DlL_WgHPsC8hgtVEHKw5nvxI91Ax3U2Y4xQ5KLyVfJRcQiwpezS4FYiH4l_pMIlgkZMHyGLCzMGGCRY8EfB-m7H3lQa2hEdqKqsujoD_Y_1uxhqZB5qAyUSoo8QMRTYf2u-B0rtla_akITMMY-V-_D69yiRcnYssrpJITp3-wEjAmEwRBBhz3aO-ogBVdyxjP18D22lOxcXONcdAU1PnIev2dc9Nm43-VUlJGS-iEfHcEXfs5V3qe43HDkpD8y5fcvhPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b76b77632e.mp4?token=u4odVlwfFa_k8rHYepQbB6eQOqaeElGh1Ef3oYFXzcEJDJg1Un17EXDh4z07Gxuk-T0tbLTP7a1o3Nb88DlL_WgHPsC8hgtVEHKw5nvxI91Ax3U2Y4xQ5KLyVfJRcQiwpezS4FYiH4l_pMIlgkZMHyGLCzMGGCRY8EfB-m7H3lQa2hEdqKqsujoD_Y_1uxhqZB5qAyUSoo8QMRTYf2u-B0rtla_akITMMY-V-_D69yiRcnYssrpJITp3-wEjAmEwRBBhz3aO-ogBVdyxjP18D22lOxcXONcdAU1PnIev2dc9Nm43-VUlJGS-iEfHcEXfs5V3qe43HDkpD8y5fcvhPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پهپاد‌های انتحاری با دقت و قدرت در حال منهدم کردن مقر‌های تروریست‌های تجزیه طلب در السلیمانیه و اربیل عراق هستند.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/86469" target="_blank">📅 03:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86468">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30c920400a.mp4?token=E8OT9xDqISSktordS3-JoZBx4AYrEqzU4Ux3BFFl-zkWEMyhGdQp6eQK5-av_jJ-w_tBVKjwiUsGPZfneJIfiC9ItUhSM27wGr_NZXE6N5crqOD0Ts3-xsqn4TfO8MiPddOtmGo6s9a8UJhXf6e12t-62aW8ye7rKtDU7XQcjcGcfgzXLZnfeJpMY8qlxYOCKfDr2XF-GO9kPegstxRQvPc0bMaSHhmp_G0eURjpHj6xhCZgsZdt_YgXd4wxthpmi5CWykxSlAoJz1V48_66bwuQDMbrUFStBRUiNzLQQ-gQftI07T7Gu9xAv0ILvFIV_fhsU_FNMs16LdB8RuWX4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30c920400a.mp4?token=E8OT9xDqISSktordS3-JoZBx4AYrEqzU4Ux3BFFl-zkWEMyhGdQp6eQK5-av_jJ-w_tBVKjwiUsGPZfneJIfiC9ItUhSM27wGr_NZXE6N5crqOD0Ts3-xsqn4TfO8MiPddOtmGo6s9a8UJhXf6e12t-62aW8ye7rKtDU7XQcjcGcfgzXLZnfeJpMY8qlxYOCKfDr2XF-GO9kPegstxRQvPc0bMaSHhmp_G0eURjpHj6xhCZgsZdt_YgXd4wxthpmi5CWykxSlAoJz1V48_66bwuQDMbrUFStBRUiNzLQQ-gQftI07T7Gu9xAv0ILvFIV_fhsU_FNMs16LdB8RuWX4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الضربات الواسعة على مقرات ومعاقل أرهابيي المعارضة الكردية في السليمانية وأربيل مستمرة حتى اللحظة.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/86468" target="_blank">📅 03:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86467">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6576974dff.mp4?token=O7nXiClneZ2_GSF0pVYmhiKO8hTKK8_D4JNT3jdTUtHDvb552ygpEkxUV_KjvqQFiWKgvrryvceYQ390Saj2e4bLtWnqSJwwizRj6S9VaMRukV7ic0-4TVST1JZvObsxj4gzN8Q5OCZu2UNWoAmOj3-8LXrHyMuRJl2A9MgAlX7-7QMdOFnqhyx60OkFFBhMHqaHUqIMn3vW6M660RarrkLLEiTnOSPfPQV-Y83sgtlCHoLrPpTE1YIuPJMXwoL3hgmqCGfoEnTmNCKLkb6dlp_YXhOxi1zXOpdQK1pjfLyOIwruuBfcoPhbK_clZXTgUoYevT_hzvKwaIRiEfYpqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6576974dff.mp4?token=O7nXiClneZ2_GSF0pVYmhiKO8hTKK8_D4JNT3jdTUtHDvb552ygpEkxUV_KjvqQFiWKgvrryvceYQ390Saj2e4bLtWnqSJwwizRj6S9VaMRukV7ic0-4TVST1JZvObsxj4gzN8Q5OCZu2UNWoAmOj3-8LXrHyMuRJl2A9MgAlX7-7QMdOFnqhyx60OkFFBhMHqaHUqIMn3vW6M660RarrkLLEiTnOSPfPQV-Y83sgtlCHoLrPpTE1YIuPJMXwoL3hgmqCGfoEnTmNCKLkb6dlp_YXhOxi1zXOpdQK1pjfLyOIwruuBfcoPhbK_clZXTgUoYevT_hzvKwaIRiEfYpqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  اصابة مباشر للمسيرات الإنتحارية</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/86467" target="_blank">📅 03:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86466">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3195c11a42.mp4?token=g3XVDmWRD4Gn8c4MSMi3AY0DZ40zzBRQO3U_dmcSXO6HWdnqSyXSjKRT4HD9kS8P_dRePy_HdIrjKGlAvAP-MtyucSDW-UcyHxpLBUwmZs0SowLMzmIirZ5mLqhMAQhzXwpWO6QC7M1rz12wffgpNtwwho4awgj2Y-ybTD3fRGv_UXBYUrG3DHseZE5M624eyOenimywbh0uQ5E5fBaGnH7hmDaULe3ML0E3WHZ8VNWF_qteX0eaW6zZMdBBUCMAdrJ_VuEZIu3YSkk3HHd7FpdbAwQpZrwslrFJDmDxsgyoVJnW0CxnGKDxDeNlNijI-sCQxYNPx395ZxfyM2pEMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3195c11a42.mp4?token=g3XVDmWRD4Gn8c4MSMi3AY0DZ40zzBRQO3U_dmcSXO6HWdnqSyXSjKRT4HD9kS8P_dRePy_HdIrjKGlAvAP-MtyucSDW-UcyHxpLBUwmZs0SowLMzmIirZ5mLqhMAQhzXwpWO6QC7M1rz12wffgpNtwwho4awgj2Y-ybTD3fRGv_UXBYUrG3DHseZE5M624eyOenimywbh0uQ5E5fBaGnH7hmDaULe3ML0E3WHZ8VNWF_qteX0eaW6zZMdBBUCMAdrJ_VuEZIu3YSkk3HHd7FpdbAwQpZrwslrFJDmDxsgyoVJnW0CxnGKDxDeNlNijI-sCQxYNPx395ZxfyM2pEMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجدداً.. هجمات جديدة تدك معاقل إرهابيي المعارضة الكردية في أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/86466" target="_blank">📅 03:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86465">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مسيرات انتحارية تدك مقرات المعارضة الكردية الإرهابية في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/86465" target="_blank">📅 03:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86464">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02d3f0ef6d.mp4?token=mNXgqGVBKXLHJdPai6iMMQnVe5w6l5debXMyFqLt9QUMTb_4_wEpEcMwh_RZXYNG1U6HXx6NHnhT1dS0qBNl5-xmB5ze0P3fz2sJHFpCDQLFAng3BUyPSknAXt7kYg-8uy3_xxF1x7Xo0LXTtCM1ITvhrkldDjfmiwoy-pGjxW1uxSBC7daDTIcK9Tc2cfDowd3zbdrYC8FjPsUJGq1gBrpupB3BIIBwOHiN1p6uF94Z9NTETMX-HKgY4Bmtdt2tbTS-y7U32mxFAOmS-u_uPAV2V3UMPJ4WWySEZ6PFnczxz4dC_MXKw3-P7_345zclY3gtgjl5015lgTD1whQPHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02d3f0ef6d.mp4?token=mNXgqGVBKXLHJdPai6iMMQnVe5w6l5debXMyFqLt9QUMTb_4_wEpEcMwh_RZXYNG1U6HXx6NHnhT1dS0qBNl5-xmB5ze0P3fz2sJHFpCDQLFAng3BUyPSknAXt7kYg-8uy3_xxF1x7Xo0LXTtCM1ITvhrkldDjfmiwoy-pGjxW1uxSBC7daDTIcK9Tc2cfDowd3zbdrYC8FjPsUJGq1gBrpupB3BIIBwOHiN1p6uF94Z9NTETMX-HKgY4Bmtdt2tbTS-y7U32mxFAOmS-u_uPAV2V3UMPJ4WWySEZ6PFnczxz4dC_MXKw3-P7_345zclY3gtgjl5015lgTD1whQPHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الحرائق تشتعل في مقرات الإنفصاليين الأكراد بمحافظة السليمانية جراء استهدافهم بأسراب من المسيرات.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/86464" target="_blank">📅 03:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86463">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9Q69Qw2WZBCBvQ6EuvC-cboht3HaipQbJuX8TIAVmckS8yIWycYGt6r7AWKu0M5ngb7gwNQhFu2NUAL0tHTODzSE2EhkJv2Sh0l487h7Hxi6hL4aHBshH3Qr4uDEagyaFsJEnh3oI8oVLD04TpV2SH366LPdyhTUMLfGzzcZwFU3O2UoFVxLY9vfmgIDaH6dCLap7djYYcsEIX22uJM9N2ICjCu6Ig6R5r9VBZq8wec266I4DRKhJRgyWghTPs1mGteLInEL0cTMnGt5oNCl7FMJuXIdFbBc-UQUjkwelPdL24F6X6T9Lz8K8tRXurO7CRFN3zi3LXiyrG45qrErw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات هي الأعنف تدمر مقرات ومخازن السلاح التابعة للمعارضة الكردية الإيرانية في السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/86463" target="_blank">📅 03:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86462">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bec23a469b.mp4?token=OD-91tI9Kr8Pp3SJydqm6Vv4EG0dp2J6o5NxjjxYMUmKXMjwb_IljtgHM8m7M_xRbAsstWjJszJh8LmhUT6iW7bPE1nmnOAHAm-lX-o_6uCwx1IAQguhFNrnFKgsF1bhVRp_efAwX_1DqlLtAuASUpLuF_c97EM1TFP2OTZgkwvH6ogm6hp_TbRjAsjmMbL0z-p0tO_a3oC2GovCp46kEg0pfs9MEgUJd4WDRu3YfrfXcFi4GaTSxAmsR_m1Vz9OorZAR4pyqHW-og8YYJtvC5Q_xS9ip9GVQIBz8xaxNzg2yY9gGBAckROcF-As5EPrPWrJsRBz0iwwD0a6BQmMWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bec23a469b.mp4?token=OD-91tI9Kr8Pp3SJydqm6Vv4EG0dp2J6o5NxjjxYMUmKXMjwb_IljtgHM8m7M_xRbAsstWjJszJh8LmhUT6iW7bPE1nmnOAHAm-lX-o_6uCwx1IAQguhFNrnFKgsF1bhVRp_efAwX_1DqlLtAuASUpLuF_c97EM1TFP2OTZgkwvH6ogm6hp_TbRjAsjmMbL0z-p0tO_a3oC2GovCp46kEg0pfs9MEgUJd4WDRu3YfrfXcFi4GaTSxAmsR_m1Vz9OorZAR4pyqHW-og8YYJtvC5Q_xS9ip9GVQIBz8xaxNzg2yY9gGBAckROcF-As5EPrPWrJsRBz0iwwD0a6BQmMWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارهای مهیب در مقرهای تروریست‌های تجزیه طلب‌ در السلیمانیه عراق</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/86462" target="_blank">📅 03:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86461">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228aa39f63.mp4?token=LIUr51qE0FqabFg_o4nZx9Nc00abM4-hYo1ndhx1AIxwPtlhcI6L-4lnAxt8idFnVPvXwuHy1AeiozdW7w3RekS7qgbDkcdg0I3a82wxqLtd2LxoUpyMCWHOb6M_z8JEpiB9InPy0tmEzqX07fVCLgYC_ilSi6tT0G2p439cgtWEQ_SaseJE1w_PouhohFRpOqIngYMAE9zJL_pWWLKw2c_VrBBRyXqRIBvsfm8mYvrO5wYmcsryiF-bSnLyU0FyPSZ0xHlel2ZvKgYEN3lHgRjAkjcE4bDESRo4SIGxkOKPM4mpe5XN_SOL-SjTNG-RqJm6wVswNibZS31yDv3V_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228aa39f63.mp4?token=LIUr51qE0FqabFg_o4nZx9Nc00abM4-hYo1ndhx1AIxwPtlhcI6L-4lnAxt8idFnVPvXwuHy1AeiozdW7w3RekS7qgbDkcdg0I3a82wxqLtd2LxoUpyMCWHOb6M_z8JEpiB9InPy0tmEzqX07fVCLgYC_ilSi6tT0G2p439cgtWEQ_SaseJE1w_PouhohFRpOqIngYMAE9zJL_pWWLKw2c_VrBBRyXqRIBvsfm8mYvrO5wYmcsryiF-bSnLyU0FyPSZ0xHlel2ZvKgYEN3lHgRjAkjcE4bDESRo4SIGxkOKPM4mpe5XN_SOL-SjTNG-RqJm6wVswNibZS31yDv3V_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات كبيرة جداً تطال مقرات الإنفصاليين الأكراد جراء دكها بأسراب من المسيرات الإنتحارية</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/86461" target="_blank">📅 03:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86460">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09426ed436.mp4?token=vihSs1WEbFKI_gh9tqJE7onte4QYo3kNtPScNSskVXuKgFzMv7cLiszAXvCAPWnyMgiPZRdjel0xsprsAFkvue8tf9m_YcZf2e1znk7UwI5gLUh_RvVelMoTsbcq2yDxcUsp57lb_pig2Skb9jQXdF08hJ8S5LkxJkIzXPAKCYzlHziA5-irl2FGeS2_1mlLQhObONuBkcMtZVFlz3mJdFbBs9-0OOSYwNjb3ffC4vF-3W2RkqzoP8a20UnInNsXXjrVKz2wpL8YC3OR9TSFdcr0f9VkPrzYkZblBHyiZZxrfnfmU9G7ifBifNqJhMSBXP2U9Cjqlrx3O4Xl-0wqfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09426ed436.mp4?token=vihSs1WEbFKI_gh9tqJE7onte4QYo3kNtPScNSskVXuKgFzMv7cLiszAXvCAPWnyMgiPZRdjel0xsprsAFkvue8tf9m_YcZf2e1znk7UwI5gLUh_RvVelMoTsbcq2yDxcUsp57lb_pig2Skb9jQXdF08hJ8S5LkxJkIzXPAKCYzlHziA5-irl2FGeS2_1mlLQhObONuBkcMtZVFlz3mJdFbBs9-0OOSYwNjb3ffC4vF-3W2RkqzoP8a20UnInNsXXjrVKz2wpL8YC3OR9TSFdcr0f9VkPrzYkZblBHyiZZxrfnfmU9G7ifBifNqJhMSBXP2U9Cjqlrx3O4Xl-0wqfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لت و پار کردن تروریست‌های تجزیه طلب همچنان ادامه دارد</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/86460" target="_blank">📅 03:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86459">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔥
إصابة مباشرة ودقيقة.. انفجار كبير داخل مقر تابع لإرهابيي المعارضة الكردية في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/86459" target="_blank">📅 03:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86458">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/638cc24dc4.mp4?token=PGBTgPzYBgU25ZnDGB_MQykjh_haJR8xUIg1d4bGAnXIDVA4FOf2wq8AVLevHUZJZwf8gehSc79jK_P42MkJAdYMQkHz9TS6zNJD9LGNJ1glfPNSntNiEae4ijrmDW_zlWxiWt2dWu9bNFGwXFN25o6JF10uBu8lT6vMseZPuBntNX1hP3fbKdq2Xqsc4htJzNenf5ujF7eweBG9kl4Kl-Y6Ix_X0SWcp1dqvq30DA0BYhg3vPx-3fXfSr6_FVGLdosWlc8xJ_xlwIwYivnC_V-OHxl7UCg302SHcfYmYPUy-SI1Wb8qIBtmEoIRrmlr77EUuZXmUm8MzHYbq75Vsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/638cc24dc4.mp4?token=PGBTgPzYBgU25ZnDGB_MQykjh_haJR8xUIg1d4bGAnXIDVA4FOf2wq8AVLevHUZJZwf8gehSc79jK_P42MkJAdYMQkHz9TS6zNJD9LGNJ1glfPNSntNiEae4ijrmDW_zlWxiWt2dWu9bNFGwXFN25o6JF10uBu8lT6vMseZPuBntNX1hP3fbKdq2Xqsc4htJzNenf5ujF7eweBG9kl4Kl-Y6Ix_X0SWcp1dqvq30DA0BYhg3vPx-3fXfSr6_FVGLdosWlc8xJ_xlwIwYivnC_V-OHxl7UCg302SHcfYmYPUy-SI1Wb8qIBtmEoIRrmlr77EUuZXmUm8MzHYbq75Vsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجدداً.. سرب من المسيرات الإنتحارية يستهدف مقرات أخرى للمعارضة الكردية الإنفصالية في السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/86458" target="_blank">📅 03:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86457">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">استمرار الضربات على مقرات المعارضة الكردية في السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/86457" target="_blank">📅 03:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86456">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‏
حركة الجهاد الإسلامي:
نتحفظ على ما تم الإعلان عنه بشأن اتفاق غزة بصيغته المتداولة.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/86456" target="_blank">📅 03:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86455">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">انفجارات تهز قضاء خبات بمحافظة أربيل</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/86455" target="_blank">📅 03:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86454">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">انفجارات تهز قضاء خبات بمحافظة أربيل</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/86454" target="_blank">📅 03:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86453">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7058756733.mp4?token=kgDTFNmIjRRWXbASLKI2iBAzVlcCCE-2E-pPcQYYGWpI_fNfyD63iN1fbnnDoszebzFRUnu0xSIAaIq9Gul0RLjF09fr8osp4si-p-H4_PrpGZj42JTWZ_YCEoulSEfvqxCn5arI1wf7pIpjgbjuXiyzJU7Cf73jxh5vrlH2Kv6v9vy3h8JSPUTCm3yMeYB3awqEUwE7x6O9dFk1ZYG20iZiJreG6auzwjobFk3Jf-NlABCZ-OvF_xihhR6qJNgPnRIZig5Rliwkbxa5iYpoIO0SuW0QnP7veWjul1J0kVHxy9X-R4750X64WzkdNwHdj_VkcOhfU5Qvs1rRxf107Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7058756733.mp4?token=kgDTFNmIjRRWXbASLKI2iBAzVlcCCE-2E-pPcQYYGWpI_fNfyD63iN1fbnnDoszebzFRUnu0xSIAaIq9Gul0RLjF09fr8osp4si-p-H4_PrpGZj42JTWZ_YCEoulSEfvqxCn5arI1wf7pIpjgbjuXiyzJU7Cf73jxh5vrlH2Kv6v9vy3h8JSPUTCm3yMeYB3awqEUwE7x6O9dFk1ZYG20iZiJreG6auzwjobFk3Jf-NlABCZ-OvF_xihhR6qJNgPnRIZig5Rliwkbxa5iYpoIO0SuW0QnP7veWjul1J0kVHxy9X-R4750X64WzkdNwHdj_VkcOhfU5Qvs1rRxf107Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات ثانوية في مخازن الأسلحة جراء استهدافها بسرب من المسيرات الإنتحارية</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/86453" target="_blank">📅 03:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86452">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7efc44958b.mp4?token=PYLQxhTvT9kuLflW2VdxUaQyNLQOsaaXol4CRcBOIIHNyZxajaLLaawwqZlVnBc4plHOC2eTNNf2N_hOlJ-jZKUyn9OApTuagITx8TnUSvme74mS7V1hehNYGcf3Mem6F_Ji6q_n4nfc7VCSurgD25ITn1CAiMuDoimlSVeVHYO9S4JPwVZmTbALJ1MoR17CapnDyOya-8hLBqBH7lPku7mlT1EHyENkm_zYHNIChMO3oc5SBXr74fSyksYaoaCYbOyEeP3IthgbdNZK4z7UkY7ezl9SUCeP7Kk1v9LaD-3BO6hhyYsoFW4mjqTHW1sZ4LSfbuBNZpg_C9dn2ueOsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7efc44958b.mp4?token=PYLQxhTvT9kuLflW2VdxUaQyNLQOsaaXol4CRcBOIIHNyZxajaLLaawwqZlVnBc4plHOC2eTNNf2N_hOlJ-jZKUyn9OApTuagITx8TnUSvme74mS7V1hehNYGcf3Mem6F_Ji6q_n4nfc7VCSurgD25ITn1CAiMuDoimlSVeVHYO9S4JPwVZmTbALJ1MoR17CapnDyOya-8hLBqBH7lPku7mlT1EHyENkm_zYHNIChMO3oc5SBXr74fSyksYaoaCYbOyEeP3IthgbdNZK4z7UkY7ezl9SUCeP7Kk1v9LaD-3BO6hhyYsoFW4mjqTHW1sZ4LSfbuBNZpg_C9dn2ueOsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرائق واسعة في مقرات إرهابيي المعارضة الكردية الإيرانية في السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/86452" target="_blank">📅 03:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86450">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4193dea2c9.mp4?token=sZXvTae2plj358YdN1fAa3ZSvLYmpAYSPokgwZUkqyKhi7j2CbZ3bfsS_X8vjsaorL5ZAB0Ry9XdleHp-shn6Q055IykP8ePnJB8AocEBtYNkmq74A3NiUjQtMsPPbT5vHKMiPIYnynu_WShIdBNWbqdHgdbVLGnyuk7D_Q83dVC9NUrV2q8vpvxW0_1HEPeJzhnaBF2hrL-_kr8B0QA7-x-OK_57_JEcEp8HAyUTuuNkr_t5_d_YM6BFkjrSmp1oWenDGzYF1s2KHbwu0HSKBaYEWunPOgMqMMw9FJX_cRDPVJ5HT7OnZGKZAr1Pm1MjYQEQR-7YifWC-hx_C3gkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4193dea2c9.mp4?token=sZXvTae2plj358YdN1fAa3ZSvLYmpAYSPokgwZUkqyKhi7j2CbZ3bfsS_X8vjsaorL5ZAB0Ry9XdleHp-shn6Q055IykP8ePnJB8AocEBtYNkmq74A3NiUjQtMsPPbT5vHKMiPIYnynu_WShIdBNWbqdHgdbVLGnyuk7D_Q83dVC9NUrV2q8vpvxW0_1HEPeJzhnaBF2hrL-_kr8B0QA7-x-OK_57_JEcEp8HAyUTuuNkr_t5_d_YM6BFkjrSmp1oWenDGzYF1s2KHbwu0HSKBaYEWunPOgMqMMw9FJX_cRDPVJ5HT7OnZGKZAr1Pm1MjYQEQR-7YifWC-hx_C3gkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرائق واسعة في مقرات إرهابيي المعارضة الكردية الإيرانية في السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/86450" target="_blank">📅 03:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86449">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20fbbfd350.mp4?token=NGBj-oilp8MS8wNXuoVKLP4ZQhi3_-NwCjDVRyDKrsh_8JrE_UOYuyzAHPfO-JwD0h7K_B9BBVb7_RjikZkmaR27akwKSys8iPPyau1HDl_eGrbMBk_KbKDh1SXWe8qeOFzPwGih7J-rV0-5nBzZLcybEck8kObb3aSgOANYJCnLYECnVLEJijlX2yVyy_1ild5PewtuUaYbSr5oQvUh5N8Se0RdfTrYjjPkyExW_XNporZuw16BqZFt0eDkgcxORaACKNdq0emVP2ZjqYfaDguzVe_PtDdS-OoyJ92_FHj6j6L5HvFKupTdLNVzmU2xaUTboF3uWu6ZU4ogwVZXhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20fbbfd350.mp4?token=NGBj-oilp8MS8wNXuoVKLP4ZQhi3_-NwCjDVRyDKrsh_8JrE_UOYuyzAHPfO-JwD0h7K_B9BBVb7_RjikZkmaR27akwKSys8iPPyau1HDl_eGrbMBk_KbKDh1SXWe8qeOFzPwGih7J-rV0-5nBzZLcybEck8kObb3aSgOANYJCnLYECnVLEJijlX2yVyy_1ild5PewtuUaYbSr5oQvUh5N8Se0RdfTrYjjPkyExW_XNporZuw16BqZFt0eDkgcxORaACKNdq0emVP2ZjqYfaDguzVe_PtDdS-OoyJ92_FHj6j6L5HvFKupTdLNVzmU2xaUTboF3uWu6ZU4ogwVZXhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسيرات تستهدف مقرات المعارضة الكردية في السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/86449" target="_blank">📅 03:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86448">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/343f6cda6b.mp4?token=UTUecJVeFwNC0vS6laEFQz1ez3SfRhdUOwLpaFOCwu0WTbj01Xgtqfhau0oV_47GjNDFY9AW4XUWNoebW1vxxbkSAHsH1J2PADFZ2yCv28BQWA8RmqIPojl8aDtgBw28cH-_qM4nX0Fj2Kr5DepWssokwbqhxs6GSBZsp2M-Cyze53Bs9zeh7M0oqzfwK_I0i97zGHuaoeiNVIRH_CzDoUsUCUKm7LFdSeNg6ssGWUFEL4VMwDcecoqJmwSyvJP7SL9Ok0wTFXFq4pZcwHlDcNapOB0QBDFXnW7MKhc-SVbQ7234SJdxnv7c2wxyJo5cVM78sWSMQskoe6XNu71t5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/343f6cda6b.mp4?token=UTUecJVeFwNC0vS6laEFQz1ez3SfRhdUOwLpaFOCwu0WTbj01Xgtqfhau0oV_47GjNDFY9AW4XUWNoebW1vxxbkSAHsH1J2PADFZ2yCv28BQWA8RmqIPojl8aDtgBw28cH-_qM4nX0Fj2Kr5DepWssokwbqhxs6GSBZsp2M-Cyze53Bs9zeh7M0oqzfwK_I0i97zGHuaoeiNVIRH_CzDoUsUCUKm7LFdSeNg6ssGWUFEL4VMwDcecoqJmwSyvJP7SL9Ok0wTFXFq4pZcwHlDcNapOB0QBDFXnW7MKhc-SVbQ7234SJdxnv7c2wxyJo5cVM78sWSMQskoe6XNu71t5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسيرات تستهدف مقرات المعارضة الكردية في السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/86448" target="_blank">📅 03:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86447">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">مسيرات تستهدف مقرات المعارضة الكردية في السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/86447" target="_blank">📅 03:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86446">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AijjgwAi31NreALvL6gFxRRoGHnDihGB5mvvBZ5BE4M3OoBqhvfcvFVzkimFe1TUL0Lt2KEWQelLyQn8DLQXGTrHvC4g1EqG_yxNwTelqyoiQy70SPJl7872k74y7QUgmRkUeXf1yYlS3gjKl7tWIuvND8r3oqbNCzwn0RX6SXIEJu4j1bTpHzk0NFBJUpLhFwbiiQFST9wdCTyCFF2JB7042v3q8wEWOVLZrwqYXhnO-Fb-Dfp2jfZKaJzXt3Py9rXHwXfvwBHObvSTfd2-BpItZGoaM9aTYysxxUFIH3MTlMKLu9NGbeS0uwBBQJQMjAItA0sNVD89J-ic7NK_2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
اليوم، توصل مجلس السلام إلى اتفاق تاريخي لنزع السلاح الكامل لحماس وجميع الجماعات المسلحة الأخرى في غزة. هذه خطوة هائلة نحو السلام والأمن الدائمين.
يعد هذا الاتفاق خطوة حاسمة نحو حكم غزة أخيرا من قبل حكومة فلسطينية جديدة ستعمل عن كثب مع مجلس السلام لمساعدة الشعب الفلسطيني. وفي الوقت نفسه، سيكون لدى إسرائيل الأمن الذي تستحقه، حيث لم تعد غزة تستخدم كقاعدة للهجمات الإرهابية.
هذا معلم رئيسي في تنفيذ خطة ترامب المكونة من 20 نقطة. سيتم تنفيذ الاتفاقية على مراحل منظمة بعناية. مع اكتمال نزع السلاح، ستنسحب القوات الإسرائيلية، وستعمل قوة الاستقرار الدولية مع قوة شرطة فلسطينية جديدة لتحمل المسؤولية عن سلامة غزة لسكانها وجيرانها.
قبل عام واحد كانت هناك حرب عنيفة مستعرة وأزمة إنسانية واحتجز الرهائن في الأسر الوحشي. لقد أحرزنا تقدما تاريخيا ولا يزال هناك الكثير من العمل الذي يتعين القيام به.
أود أن أشكر الوسطاء - مصر وقطر وتركيا - على جهودهم الهامة، وخاصة فريقي المتميز، الذي جعل عمله الدؤوب هذا الاختراق التاريخي ممكنا.
لن يسمح بإعادة بناء التهديد الذي ظهر من غزة في 7 أكتوبر!
بموجب هذا الاتفاق، ستكون غزة أخيرا في أيدي حكومة فلسطينية جديدة تخدم شعبها.
تهانينا للجميع على هذا التطور المذهل، الذي قال الجميع إنه لا يمكن تحقيقه أبدا!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/86446" target="_blank">📅 01:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86445">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇸🇾
‏الجولاني يستنكر محاولة استهداف ميليشيات تابعة لإيران في العراق للمنشآت البترولية السعودية.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/86445" target="_blank">📅 01:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86444">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee6571e4ae.mp4?token=bolDGNn9SOu--yaRi-sOeSbNSjuGIGlyyi1z17SJoVsGltRZoeq6gI5K4mLRfYWfCWNWKlgYe42uBuo2MShlB7sYLa1PBAVsM_bxPahCB_UjxBQeGyxR7v2hBudEaEswq6ql74-BrAxXCXUJ-QWkEB6hvygRMN-gY1_Q4FweOuLtK5xnx0fnevhAROJuYAWuFWaisDrRK5sIrp__Q-v9gUOA3bObIBBEvoZdxm4aXhAMLcfJ7TrVh_xuxIjT0pOGtiJCHfPvHVCSbY_x8cq5ghI5aoSn8DXaFbqCKeM9YtEcvcjTaagslp7H0K0KXQyon0Zk8SdgDo4wOnhAQx2FHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee6571e4ae.mp4?token=bolDGNn9SOu--yaRi-sOeSbNSjuGIGlyyi1z17SJoVsGltRZoeq6gI5K4mLRfYWfCWNWKlgYe42uBuo2MShlB7sYLa1PBAVsM_bxPahCB_UjxBQeGyxR7v2hBudEaEswq6ql74-BrAxXCXUJ-QWkEB6hvygRMN-gY1_Q4FweOuLtK5xnx0fnevhAROJuYAWuFWaisDrRK5sIrp__Q-v9gUOA3bObIBBEvoZdxm4aXhAMLcfJ7TrVh_xuxIjT0pOGtiJCHfPvHVCSbY_x8cq5ghI5aoSn8DXaFbqCKeM9YtEcvcjTaagslp7H0K0KXQyon0Zk8SdgDo4wOnhAQx2FHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
‏نتنياهو  وكاتس : تدمير أنفاق قلعة الشقيف جاءت رداً على خرق حزب الله لاتفاق وقف النار.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/86444" target="_blank">📅 01:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86443">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇮🇶
طيران حربي معادي منخفض في اجواء سهل نينوى بمحافظة نينوى شمالي العراق.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/86443" target="_blank">📅 00:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86442">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65aa1a707f.mp4?token=Kt4sShBJR-2Dx29TzZz_l_SmZmFvWQBTfNJjk_2IsGMx7Geak7s0n5SP-rawVP3ehAAPBKYcqOGjzZJbNsDbACDw1WctyfoR2xB8sxhDYJecZJpp-ja-i37uv_vIuTzuJhcbk_mFGQTzxEPO3AMgKN5kFnpIOEMR_SemxprdUu-l7jCsdaRMMO2QoPz6g_yXVLO8VzYYSXMRdkKUV_zyXdckU7mM0euPyxJkttD8utZX9m-ynR7uS7pmdSnL2Zp1aV4zKnI6FzoVZ65-ypw0NhTiQOPDutrA7URGBYDMu7GFsTs4_AVvzwrM35iyq3kWATgY-FSrQEKCb-S8ot1AmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65aa1a707f.mp4?token=Kt4sShBJR-2Dx29TzZz_l_SmZmFvWQBTfNJjk_2IsGMx7Geak7s0n5SP-rawVP3ehAAPBKYcqOGjzZJbNsDbACDw1WctyfoR2xB8sxhDYJecZJpp-ja-i37uv_vIuTzuJhcbk_mFGQTzxEPO3AMgKN5kFnpIOEMR_SemxprdUu-l7jCsdaRMMO2QoPz6g_yXVLO8VzYYSXMRdkKUV_zyXdckU7mM0euPyxJkttD8utZX9m-ynR7uS7pmdSnL2Zp1aV4zKnI6FzoVZ65-ypw0NhTiQOPDutrA7URGBYDMu7GFsTs4_AVvzwrM35iyq3kWATgY-FSrQEKCb-S8ot1AmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الذكرى السنوية لرحيل المجاهد القائد الكبير ابو حسن المالكي ورفاقه
هذا وين الگال ما عدهم رجال
بالنجف مدفون حماي الحمى</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/86442" target="_blank">📅 00:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86441">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇮🇱
‏
نتنياهو  وكاتس :
تدمير أنفاق قلعة الشقيف جاءت رداً على خرق حزب الله لاتفاق وقف النار.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/86441" target="_blank">📅 00:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86440">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇪🇬
🇮🇱
‏جيش العدو الإسرائيلي ينفي الادعاءات باستهداف ميناء دمياط في مصر.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/86440" target="_blank">📅 00:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86439">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">الاعلام الاجنبي:
‏أصر الوسيط الباكستاني يوم الخميس على أن المفاوضات بين إيران والولايات المتحدة لا تزال جارية، حتى مع قيام واشنطن بتنفيذ "موجة كبيرة من الضربات" على خصمها رداً على هجمات جديدة استهدفت الأردن.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/86439" target="_blank">📅 23:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86438">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-zFVqSvH_Fw4agpLfD98Gk3PvC0BZXVpIehiVX4rBQpKl8PXQR8S7bg1o-1VHUR75Yv98-Uhgj1EGwWhKVgVXSvQQZoS4i5GE21KXpJFMH7e5w745dsoApPMf5Ktj3G8YUEekoCslr2wM4AQNTRk2y_oek6jWCG4LmkfQvX2CcpIHMKBhATUMgtaPp3lPPyWXn8pr3vi3bNGwn-R729JWjPbZ6aOJhPOUsCtMevXCxk_O0ARYPnPks4EgDxhU4WcHRvQldcw-eznJewq4VQ4KE5v8Mn0TVn8YqFTgVZTe083LIE1seP1NygEsXc2BAY0JhQ26W7gUO4Ie62xAgjyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقجي:
مصر صديق وشريك مهم في المنطقة، وأمنها ذو أهمية قصوى بالنسبة لنا.
يجب علينا جميعًا توخي الحذر من المؤامرات الإسرائيلية والعمليات المضللة التي تهدف إلى تقويض السلام الإقليمي.
التهديد واضح ومتبادل، ويخشى التضامن الإسلامي.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/86438" target="_blank">📅 23:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86437">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇮🇶
المتحدث باسم الحكومة العراقية: الحكومة لم تمنح أي موافقة لتنفيذ اعتداءات على مواقع معينة أو جماعات محددة داخل الأراضي العراقية، والحكومة ليس لديها أي علم مسبق بتنفيذ الاعتداءات على الأراضي العراقية،و تعليق زيارة رئيس الوزراء إلى السعودية بعد الاعتداءات الأخيرة…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/86437" target="_blank">📅 23:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86436">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a56c23c8e.mp4?token=D8A7oc_Lgumm5KTzOUuqjFeV_IcU_xra-wmCAZX4WykeBYWFLu5hPqxmY6z3McfVUb9Om7JFyv7js0SlfrSf5eUv3Tb7OkOfZpdIPFOHs6U82R6do7YjZIJZSiGS5KF75foVJo2OlYeJQ5E_8Ly5HMYZBjUXWI7LDjNBRtFeQ2NXelgidYDq7OCeQ087_2vxa7z99ZBZPmCiDjwOoMRH5enD0JEctZV-_wzgmw7Nmn0OQ6A8Q8vcVYDYbgnerf8nYhBiZhNJsEEOMGq65GyEocEyMYc-TZFOXBd5kL99EMhfbr9I74l6kPvaGSitpjFAa3jvYS75b7XnHKviIOix_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a56c23c8e.mp4?token=D8A7oc_Lgumm5KTzOUuqjFeV_IcU_xra-wmCAZX4WykeBYWFLu5hPqxmY6z3McfVUb9Om7JFyv7js0SlfrSf5eUv3Tb7OkOfZpdIPFOHs6U82R6do7YjZIJZSiGS5KF75foVJo2OlYeJQ5E_8Ly5HMYZBjUXWI7LDjNBRtFeQ2NXelgidYDq7OCeQ087_2vxa7z99ZBZPmCiDjwOoMRH5enD0JEctZV-_wzgmw7Nmn0OQ6A8Q8vcVYDYbgnerf8nYhBiZhNJsEEOMGq65GyEocEyMYc-TZFOXBd5kL99EMhfbr9I74l6kPvaGSitpjFAa3jvYS75b7XnHKviIOix_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمليات هبوط واقلاع من قاعدة موفق السلطي بالاردن منذ عصر اليوم والى الان.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/86436" target="_blank">📅 23:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86435">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇮🇶
المتحدث باسم الحكومة العراقية:
الحكومة لم تمنح أي موافقة لتنفيذ اعتداءات على مواقع معينة أو جماعات محددة داخل الأراضي العراقية، والحكومة ليس لديها أي علم مسبق بتنفيذ الاعتداءات على الأراضي العراقية،و تعليق زيارة رئيس الوزراء إلى السعودية بعد الاعتداءات الأخيرة والحكومة العراقية خاطبت السعودية لتقديم الأدلة حول ادعاءات الهجمات.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/86435" target="_blank">📅 22:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86434">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b961f0162.mp4?token=gKTYYQmtkdkqFGSWMHl79IRIkNG5Ms6wVKhh1kfmDPyhy5-65GcevJMmDAb-YAzAujGFRcj-pBRpExDCWGjxiytacb3tNaO4llRsmjp3_ohkDopwttPppSsmfhH5O3Nr_AZqiTqd3Vvs_CiQND8ibdkR2JDlxragwOrNOyoCo4u9eF1ngqUSfGwpPSlMr7nfbw2j5UsToW7U2Y_nXsyPhe-GA4rKKZOaBAU1so75z6yXgYr0XnuKTrgk4CmD6yyGv4CynnQl7f2Npo8enGaUAcGY9UsgQQFwFX_GpOEHLvNwNOECU8EooiXMyltY1cpTW6Amvy3EuYYfEKqhcYWl4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b961f0162.mp4?token=gKTYYQmtkdkqFGSWMHl79IRIkNG5Ms6wVKhh1kfmDPyhy5-65GcevJMmDAb-YAzAujGFRcj-pBRpExDCWGjxiytacb3tNaO4llRsmjp3_ohkDopwttPppSsmfhH5O3Nr_AZqiTqd3Vvs_CiQND8ibdkR2JDlxragwOrNOyoCo4u9eF1ngqUSfGwpPSlMr7nfbw2j5UsToW7U2Y_nXsyPhe-GA4rKKZOaBAU1so75z6yXgYr0XnuKTrgk4CmD6yyGv4CynnQl7f2Npo8enGaUAcGY9UsgQQFwFX_GpOEHLvNwNOECU8EooiXMyltY1cpTW6Amvy3EuYYfEKqhcYWl4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
سماحة الشهيد سيد حسن نصرالله (رضوان الله عليه) قالها سابقا
"كيف يمكن لأناسٍ طبيعيين أن ينظروا بعين الود والمحبة إلى السعوديين"</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/86434" target="_blank">📅 22:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86433">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/86433" target="_blank">📅 22:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86432">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elyF_VeujOFyn7TD_--z8Mwf5O2Txx8012l_YviZoZjelsLPmxxlgOx84kN3hC9cAWfQfVb-BU-0dgDvClKVOZBvoVQC0IrTDZsob-vAdEi8ql8jAFZgwu4ccaEHDRKph8e2KSKbhrf9aXThXg5DsnP6kHq3oAm-J7PUfnhcfDvaoTKGRlbWDNrtHpfYBBPRWwGmSsR35jnc2aGp8etMzn6_4rqrsYY07yZC2tWig6A0pgpa_QOyVIyU3s32hmQS9BbD5JV7zyvOMQACTeNBCtwlSzelh7BAsiAE6G-Oo9PegA3hjKVkqJubCBiApnHMgzrzWzFV_bybjH76D8MWWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
جمهورنا الكريم
...
🔻
لغرض التواصل معنا ونقل مشاكلكم وارسال الاخبار والمواد الصورية والفديوات ، سنكون على مدار الساعة معكم نجيبكم.
للمراسلة
@Nayaforiraq_bot</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/86432" target="_blank">📅 22:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86431">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇮🇶
🇷🇺
الخطوط الجوية العراقية تستأنف رحلاتها إلى موسكو بعد توقف دام 5 شهور.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/86431" target="_blank">📅 22:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86429">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58a90d4340.mp4?token=qVHft9boGr3kbBIeF_JHzCTN95OesIv_zx8QCqCiXpn7ZVjkzZRKF7ZV8K1VlnBGtDOQ52pa4uJYXiytRgr3CKP0zY6b8nNw0P3tvP5hrFrxe4WGEMzhowqRHbbDtHwM6qkWpcm-gYKt3ZhBjnoOBLw9IdXXio8Oe1jbqUN3Ux4p0ehJlbj0WWbFwX9_IqGV3ZxDZhMdtwe6CgMZwg7n4ZS4dKReahWbQOgoNCxNGJaPSsk1yHQ9MRcDnOYJb021_2kDHONt2fg8iQ268tqGyG6kLaxzknm-bFitkSoSjz3P12AcoRy9Jk7ahxSsA-73PfMBIdJIum0l6gGIugVjAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58a90d4340.mp4?token=qVHft9boGr3kbBIeF_JHzCTN95OesIv_zx8QCqCiXpn7ZVjkzZRKF7ZV8K1VlnBGtDOQ52pa4uJYXiytRgr3CKP0zY6b8nNw0P3tvP5hrFrxe4WGEMzhowqRHbbDtHwM6qkWpcm-gYKt3ZhBjnoOBLw9IdXXio8Oe1jbqUN3Ux4p0ehJlbj0WWbFwX9_IqGV3ZxDZhMdtwe6CgMZwg7n4ZS4dKReahWbQOgoNCxNGJaPSsk1yHQ9MRcDnOYJb021_2kDHONt2fg8iQ268tqGyG6kLaxzknm-bFitkSoSjz3P12AcoRy9Jk7ahxSsA-73PfMBIdJIum0l6gGIugVjAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمليات هبوط واقلاع من قاعدة موفق السلطي بالاردن منذ عصر اليوم والى الان.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/86429" target="_blank">📅 22:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86428">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇶
من تشييع جثاميين الطاهرة للشهداء الذين استشهدو في القصف السعودي على الاراضي العراقية.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/86428" target="_blank">📅 21:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86427">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇶
‏اعلام السعودي: بعثات غربية في بغداد أعادت تنظيم حركة كوادرها وقلصت التنقلات الخارجية.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/86427" target="_blank">📅 21:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86426">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇮🇶
‏الاعلام السعودي: السفارة الأميركية في بغداد تصدر تعليمات تقضي بتقييد حركة موظفيها.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/86426" target="_blank">📅 21:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86425">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇮🇶
‏
الاعلام السعودي:
السفارة الأميركية في بغداد تصدر تعليمات تقضي بتقييد حركة موظفيها.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/86425" target="_blank">📅 21:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86424">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ae498044a.mp4?token=b76p15bM5ak1KoT6PAUdQU8xhQmOqrHLDpJsWwl8a4MAv_WEl-DLGgDjhpTepjSNTgXKLZA1VaTUy92-urS15q4dcvDbQjkPbM21L4lWYpY7m5hVWL2fktOo1_nblkToW7OPUeFAjWdwCmW2fl0TjFaoOUvPYLVOKkEotJyiRYmOq4mYvR5LWw09F0uLHP0JySX2f5Ai_OJJh-pI4KJxu59R9of6htWpmHKt7wy-YHUTyUB2ZAKHHUWH4KwXWvhS1W5EOWJ-Opm2u7TvcGrCkWsl7uDQp5m3zP-U0e-Qo6tDsSNYUXR0hIzjBU6Tqluwj-bnENoR20MrjrtcUB3ZAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ae498044a.mp4?token=b76p15bM5ak1KoT6PAUdQU8xhQmOqrHLDpJsWwl8a4MAv_WEl-DLGgDjhpTepjSNTgXKLZA1VaTUy92-urS15q4dcvDbQjkPbM21L4lWYpY7m5hVWL2fktOo1_nblkToW7OPUeFAjWdwCmW2fl0TjFaoOUvPYLVOKkEotJyiRYmOq4mYvR5LWw09F0uLHP0JySX2f5Ai_OJJh-pI4KJxu59R9of6htWpmHKt7wy-YHUTyUB2ZAKHHUWH4KwXWvhS1W5EOWJ-Opm2u7TvcGrCkWsl7uDQp5m3zP-U0e-Qo6tDsSNYUXR0hIzjBU6Tqluwj-bnENoR20MrjrtcUB3ZAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بيان العلاقات العامة للجيش في المرحلة السادسة والعشرين من عملية البرق، وانتقامًا لدماء الشهيد الأمير العميد ماجد كاظمي، الطيار الشجاع لطائرة سوخوي 24
التابعة لسلاح الجو الإيراني استهدفت طائرات إيرانية مسيرة مولدات الكهرباء وأنظمة الملاحة والمباني الإدارية والمساندة التابعة للجيش الأمريكي في قاعدة الشيخ عيسى
أسفرت هجمات الأيام الماضية، وكذلك الليلة، على القواعد الأمريكية في المنطقة، رغم أنظمة الدفاع والمعدات المتطورة فيها، عن أضرار جسيمة في معدات ومراكز انتشار القوات الأمريكية.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/86424" target="_blank">📅 21:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86423">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇺🇸
مجلس الشيوخ الأمريكي
يصوت ضد مشروع قرار لوقف العمليات العسكرية ضد إيران.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/86423" target="_blank">📅 20:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86422">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇪🇬
البحرية البريطانية تؤكد تعرض سفينتين في مصر لاستهداف بواسطة مسيرتين.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/86422" target="_blank">📅 20:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86421">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‏
الخارجية الفرنسية:
إغلاق مضيق هرمز يؤثر على اقتصاد العالم.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/86421" target="_blank">📅 20:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86420">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80be21696.mp4?token=qFQjCRVJiudBVGfgFeH_LhcwBmbBK-fR5gxBvfRDwtWURsRlGkFKsAf_2tsKPeXEaiNjTuPhl41JmVlaYZnIJ5kEMiTjirY9o-LpreSS-4LE7p2Zpv2KZZ_SJQCLA5SBjELD5fM-dO8i4F4KuXUXFAoZIKs-Yi5O7hbUnMOqRpgT6W-rqx9Zs_MEezjY9_Zy_p1nIafrnggiov1x4fEANddnEnVBpay4aPvKf8Pne1JrW9Cqtz66qwRWbFbdQcx3kDyCkZJbsRoV__RJRVnF7MlPPa5aq2wCNvtZjiuBbtREj0GgUH9KLbG58AjT8G0XrRV5V3WAOxq7m1gni4KZ8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80be21696.mp4?token=qFQjCRVJiudBVGfgFeH_LhcwBmbBK-fR5gxBvfRDwtWURsRlGkFKsAf_2tsKPeXEaiNjTuPhl41JmVlaYZnIJ5kEMiTjirY9o-LpreSS-4LE7p2Zpv2KZZ_SJQCLA5SBjELD5fM-dO8i4F4KuXUXFAoZIKs-Yi5O7hbUnMOqRpgT6W-rqx9Zs_MEezjY9_Zy_p1nIafrnggiov1x4fEANddnEnVBpay4aPvKf8Pne1JrW9Cqtz66qwRWbFbdQcx3kDyCkZJbsRoV__RJRVnF7MlPPa5aq2wCNvtZjiuBbtREj0GgUH9KLbG58AjT8G0XrRV5V3WAOxq7m1gni4KZ8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
سماع صوت طيران مسير في قضاء كوية بمحافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/86420" target="_blank">📅 20:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86419">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phQQuJctdiG2t3ZUrZME-9EVsJuRNhF9UPeef-J5UwFfWXW2Zd19U2XBJKxsSWSuixNLd-7tK4QYC0DSUUIVSVrXUKhWg4OApgDhxQVM3mt5SXDEtt7LYTj5ndjYobA4D5VE5H-E4n26g1JR4U8ZIieiNdt16mcgrwct2xLSv_WLEe3Ea1lucccNHBwzR0ELtd7brnZyN8vLl68a3HPABt0jBt4U3D0h2R8E-HyVX3s-cON871cyW3o5ASJQSZ96LAUChTtUJf672UO5pIm1tIlEGfFNwWVrwZVQwRaX2bc4jgUBOd2IWY_qAVkcPZLVWuuVKI3TpZHDF5lLuJRUWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الاعلام الاجنبي‏: السلطات المصرية حملت إيران مسؤولية الهجوم على ميناء دمياط.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/86419" target="_blank">📅 19:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86418">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95f68ec6f4.mp4?token=Nqo6Ri8L7-LgsFCdPGr22o96gg5iTYWe49shrVXHPY6-C5LIgsVUjXMkTyaXCocgUWQHk3Ij-0yT7HLxn9_7sW0AynRVFFvb5hErFph_ecwG8kj8ZtxTubHihEXipvXADOkTXAmG37Z4kUREwep-qGYeFRDgw32bP89qzzg5JTlrwCccDAGCumk5LFO8jDTrZddLGKo7nslfSrKWRyqwPczFbhxmPuR6Mz36xO3zWKIBWGf0mCFhf6ajUyvMheyd5Z0gcblU3mo4k5zVdxKGVo-DVPeZoPUcbVDd5Sd-FV1B8gJtzdtpetcQ5OPX7QbbEhCKdJ4DLCtWSaEEwY8fiTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95f68ec6f4.mp4?token=Nqo6Ri8L7-LgsFCdPGr22o96gg5iTYWe49shrVXHPY6-C5LIgsVUjXMkTyaXCocgUWQHk3Ij-0yT7HLxn9_7sW0AynRVFFvb5hErFph_ecwG8kj8ZtxTubHihEXipvXADOkTXAmG37Z4kUREwep-qGYeFRDgw32bP89qzzg5JTlrwCccDAGCumk5LFO8jDTrZddLGKo7nslfSrKWRyqwPczFbhxmPuR6Mz36xO3zWKIBWGf0mCFhf6ajUyvMheyd5Z0gcblU3mo4k5zVdxKGVo-DVPeZoPUcbVDd5Sd-FV1B8gJtzdtpetcQ5OPX7QbbEhCKdJ4DLCtWSaEEwY8fiTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
نتنياهو
: عمدة نيويورك زهران مامداني، "يدعم إيران وحماس وحزب الله".</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/86418" target="_blank">📅 19:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86417">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ace29ffb85.mp4?token=cnKnpy-1HMksHgusQ9nubbxPOhmGWTTrtFNjJrufMrGnQIgjl49NYOegf3sXq36tShaeTM0SqNwJWwDjD6dsfOPFcuJO4S833ALD5A7t3zoJk_gWBneL_ss_6ZYpOCZCFxEZOAbXi3iY6BPLY979LPUblCEsLXSpctWaPUjbzfTTSGzJNtd3885tBN6EcK35JpSP1dYu9_ZuIV0_1A9zNvoe2DVzoKH8PGCwy-H1SVx9-5S52xZVveNeQjcgNF26RD8cTwr_7mloM_cDnYWCm5rjXSr8kmSjcSJxkVFB7nArPUxYfYSbYtzx-Q7ECdH0mtQFhOkQrtgJIJT_dRxBpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ace29ffb85.mp4?token=cnKnpy-1HMksHgusQ9nubbxPOhmGWTTrtFNjJrufMrGnQIgjl49NYOegf3sXq36tShaeTM0SqNwJWwDjD6dsfOPFcuJO4S833ALD5A7t3zoJk_gWBneL_ss_6ZYpOCZCFxEZOAbXi3iY6BPLY979LPUblCEsLXSpctWaPUjbzfTTSGzJNtd3885tBN6EcK35JpSP1dYu9_ZuIV0_1A9zNvoe2DVzoKH8PGCwy-H1SVx9-5S52xZVveNeQjcgNF26RD8cTwr_7mloM_cDnYWCm5rjXSr8kmSjcSJxkVFB7nArPUxYfYSbYtzx-Q7ECdH0mtQFhOkQrtgJIJT_dRxBpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
من تشييع جثاميين الطاهرة للشهداء الذين استشهدو في القصف السعودي على الاراضي العراقية.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/86417" target="_blank">📅 19:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86416">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/987b1f2bad.mp4?token=UUQrObsTQ-2uffNnIxgcYhnJUDxQQkj2cCPODraKztFmvG-G8EXi7njebKuskEefBJt8fI9_1ZqKgLGyOaDKF_yIHP--Zq_BQa2hFs8stIwjMC_YcomPBRgimTNaQRkA_Xq4qtkVXokUVf8L8tV-pwsIcKXQgrmMvScqeeRHEgWMwKKXLmZhZ4c_iyJ65rY9X3mIEqQU8mZDvSr4OuN2s1UJVCa7KCEuBPLPsASMl8_Py7O2cqe_yWMKg_0UL9HAuk64kwr4obBg3lTfkBBiCqkj9GIL9QxDaYgiEZCwYCJxh5X9mhRTYWlH7KayKzXAF6-TEtKiwerZJLlDpW_w6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/987b1f2bad.mp4?token=UUQrObsTQ-2uffNnIxgcYhnJUDxQQkj2cCPODraKztFmvG-G8EXi7njebKuskEefBJt8fI9_1ZqKgLGyOaDKF_yIHP--Zq_BQa2hFs8stIwjMC_YcomPBRgimTNaQRkA_Xq4qtkVXokUVf8L8tV-pwsIcKXQgrmMvScqeeRHEgWMwKKXLmZhZ4c_iyJ65rY9X3mIEqQU8mZDvSr4OuN2s1UJVCa7KCEuBPLPsASMl8_Py7O2cqe_yWMKg_0UL9HAuk64kwr4obBg3lTfkBBiCqkj9GIL9QxDaYgiEZCwYCJxh5X9mhRTYWlH7KayKzXAF6-TEtKiwerZJLlDpW_w6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
طيران مسير معادي في سماء محافظة البصرة جنوبي العراق.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/86416" target="_blank">📅 19:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86415">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">الاعلام الاجنبي‏:
السلطات المصرية حملت إيران مسؤولية الهجوم على ميناء دمياط.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/86415" target="_blank">📅 19:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86414">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇮🇶
سماع صوت طيران مسير في قضاء كوية بمحافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/86414" target="_blank">📅 19:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86410">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fHZ7GUmeLIfAIErkbL_p2A3YS9M8JvOvgj0dhKqSS3Us7eLIsDGLkXgWqeqtD60YRcz_CdD54S_x7Jequ4SU3exQzFl6b5g8vANTmup-sv4VC1IFpE7BLeANzmups5oP-9XOT-4VUaW_Kh2ZGcG3V-PYP6E0Ovq0i5GzorNw10sF--I1mmmpukIF3q77juqkFrvkf8r8SaXtdW22zSNPQGR4BOJJWOzRccLyUrcma0zkORSHKpCaqnjDqmyyXPvhee6ljaixuMPTkps2w29IKybfvawjUOJkEVSVuDWBNqPiLIYgulMn2gFcHcAIl5jDDJSCw7r9TxySkD_QLndUHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PE_T4kQjCRYDz5CVrIEk6QN40ACuwLrZuR6o0dI4k-JHzX1oLdHsZ0fiI6YmdRgHAHwltQ2wo1jm9iVY3HwitF_h6tZWZUUod6YfxhKqP1tggmM9xa8BMO2A2y7QAzEJ5vPJgnHynzwJsO4Q-KmGC7zNidAD-5zo0BfgUVMWG4yfDtCCBn0ZXX7ymhj3jT3BTUligIe_rW7bZYomLUzDN3nK3zbZgScOVAZYAV4-ftIffy7GDkDy--yZgmBkHP5-nRr579dMJAQhFheqP7tQWAdCaSryCQOSzJIM_l8KZp2P265CYT3lkRuuDkRR2nhwzLP4DJ8fl1OHUYYFcXDDCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XVMsSZ-HMfxPRgQUzyO551svjhIFC-82O66_65QhZTV6IFx4OxUi3MuNC7FhpF7bAeDp5ixvdS3AV0gkAX6PksVpbaca__GoQ767BmJRxKDt7Z8iqFB1dAN3Rn9UK5-s-W4JZjNGnNE5xbkcycqRn2Xs28vfp7tLfeOu-SE2YZeetBivKKsERd9KEr7r-1yk5nJX_jX8k9bo4wnKJihs2N_avC_qEaLg-OatmGuVQ68N2GjIfaTYWJs7xTaUv7rczm-IgvadCSN8UvgnIuN3Vhkae_vjCnMMkCiHAnzaAPcrDmdXwRg62M6EE-l8Gv72rfWofeaIZpZ7fD3XdGz1Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kRDJBTS4QrGPlAa9poS1SJQcp0YaGlCx5AqleY9t9XxqV80WbdK7K3__5DOoeUr2GVZFdd9oIBlllWwiCtRPAaRDwIvDO7BDHNibcPHiazAFpyYeAvekaHfdHYBpWPYS5H2yZFRA6KeLXh-XRdEyGCee2KF_OwcdtdsQ9JGdhm4BeDsPvEEMpf9nhC0QZxYAMnIw0PMCMu6rb6MYHKWn5jlmUlaZUzkk0Or9CsNC6xfGFTT0BCBWajylHe4mnpYLKLrXeY7bLqgPNiLaqVqDyr60ZGmZyJnUvQ5BGVNpns1O6Gq7-PqOpWyLMlRKzOVcvXWhGDaTqQBUHxxyc5TX7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
🇮🇷
تشييع مهيب لجثامين شهداء الاعتداءات الاميركية السعودية الغادرة في كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/86410" target="_blank">📅 19:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86409">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‏وافقت الاتحادات الوطنية الـ 55 التابعة للاتحاد الأوروبي لكرة القدم بالإجماع على مقاطعة كأس العالم وجميع مسابقات الفيفا إذا مضى جياني إنفانتينو قدماً في خططه لبيع جزء من الفيفا لمستثمرين من القطاع الخاص.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/86409" target="_blank">📅 19:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86408">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8dcb22e88.mp4?token=Bq87OipJBEGH6nRnjVlICgxYyCDp916aOlVU8ZVqpSwxQKQ_B8zjMGiMt9FE7j_krK40RuzAHw2qLJ8sFBa0GVt8tLHv_r3LxnbixgblqcbDgCewUso5OoZqCMa31MZ1DUNb6mlVCgya9dMbIvAsJ-4aLsHHqzxKTMq4Ic67DirxSBgONX0qpVQ7IribFqjaG1tGQL5IA8e9YQb-M1yqdrWMbeVEvAEq57i5De59oi8OGJzLjxNdkAq6iDsvzyJ3AJGxTV9lFP5K7XDGJ1GuFCwo550NnUMHsbwvYovA2jyWip6fFsVGzA2kr5O6xAet5fbUNIjlPrtu90yJsuSntQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8dcb22e88.mp4?token=Bq87OipJBEGH6nRnjVlICgxYyCDp916aOlVU8ZVqpSwxQKQ_B8zjMGiMt9FE7j_krK40RuzAHw2qLJ8sFBa0GVt8tLHv_r3LxnbixgblqcbDgCewUso5OoZqCMa31MZ1DUNb6mlVCgya9dMbIvAsJ-4aLsHHqzxKTMq4Ic67DirxSBgONX0qpVQ7IribFqjaG1tGQL5IA8e9YQb-M1yqdrWMbeVEvAEq57i5De59oi8OGJzLjxNdkAq6iDsvzyJ3AJGxTV9lFP5K7XDGJ1GuFCwo550NnUMHsbwvYovA2jyWip6fFsVGzA2kr5O6xAet5fbUNIjlPrtu90yJsuSntQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇺🇸
سنتكوم تنشر تسجيلًا صوتيًا تزعم أنه يوثق تهديدًا منسوبًا للحرس الثوري للسفن التي تحاول عبور مضيق هرمز لمخالفتها قوانين وتعليمات العبور.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/86408" target="_blank">📅 18:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86406">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇶
🇾🇪
🔻
رويترز : قال مسؤولان في المنطقة إن الحوثيين اليمنيين هاجموا السعودية هذا الأسبوع من الأراضي العراقية بالتنسيق مع الجماعات المسلحة العراقية، وفقاً لتقييمات أجرتها السعودية وشركاؤها الإقليميون، مما يعكس تزايد التنسيق بين الميليشيات الموالية لإيران.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/86406" target="_blank">📅 18:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86405">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db13ec2079.mp4?token=LG24BfUBPS1HPp5qQ1goIEZW0USkCJ_yxVgSM1JGKjgqoPgUwXe0pEbe3QvTGWCeqoHeeLfQLVeGpSnj_Y3VPEOpsFiAasLweH5pPZ8LHNN5LKAYw4iBbQVTedlZ20bEHGAARLQVgZQhyUduP7x-7QsM3m8b4TS0gmtkt8PdJceOFbG43yXe5Ui98MnwXjYfHMNGQN8Naa2wCeBN0l473_BIdc--3-IBgiZ5fse8eb3UOuEJGabcAAnFb2ZTLrSACTK-BA2TTVyR9AabgYmkr5_yNFhGQ1-C4z3ut_RgamWxEvCdy4WjuN3Os9rXP8yU735iwq-GW3xj0WGw56M9Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db13ec2079.mp4?token=LG24BfUBPS1HPp5qQ1goIEZW0USkCJ_yxVgSM1JGKjgqoPgUwXe0pEbe3QvTGWCeqoHeeLfQLVeGpSnj_Y3VPEOpsFiAasLweH5pPZ8LHNN5LKAYw4iBbQVTedlZ20bEHGAARLQVgZQhyUduP7x-7QsM3m8b4TS0gmtkt8PdJceOFbG43yXe5Ui98MnwXjYfHMNGQN8Naa2wCeBN0l473_BIdc--3-IBgiZ5fse8eb3UOuEJGabcAAnFb2ZTLrSACTK-BA2TTVyR9AabgYmkr5_yNFhGQ1-C4z3ut_RgamWxEvCdy4WjuN3Os9rXP8yU735iwq-GW3xj0WGw56M9Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عدوان يستهدف العاصمة اليمنية صنعاء</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/86405" target="_blank">📅 18:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86404">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">هزة أرضية في محافظة كركوك</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/86404" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86403">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">انباء عن انفجارات في صنعاء</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/86403" target="_blank">📅 18:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86402">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">انباء عن انفجارات في صنعاء</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/86402" target="_blank">📅 18:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86401">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">السيد عبدالملك الحوثي: ترامب يقول بنفسه عن السعودي بأنه بقرة حلوب يحلبونها حتى يجف ضرعها ثم يذبحونها بعد ذلك</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/86401" target="_blank">📅 18:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86400">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436447c59d.mp4?token=rpw-h2GuQsKczWQeZqAlserf8msRBQU3UNSLR_OgrYi3B8X9BeGrUt3hJ3vCFsKGKSUUreTAQaj3J7aUnK4W0QzRvilNQiCn4R5uHKM6KcaHoYv9E8qMPqI9fJB3EDZALy9EjvHfQmNx-zz6K8dWDHcVn9uNKFWUoryXOSTNix3xkaprTCkiGqqe4h_DJEFBV2NnmqeJzl4fdi-_2FkHV6-fvucLnj2HWHMsxANer0STLeDxhf5NNokCTTdwBFQhAy0VSePitnYqQ2GILYmJBj2OsHupkXDbLkDkSEafGJ9G2eAljhM7LGuaignAsgwNhzraeGUa64R-ijObf1bUgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436447c59d.mp4?token=rpw-h2GuQsKczWQeZqAlserf8msRBQU3UNSLR_OgrYi3B8X9BeGrUt3hJ3vCFsKGKSUUreTAQaj3J7aUnK4W0QzRvilNQiCn4R5uHKM6KcaHoYv9E8qMPqI9fJB3EDZALy9EjvHfQmNx-zz6K8dWDHcVn9uNKFWUoryXOSTNix3xkaprTCkiGqqe4h_DJEFBV2NnmqeJzl4fdi-_2FkHV6-fvucLnj2HWHMsxANer0STLeDxhf5NNokCTTdwBFQhAy0VSePitnYqQ2GILYmJBj2OsHupkXDbLkDkSEafGJ9G2eAljhM7LGuaignAsgwNhzraeGUa64R-ijObf1bUgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇰🇼
الاقمار الصناعية تظهر ان إيران تمكنت من استهداف قاعدة علي السالم الجوية الأمريكية في الكويت الليلة الماضية. لم يتضح بعد نوع المنشآت التي كانت موجودة هناك.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/86400" target="_blank">📅 17:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86399">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🌟
🤡
Zelenskyy, be careful tonight. Mama Odesa is in danger</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/86399" target="_blank">📅 17:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86398">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2dVBuLEhshOPKRuR0_dFFtkNpFHl4nm53mLVIzn1i5Uc_0CLhpVO8-l1jV_h9lCQiGnQ9Po7AAO3-h7wCnp7J1FGXBDYofwPdjqgJOTf3wDY3bv1_7gSaFMt9cEJCn-klTmF0FhFQwi6-iBaA5V13OQ6aZETpHaGqUN86Fwuit7d91hsBpMHGlXASBm9auXs83pDDJUgd4oWmPncrM3pVJ1ECqkF8F4yw6cnYBa29DLEfTyESN5i2K7Vl0b7jJ4h2UEfuoP59dJ97hgAoXXVa3W3Z_rgwI4vfkw5u7Hb2GoO_2JtJPX57LrBwoHgcnvbByD041dZKYKsV-IbELCWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إعلام غربي : تعمل السعودية على تشكيل تحالف دولي يهدف إلى حماية طرق الشحن في البحر الأحمر من هجمات الحوثيين، وفقًا لمصادر مطلعة على المناقشات.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/86398" target="_blank">📅 17:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86397">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇾🇪
🇮🇶
السيد عبدالملك الحوثي: نتوجه بخالص العزاء والمواساة إلى الشعب العراقي العزيز ومؤسسته الأمنية ومجاهديه الأعزاء وإلى أسر الشهداء في العدوان الأمريكي السعودي الغادر الظالم، نستنكر وندين العدوان الأمريكي السعودي الظالم ونؤكد على تضامننا الكامل مع الشعب العراقي…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/86397" target="_blank">📅 16:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86396">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇾🇪
🇮🇶
السيد عبدالملك الحوثي:
نتوجه بخالص العزاء والمواساة إلى الشعب العراقي العزيز ومؤسسته الأمنية ومجاهديه الأعزاء وإلى أسر الشهداء في العدوان الأمريكي السعودي الغادر الظالم، نستنكر وندين العدوان الأمريكي السعودي الظالم ونؤكد على تضامننا الكامل مع الشعب العراقي ومؤسسته الأمنية ومجاهديه الأعزاء بكل مستويات التضامن والموقف.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/86396" target="_blank">📅 16:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86395">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhnyQfqLOFtncCGJkZuTsNCxeZogjisixhGWCbHD2YNdShnXllHK4vXJAJwxiX2qKwM2s6Nzs0z6jtSfYoYPIwtk-Exg0osLRbXuYaGxgZajt7z18nufcU8WHpTZKBVH-RkoJc7eoSQVRsLfaFT15wRMwKjaq30j53TV7xX6L1whPXtcPnrUu83XA-kVfjTlkSV1ziLFR1JZu1TWrZCGCWvcK-Mu-rtfmQeT_Ht88No2kWL0be51IZ2NifLrzVplegHMp7e7950_Voj-GvzRfZC2n9gfSJ7ixdSbmSxvAgGt3to6HHGgTkD8et8Lt2MdO7pFcHnvsfIzxnX7VqsdCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
حرس الثورة الاسلامية:  صباح اليوم، وفي إطار العملية "النصر 2" ومعاقبة الغزاة، تم استهداف قاعدة جوية أمريكية في علي السالم، حيث تم إشعال وتدمير منشأتين للطائرات بدون طيار وخزان وقود للطائرات والمروحيات العسكرية.  يجب أن يعلم المسلمون في الكويت أن معاقبة الغزاة…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/86395" target="_blank">📅 16:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86394">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba0b5a4b97.mp4?token=qlwVIpkri_aXm89YrkMr338xNV5ZMSLX492EVrTn1xV6dnxr9n4dGUauMrfTeyXKvcAQLA8gz7LxwPiIAzV-fr3-ThoM9qbgCRpRIhnh_0UlvlIAfbMN_Gpd3c_m0fKYxeDZcNYOahM0dIcuTEi9pPl5ASUVOtCNC5eaLxyEeWJvPR5eY2OWxmrLmCf-XADjFYFOqOkMerK-UWh-za8BWekpwQthRrHa8zaIF1djpE0wwhfXeV2wIU-9qdeKUppBBwytBIdYLGzxYc3nmajVlEYGuxGnUJFOter_9inw9Fnh_xDlj6t_9HacmaKSP7fCqpkgQVtsZ26GApgBhiAhYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba0b5a4b97.mp4?token=qlwVIpkri_aXm89YrkMr338xNV5ZMSLX492EVrTn1xV6dnxr9n4dGUauMrfTeyXKvcAQLA8gz7LxwPiIAzV-fr3-ThoM9qbgCRpRIhnh_0UlvlIAfbMN_Gpd3c_m0fKYxeDZcNYOahM0dIcuTEi9pPl5ASUVOtCNC5eaLxyEeWJvPR5eY2OWxmrLmCf-XADjFYFOqOkMerK-UWh-za8BWekpwQthRrHa8zaIF1djpE0wwhfXeV2wIU-9qdeKUppBBwytBIdYLGzxYc3nmajVlEYGuxGnUJFOter_9inw9Fnh_xDlj6t_9HacmaKSP7fCqpkgQVtsZ26GApgBhiAhYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
حرس الثورة الاسلامية:
صباح اليوم، وفي إطار العملية "النصر 2" ومعاقبة الغزاة، تم استهداف قاعدة جوية أمريكية في علي السالم، حيث تم إشعال وتدمير منشأتين للطائرات بدون طيار وخزان وقود للطائرات والمروحيات العسكرية.
يجب أن يعلم المسلمون في الكويت أن معاقبة الغزاة مستمرة حتى يتم إنهاء نهب ثروات وموارد المسلمين الوطنية، وطرد المحتلين واللصوص الأمريكيين من المنطقة.
ولا النصر إلا من عند الله العزيز الحكيم.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/86394" target="_blank">📅 16:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86393">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hg7Efq5TZd9lHgxBoXmvI59siMyhd01uQLb-EdTvWXbIkOrwobVIieyKcTjw3MSNsQLil5DFwHwPlvMwk4U-kaCv6_4yrmqRh8zDfjYMctDYi28mI_AJx6iN96sijjhbsmZe1xPI56BYCHosBeF2CpYZ2foE1SUitoRRx6Ef8mY_8lk45gyOuJNdFMe1Zpb0CZpHhJ4cQSq5KTLIuUyp2keQcd1GgdHY2nl_MXHwBgtO_8cOXW-Toui2yLltMmpb3YeQ5iW-kYoapjcOmBcEc080yI2jLLo1Wi91xAEYZtDQkeDDWbpUI4fUw2VkNNGbAh9tkZw-xnDaFZF76XGj4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇵
🇷🇺
اوكرانيا تزعم:
من المرجح أن روسيا استخدمت ولاول مرة صاروخًا كوريًا شماليًا في هجوم مميت استهدف مبنى بالقرب من مدينة كريفي ريه.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/86393" target="_blank">📅 16:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86392">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇪🇬
🇾🇪
مصدر بوزارة الخارجية اليمنية:
لا صحة للشائعات حول استهداف اليمن سفينة في ميناء دمياط بجمهورية مصر العربية، الموقف اليمني واضح ومعلن وصريح ويستهدف النظام السعودي فقط لحصاره الظالم وعدوانه المستمر على الشعب اليمني.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/86392" target="_blank">📅 16:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86389">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cJeCdcbFDU4BPHV1OOBD8v6gIqmhc2ia8ANS-Gqerhaz_xwpHIEuOpU8hl5X55n8eHyAC196abnVBj86sKZ4F4YOmrP7v0l43IKQuOilkldlxfeNDhBxJPD0RP7_SnzTeSkdOJG_-4kfvpDIey7Be53MAWWYemecuWt1C5BHWDs9RLSRmY60KbwaGNnkgZ6WvVvpyHavYqTZT69f1PzUmFyPCaRiJ2A7hK_wsiG9KdyOVo7lAKqvbGV-XeoRCPJnEoP4wmoQcu3_rEBZpYTWToVYaZN_kgP9Iwi65cKdMl0aNbpW3s8Feh6-6o4fmSxiat4_WR9TJg7KngYEmTRISw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k5lZg6eJ9cr7ji6qVdC7QdoiJ6GfWHUZfc2x1V_84dpFj0b_STGou_zLUNGwBvVxvAz7rxcSxrykQYJIW_kn64JsYCVrQRhP0T2PN9VBImTGJUk9zepwlAbdpxcwrQDCgPu9cvsibcG0NsxN0lc2i8Y1RMviv5MkoQ61dnhUWWsqTL025bPAIfWLVv7Hd5dEIFpOE0LNCbx3PGGWG24fqOeps26s6Rl4TCG1IRo8bO30qXOgYBYQeugpF2--xvT_1pCTnF8Mhc9b7W4gMIqi2gCtC72N0Zrm7Ryr0E1vkRB_-JlTwBs9JDg5VuHYkDrF3l32vBMJBO5kNgqENK2nkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QKH_uKUlIN1Z8QA4i3dPSx3yIqu_M6XyOJEOA_wdrjclqU-NUfxnFjQTg46ctAJyUgbz2tPISaeNePg9oaLdVHM1qKJm4plo1msyvMi8nOrOK6YuuPqC7867vHcBl7o_RBmMZpoy-hvz63WRbBQCN-xH36Kbzd6Iq5p6_8264za84_X0vUqjs17JcEom-yGRWKWkDCsaaGvkEeQukAIr6iCUyXtefKXFUabDhapbDNbVZmM4AhRt0JQmb04JtmBYzGGuFzbGSFnHp1H9e0arHQlmnwzF7_sh3G6bQsFbCJbG7Igs91SWy02uuqEJOxR00IjPOoEZwTGPkGN8AuOj_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
خاص لنايا |
هبوط عدة طائرات امريكية في قاعدة عيسى الجوية بالبحرين.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/86389" target="_blank">📅 15:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86388">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇾🇪
وزارة الخارجية اليمنية
:
في مؤشر يفضح مستوى التنسيق والتعاون الأمريكي، السعودي، الإسرائيلي، استقبل المجرم ترامب كلاً من المجرم نتنياهو ووزير دفاع النظام السعودي.
أن هذه اللقاءات تأتي في وقت يرتكب فيه كيان العدو الإسرائيلي، أبشع الجرائم بحق الشعب الفلسطيني واستمرار احتلاله للأراضي اللبنانية والسورية والعدوان الأمريكي المستمر على الجمهورية الإسلامية في إيران والجمهورية العراقية وبمشاركة النظام السعودي الذي يواصل حصاره على الجمهورية اليمنية وانتهاك سيادتها واستقلالها.
تلك اللقاءات، تكشف الدور السيء الذي يقوم به النظام السعودي في المنطقة العربية والأمة الإسلامية خدمة للمشروع الصهيوني ضمن مخطط ما يسمى بتغيير الشرق الأوسط.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/86388" target="_blank">📅 15:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86387">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">النتن يتعرض لموقف محرج
🇮🇱
السيناتور الأميركي جون فيترمان يستقبل نتن ياهو مرتديًا سروالًا قصيرًا، في مشهد عكس حالة من عدم الاكتراث إذ بدا منشغلًا بهاتفه طوال اللقاء دون أن يُظهر اهتمامًا يُذكر أثناء الاستقبال.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/86387" target="_blank">📅 15:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86386">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇮🇱
إنهيار في جيش الإحتلال.. عناصر الجيش الصهيوني يتمردون في قاعدة سديه تيمان بعد خلاف مع قائد الكتيبة ويتركون أسلحتهم ويغادرون القاعدة إلى منازلهم.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/86386" target="_blank">📅 14:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86385">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">الله أكبر
إسقاط مسيرة معادية في سماء ميناء الامام الخميني بمحافظة خوزستان جنوبي إيران.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/86385" target="_blank">📅 14:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86382">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ad4e6f260.mp4?token=MzYX7ZXu0D1fZwsnFysjSyxyldAmEk2kWfQM_nCmRqVzIdvej6O4GFQiOmo0-OFSF9LPz44mreWn8dLdpU7xKbCkJ9wCI1FiaBEH21G3UjKJSEmqYpq5Ss32khs5cmCzwuqjgcdOIhKhit9UxseQSHR33snR66APPXI6YgsmNrdeTo3OmBMJ4LgYRknXw4cWEc0ur1aPMWjasCQ77MZs2jtivOASVK_VsW8_NADYo3mdU5GYyNAXbQ1xq7C2-2SV5H4KsTAoTPzOt903v0cz5rbcJECZJS5lPBdRqn-NlWz2YDh4YOdsM3kRi69v06Xk7gMQAqe_IXXAERVaOxCjpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ad4e6f260.mp4?token=MzYX7ZXu0D1fZwsnFysjSyxyldAmEk2kWfQM_nCmRqVzIdvej6O4GFQiOmo0-OFSF9LPz44mreWn8dLdpU7xKbCkJ9wCI1FiaBEH21G3UjKJSEmqYpq5Ss32khs5cmCzwuqjgcdOIhKhit9UxseQSHR33snR66APPXI6YgsmNrdeTo3OmBMJ4LgYRknXw4cWEc0ur1aPMWjasCQ77MZs2jtivOASVK_VsW8_NADYo3mdU5GYyNAXbQ1xq7C2-2SV5H4KsTAoTPzOt903v0cz5rbcJECZJS5lPBdRqn-NlWz2YDh4YOdsM3kRi69v06Xk7gMQAqe_IXXAERVaOxCjpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
إنهيار في جيش الإحتلال..
عناصر الجيش الصهيوني يتمردون في قاعدة سديه تيمان بعد خلاف مع قائد الكتيبة ويتركون أسلحتهم ويغادرون القاعدة إلى منازلهم.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/86382" target="_blank">📅 14:53 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

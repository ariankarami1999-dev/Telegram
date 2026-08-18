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
<img src="https://cdn4.telesco.pe/file/Inx2ztDzVVgsf73jZ8rExwmA-v89JafQG7RPLBwq5hVlhx8ezbTC_HoXyY6AX6lv76T8m76bl52XhiDofr5Dv0gtNcEuQFahvfPCzIyojQRDkf6xxWpD26tILV7SC3CWursswFObvyjqhCQzjW0R3C-KafKZCcKZUBuEgmGCvd79tJKoiWPwHkWNYOnIv7eNkqzmotYXcfdiNtPntqIBXIZj2ASUqYOqke2B0vAQoweJ2yy1iPK00L0G98R2f0qtreqR7y2PbXNhWdOLKXWFa4X3TKYKvsRnhbDiG0yQ8SGCWailEbkulOPba4nG5nuFXo9_QQ6Kf88EYO-A2biJJA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 271K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-27 21:53:45</div>
<hr>

<div class="tg-post" id="msg-88106">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇺🇸
وزارة العدل الأمريكية:
توجيه اتهامات إلى 17 إيرانيا بتنفيذ حملة واسعة لسرقة البيانات عبر هجمات إلكترونية، المتهمون استهدفوا 144 جامعة أمريكية و178 جامعة أجنبية و42 شركة ووكالات حكومية.</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/naya_foriraq/88106" target="_blank">📅 21:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88105">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔻
حزب الله: بالفيديو سِيري عَلَى اسمِ اللَّه</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/naya_foriraq/88105" target="_blank">📅 21:46 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88104">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMDe5F-QcSlSaK0IEWwdvR5ehQlA4s6ugTT4RAvB4tA4rr0uH55CGMRGXsgMI1zFq6PiNhSgl3MwdjN8wwZrV_DigzUCRnrri9jY69biWSJZBKa-WEMdkeR34dRJ2lTOsOScuLHdb4P3badTKu9plO4rg4D2Ch8AFplSn3-qi-vtuihgCr910jVjMsvXlsWEhTYP8WM7vw5yb0kuSW9DoezoukhOFYHDcFPmkSNLT4QcPTQWTX1eLE99m4coAEDbtnlZ_JwmzLZBU-mEFmGYzX0PXOKmFuAPoakHpeGzUpyyCNfxL3z6AlfhTky7IAi8Yo6YeaZ2YwVAXFA5crdC_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزير الخارجية الفرنسي على خلفية طرد موظفين اثنين من سفارة الفرنسية في طهران:
سيتم طرد اثنين من الدبلوماسيين الإيرانيين خلال الأيام المقبلة.</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/naya_foriraq/88104" target="_blank">📅 21:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88103">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇾🇪
🇸🇦
إستهداف صاروخي لسفينة سعودية قبالة ميناء المخا اليمنية من قبل أنصار الله.</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/naya_foriraq/88103" target="_blank">📅 20:55 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88102">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YESug8b3ywsX8b-EXWmMj5q1HgbBcwZhbwd7fs7aZXTzZfB12xwlN6_zXiTkaqKKXwzd7Dsargt-JnQFRr-R9QNe006rcFdeYNeuy4xHgDEhev3H5wD7rnkNGCzEyS-FJweT_HmD5U6ZgCUBDZSYsjLn10t1tjA1GwqkXN3PWt6rn787hJL4drP5kQ-3X_MEWDIgsfI4e_OZSYaQUr2IeQYbCySrdRwiUsaI2i8e4gd1vsDnTjs8WTSGSCwAwPkPM0A7ScwOgwDKhtSZeeTAp92w8mVLsiUXibYF9m5xBsXoLe9aZIg--cvPkJNdrk3yliQjOLLyT6o6U3skmqoLCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
الولايات المتحدة تفرض عقوبات على رئيسة "المحكمة الجنائية الدولية" توموكو أكاني.</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/naya_foriraq/88102" target="_blank">📅 20:37 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88101">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">#متابعات
🇮🇶
ازدحامات تشهدها معظم محطات الوقود في العاصمة العراقية بغداد بالتزامن مع فقدان البنزين المحسّن من عدد من المحطات ما أدى إلى توافد أعداد كبيرة من المركبات واصطفافها في طوابير طويلة.</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/naya_foriraq/88101" target="_blank">📅 20:36 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88100">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2n3N8MeWg4OcyJLHYvldW5dRQm9Z9a8KyCow2qyiXijy6APmErIfq4EVsJrP2s7WDOICN1eiEm12UtFEKdr28knnwxvHx6M5pQzm_Nb4R0p2bKt1gywMXiCV0i2SW975RksMYdJMkUex0pZGxcOxEzA2TCy3vKF5rzXmpNLQJcPF1LJQXJkdo3urGcJEdBZmEZNNOYL_ttvTtKPv6mtWnRBxpKWWoWiQZNV8XG6nTA1i8wrOX1CiVLkt5e14tWOnnJLmxTjWCaRvSxwCl1VCWuNgLLlqYYXlsW8VVtOuRWCRV8PZAU_A4BmNogNdUYi7H4MDXIlJX-M80ytjjppew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالبياف
:
يعتقد الأمريكيون أن الضغط على إيران بشكل أكبر سيؤدي إلى انتزاع تنازلات لم تكن جزءاً من الاتفاق.
‏بيسنت وهيغسيث ليسا في مستواهم على الإطلاق. كفّوا عن انتظار هؤلاء المهرجين ليُخرجوا معجزة وينظفوا الفوضى التي أحدثتموها.</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/naya_foriraq/88100" target="_blank">📅 20:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88099">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a206509c.mp4?token=W-oszVOITPqzuQWm8tEeY_iA-tcQWWNYiWtJrOlY8BBVrv202DCFJAK4nkiDhtL_bAoPdZv8KD-O2uo38L9GlVPM9plXXVn2og4oX3QW9eN3llKHVm-u9yfFRoZvFX3oVp4JYEe-yMPuJ8_xStT4xFp7lh3xoJOE5bbCK2WaS7wROhypMY-R2__y8_-yQ7_9dVbSl716GxnbWSwrvMQuMXC2u2lclao3ioPLP64mbtrUwnJ4JPrmgcs2KKOXNUzTWivWRaFspS_neLD1lTNUIGJnSJWvvhlkcnldOVgxU0oB8rD5fh_3JxTGump8tZMCCzdEkofPI_rMl6EPfgnnaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a206509c.mp4?token=W-oszVOITPqzuQWm8tEeY_iA-tcQWWNYiWtJrOlY8BBVrv202DCFJAK4nkiDhtL_bAoPdZv8KD-O2uo38L9GlVPM9plXXVn2og4oX3QW9eN3llKHVm-u9yfFRoZvFX3oVp4JYEe-yMPuJ8_xStT4xFp7lh3xoJOE5bbCK2WaS7wROhypMY-R2__y8_-yQ7_9dVbSl716GxnbWSwrvMQuMXC2u2lclao3ioPLP64mbtrUwnJ4JPrmgcs2KKOXNUzTWivWRaFspS_neLD1lTNUIGJnSJWvvhlkcnldOVgxU0oB8rD5fh_3JxTGump8tZMCCzdEkofPI_rMl6EPfgnnaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏انفجار هائل في مصنع فنلندي قرب الحدود الروسية</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/naya_foriraq/88099" target="_blank">📅 20:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88097">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y_XN8GOiANVwebFtGLAHjJ8nr8Hs2r3WBGJ61IwfrhT30MLSCf19D7OIRbAhqbDe9TkNjoRF1Fa1M0Zq_mf7s7RWcSSOkddEWBslfVzrZa8uZJGGKlRzKgoElEzk_xFd8V0mwXqmkXdAOD60s4Iywd8frrkSlkV8guxMyuCWK5lZDZziuzyv1yvlMPaGRPuOYl9VLSXjx_KQPUpifAMgydG5JGhhmuuTYiMVxS5RSwyb9y2z3u2TgVDZIQP_IhsThcS_ZVZxfZaG3hHxUM5oI9Fz0ECR4MxfMouV1MkP1TNojr5mlu5gnYfjFDb1EQ3qM_otNGiFSO8yF5JvB-HHoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fYZMQ8oQFL7B8yBBU5PcrCnpzmxhwChaOdaijdxR3bPRNPXhwlxS9YbPjtPjOmmX1sYiq-1UUzvywUKHF8r6_5jgpJu8x_2LBXiC5_UnSa2ub2QHBwvrypn7zKOhxZVUvIqIewW-mbEAy_LlnoyoP6iuDH-NaoaJL5flUSwouk0NAqChpaCmzS_MtoneMEjXtB3y9WgGDgKSp8DNqgteAKqSLnnaH5_BR3BD8ycRR0pe3ktt6kxs874k6ceKfGv-8RUEqkpUBbuvTMNNOSM_6ZeMyPkRwVMJ1v-M3hV_7E1q6JSeX2PgwpM22lOXVZMt32EnS64CcCnXnV2K9WBbvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
تسريب النفط الخام يضهر بوضوح من امام خليج عمان بعد استهداف عدة حاملات النفط لمخالفتها قوانين عبور مضيق هرمز.</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/naya_foriraq/88097" target="_blank">📅 20:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88096">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">غارات اسرائيلية جديدة تهز مطار أبو الظهور في ريف إدلب الشرقي</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/naya_foriraq/88096" target="_blank">📅 20:13 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88094">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/897db561c3.mp4?token=iWha-UYNx3ijdU4psptJZPOeF4MbG4MquOXY0HBd4lIlkbrdSj86GB1Yq_NcqFDcxogW1Bfm-U9yi5-lrFJhzNYsWkBdrg2-LFo84czL7jYeN2YRkTaZXKEWwnur9B68Fq-4Q6F-bKwQi9qHlEQDg0iX9Xb64Ag5Loj5JVcsy29tLej03X4xlGp1OTl0qgDqbjHFFBubtQv06k9CDLbgoTGIPUV-MNxmpQBVuxbVg70QMn7COsLfIy-3FRfbp3Uv0ahqNjaaqsl8cGxdwLfIyJyKKexViihDulxdhvwMTA7qsrFP06Esm-MJDwZQq-yoOg1WSgTa21Y5-9mGi-_iiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/897db561c3.mp4?token=iWha-UYNx3ijdU4psptJZPOeF4MbG4MquOXY0HBd4lIlkbrdSj86GB1Yq_NcqFDcxogW1Bfm-U9yi5-lrFJhzNYsWkBdrg2-LFo84czL7jYeN2YRkTaZXKEWwnur9B68Fq-4Q6F-bKwQi9qHlEQDg0iX9Xb64Ag5Loj5JVcsy29tLej03X4xlGp1OTl0qgDqbjHFFBubtQv06k9CDLbgoTGIPUV-MNxmpQBVuxbVg70QMn7COsLfIy-3FRfbp3Uv0ahqNjaaqsl8cGxdwLfIyJyKKexViihDulxdhvwMTA7qsrFP06Esm-MJDwZQq-yoOg1WSgTa21Y5-9mGi-_iiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مقتل ستة نساء كحصيلة اولية نتيجة حادث عنيف قرب مطار المثنى بالعاصمة بغداد.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/88094" target="_blank">📅 19:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88093">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">إعلام أوربي يدعي :
تقوم روسيا بشحن المتفجرات ومكونات الطائرات بدون طيار والذخيرة إلى إيران عبر بحر قزوين لمساعدة طهران على إعادة بناء مخزوناتها التي تضررت في الضربات التي شنتها الولايات المتحدة وإسرائيل.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/88093" target="_blank">📅 19:47 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88092">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇮🇶
سوالف الگهوة
اكو نائب حليو صغيرون مجكنم ؛ البارحة المالكي غاسلة بالكاع غسل ولبس ؛ خطية يحاول يقلد ابو عمار مصطفى سند من جان مهاجم بالحادلة بس مجتي بيده ؛ عمو بعدك صغيرون بعد لا تعيدها …</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/88092" target="_blank">📅 19:30 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88090">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b6184389.mp4?token=EHaHW1KoTxKg5-rtREd6Pq5XhJOOV0ss4d7GqFSKw64LgRCtJQlZBMzqS4Y-N8EkKFnYSLadBJFBB2w8xP2biZS7JDaFxMEVI4OB2M_b6BgNVY_PJbebqz6_8xm-7zeoDHHKN1eZWvBj8dTJz9TQReIT0DLCJaWOWHZQLGwcKB3AkyIV5ZYQ9Bs5mH1P_0SzwWRqoP06nj2L7QsRbPn13N7w-b_UApkQb04TyrSiq2pfHFpcTobp4GiAOb0ZvCn5k-2JvzSUwAax7mv0Z7xHEKsyvowDl3lKsxffU5vySiP2uERELMIO5Ahv35ZeNdYAX19FcajrYjIe-wgX2qR-fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b6184389.mp4?token=EHaHW1KoTxKg5-rtREd6Pq5XhJOOV0ss4d7GqFSKw64LgRCtJQlZBMzqS4Y-N8EkKFnYSLadBJFBB2w8xP2biZS7JDaFxMEVI4OB2M_b6BgNVY_PJbebqz6_8xm-7zeoDHHKN1eZWvBj8dTJz9TQReIT0DLCJaWOWHZQLGwcKB3AkyIV5ZYQ9Bs5mH1P_0SzwWRqoP06nj2L7QsRbPn13N7w-b_UApkQb04TyrSiq2pfHFpcTobp4GiAOb0ZvCn5k-2JvzSUwAax7mv0Z7xHEKsyvowDl3lKsxffU5vySiP2uERELMIO5Ahv35ZeNdYAX19FcajrYjIe-wgX2qR-fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعمدة الدخان تشاهد من مختلف انحاء السليمانية</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/88090" target="_blank">📅 19:20 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88089">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/352e85edac.mp4?token=Vw0B-D6yLvJ_OIkw3wj7U6TzGMhaFYI9b0ZiHCC7pGcV9FXrfRSuzkPsQxV9ulrl2XywrZtGxgnlsbMSTAi9KCDf_UJdPRZke6xlaTFPeERpl3lYHrW2ZTovQ9YHDLc337zArIz_ETSC2qP6VPKH4F0MFqwiOXZeSg3Df_0-uotD-pmKqnm1iaDOA31u555lBzpmQlRzSUayUsXr2Eu2iLr-efRDGLbhHtVf7GCoLmOFBpKIaGPFk7ji0EpuiD2NnScE-1YsHBfvSsEn6D38qXqKQU-qOOwUQm_iw0enhh3HKx3PeEqobsvPvX4jJgqtsTA3kMPUfGpGLBmTbt_MGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/352e85edac.mp4?token=Vw0B-D6yLvJ_OIkw3wj7U6TzGMhaFYI9b0ZiHCC7pGcV9FXrfRSuzkPsQxV9ulrl2XywrZtGxgnlsbMSTAi9KCDf_UJdPRZke6xlaTFPeERpl3lYHrW2ZTovQ9YHDLc337zArIz_ETSC2qP6VPKH4F0MFqwiOXZeSg3Df_0-uotD-pmKqnm1iaDOA31u555lBzpmQlRzSUayUsXr2Eu2iLr-efRDGLbhHtVf7GCoLmOFBpKIaGPFk7ji0EpuiD2NnScE-1YsHBfvSsEn6D38qXqKQU-qOOwUQm_iw0enhh3HKx3PeEqobsvPvX4jJgqtsTA3kMPUfGpGLBmTbt_MGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاعد كثيف لاعمدة الدخان من السليمانية</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/88089" target="_blank">📅 19:18 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88088">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17b671c100.mp4?token=H_bTnihsVHAOFzrLHZAnn96YbsB-RYnrEZyoIUAdQsw-pN_ugQl_wymSWJcEQtdKX--irrW70djncfGw2vwzmEv-4sk5C8iX_sfcJEvB4KnmcJNDESqHK5xrd24slY8hLzOAyTOlDyaf9oKThbJirIOinELi9zHSI6Caizq0nxB13WmJ5-EIezD6gwZccMeWKjLKY89IYwn3PzxaDXNyseYgPAssaYBahr__1IyXu-nLpd1ax2mZrccfP0ercWAuG-LFs3sTH7OLpGM0V9-uYQwo31wqPdv9fe0OeDSI5Kk4Wc_zVnuja_2tqu4H0aQNdz-tY2hrBw6_sNdh4HoJBF-jK-xpeO7qYu-wTbqrgclvrQy_JUL9CFP4baZQV7vQsIbtsrDNTIkIZQjp2rx6wqFB-xe6wbjG3XTFZbX9nPO9ivn_XscyvbOhA6t05yJV5aTUfyXMXhPZMPRiPM2Q85lXCSYpailRHuvqrqS8CvKcQuo3xOgwqL7kQU4CrspSr0b74Hs9anQxbyrjQzmUu3-gUy_6mtpiVfr4DU5_PRyEju80ItjCH8AphnvRKf06N4dJBdePfAmElh4KtiSB70C-doLUaJcpcciT0KNFzqoSHehTvrPtOIflNp4fCEuYozwSHVqURt_ttzNnPkG-FgmAFkpzGvyRziduAh_MPo0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17b671c100.mp4?token=H_bTnihsVHAOFzrLHZAnn96YbsB-RYnrEZyoIUAdQsw-pN_ugQl_wymSWJcEQtdKX--irrW70djncfGw2vwzmEv-4sk5C8iX_sfcJEvB4KnmcJNDESqHK5xrd24slY8hLzOAyTOlDyaf9oKThbJirIOinELi9zHSI6Caizq0nxB13WmJ5-EIezD6gwZccMeWKjLKY89IYwn3PzxaDXNyseYgPAssaYBahr__1IyXu-nLpd1ax2mZrccfP0ercWAuG-LFs3sTH7OLpGM0V9-uYQwo31wqPdv9fe0OeDSI5Kk4Wc_zVnuja_2tqu4H0aQNdz-tY2hrBw6_sNdh4HoJBF-jK-xpeO7qYu-wTbqrgclvrQy_JUL9CFP4baZQV7vQsIbtsrDNTIkIZQjp2rx6wqFB-xe6wbjG3XTFZbX9nPO9ivn_XscyvbOhA6t05yJV5aTUfyXMXhPZMPRiPM2Q85lXCSYpailRHuvqrqS8CvKcQuo3xOgwqL7kQU4CrspSr0b74Hs9anQxbyrjQzmUu3-gUy_6mtpiVfr4DU5_PRyEju80ItjCH8AphnvRKf06N4dJBdePfAmElh4KtiSB70C-doLUaJcpcciT0KNFzqoSHehTvrPtOIflNp4fCEuYozwSHVqURt_ttzNnPkG-FgmAFkpzGvyRziduAh_MPo0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من محافظة السليمانية بعد الانفجار المجهول</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/88088" target="_blank">📅 19:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88087">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90c491d94.mp4?token=ihqmAL4ufnczuMZqeMZqrXh3LiLtnj9CLSJ0ofZhmvUDOcLi3RTLgVrkJZ27PN2DtUg5_2Hng90o1xA90Vk2bZt8Ns-6H4i1EOr8bA-Pm4ujKLU-L_2I3VwV8--p621jNdc76rFVWjqT8Ds-bXVSQR-XDGF_TAblPBDsk-Fj4qK_gDAnblImCT-PyZJsvIfTQpSDUTNCq2anglfKdApUOrOy9Nf-xHHB7mrVlUil1GrgjrDHUVk0fUKZ1dyENo7zzgv0-L1H6EewUL-7lupiObbgdMnZ7z5prGh1sln-8RvYU4DrwDoyclhJkdE14_B91N6Q-WyiFjd5zhbGB0yywQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90c491d94.mp4?token=ihqmAL4ufnczuMZqeMZqrXh3LiLtnj9CLSJ0ofZhmvUDOcLi3RTLgVrkJZ27PN2DtUg5_2Hng90o1xA90Vk2bZt8Ns-6H4i1EOr8bA-Pm4ujKLU-L_2I3VwV8--p621jNdc76rFVWjqT8Ds-bXVSQR-XDGF_TAblPBDsk-Fj4qK_gDAnblImCT-PyZJsvIfTQpSDUTNCq2anglfKdApUOrOy9Nf-xHHB7mrVlUil1GrgjrDHUVk0fUKZ1dyENo7zzgv0-L1H6EewUL-7lupiObbgdMnZ7z5prGh1sln-8RvYU4DrwDoyclhJkdE14_B91N6Q-WyiFjd5zhbGB0yywQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعمدة الدخان تتصاعد من محافظة السليمانية</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/88087" target="_blank">📅 19:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88086">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دوي انفجار يهز محافظة السليمانية شمالي العراق تبعه حريق مجهول</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/88086" target="_blank">📅 19:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88085">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دوي انفجار يهز محافظة السليمانية شمالي العراق تبعه حريق مجهول</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/88085" target="_blank">📅 19:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88084">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R1gyxX7d5vUhrGT04dz2s1RXTPxCuFxWPH5VbsrkTIojXhXyVaBBJtXTGlwhurmurFxYmosQA6Q8569UdCXRDsrEK94CSltgIYeeRn2bsJanEfSWJzXvy_g1w8s7z83L2dJXc1HP35_5JBrt7CoA5PvmY7UUMQVCr7vAPvRvLUtdFq5ySVPsC4SFK6AjDXa72THU_V5uWtQnLnwogeLM4n_GgDDL1DSH-y-mboGJ8zfGd2x2Cvx8kidz2pPgrI7k0U1xL8FIrhJLV-ZqRhnu6ieoRoKRRtW-6feUOYivsH94U_TqVcOnYiuxv1VJkX4FUNNLGIVpkCiGNumrq_Dcxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
منصات مقربة من حركة أنصار الله الأوفياء تدعو لوقفة احتجاجية في بغداد يوم غد ضد الفتنة والدعوات الخارجية التي يفرضها توم بارك حسب تعبيرهم .</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/88084" target="_blank">📅 18:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88083">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">واشنطن بوست:
الولايات المتحدة تدرس تقليص وجودها العسكري في الخليج بمجرد انتهاء الحرب</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/88083" target="_blank">📅 18:46 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88082">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9cf316785.mp4?token=kZMECf2eEjfRcuxv7oxsgHK42u0Q4BguyQId6JgwFq7ZeY3FLF2PmTvJlGn9NEt_rmYNuQpg01fq6giOd24koLFQItF3EDGoJU-yz62iHAyEl7ps8PoPqObOqZ_I6sQ_yScT1X25VKh2j2IO-ClmcNYGkAeEPr3cRAz-RgRlaRKNcuQdMNhC4Umu5IBhSd9WuLELV4_34REBEVaBKyiZP5m-T6HI4kIhg9nQ2mUbJRPAbfKueSsKJ1WhuulsSMi_ns-quKqIT5uJrmRwuEIEiObaHbG-ZZPbR6I-sXovfMYZg0GupHe11V0en93WRxcdummElO6rhHteivq-JnkdVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9cf316785.mp4?token=kZMECf2eEjfRcuxv7oxsgHK42u0Q4BguyQId6JgwFq7ZeY3FLF2PmTvJlGn9NEt_rmYNuQpg01fq6giOd24koLFQItF3EDGoJU-yz62iHAyEl7ps8PoPqObOqZ_I6sQ_yScT1X25VKh2j2IO-ClmcNYGkAeEPr3cRAz-RgRlaRKNcuQdMNhC4Umu5IBhSd9WuLELV4_34REBEVaBKyiZP5m-T6HI4kIhg9nQ2mUbJRPAbfKueSsKJ1WhuulsSMi_ns-quKqIT5uJrmRwuEIEiObaHbG-ZZPbR6I-sXovfMYZg0GupHe11V0en93WRxcdummElO6rhHteivq-JnkdVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
قوات امنية كبيرة تدخل مدينة سامراء شمالي العراق لاسباب غير معروفة.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/88082" target="_blank">📅 18:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88081">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇶
خلية الاعلام الامني العراقي:
ما يتم تداوله من قبل البعض أو تضخيم الأجداث بخصوص 30 أيلول هو توصيف غير دقيق ولا يعكس حقيقة المسار الذي تتبناه الدولة.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/88081" target="_blank">📅 18:43 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88080">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">انفجارات عنيفة تسمع بسماء منطقة بر دبي</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/88080" target="_blank">📅 18:33 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88079">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دوي صافرات الإنذار في دبي</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/88079" target="_blank">📅 18:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88078">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">دوي صافرات الإنذار في دبي</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/88078" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88077">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">هجوم صاروخي على دبي</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/88077" target="_blank">📅 18:25 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88076">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRdosakbMm_fPMlXAq_v1gzazJ8wM__uNaRi4F_40XMjtWgY7qI6T-5S0UBAF72CHVTAVrHWCAJs3KgbgiykxF_yPrV5h7Ubf4pMYqwClNojWbZpM17zh7xNSo9hb5cofXNBmfkkOtQA8gs5O4raVSXB_hcYxagj8XRWcRXgWwFyrVmW6s_YeN_xYsoq4rxqHiZACUvOGNTlt5xxtdQl_Bnz_oWJpuGRNwZCwvZeDu-M7dNycPmJ1GzPsnTb-0PgWwmdm9lBZQm_VgjvRdByZBb3ESJwHNY9G5vyQGZFqnr2RtrwCFPcuhVe-4_znJObWzElad9BM0F9f3hTFTCGkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوي صافرات الإنذار في دبي</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/88076" target="_blank">📅 18:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88075">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دوي صافرات الإنذار في دبي</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/88075" target="_blank">📅 18:23 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88074">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">حدث بحري قرب سواحل عمان</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/88074" target="_blank">📅 18:21 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88073">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/88073" target="_blank">📅 18:21 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88072">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">حدث بحري قرب سواحل عمان</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/88072" target="_blank">📅 17:55 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88071">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VA43BM8fCNiQdtQCRihtWGME5fh3CPjNiVW7TRVsF7kS8xwsAkWExq6lIdmLW2zLNO7uXqtP6Mk4TIB8IODZR7YCuM4pfdqOL3n84B4SD5lvtLxoydRGipJwL9TdtLRuXwRBk4pzoOKreN2o8BXWiu7O9RWayHw6rdS8ikMiDs-PKz7epvO6giGENV9ZALvJkzo5mVL_6qIpHE8KCz315SFWANKIMmKiXCyKq_vmh9SMxLHy1ArtEL4KDi157_Ko2eUwe1v2hlkwGI9juZ4OcZjcrLbOqwzdLS0uEuThg-YYuYbn2pIawBWTT8IA8Ou5ZvRuJLT7eOsE8rqHJa9oUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدث بحري قرب سواحل عمان</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/88071" target="_blank">📅 17:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88070">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‏مدير الوكالة الدولية للطاقة الذرية: تم العثور في سوريا على أطنان من المواد النووية التي يمكن استخدامها استخدامًا سيئًا.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/88070" target="_blank">📅 17:26 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88069">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">الكويت تقول ‏ان ثلاث مغذيات فرعية من محطة التحويل الرئيسية الرميثية (B) خرجت عن الخدمة .</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/88069" target="_blank">📅 17:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88068">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfZcIXsj6UwLV0SegijR_0hxGq6pCHVbtkpwYnR1Zb2ECS4vS3MJTtL10QYZenQ9vbEX9V74QwNUIDagOcW2yzmGs_qPTFQunCopLfQ6e3QbpQU02a0MUdEFMVlfcZZ1O_QTOnMk_N1f9bSxKXs_6TwblQolrJEy0Wb5vN4t8lGuBkd06DcGZ_9DgLrVjqqIYcskAjnyEBc11CZhMpnA4qDiM32mtPDGu5QBlKnxGj40Mz8kjkfgR-MKZHgdUtiah5rblrGSXZFOKlMPdZJDGbDejCaMw7ii3xy8RztPxgEHHbuKujRHEZPYcjXhRSA7zs-bWKy3soXD_ZlSw-qqJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🌟
‏
ترامب:
لا توجد أي محادثات أو حوارات جارية، أو مُجدولة، مع الجمهورية الإسلامية الإيرانية. الحصار البحري لا يزال ساري المفعول بالكامل. مضيق هرمز مفتوح ويعمل. جميع الألغام المائية قد أُزيلت أو فُجّرت.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/88068" target="_blank">📅 17:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88067">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">الوكالة الدولية للطاقة الذرية:
انفجار لطائرة مسيرة في محطة زابوروجيا للطاقة النووية الاوكرانية، وذلك في حوالي الساعة 06:00 صباح اليوم. مما أسفر عن 16 إصابة، بما في ذلك وفاة شخص وإصابة ثلاثة آخرين بجروح خطيرة، بين العاملين والمقاولين. ولم ترد أي تقارير عن أضرار تتعلق بالسلامة النووية أو الأمن.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/88067" target="_blank">📅 16:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88066">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇸🇴
النائب الصومالي عبدي حاشي عبد الله: أصبحت الصومال ساحة معركة بين إسرائيل وتركيا.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/88066" target="_blank">📅 16:47 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88065">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">والي العراق والشام توم باراك: ‏ نشعر بقلق بالغ إزاء الغارات الجوية الإسرائيلية المؤكدة على قاعدة أبو الظهور الجوية، والتي تشكل تصعيداً غير ضروري لا يساهم في تعزيز الاستقرار الإقليمي.  ‏لم تتبنَّ حكومة الشرع موقفاً عدوانياً، ولم تُبقِ على قواتٍ بالوكالة. بل…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/88065" target="_blank">📅 16:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88064">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇮🇶
🔻
حماة الأرض .. حشد الأرض
مستعدون للدفاع عن العراق امام كل خطر</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/88064" target="_blank">📅 16:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88063">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1_i40flI94VspcYujWaKePvPJMWnwcSVnwVqZuV2MugOfjWu9WqlNDJUo72tCAawV9qTLtkjFcMvPhKwppKE5VXag8MNYcBrAZOk-5eYuFtjHx-uTrk3Uqe6r6pXYp328N5qMpMq_nCBDqrw-e9FJW1koHYsKfCFQlpjyZVgNi_zilebDEmvvXgb7Y3OSHsq7CAcYq6W-S1SyRec0qRe-Xb-fov3QIBo-RnYEZNfjECL6d3BoNm1zLn-0X7jC5aKf2RmrkvYSm6Fs_aZKQBeo-cnXKQWT5JgYQH17jTYCF5jJLBHEUvTvxtwK3h-zGKzgHQqk5HIldpPseW7XnwTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مطار أبو الظهور بعد الغارات الاسرائيلية</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/88063" target="_blank">📅 15:09 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88062">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUhkYKwaSzck9SLNIG8gHtHb6KsiB49XmcssE3BvloC8B5pMnsHgHO8Pek2Ttma3OGg6l2DBw8iUjcml7WPMxDa-ePTh0AdYqgtciiWJwjPPJzq2CQJWEfz0rpeDPlJUCKMfo2ItGj7I7Z9KZqsbd2LsxvHN6K2hLKlxUZx4YMMr0FmDqSKWGydqG2Sr9HKbSdpHp3croSceqXkuqMwNkh5I5MqvAyuC1klftcA1_oJhXdHLECWNdZ2ZG-70mpBrkXdEvSmvG2PVjOQIfGe-F3MucHmd8mEK7JGX1zi2UCo81cc042BICS-vpLRwg5z4AIQJWrJbPwykVfyZvFSMew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد من الغارات الاسرائيلية على ريف ادلب</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/88062" target="_blank">📅 15:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88061">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/452a2d8719.mp4?token=k0oqdd5rXtAEpQAs7CTjmOBSkrD38NX7aG4xsJCB-hWyFqkAbqAJwgNg7raBbB1-Ru9m7rafGhmay1-zh6i_7hc-27iMrUOoatRcVzx8j9kRUMF6sb2SH_sZG3mdmSNdOWocXFSTaB94SIyZ7Cp38uhuI0CDEHzcQTTf7SW4dh0ITX4tPqZucWVK3IL_vh4tosEKh_XncV_Vs_rSvSIniS7OCgPJWRhY79uY4ZZnwAVgsvGUB3h1SD7id3yEMMbRomuVDom6qHcdmRuKt9pbocQUZ2427Sk9jX8G8mjSjZ02rtxLAMqKE19jNTirt2mYGs8IQ8TtgCXaP6iWrNsfxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/452a2d8719.mp4?token=k0oqdd5rXtAEpQAs7CTjmOBSkrD38NX7aG4xsJCB-hWyFqkAbqAJwgNg7raBbB1-Ru9m7rafGhmay1-zh6i_7hc-27iMrUOoatRcVzx8j9kRUMF6sb2SH_sZG3mdmSNdOWocXFSTaB94SIyZ7Cp38uhuI0CDEHzcQTTf7SW4dh0ITX4tPqZucWVK3IL_vh4tosEKh_XncV_Vs_rSvSIniS7OCgPJWRhY79uY4ZZnwAVgsvGUB3h1SD7id3yEMMbRomuVDom6qHcdmRuKt9pbocQUZ2427Sk9jX8G8mjSjZ02rtxLAMqKE19jNTirt2mYGs8IQ8TtgCXaP6iWrNsfxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غارات اسرائيلية جديدة تهز مطار أبو الظهور في ريف إدلب الشرقي</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/88061" target="_blank">📅 15:07 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88060">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">غارات اسرائيلية جديدة تهز مطار أبو الظهور في ريف إدلب الشرقي</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/88060" target="_blank">📅 15:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88059">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">#ترفيهي
🇺🇸
🌟
‏ترامب: مضيق هرمز - أرض أمريكية جديدة</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/88059" target="_blank">📅 15:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88058">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjZhnO3puBESBPhDpopADMFTQCJBAzwAP7uWhwP53dpyB2mL2XoKtB2-d6Lbb6IiTQoWIjaJKulpYkBdym55gZuvUrO9Rd58w6b0xxCZtY5aUYCvVHutRLjYQBrcTqKKhOnuR6PN9GgHLSgvkKouXygBA5nmwuvlGc18tKVG3ZVj_h6l-ei7lS6WJnJRj_9lkMjyMcKvCX3MbzYDUr5M-XHk6ZeqojwZtoKRxpGPTe2JlINBSXcT_th1UIGMloSN4uM7c-94TcXC3rSEzKZpPUhAo0k8xz6K3j7cngUAQKxFTPtjlaH2eTtE2I9Mt4Vf3SjtAGGUwN3fI2ZsLDJM-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#ترفيهي
🇺🇸
🌟
‏
ترامب:
مضيق هرمز - أرض أمريكية جديدة</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/88058" target="_blank">📅 14:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88057">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇮🇶
المرجع الديني السيد علي الأكبر الحائري
: فإنّنا نؤكّد أكثر من أيّ وقت مضى ضرورة الحفاظ على الطاقات والقدرات التي اكتسبها المقاتلون الذين شاركوا في مواجهة داعش، وعدم المساس بها، بل الاستفادة منها وتسخيرها في خدمة العراق والدفاع عن حدوده وأمنه، بما ينسجم مع الدستور والقانون وتحت سلطة الدولة.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/88057" target="_blank">📅 14:20 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88056">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRKqXJTUvePpPJjiMxn4fZG4P1Wtj2P_cfdH_GsBQKFBlSQvpD9YdmWtErRK2AESBtJxiSV_b_DvHQAO3QRLhOLtABdrVaOP4N8oRuh-tUsRVC66W6bJ8GIN1LnNhv7xUB8jxuNRzW47Vn7vn86Afo97s9yw8cRnf7W2Ee02-2tn7jzWnLw4TY1mOIRWV6uujm5KL6AxuqFMdMo8buCnXtsZaPXSnQUcja3IUTb-vAfRsvDnu9awWL5xZf_9rN1nXPrEGtdXDWz-I5aw4b4nzpVu8U01mphG1OfGQnpCjhiqzZpmHIXQQ7k6q9X0z_dmcqBPRA99XVp3xyZZml5LyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">والي العراق والشام توم باراك:
‏
نشعر بقلق بالغ إزاء الغارات الجوية الإسرائيلية المؤكدة على قاعدة أبو الظهور الجوية، والتي تشكل تصعيداً غير ضروري لا يساهم في تعزيز الاستقرار الإقليمي.
‏لم تتبنَّ حكومة الشرع موقفاً عدوانياً، ولم تُبقِ على قواتٍ بالوكالة. بل إنها أبدت مراراً وتكراراً تفضيلها لخفض التصعيد مع إسرائيل. وقد استضافت الولايات المتحدة في الماضي، وستستمر في المستقبل، حواراتٍ لتشجيع الحوار الدبلوماسي بدلاً من اللجوء إلى العنف العسكري الذي يُحبط كلا البلدين.
‏تُبنى اتفاقيات خفض التصعيد الدائمة من خلال حوارات مستمرة مع جميع الدول والأطراف المعنية.
‏لا تزال الولايات المتحدة تؤمن بأن ضبط النفس والحوار هما المسار الأكثر بناءً. ونشجع جميع الأطراف على إعطاء الأولوية للحوار المنطقي على حساب المزيد من الحوادث العسكرية.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/88056" target="_blank">📅 14:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88055">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeee33539d.mp4?token=HljtKL7W52ZYCE1qBO3f0klTaGcU0332MQ6uaC16a4aD7kS_5OUeC9Rka1Ff6ZYGP4SvF-_F63CtNvznrYM0SO6rXKyinmB-o8MOuGkrpEsNWa3TMmoPxBTC_K2ghjmAo5zWD_EFufgXZ20puEOQC9rnr-1fMcGeBo-799g7kJyfGC9oTZea9Q7Jp4fojBHjOr4r5spC1TZeTFZytMZu5diqSrNOV_OqOuuV7c6aQhJqDtdx-o95oYIFS5CgftD0H9i1tPwAjts34R3Dbzn2EUaI8isem9L8aSB2sip6jwLKlH-6pkAQdC1EddZevVCy_LuzQiJdUrTaNVkDGjJn1TA-zduWr8A7OJW0pFuys5aD1x9cdDT4ePzWu6JxhtSGj6uxNuvs9zWScwZ0bqVb1zYhVW6BXwvbtXjs-FIBunAIuH5xlb7I1eerbVDxJkDHTN4_Zjsc08q1ep_phW22RWVGw8MW-svIMlomJX8ukGWlZh--76J0SwR4_Gp8wSzEaS0CInwWZ5NicLy2ht5ryzB2Uilbfa9Gzx0gWWyu30aZkkVaV7CTKwQqZ-0Yba5LRQfTfZTyencMVTwKDnrS1dMINVyzn3oWCgqBRtSQ1U_SXV1xMPw9rnxc-vBpXoH7rU85zqTZC5LN6fdsjliY72eRHkhFqDPHzA-XXu7NLJU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeee33539d.mp4?token=HljtKL7W52ZYCE1qBO3f0klTaGcU0332MQ6uaC16a4aD7kS_5OUeC9Rka1Ff6ZYGP4SvF-_F63CtNvznrYM0SO6rXKyinmB-o8MOuGkrpEsNWa3TMmoPxBTC_K2ghjmAo5zWD_EFufgXZ20puEOQC9rnr-1fMcGeBo-799g7kJyfGC9oTZea9Q7Jp4fojBHjOr4r5spC1TZeTFZytMZu5diqSrNOV_OqOuuV7c6aQhJqDtdx-o95oYIFS5CgftD0H9i1tPwAjts34R3Dbzn2EUaI8isem9L8aSB2sip6jwLKlH-6pkAQdC1EddZevVCy_LuzQiJdUrTaNVkDGjJn1TA-zduWr8A7OJW0pFuys5aD1x9cdDT4ePzWu6JxhtSGj6uxNuvs9zWScwZ0bqVb1zYhVW6BXwvbtXjs-FIBunAIuH5xlb7I1eerbVDxJkDHTN4_Zjsc08q1ep_phW22RWVGw8MW-svIMlomJX8ukGWlZh--76J0SwR4_Gp8wSzEaS0CInwWZ5NicLy2ht5ryzB2Uilbfa9Gzx0gWWyu30aZkkVaV7CTKwQqZ-0Yba5LRQfTfZTyencMVTwKDnrS1dMINVyzn3oWCgqBRtSQ1U_SXV1xMPw9rnxc-vBpXoH7rU85zqTZC5LN6fdsjliY72eRHkhFqDPHzA-XXu7NLJU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
اختفاء وفقدان ثلاثة شبان من محافظة اربيل في اقليم كردستان العراق منذ ما يقارب الأسبوع بعد ان حاولوا الذهاب تهريب الى اليونان عبر الاراضي التركية وكان هذا اخر فيديو لهم. وتأتي موجة الهجرة المتواصلة في الاقليم بسبب الفساد والوضع الاقتصادي وانشغال العوائل الحاكمة بزيادة ثروتها وتكديسها وترك الشعب يعاني.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/88055" target="_blank">📅 14:12 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88054">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇶🇦
وزارة الخارجية القطرية:
المبعوثون ينتظرون وصول سلطنة عمان وإيران إلى اتفاق ثنائي بشأن مضيق هرمز قبل العودة إلى المفاوضات الأوسع بين الولايات المتحدة وإيران.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/88054" target="_blank">📅 13:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88053">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇶
🇺🇸
رئيس ائتلاف دولة القانون نوري المالكي للقائم بأعمال سفارة الولايات المتحدة لدى العراق: الدولة ومؤسساتها الدستورية هي المرجعية في إدارة الملفات الأمنية والعسكرية وحصر السلاح.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/88053" target="_blank">📅 13:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88052">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IawvEM86zeYe8WHJ0_VpStwiC3dk7qym2WFKIV_JeNg2W9N_FOwiICwhGhmiI3G8Aihb3aMaugO3W5sR-WjXbYRpF3U0ZzNPKDKtnMT1h4XtzE7oAgSddlL8iTSPwvf7x_EAZacOpgaP28DLajJJEXUVDVdeou5TmZK996Un5F-nh0Brkl7rVhX9dGS5SkM8wN6TocWrvWrLCKgaMl6HWt1bLhRHufadNbgK0Zy6vjWvWo3sFqxwEeje5w-Md9EJD0bdNmXynYCm9IPfvuac-tC7py8tbAVRGZY9V7WTv-e8MTegQD1DL7pegkiO4cmBQS1CZB6hM4xo4HMX5MA-qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الحاج هادي العامري:
ندعو الأطراف كافة الى التحلي بلغة الإعتدال والتهدئة، وتجنب الإحتقان في المواقف والتمسك بمقومات القوة والمنعة للعراق الذي نتوق له جميعا، سيدا موقرا عزيزا، ونبذ كل ما من شأنه أن يخلق الفجوات ويغذي الخلافات.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/88052" target="_blank">📅 13:12 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88051">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇶
علي الزيدي حول الهجوم على أربيل:
الدولة لن تتهاون في حماية أمن العراق وسيادته وأن الجهات المختصة ستتولى التحقيق في ملابسات هذه الاعتداءات وملاحقة المسؤولين عنها وفق القانون.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/88051" target="_blank">📅 13:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88050">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇮🇷
رئيس البرلمان الإيراني محمدباقر قالیباف:
لن يفتح مضيق هرمز قبل رفع الحصار، وتحرير الأموال المجمدة، وإلغاء العقوبات النفطية، وإنهاء التهديدات والعمليات العسكرية في جميع الجبهات. إيران مستعدة، بما يتناسب مع الإجراءات والتعديات التي يرتكبها العدو، لإلحاق هزيمة أثقل منه سابقًا.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/88050" target="_blank">📅 12:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88049">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇮🇷
🇮🇶
مصدر إيراني: قالیباف يزور غدًا العراق على رأس وفد برلماني رفيع المستوى، بهدف إجراء حوارات حول التطورات الإقليمية، وتعزيز التعاون الاستراتيجي بين طهران وبغداد، واستكشاف الحلول المشتركة للمساهمة في تحقيق الاستقرار والأمن في غرب آسيا.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/88049" target="_blank">📅 12:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88048">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">بعد قليل سوف يتم استلام المخطوف إلى أمن الحشد</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/88048" target="_blank">📅 11:58 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88047">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔻
‏
رويترز:
شركتا شحن صينيتان عملاقتان توقفان إرسال ناقلات النفط عبر مضيقي هرمز وباب المندب.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/88047" target="_blank">📅 11:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88046">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b581c02b.mp4?token=nxHni_b-l9I-sf89g3BkIsAsVmXep3mKJ_oRbr4EQND2GUu_e0Fe2N3eJsEUISjaepGSBb6fErQ2UR-GEYHTrJ6lS4fF5BjMGDkqLOw8LiHgmBMokmfCYJiDpWt9eVaw-oHG7oI8di065BxauuGYQeoOITOYNiZbrViH0QhUyicjHX1FGW-KyIkD-R5xmuscpcJfPFcIclFozDdrOwGgTux2GfpxH92r0lTCvccM5yzVFnrOMn9V8SOdfhbyuIaIQ9JeBPCiqZi4bqOfyRGsHTqJ0QcE03ntP_xaUXaexknEIe3dTxJyWfn8wb-Y8_ZyHqgReVX6U9m5Pr2gbArbkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b581c02b.mp4?token=nxHni_b-l9I-sf89g3BkIsAsVmXep3mKJ_oRbr4EQND2GUu_e0Fe2N3eJsEUISjaepGSBb6fErQ2UR-GEYHTrJ6lS4fF5BjMGDkqLOw8LiHgmBMokmfCYJiDpWt9eVaw-oHG7oI8di065BxauuGYQeoOITOYNiZbrViH0QhUyicjHX1FGW-KyIkD-R5xmuscpcJfPFcIclFozDdrOwGgTux2GfpxH92r0lTCvccM5yzVFnrOMn9V8SOdfhbyuIaIQ9JeBPCiqZi4bqOfyRGsHTqJ0QcE03ntP_xaUXaexknEIe3dTxJyWfn8wb-Y8_ZyHqgReVX6U9m5Pr2gbArbkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صباح العزة والكرامة و الآباء
🇮🇶
النجباء بالميدان</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/88046" target="_blank">📅 11:12 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88045">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NdMS7_irrQcXvyniPsxTRA83pwGjbGACLLJjiOBFBIU8l_LVYRDwvQmkRQK88fL8THSOiaQ12ldHD4Nn6m9Xv0_o5p4YIGFFoGsqpU7yxIE9D2_SucQFkGMfxclrsJ_zibFMdB2bmoYlzNuXtKk5bqf2oELI_GevrezUuoCodUM8pmNCzqRrtMps1F8FKIqZ--nLlR7qhnjx4xvH2wWw32tDy7LGtC2DGvsOEH0otlE7oNPbhojq2vdeRxyZhdu3Faio8Bi-3yj-ZAJefpO-4Fkc09UsjYlBzeOCdpUERQrTrdo1J9hsMoKeddu24CPg5HwJ1eKzX0shYFf-wd583g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
بعد عدوانها الغاشم على العراق ومقرات الحشدالشعبي..
السعودية تدين وتستنكر باشد العبارات الاعتداء على اقليم كردستان وتصفه بالإنتهاك السافر لسيادة جمهورية العراق!!</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/88045" target="_blank">📅 11:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88044">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc90a1fcd.mp4?token=X4iC2N8LfygBTunLaLoDA1ozgxMVQcUCTzoFzqEY0CJRjf5zPazl76lSI5mhTiD4_IvDlt3oxWSdJJYyqVqiud_KB589ALKprLUKPwuSaw02tLXWbgW8f1P8DPKHqN52C_Vn8SHuWOhArYjKHst1lN5Zt2UOs7eseRqaY2mgS8pQljuSoM-o5hxuA8LfZJfKClnkQkPIiPIgFRZ7xqg647oImQglDzkS_3IJGOsnvP9h50N_mCe3Yy8VwHOsD6I6krePTwFY2O0xu50joG_u_deCl4rkPsqKzujzVfKLbOEuPSbIwbdiKc2L6TGRKcHN5hyCFQB-jY-58hGgtpOb1TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc90a1fcd.mp4?token=X4iC2N8LfygBTunLaLoDA1ozgxMVQcUCTzoFzqEY0CJRjf5zPazl76lSI5mhTiD4_IvDlt3oxWSdJJYyqVqiud_KB589ALKprLUKPwuSaw02tLXWbgW8f1P8DPKHqN52C_Vn8SHuWOhArYjKHst1lN5Zt2UOs7eseRqaY2mgS8pQljuSoM-o5hxuA8LfZJfKClnkQkPIiPIgFRZ7xqg647oImQglDzkS_3IJGOsnvP9h50N_mCe3Yy8VwHOsD6I6krePTwFY2O0xu50joG_u_deCl4rkPsqKzujzVfKLbOEuPSbIwbdiKc2L6TGRKcHN5hyCFQB-jY-58hGgtpOb1TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
إعتداء القوات الحكومية على الفلاحين المطالبين بمستحقاتهم المتأخرة خلال مظاهرة في العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/88044" target="_blank">📅 11:06 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88043">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5ewIMe8zEwaZq4K05XW9kEsXx4KkyQQ3zXSmKXJqSQ9RfGMkFdF6z6uXD2GwIpedBwdmVH6SinS8srVTn0uZdVmHHH6-a1hQhpU_FgM3ObeEieKrixlc9rZxZ1ky_kUGk9URbh0UYTUi8tsOCh9y4Xv4Cx4BwtkSRuBOqbfD296qhpPOESPXJg7TOlKwcZlgHh6nFSn3uS0ri_EoJFDKdkLTuP8zUzV2DivHljyvoiBL9RC8K4VPkf9wQD3iWfWqs11cJp4EWcAjpAlyV6vZiV6FHH7H9z5WhjUvOIeSoqD4nAZ3WPhravC9BjLfFHxHlj8CIyNmaLoGSt0ZB6oTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
في وقت سابق من هذا الشهر، سأل جانيش كومار، رئيس لجنة الانتخابات الهندية، إدارتنا: "كيف يمكنكم إجراء انتخابات في الولايات المتحدة بدون بطاقة هوية شخصية صالحة؟"
بلغ عدد الناخبين في الانتخابات الهندية الأخيرة 646 مليون ناخب. أقل من 1٪ صوتوا عن طريق البريد، وكان على كل ناخب تقديم وثيقة هوية شخصية صالحة.
نحن بحاجة إلى تمرير "قانون إنقاذ أمريكا" الآن!</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/88043" target="_blank">📅 11:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88042">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇶
هيئة الإعلام والإتصالات تصدر قرار تحذير لقناة الرشيد الفضائية ومنع ظهور أحمد الطيب وإيقاف برنامج.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/88042" target="_blank">📅 11:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88041">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bcdc5a1a2.mp4?token=qr39hUhxJu8txY0DwV97nNT-NkUZsPP7dQ_aBTHAFapB4pgmn0J2sFbU2sPiPacBkzGyoWD-HBHIt0OGQUvEfDb1yYm1yWjr_WH6WFWOkqtdF3q6GYfQ3ZE2t2YWJer7desuqGLhHLreLyASHqmWuesPvnYud_yaEaW0D3SVfJjySHAbMxnZw4OcB4_MvzBuEyP4U5_KJWzJqber4auVsixLzFcg7ZLwdaN9V2_cSxvV4UjPm92U_l7L71sa5dAbrRp9CXgKjQkIYT2PwM7Bwf5Rq-4h8WybOxRxYTuiI50R0VwVu9Th7Nwdqcm8kveg0kLoR7S4bU_FKuJANGwQ9bTnFCC_4180tUsUpF_JdD9xv3naSBZneNKI4YBgq5FnFsl-B05ceVt7rXQpNvIEe5m1AvLbb1-8EL-Z66hRUKi8eDYJMaB4bmslpv__x6Sge0dqSsORfwNPmN5Vh6RGmdsFZcNg-m2_zd-_dS-tHf0icdjrttfKn2atdmGp_haGLQZiVzzr_HJeHPOxbMhpNvz2aoUeh1NLrpaQsgDVeVoEFXcMEW7A0XUA5VeZSkGH2T1ioY5uAtScw3cJTKhLHiLxDe9THrPgb3PeCPrjRuxCtAPbchcg4RYiaJ82DiTAph3i18TI1nLO0DfzADatTs87jv5yGZmY4Lt8IolG7RM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bcdc5a1a2.mp4?token=qr39hUhxJu8txY0DwV97nNT-NkUZsPP7dQ_aBTHAFapB4pgmn0J2sFbU2sPiPacBkzGyoWD-HBHIt0OGQUvEfDb1yYm1yWjr_WH6WFWOkqtdF3q6GYfQ3ZE2t2YWJer7desuqGLhHLreLyASHqmWuesPvnYud_yaEaW0D3SVfJjySHAbMxnZw4OcB4_MvzBuEyP4U5_KJWzJqber4auVsixLzFcg7ZLwdaN9V2_cSxvV4UjPm92U_l7L71sa5dAbrRp9CXgKjQkIYT2PwM7Bwf5Rq-4h8WybOxRxYTuiI50R0VwVu9Th7Nwdqcm8kveg0kLoR7S4bU_FKuJANGwQ9bTnFCC_4180tUsUpF_JdD9xv3naSBZneNKI4YBgq5FnFsl-B05ceVt7rXQpNvIEe5m1AvLbb1-8EL-Z66hRUKi8eDYJMaB4bmslpv__x6Sge0dqSsORfwNPmN5Vh6RGmdsFZcNg-m2_zd-_dS-tHf0icdjrttfKn2atdmGp_haGLQZiVzzr_HJeHPOxbMhpNvz2aoUeh1NLrpaQsgDVeVoEFXcMEW7A0XUA5VeZSkGH2T1ioY5uAtScw3cJTKhLHiLxDe9THrPgb3PeCPrjRuxCtAPbchcg4RYiaJ82DiTAph3i18TI1nLO0DfzADatTs87jv5yGZmY4Lt8IolG7RM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
إعتداء القوات الحكومية على الفلاحين المطالبين بمستحقاتهم المتأخرة خلال مظاهرة في العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/88041" target="_blank">📅 10:56 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88040">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇾🇪
🇸🇦
هجوم بأسراب من المسيرات على مواقع مرتزقة السعودية في مديرية حيس جنوبي محافظة الحديدة اليمنية.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/88040" target="_blank">📅 10:42 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88039">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇮🇷
مصدر إيراني:
تم تحديد واعتقال شخص في العاصمة طهران قام بجمع وإرسال صور وإحداثيات لبعض المواقع الاستراتيجية والأمنية في البلاد إلى جماعات معارضة للجمهورية الإسلامية.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/88039" target="_blank">📅 10:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88038">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔻
إنفجار لغم في بادية محافظة السماوة جنوبي العراق؛ إصابة منتسب حدود كحصيلة أولية.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/88038" target="_blank">📅 10:18 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88037">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇷🇺
الدفاع الروسية:
دفاعتنا الجوية دمرت 791 مسيرة أوكرانية في أجواء عدة مناطق روسية خلال الليلة الماضية.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/88037" target="_blank">📅 09:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88036">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇮🇱
جيش الإحتلال الإسرائيلي:
تم إطلاق صاروخ اعتراضي نحو هدف في منطقة زرعيت عند الحدود اللبنانية.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/88036" target="_blank">📅 09:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88035">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇷
🇮🇶
مصدر إيراني:
قالیباف يزور غدًا العراق على رأس وفد برلماني رفيع المستوى، بهدف إجراء حوارات حول التطورات الإقليمية، وتعزيز التعاون الاستراتيجي بين طهران وبغداد، واستكشاف الحلول المشتركة للمساهمة في تحقيق الاستقرار والأمن في غرب آسيا.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/88035" target="_blank">📅 08:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88034">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/By6N0LLjdT6chtp48bZ6IcLCwgBJEJCM7f1RIYAVnBSIs75YuxufSLaU0UMGh3di5vb5r9en95Z88b2TrdYlTUm0gYz8Es6LrdKqliG2KaedVOJxXBhliMeofJyE-ckKK8Y7tZkVAJzpWimx0fYMC73ZKWhRvOFSwpy-bFZzGtnRgYgDw0wRZgGVyP-lXrP5SI8SazvngV6ND07M1vMqNf7g9ofP2ijHCRaCdsMx7-B4ozE0bghxzOu_p_kQPGK3p1zL8ttLGxtvciHNd21r1oQ1pX18-VHE5VCBiqSdf16FTx6sE6TkYtknCbC4NH12RVIYWHHCDLS8igG2znYDGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
جمهور فصائل المقاومة العراقية يريد نسخة عامري الأهوار …</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/88034" target="_blank">📅 08:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88033">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇱
🇱🇧
انفجار عبوة ناسفة في الجليل المحتل مستوطنة المطلة اصابة خمسة مستوطنين كحصيلة اولية ..</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/88033" target="_blank">📅 08:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88032">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/044201b963.mp4?token=UYs6oWR63JBhkvZeTZcSPjIATiAtHlqMCIbSUA9bJyQlazaE9z-MH7rJN4bKsF4_ExuSK8Pay5NLiPLctq3i4WCSFqpYHgeLbBxeMMRpRtbiCYKKcHsUKc9sM65XJ9aYNpZ4M-2SlJRUPLAdN6HJIUZx99Q5uI4JAmhV_meCnnE2NZ7S24JQPoQPO4MfRfbdFYt0pVu4A5PgZtFteyYLzwJ9l3xqifey4OHYytPJxzB113vlXgyB_p3HRc0F9SF2EkdhLbOkqrEL6yTSLj1nehFM8iVsh6CA33By0wHDqYlpXd9JJesI65VBCVe9RKpWjkufCCQanHtZnfZjZqvMxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/044201b963.mp4?token=UYs6oWR63JBhkvZeTZcSPjIATiAtHlqMCIbSUA9bJyQlazaE9z-MH7rJN4bKsF4_ExuSK8Pay5NLiPLctq3i4WCSFqpYHgeLbBxeMMRpRtbiCYKKcHsUKc9sM65XJ9aYNpZ4M-2SlJRUPLAdN6HJIUZx99Q5uI4JAmhV_meCnnE2NZ7S24JQPoQPO4MfRfbdFYt0pVu4A5PgZtFteyYLzwJ9l3xqifey4OHYytPJxzB113vlXgyB_p3HRc0F9SF2EkdhLbOkqrEL6yTSLj1nehFM8iVsh6CA33By0wHDqYlpXd9JJesI65VBCVe9RKpWjkufCCQanHtZnfZjZqvMxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
نيران لا تتوقف من موقع الحادث وانباء عن قتلى ومصابيين داخل مستودع الوقود في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/88032" target="_blank">📅 01:58 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88031">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aba96102ee.mp4?token=BihqvcyK2duBxF3q0j07dEtI0eCY9ym-a4naotcWzLKf8idQX8Vae5eqKrAG-xoMnT9UuNGOiHAyntlq2qeEPamLZfFVY98kBwJtqR5LKpkRamFliwe6WW4WfDByO38Zgcp9ZfrKZ89w71Val2yFW20xXyeALGE5MH0d6RYjlyK2TuhbHDxinaIaynAYptnWs4Wr33tjB7LfjTOzvEjpEVtfgtOuyu8-0pCFYGmtbs4DVhhryu1ebzehp9BajMSyu9-6XWydCie5wkBuFD-H47HTFz3cqI3Y3js71KieNYYX_JC9U-LdlJTrYhk_reR5BhEKFharqOoamrC3pZ77zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aba96102ee.mp4?token=BihqvcyK2duBxF3q0j07dEtI0eCY9ym-a4naotcWzLKf8idQX8Vae5eqKrAG-xoMnT9UuNGOiHAyntlq2qeEPamLZfFVY98kBwJtqR5LKpkRamFliwe6WW4WfDByO38Zgcp9ZfrKZ89w71Val2yFW20xXyeALGE5MH0d6RYjlyK2TuhbHDxinaIaynAYptnWs4Wr33tjB7LfjTOzvEjpEVtfgtOuyu8-0pCFYGmtbs4DVhhryu1ebzehp9BajMSyu9-6XWydCie5wkBuFD-H47HTFz3cqI3Y3js71KieNYYX_JC9U-LdlJTrYhk_reR5BhEKFharqOoamrC3pZ77zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
توسع رقعة الحريق بعد اندلاع حريق مجهول في خزان للوقود في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/88031" target="_blank">📅 01:57 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88030">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d70a886426.mp4?token=YDnz_VvL6skFyKVijU_9r8INWNn0z7klYitzhOtvhJeBYe0w1QyZkrSSwblbYONtmt6xFejO04Rk3xViuMmucpHy62du5Da4f7V89AsBxLnQCrtdwuPr6cSK89xHvQCmJ9JClC2GQX0fSy4UgADVBTWGQEDFjtcpuPdVLFa0oSfL-Dsrg2aS5DxE8WBKB7UROJoyzQb25MYWsNHb9B516u3acJyYBE87-QG54y7q3EKBhIPh4V2-08iJ1UZTfuS2mmknQ0M4KtgrG2QikO14HW1nUIeCgeMWwmuLp6lxpKyzUaRzcU3XPJnl7BrculRC7AEaSLIDdwkCsvk5INuMdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d70a886426.mp4?token=YDnz_VvL6skFyKVijU_9r8INWNn0z7klYitzhOtvhJeBYe0w1QyZkrSSwblbYONtmt6xFejO04Rk3xViuMmucpHy62du5Da4f7V89AsBxLnQCrtdwuPr6cSK89xHvQCmJ9JClC2GQX0fSy4UgADVBTWGQEDFjtcpuPdVLFa0oSfL-Dsrg2aS5DxE8WBKB7UROJoyzQb25MYWsNHb9B516u3acJyYBE87-QG54y7q3EKBhIPh4V2-08iJ1UZTfuS2mmknQ0M4KtgrG2QikO14HW1nUIeCgeMWwmuLp6lxpKyzUaRzcU3XPJnl7BrculRC7AEaSLIDdwkCsvk5INuMdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حريق خزان وقود في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/88030" target="_blank">📅 01:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88029">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">انباء عن سماع دوي انفجار في محافظة اربيل</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/88029" target="_blank">📅 01:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88027">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇺🇸
🇹🇷
‏
الرئاسة التركية:
أردوغان أبلغ ترمب أهمية مواصلة المحادثات مع إيران.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/88027" target="_blank">📅 01:09 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88026">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇮🇶
الحاج ابو مجاهد العساف: ننتظر من الإخوة الكبار وحكمائهم العمل على تصحيح الاعوجاج الأمني الذي تسبب فيه الرئيس المكلف كي لا تبقى حجة لأحد، ولضمان الاستقرار وصون الكرامة وعدم الانجرار إلى ما يسر الأعداء.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/88026" target="_blank">📅 00:40 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88025">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2ulKireePSMk0Yt3e85bh4cVkyHyUI4dQDeY8SrEJXR3Ia7NSCuohA2jBpBfI_eWiSaGIML-pIAK4T4DiW9syV8jze-qS36vQIb9gmCIuJvucECScFf3V9dcHV-EK0bQftEPJDRhLAq6jDJEjCcHbMr69b8H92zTMo3S9vJCxszhpp07r1BN6lPjYU7dYzknJX-JUwTxgrJPI3cgQ4voKTGYvB8OLl9gj3uFsCLs-M3bZLtyYR1DkKS_sCfSGzUlUKVQpSRHCNCPGqbF-FcXnuG6lcqshL3iO6LX3xxhcGhbtlqgUv20tH78EBeww5ptReG6WYF75G531KE_MCWDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الحاج ابو مجاهد العساف:
ننتظر من الإخوة الكبار وحكمائهم العمل على تصحيح الاعوجاج الأمني الذي تسبب فيه الرئيس المكلف كي لا تبقى حجة لأحد، ولضمان الاستقرار وصون الكرامة وعدم الانجرار إلى ما يسر الأعداء.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/88025" target="_blank">📅 00:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88024">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owebqe0n9r9g-buGrnCI0sq7tGDw17nRh4jSqZ34kZL1PobB5QflwW-TIPZfcgRp0DF8tHOXxPQj8KXAH1LqoSguYi1_ju1jRvM5hBK5G_wubrczDS3HvzFt2jmfmVTbtX2nDnmzPJvTnUjPL_QjUou6KnpQYzg7UP3H4wVFZJf0O9jmvmMEVklNXhS-LZOhtROk_uLkqTfa68UgLZ-Iq5IBmxG1-BxX5SlaaM780adl_DGHEEPCvKD09GypLL3gfPzkB3406_ltb6ljMKqcLeH2idMwxCjxNE2n6gv_NQK2uJP6rBYUlVLmefAVm88AZGyYWMq4SFhOfjoPaV08lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">يوبخ ترامب صحفيًا من سي ان ان: اصمت! أنت تتصرف بقلة احترام أمام هذا الشاب. ألا ترى أنها تتصرف بقلة احترام؟ إنه يفهم. اصمت! أنت تنشر أخبارًا كاذبة. اصمت! أنت صحفي مزيف.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/88024" target="_blank">📅 00:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88022">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02a9f19058.mp4?token=a3Dv5NCh5XCaPjj2PGsn85GE62baz08aEL9dAl3rxxEC90F1xWMIdYwbK-7VnXFQUL3kZ0Pn39UGPFe0aGFmSgHX1c4IjBHv6q-oA8FVEi6wH1226Bu98SqrfKo-p3sRV5f4hl8qWRYBLpfq6GyUBoPcIlPCOp1BoRlDD_Cxyj2GJvxBzy1jKHG1AQtwkMnbYB9Hlnks-Ir5SEhcSK4JoAUomMPlqr2-f_xAMC276MWgdWczuEiewz6lIChIncuAQUFLA_YArnBB8obkMeleSLc9F9Ds5OIHXG_fSDN1cuE2Px9dW9oS7obR6wbshKDfCcxJYR5ylmRfLDe7H24f1o2A8F1bnvo6nbaf4T6HaS2l930N08MJ9Q4ePCXB3kqgV0O_1HlVZU3924c_0e2bqWf1VXVzM3LquaLoYYOJX8c_rPv98EpcZyxnlQE4LJSUWbmbVuJqgc4-bVJXfRkgcgCzmKm2UbPsTQzqq6fsATDGX4O1IHZdEaEorrlwSKajbG7StJcSYK83QecI2nhZnf8rK6946QWM0kfW1AUk-wlWtgWQdHpK1OJyvc3Q8Auhr2H0dvzLUZ8g99RGqOAXY9OYsxG4j8oSi678xxC6ynl9H3rDujWM83mIOTHTBRP0CeEN5-OB09pBxhQWjxVBDG2uNjRl0QI9sLpCA6K5DUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02a9f19058.mp4?token=a3Dv5NCh5XCaPjj2PGsn85GE62baz08aEL9dAl3rxxEC90F1xWMIdYwbK-7VnXFQUL3kZ0Pn39UGPFe0aGFmSgHX1c4IjBHv6q-oA8FVEi6wH1226Bu98SqrfKo-p3sRV5f4hl8qWRYBLpfq6GyUBoPcIlPCOp1BoRlDD_Cxyj2GJvxBzy1jKHG1AQtwkMnbYB9Hlnks-Ir5SEhcSK4JoAUomMPlqr2-f_xAMC276MWgdWczuEiewz6lIChIncuAQUFLA_YArnBB8obkMeleSLc9F9Ds5OIHXG_fSDN1cuE2Px9dW9oS7obR6wbshKDfCcxJYR5ylmRfLDe7H24f1o2A8F1bnvo6nbaf4T6HaS2l930N08MJ9Q4ePCXB3kqgV0O_1HlVZU3924c_0e2bqWf1VXVzM3LquaLoYYOJX8c_rPv98EpcZyxnlQE4LJSUWbmbVuJqgc4-bVJXfRkgcgCzmKm2UbPsTQzqq6fsATDGX4O1IHZdEaEorrlwSKajbG7StJcSYK83QecI2nhZnf8rK6946QWM0kfW1AUk-wlWtgWQdHpK1OJyvc3Q8Auhr2H0dvzLUZ8g99RGqOAXY9OYsxG4j8oSi678xxC6ynl9H3rDujWM83mIOTHTBRP0CeEN5-OB09pBxhQWjxVBDG2uNjRl0QI9sLpCA6K5DUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خلية الاعلام الامني:
نفذ صقور القوة الجوية بواسطة طائرات F-16 ضربتين جويتين ناجحتين ومباشرتين استهدفتا الموقع المحدد.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/88022" target="_blank">📅 00:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88021">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HXbhZnS-dCKoI7ydR6d6RGvB2QoOMAvHXNYpaBHYpaOaDB26XksuAv9CVy689J5Q1B0-3Zzavg0NI4wy7PZ7vKQnA7Ay91FmArKZxniSMGYw7VqRa2NfzD9XrUTu7YRM4QH3j7vg7EWaviLgqALV7SQ6cEOc5C023VEy6g6o5f9jlLe7HOwWNS7r7ShZbKgE8Y-eNaxeg3qhmysYDt3lIDld_o2hx1KMJPuEKp6vNV0FiLefD51sVsUMzuO_hG4Pu2RPJbLFSyhUwiB5WUCV2o7EFwt1vf5ffRVhYAMyqur3lGvCDenuMR0_RGkFuJyLlm26XS315JrCPRP8UwT2hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب ينشر:</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/88021" target="_blank">📅 00:18 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88019">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb50f87ee1.mp4?token=ZSwMXZXOXM9MQbNLqo6o0NuTHw3UYbkMieCugzaLjCmX8ghKUWpW_Gs7k1b5PVZ8f-YeXRKral3-dd5Rkgs3gIwqkR2GySdOSHlqMUODjcfIc1DnHMQomphH8eR_WbueDwqzH6T2L0FJxZo8FcASFFQA7GG3xT_K_vVC3Sx2jj3tXptOy1SIWTdPIbPSGIwR5hED4XOLmh6ae6-zQ288HB0MyNYIYCvgSNp2W6h-gU21LWOWLoR5soLKwcxkHOP2YK4ASVRqeWoTac821PUB1SgJICdu4IirUyNIvx4rPVGyIk7pDdU0AyyiyJU4An728bWFIqYrUl52J1RG5zessw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb50f87ee1.mp4?token=ZSwMXZXOXM9MQbNLqo6o0NuTHw3UYbkMieCugzaLjCmX8ghKUWpW_Gs7k1b5PVZ8f-YeXRKral3-dd5Rkgs3gIwqkR2GySdOSHlqMUODjcfIc1DnHMQomphH8eR_WbueDwqzH6T2L0FJxZo8FcASFFQA7GG3xT_K_vVC3Sx2jj3tXptOy1SIWTdPIbPSGIwR5hED4XOLmh6ae6-zQ288HB0MyNYIYCvgSNp2W6h-gU21LWOWLoR5soLKwcxkHOP2YK4ASVRqeWoTac821PUB1SgJICdu4IirUyNIvx4rPVGyIk7pDdU0AyyiyJU4An728bWFIqYrUl52J1RG5zessw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
القوات الحكومية تداهم منطقة العمارات الملح في محافظة ميسان جنوبي العراق بعد اندلاع تظاهرات تطالب بالخدمات</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/88019" target="_blank">📅 00:06 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88018">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سيصدر بعد قليل بيان هام للمسؤول الامني لكتائب حزب الله الحاج أبو مجاهد العساف.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/88018" target="_blank">📅 00:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88017">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‏
ألمانيا
: هجوم إلكتروني على وزارتين في حكومة ولاية برلين.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/88017" target="_blank">📅 23:49 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88014">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lOUxYnC86k3YKNqd1ajJoL5Xo_cVTt0FwVbuVU12fGLyH9uMquwC-VM5_8BRz54zxqwXo_WZkeCfwAj553vZowGK7Kvt4MEblW0fzmNPcyfjpk5OvzQRTaxrC53iyR4nl-YlID9bFmGPY-asGed07TlaS6NuuTwvt6rnA0AVmaIgkMZ6_4DWZ_LZmU8HvXFjVE_MZKK-pWGKEnnHXjrTcZ71lsSuUOOndO128m2PvkF0OzYBzjZ-oLRiYMvgHtaFa-yaBBfH6e1Uj-SqEyA7xYocdW9E-eYBfM662NsoMbOTSzQGeYrzYw2A2ECYK3bpXCjtgtUWR90Gg4q5DNZrZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/azQirVIbuyzV_-DhJn-xkU1TucxH8JiVDf9TFJOg_jWEOOc9uaZc_GztfbM1QQxgrvWri9IOkrZeee7qiwAuCp_dss4C2t7bdiNIblVpVCfxvYUmPCYGCEHUXuitMozid9mrNT95X6Qv0oJD7ptLo1y7NJXo-iYRRXuojuhYzye_71omMom8r6tVn5hLhEdY-x0IeApCinZiOi6cHiCM8Aqss7zrIoxtACqj5RKKMnZ5FXEilc931DuS_hUeZk7osPaGY8oMaLhROOxAUQbwl9K5-weMNIAOnXtRpVDYUfGuAgLmX0YwuRH-u6YWHg0G8KZPU-P942JJVQBlKD16Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NEsFV6t9eJf0MEFeVNAInJS5lnz52j1Cs91iDkJP7ZXq4g1qOwUHJQyjsnKemyZvLjl04qOs34Mkquf0nFQcb69SdYwcLNktshrHbx1SFOHZ3mBPPY8dalYkK3zySvRGUlVGqyqEvfATa2PH_GpI4UwTxyWUOjXmxZNas8J2-3s7EusZi82zv5Vjh5zEmEBpPEwk2x2o1CoOge6LCq4xurI6zaKGLak2lEIUXf17Khv80PsTtE6xvTmG9SgJ_3ChknH3APWFxDC3-cemWFJFmC9dqcLEFilpumJf15ekqDNpuRZy4fiWSi3bVV7Jx47TG9iehE5NpirfyQ9QpptMaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امتناع عدد من الطائرات المدنية عن الهبوط في مطار دبي، واتخاذها مسارات دائرية في الأجواء، لأسباب لا تزال مجهولة.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/88014" target="_blank">📅 23:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88013">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‏كوشنر: محادثاتنا مع إيران إيجابية وفعالة لكن لم نصل لتفاهم بعد.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/88013" target="_blank">📅 22:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88012">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LY0hMvXjQzE9mcNSbPVs6yCa8cCHI2JBwDrtJHr3kwDXKKZkOCUFPG6Y3iVDL-lJHtK2hrSk7B6Y8YvsDZVG4IMb5wB8ha0p2V_2_PfmirFG9LPX2LOuRm7r7knROrElMOPtQdQvxD9zE1S2wuipUAQlNA9fRAYcCb0ShIcGM0L2KZrrM_OzFhF9LlrDz0v7YDc9HXc4O5cO2onc4INV19YCQhd1WYh9xixDscDeSdsz7M0JDlsAc4kWboAIeDM5GGkf3rTamzgpMRBJJxC7S8jVh-fUqBe4YsuwkwA4pnvqeerNZLqxUGYt9OSc4JZvsn6_rpddZkzoB5EJVLahyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رويترز
: العقود الآجلة لخام برنت تصعد بما يعادل 2.65 % مسجلة 90.87 دولارا للبرميل عند التسوية.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/88012" target="_blank">📅 22:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88011">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gt6BxsHWXx53l9hThsJubZZ6sECMgreHaPOwUTUDQKrTB4NnisgjsMQWEC1x5gR13j4a5P_EPFLPTzgCDNkAFOv5kvTQ_2KgJyKCkVN3I0VZ7Sqkk2Qh75irjpIyttpT-lPL8xVK13rye3LoY1mgdKBy_6e8NZGonC5ao7E2dqPC68eXGhFkWqNGZON_8BoP8e1DB0WOigmn4b7B44O7KlUcaUCEeslba4jZqnBPKs3K767qkAWCsPl1wBeDfLaLueoK3mFpOrpn8JwBKqXSpQCZIXsipOxfhxIpNovSrKd_Qxm5kKcy7PQCgeWjQabuTkiuSWeLryLiYKj1SvJkTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقجي
: لا شيء يبرر الهجوم المتهور على مكتب رئيس الوزراء بارزاني. يجب على الأصدقاء الأكراد توخي الحذر من المؤامرات المفتعلة التي تهدف إلى زرع الفتنة بين الجيران.
لقد حمينا أصدقاءنا الأكراد من صدام وداعش، ونحن ممتنون للأمن الذي وفروه على حدودنا.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/88011" target="_blank">📅 22:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88010">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/def859cee1.mp4?token=W0BT5ziAw4HgJg311wWqgerAmsJfrhGP_xPzUx9NOTSuZl0PPsrOng-uES3NZfkCiLZskPSSTQ-KnQe117TTMtKw6YygUw0JNM1PkcNtis23LJsHC4BKJi4bpAtbf9gSDlV1NLXywy2SCExYLBMIt-XT1Zt8BlzxyMOpQ2cQ2jhI7q5piLKjR3CX42x4XDtcnzHE8wQ1_zD2UzR1nwyNQmTddWDLgkXlQizgdlb99sZDoJrc-L1DBHxCKqR-rnnsdcVHcXjmpEJtMIxGym2BDwmOlJH2xxFuCcSFxO9k-QjZiRIiP4VNFFS_SrqXRZnOii1LxNfaq-hwrNHbvBHfIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/def859cee1.mp4?token=W0BT5ziAw4HgJg311wWqgerAmsJfrhGP_xPzUx9NOTSuZl0PPsrOng-uES3NZfkCiLZskPSSTQ-KnQe117TTMtKw6YygUw0JNM1PkcNtis23LJsHC4BKJi4bpAtbf9gSDlV1NLXywy2SCExYLBMIt-XT1Zt8BlzxyMOpQ2cQ2jhI7q5piLKjR3CX42x4XDtcnzHE8wQ1_zD2UzR1nwyNQmTddWDLgkXlQizgdlb99sZDoJrc-L1DBHxCKqR-rnnsdcVHcXjmpEJtMIxGym2BDwmOlJH2xxFuCcSFxO9k-QjZiRIiP4VNFFS_SrqXRZnOii1LxNfaq-hwrNHbvBHfIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">يوبخ ترامب صحفيًا من سي ان ان: اصمت! أنت تتصرف بقلة احترام أمام هذا الشاب. ألا ترى أنها تتصرف بقلة احترام؟ إنه يفهم. اصمت! أنت تنشر أخبارًا كاذبة. اصمت! أنت صحفي مزيف.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/88010" target="_blank">📅 21:45 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88009">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8452420aca.mp4?token=cZit7qcV06XATVj4dBFdxlFfy2kjZW4jgBB2VSdUswsYhX4CXFZUVlE-QO_ZNdMP3JWmb7Pw0hl_4arSJz4Us7KXZCePjkY6YMv3UOProoR1gTnFkVTkIEGDGXvHf4V8B9s3YrFHHX4BqMDj6k1X3FmAjQpL4hdR6eQXzYTep6TP20A5mBNNcgW_02j1zyq0hwAV0kelioAyekuaP0NoQy7ci5cNglQsaP2EicqiUhpPPXGjRvmNQYevhtHV6oSBzyQCS9-pRPA9y5DfZT0pWHrd0DH-0UnaewOAwskWD5A97ToJxZ0L9JtEgaDkpEvJhkilejZGsJn1H9_jmWX7eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8452420aca.mp4?token=cZit7qcV06XATVj4dBFdxlFfy2kjZW4jgBB2VSdUswsYhX4CXFZUVlE-QO_ZNdMP3JWmb7Pw0hl_4arSJz4Us7KXZCePjkY6YMv3UOProoR1gTnFkVTkIEGDGXvHf4V8B9s3YrFHHX4BqMDj6k1X3FmAjQpL4hdR6eQXzYTep6TP20A5mBNNcgW_02j1zyq0hwAV0kelioAyekuaP0NoQy7ci5cNglQsaP2EicqiUhpPPXGjRvmNQYevhtHV6oSBzyQCS9-pRPA9y5DfZT0pWHrd0DH-0UnaewOAwskWD5A97ToJxZ0L9JtEgaDkpEvJhkilejZGsJn1H9_jmWX7eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: هدوء، هدوء، هدوء. أنتم وقحون للغاية. هدوء. من معكم؟  الصحفي: أنا من شبكة سي إن إن.  ترامب: أنتم تنشرون أخبارًا كاذبة. اهدأوا، اهدأوا، اهدأوا. أنتم صحفي كاذب.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/88009" target="_blank">📅 21:43 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88008">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311dd58f45.mp4?token=DCJ-l38n-Z6ghTCzCZrOz5u-TLMVNoKfLz9OLi061zIRTSLMrzmeRYESrb3VTQfrnJTV-6KuaaGLfGx-9tzuXxZUz50O9lYeP2NEsrjMVQ4d2h3OvP7fl8zRoWSkONV3ymrDQtBJdd9uZh8pkLeKieB4W0Z9ewmsMaD6faFOu52iGUrfGJppeYi9znmDn06NUV4U_YpvXXc0dcTtzMluQ_U7OfmHyB7-MjswrZMDKkQV_pvARZj1yQlXESb9EJxqMOOpwye8RmI-CkaqHoVAMRnH46Wpf7SgD69wi-GwxpXOoycu4CVcdLWFRURJm4rz5Jt_mOrYGrsT4MMjA_jBYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311dd58f45.mp4?token=DCJ-l38n-Z6ghTCzCZrOz5u-TLMVNoKfLz9OLi061zIRTSLMrzmeRYESrb3VTQfrnJTV-6KuaaGLfGx-9tzuXxZUz50O9lYeP2NEsrjMVQ4d2h3OvP7fl8zRoWSkONV3ymrDQtBJdd9uZh8pkLeKieB4W0Z9ewmsMaD6faFOu52iGUrfGJppeYi9znmDn06NUV4U_YpvXXc0dcTtzMluQ_U7OfmHyB7-MjswrZMDKkQV_pvARZj1yQlXESb9EJxqMOOpwye8RmI-CkaqHoVAMRnH46Wpf7SgD69wi-GwxpXOoycu4CVcdLWFRURJm4rz5Jt_mOrYGrsT4MMjA_jBYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: هدوء، هدوء، هدوء. أنتم وقحون للغاية. هدوء. من معكم؟  الصحفي: أنا من شبكة سي إن إن.  ترامب: أنتم تنشرون أخبارًا كاذبة. اهدأوا، اهدأوا، اهدأوا. أنتم صحفي كاذب.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/88008" target="_blank">📅 21:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88007">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d95f5147a.mp4?token=SCA3V31-Y8Uu40C3xduFdAtwVzINLpB9FmSxMIUBKDL6_ExuMwXW2lb5lSX1Gs3gbW2xpMuKuibrRt4oCy3xXlk9G5tC3APvc46tYiU17e9qwvcG3fgFzs10KTafNjmhLBrTFaqYe09P3_qzx-3sS5QhDOtfDEAVAQAH2aqquWvpoMlq6m4ieI5s3_3OBPSlwQknXdV_e0rrX7gKX3nk_C0NgGwJsU6KKEv5dZVeIYTaHe_7nQMOeIK6ZGFGoJ65r49WARliuzOMLHf687nba3zTtU6uHfr1-Y2q7jKMzKakmC7xmzKJi54jJjgvJbkcMBERoVHDtAIVpriPre7pnIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d95f5147a.mp4?token=SCA3V31-Y8Uu40C3xduFdAtwVzINLpB9FmSxMIUBKDL6_ExuMwXW2lb5lSX1Gs3gbW2xpMuKuibrRt4oCy3xXlk9G5tC3APvc46tYiU17e9qwvcG3fgFzs10KTafNjmhLBrTFaqYe09P3_qzx-3sS5QhDOtfDEAVAQAH2aqquWvpoMlq6m4ieI5s3_3OBPSlwQknXdV_e0rrX7gKX3nk_C0NgGwJsU6KKEv5dZVeIYTaHe_7nQMOeIK6ZGFGoJ65r49WARliuzOMLHf687nba3zTtU6uHfr1-Y2q7jKMzKakmC7xmzKJi54jJjgvJbkcMBERoVHDtAIVpriPre7pnIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترمب: سنقوم بإنهاء الاتفاق مع إيران.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/88007" target="_blank">📅 21:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88006">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFN-gW3_dgmM1gP-bZPp3Dtj7MeFwHwTG0UCjE_-XpAMZhu827W7TSgIJ7Em-2yAcS19dcDU-g5Pt3sYHUzTzqfvPZoZ6fq743Lx5KQsRwY6RQp6iBQwe9W1mW7yoHXH_W-SQHjK6u1HCwT3iw-yD5kZPoUQUWZOj9uNZjtG69-peIZwd_sw2yVn-6hqdPfKRejp9I0IKsR3bcwij6YO5zOTjjdh1-7gWBKxmDCD__2rfo3elEecRS03k3G12_f8jLYOv8ulOoJbeWWtQ_e7IESQ7RunHdywlNAPizDtjg-TswH3MMWuGu2bEWQvFumxTbmkr1nKm2Fcz81uPZV4Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدر لنايا
العامري في اجتماع الإطار التنسيقي كل بنادق فصائل المقاومة في العراق هي بنادق بدر قبل ان تكون بنادق جهات محترمة بالمقاومة …</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/88006" target="_blank">📅 21:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88005">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇺🇸
ترامب: قال لي رئيس جمهورية كوريا الجنوبية إنه يفضل عدم التدخل في الملف الإيراني.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/88005" target="_blank">📅 21:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88004">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇺🇸
ترامب
: قال لي رئيس جمهورية كوريا الجنوبية إنه يفضل عدم التدخل في الملف الإيراني.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/88004" target="_blank">📅 21:32 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88003">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6iXPXT-Gki3TBqX9kaOB-O6Y-vvaaHFCklp9_Z6-KXZe1ZrRLbhG1doye72sKO-In3-9k_NB_3ul45MRGIFSyNyx9pQ6SwXDJ50IY9UrlUJ0Wo2wBtKBomaI4NTx_iAE5jSdWCOx-mQPHodTWeKvxfbWkXxbGjhcbjbJmDsqUF8reQld49e8sj05y-cGowxE8TSNk0krFOA1qOuU9vjUyYHbJ3rBaz4PkRGxYVpXNI7NrjOThSBYVn6VDH803-qXO2JC-l5SEPq6-sycieTpVVuwvQ6YgJF9Bkgktza3TStdaTV4C7Lfkm-WPhIELFqBoP4YDVgbqRUoRD1RGhZSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وَدَّ الَّذِينَ كَفَرُوا لَوْ تَغْفُلُونَ عَنْ أَسْلِحَتِكُمْ وَأَمْتِعَتِكُمْ فَيَمِيلُونَ عَلَيْكُم مَّيْلَةً وَاحِدَةً ۚ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/88003" target="_blank">📅 21:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88002">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kKh3ONFAnhbvuQY3fz6o3a6fysp3eG8v4kKyQUiMoZ13uDdzwEf1XPJ-zKdRgf28Xah8KZQmSCmhlsXRoxMTHv-Ozd22iiTWjmnQSYDLIJZ79XfHiIV0VrFzEa1i76bkbWkkZXyLj1sj7iMnUwSQTnLwmD_OwQSHBKCa5th3htQX0EHc9Mt1-y5PvDZCeGEITaqQqbeXz79mKOQ18bKbbgdXvps0hQVXP99EQC88VtRqUrdRT24m88DDfryaMJnnDZkfo6SndczsUHIAa09teVZNOAoshZnbOqykeHScWyyBufb9YCndjl42hDlXplAM5okMCBRQAcXl_BZEy21bfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
السيد مقتدى الصدر:
أكرر قولي على الإخوة في الحرس الثوري عدم ضرب الأراضي العراقية فهذا عين شماتة الأعداء.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/88002" target="_blank">📅 21:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88001">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">العامري يسوگ عليهم باجتماع الإطار من مكتب سيد عمار الان   العامري يتصل على ابو فدك والفياض اطلقوا سراح سيد عباس فورا</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/88001" target="_blank">📅 21:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88000">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QH36O6x3x0-PnB8yAl0-fxnUvOmC3pHBJBgc_h_9hZrVZRjpcyPdZxJ65qNwpU6l-H-9uTIDdDSH95yNPv34Me5Ch_AI114ZvWtc2D2r0NO-k2F7XeCLiPi_4ouF0oLUnFnr2qDvFhJI1EK8Xm6nkj0LFCyG8QXzM6_cZrVfkUcFNO7aHBJcHvEMAgMygriE7VQn20pX25EmbcBXq_c0tSJoWj04YXy0Ol65natz30whsMrPxjuGu1qGTmjK_6ZUV6zEARXe_1bMwdFlWKmyQishisbpM_FyVgLDxxfM5k1OeH-NiCzdybN2t2ailFItnPHNanw8TUI_ay3rkkKdiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد قليل سوف يتم استلام المخطوف إلى أمن الحشد</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/88000" target="_blank">📅 21:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87999">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/87999" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔻
عاشت المقاومة العراقية البطلة وسلاحها الموجه نحو الاحتلال</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/87999" target="_blank">📅 21:14 · 26 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/cQin8y0qb98N7f43ogRG9hzrit8iKBQybSdGBChM5PDDz4opsSG-rTnYeH90gmwpWaUn5SjFZm5-Y5OK9ldzxtvwh6694UMfHimquuLAdFqX_OEPo3sVz5oaLR4Wy0gtZCGwPMQZXGvQ9JmVHvGhCHpufwbJLyRtMjwrhDVHqjzn3RyN4o2ev52hgb5StozctqXv4aEzQVVUCUFVPZdcceuwwBYq8jPD8BzFmEWmAKTNDFTf7E4V1CXkF2OpObfXLNq7-NPTr2rwOIBrQ_2eWoZVVraaSLfS0mZGeEX8UB2sL9xnkwHXhX-qrolTud-PFTJWqrQ-SAhOf4ml5UVc-A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 268K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-09 06:01:38</div>
<hr>

<div class="tg-post" id="msg-88864">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa1a420d2d.mp4?token=jAhacWnvgtvBLgGn7dQOQH_JXFnV3t_lmQ1ifZxChHHJEqmamiqwKvWi1mqtFPOT-92ke91eeaLbA9MDJ3mUq-J7e-706HlpF8D03YAz4NJja0CLI916fKi6C1XPWM9ZEE_Z7TLweAuMH42xKNZaHozhIZ1KKFoxGlxpKA9Dfts4_Q1t9O7LhIjD84OXcG1GaZIgQ8Az7DExsWh45CdVkGXbNuM9fhUOALnhbPALR7iUN0qn8rWRq15_GHG1O4f_3ILzJPNK-74r1VZLjQKGiGKJCJbqNW0Vzk5cjPgZD8ycJBq6GX71ESYzJI3ok57KiZEEvr1aXICyYxrZpYCSgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa1a420d2d.mp4?token=jAhacWnvgtvBLgGn7dQOQH_JXFnV3t_lmQ1ifZxChHHJEqmamiqwKvWi1mqtFPOT-92ke91eeaLbA9MDJ3mUq-J7e-706HlpF8D03YAz4NJja0CLI916fKi6C1XPWM9ZEE_Z7TLweAuMH42xKNZaHozhIZ1KKFoxGlxpKA9Dfts4_Q1t9O7LhIjD84OXcG1GaZIgQ8Az7DExsWh45CdVkGXbNuM9fhUOALnhbPALR7iUN0qn8rWRq15_GHG1O4f_3ILzJPNK-74r1VZLjQKGiGKJCJbqNW0Vzk5cjPgZD8ycJBq6GX71ESYzJI3ok57KiZEEvr1aXICyYxrZpYCSgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
😆
ترمب: جزيرة "خرج" الإيرانية تتعرض للتدمير</div>
<div class="tg-footer">👁️ 427 · <a href="https://t.me/naya_foriraq/88864" target="_blank">📅 06:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88863">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‏
😆
ترمب: جزيرة "خرج" الإيرانية تتعرض للتدمير</div>
<div class="tg-footer">👁️ 795 · <a href="https://t.me/naya_foriraq/88863" target="_blank">📅 05:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88862">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c79390d1f.mp4?token=fiO83DubEMPtVPf7dqPGsuLJiaUreHrFOWMGZ2l4NnQhb1ZQy75WnPMU7HtOHmYfmTbyRmnlQ_iS2SY2mLYoGDemc86PQnfwpQMRfCpm8VNT4F5DK9n4pEmwiK3GH0fvgxqSjzfkdD8q5ufnfBcy8IIQvl6PvfYxuMSSu6OIjMLqX6DhqkDZ6LncAeM0E78-JRBgX38hIXt-VkNh43o9DB32KUbermfmMrhKKcUp5AmAvlLcEdeM4z0jELd-YBU7EGmkmZsXCkOQH8JE2R7w_cXtkEYEp3Zj0nXXNYk8guYAU4KFt0JVCiEz6ug2Ybk-CnrsQoQl7_epmB1CjhPJ7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c79390d1f.mp4?token=fiO83DubEMPtVPf7dqPGsuLJiaUreHrFOWMGZ2l4NnQhb1ZQy75WnPMU7HtOHmYfmTbyRmnlQ_iS2SY2mLYoGDemc86PQnfwpQMRfCpm8VNT4F5DK9n4pEmwiK3GH0fvgxqSjzfkdD8q5ufnfBcy8IIQvl6PvfYxuMSSu6OIjMLqX6DhqkDZ6LncAeM0E78-JRBgX38hIXt-VkNh43o9DB32KUbermfmMrhKKcUp5AmAvlLcEdeM4z0jELd-YBU7EGmkmZsXCkOQH8JE2R7w_cXtkEYEp3Zj0nXXNYk8guYAU4KFt0JVCiEz6ug2Ybk-CnrsQoQl7_epmB1CjhPJ7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
ارتفاع أعمدة الدخان من مصفى الدورة جنوبي العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/naya_foriraq/88862" target="_blank">📅 05:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88861">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e138b9204f.mp4?token=EjV38w_wWVOvSwHuupLnZiCa-tcGeRlyd4CruZMr6pM7vIh_YIlkt5GGrBTtpQwqxThH9ByIiRJelbq_ll0Fo8OBahNA-Hv_rLAQ-xgfT9bS4o9ET_ap7Nw4sHepZRZzc0ynjGZuufPlcEsWug3mPYhXAsVFymVFRxXDJq_exQ3eVMnmAbsVl3iPaPI1Vy64ok9JGnPHxa451Q0qPtj_n-dUhwxmz17Kcd90nF310K9lyzprGLQRekC5ywSVc5MD34xzsQG2intrT54AKKnTaAwWVmHaNN8Dov3dfM_dEIAZDQuY6PZUBWx153HyPsWiFZEHmgGwH0yJHBfQOmEt0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e138b9204f.mp4?token=EjV38w_wWVOvSwHuupLnZiCa-tcGeRlyd4CruZMr6pM7vIh_YIlkt5GGrBTtpQwqxThH9ByIiRJelbq_ll0Fo8OBahNA-Hv_rLAQ-xgfT9bS4o9ET_ap7Nw4sHepZRZzc0ynjGZuufPlcEsWug3mPYhXAsVFymVFRxXDJq_exQ3eVMnmAbsVl3iPaPI1Vy64ok9JGnPHxa451Q0qPtj_n-dUhwxmz17Kcd90nF310K9lyzprGLQRekC5ywSVc5MD34xzsQG2intrT54AKKnTaAwWVmHaNN8Dov3dfM_dEIAZDQuY6PZUBWx153HyPsWiFZEHmgGwH0yJHBfQOmEt0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
ارتفاع أعمدة الدخان من مصفى الدورة جنوبي العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/naya_foriraq/88861" target="_blank">📅 05:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88860">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇺🇸
ما تسمى القيادة المركزية الاميركية:
زعم الحرس الثوري الإيراني في بيان صدر مؤخراً أن الضربات التي شنتها القوات الأمريكية لمنع الحرس الثوري من زرع ألغام في مضيق هرمز كانت "عملاً عدوانياً". هذا الادعاء باطل تماماً.
اتخذت القوات الأمريكية إجراءً محدودًا ودقيقًا ضد قوات زرع الألغام التابعة للحرس الثوري الإيراني التي كانت تشكل تهديدًا وشيكًا في مضيق هرمز. في جوهر الأمر، إيران هي من خلقت هذا التهديد، وقام الجيش الأمريكي بإزالته لحماية البحارة المدنيين، والشحن التجاري، وحرية حركة التجارة العالمية.</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/naya_foriraq/88860" target="_blank">📅 04:28 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88859">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇮🇷
🔻
الحرس الثوري:  لحظة إطلاق الصواريخ في عملية "محمد بن عبد الله (ص)" المشتركة بين الطائرات المسيرة والصواريخ، والتي استهدفت البنية التحتية والمرافق الفنية ومواقع تمركز طائرات العدو في قاعدتين جويتين أمريكيتين في الأردن، وهما قاعدة "الملك حسين" و"الأزرق"،…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/88859" target="_blank">📅 03:20 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88858">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترفيهي
🔻
الجيش الأردني:
اعتراض 8 صواريخ اخترقت المجال الجوي للمملكة.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/88858" target="_blank">📅 02:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88857">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔻
وول ستريت جورنال:
تسعى إدارة ترامب إلى تجنب العودة إلى مواجهات عسكرية واسعة النطاق مع إيران، وهو ما قد يزيد من الضغط على مخزونات الولايات المتحدة من صواريخ الاعتراض وأنواع أخرى من الأسلحة.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/88857" target="_blank">📅 02:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88856">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a27dc0bc98.mp4?token=NNF_-tFhJlyx5_S7aVINknmJLEr8j4zJxF0UPPId1hcOzwqHUDCNe3gOtzZPLEF5VEm3ZFaeoyTA5r3loqC39Xo8chtLd8v7wL0ejnZxduKP05bisqlQwBB5TlPgfBKtyFSPz7QJ2lp-hgppnlzKGmXE-2DAGINZDMipSd8OwyRUi75WlCLkB1Iv2sOPiZSdv84m4vb8TqK-pHdeVj20_DjmE_AmzinZc3jMs3e6fqSVDAxHHGQGaVSEAXBw8Bjul-jEhBFPLQZnKDOgdjLgTFjRYR36zxvm0aryNbPXF3dPg2aAym470ws675KnTeasFxTOnLmjRpey05rKRY8wEa2oSf94gYllf28b5cpFH9PVUjfH0RjHknyoSffz_XUP1h8yu9hHpefBaIaNpsvnFAUUefdwbw5OFA5S3UcQhQufbgQvYMFGYArLbbWs--ieyuU5KW_a07ryJDJkDIqn6RNJNlwlGUNzvGL5wBeLIX1-tB41uke-xR2GfOFVOGbbeA-cp6koMaj5jAD2jk-5yjE7Ot4wI9dBQA4_4nz966pSEBRifMSj_4ZJ2gcMtBYKf20IZik-GaMBVp2pfKR5icQhwehqadavTMnVTEE3hByt627Z9aocnfs-60zo54fRklTI7_xu80FyCgb88KOfH4uhNeqXRoe72zenuV4tXdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a27dc0bc98.mp4?token=NNF_-tFhJlyx5_S7aVINknmJLEr8j4zJxF0UPPId1hcOzwqHUDCNe3gOtzZPLEF5VEm3ZFaeoyTA5r3loqC39Xo8chtLd8v7wL0ejnZxduKP05bisqlQwBB5TlPgfBKtyFSPz7QJ2lp-hgppnlzKGmXE-2DAGINZDMipSd8OwyRUi75WlCLkB1Iv2sOPiZSdv84m4vb8TqK-pHdeVj20_DjmE_AmzinZc3jMs3e6fqSVDAxHHGQGaVSEAXBw8Bjul-jEhBFPLQZnKDOgdjLgTFjRYR36zxvm0aryNbPXF3dPg2aAym470ws675KnTeasFxTOnLmjRpey05rKRY8wEa2oSf94gYllf28b5cpFH9PVUjfH0RjHknyoSffz_XUP1h8yu9hHpefBaIaNpsvnFAUUefdwbw5OFA5S3UcQhQufbgQvYMFGYArLbbWs--ieyuU5KW_a07ryJDJkDIqn6RNJNlwlGUNzvGL5wBeLIX1-tB41uke-xR2GfOFVOGbbeA-cp6koMaj5jAD2jk-5yjE7Ot4wI9dBQA4_4nz966pSEBRifMSj_4ZJ2gcMtBYKf20IZik-GaMBVp2pfKR5icQhwehqadavTMnVTEE3hByt627Z9aocnfs-60zo54fRklTI7_xu80FyCgb88KOfH4uhNeqXRoe72zenuV4tXdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🔻
الحرس الثوري:
لحظة إطلاق الصواريخ في عملية "محمد بن عبد الله (ص)" المشتركة بين الطائرات المسيرة والصواريخ، والتي استهدفت البنية التحتية والمرافق الفنية ومواقع تمركز طائرات العدو في قاعدتين جويتين أمريكيتين في الأردن، وهما قاعدة "الملك حسين" و"الأزرق"، وذلك بإطلاق صواريخ باليستية.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/88856" target="_blank">📅 02:29 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88855">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWDuymaTfur9vOMO3tmKH2kJVFl61J9QYmaNeO0d4zrs7KCpCFLOyEndxGWnnyhHqpN7QLinSNOzKUPH8O0LJNYk1dJDXKFM7cttVSq98ReteZU09gRAKcE-EPalyx4XR_FomVhoWsNOfhch_gpq11LU1FELhQFSj1WjrKzf1zDWwxdySpiYMuVQNYXFDnKyvrg51qRijHusOdRuTATL533khaHbbsGn5E-9fkCwx4RbRGeW-08IczWletFoEpBumfV2GXixPEABrOoEej0GhwxI2VNTc0U4MdVUEvafqgnilEaP2zYEjJRJA2erNnaY3P5eOecVhh8WhoTzFwuNNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من الرشقات الصاروخية الإيرانية التي أطلقت نحو القواعد الأمريكية في الأردن.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/88855" target="_blank">📅 02:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88854">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔻
🇮🇷
الحرس الثوري:
بسم الله قاصم الجبارين
"فَمَنِ اعْتَدَىٰ عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَىٰ عَلَيْكُمْ"
🔹
أيها الشعب الإيراني الكريم والثائر،
إن تواجدكم البطولي المتواصل وغير المسبوق لمدة 183 ليلة في الميدان، قد أذهل العدو وأثار دهشته، وهو مصدر أمل للمستضعفين ونور لعيون مجاهدي الإسلام.
🔹
قبل دقائق، قام مقاتلو القوة الفضائية التابعة لحرس الثورة الإسلامية، ردًا على العدوان الجوي الذي شنته العدو الأمريكي والصهيوني على جزيرة "لارك"، بعملية "تأديب المعتدين" من خلال عملية مشتركة بالصواريخ والطائرات المسيرة تحت اسم "يا محمد بن عبد الله (ص)"، حيث تم تدمير البنية التحتية الفنية والإصلاحية ومواقع استقرار طائرات العدو في قاعدتين جويتين أمريكيتين، وهما "الملك حسين" و"الأزرق" في الأردن، وذلك بإطلاق صواريخ باليستية، مما أحدث أضرارًا جسيمة.
🔹
حذر حرس الثورة الإسلامية، مؤكدًا أن العدوان والجريمة لن تحل مشكلة استياس العدو من إضعاف سيطرة الجمهورية الإسلامية على مضيق هرمز، وأن كل هجوم سيقابل بردود فعل أقوى.
"وَمَا النَّصْرُ إِلَّا مِنْ عِنْدِ اللَّهِ الْعَزِيزِ الْحَكِيمِ"</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/88854" target="_blank">📅 02:21 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88853">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">انفجارات تهز الامارات</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/88853" target="_blank">📅 02:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88852">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پاسخ کوبنده فرزندان ایران زمین همچنان ادامه دارد</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/88852" target="_blank">📅 02:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88851">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇸🇦
توقف العمليات الجوية في مطار الملك عبدالعزيز في جدة السعودية.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/88851" target="_blank">📅 01:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88850">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مسؤول أمريكي: نتعرض لهجوم صاروخي من إيران</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/88850" target="_blank">📅 01:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88849">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/755c0bd3e6.mp4?token=cPFFuvHM6wV_5DqyHEMz6S0Z-yjJgvWwXKBL7iJgWbsNR8SmlLfIPRoUzSniPzbrqomjOLounqRloHZSf_qtNSnoaS12LmSHeektkeFDntB1Qe4t-FcgutInOeRvk8XuErnwgY7uWeTolJvvWC5HKEc-x5hlzokTDP6f1GDpJYgriI3YEwK0Dfs68URTuoH7y_V1ShNRi8LRkHQERUrH42HAtu6DL9KXsjjETfRzzIpFITh4dEhFG7rQx_cA9u3ErFxOvmqfXERCP0a5crnIB7G__90WIPV1_ZMJZncgfqy1KFzrNdEy02nC1p2-PZKl9inzHc4b7sCvnqedcFMKaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/755c0bd3e6.mp4?token=cPFFuvHM6wV_5DqyHEMz6S0Z-yjJgvWwXKBL7iJgWbsNR8SmlLfIPRoUzSniPzbrqomjOLounqRloHZSf_qtNSnoaS12LmSHeektkeFDntB1Qe4t-FcgutInOeRvk8XuErnwgY7uWeTolJvvWC5HKEc-x5hlzokTDP6f1GDpJYgriI3YEwK0Dfs68URTuoH7y_V1ShNRi8LRkHQERUrH42HAtu6DL9KXsjjETfRzzIpFITh4dEhFG7rQx_cA9u3ErFxOvmqfXERCP0a5crnIB7G__90WIPV1_ZMJZncgfqy1KFzrNdEy02nC1p2-PZKl9inzHc4b7sCvnqedcFMKaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من الهجوم الصاروخي على موفق السلطي في الأردن</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/88849" target="_blank">📅 01:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88848">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45fbe0853d.mp4?token=p25u6NYRCtxvH4UK0ZUcBpz4EjI1RGH3GSwRccAw7sa6EF4LpSrjZ3Q10yYyAio0A0ZauuzqTX5H-cLHIC9hm-nrnohzqbA5NEVQSZQgW0ljgJ0LoumvvT3BlnOBqg0EY9Vc-9lKKPOnEbuKVmfJoOpHGiREovn5Szj9ZMU42OGoQskMS_omikpuQ-99Updnx6m4yM-Ga4LSDYWImd1N3DRprr5suGozOW2ynH18UQZVkrP7hdI3WbEuV8GxX5UmHU9T6Gwlpk7_a9pJxACSpE5hk2wC7rP8Vbuwc19Ih_zjL2GgH45Q5DkCT44I8XjRZswuZ4T3gnU6Ypzk_OrRhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45fbe0853d.mp4?token=p25u6NYRCtxvH4UK0ZUcBpz4EjI1RGH3GSwRccAw7sa6EF4LpSrjZ3Q10yYyAio0A0ZauuzqTX5H-cLHIC9hm-nrnohzqbA5NEVQSZQgW0ljgJ0LoumvvT3BlnOBqg0EY9Vc-9lKKPOnEbuKVmfJoOpHGiREovn5Szj9ZMU42OGoQskMS_omikpuQ-99Updnx6m4yM-Ga4LSDYWImd1N3DRprr5suGozOW2ynH18UQZVkrP7hdI3WbEuV8GxX5UmHU9T6Gwlpk7_a9pJxACSpE5hk2wC7rP8Vbuwc19Ih_zjL2GgH45Q5DkCT44I8XjRZswuZ4T3gnU6Ypzk_OrRhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انقضاض الصواريخ الإيرانية على قاعدة موفق السلطي الأمريكية وسط تفعيل مكثف لمنظومة الباتريوت الدفاعية</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/88848" target="_blank">📅 01:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88847">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f2d04d67d.mp4?token=BSbB4Ch8EXqUbJpg_9S7SycCmfq92Dup1i3z_gWWAFhNn0fhetl1hh8E56bfETj2GxLbSolQqToPz54BBdEG1TqFJaSfA8RhruqeENlj_RQj5ZTn82xcDk-Z6okvi0fmTMKWP4mCpqjkS3LX4uZztF5Xb3gYIk792A0taere4lC8gBm9FQR6kEcmhr9z5wvzTlIZBGcL-dSSvUj8YOSPXjvRxdFdexVoou89yv-ND-9vrHmNaVjUalsBLIq8TaceTc6Sq1rVXanjPkQRqyhkKRtlRdz0Nqac4XIKi2V3S6G6T51E6lcNtP-ABdINkWH7q81dPukurivSHfvJ1caX4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f2d04d67d.mp4?token=BSbB4Ch8EXqUbJpg_9S7SycCmfq92Dup1i3z_gWWAFhNn0fhetl1hh8E56bfETj2GxLbSolQqToPz54BBdEG1TqFJaSfA8RhruqeENlj_RQj5ZTn82xcDk-Z6okvi0fmTMKWP4mCpqjkS3LX4uZztF5Xb3gYIk792A0taere4lC8gBm9FQR6kEcmhr9z5wvzTlIZBGcL-dSSvUj8YOSPXjvRxdFdexVoou89yv-ND-9vrHmNaVjUalsBLIq8TaceTc6Sq1rVXanjPkQRqyhkKRtlRdz0Nqac4XIKi2V3S6G6T51E6lcNtP-ABdINkWH7q81dPukurivSHfvJ1caX4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موجة صاروخية تدك قاعدة العديد الأمريكية في قطر</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/88847" target="_blank">📅 01:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88846">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">انفجارات تهز قطر</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/88846" target="_blank">📅 01:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88845">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e60316bfc.mp4?token=hLf_IjAzwXz2v8dbzIgXuGPjsBSywxzmVStQYdCsmTbz-fyHiA7yNlJVQmZI46LcX1N_4LO7jEjE5FZq3pT1XfDfNt8kB4TgRyP_9iYPAdQVasVMEpA_pEDhSBUDUw-TDEqML68B5jsK_lq0kF_Eyvsu0GG4z1y60hR-_YTrh73Ke5dkgT0opfheQi1ZwXxgZKQuMWK_33ayjLIoWreirywR40A0RYb6-NlpMZJfkQMj8w9LE4DzLHrWa511oq68zM6lAXuCH_YIozOw9_ha6N1iY58U6y6SZ2w0fM-ITKLSzYa-SUMRKP6kaMcMSKBp9UE_ru4rOM4QGum2oqqnEWVYsA-HOqBr6yZ_LzjkgPa4lYsL2bc-Wo2rqH9CcruNhLJGjStU9oSD8nvbkMHGz5jsK_h1hKcKFDyzxcacIceBunQcp8jZSPVeXvsdzEd70ibO5qlgcUU8gfuGbMr-hjvNxsSTaa3SlqESCKj06JEe4iOkQSzoRlk9PzvJEWkACME4MNUfxkv1-5koLnpSSU-Y02jYIgSZ_GRBIqihvfw1BNgMHTfroTZvTcSn-zCDgf0cLrTv2bZqMktYueN7a5QuMOIfxC9q-Rv0N3rZ_DPnndCZ3xVK36CFvZNO2o3mPUeukPURvS45NZIztdq5CG5gZ6OGHBRiNf0m7Fn1710" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e60316bfc.mp4?token=hLf_IjAzwXz2v8dbzIgXuGPjsBSywxzmVStQYdCsmTbz-fyHiA7yNlJVQmZI46LcX1N_4LO7jEjE5FZq3pT1XfDfNt8kB4TgRyP_9iYPAdQVasVMEpA_pEDhSBUDUw-TDEqML68B5jsK_lq0kF_Eyvsu0GG4z1y60hR-_YTrh73Ke5dkgT0opfheQi1ZwXxgZKQuMWK_33ayjLIoWreirywR40A0RYb6-NlpMZJfkQMj8w9LE4DzLHrWa511oq68zM6lAXuCH_YIozOw9_ha6N1iY58U6y6SZ2w0fM-ITKLSzYa-SUMRKP6kaMcMSKBp9UE_ru4rOM4QGum2oqqnEWVYsA-HOqBr6yZ_LzjkgPa4lYsL2bc-Wo2rqH9CcruNhLJGjStU9oSD8nvbkMHGz5jsK_h1hKcKFDyzxcacIceBunQcp8jZSPVeXvsdzEd70ibO5qlgcUU8gfuGbMr-hjvNxsSTaa3SlqESCKj06JEe4iOkQSzoRlk9PzvJEWkACME4MNUfxkv1-5koLnpSSU-Y02jYIgSZ_GRBIqihvfw1BNgMHTfroTZvTcSn-zCDgf0cLrTv2bZqMktYueN7a5QuMOIfxC9q-Rv0N3rZ_DPnndCZ3xVK36CFvZNO2o3mPUeukPURvS45NZIztdq5CG5gZ6OGHBRiNf0m7Fn1710" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دويلة الكويت تطفئ مشاعل أبار النفط وتبدء التعتيم خوفا من الاستهداف والرد الإيراني.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/88845" target="_blank">📅 01:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88844">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">انفجارات تهز قطر</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/88844" target="_blank">📅 01:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88842">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-iIVJ_6RL5rcvNmvIcvCCTECQo_FcWAoSF0HO1v_fXiBfZqQR5CEwGvlZqdH3UYyMW5zoeveuuW1yl66ntu-N4iVFnnlJ2tEFEW-uwnazHy_UsoP8evQvFIzWl0VweEeCO74B_vNVPA_VGVpui2gm3ibl42EWMOZj70iWxfetVB0TxAK8Hn2fz7G61OMuASwaoUG5RWfF-kwEjaNXoGwPVtOOHl5K9vmjMwf-EiW_-BevP5OKTCRBEYoHvt1GNZmdi8HiLHR_TMj_nHypgWDJTMVpXoRBNKGX70arDkcOxnNCWJY99JoOF4YGBee2ejJ-LRHfEPY_2DzvTvV-b1Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5aaf124627.mp4?token=X9evBrO2WPAYcgl8T8wEcKEH2Y_5KEHSzrzW9KgpBBdXYjND-W8X7F2Cdf0aSk4CoRAMpZrFkaJ8FLzM4ue45bNvYHFTuja5dmt6pgfkE4ZMJmMU_BiMfvd2T_IGf9DKOM0J8JGe0rDzjqynEzYJygdPlSqucT6Gpd99Pn9UhB6kyZTz5Wpd5xr09iO8zj1XmtHSP7LgOcrWBOcx9-Xtw2q5_k48KNXI5tFOqXRHBc_PuIFuWPicnyhngq2FzeJ7PlByinrDQly9NViv6Yo9C3Kr3tI89P0ql4Xwrbla-4lpwbw4hh6mcmtRstYZlYzT08gMC4qEOhuLS0mX0Vf5mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5aaf124627.mp4?token=X9evBrO2WPAYcgl8T8wEcKEH2Y_5KEHSzrzW9KgpBBdXYjND-W8X7F2Cdf0aSk4CoRAMpZrFkaJ8FLzM4ue45bNvYHFTuja5dmt6pgfkE4ZMJmMU_BiMfvd2T_IGf9DKOM0J8JGe0rDzjqynEzYJygdPlSqucT6Gpd99Pn9UhB6kyZTz5Wpd5xr09iO8zj1XmtHSP7LgOcrWBOcx9-Xtw2q5_k48KNXI5tFOqXRHBc_PuIFuWPicnyhngq2FzeJ7PlByinrDQly9NViv6Yo9C3Kr3tI89P0ql4Xwrbla-4lpwbw4hh6mcmtRstYZlYzT08gMC4qEOhuLS0mX0Vf5mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">السماء تتزين بالصواريخ الإيرانية المتوجهة نحو القواعد الأمريكية</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/88842" target="_blank">📅 01:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88841">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">السماء تتزين بالصواريخ الإيرانية المتوجهة نحو القواعد الأمريكية</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/88841" target="_blank">📅 01:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88840">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fcf5d931c.mp4?token=NHnOTNy1lco1baj3qBWaGAUV5zS9bcsVEHpB3lsVKocAWVbrGGFrY46vByqViCj_FWYGUsR2bGhBCD-p_i6FrCOKKt9gR3xQV9ReF8tFffxLBV4BNKav0QGQ6H205vj1Ov4q5qR655ioNBkq2xt6lpZh9yBiIRcGNaOdVJXrWRrbXweRMgWWqSI2FG6B9H35YGW5tuiJgyugpQSxz6JGWcMRRQyzGCXu9bcotU9cG7Jb5QvOYYoBjxvL4FT1knHoanknplMpH1hgqEhYEDIF7wLGUVpnDf2kAprgmqTwmTTipKFPIB2X3os4oaGkxnmdc536j284hUmJb8hLEl0hHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fcf5d931c.mp4?token=NHnOTNy1lco1baj3qBWaGAUV5zS9bcsVEHpB3lsVKocAWVbrGGFrY46vByqViCj_FWYGUsR2bGhBCD-p_i6FrCOKKt9gR3xQV9ReF8tFffxLBV4BNKav0QGQ6H205vj1Ov4q5qR655ioNBkq2xt6lpZh9yBiIRcGNaOdVJXrWRrbXweRMgWWqSI2FG6B9H35YGW5tuiJgyugpQSxz6JGWcMRRQyzGCXu9bcotU9cG7Jb5QvOYYoBjxvL4FT1knHoanknplMpH1hgqEhYEDIF7wLGUVpnDf2kAprgmqTwmTTipKFPIB2X3os4oaGkxnmdc536j284hUmJb8hLEl0hHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">السماء تتزين بالصواريخ الإيرانية المتوجهة نحو القواعد الأمريكية</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/88840" target="_blank">📅 01:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88839">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7130d96ff8.mp4?token=pT_qd6MxJ4tT2lnQ9hZp3vcMc9sJxh8LP1PSIDjIR965xEfwvGFGVIdArRyOqsEh-4Q9afDivKBiiwtGJ13Xr3NOqPHrQRWPkA11TLAQ8u0QRu77_-le8TxrRzuano1MFyj8zjAowumFkH6zdVaYh2JUwJwRkNhTpY_JPMwb4hjojObjrHm9c2S82DypRzH2_JJ16VYlCGy4UiFZN32fidT_YPHluer7EuohTcNvZOlTYNUgFd_TzAjTTt-UB8U1tkRrJEBsxeqqGG4mfGAEc044WsNxvvWwf1ygUx3LDvcFFuYg3plwyiLdRNmz3Yu1RmJ_hQKf8IBh7dN3dYgKHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7130d96ff8.mp4?token=pT_qd6MxJ4tT2lnQ9hZp3vcMc9sJxh8LP1PSIDjIR965xEfwvGFGVIdArRyOqsEh-4Q9afDivKBiiwtGJ13Xr3NOqPHrQRWPkA11TLAQ8u0QRu77_-le8TxrRzuano1MFyj8zjAowumFkH6zdVaYh2JUwJwRkNhTpY_JPMwb4hjojObjrHm9c2S82DypRzH2_JJ16VYlCGy4UiFZN32fidT_YPHluer7EuohTcNvZOlTYNUgFd_TzAjTTt-UB8U1tkRrJEBsxeqqGG4mfGAEc044WsNxvvWwf1ygUx3LDvcFFuYg3plwyiLdRNmz3Yu1RmJ_hQKf8IBh7dN3dYgKHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ الإيرانية تنطلق نحو القواعد الأمريكية</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/88839" target="_blank">📅 01:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88838">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/315c7b50c1.mp4?token=IgBzEHrTHLrrtVEXTI3PdnmzXyppORCLmndsOpiR7k_TkPf0enGXoI4OtyU47_B7AZWDQwEhyZvuUWCF6ZoRK4Fk0aQOzwzPXu38Gz7q5k-cU9-PUvoLO8snNSTHtweMeI7YR6BW5FjL1KFGF9nLpigtnTYtciOFwRj1SLNteF_RK81XuvPh3JuyB12oiIIZRN38464CYAvgFnxP-t9y_nNnX4iOtbOJYOI-ArfUFbp3Tft8TvZSdDOi4UbAjBGhgGVzeO3yh2yA1RHFwZRsqlu9rJmUaQYWP0NpG-cawniv8mUZAdAKnWQ13hSIGg5JfBloVNfSwUk_n57Xfgij7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/315c7b50c1.mp4?token=IgBzEHrTHLrrtVEXTI3PdnmzXyppORCLmndsOpiR7k_TkPf0enGXoI4OtyU47_B7AZWDQwEhyZvuUWCF6ZoRK4Fk0aQOzwzPXu38Gz7q5k-cU9-PUvoLO8snNSTHtweMeI7YR6BW5FjL1KFGF9nLpigtnTYtciOFwRj1SLNteF_RK81XuvPh3JuyB12oiIIZRN38464CYAvgFnxP-t9y_nNnX4iOtbOJYOI-ArfUFbp3Tft8TvZSdDOi4UbAjBGhgGVzeO3yh2yA1RHFwZRsqlu9rJmUaQYWP0NpG-cawniv8mUZAdAKnWQ13hSIGg5JfBloVNfSwUk_n57Xfgij7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ الإيرانية المتجهة نحو القواعد الأمريكية في الأردن</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/88838" target="_blank">📅 01:36 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88837">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">أسعار النفط تصعد بأكثر من 2%</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/88837" target="_blank">📅 01:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88836">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd66fd0ad1.mp4?token=iurA3oCLJanQuScOgEhjhY72vkZFEZffCqBq6dzTA0frGncwwqw5v517lbWSkOF0FnGcQuhDEjD1sSHpA0Q6TXNfGMdGeWT2CJN2GL2VduHrdz9_ylUusD_hIjfHimYzd62EbAM041mkTo9meebnqf5JRxaI2l6AuRJgWW8dxaHrq1GW6U8WzctQ8LD19MaNPYIBfPF7xhzT41fl18mhyt_3L8bMyugnSSIJK-ExS2k7MbLQ2gjgQBxtvudxRTy4lFBZBifsIsj2F6j5mxNLZ_qMfCDGyG9tA88GYgtXyiR2egdHqqy_4bJtuMm3OurUO-YqVIPcCC-YrEi1OR76SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd66fd0ad1.mp4?token=iurA3oCLJanQuScOgEhjhY72vkZFEZffCqBq6dzTA0frGncwwqw5v517lbWSkOF0FnGcQuhDEjD1sSHpA0Q6TXNfGMdGeWT2CJN2GL2VduHrdz9_ylUusD_hIjfHimYzd62EbAM041mkTo9meebnqf5JRxaI2l6AuRJgWW8dxaHrq1GW6U8WzctQ8LD19MaNPYIBfPF7xhzT41fl18mhyt_3L8bMyugnSSIJK-ExS2k7MbLQ2gjgQBxtvudxRTy4lFBZBifsIsj2F6j5mxNLZ_qMfCDGyG9tA88GYgtXyiR2egdHqqy_4bJtuMm3OurUO-YqVIPcCC-YrEi1OR76SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موجة جديدة تنطلق</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/88836" target="_blank">📅 01:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88835">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ee455c5e0.mp4?token=UeegCEeg4dFJLfph4ZuPm5s3jthtjTdGpHlMwVWd73HJKQke4gbXfEn9VCUVXqaJxKJuDmMhHz1iKlsIXKdeUDwzbm0dlOwUFeV4cVVladphwehCK01vSqVZ7rxvSCC2RuIWtE6UmJKYTMr4wQhi20COv-AHCywVdyJ4YZMt8Oz4phQY1df6pwrK7wtUp-PNohKWk6zweYq5RQtHe39vF2s1DBV5tcWiLTVdHggT5ty-WxrH9-1451pwbtU4a3Y4mb6GPKF2C7oFCkn-e1unKrglAP9vQKzZ5_MmJx9GQdPEE5r5OkHzH2UYl2Uh7JlN_z4wK13GNKVrolL3clC3WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ee455c5e0.mp4?token=UeegCEeg4dFJLfph4ZuPm5s3jthtjTdGpHlMwVWd73HJKQke4gbXfEn9VCUVXqaJxKJuDmMhHz1iKlsIXKdeUDwzbm0dlOwUFeV4cVVladphwehCK01vSqVZ7rxvSCC2RuIWtE6UmJKYTMr4wQhi20COv-AHCywVdyJ4YZMt8Oz4phQY1df6pwrK7wtUp-PNohKWk6zweYq5RQtHe39vF2s1DBV5tcWiLTVdHggT5ty-WxrH9-1451pwbtU4a3Y4mb6GPKF2C7oFCkn-e1unKrglAP9vQKzZ5_MmJx9GQdPEE5r5OkHzH2UYl2Uh7JlN_z4wK13GNKVrolL3clC3WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء الأردن تشتعل بالصواريخ الإيرانية</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/88835" target="_blank">📅 01:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88834">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c39dbf9bd0.mp4?token=eKVy4B_90gG7OvipWJA9Vnln3_KGchYyVGUjK-LSo2WW3F60Zh6sptp6Lq_IVvLrSlmiBBhbyo1v6Vsy7lls27arRfdrX3q58wZ_rTrj4tdMEtvxF3dEhBQJ91rfI5ZGMIromhqXDfPT7eyH_Ni-6vOGIqI8i-7jPfAEy00dS3IJdwwZ5Qxr2dSvg9Gv0Q4tNXyYYAB_KuTVfgdjdH9JdwcIm_Z_GZBLrKAyJtAlfUxWy8Yt3k9LScyUXf0dHUJeHG2Ux4RxzAtMh7YfCGcBVzJUj4KSapRKQ3TWIerRF5BymPoeTSnuAFxTZluByNh0YFyXwkJosLYPiKi-43pO1jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c39dbf9bd0.mp4?token=eKVy4B_90gG7OvipWJA9Vnln3_KGchYyVGUjK-LSo2WW3F60Zh6sptp6Lq_IVvLrSlmiBBhbyo1v6Vsy7lls27arRfdrX3q58wZ_rTrj4tdMEtvxF3dEhBQJ91rfI5ZGMIromhqXDfPT7eyH_Ni-6vOGIqI8i-7jPfAEy00dS3IJdwwZ5Qxr2dSvg9Gv0Q4tNXyYYAB_KuTVfgdjdH9JdwcIm_Z_GZBLrKAyJtAlfUxWy8Yt3k9LScyUXf0dHUJeHG2Ux4RxzAtMh7YfCGcBVzJUj4KSapRKQ3TWIerRF5BymPoeTSnuAFxTZluByNh0YFyXwkJosLYPiKi-43pO1jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم صاروخي عنيف يدك قاعدة موفق السلطي الأمريكية في الأردن</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/88834" target="_blank">📅 01:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88833">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/88833" target="_blank">📅 01:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88832">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/88832" target="_blank">📅 01:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88831">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GolihkzM5Gspu3supMGhYhipdKr9P9ZrwrK0DhyvqErmSPj2jOaV1zTdNxrqE3BpIAgqcZyIKdJYS06BB4beinibQu5QbBjxaXpbZID4AQADAXu6vWfdFuo1He7u9LP8jyeT5oXia540JzEK-rQao0iYf8llIy-BfF0wTTWE3e-Sr-8MT2JBlcw9fehdvozHysBtHbid-gsJcF4Y8ryW3ltZ1T3oVxKKbyb4mV3xNvE-vrgKqYB_P_Z_Vki2QjfQ_EesJ69sW-8EX6m_jBR9MvG6ntriIFUvxEJZGkRBdd3VwGsjB7hgiD20ODwFD5UHWgAufIgq38Bm2tH2V5lidA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الصواريخ الإيرانية تدك قاعدة موفق السلطي الأمريكية</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/88831" target="_blank">📅 01:20 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88830">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgtJPFpgVooTCaOVk48--gx9LeuKZwHOXe4V97QCtdPiGhfZuATGlmCS1Ndlcp-vYdTCFksX1vgyDtgsmm9EC3WB0qzgvzbDLkWq8bamMwzhrsf6H98Mzag9ZxfbDBASiLP18oUbvDaicNlFjBJ8FR3YQkaMYzYVzm7CnJqH-Nw6vVPHkbU3CtnMsIgtoiJxfhCC3eC49baaVSwXtCoP3OHf4hFGRe5NufBSF2tCo5BqUAHQp_DxdcHlcWYoPKaN3sS5TVRvM6MhDEvMRIF_8bf9N72KfdSGj9TbirgSanNOt5TNBpMCV5e4YJCxD15AUUB7RttXsBnq8BQtKGqupQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الدفاعات الاردنية تحاول جاهدة التصدي للهجوم الصاروخي الايراني</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/88830" target="_blank">📅 01:20 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88829">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ac97b51cd.mp4?token=YEZE8ek7NIvJxtYOqKjjD8kMo5nlAjfTWeMKILKfM4dNq7fx9dTFewMv9sJdo4-5lVQdH66Zx0TxmtdrpRkyPrE7bo0HnbxEBeF5JdO1iFqHrYJOZVXM6tkNlC2hEpdqaJHnk71vf7BV_ye9uT9VzyJPIPIl17RTO2Dt-1viLFZjPHd4ubfTSZ2SQ_hxuIl8V6teG0MFsebbxQruAMkxpfIpsHksmXDB3OC-QbmlGCxV40IcvUPV3f1RPLK0jvJGpPsdAdQc3zAWzGcr4xiKL2vvXE2v9xPgHQhtGHMOvkPhvqkq2dCFdEeDYMLvTRcKvgg3ylywbh4KwOvo8EG-iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ac97b51cd.mp4?token=YEZE8ek7NIvJxtYOqKjjD8kMo5nlAjfTWeMKILKfM4dNq7fx9dTFewMv9sJdo4-5lVQdH66Zx0TxmtdrpRkyPrE7bo0HnbxEBeF5JdO1iFqHrYJOZVXM6tkNlC2hEpdqaJHnk71vf7BV_ye9uT9VzyJPIPIl17RTO2Dt-1viLFZjPHd4ubfTSZ2SQ_hxuIl8V6teG0MFsebbxQruAMkxpfIpsHksmXDB3OC-QbmlGCxV40IcvUPV3f1RPLK0jvJGpPsdAdQc3zAWzGcr4xiKL2vvXE2v9xPgHQhtGHMOvkPhvqkq2dCFdEeDYMLvTRcKvgg3ylywbh4KwOvo8EG-iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في سماء قاعدة موفق السلطي</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/88829" target="_blank">📅 01:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88828">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1671a7ac6b.mp4?token=jCYAovK9NeurZTB41rr0W7oVhDQSQv2dZswOmcP4I1E85xTfPnxRH7y-Zsy2ZEJzDWh3mI1hz6DEJM641cmXTIA6stRticz570QVlxfDzwruF3oxxjuz-B-gFha_H7yScfrtCrquxqZWJgZBaYK8LRoOt0OW6vjidgYZq0p9yNIuWcOnDeWVI-FlTlK_IFm6Jx0rVSdnmYh8rWNO6wbi52mfQlDUPZCcVECNFonKG6Cwfa4ozc4NuLKQW-RLAsa9D7lb7jq2imEXOvGUbC6z2cP1e-ww-via-oO1iOHA-MEZvC51RbOiVOmJ8cR8JudwCUbWVj-RYIwunSemWwrUBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1671a7ac6b.mp4?token=jCYAovK9NeurZTB41rr0W7oVhDQSQv2dZswOmcP4I1E85xTfPnxRH7y-Zsy2ZEJzDWh3mI1hz6DEJM641cmXTIA6stRticz570QVlxfDzwruF3oxxjuz-B-gFha_H7yScfrtCrquxqZWJgZBaYK8LRoOt0OW6vjidgYZq0p9yNIuWcOnDeWVI-FlTlK_IFm6Jx0rVSdnmYh8rWNO6wbi52mfQlDUPZCcVECNFonKG6Cwfa4ozc4NuLKQW-RLAsa9D7lb7jq2imEXOvGUbC6z2cP1e-ww-via-oO1iOHA-MEZvC51RbOiVOmJ8cR8JudwCUbWVj-RYIwunSemWwrUBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صاروخ إيران يشق الطريق نحو قاعدة موفق السلطي الأمريكية في الأردن</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/88828" target="_blank">📅 01:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88827">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">القواعد الامريكية في سوريا تطلق صواريخ إعتراضية</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/88827" target="_blank">📅 01:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88826">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc01134378.mp4?token=MHuUsM2nUClKc7Nf3f8eiDRK0eO_fkRXKkW2f1kO_uojayelh7SAucWw33k_lnZvHnHe-_kTyT6uQMg0-b5faiUTNmNTVBHSeEDlRINI8qJ0q5LZ6jtrDY9CSZhKOY6_9GaQcoeyU1bPOdHAteZbRrQ9572L--y1LqOouu1T2dnA07aQ2d93dNbaFXgxGfP27YKQckEG46JkgdG-0JVTS1zIRsbLgHf0bsn3otEasqIoaQZ4hSuYsoKB-CxdcuhbnzfNBwM0ze4XvtcL33Zgvy8bscoehLYga5i3khPDGtV1U3UntnU6yDx0lCcuXPaU3IRloqoh7jft3SrUxv-20Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc01134378.mp4?token=MHuUsM2nUClKc7Nf3f8eiDRK0eO_fkRXKkW2f1kO_uojayelh7SAucWw33k_lnZvHnHe-_kTyT6uQMg0-b5faiUTNmNTVBHSeEDlRINI8qJ0q5LZ6jtrDY9CSZhKOY6_9GaQcoeyU1bPOdHAteZbRrQ9572L--y1LqOouu1T2dnA07aQ2d93dNbaFXgxGfP27YKQckEG46JkgdG-0JVTS1zIRsbLgHf0bsn3otEasqIoaQZ4hSuYsoKB-CxdcuhbnzfNBwM0ze4XvtcL33Zgvy8bscoehLYga5i3khPDGtV1U3UntnU6yDx0lCcuXPaU3IRloqoh7jft3SrUxv-20Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  انفجار عنيف داخل قاعدة موفق السلطي بالأردن</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/88826" target="_blank">📅 01:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88825">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">انباء عن انفجارات في الأردن</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/88825" target="_blank">📅 01:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88823">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mtn28KQk0AMo5gEGlCGmEc3b6fiA5zTlurhk1o8hKUmruin5QEWDTL5XMtUuPS0KeG2En-uXbHLqSiBYuKDi-GF3XWmFIQ3VcBuQWcXtJPn2uXabTNzhARfGifvhV49QLhM3o_3d6XCPb4zcE4MS3p2ZYxCUjkmgPEVFX0rEZZa2Ay7GAPLu5unYohVyDdi0LNSEQ4pSHO5xes4vtxCNkEpNt49xb32t7a6Vc_5SDzZc0CGfTMXwP3zLi_A07dldFM4stEmfGqG2UbosfN85b7b8dIldq16FO-9r6mE0AfJDgr2t4zZKfwx0yI9z4oPt_YMKlHQAqvuKAv88gAVUhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cHb6aeDkePbSMMfsxVA5LZJ-SLt6nZpI7DAkow04MMIQ-HqtRmTzdpzhgN8lOUrF9g0qwu1nyGjLfNNmUYkUrmuPm02IJBhZM9Z9NWDw_CtckjIzUV_Fl1TDDFWyK6eQ9V10PO7OwmGtOu0NeFEGWX2DSb_B0CqQKPRy-uG-PBzOXWBP3R9qY4JVnhZdA2sMyg3n18MW-LQSL92JfaXlvyRdgXic7MpDoWYEgje8m8-dE4N-vh_BvPxwQpY5zCG3QA3F48BKYqD2IaSVQoY3p2fE_zxPnuwGbenbyuvp7efbPio2f0a8vWW8bwCVEadELxfJWUBCPjKnvsWymgiw6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/88823" target="_blank">📅 01:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88822">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/88822" target="_blank">📅 01:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88821">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">انباء عن انفجارات في الأردن</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/88821" target="_blank">📅 01:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88820">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">رشقة صاروخية أخرى تنطلق الان من إيران</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/88820" target="_blank">📅 01:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88819">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/88819" target="_blank">📅 01:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88818">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇮🇷
مشاهد متداولة لإطلاق صواريخ من إيران نحو أهداف معادية.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/88818" target="_blank">📅 01:07 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88817">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇮🇷
المتحدث باسم منظمة الطيران المدني الإيراني:
حالة الطيران في البلاد طبيعية، وتستمر عمليات مطار مهرآباد الدولي في طهران دون انقطاع. الرحلات والأنشطة الجوية في البلاد تجري بشكل طبيعي.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/88817" target="_blank">📅 01:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88816">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/478cd89f5e.mp4?token=VgJIKu1lLJ1kop7V_0Civv8IqG1lD4whmONcfOrjeQBfMtJMnHyUHy7zuA7dOxjIh5Gg-5OuRX37TmqREna-wdn2-x0DAVHeHRPHXsSMfvPmt5w6cDdyfoGd3UdJR-RefQQAOn5RmqCtiCooqrd1IYLMvfnsnHVYVM_6Fbyzqx1JGwN_qbpD5GplsB_aYh03jYsltzSfuG-c0-AJ6TdM_oJtHPGiDxvsAteOxS21csNrotRT0h-VJDFhRwiTmwMDpNKmXHghrk0CB_nfnOr4wktBdAMvCLWVoKxWbJtOmCDnEiygjbdz81JRT6meqH5lJfGS-hVkCQfMNu82MrFLCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/478cd89f5e.mp4?token=VgJIKu1lLJ1kop7V_0Civv8IqG1lD4whmONcfOrjeQBfMtJMnHyUHy7zuA7dOxjIh5Gg-5OuRX37TmqREna-wdn2-x0DAVHeHRPHXsSMfvPmt5w6cDdyfoGd3UdJR-RefQQAOn5RmqCtiCooqrd1IYLMvfnsnHVYVM_6Fbyzqx1JGwN_qbpD5GplsB_aYh03jYsltzSfuG-c0-AJ6TdM_oJtHPGiDxvsAteOxS21csNrotRT0h-VJDFhRwiTmwMDpNKmXHghrk0CB_nfnOr4wktBdAMvCLWVoKxWbJtOmCDnEiygjbdz81JRT6meqH5lJfGS-hVkCQfMNu82MrFLCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
أنباء عن إطلاق صواريخ من إيران.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/88816" target="_blank">📅 00:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88815">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇮🇷
أنباء عن إطلاق صواريخ من إيران.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/88815" target="_blank">📅 00:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88814">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQFre0G_ZxQCh1MHLqqUJl25wkaOnYj0B_mWyREp-mIR3NoJtS2ocR9hVJCd3B1NkCteDf9bNYtZy7q3CAzlcPXDleoEdUQ9GzztI-qpOHKhSbZdFSzV1Rs5w6UWTVUwMMSGH2rZkDXJaL7Z9JsJprRg-6uZMcacltTkEhrEqyIsFCTZFAbu1h0w8Q3M-ywWWCq_-Up2kwpF176inkl_6rQhIhg5s0JCOA9goJOFgPUm2hwvF7qQyTEGOj8BHRgUYcA1RAHQxLjVvkzkfJGfES1Jt-7TP6_OI2Qpn5WKQx-mw3nnrBDz4IJhYXOCPGQvPgCnLhDnPdFmNqgXCz3UKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
إبراهيم عزيزي:
إن اختبار عزيمتنا مرة أخرى لن يؤدي إلا إلى زيادة تكلفة إخفاقاتكم المهينة.
بلا شك، لن تمر أي جريمة دون عقاب على أي مستوى؛ بل إن رد فعل أكثر تدميراً وإيلاماً وتعليماً سيكمل سلسلة إخفاقاتكم.
انتظروا بخوف وحذر.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/88814" target="_blank">📅 00:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88813">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">عدوان على جزيرة لارك الايرانية</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/88813" target="_blank">📅 00:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88812">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9nWhWO8kyvYLYx1YEW2D3eMuoDKSCh_gUuxCoA4OhMpXTE4Ngrio-d5pIXrSCOhgJHI-VxNPrnzdusD1awIZgmNypTOPLJ5qATxUMUB-WUMZEVy9Lew96-Q8iOHQb_KaPXyMgWPa1KQDaRnPnl_gBjQy9iPbunYRUChozKl8NqMAOIfLQiMpO16Nl3c2-2rMHoFXJ-AIfrbi5tyRqeJ44_MIMc2p1nNiqObsr9LSZQXUKMe9iPGEE-l0PRo-TR-fBKxV7NkZzYsqSfP3vLwYTbgGEjJi-zjRQQOJdQtBcrPS4nkv-JkUkfLeCAG4nLD9lhJB1LgguhB1UHL_YH8OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المتحدث بإسم الحرس الثوري: سيتم معاقبة العدو الإرهابي لعدوانه على جزيرة لارك.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/88812" target="_blank">📅 00:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88811">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">في خطاب انتخابي ومحاولة لإعادة انتخابه بالتزامن مع تراجع شعبيته.
🇮🇱
نتن ياهو: إيران تحاول استئناف برنامجها النووي، وطالما كنت في منصبي، سأمنعها من فعل ذلك مرة أخرى</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/88811" target="_blank">📅 00:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88810">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIfK4K9ToyuLUvpBdH7GA47y-jOQkzsbd_3dTWR4ML2XwBfFonKn_vAWFpdk_f3DBHfCwKKE42jkPcLxtakSaxhQ4GGmx2nkk_FAw0R3a4Jyau_I6-weL2Q6PW5Rlg2oK8JIoySG8Arv-yHz1AfMIZuL3y6wM3Ah_U4JKpQNCAOUB0hixzfrm66zr4BLDxPwGcZASWA34eNALBThfcxhyMywlkW2CuVhDLkGixEd-hqHjZKhBiMKWcLcP-fZbnyuO6LSvBZZiKNPUzi5qMYob42_DjZScKchofboxSdSW9Qg3JxBeCl9uHbaXfQ-j4epiY_zC31kfdwFecvUZZWZYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحرس الثوري:  العدو الأمريكي - الإسرائيلي، مرة أخرى، وبسبب يأسِه من حل المشكلات الداخلية وتقليل مصداقيته بين دول المنطقة، يسعى إلى إحياء دوره المشؤوم وتبرير الرأي العام، فقام بعمل عدواني بالهجوم على جزيرة لارك، مما أدى إلى استشهاد وإصابة عدد من المقاتلين…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/88810" target="_blank">📅 23:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88808">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔻
شهود عيان لنايا:
ابو يمعة وعبدالله بندورة يهرعون للملاجئ وملك البحرين يرتدي بدلته العسكرية.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/88808" target="_blank">📅 23:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88807">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lz4CTcUEnfonOnjkk0z6KWOL7lJt50B5rHOR_lo4eIlLqkU_Mmr6vdis_tXlFSvLNCOgzJOo2ulr1b7X2iseSD3mIfR4lTNuVqd5IU7WBuDxrcLF8q4A5FW9RerySc9mFC1exkzCcbhQaqQUJy__qffKyILiebVA5M41su6uO9XkKEoDYJ0GIUjYrE8vZeTttdEYH7Nvenenh-3pykjnFCSfHiAGTx5eU68NVW71g-SKqcUWQCbRDyRNhe_fs9pUKcd6j8Wwqjtus_T3UnKZYkRFecxk-yCZzXBWhpiJz56Vv-u7Y6tjQN83O7VrdmZydSm_xyIvR7j8EUR1nTZPZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عدوان على جزيرة لارك الايرانية</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/88807" target="_blank">📅 23:29 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88806">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇯🇴
🇺🇸
‏
اعلام العدو:
الطائرة الأمريكية التي ضربت جزيرة لارك قبل ساعات قليلة انطلقت من قاعدة في الأردن.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/88806" target="_blank">📅 23:28 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88805">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">مصدر إيراني: إرتقاء شهداء جراء العدوان الأمريكي على جزيرة لارك جنوبي إيران.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/88805" target="_blank">📅 23:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88804">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">عدوان على جزيرة لارك الايرانية</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/88804" target="_blank">📅 23:11 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88802">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e8G2bww4oV-ulXarGzs7J7KRxmquu9nRpbkq8GuFjMb2o_eWYPvjHuOTHmKvkYJU9cbWlEP5_hvuTZUOpQ_nxJEycJE7_mbONScuC_BvkjDnZrKfBIfdFuh5_QUopMmTRfaZLJZ8EcGR2rvy5yH7IKsNu1bT7Zamr3dEZXdZqB6naW4JRZnHfYWObGxcSabGayl8BvIbFCga0xCc4slTdEu-tApHQQby5M--gYKdWt2I5jtssijsa2VaPrUcIva48eVVZ3b98l3kahQO6PNML0SkvwZTySS5kT_GA4YsHF47XER9-ATXMGveN-8nxaoM2RQMtlZhUU2W-QD7N36hpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tLbjf2GaolfZfvyDDU--r3ewo_dXZWDp3VZUM3K0qq3BE0Hl9oZAl-4cgIdbmKQ9K_oyhvH3I2ghcmvyZ1wQlNkQmEJNLQjkgvNCiu5P-sQyKstmP48eOWSjBdKMX13NNKsbGotxL2oftn9Odt0-No4iFrhPcPtQSWbs73i09F09c3EqSNyvG8B-5GdSgZF4CsNxuytzksYn-66wvfn0eiTMbkXzIVBmgORSEICguf48YaC2nCdhePXYNjajzAwB1nf8im2GqDNHkk8yhi_svjKKJCAV9EzQpPbfcpWspFbDOZc8-DD0v99-rKYprVbXLOL_MGA90rBquCKfrqxOtw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
🔻
‏شوهدت ناقلة نفط تعرضت لهجوم إيراني أثناء عبورها مضيق هرمز أمس، اليوم وهي متوقفة في مكانها ‏قبالة سواحل عُمان جزيرة أم الغنام.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/88802" target="_blank">📅 22:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88801">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">عدوان على جزيرة لارك الايرانية</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/88801" target="_blank">📅 22:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88800">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">العدو الامريكي يتبنى الهجوم</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/88800" target="_blank">📅 22:47 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88799">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">عدوان على جزيرة لارك الايرانية</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/88799" target="_blank">📅 22:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88798">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">عدوان على جزيرة لارك الايرانية</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/88798" target="_blank">📅 22:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88797">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/370a134319.mp4?token=g3WlIFNTuC_2dVlPFXqdARSLezlm9QERwOtfsbmX2ykSbBiJWn6KN95N71EUJSx-Qb4mT1BahZhYP_mw77w90wB0aVEi76nB_vK90DKQ2RPZotH_jgGtAHVJONRnsm8vtjBXqIkLAD5rMLtBZINgZdDVzGcJ8N9a7Ntx76ScO7uL3VLIJvlhJrGcjNA0_u1AtULHqI5VQg2fR9I1t8CnWi_ishtZZQqSz6LLOxkEUK35LGx5wv8BHw_kE_4pGTnuCqSFNos4e6WtCmH23Lg6rgjkZo7BZ724TzZC6tqJzt_PEdkw5EIwmqUftfD767NMYkVwcUsKfuLK7jbAC4nibA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/370a134319.mp4?token=g3WlIFNTuC_2dVlPFXqdARSLezlm9QERwOtfsbmX2ykSbBiJWn6KN95N71EUJSx-Qb4mT1BahZhYP_mw77w90wB0aVEi76nB_vK90DKQ2RPZotH_jgGtAHVJONRnsm8vtjBXqIkLAD5rMLtBZINgZdDVzGcJ8N9a7Ntx76ScO7uL3VLIJvlhJrGcjNA0_u1AtULHqI5VQg2fR9I1t8CnWi_ishtZZQqSz6LLOxkEUK35LGx5wv8BHw_kE_4pGTnuCqSFNos4e6WtCmH23Lg6rgjkZo7BZ724TzZC6tqJzt_PEdkw5EIwmqUftfD767NMYkVwcUsKfuLK7jbAC4nibA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتن ياهو: في إيران يقولون إن "بيبي" مجنون، أو أنه شخص غير عقلاني - وسيكتشفون قريبًا من هو المجنون، أو الشخص غير العقلاني الحقيقي.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/88797" target="_blank">📅 22:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88796">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">نتن ياهو: منعناهم مرة واحدة - سنمنعهم مرة أخرى.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/88796" target="_blank">📅 22:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88795">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نتن ياهو: الإيرانيون لم يتخلوا عن البرنامج النووي - نحن على يقين من أنهم يريدون استئناف برنامجهم النووي بهدف امتلاك سلاح نووي. التهديد لم يزول.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/88795" target="_blank">📅 22:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88794">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نتن ياهو: لابد من اتخاذ إجراء حيال إيران. يجب إزالة التهديد الإيراني وإسقاط النظام.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/88794" target="_blank">📅 22:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88793">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نتن ياهو:
لابد من اتخاذ إجراء حيال إيران. يجب إزالة التهديد الإيراني وإسقاط النظام.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/88793" target="_blank">📅 22:26 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88792">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇷
تقرير بحري غربي:‏
يستخدم الحرس الثوري الإيراني زوارق صغيرة لتحديد السفن العابرة لمضيق هرمز.
‏خلال عبور مضيق هرمز مؤخراً، استخدم زورق إيراني صغير كشافاً ضوئياً لتحديد هوية سفينة أخرى من خلال قراءة اسمها من هيكلها أثناء إبحارها عبر الممر العماني. وعلى إثر ذلك، نادت القوات الإيرانية السفينة باسمها، وأعلنت أنها "مُسجلة في نظامها" وتخضع للمراقبة، وأمرتها بإلغاء العبور وإلا ستواجه إجراءات قانونية.
‏إيران تعرف بالضبط من هي السفن التي تعبر عبر الممر العماني ومتى</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/88792" target="_blank">📅 22:16 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88791">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmVSccwr5-uzOat-c_WbNAUzFcXsbqP6fnUhKh3Ijc_J7PET9CsBgpzNwv3FryfgV86wtTfylyGL2Rsx85A7ffJ5lYKmGKBzI2j7ryjDGTojEge2ATJ70Xiw5VU4WcOgWBpV1PPRQxvvya8oJ2lq9qAeoV-wEqmiQ6xWPk4ZrNbOXkXdQsezjjoP3IO6m13V7ZkdMPjMf-ntq2dCSSRyMaZ6jELenKJaMESRXRVjcfm-732Tr28lK9IdYULi3mNjJCzhmmJRvQSuN0ZZQOoI0BrznT4BiDVf4EpYsMC13v_CTMY3QM3Iv2kFl__B7MV-hC1ncS2q1-z_TwMBQLoY7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏
ترامب:
على جميع الشركات الكندية التي تتعامل تجارياً مع أمريكا أن تنتقل إلى الولايات المتحدة الأمريكية فوراً. ‏كثير منها شركات غادرت البلاد منذ سنوات بسبب القيادة الأمريكية الغبية. ‏عند عودتك، لن تكون هناك رسوم جمركية!</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/88791" target="_blank">📅 22:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88790">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🌟
🇺🇸
ترامب:
‏
عندما أعلنت ترشحي للانتخابات الرئاسية لعام 2024، في بدايتها، كانت شركة فورد تستعد لإغلاق مصنعها الضخم في ديترويت. ولأنني كنت متقدمًا في استطلاعات الرأي، قرروا إبقاءه مفتوحًا لفترة أطول قليلًا لمعرفة ما سيحدث. والآن، يعمل المصنع على مدار الساعة، وهو من أكثر مصانع السيارات ربحية في العالم! وهناك أمثلة أخرى كثيرة، سواء لشركة فورد أو جنرال موتورز أو غيرها. لقد أنعشت، بل وأنقذت، صناعة السيارات في أمريكا. ويعود الفضل في ذلك إلى ما فعلته بالتعريفات الجمركية. تُعد كندا من أسوأ الدول التي تستغل هذه التعريفات. لا أريد سيارات كندية، ولا قطع غيار كندية، ولا أي شيء كندي. لقد استغلونا لعقود، وسيتوقف هذا. كان ينبغي أن يحدث هذا منذ زمن مع رؤساء آخرين، تمامًا كما كان ينبغي إيقاف إيران منذ زمن. إنهم يريدون أن يُعاملوا كدولة، لكنهم ليسوا كذلك. أتعامل مع قيادات العديد من الدول، لكنني أجد كندا هي الأسوأ. لم يعد لهم الحق في ذلك!</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/88790" target="_blank">📅 21:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88789">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇧🇭
سفينة تابعة لنظام ال خليفة الارهابي في البحرين تتعرض لحدث بحري.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/88789" target="_blank">📅 21:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88788">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/88788" target="_blank">📅 21:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88787">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/88787" target="_blank">📅 21:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88786">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇮🇱
هيئة البث الإسرائيلية:
سفن حربية تركية اقتربت من سفن للبحرية الإسرائيلية وحددت لها مسارات بحرية.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/88786" target="_blank">📅 21:17 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88785">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a957ad2ca.mp4?token=rXkTGEGViVbEjTE9qfA0HWntD2QyfLapWxUQZ-RCcZCwO-hCXKmVvHSFreEpRR0Rgv4O03-_CyOtxQBBv7lYuf9u1ZSM09YqtfoYKKVgaLd0H9OMd43pOyesuw3ICcGHGaAKsDZ_SOipb1gGfSrtifoqYr0TgXUbPTnRYauzQaQUsBiA7_VfO7660M7tYxoFoPTFL2v9Q0dAAVW3sZCp22VuktLD2Tg0uKIpSMTwKM8Gui7TKFg9s_ZyrD-rwqdAREcVCKONM4aymEclmDFNmQym3ChiiCcsj_i2DV0CI-M8kH4fN83ePuaioPXhUZ9Q_FuawMES_uA2HXAB2AjtxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a957ad2ca.mp4?token=rXkTGEGViVbEjTE9qfA0HWntD2QyfLapWxUQZ-RCcZCwO-hCXKmVvHSFreEpRR0Rgv4O03-_CyOtxQBBv7lYuf9u1ZSM09YqtfoYKKVgaLd0H9OMd43pOyesuw3ICcGHGaAKsDZ_SOipb1gGfSrtifoqYr0TgXUbPTnRYauzQaQUsBiA7_VfO7660M7tYxoFoPTFL2v9Q0dAAVW3sZCp22VuktLD2Tg0uKIpSMTwKM8Gui7TKFg9s_ZyrD-rwqdAREcVCKONM4aymEclmDFNmQym3ChiiCcsj_i2DV0CI-M8kH4fN83ePuaioPXhUZ9Q_FuawMES_uA2HXAB2AjtxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
السيناتور الاميركي تيد كروز:
ما أدعو إليه هو أن يقوم الرئيس ترامب وإدارته بتزويد المتظاهرين بالأسلحة، حتى يتمكن شعب إيران من ذلك، وتزويد الأكراد بالأسلحة، والسماح للمتظاهرين بإسقاط هذا النظام من السلطة، وليس وجود قوات أمريكية على الأرض، بل شعب إيران.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/88785" target="_blank">📅 20:22 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88784">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇳🇪
جنود متمردون في قاعدة نيامي يطلقون النار على مواقع حساسة في عاصمة النيجر والقوات المسلحة تقول انها استعادت السيطرة على اجزاء من العاصمة.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/88784" target="_blank">📅 20:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88783">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇮🇱
🇮🇷
وزير الطاقة الإسرائيلي:
إذا ارتكبت إيران خطأً بمحاولة إحياء برنامجها النووي أو برنامجها للصواريخ الباليستية، حتى لو كان هناك اتفاق مع الولايات المتحدة، فسوف نكون هناك لنردعها.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/88783" target="_blank">📅 20:11 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88782">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLsh5WMLnvHfgnf4d8wrwS-Q2ikSn7o58L9symB6txDykM6yekO2SAL6wjzgMO7DVGEVKyPJFeryrDex_QG7sI2iqQ6griJRrA_1MmDSNJj1qTHuORaz6BmRR5B9iH37tUwBkXTj-MN3E8kOwnnuEMqAOuvAuyqLDdtqStmbeIc1tFfizuIhB4Pi0uWSC1DKvC4oIcFK19u4V9CK3L5zF8O9QWDYt1K_gSjbVadYuOR3lbjFf3d_cUukjhfZiDCmFrfIHc9GGFgvSIYiojOvUKJIm90_4EV7x7dY8o-2XQuWdWlh7FRSjxDYrqnI_eXs8GfLkJPFSko27hldhIS3Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
ناقلـة نفط تتعرض لصاروخ من الحرس الثوري أثناء محاولة منها لعبور مضيق هرمز، على بُعد 12 ميلًا بحريًا شمال خصب في سلطنة عُمان.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/88782" target="_blank">📅 19:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88781">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇺🇦
انفجارات في كييف.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/88781" target="_blank">📅 19:38 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88780">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc0c37ed88.mp4?token=B4WhNh1KqcFF4sZ_ST-yPUuwz9BXCajLgHppzGAca1RYCCf0GC0xr5b6m8wZKRIX4irKLN-LnA2fNPMWe4Eck3SKhDbHFAWFhY2mhsFrMwxOc1DMTZsSIckwqpTccuOC4S6cDSEA0ea6HPoZOwVOvnvlOoS3vmrnnRGFa60h606iVw88lA9nnJJk9DNVqxnwQ7mWDQ28GdnBrbh1aLgUpDNgdI0YwmcbntmKMN19VndjHtj2xu_GFdxoWVzKeLk7OAg03d-f-F9fwAVObQzBFL2f_TWph586guwXgMUB1-pYjKKnXylqDyjQ0uZytMNzCnnDQxsxrVtKpVNIx1D6ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc0c37ed88.mp4?token=B4WhNh1KqcFF4sZ_ST-yPUuwz9BXCajLgHppzGAca1RYCCf0GC0xr5b6m8wZKRIX4irKLN-LnA2fNPMWe4Eck3SKhDbHFAWFhY2mhsFrMwxOc1DMTZsSIckwqpTccuOC4S6cDSEA0ea6HPoZOwVOvnvlOoS3vmrnnRGFa60h606iVw88lA9nnJJk9DNVqxnwQ7mWDQ28GdnBrbh1aLgUpDNgdI0YwmcbntmKMN19VndjHtj2xu_GFdxoWVzKeLk7OAg03d-f-F9fwAVObQzBFL2f_TWph586guwXgMUB1-pYjKKnXylqDyjQ0uZytMNzCnnDQxsxrVtKpVNIx1D6ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▫️
في حادثة غريبة في المجر،
أقدم لص على سرقة طائرة مدنية خاصة والتحليق بها في محاولة للفرار ما دفع القوات العسكرية إلى استنفار طائرة حربية لملاحقته قبل أن يهبط بالطائرة اضطرارياً في حقل لزهور عباد الشمس.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/88780" target="_blank">📅 17:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88778">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/slIBM3X93RHzy3N2afZS0RJqgiomjO6gFjg9-uy95jGRuK8gfdeAom2De2D3wK6WCFNslmNsUgZYuz8Q8F-INBMfhTA_Oda7xhfGhoDUt_VmSCn_qFQhYnPfjaUgf5z5QvuEbNPwsUioOdoLvzUOxb5An6tUu7LDBylYiygTfqbIeII-qk_lL2MJPe7WKsfChfahcQOcoqBz8X4ODaYC1G8lZKN52to3YcWzn4Fy_RAFYJnR9M6WqD1XXPUFoUM_pXpQihDMxjkGtmKPMcD3OleKdlVb_DBT4a-MonkP6MFkcP_R4QLUWbZDtwUWRowDWVmVE4SUUqrITSOqR80Qxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FTvKvQA0ozFQAy2FFUFcUWITwrNUmctDhdJ01TKyx1qiH7FfYsiyp6OZflP2Wg3BfzrrQBZaeifZDdfWAJXrbn-8GcaYn7xAGIQ7RHF87ZKNYH8YBgyjbVQdww3fOLEE6haTxCVeDQ2RgXyWmShLVFrkxAAt4K_iW7u1PkZFCcINnw0--8al2Zu8JbYCfNEQ_LR-EPCzs0tXz-Bhu4WVVyeuec-zTi_Nbg8p46A5huJdjOpUIQsjHY5WxhO3557UqdJN3ETqG_ycQVa9PqAdOZUCnvp7KzABTnyGYkxr6W0B_5iScBvjef3A1f49ulMngoM3ePqD_SqsHKbgOdIvUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇸
رسالة سابقة من الشهيد القائد/ حذيفة الكحلوت إلى إخوانه مجاهدي الإعلام العسكري
.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/88778" target="_blank">📅 17:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88776">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kanIBQS5tsqcyFN_d5eW58HOdmu7DYAqVtdK8p7CPviXTwlwfxk-5WT2F3g9r7Ubzt3bxejawsc27GBwal6MO1dPS_BBNSlif713I8VkNais8jz8iKoEpQ-KeDcgxUomNBqWOkeMOVoxyJ_tgNss_GF_1lJ-PG5bYyhQbqwxZrHKyFjTIu8yFpdFIw4bBtjgDq6_chAoh-5TMu5UC9IkFWwOBo5S1vlNp2YXfgtlvCkb_bv88gd4wbQzvbngoy9jX1ns5VVt0ojFh2tFnpZcW2ewPMrBIsDrbjBG4Cz_SuPmA5K0hKd5wlHuFO5XPwhsbo9F4BtxeNBBCYzZ5tfp_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lliuAe9mxNVY2VEFqjz87qbS7u0VwhtqwijAxl_V594lIkTjvnomvNvd-zrOldgsjCx3ApG_eIHNSWplqLVgQk6yJ54Vn2FE0HNrwsT3D_OZiiAVsFMAoOVPeEQpTmIeTczQmQCDKavzr3_mBGndhoEAAd16LVZ4aN5ZepVMCTaarfZd3PQoiEvE6Z_GomnRTPTOyOFrVDKU1tSfPlS3sWD1f8Bomckwrepl2rzoENiyvMCIqvbV0_D-0iAhI5o0O-rVshhTZ2-eyvXYDSm6EL3NX0cUsjtMZIc75LuzyMNoFnP0O0AjSLg1HdRjOsmCXdMW6SPlhWqU65_oRkvKCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صور جديدة للرئيس الشرعي لفنزويلا المختطف نيكولاس مادورو أثناء تواجده في أحد السجون بالولايات المتحدة.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/88776" target="_blank">📅 17:19 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88775">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇮🇶
اشتباكات مسلحة في محافظة أربيل شمالي العراق،
أسفرت عن سقوط عدد من القتلى والمصابين.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/88775" target="_blank">📅 17:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88774">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇾🇪
مشاهد نوعية من استهداف القوات المسلحة اليمنية لتجمعات وآليات تابعة للعدو السعودي بطائرات رجوم المسيرة في عدد من الجبهات</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/88774" target="_blank">📅 16:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88764">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P3qtqHgN8Ad02VTFvZ8PNFMV5sZQvv_q93myD5UpHf_VIbQGqEyUFEI2X1MLflB0LYJ-BrIBKC9gveiWfrFi_3xPfq5HQcm6U-nTetmzCwnq1XncO_7fmXTaBY2F9rskRPsaiCr3OFht7M7GyBFqKjWzEcT94GT50lhSsaA7G3GuMXO7mV-itjYvdNPA472xmluqOJjpQaWHFxOJzwGX7rzytKgvSpjeVcN1wawvrl-h-wAsQG-oCpxu5TFkXQkDvqbIhzUkSL5DsXdrTHwDhGEvyLB6cqbauM7agE-zsitkyRwGAaHGBy0XHjRxYQcRchfaHULCOWhGJmGnYCwZlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WKmcBsAAR4CsKY9fNLw0l5TkggKvPNkHyg0fGpMVSHqBX61zMia6Ju1mSNdDCNeTY-rPxgZ4i9QEbG5g_zm3RJpDGI_FEL-zIYPl4sZhU2LsG_irR0d4A5ueCwSzdfZml7m5905bztPldM5-hSuC3PgK3kiib-l_VNIkceC8jP_z4PsVYbpeIjNt4DiLKmsg89gSm4VeL5hPzrT_hThwf5bs1N9OnS3sdv_cPys4vlFujs5mnITwyWmTT9lH63J-FKv2B0yuBYTkrGj1KvGWOeEhOq6TNoFsrfQ_mku1wmrlstJNjpxY7wiB_I0rr4y-jUA_C8lblGsYGE1vN7afVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/njn9PCHYzDYXjtaPWWKX5GDukb7fFHt8noYtVuKbbrmk4iNpfMVSW4bZgZaac1VoY95YQ2eM7bclIpXqfwMNk40NWbHy5UesnNJ8Sul0omx4QDSzFAuV4Zwaxc__aRsopBZgJXBYhjFe6puvTxMz93JQiVC4lo22xIdFyXCzZIUcHjTMjlm0gXRnPla3f8qpEolP3OjFqqyKA5wSFZeWE6zjsPv6z9M_vjDB7axk2KhPF6xXLkOSwNPHoBx1LPwiOlpmupWOlogetqeWI--7rjuhzsIf75poI_ZM-Vb75oR4Panh5Et6rcfcifPEUdwcZEHPRim27wSJeEA7MG-WoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vGFSS7XFThHyTMrva9OdcFvnvHRJP11ccmLUe4ZtIyPqKXlUjgUivfAGjrMSlM_gFLV2PZLTUTryly1t9CGxhbQGTekduPqXXoP1I5vAZNVt94kmEdx_vuBZvWqwk5Do2CsSImA09wtKc3hGVyqh1O4Nbbgvftu4Xaco6jNvoYJnTuX3wTDh_YjAj12te0W8KeAhVL-ux0KcdentHpJQTarRVWkQU_cnyCNZviOK4cP3XecbMhqvUZxfVyH2qRxg3JYkm7jsZxApVK7YjA38n_6m6LnJoaWgtyF0k85x6CB4Jr4KAm7X0Atricc73abMK-ud2hlEKkftAl7mN_3Mhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vVS2gMRlHK3O2JCzY-FO8Pka_XLyo6Oz3hPEML-F989gCZewS89sCKuXge4b6v6uARANjutcoU6QD9s6lLan8OdbqoE49_GlBLmdngbrwGHWTiX-1bYQ_oRiIKDMklU7mOvoy1lSrrLRLQs-5ExQavkG7ETZ-nYAFA8aSqdsypEwXbbCbRgfAWqMVlUH2PZQc-Wj1_cr4xK2oC-Oj_joJPSwjaALe5IoaniEc7wGMuDrV1k_jZWhAFdz1Di2tX-95MBERB9Oq34f9ycDijLEeNntLSEkkGl7Q9O2BNsspb9ygmOIAHWfNS6L4s3b5v20bqibxpUohGgGcRqbQPoe3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UyiXb0SL5dkGUSwvfAm3UdyD63sOJSVUUI7AjhTcD0sZ1nGLwCdi1ytGm0kusseRDG-ZiV-1qxscZFU87TkVs6HPOtmxeNVcooMlT4_8ePgitvarLGFwKFRD5H5LkvznPzGRn5xbPa4pNoihHFGvt5U1pRDrgrDlIg8pJKKlC83llnfY7YckFsUBDXvJfaV5iV4Lkp7QtgA-VV6Roz7W1cX93HMBz98TMGFp7ypassmTg6u55P1Of4PxmohPnT9mvNE_LgUSLIdOho3m57qCV5Piq6uQPMd7cdx6DZCWuS7lStguiNBNCceZX1dIpeStBBMBP1bPdwraSdKtBnH7Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vqR_vt4xahw3marOOu-ScwW8iFqE5ZJTPAGFC0Tjq1PwrXI9XpZiBsVOKmTDof-5huugLfM5WEuhdaPGC428nIJN7DRq6UKujmzCC1AyQHCvNembsLiqjLUJtxsK_7HlGTUnSDfZPR2OZuVWTt5kaIBS3fwgNz3h2-SiOrO7o1ydhPthyHphljX4kq5dz93SZLIaIjiUgMvXfiw__ct574DvLlm7NQgoWozOGT8NgSX7SHZrFm0OVFloS5csrCzrrL3mtyU_nZcoHI4Qrb6yx9giZSkccXMwVfNRSWhGX_ojzryKIJn1jZNBUS83VVxCHt5cC3Mo6VkgbovQmFoAZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WDeHq4zxf6POyGII1I5dwoHvimEgxGUj4ZaQh21HFnp626KxljOFXOcSMpaM_Xq58BziluOy8DXC98KYvEhzuexBn0mGN-2qTMB3rljUYJEVx_71Dq-PAWiM4v51GWOKEqr2Z2igXHka1RCAqy03UVgtXHn3OZNYDtexxsyA-x2Rd_h127Q8SfnMpjeStBX_p9Zk6VM6_G614ldT_eAaVMdAmMCKXvjui4tXfoDmn7vnDNirRNqhx-WKiKSt9Q8fY1iPyU_93b9d2Rf6egiF3ylwk0x2LgWYlz4C1IvNJYc0OdQIBa1_md9YN-48Bf76D32coL1tbpe1hm2r1_C38Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F8e9LHWUE0qfD2Ku4O5wIi3jEIRe3yRl8NEqV4v2M_gQfhVT4zP_gy-IQ8TkqlM7r35cfGBucojq27xEMm8pLNo5AlzWHOiTxRP3SaG8UYMkyIrEHBtAi4NBsC35z6L0PksDtYktCy4M_UmAL4EuqyDJSnJ9_H3bVXXDQgRshOS8HuaWWPGfuFeFox5J6g3m9ArUp_pntzFu5Rg1RT052QTN4lit6ODHsgM_yQ9HntVORwCKNGtO7lQ0BGUlCSMzKe71er1JZc_6ss7Ud4FuAq8gnON45Tt54jiHzTRcgOjY5YaAPCa7zPIomhF1fQLSEmha5TTweUaHuTcvOtB3HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ujD6dyBo2IVtYq8wDm_6VAMDf9L_CruxfBCPKrpS7XE1ur7MPD867pqKno7nazDSPNif_P31nhRZ2nDd7L3YW3TTPhghHtdzEcfXB0881E_lTGr57ViHshOPzFbQioXs0K6hRcW7cNhxaiKmXmCmeM1U_J6a8xGVyeVnww7MopC5aSrM-NzXqcKIgmPX2cEaQCdBtmsxKKnbSkARK5MFEO7EOOf-JSQEqxSBit_0ZtvoFmV2GSY0348hw8ZJodqG_IV1ekoKJkT266OVrSU9gvmUaGLrPBCi3yEvDUnZyjx8iZxNoVULF6YRmoVKjCF86mxhoVkM0amJXFyQ2naMjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇾🇪
صور من استهداف القوات
المسلحة اليمنية لتجمعات وآليات تابعة للعدو السعودي بطائرات رجوم المسيرة في عدد من الجبهات</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/88764" target="_blank">📅 16:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88763">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hjCukDZzWnc6hHwLQiibBYEd_kbyo_H3svjEWWzqthsiZXo4vDreWtK_Gcj34ODWPine_TSPwVyYr42wzQk-oMjxXBd-dABJYVgKWK2F5ZcV3hWjXLwt87m-wfeCmQ0am7dsOCWyQVJREYG-J3vtwVsVz-hNS3vn49vqnIoogrumY6jjmGZ5qARJXZd8lZ-iOmhv1fYmaoVYtFVu9GMwkwsnZb8II_Uk4CgPrK3e4dz5jw9Un4l5HM4up7dqksHHApwHXcL-Wkwg2pDp85GQhGUcir2ZLoU7Q1vuFmLvDwQKIJsOTJG4_g35lDnEGQpjAAMJkTc6HSbf8q8q9d4-Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب منزعج من الاستطلاعات التي يخسر فيها:
الاستطلاعات المزيفة التي تستخدمها وسائل الإعلام المتحيزة لدينا خارجة عن السيطرة، ويجب اتخاذ إجراء بشأنها.
هيئة الاتصالات الفيدرالية ستقوم بحل المشكلة!</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/88763" target="_blank">📅 16:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88762">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇺🇸
🇮🇷
تحذر قيادات عسكرية أمريكية وزير الدفاع بيت هيغسيث من أن تمديد الحرب في إيران قد يضع قوات الولايات المتحدة في جميع أنحاء العالم تحت ضغط كبير.
يقول القادة إن أشهر النشر المتواصل قد أدى إلى استنزاف السفن والصواريخ والطائرات بدون طيار وأنظمة الدفاع الجوي، بينما أضعف الاستعداد في أوروبا وآسيا والدفاع عن الوطن.
أعربت البحرية عن اعتراضها الأقوى، قائلة إن العمليات الحالية غير مستدامة وأن حوالي ربع مدمراتها فقط جاهزة للنشر.
وافق قادة الجيش والقوات الجوية على التمديد، لكنهم حذروا من مخاطر كبيرة.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/88762" target="_blank">📅 16:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88761">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SiOvF4rhDAXuhnRa4wt2msHB241qW_XudB06qp3oaW8jSgz94RjPI_BdCM69ZI4IUeXyD_x1bko2HD15c2ySeGPEpsod06IQNGV9wsYilh599P20CWfr1iE0S6K0Q2_MZ1feYzp98m6qCy79LsWMXFUqI0zYuh5xElwXx6M_QM0ORQlDYp8pmBieAObu-TvnmLRfnKGofBw_VpHujfgPZb0aA-vvJmUXfZbXLzSt8828DADOyGZA_BL9hT9NoUtWBjTnx9ZsYupkxJME4bMKU3fxfux6GtlusYoAJUjqQgKjT7EuAKSrsy29f-QDmyvcyEiKl-CktB53NGu0AyY__Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب ينشر رسميا تم تغير اسم بحرية أونتاريو الى بحرية اميركا.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/88761" target="_blank">📅 15:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88760">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇶
هيئة النزاهة العراقية:
- السجن سبع سنوات بحق وكيل وزارة النفط لشؤون التوزيع عن جريمة تضخم الأموال والكسب غير المشروع
- قرابة (26.5) مليار دينار قيمة الكسب غير المشروع والتضخُّم في أموال المُدان
- إلزام المُدان بتسديد مبلغ(53) مليار دينار يمثل قيمة الكسب غير المشروع والغرامة التي تعادلها</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/88760" target="_blank">📅 14:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88759">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇶
هيئة النزاهة العراقية:
- السجن سبع سنوات بحقّ النائب السابق طلال الزوبعي عن جريمة تضخُّم الأموال والكسب غير المشروع
- قرابة (35) مليار دينار قيمة الكسب غير المشروع والتضخُّم في أموال المُدان
- الحكم ألزم المُدان بتسديد قرابة (70) مليار دينار ردّاً لقيمة الكسب غير المشروع وغرامةً تعادلها</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/88759" target="_blank">📅 14:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88758">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ان الأمريكان قد توغلو في كل شيء
عراقي
حتى لا يستغرب بأن يتم وضع والي العراق والشام توم باراك ضمن المناهج الدراسية القادمة ..</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/88758" target="_blank">📅 13:16 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88757">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">نايا - NAYA
pinned «
ۗ وَسَيَعْلَمُ الَّذِينَ ظَلَمُوا أَيَّ مُنْقَلَبٍ يَنْقَلِبُونَ﴾.
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/88757" target="_blank">📅 13:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88756">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ۗ وَسَيَعْلَمُ الَّذِينَ ظَلَمُوا أَيَّ مُنْقَلَبٍ يَنْقَلِبُونَ﴾.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/88756" target="_blank">📅 13:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88755">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61e9cd2db8.mp4?token=qPwZVg5dunrE6zMrxVyX3Gdbh1xN4DC1pVC5bpThnNAzN3IQm3TiBQaXSzYmziL2xl_2Y6dwcmDpzzd7TulgCmk5Il8wZVz_x3Z04C42-bJdwq_P3huYPrgEhRuLgSQjaR47zU225OPwB-ctlcqyYLK8y5yyttrEEkvJfhb31XfPhcnGXYpNm82UalHVaEBPHXm65KAwf1LWCcP2WHTQ1RQqbU8kcHKM-dM36eMehZGZ5xUr11xQQt72HuG7Q1glQLkGJptGhlI4p6DBril7dTPSJtEecPxOWs5TZ-wq25MDblC4nD3qhpa26LHS0-NCDId2pOl0wrPOB2jBHrIR6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61e9cd2db8.mp4?token=qPwZVg5dunrE6zMrxVyX3Gdbh1xN4DC1pVC5bpThnNAzN3IQm3TiBQaXSzYmziL2xl_2Y6dwcmDpzzd7TulgCmk5Il8wZVz_x3Z04C42-bJdwq_P3huYPrgEhRuLgSQjaR47zU225OPwB-ctlcqyYLK8y5yyttrEEkvJfhb31XfPhcnGXYpNm82UalHVaEBPHXm65KAwf1LWCcP2WHTQ1RQqbU8kcHKM-dM36eMehZGZ5xUr11xQQt72HuG7Q1glQLkGJptGhlI4p6DBril7dTPSJtEecPxOWs5TZ-wq25MDblC4nD3qhpa26LHS0-NCDId2pOl0wrPOB2jBHrIR6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مصدر لنايا:
هبوط طائرتين امريكية في محطة الشاحنات بمطار اربيل الدولي شمالي العراق.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/88755" target="_blank">📅 13:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88754">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqagR6wgIbaRgBeqjcrujDeenkLN-gpaEjqOb6_nmDCAiOzZzL_4H5hU_LFoFa20yqyBSYgYKn3BAvNvyv-cGW3wKZjk9bIaxm3nkSj8fp4xVVpXuHWAT79qp0ByQPzozxjXNbNzJuvQ6MHOOmiXxNKIE24JwjD5yVSjeAmg7aLfftxeB59bJ1licBhZ8HA2XeEEL-yMMNMPWAAhYgo8DdyGcQ1R9HL4FZEMVtzpQVX8OXntxvfXsVSHy-7wfZRCp57_h7yx6BKwAvKeObn7VNVa2Aovc-aYpQnGb5RuuWvwDDMV9sTnQsa-brsG6eMkBMGQ9YDFppf94nKs0Glx0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#
ترفيهي
🇺🇸
السلطات الأمريكية ترحل المعلق السياسي البريطاني المتطرف ميلو يانوبولو أحد أهم مؤيدي السياسة الامريكية ضد المهاجرين لمخالفته قوانين الإقامة.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/88754" target="_blank">📅 12:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88753">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇱
إعلام العدو:
مراهقان يبلغان من العمر 14 و 16 عامًا من مدينة كريات موتسكين متهمان بالتجسس لصالح إيران مقابل الحصول على أموال.
ومن بين الأنشطة التي قاما بها، تنفيذ مهام تصوير، ورسم كتابات على الجدران، والعمل على تجنيد قاصرين آخرين لتنفيذ مهام لصالح هذا العميل.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/88753" target="_blank">📅 12:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88752">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔻
إعلام العدو:
رفضت الولايات المتحدة طلبًا من ولي العهد السعودي الأمير محمد بن سلمان بأن تتولى واشنطن قيادة حملة عسكرية ضد الحوثيين في اليمن.
أفاد مسؤولون أمريكيون أن واشنطن ستدعم عملية سعودية، لكنها لن تقودها، ويرجع ذلك جزئيًا إلى أن القوات اليمنية تستهدف حاليًا سفنًا مرتبطة بالسعودية بدلاً من السفن الأمريكية في البحر الأحمر.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/88752" target="_blank">📅 12:06 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88751">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adae5dd28e.mp4?token=SN6VNgI-_GUsfpJDDmZvytvinndH2SSdPrEkswHlRObq2hOJbvxq-h_q8uc4aNh5dPqPJBVYfJZkynaQgt242Y1_zdkHWjgdSuXguOkIuK1ogoMrvvyvKIMZojxwYx9L4NhGIylLd3OvnSS3us8TQtX2dHeG6tRgrW4M7LPcchr2AmCCTi0cOo_OyNsJsBkPFV0taeBZHwyiYWFkJOLyXLbEfiTfxTbtwRuwl-n1GjX29nw2sochgv-CUFWSyiaPEq3gmOWU03XQ_fi2F85wCW2zsx3CSghDCssAue8NYUqGqqGYmOnTp3T3yffu9Yyq1YpuXLecAIgSB6TORdiEVjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adae5dd28e.mp4?token=SN6VNgI-_GUsfpJDDmZvytvinndH2SSdPrEkswHlRObq2hOJbvxq-h_q8uc4aNh5dPqPJBVYfJZkynaQgt242Y1_zdkHWjgdSuXguOkIuK1ogoMrvvyvKIMZojxwYx9L4NhGIylLd3OvnSS3us8TQtX2dHeG6tRgrW4M7LPcchr2AmCCTi0cOo_OyNsJsBkPFV0taeBZHwyiYWFkJOLyXLbEfiTfxTbtwRuwl-n1GjX29nw2sochgv-CUFWSyiaPEq3gmOWU03XQ_fi2F85wCW2zsx3CSghDCssAue8NYUqGqqGYmOnTp3T3yffu9Yyq1YpuXLecAIgSB6TORdiEVjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
القوات اليمينة:
ترقبوا الساعة الرابعة عصرا، مشاهد نوعية جديدة لاستهداف القوات المسلحة اليمنية لتجمعات وآليات تابعة للعدو السعودي بطائرة رجوم المسيرة.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/88751" target="_blank">📅 12:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88750">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0f21690e4.mp4?token=NgJFmDwfBi_gw1g4MeMoCUe7r24YNGYOHRMptHcqluf9z7p2wy9-VBjQ2pzXmSuXZNSP3V8pkP6SUfnqj_rrBpclFfoD9A8KvOE6uZrr4eEb3O_44Dr-S_RWWtOPwlpWDVBzztdRLUe0zq28_vWdbo1qdYnoZik--H58dAhqXIYx6Xr8MbZde4aMNjihCqMCavsOp5nz6J53NrVnkYsiQ0AlhEN-Wu_dFfCqog4Vj2YcsL3fmUocRI6gRqf5Se1xvB8PyN1UCwi1pwtKsYgQ6m8uVhyN-4-FUjY_AXl2yzZvF_ERX6fpt4_JvXiNiDRFbRaNH3ZXlAtCNVJPVQpmTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0f21690e4.mp4?token=NgJFmDwfBi_gw1g4MeMoCUe7r24YNGYOHRMptHcqluf9z7p2wy9-VBjQ2pzXmSuXZNSP3V8pkP6SUfnqj_rrBpclFfoD9A8KvOE6uZrr4eEb3O_44Dr-S_RWWtOPwlpWDVBzztdRLUe0zq28_vWdbo1qdYnoZik--H58dAhqXIYx6Xr8MbZde4aMNjihCqMCavsOp5nz6J53NrVnkYsiQ0AlhEN-Wu_dFfCqog4Vj2YcsL3fmUocRI6gRqf5Se1xvB8PyN1UCwi1pwtKsYgQ6m8uVhyN-4-FUjY_AXl2yzZvF_ERX6fpt4_JvXiNiDRFbRaNH3ZXlAtCNVJPVQpmTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
🇱🇧
طيران مروحي إسرائيلي يحلق في أجواء منطقة مجرى نهر الليطاني - زوطر وينفذ عملية تمشيط.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/88750" target="_blank">📅 11:58 · 08 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/eXeeqTiPK8IBdrWK16jb5Y2xtAYsgPudittf2XxBqOX6b9BjRhDmvtojjSBXBwPs_YWgWV9ZXs5OddtetVwPJSEqwpUUFgHv4tvb5Xq92WaxX_sv0OzsotJnMMa4zYNp4kIhCH4ii4PtZ8LVw3o4gziF7NwjLt-8WAcDdSgtYqNJ32YT309CI1vvUpxgu17S5xdGdLnWrLP-r7EzOhQq8kWlK6aYWK5pbgwHQ3ncaN72OWvqlg8iD2O-wsDRH43pvX6zZgbLHcNyFOb1db3_PyuuZbJ9p06-hqyf1rOByVThc7tEl85eqM1gEq-OxmiHiuJca_i_epw9frRGEhWA9Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 251K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-07 21:27:45</div>
<hr>

<div class="tg-post" id="msg-76313">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇺🇸
مصادر أمريكية: نؤكد توصل الولايات المتحدة وإيران إلى مذكرة تفاهم بشأن مضيق هرمز والمفاوضات النووية.</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/naya_foriraq/76313" target="_blank">📅 20:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76312">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
25-05-2026
آليتين تابعتين لجيش العدو الإسرائيلي عند موقع رأس الناقورة البحري على الحدود اللبنانية الجنوبية بمحلّقتي أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/naya_foriraq/76312" target="_blank">📅 20:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76311">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
تظاهر نحو 30 رئيس بلدية إسرائيلي أمام مبنى الأمم المتحدة احتجاجًا على القرار المشين بإدراج "إسرائيل" على القائمة السوداء بتهمة العنف الجنسي إلى جانب حركة حماس. وأوضح وفد من مركز بيريز الأكاديمي أن "هذا قرار معادٍ للسامية، ومنفصل عن الواقع، وغير أخلاقي.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/naya_foriraq/76311" target="_blank">📅 20:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76310">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: بعد تقييم الوضع، تبقى سياسة الدفاع لقيادة الجبهة الداخلية دون تغيير، وستظل سارية المفعول حتى الساعة الثامنة مساءً من يوم الأحد الموافق 31 مايو 2026.</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/naya_foriraq/76310" target="_blank">📅 20:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76309">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🏴‍☠️
‏إذاعة جيش العدو: شكوك بشأن نجاح عملية اغتيال علي الحسيني قائد وحدة الصواريخ في حزب الله</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/naya_foriraq/76309" target="_blank">📅 20:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76308">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
بعد تقييم الوضع، تبقى سياسة الدفاع لقيادة الجبهة الداخلية دون تغيير، وستظل سارية المفعول حتى الساعة الثامنة مساءً من يوم الأحد الموافق 31 مايو 2026.</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/naya_foriraq/76308" target="_blank">📅 20:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76307">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇷
الرئيس الإيراني مسعود بزشكيان:
نحن لا نسعى لامتلاك أسلحة نووية، ولا نمارس الدبلوماسية بالإذلال؛ إن الاضطرابات في المنطقة سببها
إسرائيل
.</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/naya_foriraq/76307" target="_blank">📅 20:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76306">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed657d94fe.mp4?token=vZAhQ0p320DXs7Z-ukCTrDcWkeUOqOqPcdBYHkDb0e-9m_5y84P1so03pug9--y4sIfBdxmitV9n7Ywja2nLe_TxBebiAJO4bmDsauhq8QT8iFachd12rEAjK-cB4HoCckq3NJxlElrIMlHJtb5VyAg5g919GUcMxpwxZdHCxSelYTAWztXmN8Tnb_CkxFA8ERXPlrBc4hQ2ZljtAVNoCvjwIR5lgnTVy_OkcL6xHt32PGEfP3POavXMklJDCxgV1uvAghXIG-vHB0XSmYuZbRW5dmEO5d-BxFM1yJE7wframa24H8Np91Uqb6_0tRdBYp2HZEp8chyV_Dd_RwGZ7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed657d94fe.mp4?token=vZAhQ0p320DXs7Z-ukCTrDcWkeUOqOqPcdBYHkDb0e-9m_5y84P1so03pug9--y4sIfBdxmitV9n7Ywja2nLe_TxBebiAJO4bmDsauhq8QT8iFachd12rEAjK-cB4HoCckq3NJxlElrIMlHJtb5VyAg5g919GUcMxpwxZdHCxSelYTAWztXmN8Tnb_CkxFA8ERXPlrBc4hQ2ZljtAVNoCvjwIR5lgnTVy_OkcL6xHt32PGEfP3POavXMklJDCxgV1uvAghXIG-vHB0XSmYuZbRW5dmEO5d-BxFM1yJE7wframa24H8Np91Uqb6_0tRdBYp2HZEp8chyV_Dd_RwGZ7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
إعلام العدو:
انقطاع التيار الكهربائي في المطلة بعد إطلاق صواريخ من قبل حزب الله.</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/naya_foriraq/76306" target="_blank">📅 20:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76305">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇮🇷
نائب وزير الخارجية الإيراني: لن نوقع على أي تفاهم لا ينسجم مع مصالحنا وسنرد على أي انتهاك لوقف إطلاق النار.</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/naya_foriraq/76305" target="_blank">📅 19:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76304">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">⭐️
‏أكسيوس عن مسؤولين: اتفقت الولايات المتحدة وإيران على تمديد وقف إطلاق النار لمدة 60 يومًا وإطار المحادثات النووية، لكن ترامب يؤجل التوقيع شخصيًا. لقد طلب من الوسطاء بضعة أيام للتفكير في الأمر قبل اتخاذ قرار نهائي.</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/naya_foriraq/76304" target="_blank">📅 19:52 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76303">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
25-05-2026
خيمة تموضع لجنود جيش العدو الإسرائيلي في موقع حدب البستان على الحدود اللبنانية الجنوبية بمحلّقة أبابيل انقضاضيّة.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/76303" target="_blank">📅 19:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76302">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c83ccef82c.mp4?token=Hgm_MdYwSY_IWA0oQ4aNh1qem9Ehw2EEad_zEUXS7PTmpd0qOeYp3VnEyacFpGyhwBigy6xEgta8zcg61b5mCu1zXtr0N2sa-wncf0TNjAJ9IoKkTeEDeI06tSEasIiFOAGM3SDyqI88Rm_2C3NU5DjzVx3bTt_h2lO8Bl1z2eJ917MUH5m3w9yxUVpFvTdAXY5g34maIjwrtgzh972Ks4NJ2_Hpm5GUIFRzxPNpFbsFq3xwd31qELCsUcS6diMUjIEGXp07Qt2OAzUdn_2gWqrfFb6tRHX6b0152rvIVemIs2Xds6BLorJMwbVhrbTeEAz44ijBVIg6oRL76i50xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c83ccef82c.mp4?token=Hgm_MdYwSY_IWA0oQ4aNh1qem9Ehw2EEad_zEUXS7PTmpd0qOeYp3VnEyacFpGyhwBigy6xEgta8zcg61b5mCu1zXtr0N2sa-wncf0TNjAJ9IoKkTeEDeI06tSEasIiFOAGM3SDyqI88Rm_2C3NU5DjzVx3bTt_h2lO8Bl1z2eJ917MUH5m3w9yxUVpFvTdAXY5g34maIjwrtgzh972Ks4NJ2_Hpm5GUIFRzxPNpFbsFq3xwd31qELCsUcS6diMUjIEGXp07Qt2OAzUdn_2gWqrfFb6tRHX6b0152rvIVemIs2Xds6BLorJMwbVhrbTeEAz44ijBVIg6oRL76i50xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
متظاهر حريدي في محاولة إنتحار رفضاً للإنضمام إلى الخدمة العسكرية ومن تحت عجلة يهتف "نموت ولن ننضم للخدمة".
😭</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/naya_foriraq/76302" target="_blank">📅 19:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76301">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9421e16253.mp4?token=iBvfmaD_cHTHjOOkf_9s4giwdS9fM-TMFBT3VATHIGRGSvMxArmbEY5eVaF7sjvjybndrZMMd72U2Iik-ZWzZ4KuihvMIf84_fzko0htfwdWB8JeTI4T--vJcgwOYoNFv1Yhjg5VsC-TrjpGAVedm3-KNBWmqYUTaRSPY6S57xQCaPHFBiL6CVUfYIc-kdCBVywB7HBHKwnUXCGE4OoSFO_1gRPs6hDK5yonw8RStWvJjKz3KGNivIy3uNDwI_2x14poELbkVyEEqjWU6vRtYZH9G7dyukf0csBAY8o2OTfZSsQvXGtY4ktXskXGHr01jKAEGZg2V88Xd0wVKMxXZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9421e16253.mp4?token=iBvfmaD_cHTHjOOkf_9s4giwdS9fM-TMFBT3VATHIGRGSvMxArmbEY5eVaF7sjvjybndrZMMd72U2Iik-ZWzZ4KuihvMIf84_fzko0htfwdWB8JeTI4T--vJcgwOYoNFv1Yhjg5VsC-TrjpGAVedm3-KNBWmqYUTaRSPY6S57xQCaPHFBiL6CVUfYIc-kdCBVywB7HBHKwnUXCGE4OoSFO_1gRPs6hDK5yonw8RStWvJjKz3KGNivIy3uNDwI_2x14poELbkVyEEqjWU6vRtYZH9G7dyukf0csBAY8o2OTfZSsQvXGtY4ktXskXGHr01jKAEGZg2V88Xd0wVKMxXZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▫️
🇮🇶
🇮🇶
اهتمام روسي إعلامي كبير بزيارة الحاج فالح الفياض رئيس هيئة الحشد الشعبي و السيد قاسم الاعرجي للعاصمة موسكو ..</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/naya_foriraq/76301" target="_blank">📅 19:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76300">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47e2cac299.mp4?token=Cb2OThkGiGTRYDLMqQf1lSQ456T33JIzB0vMrNjABicJM6-Tq8fU-VHmfvCTVIzxLQ_JDG7dEfJyD0MQUBYa614PqGV8wP5B1JYT3aPDIaXad_Zq-7GeSFVJzsSDOSnQwKVQz1hW4Fs2eI4Gc2ZyUTHKXQLXjT7ShF0hNEIj5Z1dWxaJdY_emjzzxjZr7aFLb9swLaR0enArGlCzanuMR6CmKDo993sxFNCoP2L8BRiJ4E-tqdKS8RIpx49-YjHHT6iXoXk8KxX3yQ7ovCpdddvx7da-m37NgIevakJle0B5mUEu2PyxnaXjKohxWIEFHD0f5-F21LnHp1VP_5lP9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47e2cac299.mp4?token=Cb2OThkGiGTRYDLMqQf1lSQ456T33JIzB0vMrNjABicJM6-Tq8fU-VHmfvCTVIzxLQ_JDG7dEfJyD0MQUBYa614PqGV8wP5B1JYT3aPDIaXad_Zq-7GeSFVJzsSDOSnQwKVQz1hW4Fs2eI4Gc2ZyUTHKXQLXjT7ShF0hNEIj5Z1dWxaJdY_emjzzxjZr7aFLb9swLaR0enArGlCzanuMR6CmKDo993sxFNCoP2L8BRiJ4E-tqdKS8RIpx49-YjHHT6iXoXk8KxX3yQ7ovCpdddvx7da-m37NgIevakJle0B5mUEu2PyxnaXjKohxWIEFHD0f5-F21LnHp1VP_5lP9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
البيت الأبيض ينشر فيديو مع عبارة "هل أنت تستمع؟".</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/76300" target="_blank">📅 18:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76299">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">⭐️
إعلام العدو:
التقديرات هي أن المعركة القادمة مع إيران ستبدأ بمفاجأة تامة دون أي إنذار مسبق.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/76299" target="_blank">📅 18:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76298">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🌟
حزب الله ينشر:
لِتَعلَم كلّ أمٍ عِبريّة...
תדע כל אם עברייה...</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/76298" target="_blank">📅 18:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76297">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇺🇸
وزارة الخزانة الأمريكية تهدد سلطنة عُمان:
‏لن تتسامح حكومة الولايات المتحدة مع أي محاولة لفرض رسوم عبور في مضيق هرمز. وعلى سلطنة عُمان، على وجه الخصوص، أن تعلم أن وزارة الخزانة الأمريكية ستستهدف بقوة أي جهة متورطة - بشكل مباشر أو غير مباشر - في تسهيل فرض رسوم العبور، وسيتم معاقبة أي شريك متواطئ. يجب على جميع الدول رفض أي محاولات من جانب إيران لعرقلة حرية التجارة رفضًا قاطعًا.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/76297" target="_blank">📅 18:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76296">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a977370897.mp4?token=oNr6uChliYwpoddlIVaRKuCBJgmNqVKw2Tox33NRF8Jmcpz4Pt6X1FsayekgZ1MeIRhNrd_L24pId4qfsU88rpzik4_OQh3jecIVOObomuXYlOkiuUt1z1RaL1ZSWwWhoMRHSkg8a91yeb3_2Sa28go5wW_RyWM6MhDMAGbuza_UkIgOPxnPEGlJrAejN81js8i87NdV-lN4vep5xoQZAY14h-r3BkakFa7sxX-QXa0Nph5h5VJTKach-TY889YqpCUJHKdsGRirGRpOz9Ol46leBTIfxajWeXeR3fcfdCo9JYbrw69nW85tSqZXHx-J2O35HYZKE2BUFKkkp6e_EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a977370897.mp4?token=oNr6uChliYwpoddlIVaRKuCBJgmNqVKw2Tox33NRF8Jmcpz4Pt6X1FsayekgZ1MeIRhNrd_L24pId4qfsU88rpzik4_OQh3jecIVOObomuXYlOkiuUt1z1RaL1ZSWwWhoMRHSkg8a91yeb3_2Sa28go5wW_RyWM6MhDMAGbuza_UkIgOPxnPEGlJrAejN81js8i87NdV-lN4vep5xoQZAY14h-r3BkakFa7sxX-QXa0Nph5h5VJTKach-TY889YqpCUJHKdsGRirGRpOz9Ol46leBTIfxajWeXeR3fcfdCo9JYbrw69nW85tSqZXHx-J2O35HYZKE2BUFKkkp6e_EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
إطلاق صواريخ إعتراضية شمال فلسطين المحتلة دون تفعيل صافرات الإنذار.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/76296" target="_blank">📅 18:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76295">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">⭐️
‏
أكسيوس عن مسؤولين:
اتفقت الولايات المتحدة وإيران على تمديد وقف إطلاق النار لمدة 60 يومًا وإطار المحادثات النووية، لكن ترامب يؤجل التوقيع شخصيًا. لقد طلب من الوسطاء بضعة أيام للتفكير في الأمر قبل اتخاذ قرار نهائي.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/76295" target="_blank">📅 17:47 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76294">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🏴‍☠️
🇺🇳
‏الكيان الصهيوني يعلن تعليق علاقاته مع الأمين العام للأمم المتحدة.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/76294" target="_blank">📅 17:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76293">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🏴‍☠️
نتن ياهو يوجه الجيش الاسرائيلي برفع نسبة السيطرة في قطاع غزة من 60% الى 70%</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/76293" target="_blank">📅 17:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76292">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🏴‍☠️
نتن ياهو يوجه
الجيش الاسرائيلي
برفع نسبة السيطرة في قطاع غزة من 60% الى 70%</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/76292" target="_blank">📅 17:21 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76291">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇶
أنصار الله الأوفياء الفصيل العراقي ؛ يعلن عن استهداف قيادي بالحركة على الأيادي الصهيو أمريكية في محافظة ميسان جنوبي العراق .</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/76291" target="_blank">📅 17:18 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76290">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">تنظيم داعش الارهابي يتبنى الانفجار الذي طال جهاز مكافحة الارهاب العراقي</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/76290" target="_blank">📅 17:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76289">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇷
‏
التلفزيون الايراني:
بينما انتهكت أمريكا وقف إطلاق النار مرارًا وتكرارًا بمهاجمة الأراضي الايرانية خلال المفاوضات وفترة وقف إطلاق النار، يسعى جيش هذا البلد إلى إيجاد ذريعة لبدء حرب من خلال بناء رواية زائفة! سيكون رد إيران من خارج المنطقة. المفاوضات ما هي إلا خداع أمريكي جديد</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/76289" target="_blank">📅 16:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76288">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🤺
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 19-05-2026
آلية هندسيّة تابعة لجيش العدو الإسرائيلي في مدينة الخيام جنوبيّ لبنان بمحلّقة أبابيل انقضاضيّة.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/76288" target="_blank">📅 16:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76287">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hN25WyLr_Y7O7yv-ijMMLgKoRNGVjeEVm5YIpcBie6Nnq0wapi-36RrOV2H7qrOSxZxvVOqGU32QofGa544jxqSQBfH-sp5VXBWWmN3QNXzDwf3IGaFAI2LjdBn-CvlrfNUKFbjHAaY4vLNYvjXFlTrg-tjeszbjHPjZd4nWjvhWj2raY-RvLPxrlgfnl-JQYubvTl2y6lr0uauVrJSAQ26kdh5z6JVX5CEffVJSKa87arYbuVrrCfFbLRb2qCRWR-35fBGKcfKI3-hnQirsd0ifAe7U4YRZdvoqnpy0tg1Rpz3AxqQG2nyorZ20KTKZ1dAlRRwoH25hDAxfKWJnSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
وزير الخزانة الأمريكي:
سنمنع الطائرات الإيرانية من الهبوط في المطارات والتزود بالوقود وبيع التذاكر.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/76287" target="_blank">📅 16:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76286">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">وسائل اعلام تزعم:
إسلام أباد ستعرض يوم غد على واشنطن نقل اليورانيوم الإيراني إلى بكين تحت رقابة دولية.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/76286" target="_blank">📅 16:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76285">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r08TeGoHRJV4wyPkwXihoJoDz1SKYnheW_778sVO5mwOi54AOArjds1bYWh84ic2mFsCaU-t06QWfY-dKqFFx8ie0assIqS-xRXZQ-AwJGd2E4KCuzNwbQSVt6QmyzVzw4Qcs0qPPeogAzaN_HI4OsrTNTFseoAiRFbLLmDE190f_QrjfWbMV4ZuXYSFP4pKjnw9Ti9TGatHu1bBkURBspP-O43BQy6FmjrwBNk4fW-_20nOVCMeKFYXpADF81vrIkh9R15k2hp4-5jEkPS0xmmuHmIwO8SvB21LPbxn82VDaEANt-utMeJsZx8hMxOMXV4U_jVBZWbawOkXCGfr0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قيادي في حزب تقدم يدعو لمقاطعة منتوجات المدعو بـ(ابو جنة) بسبب حلفه بـ"الامام علي"!</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/76285" target="_blank">📅 15:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76284">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26db9455a5.mp4?token=QDwXPBGMcXstlDknxPTX-gEMeWqnL_zfLDuQhEHWoOmYwHmjyf_kuTO4HiGj-pKpGo6WXPl6WHed93uu68V7ICdW0N9Q1w7_6zzdMk3U9XM30OVoJWleMVrDTbTDFX7tfS-YwtgOzGz-U0mp3KZWrutzJn9D8QgzsOjjgVRAM1DFBuHThxjkZNF2cVBI1riG0_tYkrXN-mySwHLCxPz88I9Elq3blnCYVhIZm3NKBM1Ds162D5CvxlI9ZfVCM_IfJWRjhKskbVOWr2-l8k1zeUz42YffAxyfjEmvLrnOzuonPhMTBEs8807JuF8kechg4NHsi94qf_Dl0jmq4XkRwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26db9455a5.mp4?token=QDwXPBGMcXstlDknxPTX-gEMeWqnL_zfLDuQhEHWoOmYwHmjyf_kuTO4HiGj-pKpGo6WXPl6WHed93uu68V7ICdW0N9Q1w7_6zzdMk3U9XM30OVoJWleMVrDTbTDFX7tfS-YwtgOzGz-U0mp3KZWrutzJn9D8QgzsOjjgVRAM1DFBuHThxjkZNF2cVBI1riG0_tYkrXN-mySwHLCxPz88I9Elq3blnCYVhIZm3NKBM1Ds162D5CvxlI9ZfVCM_IfJWRjhKskbVOWr2-l8k1zeUz42YffAxyfjEmvLrnOzuonPhMTBEs8807JuF8kechg4NHsi94qf_Dl0jmq4XkRwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
‏إذاعة جيش العدو: شكوك بشأن نجاح عملية اغتيال علي الحسيني قائد وحدة الصواريخ في حزب الله</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/76284" target="_blank">📅 14:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76283">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">إعلام العدو يدعي : اغتيال علي الحسيني مسؤول الصواريخ في فرقة الإمام الحسين</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/76283" target="_blank">📅 14:46 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76282">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/704b0794ee.mp4?token=Vmg43E27RxutNB22bTzU6EmNfXQmTAKrTgLXJ-9zL4Df_-YO3B2ZYzUXEva-aqWj-n_PXeam5JYaDXkuY9dDahLn4ktUF6PbCcX207_qCq1UmRnsdJpZfP6mAu57H29UIfSm6OAf7x6jxfVlGekfECZ3HZRjaVxs1I2LKQNkytYQTKfaaaxXrAKjzlupeRHke8QxIruEaWooPxfruldT2ws1kM-OVDmJ-u7u9tbIA0ERbrWnaJVIQ1EHyHXPQK5U1avDo-BZhWCa_liljaC0anEgZg-tWJF9qxPf6ob74znzIIBqMWAw_xkcVyoq0WTTVtV2j-LMy5_7pwb-vYAX9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/704b0794ee.mp4?token=Vmg43E27RxutNB22bTzU6EmNfXQmTAKrTgLXJ-9zL4Df_-YO3B2ZYzUXEva-aqWj-n_PXeam5JYaDXkuY9dDahLn4ktUF6PbCcX207_qCq1UmRnsdJpZfP6mAu57H29UIfSm6OAf7x6jxfVlGekfECZ3HZRjaVxs1I2LKQNkytYQTKfaaaxXrAKjzlupeRHke8QxIruEaWooPxfruldT2ws1kM-OVDmJ-u7u9tbIA0ERbrWnaJVIQ1EHyHXPQK5U1avDo-BZhWCa_liljaC0anEgZg-tWJF9qxPf6ob74znzIIBqMWAw_xkcVyoq0WTTVtV2j-LMy5_7pwb-vYAX9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
أنصار الله الأوفياء الفصيل العراقي ؛ يعلن عن استهداف قيادي بالحركة على الأيادي الصهيو أمريكية في محافظة ميسان جنوبي العراق .</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/76282" target="_blank">📅 14:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76281">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ضربة جوية قرب مطار بيروت</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/76281" target="_blank">📅 14:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76280">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/406121fc42.mp4?token=CLXE3HGdclHgXYB_Wb0oydFTwTeiSDMPU5TVClu9aIi9dbF5n--U0MPZQVG9haaVLFn7M50X783Cmk9bsg7IXMT7WHWk4fmnTYeQjoly93_hK2KDggx1wHBfc8qo-zdkf1rbuZi-GGHHyqH3jJ6qXRi4Mhf5ER0HUrsZDql6yTii500qRiO4-ghpJiXO0s0dlSF4DhAz5QlQ2WhmSjRyqqf7frU_R_Vp9OeHxEHMgtnrh-UE84zySKmQTPi1pCUJ_4a9QKh6DoJoXTKPovFYNkOUT1MGlS9FNi_apypvhBPgFYi0JFoS_qz1rOiXhbfH8uPccIqVkNg0twjoi7MepA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/406121fc42.mp4?token=CLXE3HGdclHgXYB_Wb0oydFTwTeiSDMPU5TVClu9aIi9dbF5n--U0MPZQVG9haaVLFn7M50X783Cmk9bsg7IXMT7WHWk4fmnTYeQjoly93_hK2KDggx1wHBfc8qo-zdkf1rbuZi-GGHHyqH3jJ6qXRi4Mhf5ER0HUrsZDql6yTii500qRiO4-ghpJiXO0s0dlSF4DhAz5QlQ2WhmSjRyqqf7frU_R_Vp9OeHxEHMgtnrh-UE84zySKmQTPi1pCUJ_4a9QKh6DoJoXTKPovFYNkOUT1MGlS9FNi_apypvhBPgFYi0JFoS_qz1rOiXhbfH8uPccIqVkNg0twjoi7MepA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضربة جوية قرب مطار بيروت</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/76280" target="_blank">📅 14:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76279">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ضربة جوية قرب مطار بيروت</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/76279" target="_blank">📅 14:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76277">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇺🇸
جيش العدو الامريكي:
في الساعة 10:17 مساء بالتوقيت الشرقي يوم 27 مايو، أطلقت إيران صاروخا باليستيا باتجاه الكويت حدث هذا الانتهاك الصارخ لوقف إطلاق النار من قبل النظام الإيراني بعد ساعات من إطلاق القوات الإيرانية خمس طائرات بدون طيار هجومية أحادية الاتجاه تشكل تهديدا واضحا في مضيق هرمز وبالقرب منه</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/76277" target="_blank">📅 14:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76276">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رهبر انقلاب اسلامی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پیام_حضرت_آیت‌الله_سیّدمجتبیٰ_خامنه‌ای_رهبر_معظّم_انقلاب_اسلامی.pdf</div>
  <div class="tg-doc-extra">131.9 KB</div>
</div>
<a href="https://t.me/naya_foriraq/76276" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📖
متن کامل پیام حضرت آیت‌الله سیدمجتبی خامنه‌ای رهبر انقلاب اسلامی به‌مناسبت سالروز افتتاح اولین دوره مجلس شورای اسلامی و آغاز سومین سال فعالیت مجلس دوازدهم | ۷ خرداد ۱۴۰۵
🔗
https://farsi.khamenei.ir/news-content?id=62984
📲
@rahbar_enghelab_ir</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/76276" target="_blank">📅 14:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76275">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">#ترفيهي
الأمين العام لمجلس التعاون الخليجي: ندين بأشد العبارات استمرار الهجمات الإيرانية الغادرة على دولة الكويت
جا وتهديدات ترامب لعمان؟
😄</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/76275" target="_blank">📅 13:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76274">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇺🇳
الأمم المتحدة:
معلومات تشير لأن غارات إسرائيلية بما فيها على صور والنبطية أدت لمقتل مدنيين بينهم نساء وأطفال.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/76274" target="_blank">📅 13:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76273">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af565a9037.mp4?token=vuVZcH6Hoqw9mRsRIVC7GkL_9tddiXLPyVCPmeVkYmVnZ_QZiEFzsd7lf34Is1vjWB8bm-h6tCfRnmpikVO5DXxAb2ZcqahBPNeS-GB_4VhbJm6NtGDosjo6WI6WdwpQwq38bPD_UQVENH1PsX3AkIQV-jAutes7S9CmjYWKNCGQBE_766nbtb64gdgA4WnJMf0USku4mIbcgVDp6rzuydiFISSJ-bEN6AcMP8B9VdhpAWWWcBjXe13q7CosVYB4qEjxqje4iW-OzmChqjMPIBvy3APgPX-jqFLD2ZwoMDs-2ZHh9lN3fZJqxCYJk3_hQip9NANlMuTKR-ITen2Bbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af565a9037.mp4?token=vuVZcH6Hoqw9mRsRIVC7GkL_9tddiXLPyVCPmeVkYmVnZ_QZiEFzsd7lf34Is1vjWB8bm-h6tCfRnmpikVO5DXxAb2ZcqahBPNeS-GB_4VhbJm6NtGDosjo6WI6WdwpQwq38bPD_UQVENH1PsX3AkIQV-jAutes7S9CmjYWKNCGQBE_766nbtb64gdgA4WnJMf0USku4mIbcgVDp6rzuydiFISSJ-bEN6AcMP8B9VdhpAWWWcBjXe13q7CosVYB4qEjxqje4iW-OzmChqjMPIBvy3APgPX-jqFLD2ZwoMDs-2ZHh9lN3fZJqxCYJk3_hQip9NANlMuTKR-ITen2Bbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇭
‏
الشرطة السويسرية:
3 جرحى جراء هجوم بسكين في محطة قطارات بمدينة فينترتور.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76273" target="_blank">📅 13:47 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76272">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇮🇷
كلمة لقائد الثورة بعد قليل.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/76272" target="_blank">📅 13:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76271">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">📰
‏
رويترز:
تقارير للبنتاغون كشفت عن استهداف قوات أميركية عبر بيانات تحديد المواقع</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/76271" target="_blank">📅 13:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76270">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">📰
اكسيوس:
إدارة ترامب تعقد تدريبات عسكرية لاستعدادات محتملة في حالة حدوث فوضى في كوبا</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/76270" target="_blank">📅 13:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76269">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58cd922a9d.mp4?token=eSsd-svDZGD7EA2evDOdZIH7SUqKq7SzA3vEWenJ5aJOwB_nMTM3YGl3o3kG-0bBbh-aRZ4xTYUMobhM7bXp_CONE5_Hfj7FDz9Zr2ylvO5er952xqXyW3xf-WXavS9Eu1imnJwqTAIUkyPXdOtJpULK2lraF5ypPB8FHO1A0sKulnuiv7WpihLbtfdjWgI32tdGUvvoSOKRjHPB_VlmdpL8GWWYMea0c4K8c8dEYlHPikh9qARG1Q0_q0eoQcBH2TgQR7WnWFTNRl2v-jyAkHwXueqe_J1YJ3TSjBcDakXnaIgsRzwSytaTd-IprOKmb12YuCSlS9Gbjv-_xuLgyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58cd922a9d.mp4?token=eSsd-svDZGD7EA2evDOdZIH7SUqKq7SzA3vEWenJ5aJOwB_nMTM3YGl3o3kG-0bBbh-aRZ4xTYUMobhM7bXp_CONE5_Hfj7FDz9Zr2ylvO5er952xqXyW3xf-WXavS9Eu1imnJwqTAIUkyPXdOtJpULK2lraF5ypPB8FHO1A0sKulnuiv7WpihLbtfdjWgI32tdGUvvoSOKRjHPB_VlmdpL8GWWYMea0c4K8c8dEYlHPikh9qARG1Q0_q0eoQcBH2TgQR7WnWFTNRl2v-jyAkHwXueqe_J1YJ3TSjBcDakXnaIgsRzwSytaTd-IprOKmb12YuCSlS9Gbjv-_xuLgyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
🇸🇾
توغل اسرائيلي قرب تل الجلع بريف القنيطرة جنوب سوريا.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/76269" target="_blank">📅 12:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76268">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🏴‍☠️
دبابة ميركافا صهيونية تحترق بصواريخ حزب الله جنوب لبنان</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/76268" target="_blank">📅 12:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76267">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0HSHG-uvsuXF0FFE1FiFJ0a6mEgekSzJNEWZfQCyb-QHaPH8pCGKDj3DVqi5Xud4jKtePAhF_CC8YD_tgV9fcP0gLzNxHlvlPMRaX9IrDeNSpq5TA7ZVgrzu6_YfHXiWXGJXKWG3J05_99I9S5r80Ns-pWcFU-qD3L5angLJUpmwzlRTYpNztKQufPn00U12CTbabWRzk42o_1mJ51Cie3xOJn5ryW2H9rXGClRU0bC4CIPMzKsM5e12ETlCNFwzZ5lKivAFngVnNjEtd2K8hARZdNVCf71R3Y1LxPmyMHmi3-ksCnS1P9ORecDVLA862fLbmTZqa6bp4x3sfav1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
قناة العالم الفضائية تنعى مراسلها السوري "حسام زيدان"  شهيداً في غارة اسرائيلية على صيدا جنوب لبنان.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/76267" target="_blank">📅 12:18 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76266">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2pi2fjclkHm-LsXtz0J_J-aI6MJR03FKshLWNh_zU-Iyvt2rnYSqu0dvUJ9p0yKt_t-Rwot_kgLk7PYQ06UOwMBzGnOhSD70zddsXQBMXoEROTX1Xc-t8NFDCaeabjGBeCuLlgxBd5RUss_3O6Ux-RDTkD1sdSs6qr33k7T6j6Izd0RDdCuxJ3s5UOZsaxT5E3jMSYWsmhLaiRbAYuTO2-q9mHZJnnI-4SNauWO8kSW8qJWDlZRf6yrWldmkCup2QoERCXQYY0yWOO_7IlTNjbiS5rEg4RSNzAsDyX4qJnMDjDuDahuCyopr4-spWvOgQl7S2addRQMB4kR_QIZBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
السيد مقتدى الصدر يعلن انفكاك سرايا السلام عن التيار الشيعي الوطني والحاقها التحاقا تاما بالدولة.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/76266" target="_blank">📅 12:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76265">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‏حدث أمني بحري في البحر الأسود</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/76265" target="_blank">📅 11:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76264">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‏حدث أمني بحري في البحر الأسود</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/76264" target="_blank">📅 11:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76263">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🏴‍☠️
جيش الاحتلال: تحطم طائرة خفيفة الوزن في "عيمك يزرعيل" (مرج ابن عامر) نتيجة خلل أثناء الهبوط</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/76263" target="_blank">📅 11:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76262">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‏الخارجية الإيرانية: ندين الهجوم الأميركي على مناطق في بندر عباس فجر اليوم
أمريكا تواصل انتهاك وقف النار المبرم في 8 أبريل</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/76262" target="_blank">📅 11:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76261">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5918e5486f.mp4?token=oI8OSEVuOYeD0mVrs3O0R7hxBqrPeSaepv8TDImp6o7ZExaZ78zuSIX4u0jRNA-oM0uIfCZqvStPpdRSzR25hdV-mMRw4mQfsLs1wmNYQcKqix6XgS4uiVXkllrn7_zAesClgKgCCGAxQaKEvNpxPFHpYmoZjXeZY3uV36FY1GEvfneERsUMDkjxz-m0-EW0ywf_Z8j3tiYprw-BkqHIohvVlNqxzigBdJigLCmkihI6WQAMGniadDP_cs-daKscZaYl3oWpjPpKMLUpFF8ytDQVjJjDPokF2KB0LtOt6AZQgR3VwPL3AL0OTICu6fJR4ea2fBT8d2-702rZp-ryZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5918e5486f.mp4?token=oI8OSEVuOYeD0mVrs3O0R7hxBqrPeSaepv8TDImp6o7ZExaZ78zuSIX4u0jRNA-oM0uIfCZqvStPpdRSzR25hdV-mMRw4mQfsLs1wmNYQcKqix6XgS4uiVXkllrn7_zAesClgKgCCGAxQaKEvNpxPFHpYmoZjXeZY3uV36FY1GEvfneERsUMDkjxz-m0-EW0ywf_Z8j3tiYprw-BkqHIohvVlNqxzigBdJigLCmkihI6WQAMGniadDP_cs-daKscZaYl3oWpjPpKMLUpFF8ytDQVjJjDPokF2KB0LtOt6AZQgR3VwPL3AL0OTICu6fJR4ea2fBT8d2-702rZp-ryZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الحرس الثوري الإيراني ينشر مشاهد الرد على هجوم الجيش الأمريكي فجر اليوم على نقطة في ضواحي مطار بندر عباس.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/76261" target="_blank">📅 11:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76260">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">⚽️
قرعة كأس آسيا تضع منتخب العراق الشبابي إلى جانب الإمارات وتايلاند وتركمانستان.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/76260" target="_blank">📅 10:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76259">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">📰
بلومبرج: رفع ترامب نسخة جديدة من دعواه القضائية التي تبلغ قيمتها 10 مليارات دولار بتهمة التشهير ضد صحيفة وول ستريت جورنال وشركتها الأم نيوز كورب، وذلك بسبب مقال حول علاقاته الوثيقة المزعومة بجيفري إبستين.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/76259" target="_blank">📅 09:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76258">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">بوليتيكو: القوات والأسلحة الأمريكية جاهزة لمهاجمة كوبا، ولا ينقصها سوى الأمر النهائي من ترامب.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/76258" target="_blank">📅 09:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76257">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">بيانات التداول: أسعار النفط العالمية ترتفع بنحو 4% صباح الخميس وسط توقعات باضطرابات في عبور ناقلات النفط عبر مضيق هرمز</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/76257" target="_blank">📅 08:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76256">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">⭐️
دوي انفجارات عنيفة في الكويت نتيجة هجوم  صاروخي وطيران مسير،تفعيل الدفاعات الجوية الآن</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/76256" target="_blank">📅 06:52 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76255">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">⭐️
دوي انفجارات عنيفة في الكويت نتيجة هجوم  صاروخي وطيران مسير،تفعيل الدفاعات الجوية الآن</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/76255" target="_blank">📅 06:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76254">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇺🇸
🇮🇷
إن بي سي عن مسؤول أمريكي: هجمات "محدودة للغاية" و"دقيقة للغاية" قد نفذها الجيش الأمريكي بعد سلسلة من إطلاق الصواريخ والطائرات بدون طيار والقوارب الصغيرة من قبل الحرس الثوري الإيراني.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/76254" target="_blank">📅 04:16 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76253">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇺🇸
🇮🇷
أكسيوس عن مسؤول أمريكي: أطلقت إيران أربع طائرات مسيرة هجومية أحادية الاتجاه تستهدف سفينة تابعة للبحرية الأمريكية وسفينة تجارية.  اعترضت القوات الأمريكية الطائرات المسيرة وضربت أيضًا وحدة أخرى إيرانية لإطلاق الطائرات المسيرة على الأرض قبل أن تتمكن من إطلاق…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/76253" target="_blank">📅 03:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76252">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">إعلام أمريكي : الولايات المتحدة نفذت عملية دفاعية في بندر عباس بإيران، مضيفاً أن "الولايات المتحدة ستتحرك لحماية مصالحها الإقليمية، وهذا لا يؤثر على وقف إطلاق النار".</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/76252" target="_blank">📅 03:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76251">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">إعلام إيراني : الأصوات التي سمعت في بندر عباس نتيجة تفعيل الدفاعات الجوية على اجسام مشبوهة</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/76251" target="_blank">📅 02:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76250">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">إعلام إيراني : الأصوات التي سمعت في بندر عباس نتيجة تفعيل الدفاعات الجوية على اجسام مشبوهة</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/76250" target="_blank">📅 02:16 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76249">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNGzJAGCp8FP1yZwqwMsHYbdispmMsdGj9gOAhJRq8dBv4d_bOoHIkRQPjczMZoD4ih-WtQ16eC8n_YqjT1ULDbMgHu_sr0dK1IgOiFY7vkxZNXcbTKVhzHOcZybG9t4kZ-VeDTVxsZjvG3IEQXnO43tW7S41FOarMpj7PylOAii_s_mZJdj-0VY1-W2Mdj_YSAF0wKIeEVfrBqoVB98JjhCxqp2MzjYNKtYqsQxRSZuQUjGay69J1H_U73c1HwPOTtKjd0Me1DzMpoVONPbz_RogTjUkw_KY-oSMlemwqUAdgryfYyYBRgGmuSqvpmJ4XH3VD1ERgX9La8PVpRkkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏
وزارة خارجية كوريا الشمالية:
لن تتخلى كوريا الشمالية عن برنامجها النووي أبداً.
والبي زود خل يجي
...</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/76249" target="_blank">📅 01:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76248">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🌟
🌟
الجندية روتم ياناي التي قُتلت اليوم نتيجة إصابة طائرة مسيّرة مفخخة في شومِرا كانت من المفترض أن تسافر قريبًا في رحلة إلى تايلاند، لكن ذهبت سفرة الى الله.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/76248" target="_blank">📅 00:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76247">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dbfb4847d.mp4?token=Qz4pglhEOoIeAEBOQXMA7ClQOb4s-WsGozpTxwmG5fioDI4vQgp11Y8UkKHJw1Uq6rLqvqkM4rTcFODwJRH-tGkKfltI0wboPgMrFXlhYHzZH39nirQyCcjQCSBShYuwgOtZHJFdBjVSLlDiGd5TxwIudcEynuNqu2_6wRut6r1nK0uQBt_JHDpD5WJfTt9y3r4zbwWHZ7ouYLWCQjmHIysAjFIxd9Hi1zIga6h-m6J1H_KyIJIllNSROY-gb4WM6yetteBhJji1LSygJg-W9EWSOaXNAaQOkypZCCCMUqIvO7se98CfDL7ZrrAcWLKvkseGbcNZ-5JTRV0DSba13Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dbfb4847d.mp4?token=Qz4pglhEOoIeAEBOQXMA7ClQOb4s-WsGozpTxwmG5fioDI4vQgp11Y8UkKHJw1Uq6rLqvqkM4rTcFODwJRH-tGkKfltI0wboPgMrFXlhYHzZH39nirQyCcjQCSBShYuwgOtZHJFdBjVSLlDiGd5TxwIudcEynuNqu2_6wRut6r1nK0uQBt_JHDpD5WJfTt9y3r4zbwWHZ7ouYLWCQjmHIysAjFIxd9Hi1zIga6h-m6J1H_KyIJIllNSROY-gb4WM6yetteBhJji1LSygJg-W9EWSOaXNAaQOkypZCCCMUqIvO7se98CfDL7ZrrAcWLKvkseGbcNZ-5JTRV0DSba13Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
اشتباكات عنيفة في محافظة كركوك شمالي العراق بين القوات الامنية وعصابات داعsh اسفرت عن مقتل عدد من عناصر داعsh وتدمير عدة مضافات.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/76247" target="_blank">📅 00:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76246">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">هل قتل العراق العقل المدبر وأبرز مصنعي الأسلحة الكيماوية في داعش قبل يومين ؟!
ننتظر التأكيد الرسمي</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/76246" target="_blank">📅 00:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76245">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🌟
🌟
الجندية روتم ياناي التي قُتلت اليوم نتيجة إصابة طائرة مسيّرة مفخخة في شومِرا كانت من المفترض أن تسافر قريبًا في رحلة إلى تايلاند، لكن ذهبت سفرة الى الله.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/76245" target="_blank">📅 23:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76244">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDG1daCJ7dGDzmWFER-y6X4pyBFeBKzANKCpLHxGosO5tQyc44mHxQrjck0Yp0_fFqODbg_kulE583RDx4f10sRxjbsLl1KFyiKb-ZxM0xNPZg95M2O79FM6N74dilry8FK11s_wnxCUSdWUD-NMYjkznjjd7Mr6RmXycp1UpVIhMcv0s49mi6bCkvAa7kl4WAl1bfHLnxc2zutROkKzxGW5lczy9mioubaL9KctOn2z9cfJ9JbigWVgbdK1pONfQ8WNjPQa-J8v7I1rVe3Jam-zdAEzj4Pl8BU8QnSFCmtr6ZTffzCngdsWlEvuGnvpgyG_INgOWy3qUOAf_W6SdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انباء اولية: قتيل و7 جرحى في شوميراه بعد هجوم مسير لحزب الله.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/76244" target="_blank">📅 23:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76243">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🌟
أُنقذ "ترامب" من الذبح خلال عيد الأضحى. اشترت السلطات البنغلاديشية جاموسًا أمهق نادرًا يزن 700 كيلوغرام، أطلق عليه السكان المحليون لقب "ترامب" نسبةً إلى خصلة شعره الشقراء الأمامية، التي تُذكّر بتسريحة شعر السياسي الأمريكي.
كان من المقرر ذبح الحيوان خلال عيد الأضحى، لكن الوضع استقطب اهتمامًا كبيرًا، إذ بدأ الناس بالتوافد لرؤية الجاموس غير المألوف. عندها قررت السلطات التدخل، فاشترت "ترامب" من مالكه، وأرسلته إلى حديقة حيوان دكا.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/76243" target="_blank">📅 22:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76242">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 23-05-2026 منصّة منظومة مضادة للمحلّقات تابعة لجيش العدو الإسرائيلي عند مرتفع الجرداح على الحدود اللبنانية الجنوبية بمحلّقة أبابيل انقضاضيّة.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/76242" target="_blank">📅 22:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76241">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇫🇷
‏
ماكرون
: النرويج وافقت على الانضمام إلى المظلة النووية الفرنسية.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/76241" target="_blank">📅 22:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76240">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🏴‍☠️
‏جيش الاحتلال: إصابة جنديين نتيجة إطلاق قذيفة مضادة للدبابات جنوبي لبنان</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/76240" target="_blank">📅 21:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76239">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇮🇷
ممثل المرشد الإيراني بالحرس الثوري: هدف المفاوضات ليس تقديم تنازلات للعدو أو التراجع أمامه</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/76239" target="_blank">📅 21:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76238">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‏المراسل: مع استمرار ارتفاع أسعار الوقود في جميع أنحاء البلاد، يدفع الناس مبالغ أكبر مقابل السفر. هل يدفعك ذلك إلى الإسراع في إبرام الصفقة؟  ‏ترامب: الأولوية القصوى هي ألا نسمح لإيران بامتلاك سلاح نووي</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/76238" target="_blank">📅 20:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76237">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‏ترمب:   ما حدث في إيران هو تغيير لنظامين والآن نتعامل مع الثالث   سنمنح إيران فرصة وجيزة بناء على طلب رئيس وزراء باكستان وقائد جيشها  لن أقبل باتفاق غير مثالي مع إيران نود أن تنضم هذه الدول إلى اتفاقيات أبراهام. أعتقد أنهم مدينون لنا بذلك. لست متأكدًا من…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/76237" target="_blank">📅 20:52 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76236">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‏ترامب: بإمكاننا إنهاء الحرب مع إيران بسرعة كبيرة، وقد نضطر إلى ذلك. لكنني لا أعتقد أننا سنحتاج إلى ذلك</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/76236" target="_blank">📅 20:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76235">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامب: "نحن لا نتحدث عن أي تخفيف للعقوبات أو تقديم أموال. لا عقوبات، لا أموال، لا شيء على الإطلاق."</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/76235" target="_blank">📅 20:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76234">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4beb407f7c.mp4?token=ZZdYgr3FOrZ3sbNHP7RlyspisEaA0DG9d94EYmuUDxLdopEzSYnlHaZv-NOMkpY0n3AfvghqwWKGfkBNaYOONaDhffvNgY4sVcsv8EtUTYKosqRbA8F6aBw5RUiEOoUY-vlWjI6Bw49OV-ofx1USFQiPHMnxd1Gs-ZDSCyq2ZOMjcx33r7BKhCEvf8r2UbV849skej4M0Wrrg9oq9DrcUGrNwdgCMQRDwcnKN_swqmawpbyzT0TXObdQs7dfW5D-LI5-Tzs_iS2QyGV66cKzDG321rtB1c-fLwUvkjMimb9FUZYBJKjC47ro3WX50zXlJ87JQyKy8qiCcvkUnjxVCoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4beb407f7c.mp4?token=ZZdYgr3FOrZ3sbNHP7RlyspisEaA0DG9d94EYmuUDxLdopEzSYnlHaZv-NOMkpY0n3AfvghqwWKGfkBNaYOONaDhffvNgY4sVcsv8EtUTYKosqRbA8F6aBw5RUiEOoUY-vlWjI6Bw49OV-ofx1USFQiPHMnxd1Gs-ZDSCyq2ZOMjcx33r7BKhCEvf8r2UbV849skej4M0Wrrg9oq9DrcUGrNwdgCMQRDwcnKN_swqmawpbyzT0TXObdQs7dfW5D-LI5-Tzs_iS2QyGV66cKzDG321rtB1c-fLwUvkjMimb9FUZYBJKjC47ro3WX50zXlJ87JQyKy8qiCcvkUnjxVCoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: إيران بدأت تُعطينا ما نريد، وإذا لم تنجح الأمور، فسيكمل هيغسيث المهمة.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/76234" target="_blank">📅 20:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76233">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‏المراسل: هل ستكون مرتاحاً لو استولت روسيا أو الصين على اليورانيوم المخصب الإيراني؟  ‏ترامب: لا.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76233" target="_blank">📅 20:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76232">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‏ترامب يهدد سلطنة عُمان: على عُمان أن تتصرف مثل أي دولة أخرى وإلا سنفجرها</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/76232" target="_blank">📅 20:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76231">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb93e7ae7c.mp4?token=iv3BcqcC-E2i4M0617zKBkNnIoeMzqbpNNkhbnrO3WU2Xv-G0OdKtKLcQqc3fRUHZZYKId4xTtW-HcyEqVZYdTaBDy6ruRMVuDpYSVnKEm8jc96awC8FcUeBM1foU_NrbaYs7e-BJmO2BFuIc43rMeUnH_v4EPKnb9aOvEMxDoheKD8IIZREGaGo5g3HNvnO8p8wRoQEl81JDCFp9rUh2kjuV2OhcMXl8y04o33uxc6Ur0QHH6eA4M2i2mIHSdHYICLDqm6cpFdtOEu4M1EZr9k-kZHxeh74rN7uCA452PLY91G-oEPD4KNYi16c8ejHuynuxPTqQg4zrJH6R0XtIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb93e7ae7c.mp4?token=iv3BcqcC-E2i4M0617zKBkNnIoeMzqbpNNkhbnrO3WU2Xv-G0OdKtKLcQqc3fRUHZZYKId4xTtW-HcyEqVZYdTaBDy6ruRMVuDpYSVnKEm8jc96awC8FcUeBM1foU_NrbaYs7e-BJmO2BFuIc43rMeUnH_v4EPKnb9aOvEMxDoheKD8IIZREGaGo5g3HNvnO8p8wRoQEl81JDCFp9rUh2kjuV2OhcMXl8y04o33uxc6Ur0QHH6eA4M2i2mIHSdHYICLDqm6cpFdtOEu4M1EZr9k-kZHxeh74rN7uCA452PLY91G-oEPD4KNYi16c8ejHuynuxPTqQg4zrJH6R0XtIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب: ‏مضيق هرمز سيكون مفتوحا أمام الجميع ولن يتحكم به أحد.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/76231" target="_blank">📅 20:29 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76230">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇺🇸
ترامب: الإيرانيون يعتقدون أنني سأنهي الحرب بسبب الانتخابات النصفية لكنني لا أكترث بذلك.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/76230" target="_blank">📅 20:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76229">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية تصدي المقاومة الإسلامية بتاريخ 19/20-05-2026 لمحاولة التقدم الرابعة لقوات وآليات جيش العدو الإسرائيلي باتجاه بلدة حداثا جنوبيّ لبنان.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76229" target="_blank">📅 20:16 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76228">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇺🇸
روبيو: الدبلوماسية خيار أول لنا لكن هناك خيارات أخرى مع إيران.  ‏نعتقد أن هناك تقدما تم إحرازه نحو التوصل إلى اتفاق مع إيران وسنرى خلال الأيام المقبلة.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/76228" target="_blank">📅 20:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76227">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🌟
🏴‍☠️
محرقة زوطر.. إستهداف وإحراق دبابة ميركافا تابعة لجيش الإحتلال الصهيوني بالإضافة إلى إستهداف آلية نميرا وآليتي جاك هامر وجرافة D9 وتجمع لقوة صهيونية في بلدة زوطر بجنوب لبنان.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/76227" target="_blank">📅 20:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76226">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7e4a4347d.mp4?token=Jhhc645E_rgnSqVNxivicya9bPL6e72QyWl3yThpI2xgWdwtcrza0eXOGHIeZDeZwhRyevPgl-ExW5gU8ukm76_NHzZVloURucNl5pQ0q-SCc2uwR7e-aiat2-g_zzOhjYZKs04NYnXESyMMiCBVFKIsduZX9Qg3jANU9XgOVwwo2gnNA3JTre2tMDzkf6kr4h6rox0m4uLoddKPsF1_Q9X75M0Xhn3zG2BiJPBtOayJLAi3AdF6jJRIzB29XjrXn4k1059l92dZssgG4xPEUbnsSxmWcwRKsqwecuhoVs-pDvpXVevCYasUBw5W9SEk64MVebLfjOHsA0AQBbxhng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7e4a4347d.mp4?token=Jhhc645E_rgnSqVNxivicya9bPL6e72QyWl3yThpI2xgWdwtcrza0eXOGHIeZDeZwhRyevPgl-ExW5gU8ukm76_NHzZVloURucNl5pQ0q-SCc2uwR7e-aiat2-g_zzOhjYZKs04NYnXESyMMiCBVFKIsduZX9Qg3jANU9XgOVwwo2gnNA3JTre2tMDzkf6kr4h6rox0m4uLoddKPsF1_Q9X75M0Xhn3zG2BiJPBtOayJLAi3AdF6jJRIzB29XjrXn4k1059l92dZssgG4xPEUbnsSxmWcwRKsqwecuhoVs-pDvpXVevCYasUBw5W9SEk64MVebLfjOHsA0AQBbxhng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: الإيرانيون يعتقدون أنني سأنهي الحرب بسبب الانتخابات النصفية لكنني لا أكترث بذلك.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/76226" target="_blank">📅 19:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76225">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇺🇸
ترامب: لم نصل إلى اتفاق بشأن إيران بعد ولسنا راضين عن ذلك.  تلقيت دعماً كبيراً من دول أخرى بشأن إيران.  إيران تريد عقد اتفاق وسنبرم معها اتفاقا أو سننهي المهمة.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/76225" target="_blank">📅 19:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76224">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00b90fa443.mp4?token=NNJ9RXUrib0V66FdVkIHcc2ar9Jv0yVuLovPHhrlKd0nUlQ434hSB6RnrBNkAsdCgDH9jTA7VOLGgKQ4l5l6tgRBBny_0zsGaO-iFokC01PF6bY_U0d5Q3HkLAlXO4VXxpfD4rzfApAB_x9jQvez5seIF-Hp0_wYDTMghrfW_hxWjjd5xhn6jPm-v3gik4Y0PhxfSLKyJVPM6-P-EULJGcKfwgCIxiDOZ8RUhA6WAk1iWLxHiTB73p8kzhTj8JSjswTwInRjQlKqj9whlRLOXmJX574vgy6eEnJszIJsSXKpi_WDu0JvrMzaB7Dxtg0Ocfit2uHlQcpSgioIMsFKfaUe7Yw9FUcyt8CGOtqjfEar-s1eb6-fkl2PDK_mLovIPuKU5GIcwNZ-_AvNTkGKRgmD5x1sFqgufkTxV_03uJ3-b0_BA7WrBdY8P1IVlPuBlHEvs0Cx8VB_Xdt5WjBGO16NOWrMhBYzXg-zh0yA_7uTHNHWlTH3hCXPZMPkPHcQmvQoHbWZNJBV_332AIXP08faxfbWA73jF9NFRzM3aweRF2OalbTY7wz-mES2wBbk4pKFmZTySpt6T_nPnpNGxdI40XPOOi3nuLeSGBlSNzjYxNR9vWnPIoPYcVN4Kstm-4oNy1mMcHzuRL7328IbwIOnBFwIVUqaSZCr6TfJUUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00b90fa443.mp4?token=NNJ9RXUrib0V66FdVkIHcc2ar9Jv0yVuLovPHhrlKd0nUlQ434hSB6RnrBNkAsdCgDH9jTA7VOLGgKQ4l5l6tgRBBny_0zsGaO-iFokC01PF6bY_U0d5Q3HkLAlXO4VXxpfD4rzfApAB_x9jQvez5seIF-Hp0_wYDTMghrfW_hxWjjd5xhn6jPm-v3gik4Y0PhxfSLKyJVPM6-P-EULJGcKfwgCIxiDOZ8RUhA6WAk1iWLxHiTB73p8kzhTj8JSjswTwInRjQlKqj9whlRLOXmJX574vgy6eEnJszIJsSXKpi_WDu0JvrMzaB7Dxtg0Ocfit2uHlQcpSgioIMsFKfaUe7Yw9FUcyt8CGOtqjfEar-s1eb6-fkl2PDK_mLovIPuKU5GIcwNZ-_AvNTkGKRgmD5x1sFqgufkTxV_03uJ3-b0_BA7WrBdY8P1IVlPuBlHEvs0Cx8VB_Xdt5WjBGO16NOWrMhBYzXg-zh0yA_7uTHNHWlTH3hCXPZMPkPHcQmvQoHbWZNJBV_332AIXP08faxfbWA73jF9NFRzM3aweRF2OalbTY7wz-mES2wBbk4pKFmZTySpt6T_nPnpNGxdI40XPOOi3nuLeSGBlSNzjYxNR9vWnPIoPYcVN4Kstm-4oNy1mMcHzuRL7328IbwIOnBFwIVUqaSZCr6TfJUUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: لم نصل إلى اتفاق بشأن إيران بعد ولسنا راضين عن ذلك.  تلقيت دعماً كبيراً من دول أخرى بشأن إيران.  إيران تريد عقد اتفاق وسنبرم معها اتفاقا أو سننهي المهمة.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/76224" target="_blank">📅 19:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76223">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇺🇸
‏ترامب: البحرية الإيرانية وقوات إيران الجوية دمرت.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/76223" target="_blank">📅 19:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76222">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKdDowl7pG3OA2-IVHVFvCUX6ZVc38CeIjtJlmJAYY6xeqc1UBc9TrTvDdmsyotj6mAtZEyCDLAP0P8SCXVncnwTEPLr3ui5shqHTArvnHYx9PsRS8XFeP-1ML78yis4GGjvi6NXKfZYnXBc-HNe0hXFd8SmMlH72cZSq8Q65R5PRB7N2WSnc1fNPb4nQq_oY7ek-ZSStnelofbVhOqJ1rOmv-l8XQTvzSpy_WjY3hfjlO6YD8zB1jHcZ3--bur4R0dfeo4V4AhOGYtq6pmbt9B9Cke25AXjGe8wKPDqzbafnkfNM7-in2gaAm8XkBjtongtEPodBvgHSS4tAY9nEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب: إيران لن تحصل على تخفيف العقوبات مقابل التخلي عن اليورانيوم المخصب عالى النقاء.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/76222" target="_blank">📅 19:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76221">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو الاء الولائي- القناة الرسمية</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SpScvryOvJ3cHn6-AHDI0LLkBaoGUpZRqrEw4BrcD9BWZtIbpZwkXU2stK7Up9kuHwXbe4NeZG5DnzRfPxBmVDeUzjHQDOtKXfNCXL7u9Ipwu9TQaWf2znS0O2J2pC9IgsUQgMu7CtPVwN4GZlyZilSWbCbODSlMYhkmn4RX1tfcdLoBRJChMC9WVElZK3Ufgh2_FLCLVY_h3Z9PqEUOToFCjGvaDSZi2uyvA31dSOeMaXJcMYfnfE0ZpFD0vfrReiTR0W2fOcptifrt6ZgK3kDc6mnwq4CbSHvOAFKzPCOJktY0l5H1epUMlM0B0jg-YBhvIyqVRo4r4taU7Jd23w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">كل عام وانتم الى الله اقرب</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/76221" target="_blank">📅 19:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76220">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇺🇸
ترامب: يجب على السعودية الانضمام إلى اتفاقيات إبراهيم.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/76220" target="_blank">📅 19:18 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76219">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇺🇸
ترامب:
يجب على السعودية الانضمام إلى اتفاقيات إبراهيم.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/76219" target="_blank">📅 19:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76218">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇮🇷
الإعلام الإيراني:
تشير مصادر مطلعة إلى أن الرئيس الأمريكي دونالد ترامب من المرجح أن يعلن خلال الساعات القادمة من جانب واحد عن إبرام الاتفاق الإيراني الأمريكي. ويُقيّم هذا التحرك من جانب ترامب بهدف ممارسة الضغط وفرض اتفاق على الرأي العام قبل تسوية الخلافات بشكل كامل.
مع ذلك، أكد أحد أعضاء الفريق التفاوضي الإيراني أن بعض القضايا لا تزال عالقة، وأنه لن يتم التوصل إلى اتفاق حتى يتم حل جميع القضايا التي تنظر فيها إيران. ووفقًا للمصدر، إذا تم حل هذه القضايا بشكل كامل، فستعلن إيران النتيجة رسميًا.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/76218" target="_blank">📅 19:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76217">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇮🇶
وزارة الدفاع العراقية:
قتل عناصر إرهابية وتدمير وتفجير مضافات بعملية نوعية في أعقد المناطق جغرافياً في محافظة كركوك.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/76217" target="_blank">📅 18:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76216">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🌟
🏴‍☠️
محرقة زوطر..
إستهداف وإحراق دبابة ميركافا تابعة لجيش الإحتلال الصهيوني بالإضافة إلى إستهداف آلية نميرا وآليتي جاك هامر وجرافة D9 وتجمع لقوة صهيونية في بلدة زوطر بجنوب لبنان.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76216" target="_blank">📅 18:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76215">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3cd22697a.mp4?token=QlhTXue0wLvEfai4weTHojrZKn81AqWj1_O_vLz5rzUbVahHgnUBAjtGzDtrthQlSeTc9kM9Ib4f31nm2gD5D69wtbmNCQHWpKR2xcpG4fACHeFtTdcjmpdeSOWolvLxTwgoffsYvTzLP8rY3p37qHRK9TgaQ-e09Tz37KVrv5bZL4JyrZc5KfYP7smjqYB0po8MbLuKl-v0pSJVvT0v0E9nhY2HgA0k8kplPcRpSVHoe7cpBMVm6dNZgJoS7LcZmyHBxev1jRLgKbo_axXtVBnycmHoYhbFQ_0hHtOnlZJwWC9Qi0r5u7ID8LxQTdQ5OyaxNwYj-0QOC0eJ1kx6MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3cd22697a.mp4?token=QlhTXue0wLvEfai4weTHojrZKn81AqWj1_O_vLz5rzUbVahHgnUBAjtGzDtrthQlSeTc9kM9Ib4f31nm2gD5D69wtbmNCQHWpKR2xcpG4fACHeFtTdcjmpdeSOWolvLxTwgoffsYvTzLP8rY3p37qHRK9TgaQ-e09Tz37KVrv5bZL4JyrZc5KfYP7smjqYB0po8MbLuKl-v0pSJVvT0v0E9nhY2HgA0k8kplPcRpSVHoe7cpBMVm6dNZgJoS7LcZmyHBxev1jRLgKbo_axXtVBnycmHoYhbFQ_0hHtOnlZJwWC9Qi0r5u7ID8LxQTdQ5OyaxNwYj-0QOC0eJ1kx6MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
غارات صهيونية على مدينة صور اللبنانية.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/76215" target="_blank">📅 18:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76214">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇷
‏التلفزيون الإيراني: طهران ستتولى إدارة مسار حركة السفن عبر مضيق هرمز بالتعاون مع سلطنة عمان وفق المذكرة</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/76214" target="_blank">📅 18:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76213">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/foW2UCMhKPZ5BfRF96JsIsqZydqB1dF098DxTtTeunqHCFkXRW217Ph7uU53uILpe7Pd5RkEWFwbniKkgUINwNlZJE8fNOTeHh6A4c3CNswDVuNOoFiUJVDCPOT2aSrFivpWNLxZE9XJn9sc6VlDwF9YwDHxroGuiXcAzl7-d_0vHn2ySYRq6rmluwX2DQYkNYYxzair0l6c4_noj0r8fVRiN8JPVVaWCsQxUBNqaKfYdu3IPvAmxXPrKsEd9DBQmiiFfVXVX8zc5-qclvwJ78ey2iPtvlO4ILkpg2ROqmc_PoIa-wnR4CzTIdrmuVua-p5y6r4RZvlw1Zaj49C-4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
اعمدة الدخان المتصاعدة في العاصمة الإيرانية طهران ناتجة عن حريق طال مبنى سكني ولايوجد أي حادث أمني.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76213" target="_blank">📅 17:57 · 06 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

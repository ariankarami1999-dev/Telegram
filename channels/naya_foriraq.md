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
<img src="https://cdn4.telesco.pe/file/GhITPEx3jOYXFDz8aeXaFlbZjXFAymrZpfMSIm0BnPG3WuJy__0_CK4dC8RSWXua1AhZOn6hpUIRp1_PDNJ3xLV4nayry0kfKIg56se8Txe1iB5JzwCZfoDNGz92ebJrcSfW3l96z_c3PJzWwoPR7DufsNikMP06a3krCzCg7VOFx6jzFk6a3vzsSUYlvQ_mE7WBcVZKIpRD1U2a-PyGzCSgWL28CthHqUulnW9FIXL--5khVlg0EW3ii1Ez4C6FCFZDHGxKYP5OcFqoArdyRP_X-BXWzAO3k2naCGL1rbLlGgoydv0ltEJZ7frJ1lZxU06oXQNpKyIFWQasCZ26Iw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 270K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-03 07:36:06</div>
<hr>

<div class="tg-post" id="msg-88479">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZ_og4XyOkn2jqZAvflEzb16pou24SCg4yO3WcuNMYaQJ_VDNWgeaulTKY8Z2hoaqbuQ_z-DyyGxjsktzzf27rmGgucGNfHbi-NM63N8QTlUG5fBCpbdIWEH6I5jRlNvVU6w0t4Ey9jwYIx-XWAkN1Y3xuPlM9D1T5C8gfoO38R6hdSFUf1nzQ676pFoMiES193pPo-pMFU3RoNwCrKHtzhtXx2yAEC4Sb1eA4xqpGxV2yw2qD8dr0loxwOUFB50pkdtnZkpfQJSlWy3rpCsKltAPsKkUugszp1VTZkxLM-RLFtWCDaYpWOKJzM_rc1-B_NC7D-ADFGbWwqb6X5Wcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر
🔻
‏إستهداف ناقلة نفط بمقذوف حربي على بعد 9 أميال بحرية شمال شرق سلطنة عمان.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/88479" target="_blank">📅 01:41 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88478">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3dbea05a2.mp4?token=C3EKGXMNxmBXrEXHLFoDjqZBtRKX3q-PV6JO87k6xq39ed9NNq0CIG0f9BLthGsMr-YfVE9pc4lVREVLUwD8yuYjCnoBH9kAIFpNwwifOM7cEVeil2Ch9auF9AY1IYUfHg5CtODQWDb_KfXuEM57aWqRuHUu2b5Ov4TiVLP-bGKrtVu2HY2JS5zm1_h6l-hycV5n2NYhKHdqTXpS2e2UkwRuYFRDJLoROJuU10G5GYavcYLZ-xM4MESyTfqHUQ6D5fQ9eI8lDJoGXbdYjw6VmGCJFs9Vmf91KgcFbSHuEkBvCFofFKIS4QyLkNs6yuGWlcLquysb6NRVbnwtwaaq924WviweKsgpk5VU4AUllGjQFX7oLBZuAP_0YTbkUlyi1nBRNq65bt0jz-w2XgyRkKnCNLzOsb6SU7SFJxI3jVkLrtOIHGfLx5W4wmfbmOuWaRQrPV2Na2v_ygnBru1UKzLGnwCgINZQ0js4bfFEQbWt5FhXFcuG1gb40NDEfGqCcOKmcWLMFGnxko6ZNlIFrlrvIGubwNcEP55areBKdgPM9lYTiCqUltge9GnW8_f_yqcG95r8Y3hsG4eF1-XQ6m8SDhB4VmsFtgv0OpmRBW_BLzQTIKwIISnUbJvn-ugSS1DWqb8S8UnSPg1LI5vqz-QLaILzeQ5t45yVJJZ2rQc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3dbea05a2.mp4?token=C3EKGXMNxmBXrEXHLFoDjqZBtRKX3q-PV6JO87k6xq39ed9NNq0CIG0f9BLthGsMr-YfVE9pc4lVREVLUwD8yuYjCnoBH9kAIFpNwwifOM7cEVeil2Ch9auF9AY1IYUfHg5CtODQWDb_KfXuEM57aWqRuHUu2b5Ov4TiVLP-bGKrtVu2HY2JS5zm1_h6l-hycV5n2NYhKHdqTXpS2e2UkwRuYFRDJLoROJuU10G5GYavcYLZ-xM4MESyTfqHUQ6D5fQ9eI8lDJoGXbdYjw6VmGCJFs9Vmf91KgcFbSHuEkBvCFofFKIS4QyLkNs6yuGWlcLquysb6NRVbnwtwaaq924WviweKsgpk5VU4AUllGjQFX7oLBZuAP_0YTbkUlyi1nBRNq65bt0jz-w2XgyRkKnCNLzOsb6SU7SFJxI3jVkLrtOIHGfLx5W4wmfbmOuWaRQrPV2Na2v_ygnBru1UKzLGnwCgINZQ0js4bfFEQbWt5FhXFcuG1gb40NDEfGqCcOKmcWLMFGnxko6ZNlIFrlrvIGubwNcEP55areBKdgPM9lYTiCqUltge9GnW8_f_yqcG95r8Y3hsG4eF1-XQ6m8SDhB4VmsFtgv0OpmRBW_BLzQTIKwIISnUbJvn-ugSS1DWqb8S8UnSPg1LI5vqz-QLaILzeQ5t45yVJJZ2rQc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🔻
تنفرد نايا بنشر اللقطات الاولية لاعتقال الحاج ابو جعفر التميمي القيادي بالحشد الشعبي من العاصمة بغداد على يد عجلات تحتوي عبارة INSS في اشارة لجهاز الأمن الوطني العراقي</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/88478" target="_blank">📅 01:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88477">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏
🇺🇸
رويترز :
أعلنت قوات مشاة البحرية الأمريكية في سيول، يوم الاثنين، إلغاء مناورة إنزال برمائي مشتركة مع كوريا الجنوبية كانت مقررة الشهر المقبل، وذلك بسبب القيود المفروضة على القوات الأمريكية جراء الحرب مع إيران. وأضاف متحدث باسم كوريا الجنوبية أن الحليفين ما زالا يجريان مشاورات بشأن استئناف مناورة "سانغ يونغ</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/88477" target="_blank">📅 01:24 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88476">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8050a036ac.mp4?token=sQsSPmbuZVv8aOVpbS0xZkfKPkRS5sInt7MJcFJ-iormKEpIJ1BRKHG2jHqxktBSuFEknWa_d6lKCNAebdb4Sfdh1-zKvxviXaf6rF15MKJZnwm5o2gJnXzDLjW5EiET5CRsEjwTaTmXskRF3x0E672Idbxc_XWKk4iVSzEGddsMVnBu7j18kRVzTLCyTn3Ubl-C-sIbbYuKvHXjhA5WP_9LP-ZxXM36m7bzC5yMxsTi3c2SJQ0VAyvMadA74EFEIhG5zqVQcQXEm-7bHvMGOaLXqF6zl2w0fishXWZeUsU4xs35NXtp4CPK7xC-m1oV3sj3-ioTa5yxcDrXKScT4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8050a036ac.mp4?token=sQsSPmbuZVv8aOVpbS0xZkfKPkRS5sInt7MJcFJ-iormKEpIJ1BRKHG2jHqxktBSuFEknWa_d6lKCNAebdb4Sfdh1-zKvxviXaf6rF15MKJZnwm5o2gJnXzDLjW5EiET5CRsEjwTaTmXskRF3x0E672Idbxc_XWKk4iVSzEGddsMVnBu7j18kRVzTLCyTn3Ubl-C-sIbbYuKvHXjhA5WP_9LP-ZxXM36m7bzC5yMxsTi3c2SJQ0VAyvMadA74EFEIhG5zqVQcQXEm-7bHvMGOaLXqF6zl2w0fishXWZeUsU4xs35NXtp4CPK7xC-m1oV3sj3-ioTa5yxcDrXKScT4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لولا دماء بلال الوحيلي و شيخ ياسر عاتي الكعبي   لكانت الجرف الان ولاية ارهابية داعشية سلفية ..  شكرا حميد</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/88476" target="_blank">📅 00:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88475">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5i3yjaM4twDEHAW62fB4ZFJ53ebOutzRXariC4DT9Z3URYHYOlkLymMW5i9hGJPLmpfwOePqJCoYoYRcLRgZ7Mh-mn5E9hfnsXCA9mUcH8_7hw1bnit8l2idOhtsDO2Vp0D4wS2TQnVtk3FA_tsjd84lyRuCLisa4IuiJeFuujvrfsHMGmwbNKdEoLeCiGH26K7Pfve4ReO_8uSQ42yPKRiiFXcOcHdnWA_9wvqc8DS75vETwBlK-ARNNw5NShXo5faBIOF1ClmCLzsxRuHquNnpXOb9mOAauhPU9rsE68EPhOyaPavShci1T6cLldOMd0Z5YNjVQS1S8obHMvdQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏
الخارجية الاميركية تعيد نشر:
مكافأة 10 ملايين دولار لمن يدلي بمعلومات عن قائد الحرس الثوري و4 قيادات أخرى.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/88475" target="_blank">📅 23:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88474">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇺🇸
وزير الحرب الاميركي ‏هيغسيث:
لا يستبعد استخدام القوة العسكرية في مضيق هرمز أو أي مكان آخر، لا تزال إيران تمتلك بعض القدرات.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/88474" target="_blank">📅 23:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88473">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845b8cd8b7.mp4?token=AovbA0rA1BONpYX2Q4uZkSN1NPRa2NJJ9BaY4MIN20KXTaox9AgeC2VVbFSFFxEXz1lmYtOaB2hMUeQu3qjlvM4aZwqTbve-fwCDRlcFk5gGdMSO2FiRkYnHvoYMxvImLs2nWa7MC4rpxKHcL3tEk4rTkHMkdkEtNuz-y3H0qmxPzOfbkQMAnUcp_DYuCKX0r-il3v-uFNsAwUwya3FnkROSqvSzhiehnRmr6EQ4d22tsFVN1slrTFJSuaQg61CYvzz1P_zoDvb8CeFuy2_Q9G81IIfZ9ZcKS_tqvNIWIegOMAOjaIJK5B35Xe8-VY1HfSqFu_vFyhZ9bGkje5QpQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845b8cd8b7.mp4?token=AovbA0rA1BONpYX2Q4uZkSN1NPRa2NJJ9BaY4MIN20KXTaox9AgeC2VVbFSFFxEXz1lmYtOaB2hMUeQu3qjlvM4aZwqTbve-fwCDRlcFk5gGdMSO2FiRkYnHvoYMxvImLs2nWa7MC4rpxKHcL3tEk4rTkHMkdkEtNuz-y3H0qmxPzOfbkQMAnUcp_DYuCKX0r-il3v-uFNsAwUwya3FnkROSqvSzhiehnRmr6EQ4d22tsFVN1slrTFJSuaQg61CYvzz1P_zoDvb8CeFuy2_Q9G81IIfZ9ZcKS_tqvNIWIegOMAOjaIJK5B35Xe8-VY1HfSqFu_vFyhZ9bGkje5QpQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب الترجمة بتصرف " كندا ٥٦ لسنوات طويلة وجانت ناصبة علينا "</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/88473" target="_blank">📅 21:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88472">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d9654cfd2.mp4?token=CX_QEnnfBfQ-zEaaPY4j-p5uiT9C3f0-jeeGcJK2_AXZdXOQdk1EAT70g6Q9A0l-AAGZVtFNvdNnFxqAHQjGmCZN4Vhjo4TtO-PxPhU6Ix-IIg5dEpn4vUgNsWOzDJd3Hy9r9tYz60ZgV_9l-YYil3vAQsdRtfmHGzaF1J5Pbb9MQrehW71IYcHv4l1z5LPfKwJf8oID7AGGVL7fNbTMCzNkKdWpXvY_Qw0-a4DV4GuVbJoyk63-JAFp_1MVTkgRU6U5efRMvhS4FwO0doltcSaq5HlXkcua46BEiuf4R1CuPeJdd4mEO-1jF-wKJMsw3FY7oGegY_Eb1R3mIWAFGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d9654cfd2.mp4?token=CX_QEnnfBfQ-zEaaPY4j-p5uiT9C3f0-jeeGcJK2_AXZdXOQdk1EAT70g6Q9A0l-AAGZVtFNvdNnFxqAHQjGmCZN4Vhjo4TtO-PxPhU6Ix-IIg5dEpn4vUgNsWOzDJd3Hy9r9tYz60ZgV_9l-YYil3vAQsdRtfmHGzaF1J5Pbb9MQrehW71IYcHv4l1z5LPfKwJf8oID7AGGVL7fNbTMCzNkKdWpXvY_Qw0-a4DV4GuVbJoyk63-JAFp_1MVTkgRU6U5efRMvhS4FwO0doltcSaq5HlXkcua46BEiuf4R1CuPeJdd4mEO-1jF-wKJMsw3FY7oGegY_Eb1R3mIWAFGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
العاصمة اليمنية صنعاء تحتفل بمناسبة مولد النبوي (صلى الله عليه وعلى آله وسلم).</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/88472" target="_blank">📅 21:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88471">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇸🇦
🇮🇷
بيان سعودي فرنسي:
باريس والرياض تدعوان إيران إلى استئناف تعاونها الكامل مع الوكالة الدولية للطاقة الذرية.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/88471" target="_blank">📅 21:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88470">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇺🇸
🇸🇾
الولايات المتحدة تستعد لرفع تصنيف سوريا كدولة راعية للإرهاب بعد 47 عاماً، سوف تقوم إدارة ترامب بإلغاء التصنيف يوم الاثنين.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/88470" target="_blank">📅 20:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88469">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c955d03b1b.mp4?token=jvJMBYpxOnzxT_RQziDytpJJQA3Vy5BTFH03jVthjek4ZwR4Ney1_iV93mdLwvFvvsYT3hfsZXU7hVSOuhQCMFlRozV0K3jEMafIHQl0rQK4yhCYJrZGmFM37NCextKXHzp_pGNkKs0bsBP9Mb0tbqfXL-gYD_ua7J18PK5RsaudAqoitQL7baFrMhk0-jADN3AKsH-f7Ezg029rzdAjoe-wDJ4xFhDhc7X5VlAKHmhU44uUZU-uHgL3cJ5kI04ySfLulLqQtNanUQzcISqiMb5htKnAc7zDmCofClM-0-55dOsD0FQ3FyzzSSt4WyicF0PGyAzFHQh-EcwK5-ptQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c955d03b1b.mp4?token=jvJMBYpxOnzxT_RQziDytpJJQA3Vy5BTFH03jVthjek4ZwR4Ney1_iV93mdLwvFvvsYT3hfsZXU7hVSOuhQCMFlRozV0K3jEMafIHQl0rQK4yhCYJrZGmFM37NCextKXHzp_pGNkKs0bsBP9Mb0tbqfXL-gYD_ua7J18PK5RsaudAqoitQL7baFrMhk0-jADN3AKsH-f7Ezg029rzdAjoe-wDJ4xFhDhc7X5VlAKHmhU44uUZU-uHgL3cJ5kI04ySfLulLqQtNanUQzcISqiMb5htKnAc7zDmCofClM-0-55dOsD0FQ3FyzzSSt4WyicF0PGyAzFHQh-EcwK5-ptQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏
وزير الخزانة الأميركي:
نطلق الهجوم الاقتصادي على إيران، توقف التراخيص العامة التي كانت تسمح ببعض التحويلات المالية إلى إيران - بيان وزارة الخزانة،أي عدو يسهل غسيل الأموال نيابة عن إيران، سيتم استبعاده من نظام الدولار الأمريكي،حان الوقت لقادة العالم للاختيار بين الرخاء والعزلة وبين السلام والإرهاب وبين أمريكا وإيران.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/88469" target="_blank">📅 20:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88467">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XdErM9rTfioLGu9No09KRqLhbWoBrcqzHVzon4YikQfVrOqIKaJF5QD6V1uzdLe4vhzderBGrGD9ebqjAj0lZrL6Bf_jRHcbk_Xkm5fkxp2_d97UUBmyAEAnBeWSEABV0uAkMbDZ6ILzH2B_oiybveKkWTW7jvd0gJ3SUwBkRB84doLc4w3bwvtmOQF5kzGRYWljHIsxmj-AM2x1kz9x-PDCzfmKA-deaXiOq7vIyAFk4fSNxJOAL4ZByhjbTuAjwAnlFe4x6ddfA2QRq1QuOPD3SPExD9V2G7yEBc95j8jQzTcji5hqkO8QsimEF_hFoLlnnGSajt5DOSzmZ4Aeeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JXe_SGF2Rsje9LGg5EQguK6Kc23UcYfRRW6sP1oHk9iukby4PhxshteAQZSAzqtdhtTlVBWqscd08Rboj24ZpusYhf1QOrRfE4HAPjDt6YG-r9TGdfmkfMFzOAjoKLD4X_Gsh5kFTzan3yevb7Zi4d59cy42SpevNuRXn-oa9FgpspFtG_yscISJf7blAOSZwjDM3SnXSV5tc2PgwkYL9B7zVAbEtpYjxha1g5HrssVyT2w8Jo6v8fLAonOXjJH8ddQRnUPDtELIc2mYJsCxSUdvimllOaGkPFjkankQ96l1OxLNg7nt2e_keNUej_-k_AUJ1gksk-WDx_TFZodWGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
🇰🇵
ترامب يعيد نشر صور قديمة تتعلق بلقائه مع رئيس جمهورية كوريا الديمقراطية.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/88467" target="_blank">📅 20:33 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88466">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-DuOmvJEbv8vejJb-t2di2jj4IxrAWSPJAopu7Ih2Pu0hjWo_tqOCljww5utnGo9hQU6myUT9o16FEUG7XB-gBlN-CqQnW2wjDHZNZM9vluHLzE4jcUtv2Yo3dRV8K7xHaQPPWV5kQM2IIlHSJYVFVELAR09k7B24z-51pbPbgmnopzTO3r4DR409rfZrCYwO0jix1x3b6gojxnug7pO9t5qc664RD4tkDtFml28OskRrleuAuj-AtljctcPUFcEJ5can2-82XPA7T5Pp0TGgP8Tdxl_BFZ42Zq3cnRzG40q4thDMPrItfX9CE_Vh-uhkqGJonU-rG8CFuFH_amyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالبياف:
يدرك الأمريكيون أن لا أحد سيصدق هراءهم؛ فأمريكا ليست في وضع اقتصادي يسمح لها بتقييد علاقاتها مع الدول الأخرى أكثر من ذلك.
‏أعلن شركاء إيران التجاريون، سواء في وسائل الإعلام أو من خلال إرسال رسائل إلينا، أنهم لا يعترفون بهذه التصريحات في أي مكان.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/88466" target="_blank">📅 20:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88465">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPEYw9aBJ6iCI8zdHJPmF1k6-yQ9W5ftjvLEjn2X4EZX9jz6HxzIyWNC5DI7palxvLSjz190CoUipXTteqOEy-0gJLNyXbYMwXTa1rBRGrNT0GZDFayybUS30zfvrSGiFmcKxv0WNpEE0cB_89gcoZZxcPPAtTmfk_Ad8wS4HRg-NJn4DmUvZHp2H6fy4Pc-c_6fJCOYtlliWNKECyMuSMmDOldzDHREZPHQckGu7h3NfXEVxqPJFvL8y0yJgRidoVSiIdhNqj6sOTH3Ndjo9yNBa4yceg4YzcHzu-Yq03EcnwpG4GhBUwV1oQxyO98gKnXO2mdJ4OXCdqbEpABWwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇸🇾
الولايات المتحدة تستعد لرفع تصنيف سوريا كدولة راعية للإرهاب بعد 47 عاماً، سوف تقوم إدارة ترامب بإلغاء التصنيف يوم الاثنين.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/88465" target="_blank">📅 20:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88464">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇱
🇮🇷
نتنياهو
: حاولت إيران اغتيال أحد أفراد عائلتي.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/88464" target="_blank">📅 19:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88463">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇺🇸
🇸🇾
الولايات المتحدة تستعد لرفع تصنيف سوريا كدولة راعية للإرهاب بعد 47 عاماً، سوف تقوم إدارة ترامب بإلغاء التصنيف يوم الاثنين.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/88463" target="_blank">📅 19:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88462">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88b5c9408c.mp4?token=LsQ23OJ2My72v7KNp7X8JuRrMp--5Gim9SXaeEvkeblTcoD63HxXYwdvDF3WULU07EPhHgoLUvKQTOyd6UF_N2qdxqYpuyv1Z_dfBwQ6xf_vjYfqOKKZU6m04QrxiOIvrYSwnd6NbS9On626RdQKOJSa9X9v1krkD3S7XxkmIVleYCEsDTqbedYa58fhDKuXjh0xUWTT_XPmdhSyF9i_Rxv53Jdeh6FNcu8uMk3bYCZucNWuRtV92__bv6tvnSvL4LefuQxUuVifftVB-_4SXxY3IWr2ofBdsQBAd19RPQWDywPdyyNO3k9C90-Tq5l2fOceealQ0-bpYlhGT8_lGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88b5c9408c.mp4?token=LsQ23OJ2My72v7KNp7X8JuRrMp--5Gim9SXaeEvkeblTcoD63HxXYwdvDF3WULU07EPhHgoLUvKQTOyd6UF_N2qdxqYpuyv1Z_dfBwQ6xf_vjYfqOKKZU6m04QrxiOIvrYSwnd6NbS9On626RdQKOJSa9X9v1krkD3S7XxkmIVleYCEsDTqbedYa58fhDKuXjh0xUWTT_XPmdhSyF9i_Rxv53Jdeh6FNcu8uMk3bYCZucNWuRtV92__bv6tvnSvL4LefuQxUuVifftVB-_4SXxY3IWr2ofBdsQBAd19RPQWDywPdyyNO3k9C90-Tq5l2fOceealQ0-bpYlhGT8_lGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏صور الاقمار الصناعية تظهر قيام القوات الأمريكية بزيادة عدد طائرات التزود بالوقود المتمركزة في الإمارات تدريجيا</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/88462" target="_blank">📅 19:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88461">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇮🇶
مجلس الوزراء العراقي يوافق على منح فرصة امتحانية واحدة لطلبة الثالث المتوسط والسادس الإعدادي (بفروعه كافة) الراسبين بما لا يزيد عن (4) مواد للعام الدراسي (2025- 2026)، على ان يؤدوا الامتحان ضمن دور خاص تحدد اللجنة الدائمة للامتحانات العامة موعده لاحقاً.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/88461" target="_blank">📅 19:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88460">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZ6fiulRTPcdDwvtIH-GRIVwXD2F08ekBqHCcu0_YukeXeraxIHzTVITB-IAtcBfH_m5dPaPFUCoTcMJzJpStrVVC779YZbiY1yQQeaQTof9PzsrDwoQ6kdTGxNsJIolEn4pgfWWQ7uBbLZN11RMiq92XLlVBnfSLAg4QruhTT3NOxkpvp7m_M6k7MBkOI10uK41fZenX7NYCUbF29f6YevBShah-GYduzyNsD6UamfQ3pQDpP4skN_iDWJmIiv6eirmr0svJcdN4VhNmcv9AL3mRqwr6nQ6Xl0rbl4dzgsK7Wqr7JAkxdgO1lUm5R_gdl53aVB4lyeTVNwnZixrog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
وزير الاتصالات العراقي مصطفى سند:
بعملية نوعية وبالتعاون مع جهاز الأمن الوطني، فككنا الآن واحدةً من أكبر الشبكات التي تُهرّب الإنترنت (المدمج) والفضائي غير الرسمي، وتعيد بيعه للمواطنين والشركات، وتمت مصادرة الأجهزة واعتقال مدير الشبكة الواقع مقرها في العاصمة بغداد (الأعظمية)، كما تم رصد شبكات أخرى سيتم تفكيكها واعتقال افرادها تباعاً.
وتتجاوز المبالغ المهدورة للانترنت المدموج والفضائي غير الرسمي، اكثر من 100 مليار دينار بالسنة.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/88460" target="_blank">📅 18:54 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88459">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇫🇷
الرئيس التنفيذي لشركة توتال إنيرجيز عن ارتفاع تكلفة الشحن:
نشتري براميل النفط من الخليج بسعر يتراوح بين 50 و60 دولارًا، بينما تضيف تكلفة شحن البرميل عبر ناقلات النفط العملاقة عبر مضيق هرمز حوالي 10 دولارات. وهذا يعني أن تكلفة الشحنة الواحدة تصل إلى حوالي 20 مليون دولار.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/88459" target="_blank">📅 18:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88458">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/88458" target="_blank">📅 18:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88457">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/88457" target="_blank">📅 18:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88456">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">الامين العام للامم المتحدة ‏غوتيريش: توقفت حركة النقل تقريبًا في مضيق هرمز.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/88456" target="_blank">📅 18:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88454">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇾🇪
🇾🇪
بيان مرتقب للقوات المسلحة اليمنية للإعلان عن عدد من العمليات العسكرية.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/88454" target="_blank">📅 17:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88452">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cgo_Q5yh0kL3NKO9QUvOAc-uoI-HOfoU8AFNqXewV12Mu5-bzemWOkWZfZkzOHMdyB7vAE2oBQGWVZLi1XeEC-nTRRzKZgUNhBigyE4C4duQFQScvh3X9Gwekm8ALVRl5KFBkyTQvTn3EGb-CbVVIO7ZtHojzCbM4HpR_VEdTgNHpA-4dG4NhX4ogoIccosksgJcmGl8Ro1gcdFUkfRKzQGKF8XSC3SHxQkP6doIyJdFpYE598BjhtsN8oh6IrcUWX8PLeDzZlIsO7s-SyqxrU1O_6vPx-Ebj10176nyjV6D6HeKB1lW4uXy6Pik0x97kik5GXadzZTzVjgTKt42tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lvnPE9DjlhzZKLDSgQGQ012f2QSDDhGyiwX8ZR3ZDczBlApIk8e0O1bONSFJlNhaACCyva_BsHhX8gDH2t_4oeI-oz3IhKelfnYo9RAwJVNDb_ZJOp4LRTaEfmhi_FnFwHGUyRGnQZdyt_ms_mnQ9KW86Vq5vkyLh0SvBUy9d2weGTsPZ3j8THFATADEJhWJDu6aaCLpX5TXcA_lVBYfbrchgKSOr89as7kbIVN5AIHeq4ipXcoNj6pwOfbIPdgTkt_HmAihcsL7sOwjWORG0IEmTBpvc_PlXRds-RC938DaAb02w_Z2C4bp3ZFD_Cuymz011RDQGb_pyclvoHLwbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بعد ضربات من أنصار الله في اليمن   مستودعات أسلحة العدو السعودي ومرتزقته تحترق في منفذ الوديعة.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/88452" target="_blank">📅 17:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88451">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ef5880eec.mp4?token=IydddNDInRLvjOfFtKWg7HmtYht1FgSq7fhwd9NFHDz5uxldceI4MUhIERpHYoeQ7zJSpOHbIcma5sc_otYiwY7VXlx_t3NqE_y30eBEdhGKXpogvjhYrkAjNbFqB9mXUR9jSD3Uw3y4v3YrbyyBFPcv4pzfdgQ2USVCh5OHCzouBh9DM_6shXaCPnGuNDMOOiucgQ2GZ2wfGD-7vrF0R0rBj8USopb3plPdKiA6lOyywyAvyYrh8AbuTnfbWZQbPQ5lPRD4kCGPLU2djzmMLT50yW-2zT6Bvz_DJUC0rBdkLdaHK0rPWo_Ej3wsvvzKskh0kmq12UStgqyggokNxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ef5880eec.mp4?token=IydddNDInRLvjOfFtKWg7HmtYht1FgSq7fhwd9NFHDz5uxldceI4MUhIERpHYoeQ7zJSpOHbIcma5sc_otYiwY7VXlx_t3NqE_y30eBEdhGKXpogvjhYrkAjNbFqB9mXUR9jSD3Uw3y4v3YrbyyBFPcv4pzfdgQ2USVCh5OHCzouBh9DM_6shXaCPnGuNDMOOiucgQ2GZ2wfGD-7vrF0R0rBj8USopb3plPdKiA6lOyywyAvyYrh8AbuTnfbWZQbPQ5lPRD4kCGPLU2djzmMLT50yW-2zT6Bvz_DJUC0rBdkLdaHK0rPWo_Ej3wsvvzKskh0kmq12UStgqyggokNxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد ضربات من أنصار الله في اليمن
مستودعات أسلحة العدو السعودي ومرتزقته تحترق في منفذ الوديعة.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/88451" target="_blank">📅 17:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88450">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y15Us6pvSGOOiSPrw08sCDQVaqUTMckkuSsxTWNTdSR7_fmoqDQtAPPI4lDKOSYVze8kz90XRIQ41i8mkhOe3crnpYmFJwOLD8rAmOasoKtKWrmPZR4qqv4HjMoeKksuvDO9i3BPQbXWNeYtTixKtuopvFARL6BjOPlHKYBtpT1ecqBJE4qhdYMKj00KY5JxnW6F8FIB_Yt6pJCFbC7E_qT0z77ojPRkkmvE52_6xVsD-YtzGV861EfBg4LDkGXvRsqoMZihYPIW-QF0JDUvhwZrGNpNtkGZ7hhnD4rEH52fOPWY6xPceG8VZBki8KdYn-lbTXNQQc4jF9SWs1gb9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب الترجمة بتصرف " كندا ٥٦ لسنوات طويلة وجانت ناصبة علينا "</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/88450" target="_blank">📅 17:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88449">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76c68e0f99.mp4?token=MtiN_wgRDsy2BcN69jbeW4lDQkA3jvMyvJgMtKyqntuIQypItXEwpl45BuBtg155TfUJnaqUbGKY5FWMUnXrgL19fns6SwTHDJfopVwTIFK10fKLCifSWgcN_mCPV3yrdnPDZEmuyqfFb5O9L5JoQwCCURTr-VYxVadjqQR02v-9FeSV0FhOksOX_y5aG4p1jsbpNII459K2Ir6USzrm6hUyfP6q84zoPSNCNF3hW2_LJcUv_W8bSHHsBOqHqOUuYJ_NBIR5nfoS-OFqMLlyHQ8uqiDAxyx3jIsKWL5-uI7I9tfAVUl1DqNJRWCu1-B28ey_94mB--E71wGFQponNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76c68e0f99.mp4?token=MtiN_wgRDsy2BcN69jbeW4lDQkA3jvMyvJgMtKyqntuIQypItXEwpl45BuBtg155TfUJnaqUbGKY5FWMUnXrgL19fns6SwTHDJfopVwTIFK10fKLCifSWgcN_mCPV3yrdnPDZEmuyqfFb5O9L5JoQwCCURTr-VYxVadjqQR02v-9FeSV0FhOksOX_y5aG4p1jsbpNII459K2Ir6USzrm6hUyfP6q84zoPSNCNF3hW2_LJcUv_W8bSHHsBOqHqOUuYJ_NBIR5nfoS-OFqMLlyHQ8uqiDAxyx3jIsKWL5-uI7I9tfAVUl1DqNJRWCu1-B28ey_94mB--E71wGFQponNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوة من فوج مغاوير الرابع تتجه نحو الجسر المعلق</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/88449" target="_blank">📅 16:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88448">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfc052bc00.mp4?token=FHtLaIOFQYBM772mQqnO59y6JPQQA7jHIffqrPd0sJCAEEYdmCib5_NkV5JGK0HYljCUECQf2DPgspD83xaMylWupcCheAILAA7U1NRCnSsw_qDfrTfyZ4CKd7KSgmHplV5blEh4FIsDUL3IGrMnilBfieNH88v7JHS3ES-5OzXv1HS1_TH9TJw4pHbEyPHo7ZGTUomKF1X8PwKptGu3Byan1b_m6nLUfiMzGgIikoytPXTOB7WKDBoQ3sEGSua2l6uEYHXJwls5ZIavdp4-SGoGyCBg2dm7XY4Pk2BMJbKGxzw7ufwZF4Y1qY9-AY7skcc5fXJTVbzVfjnnQcHMrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfc052bc00.mp4?token=FHtLaIOFQYBM772mQqnO59y6JPQQA7jHIffqrPd0sJCAEEYdmCib5_NkV5JGK0HYljCUECQf2DPgspD83xaMylWupcCheAILAA7U1NRCnSsw_qDfrTfyZ4CKd7KSgmHplV5blEh4FIsDUL3IGrMnilBfieNH88v7JHS3ES-5OzXv1HS1_TH9TJw4pHbEyPHo7ZGTUomKF1X8PwKptGu3Byan1b_m6nLUfiMzGgIikoytPXTOB7WKDBoQ3sEGSua2l6uEYHXJwls5ZIavdp4-SGoGyCBg2dm7XY4Pk2BMJbKGxzw7ufwZF4Y1qY9-AY7skcc5fXJTVbzVfjnnQcHMrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مصدر امني   انتشار قوات سوات الداخلية لاول مرة بالقرب من مداخل المنطقة الخضراء بالجادرية وطلب إسناد من الشرطة الاتحادية من جهة المسبح إلى فلكة الحسنين .</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/88448" target="_blank">📅 16:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88447">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇶
مصدر امني   انتشار قوات سوات الداخلية لاول مرة بالقرب من مداخل المنطقة الخضراء بالجادرية وطلب إسناد من الشرطة الاتحادية من جهة المسبح إلى فلكة الحسنين .</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/88447" target="_blank">📅 16:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88446">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مصدر امني يوضح لنايا   قطّع طريق مطار بغداد الدولي على خلفية زيارة قائد الجيش الألماني للعراق</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/88446" target="_blank">📅 16:38 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88445">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jbCvMKlcp7qgOuh_K4F3vAmq_nnetjhDxTplOSz78B8_njRZO_aaybR5-UlTqXqoGtmOc59tE0KXfDUvxsu6yoW4t2pnhrdUY6am3Zt3At2APCHMq-FhUeCe-lzPiOecxi_KMJk0kHvjnOf_mB778DWfn_J9dkSA_AvPvVRJUqwI-40IeVqOJEV5GM7W2uYC_8LwDOwkhX3R2SwNuV4NNrahDHBvwbF6UErmrySjBnNd1-wJUmFgWefFdYgQOoEtZWTHVFhH_UvQxfKyAhsmn0vuL4G-lBvItTH7ztLKhunzKW1WvaxnehHN3auhhg89mz8KeBDjTcXefY4JnY3l3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
القوات الامنية العراقية تضبط (428,794) قطعة من الأدوية البشرية المهربة وغير المفحوصة في العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/88445" target="_blank">📅 16:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88444">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔻
مناشدات عبر بوت نايا:
نناشد وزير التربية التفضل بالنظر بعين الأبوة والمسؤولية إلى ظروف طلبة السادس الإعدادي، والتوجيه نحو تأجيل امتحانات الدور الثاني، وأن يكون الامتحان موحدًا لطلبة الدور الثاني وطلبة الدخول الشامل.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/88444" target="_blank">📅 16:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88443">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8a39d0b36.mp4?token=M25n6sVSvlQCjQQwxjsrfvuvDdwuXqasJZ8cbCW19AJpcUSt8hN8DczxQu5frVstEIQgTf79_72medFjlJjHBNTcoN3pq_3Q3pVTwTHp_kC-HsWovRDHuBYkWK3FzaL8Ewil6wMc1Zuo0D7wGfKT7TgEOv8C-wBHcwWTaGUzU0Qbs32Xb_YduWaAIqkvzkzUkgndHWX2ydUwNFgGGFE621bVrhLVnn7YaLNDzx2jw6n6yjjbHRhKDIrx5RP_Ki--Cj5LgGgAwiTXRKOpzJlizfMpcyuakjDDnzmgAkXMeYfZTMbt6xwq7Xmb7S4s9CRvAUIdVqG7WN4xBBqmQ7JYGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8a39d0b36.mp4?token=M25n6sVSvlQCjQQwxjsrfvuvDdwuXqasJZ8cbCW19AJpcUSt8hN8DczxQu5frVstEIQgTf79_72medFjlJjHBNTcoN3pq_3Q3pVTwTHp_kC-HsWovRDHuBYkWK3FzaL8Ewil6wMc1Zuo0D7wGfKT7TgEOv8C-wBHcwWTaGUzU0Qbs32Xb_YduWaAIqkvzkzUkgndHWX2ydUwNFgGGFE621bVrhLVnn7YaLNDzx2jw6n6yjjbHRhKDIrx5RP_Ki--Cj5LgGgAwiTXRKOpzJlizfMpcyuakjDDnzmgAkXMeYfZTMbt6xwq7Xmb7S4s9CRvAUIdVqG7WN4xBBqmQ7JYGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مراقبون
اعتقال ابو جعفر التميمي دون الرجوع للمؤسسة الدستورية التي ينتمي لها ضرب للقانون العسكري ويندرج ضمن خطة توم باراك لاشعال الفتنة بين القوى الامنية واشعال الحرب الاهلية التي يتربص بها أعداء العراق …</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/88443" target="_blank">📅 16:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88442">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWnAHyEqaBKP-d95AR1CxxY0-iy5A9-P4QsUBq-kKI7-XpGdQ3g9O7uZ5t-Buk9J9MAP2noqdGVPwkQqd8b-rf9qzJovUkzJk5zufpjzEkfaQANQYrhaws7niVap9cFn0z3yWdXxQl4ykxqRnaeSbtDsoiQRQWZN3uSv-K3oQH2mjGUZYS5lw0S_cEUqHG2I6zIFVHaTLvpVHC6N7a1-aFb-JM4qA3xdIwm-ClP-neWuHIPiutCxJCBwa93OFh2Ggw2uflhT8f9_nsggCbump5MRkNZqMyOByYFPeT4RHFn6TPN19i9eLhtmkUczfiFP49m1dr9qo-bjE3cTOJd7Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب ايران تنهار</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/88442" target="_blank">📅 16:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88441">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">قطع طريق مطار بغداد الدولي لأسباب مجهولة</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/88441" target="_blank">📅 15:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88440">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">إغلاق ساحة الحسنين بمنطقة الجادرية وسط العاصمة بغداد</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/88440" target="_blank">📅 15:46 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88439">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇾🇪
🇾🇪
بيان مرتقب للقوات المسلحة اليمنية للإعلان عن عدد من العمليات العسكرية.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/88439" target="_blank">📅 15:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88438">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">غلق المنطقة الخضراء وسط بغداد من جهة المعلق وانتشار قوات مكافحة الشغب</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/88438" target="_blank">📅 15:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88437">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7PvVmlNbL3WJDViUVCB3JuSizxhswM2IB6qWdCg39zqjWHc19odkjfiyfoIslI2xRI2Y6vmYUJ81PQbJdP77t2rsfVtkiAe1c8wAjTIu7UuDTfq2AoKfGD3jcMIiCWXs8jT0MDQegslhORdRWw9PIwyDXFkFwhrkdF6n1AbnT3eor3pTEtpACM3NBp6KNXaMpHX-lQCKn54spukKVECrt7QXCaWTlyhCGTI-dmu9V3BFKjK689gKt8qciMIFY93WpP1zuo7p7eaDfCIFa1rFKkokmIGMgqAgaNtKcLXPfHK9edltBbWRPsMVtirtJi775lH4tVJJyakyW6ReYKA7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غلق المنطقة الخضراء وسط بغداد من جهة المعلق وانتشار قوات مكافحة الشغب</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/88437" target="_blank">📅 15:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88436">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‏
رئيس وكالة الطاقة الدولية:
قلق بشأن وضع الغاز في أوروبا هذا الشتاء بسبب انخفاض المخزونات، وانقطاع الإمدادات من الشرق الأوسط، ونهاية إمدادات الغاز الطبيعي المسال الروسي.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/88436" target="_blank">📅 15:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88435">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">انقطاع الكهرباء ‏عن منطقة مزارع العبدلي في الكويت بالكامل لاسباب غير معروفة</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/88435" target="_blank">📅 14:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88434">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q31us22E1uSacff3LOVLFsQ1DUZYiCLSYj79EDuD1E6DGu_EBqKmnfpR4C-vGkhmrbv51mPc7NvwIf1yWI6HkPXS1o4R5PHr6efzofINnO3N_RueV5YsSaPq6WanusvA8LM3FFGGnluvA2sApUJI4f4C6oQjrvrPeVrzzhudxlwB6keZ-6aCyXk-k9i0RGg3JjR3JxtL0FFAnDysVwnfBpg78djRtsvGoLL48m_mvfP1Mg08zrUSVeZHyJA6K_q6kmu4R8SqCEkRrjLXqUYFjWa5ARXhlRjVpX9XTLV5dBE4eSiOHcxRZv47UlMo7F4fM5SkB_kr1GRVREoozk-Hkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الكويت ليست بخير</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/88434" target="_blank">📅 14:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88433">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8v7XMOh84i3lXVkhCCR8b8IW1Y0pCm34hsJwOtJCxCXOQfLw4SGrTkeu1kA2DPQP53HRcsdo4DwR8I08R5bW0wz6IeIMbXlGxEBbS-6ybPr4HwE0fsncBYFRChsIr13QITL9d-22-uKq3j5s3Wpx-bEcqVLQLg--45qy1wsWTIoCkkprl3ffhq7OeYPnEPZOpmiR2AfdKFdWRv3KpMylGGjYyrohKoM_gFGdRpL8WM7yL5A6T9_DRUdPvRL6F7wKQZxDVjeC_ulXcHjmhSWYK2Z-EGInYhp9EUGR8J6G3tj00yAl7XY5ei4BfaovW8P5w5ZR4AFYr-NFOHaqChEeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاليباف:
‏لنجعل أمريكا جائعة مرة أخرى! ‏لا يمكنك التستر على الهزائم بادعاءات كاذبة.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/88433" target="_blank">📅 14:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88432">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQbcG4wUScfDVXQcI6gI4O3sQr3ysdpocddM2_Md5VIXhgT1Cw-MpnBoH2FWLzLBwNdnR7AUaGaCsbLjEYfZLVYqv1at8vZr3qCirC9bKHFHVQ4UTTBpza_mCmVDdSeTaHLSyp5lnVGrqAhaZSpeB92FhZKK09P3JmUdlKawACaC4gj-RP22sSWpjsqr86QK_bEP75bLzbvGFqomyr999sNz61SKfPbXDFtra1KrdpfLnx-OTTME2uLrHey9RwNIJWBn0o-C5jhAPMeqPj5_qBN-ynj2Aoz5a_7q1d5oVrxUnfCmk5atui2m2cdMVWnykD6Kf5a1c50nznOm-GYdNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدير مديرية الإعلام في هيئة الحشد الشعبي مهند العقابي:
جماهير الحشد الأحبة، تمت تسوية الالتباس الحاصل بشأن اعتقال الإخوة في الحشد، وتسليم الموقوفين إلى أبطال أمن الحشد الشعبي، لمتابعة ملفهم مع قضائنا العادل.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/88432" target="_blank">📅 14:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88431">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8b09c0dce.mp4?token=BzJd8nrO54ajW5_h1VoN3KdncwzBb6dxLXZqdEt1QIJ9S699IYl72fCR2ujnuBITsNCZ1GNb9ySmZv1X4tZqPNGmdrPDEf0VWtafEr3nFBIqp8RdaS8BLrggIQ5tYMCYSk-hKl1BEPCZGWWzO1VLRfKOHKSUrMBgXW674HS--J2YWvz5qcGnDIxEUGo4IpMr3TwUBDoA7YUeHuwzij2GL9-e5LgdzCM_Jyc2ygQMzGvXfwGr5GoZVdMP0QgByEHLbZVzsQwLsfglJXAAMfrTNtZ-ldHk9p-EWjiA9LjoVM0v6X4D42AYuavCPEFNovEv7HjEng9ppLuYJhWU9fMmbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8b09c0dce.mp4?token=BzJd8nrO54ajW5_h1VoN3KdncwzBb6dxLXZqdEt1QIJ9S699IYl72fCR2ujnuBITsNCZ1GNb9ySmZv1X4tZqPNGmdrPDEf0VWtafEr3nFBIqp8RdaS8BLrggIQ5tYMCYSk-hKl1BEPCZGWWzO1VLRfKOHKSUrMBgXW674HS--J2YWvz5qcGnDIxEUGo4IpMr3TwUBDoA7YUeHuwzij2GL9-e5LgdzCM_Jyc2ygQMzGvXfwGr5GoZVdMP0QgByEHLbZVzsQwLsfglJXAAMfrTNtZ-ldHk9p-EWjiA9LjoVM0v6X4D42AYuavCPEFNovEv7HjEng9ppLuYJhWU9fMmbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قطع طريق مطار بغداد الدولي لأسباب مجهولة</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/88431" target="_blank">📅 14:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88430">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b122a3fb40.mp4?token=XB_fE__RSOdCeizpXmzFvtJOCjLMIElDAF0ddFiUp1T407kH_O4soLAvL-pA8RGIsUy7DNOS-Y7xlHFqLoAD60NucbxJ0FEQXWNWZNeU_djMIgEES4ZDowJ0oONKGHRfX-o0dpoykmd3OEF4MqgAvQOv5xrrm8xYZSeBKR8kB4UcE8EV9sWzMHDHGZhH8-0FsYlPuJsUbY-Ewi2lY5SN16u3GEI365JOvKVCS1wXma4XDL6dv2mcZRa4G9czo5vwzliA6qdR5WzE7hfUesSl7RkweZnvLA8Rwx0MGbxRMvUF5Q6XGqSWNgdbjJvV5rV_xMau6fZv7k-_oo5S1Ez48g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b122a3fb40.mp4?token=XB_fE__RSOdCeizpXmzFvtJOCjLMIElDAF0ddFiUp1T407kH_O4soLAvL-pA8RGIsUy7DNOS-Y7xlHFqLoAD60NucbxJ0FEQXWNWZNeU_djMIgEES4ZDowJ0oONKGHRfX-o0dpoykmd3OEF4MqgAvQOv5xrrm8xYZSeBKR8kB4UcE8EV9sWzMHDHGZhH8-0FsYlPuJsUbY-Ewi2lY5SN16u3GEI365JOvKVCS1wXma4XDL6dv2mcZRa4G9czo5vwzliA6qdR5WzE7hfUesSl7RkweZnvLA8Rwx0MGbxRMvUF5Q6XGqSWNgdbjJvV5rV_xMau6fZv7k-_oo5S1Ez48g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماع دوي انفجار في مدينة تدمر السورية</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/88430" target="_blank">📅 13:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88429">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">سماع دوي انفجار في مدينة تدمر السورية</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/88429" target="_blank">📅 13:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88428">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dec4022a6a.mp4?token=Znia2SJlRDFlfASfVBJYsT64OiVDdFwft6hWG-80F0bnZAjesM__83NyOtQ0x2CvQ-cTAbOrTXQEcgem4JFwVyK8PYVgNSguIHtPJKK1cZulqLRs0h3HMu56fmHcI_vs9ad81Z9qAZrQ_yS4UVAl4yTm22viS0FD0o64la1ptVZSHchScjoOWamb25q-v7xZQEATaPAnjTwrnlT9hpYPT23F5m5J7teg7HarV6hoR6JbP10kAcvp-WyGxVjOgHQdLsV0za6Yizbj7mroZI3N5WeAUm44uRa-64P31mBMgwsY_-mtFTzOu5_aQd5kgWSyIwNUrB00qeeUjtUD5Ewj3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dec4022a6a.mp4?token=Znia2SJlRDFlfASfVBJYsT64OiVDdFwft6hWG-80F0bnZAjesM__83NyOtQ0x2CvQ-cTAbOrTXQEcgem4JFwVyK8PYVgNSguIHtPJKK1cZulqLRs0h3HMu56fmHcI_vs9ad81Z9qAZrQ_yS4UVAl4yTm22viS0FD0o64la1ptVZSHchScjoOWamb25q-v7xZQEATaPAnjTwrnlT9hpYPT23F5m5J7teg7HarV6hoR6JbP10kAcvp-WyGxVjOgHQdLsV0za6Yizbj7mroZI3N5WeAUm44uRa-64P31mBMgwsY_-mtFTzOu5_aQd5kgWSyIwNUrB00qeeUjtUD5Ewj3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحشيدات امنية كبرى داخل المنطقة الخضراء من قبل قوات مكافحة الشغب</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/88428" target="_blank">📅 13:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88427">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔻
إنفجار مجهول في قضاء كويا بمحافظة أربيل شمالي العراق ؛ إصابة 4 أشخاص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/88427" target="_blank">📅 12:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88426">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇷
هجوم مسلح من قبل عناصر إرهابية في مدينة زاهدان جنوب شرق إيران؛ إستشهاد منتسب كحصيلة أولية.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/88426" target="_blank">📅 12:35 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88425">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇮🇷
🇵🇰
وصل قائد الجيش الباكستاني "عاصم منير" إلى العاصمة الإيرانية طهران، للقاء المسؤولين الإيرانيين.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/88425" target="_blank">📅 12:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88424">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab1fc56eb9.mp4?token=UY1DaD661EjDR2Nznck2PzxjtnMGqKKXiIOLZYuwYHYH_5FIJ4pGh3SfJOioAllIjgtAEKKlj4pS8-QY1S_QbpdcUVLAEvp5IjnAl-v-n_SsGnHfX4EgbKWseiQP89cRs2gRzhN9tc5x_BXbtUCuP8KSgynrOB0tTT2Qdw8fqo55NY-k-fPrbaBGl9vUdI2zMhusOlkkES6gDbNsUSt9C6feAcGV9bzf8I4BnzlxR6gyvhv5ZgQGdfzgBuL14jJCQuEKsZVBEHumHOM9l4sJw2JjMKxpxur4-913zixdli4YWF2xK8ZkCjxw0LR9skl1fk_WlMtTZrQEjQGdlzStPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab1fc56eb9.mp4?token=UY1DaD661EjDR2Nznck2PzxjtnMGqKKXiIOLZYuwYHYH_5FIJ4pGh3SfJOioAllIjgtAEKKlj4pS8-QY1S_QbpdcUVLAEvp5IjnAl-v-n_SsGnHfX4EgbKWseiQP89cRs2gRzhN9tc5x_BXbtUCuP8KSgynrOB0tTT2Qdw8fqo55NY-k-fPrbaBGl9vUdI2zMhusOlkkES6gDbNsUSt9C6feAcGV9bzf8I4BnzlxR6gyvhv5ZgQGdfzgBuL14jJCQuEKsZVBEHumHOM9l4sJw2JjMKxpxur4-913zixdli4YWF2xK8ZkCjxw0LR9skl1fk_WlMtTZrQEjQGdlzStPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">على الرغم من اتفاق الإطار التنسيقي   بأن مذكرات القبض تنفذها مديرية الامن والانضباط بالحشد الشعبي في حال كون المعتقل منتسب ؛ قوة مجهولة تداهم مناطق شرق القناة وتعتقل الحاج ابو جعفر  و قوة اخرى تعتقل ثلاثة أشخاص من منطقة البلديات</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/88424" target="_blank">📅 11:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88423">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a5ed1dfe3.mp4?token=m33vMe_r0A96wPB41T9uUa7uh_QplwiYijVARxkhs18VwEipXgRoXLggHMKyLnoRIkdwh2b8IeWVYVycQjoSS8yqLP4pUrx8bXQqcCMYqTvs921DWV3nLhyq1EZ2skEjmRCJM9pspvNsm_m_pn-AtwRClnqU2Tfo2A-qeMLS6MJe7MB1cqQ4z7yYQymtJECQob8wSwC-EGyk0ItWYwckzilhnJCll9lAQUKoz7V5yR0P0-WM_SMZxJhO5JLlBpYnXdUiP_8wQWy5tN8fw9UCSR874ca8UHBnadE0MPmwRrls-mk0m8VvZNgmGf2gPpkiSCuUuYot1qvAvO2zWgyZWrF8vj-tfApCIRVBxCcGToaFnFZ8GVUoORMxoMfRmpeq5xDYM5mMxXBXHLbAXurkNmNoud7WRyz31_-kIhztnJsj5jQ0QSjhZxgycqmwdpH9NQc2U_atOlc10TlVfEet06eQBYZ8YBSmmFCewfNEpQ_lrKh3jIr-uwZ_Q_67OGxch3x8b4P115ItSlbfxUE71zo5DA_XSu_6y2Dthl6-Bw_EkZpp9x0p5eB9GTWeeJHDgHfgzXEQfkdwOe1jCjAxRNtnPGtjS0sRfA1tZ3CdomKD17NYQivk1YCj1yJdcN7wKb-QSeH0Cz3avgVA4UiGcxTBjU0nMWrLf5PWcS9L9Xc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a5ed1dfe3.mp4?token=m33vMe_r0A96wPB41T9uUa7uh_QplwiYijVARxkhs18VwEipXgRoXLggHMKyLnoRIkdwh2b8IeWVYVycQjoSS8yqLP4pUrx8bXQqcCMYqTvs921DWV3nLhyq1EZ2skEjmRCJM9pspvNsm_m_pn-AtwRClnqU2Tfo2A-qeMLS6MJe7MB1cqQ4z7yYQymtJECQob8wSwC-EGyk0ItWYwckzilhnJCll9lAQUKoz7V5yR0P0-WM_SMZxJhO5JLlBpYnXdUiP_8wQWy5tN8fw9UCSR874ca8UHBnadE0MPmwRrls-mk0m8VvZNgmGf2gPpkiSCuUuYot1qvAvO2zWgyZWrF8vj-tfApCIRVBxCcGToaFnFZ8GVUoORMxoMfRmpeq5xDYM5mMxXBXHLbAXurkNmNoud7WRyz31_-kIhztnJsj5jQ0QSjhZxgycqmwdpH9NQc2U_atOlc10TlVfEet06eQBYZ8YBSmmFCewfNEpQ_lrKh3jIr-uwZ_Q_67OGxch3x8b4P115ItSlbfxUE71zo5DA_XSu_6y2Dthl6-Bw_EkZpp9x0p5eB9GTWeeJHDgHfgzXEQfkdwOe1jCjAxRNtnPGtjS0sRfA1tZ3CdomKD17NYQivk1YCj1yJdcN7wKb-QSeH0Cz3avgVA4UiGcxTBjU0nMWrLf5PWcS9L9Xc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
محكمة الجنايات الرابعة بدمشق تحكم بالسجن المؤبد على مفتي الجمهورية السوري السابق الشيخ أحمد حسون.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/88423" target="_blank">📅 11:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88422">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">على الرغم من اتفاق الإطار التنسيقي   بأن مذكرات القبض تنفذها مديرية الامن والانضباط بالحشد الشعبي في حال كون المعتقل منتسب ؛ قوة مجهولة تداهم مناطق شرق القناة وتعتقل الحاج ابو جعفر  و قوة اخرى تعتقل ثلاثة أشخاص من منطقة البلديات</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/88422" target="_blank">📅 11:39 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88421">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f67556e45.mp4?token=bH1k0v-iUaBPiI9jUHNqqO6nVtlu7M6IWUkIyxntvgaBZSySVf_XDnpgX2FDOSUEP4OBdAftVdgXoqbQV1exDbAQ9mapG3AijlaxrBA6uXaqneNcBOL1cIGFltpwkmySudqt-pJ9LeqgCXa_eNEKvG8eAcBxrMsXEybNRpJkmrZhjRXo5j2h9kESNmD9kL_48Xyb94mXLk_Xds__V4T4ZLCQU5JuLccEigBbZ_LHmKtrmfq_aluNE2efLE9RVGCOq1T585Jn11I3USMqw2X8QD6Mq1x3OPtgZY1lfQtReQGyarEz-e886wGHgxpD6oA0sJrS-rYzavijxBpAx-BivA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f67556e45.mp4?token=bH1k0v-iUaBPiI9jUHNqqO6nVtlu7M6IWUkIyxntvgaBZSySVf_XDnpgX2FDOSUEP4OBdAftVdgXoqbQV1exDbAQ9mapG3AijlaxrBA6uXaqneNcBOL1cIGFltpwkmySudqt-pJ9LeqgCXa_eNEKvG8eAcBxrMsXEybNRpJkmrZhjRXo5j2h9kESNmD9kL_48Xyb94mXLk_Xds__V4T4ZLCQU5JuLccEigBbZ_LHmKtrmfq_aluNE2efLE9RVGCOq1T585Jn11I3USMqw2X8QD6Mq1x3OPtgZY1lfQtReQGyarEz-e886wGHgxpD6oA0sJrS-rYzavijxBpAx-BivA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
الخارجية الإيرانية:
أمن إيران والعراق مرتبط ببعض، ويجب أن تكون حدود هذين البلدين آمنة.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/88421" target="_blank">📅 11:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88420">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQVTbQ9nq1dvS60CPiFfCEGzeYncDGdSe8dYZYZqMEoDAPXr3u7ylhfWSiTm81eIgHdvmi8Ggtzy0D4f25dBTIUiT2itW2mVOvxx_bzzsFMQPloWTyICaN-8lS3TJ3mKrfOYo94lYu90HINCAZAZc80tglj9BOVGgbPiJdl-GqEmuruzrMiazB4XKrdF9JEk4Fk2Zy5bkKF1TXID0pYfs9UAv9uqhjA5N81bjrWiHfYIFqE0MEibnfR63G4aJZSoIlqF0flEEV0PaNm4Ynqi8SPM9A8jIHUg16gtcfMj8s9VUdadtiVcEkFICE3WlqFE-1EZ92iggsA7-n8e8iS0bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/88420" target="_blank">📅 11:14 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88419">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/88419" target="_blank">📅 11:14 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88418">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/253e1af33a.mp4?token=Ig31a44LZUCCyoe4do-pwtYJwkDi8WVutMha2BMOnARiAFRiyAhRQdfo9M2peM3pL9BP1UefHOJZPuOtS3F_5oIjSkKRVlpP0hIV4xPhOfwvCl7fCjRz7heBkUWy4IpjCFfJyG-jS4RrZT3-BOuS5Movpd6szOuMNzhMqS1AN35Z1KskcTB9pT12F7Qnm1gzI2CPnISergtXsJ4ODx-2QG64KtUFENe6bVIbTBVNF4ExpmcjE7RUuqqoLZ8jm11W2hikxIuStXsAa6irM6RFjux9-04MjMWKX-vk7a2cJX55-tD3F0BClyz30_mQok_W2ZxA0-jn0N4xQOjk0fAXXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/253e1af33a.mp4?token=Ig31a44LZUCCyoe4do-pwtYJwkDi8WVutMha2BMOnARiAFRiyAhRQdfo9M2peM3pL9BP1UefHOJZPuOtS3F_5oIjSkKRVlpP0hIV4xPhOfwvCl7fCjRz7heBkUWy4IpjCFfJyG-jS4RrZT3-BOuS5Movpd6szOuMNzhMqS1AN35Z1KskcTB9pT12F7Qnm1gzI2CPnISergtXsJ4ODx-2QG64KtUFENe6bVIbTBVNF4ExpmcjE7RUuqqoLZ8jm11W2hikxIuStXsAa6irM6RFjux9-04MjMWKX-vk7a2cJX55-tD3F0BClyz30_mQok_W2ZxA0-jn0N4xQOjk0fAXXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سقوط طائرة حربية تابعة للقوات الجوية الإندونيسية.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/88418" target="_blank">📅 11:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88417">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/By9E0LNWkXe4J126bED4QYr2CivNU0T38de-sKaTksD2nGi93o3vjoptHqKimWTJSQWNpJPuhtGkPfpBPlHoIZEbCPqdEFfNp8vDGjnA6YmOUGartuzMROyxTylmzAb-MYWEbDRX67MhE8HsnHWImt7-1yFxC91Go-50vavZg6woefxkwRm-7r9A8xj7XMkxe_890f_HiYE3HTDVDTj-Z2j-jTwNtsS_qC7cpR3izyIYKWZSRDlSGTLjDT_0eFMAIiawX9XIL4hDgVmND8gMe-m9XoEABbk8lmzh4z1LARUJ-AOecgY31tAjEYHAXwDXWQeEIhiCDrrTguylI1jwmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسقط وصاية توم باراك على العراق والشام</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/88417" target="_blank">📅 11:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88416">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9ba72a77c.mp4?token=OeSkFeX8Xj9U4Ux4SOOYTWn-kRd8Ga7Vn5-eCJ8R5XdF9JYWuT0DDup6uREGnlHS3tnFcOCMlhGqHZeajSeWkGx4VaIH2jnYnYh7YGJhKH9zjxKLdmPcNiVfoQYtUtHMQjqBr7Jd042IcruUQioiQ7Oy8p9IX4iQSlMaq8-0BNNhGGX6P3uTsic_AQEShOtWhttpXYZzdHMJWt0x0sIfEh-1rZoFcuENiL4DHlYKqsRW0CqPcLQJoy0M9I_Gb3PP2Vi7XVYKYsy2NVnYJb8jMn2AM47nk6gY5D74KjoEvrl3osauDgsFusnLzWPx_-xuYajCi1E4uSCPJkynNVuDqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9ba72a77c.mp4?token=OeSkFeX8Xj9U4Ux4SOOYTWn-kRd8Ga7Vn5-eCJ8R5XdF9JYWuT0DDup6uREGnlHS3tnFcOCMlhGqHZeajSeWkGx4VaIH2jnYnYh7YGJhKH9zjxKLdmPcNiVfoQYtUtHMQjqBr7Jd042IcruUQioiQ7Oy8p9IX4iQSlMaq8-0BNNhGGX6P3uTsic_AQEShOtWhttpXYZzdHMJWt0x0sIfEh-1rZoFcuENiL4DHlYKqsRW0CqPcLQJoy0M9I_Gb3PP2Vi7XVYKYsy2NVnYJb8jMn2AM47nk6gY5D74KjoEvrl3osauDgsFusnLzWPx_-xuYajCi1E4uSCPJkynNVuDqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
المتحدث بإسم عشيرة الهركي: لا نتائج إيجابية خلال الإجتماع مع وزارة الداخلية والأمور تتجه نحو التصعيد ضد قوات البيشمركة التي تستمر في إعتقال الزعيم خورشيد الهركي.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/88416" target="_blank">📅 10:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88415">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇷
القضاء الإيراني:
شحنة نفط أمريكية تم مصادرتها وبيعها لصالح مرضى "الفراشة الجلدي" بأمر من المحكمة الإيرانية.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/88415" target="_blank">📅 10:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88414">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lF5BcI2tlZkY8nBfCa_yYl0vVq1nxrEb09GjX9Tim_Q0j1PXlKFa-EnqglfEqWndRKu2HV38zTYGPyogjN3TJ1ZU7sHaJVCrCM4TtI1vAvE62GEnaDY46AF8rDz2kjzBGQW4fb2RGz4Jx2riuQPeBmFCzQgo0Wx1yg86PSJl_j_s9RswIkk2VSRbn8_0XHbvpqgadrjGbSGzFlMjdMjgbiQlSYP-3tmd0iKXrG4i_KeS2ZpQ-5LwJeeI68aQ0TOUBlX1lArRE16pzKqPsbA6n4lIryOugIuM8d-6JaAkX--c-gtXHhfFgnBEFuvwW1JAOm1KiyrmE70QIEVAXnyW7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">على الرغم من اتفاق الإطار التنسيقي   بأن مذكرات القبض تنفذها مديرية الامن والانضباط بالحشد الشعبي في حال كون المعتقل منتسب ؛ قوة مجهولة تداهم مناطق شرق القناة وتعتقل الحاج ابو جعفر  و قوة اخرى تعتقل ثلاثة أشخاص من منطقة البلديات</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/88414" target="_blank">📅 09:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88413">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocx58hsdIruiaPXa_KyvlqL3KnVov5IEl4WLl1iCdaUyRmshm6Ti6N4sQa2gasSfCdZLmhMEMCBDSSSHUfVbL_O5X3vZ2JubAKs_7LSgABSU7uTLm1GULCcrHv34uP_c3j1NMXescwX9-g5QlDjefYLj38QIEMchltiVE6MHRHNcVImqH7E4WLVs0h1E8Xc4QBa80H5QVywMOyJWItibUefPY6WRH-o69sm-AF6rHxBGFPqVVSfwQohjdbJZtYGz2z9oz5KAuyuqNRKremP9OPeZLaL_vjLCAmNChC3ZcvzLAQVsntHxUhcGraJKW3sewh4mvG48jSvRWlBvxXe93Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">على الرغم من اتفاق الإطار التنسيقي   بأن مذكرات القبض تنفذها مديرية الامن والانضباط بالحشد الشعبي في حال كون المعتقل منتسب ؛ قوة مجهولة تداهم مناطق شرق القناة وتعتقل الحاج ابو جعفر  و قوة اخرى تعتقل ثلاثة أشخاص من منطقة البلديات</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/88413" target="_blank">📅 09:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88412">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">رشقة صاروخية باتجاه السعودية الان من أنصار الله في اليمن</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/88412" target="_blank">📅 08:59 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88411">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/88411" target="_blank">📅 08:59 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88410">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">على الرغم من اتفاق الإطار التنسيقي
بأن مذكرات القبض تنفذها مديرية الامن والانضباط بالحشد الشعبي في حال كون المعتقل منتسب ؛ قوة مجهولة تداهم مناطق شرق القناة وتعتقل الحاج ابو جعفر  و قوة اخرى تعتقل ثلاثة أشخاص من منطقة البلديات</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/88410" target="_blank">📅 08:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88409">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نايا - NAYA
pinned «
كُلَّمَا أَوْقَدُوا نَارًا لِّلْحَرْبِ أَطْفَأَهَا اللَّهُ ۚ وَيَسْعَوْنَ فِي الْأَرْضِ فَسَادًا ۚ وَاللَّهُ لَا يُحِبُّ الْمُفْسِدِينَ
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/88409" target="_blank">📅 08:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88408">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">كُلَّمَا أَوْقَدُوا نَارًا لِّلْحَرْبِ أَطْفَأَهَا اللَّهُ ۚ وَيَسْعَوْنَ فِي الْأَرْضِ فَسَادًا ۚ وَاللَّهُ لَا يُحِبُّ الْمُفْسِدِينَ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/88408" target="_blank">📅 08:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88407">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac7120c31b.mp4?token=oqypcBZS9ijwO_yM-l2pFaGpByWjMwPo2CgsvyGOa2vyDLRHeXuDiHGAnF8bgIVkJJSiK4a5s_srnNcnQ5Z2WRZtoR_z5pCQVudhfGU0Nm89Uf7CJ5KTLXgWxRyyL5FxmNoTplf32dGkQ6rQUaeo0ScQ2NgQLjn9h6CPuJ5N-6VZGvz7NGzz3Kuh3rPBAtN0KSK1gdvoFowZ12y_zCE5gkXTzLPoHbueIWmnPx71b4Fn9gJLF82F-N7zMKa6ASBmoWFfa6NDDFzL_6-73cx_0_1ohFJL1wRkrRMU-p5LHPOJH037Qk9HLz6Bw9lFJpFD9XMVjsSSKl-n7hCAjL-mKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac7120c31b.mp4?token=oqypcBZS9ijwO_yM-l2pFaGpByWjMwPo2CgsvyGOa2vyDLRHeXuDiHGAnF8bgIVkJJSiK4a5s_srnNcnQ5Z2WRZtoR_z5pCQVudhfGU0Nm89Uf7CJ5KTLXgWxRyyL5FxmNoTplf32dGkQ6rQUaeo0ScQ2NgQLjn9h6CPuJ5N-6VZGvz7NGzz3Kuh3rPBAtN0KSK1gdvoFowZ12y_zCE5gkXTzLPoHbueIWmnPx71b4Fn9gJLF82F-N7zMKa6ASBmoWFfa6NDDFzL_6-73cx_0_1ohFJL1wRkrRMU-p5LHPOJH037Qk9HLz6Bw9lFJpFD9XMVjsSSKl-n7hCAjL-mKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/88407" target="_blank">📅 08:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88406">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔻
دوي إنفجار عنيف داخل أحد مقرات مرتزقة السعودية في مدينة عدن اليمنية.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/88406" target="_blank">📅 03:06 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88405">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">إطلاق نيران كثيفة صوب مصفاة لاناز في قضاء خبات بمحافظة أربيل.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/88405" target="_blank">📅 02:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88404">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqk9ruOFJttnpWXZz8xznky4JHmHZuHNGEWZCL5_jZuEoH3JRcryMClJbcEL2Q0F_sH1ikn_7ZA-Ow5NIH6FzCqd8_yBrQeNINkJpTuU5o08iCa1tQDHJjwPJ_LzFkIN8jtLNuikhAlDo_VyhHbo4GjcxZwDnyMAyClVWrFm6iszkaPGHe6PBg0hyEU7nDsuKADTxPnY8_ujgJwaPPmMS5MMUXDoYKiENDz-QTrQTyYvcavoRinsO2IOsw16_58Rzv21Wv2gAu3onQuM7FS7EC5kLA4uXMVEjIRrk7s2a6ngxlGREgRnlwCJQnZnWFfUaBhO0H23YKYoKfSfNtDfmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اربيل امن وامان</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/88404" target="_blank">📅 01:49 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88403">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4aa2b6b21.mp4?token=FlfDf05BP1ygnjmGW2CYxVSoHJ-fLNpXNRigGP72OyIiGb8QWa0HEmvoRrIm8tzsCJZFZb4dvIK8OzV6uh6z2GTOpjYpGDUXx_hLfPwsNQgd5WHp_EECZv2glfwIY9gZjFFxp7MD0H59HqDUMI1r2sDxlojteEjzMNFJ40YVpFvprMKHGXg8Rn4svy-052kg3wVQaAZdrYuNDx2bMpPMmdTmKeTVpc77rUV6vFofPxcfND9GrHoVcmZo9Xq-Iyfb8nUoPW75NOzQUC0k4PD-eT2ChLORB3udmcTO_PGTcmdb2VHbhHiwz0zqb-xHQJX7BcdXG2YAuNVnjBJUUReFxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4aa2b6b21.mp4?token=FlfDf05BP1ygnjmGW2CYxVSoHJ-fLNpXNRigGP72OyIiGb8QWa0HEmvoRrIm8tzsCJZFZb4dvIK8OzV6uh6z2GTOpjYpGDUXx_hLfPwsNQgd5WHp_EECZv2glfwIY9gZjFFxp7MD0H59HqDUMI1r2sDxlojteEjzMNFJ40YVpFvprMKHGXg8Rn4svy-052kg3wVQaAZdrYuNDx2bMpPMmdTmKeTVpc77rUV6vFofPxcfND9GrHoVcmZo9Xq-Iyfb8nUoPW75NOzQUC0k4PD-eT2ChLORB3udmcTO_PGTcmdb2VHbhHiwz0zqb-xHQJX7BcdXG2YAuNVnjBJUUReFxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العشرات من عشيرة الهركي يتوافدون الى منزل خورشيد الهركي لمواجهة قوات البيشمركة.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/88403" target="_blank">📅 01:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88402">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2921b037ec.mp4?token=hl3Lv8Tqy-62NouxMnS6W3TwwV9xjUPUqJubzxTiLGe306X1j9R0YQKOl535tAFuiC8mwkIX_SWI8cbfSh3DpKawY1g2rIZjz61KaE9Pwrk2d0YFeWCYvln_7Ek4RGMVGbO9dxdUgte7nRqztud1zPh9fkEmK5tVXQIbQEjd_YLI_117dY5AOGXa5LvFDjwBmN_mg4DvKdRQ8QFcASltmeaQT1dqjNGROHtrkt5NqD2EgDiujuJ_W_ISud-fEEPvmvVzqlOQrYlnqLeomDSBFZtsLUpecJYFXI18WPGIuQLa-oaVwTBJqnA1TAIRr2KZtRQYbwuDUlL5rqr9S4HkeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2921b037ec.mp4?token=hl3Lv8Tqy-62NouxMnS6W3TwwV9xjUPUqJubzxTiLGe306X1j9R0YQKOl535tAFuiC8mwkIX_SWI8cbfSh3DpKawY1g2rIZjz61KaE9Pwrk2d0YFeWCYvln_7Ek4RGMVGbO9dxdUgte7nRqztud1zPh9fkEmK5tVXQIbQEjd_YLI_117dY5AOGXa5LvFDjwBmN_mg4DvKdRQ8QFcASltmeaQT1dqjNGROHtrkt5NqD2EgDiujuJ_W_ISud-fEEPvmvVzqlOQrYlnqLeomDSBFZtsLUpecJYFXI18WPGIuQLa-oaVwTBJqnA1TAIRr2KZtRQYbwuDUlL5rqr9S4HkeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
وسائل إعلام كردية: خورشيد هركي أبلغ أبناء عشيرته ببدء المعركة ضد البيشمركة.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/88402" target="_blank">📅 01:46 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88400">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4ca1f3d6d.mp4?token=UNoNZx9RcWqanQygImei2xi7dlDf998RbzcSPnnxWPwt9JpCrD-zL3WfSDyN9Aimap4hTUBLgPhoVg5W3gonGICmPcJNY3AVPqdeYlc0JHryuieDg3DiY9bg9Z0zRqKx6B1Uu3FmawSn6239Y_tYkIlHfX5i4Qt9KheOI98oVrI-IJah7OXFrlIHyDPy9o9TIhhZO18JQ-Cah2IRTycHhIUnwcMpA_QjEs7QL6CeFn77Wx9v4bPfeI9i6d3O0JupDbCHqiBegCUclDn2x862RNAzFlBOmm6ZYUZlL3tbkAG3DnR1TuL_B7uQKsM8vuEOhOKrYVR2QwK8NytKHfNlyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4ca1f3d6d.mp4?token=UNoNZx9RcWqanQygImei2xi7dlDf998RbzcSPnnxWPwt9JpCrD-zL3WfSDyN9Aimap4hTUBLgPhoVg5W3gonGICmPcJNY3AVPqdeYlc0JHryuieDg3DiY9bg9Z0zRqKx6B1Uu3FmawSn6239Y_tYkIlHfX5i4Qt9KheOI98oVrI-IJah7OXFrlIHyDPy9o9TIhhZO18JQ-Cah2IRTycHhIUnwcMpA_QjEs7QL6CeFn77Wx9v4bPfeI9i6d3O0JupDbCHqiBegCUclDn2x862RNAzFlBOmm6ZYUZlL3tbkAG3DnR1TuL_B7uQKsM8vuEOhOKrYVR2QwK8NytKHfNlyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبادل إطلاق النار بين عشيرة الهركي ومليشيات البيشمركة في محيط مصفاة خبات بمحافظة أربيل</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/88400" target="_blank">📅 01:46 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88399">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df8833d650.mp4?token=Y-8lxp7Tat4Yt5J_5jiH-Fh0RLfFBXfTVZPghjjqaX16jW-ZRD94FDllxU9W37WcbalUa2Mo8oHnSSM3PBf7_XS9u3DrZ7nm5w1Xywb_R0C6fGs9BwQeXJPpcXX5n5LqGqtunaLb3IxItSO0YgFCJG_YPAL3vfJ-MVzys9QiBX_EmIMSx6LqPh9bqI6RMsTHbRDNMI_7hm0kZG9AFftCXwQq73V-jULY_bMXY1f2yDL_mY-7TWJRpw8xil-85AO32GgPQT3W0xF9Ahk5bgEHe1oW2x0tgV4mdNbTIThbCM5osQ0aiYzajWv7db-sDm0a4oG5N9kss2Y5G2yZ-ZZmqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df8833d650.mp4?token=Y-8lxp7Tat4Yt5J_5jiH-Fh0RLfFBXfTVZPghjjqaX16jW-ZRD94FDllxU9W37WcbalUa2Mo8oHnSSM3PBf7_XS9u3DrZ7nm5w1Xywb_R0C6fGs9BwQeXJPpcXX5n5LqGqtunaLb3IxItSO0YgFCJG_YPAL3vfJ-MVzys9QiBX_EmIMSx6LqPh9bqI6RMsTHbRDNMI_7hm0kZG9AFftCXwQq73V-jULY_bMXY1f2yDL_mY-7TWJRpw8xil-85AO32GgPQT3W0xF9Ahk5bgEHe1oW2x0tgV4mdNbTIThbCM5osQ0aiYzajWv7db-sDm0a4oG5N9kss2Y5G2yZ-ZZmqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلبية لدعوة خورشيد هركي.. مسلحين تابعين لعشيرة الهركي ينتشرون في محيط مصفاة خبات بمحافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/88399" target="_blank">📅 01:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88398">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4890b6251a.mp4?token=KZEacqlI0iaIy6-kvEw-qi_zO8iio2SvEmPQYuB7Qtf4vwFS_H5t30J_k-XAX0ZOUM4NEXLAcaW78FZppG9NFREJOx37M-z6reI0vHJDNgqvwpm5YY-djPVesa4-vDDqKshaeNmi-TLpqON9j0LNgbIDJlUzAnroXVyf-6ut4wuWSlBzKr3nphz6ArOmRn5z7y69sd4CNQmPpGpcQv57T-xk5R_WW1OVRB31qPOLIaC6lTkm6DJTBxnEu4ZmyR9EL0PXlsEpBxXJmWR-W88z-Y2T1HkeQtEfPXaFIgPGodnd9D_Kt93Tn23ksW-KEL2TRKX8z6CKUjZohWr9k0RPXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4890b6251a.mp4?token=KZEacqlI0iaIy6-kvEw-qi_zO8iio2SvEmPQYuB7Qtf4vwFS_H5t30J_k-XAX0ZOUM4NEXLAcaW78FZppG9NFREJOx37M-z6reI0vHJDNgqvwpm5YY-djPVesa4-vDDqKshaeNmi-TLpqON9j0LNgbIDJlUzAnroXVyf-6ut4wuWSlBzKr3nphz6ArOmRn5z7y69sd4CNQmPpGpcQv57T-xk5R_WW1OVRB31qPOLIaC6lTkm6DJTBxnEu4ZmyR9EL0PXlsEpBxXJmWR-W88z-Y2T1HkeQtEfPXaFIgPGodnd9D_Kt93Tn23ksW-KEL2TRKX8z6CKUjZohWr9k0RPXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
وسائل إعلام كردية: خورشيد هركي أبلغ أبناء عشيرته ببدء المعركة ضد البيشمركة.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/88398" target="_blank">📅 01:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88397">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇺🇸
وزير الخزانة الأمريكي:
أي عمل عسكري ضد قواتنا أو ضد دول الخليج سيرد عليه الرئيس ترمب بسرعة وحزم.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/88397" target="_blank">📅 01:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88396">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ارتال إضافية للبيشمركة تتحرك تجاه قضاء خبات بمحافظة أربيل</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/88396" target="_blank">📅 01:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88395">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/962b98f198.mp4?token=gC89kb8xrylr3uW2PF8DCphJOFfzvcWjc-h_mP1iApvOb2qQFkvMQvgVVL7XFpj2ezkrec2FgSweNNLCSgR4Ui6fDQMIFWJoCoLCdNH1yhXRr8TVNXFiMkAKSp1XPYMYJbwDBFVhKOLsbi4gd9jVQ9MphKyV6N60IE1GYJUBeQaq1DorjTwPze9PNe2nexzEaonOKHYb3raFb56nguKrGzZZiju4lTz04Bfvo-U4fCnlxvLkVFqeIFyCB0l2DxXT7nUwuAIKVdtNylnv3Ula2jtx_ZUNahPIfZVaj2rRJQIZbKCs-cCJbEGiZRNaoTTy5uJox9QaN0t3jtXaRCqFOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/962b98f198.mp4?token=gC89kb8xrylr3uW2PF8DCphJOFfzvcWjc-h_mP1iApvOb2qQFkvMQvgVVL7XFpj2ezkrec2FgSweNNLCSgR4Ui6fDQMIFWJoCoLCdNH1yhXRr8TVNXFiMkAKSp1XPYMYJbwDBFVhKOLsbi4gd9jVQ9MphKyV6N60IE1GYJUBeQaq1DorjTwPze9PNe2nexzEaonOKHYb3raFb56nguKrGzZZiju4lTz04Bfvo-U4fCnlxvLkVFqeIFyCB0l2DxXT7nUwuAIKVdtNylnv3Ula2jtx_ZUNahPIfZVaj2rRJQIZbKCs-cCJbEGiZRNaoTTy5uJox9QaN0t3jtXaRCqFOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تعزيزات عسكرية كبيرة للبيشمركة تتوجه نحو قضاء خبات بمحافظة أربيل لمواجهة عشيرة الهركي.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/88395" target="_blank">📅 01:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88394">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d46a0d3bee.mp4?token=Za0oKbK3nu_MEj2Vt9I4dum4ZOdnSxcUlqiYqNN4kLjQvtwrHEH8FKVQlN7N_REZF3PKbvjXHhgVo0dkjaM-nDpeMevnkG2q8-pT0UTC9BzdjkUbDbnnWHtgABjtRdEeXC2jK_VFMLTePa6R1ydwgZuFdVh_EiBE2t4vb4T2hPuzLoerX4WcF77GCICXEs7IfcJZCrsvOz_e-rAAgQJ9P_ymGFh3lQMJqyN2drmF-bgAwdIY13G-gn1kbvzsGJBQ5dkBjq5D7xITW0AQIkx4LimgLfuMbYlj5FRcOYLlEBNZSOHlIt02e5M0NnM0tHLpiohi3zDqbq5WLp_wTPvLJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d46a0d3bee.mp4?token=Za0oKbK3nu_MEj2Vt9I4dum4ZOdnSxcUlqiYqNN4kLjQvtwrHEH8FKVQlN7N_REZF3PKbvjXHhgVo0dkjaM-nDpeMevnkG2q8-pT0UTC9BzdjkUbDbnnWHtgABjtRdEeXC2jK_VFMLTePa6R1ydwgZuFdVh_EiBE2t4vb4T2hPuzLoerX4WcF77GCICXEs7IfcJZCrsvOz_e-rAAgQJ9P_ymGFh3lQMJqyN2drmF-bgAwdIY13G-gn1kbvzsGJBQ5dkBjq5D7xITW0AQIkx4LimgLfuMbYlj5FRcOYLlEBNZSOHlIt02e5M0NnM0tHLpiohi3zDqbq5WLp_wTPvLJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشتباكات عنيفة وتعزيزات عسكرية من كلا الطرفين تتجه صوب قضاء خبات.  البيشمركة حاليا: السيطرة تحت الوضع
😆</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/88394" target="_blank">📅 01:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88393">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d3d19f9e5.mp4?token=AG-ZMnMH4I7ysuqnxxTLqaMrmbQf89U-Z1gVkZJPc8w1tjC7FNHWcouVjRE5imEPL2_Mx1Zuz-ozEDhclUYBXq0ln3vP2PmplZ3cSY83GrbOW9FgcPzsOMKBL94cfMAKVcKEGTsA-jrmecg4JFtzQYe5ilwh6Vfe5Cb-ut4ko3ul9ZPMkipsHb_OaWR0rJkWcQHhS90zgq1aY6ZeJogJ4dSLXiKi_cxzM8N-ncZZPnV3lycw7S1e_HZP47YZwAZYClR8z18AKWNHBeb7csXnm9FHvrtq7wUBA7_pLI8-uFI3WuXgmya2SssBHagLPY-NP7HHC5baGpNxjbFx6emasA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d3d19f9e5.mp4?token=AG-ZMnMH4I7ysuqnxxTLqaMrmbQf89U-Z1gVkZJPc8w1tjC7FNHWcouVjRE5imEPL2_Mx1Zuz-ozEDhclUYBXq0ln3vP2PmplZ3cSY83GrbOW9FgcPzsOMKBL94cfMAKVcKEGTsA-jrmecg4JFtzQYe5ilwh6Vfe5Cb-ut4ko3ul9ZPMkipsHb_OaWR0rJkWcQHhS90zgq1aY6ZeJogJ4dSLXiKi_cxzM8N-ncZZPnV3lycw7S1e_HZP47YZwAZYClR8z18AKWNHBeb7csXnm9FHvrtq7wUBA7_pLI8-uFI3WuXgmya2SssBHagLPY-NP7HHC5baGpNxjbFx6emasA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خروج مسلح كثيف لقبيلة الهركية مع غلق معظم الطرقات المركزية في محافظة اربيل.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/88393" target="_blank">📅 01:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88392">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45f58106d3.mp4?token=f2YkwHxyPDMHjiyCskdnrbepIXdEfOAt68iUlRTYpDlig6ecfmd4HIYC-ayBzdeyJaIK4NAhtUuCwWXzLulUQY4a575-hXLRJs137PjdMUWBvFrVAb_5fkZNLjzD3-PPMudzWoQvqDV1G0tX6ujsy4QnQ1vdbehaG8N_UaQ1RZaaP_76rPCe8pOlxN42LeTfxwkcCRoJaHcujFdWq55qyOM-CqJkhTl-_s_iwq3EjLJZg8rJhl6dbZjbmiFu-hARPoLhUa0xVAm_5DA9ehApoHIQ6ys0fp3BspEG3t2ypU3DTBEquvMluQ1ZeiidzSLoMLDFJO0O6_Sy2KBlkJTtcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45f58106d3.mp4?token=f2YkwHxyPDMHjiyCskdnrbepIXdEfOAt68iUlRTYpDlig6ecfmd4HIYC-ayBzdeyJaIK4NAhtUuCwWXzLulUQY4a575-hXLRJs137PjdMUWBvFrVAb_5fkZNLjzD3-PPMudzWoQvqDV1G0tX6ujsy4QnQ1vdbehaG8N_UaQ1RZaaP_76rPCe8pOlxN42LeTfxwkcCRoJaHcujFdWq55qyOM-CqJkhTl-_s_iwq3EjLJZg8rJhl6dbZjbmiFu-hARPoLhUa0xVAm_5DA9ehApoHIQ6ys0fp3BspEG3t2ypU3DTBEquvMluQ1ZeiidzSLoMLDFJO0O6_Sy2KBlkJTtcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
عبر نايا   مراقبون أمنيون يتسألون عن دور مدير مكتب القائد العام للقوات المسلحة العراقية الفريق الركن الأول عبد الأمير الشمري والمشروع المكلف به   بنزع السلاح و ان كان يشمل هذا الأمر ايضا اقليم كردستان العراق وسط حالة سقوط المدينة وخروجها عن السيطرة الامنية…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/88392" target="_blank">📅 01:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88391">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇮🇶
عبر نايا
مراقبون أمنيون يتسألون عن دور مدير مكتب القائد العام للقوات المسلحة العراقية الفريق الركن الأول عبد الأمير الشمري والمشروع المكلف به
بنزع السلاح و ان كان يشمل هذا الأمر ايضا اقليم كردستان العراق وسط حالة سقوط المدينة وخروجها عن السيطرة الامنية . ام ان الأمر منوط فقط بسلاح وسط وجنوب العراق .
نعم لحصر السلاح المنفلت</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/88391" target="_blank">📅 01:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88390">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60bdb6ffa4.mp4?token=t9kwDLfiiyOcfQigKOEoHs4fVct8eU5YgMpVXwKqq4lfjCwly4nGe2IJYDWSdgZZKbI0YoRrfkyqHHxcVelvN1EqpEQH2-NqZUgIUXzy0LdXWtVaytGK3iXCz2DOMhLAeRTGRCyWy9voEN4WCD1P6ndwH29YUwBU3B2feKpbrRED1TepZPXK0c6eBzxAsMOVqZY0dHmJO-HApDcfGkOTG-PdqfQ2t67ZFV9kJsn9uyzX92869q8DTxh9HXYEJU90Rmpur5Ia0unn95IglMfuhsrL7HutZqGIUKeeVzMc2ZVe4QkaBO01gf1kARSuYrZT4eHwUEp-dvGC7XLDSyFaOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60bdb6ffa4.mp4?token=t9kwDLfiiyOcfQigKOEoHs4fVct8eU5YgMpVXwKqq4lfjCwly4nGe2IJYDWSdgZZKbI0YoRrfkyqHHxcVelvN1EqpEQH2-NqZUgIUXzy0LdXWtVaytGK3iXCz2DOMhLAeRTGRCyWy9voEN4WCD1P6ndwH29YUwBU3B2feKpbrRED1TepZPXK0c6eBzxAsMOVqZY0dHmJO-HApDcfGkOTG-PdqfQ2t67ZFV9kJsn9uyzX92869q8DTxh9HXYEJU90Rmpur5Ia0unn95IglMfuhsrL7HutZqGIUKeeVzMc2ZVe4QkaBO01gf1kARSuYrZT4eHwUEp-dvGC7XLDSyFaOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
تستمر تحشيدات الهركية في قضاء خبات استعدادا لمواجهات اكبر مع البيشمركة.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/88390" target="_blank">📅 01:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88389">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20747c723a.mp4?token=YKjMp1lMglIikocIJcOfqEHLBtHxTtnvBBs_OBGbu2vrp5HYoQJH45C8ConQKhIboIjRFJwk0lEutUQaNRwm8fn_JylPyFFPFcU5UlsZb4aoXIivM_9Mxv6OOUIVwJf6PnCG8rBGO1PQMH640lhbtQqp1wWrSTHv7IRFVdqFBOW0fXYJf-citB6UaTInjMkQUTH6TdOkTWtWxeq0Le_BQzbF8D5hZCQ1zvkrcyqexuprLWhCnvTxSckfXhIM8fVceQQAgE0gZCflbo2AherE74YKm3gNSztzz-ALRXFzdaidaKpcmyHOHFq_uyo3TE-yCV4Wm7ozgaeSN77e-uyWDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20747c723a.mp4?token=YKjMp1lMglIikocIJcOfqEHLBtHxTtnvBBs_OBGbu2vrp5HYoQJH45C8ConQKhIboIjRFJwk0lEutUQaNRwm8fn_JylPyFFPFcU5UlsZb4aoXIivM_9Mxv6OOUIVwJf6PnCG8rBGO1PQMH640lhbtQqp1wWrSTHv7IRFVdqFBOW0fXYJf-citB6UaTInjMkQUTH6TdOkTWtWxeq0Le_BQzbF8D5hZCQ1zvkrcyqexuprLWhCnvTxSckfXhIM8fVceQQAgE0gZCflbo2AherE74YKm3gNSztzz-ALRXFzdaidaKpcmyHOHFq_uyo3TE-yCV4Wm7ozgaeSN77e-uyWDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
لمن يتساءل عن أسباب الانفلات الحاصل حالياً في محافظة أربيل... تعود خلفياته إلى خلافات بين زعيم قبيلة الهركية في قضاء خبات والحزب الديمقراطي الكردستاني.  وكان زعيم القبيلة قد انضم إلى حزب بارزاني، إلا أن خلافات نشبت بين الطرفين لاحقاً ما دفعه إلى الانسحاب…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/88389" target="_blank">📅 00:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88388">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">انفلات امني في محافظة اربيل شمالي العراق بسبب اعتقال خورشيد هركي وعدم الافراج عنه.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/88388" target="_blank">📅 00:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88387">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11d4806f03.mp4?token=lrHqkzoyPxEkd-Fgig6jndG-5f3Q5oJe04XnoZlS88GWvbq2ssoORqsQdmx4RPC-RjxU1EiXB0tuRL76VO3XbYjz_PLyQnM0QW5w1FSWnjy8aNVqqQyJqb_Njx8m6bQMWMerh-hW0Cm9jOIjs1TqmhhHPjCJ8X_u1mq-ul7bdy345t53TG1tg5nR05mjAwujudSdls6q1fRcv5q3orppjHCWaOY43L6mymZEYWyJgOzPlqEmyunXlIj3-OcivYhtNQeJiAL5NEK7FLd52BQj2lnlfeOgB1NgWc6S3juNO2SlGpLGpr3MUNNWk5AI1aZp7dxyu-XYyXmzLA37dgF-bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11d4806f03.mp4?token=lrHqkzoyPxEkd-Fgig6jndG-5f3Q5oJe04XnoZlS88GWvbq2ssoORqsQdmx4RPC-RjxU1EiXB0tuRL76VO3XbYjz_PLyQnM0QW5w1FSWnjy8aNVqqQyJqb_Njx8m6bQMWMerh-hW0Cm9jOIjs1TqmhhHPjCJ8X_u1mq-ul7bdy345t53TG1tg5nR05mjAwujudSdls6q1fRcv5q3orppjHCWaOY43L6mymZEYWyJgOzPlqEmyunXlIj3-OcivYhtNQeJiAL5NEK7FLd52BQj2lnlfeOgB1NgWc6S3juNO2SlGpLGpr3MUNNWk5AI1aZp7dxyu-XYyXmzLA37dgF-bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
بمختلف انواع الاسلحة المتوسطة والخفيفة تبدأ مواجهات بين الهركية والبيشمركة بمحافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/88387" target="_blank">📅 00:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88386">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3162c91ec2.mp4?token=d0RsFglXocGExtq-NSnXBUscvDgsEpIWVGG6_MkFQGqZpNZOk6KwLoIO0t41RSzeUp9Vd58HoorOpjDFh4QET1f59-YbFqdE1iKLu1Lu6bRoIdeaUcdyerWSKQLPb2gJ5kuFW_U9y8Yyk_mv_43Jbm4PKZvK7AEhWoFq3fNA1oKo_6PRQbO7bvs_KJN_-57r9tg7ZESjlZnAtu5YB8KJCKfU_u7P1iK7N6_nqbw_Q3TeoHTlw3EVts-z2Ie2gIdQOuVGX0Kcm4yyqippkCZlBRWNIbZxPBRVPTVbLEbf_LiHqoxMqLZQ1w8VnJG9d_q7PuLxyAhpNBXou5qctOPjiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3162c91ec2.mp4?token=d0RsFglXocGExtq-NSnXBUscvDgsEpIWVGG6_MkFQGqZpNZOk6KwLoIO0t41RSzeUp9Vd58HoorOpjDFh4QET1f59-YbFqdE1iKLu1Lu6bRoIdeaUcdyerWSKQLPb2gJ5kuFW_U9y8Yyk_mv_43Jbm4PKZvK7AEhWoFq3fNA1oKo_6PRQbO7bvs_KJN_-57r9tg7ZESjlZnAtu5YB8KJCKfU_u7P1iK7N6_nqbw_Q3TeoHTlw3EVts-z2Ie2gIdQOuVGX0Kcm4yyqippkCZlBRWNIbZxPBRVPTVbLEbf_LiHqoxMqLZQ1w8VnJG9d_q7PuLxyAhpNBXou5qctOPjiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
البيشمركة ترسل تعزيزات عسكرية ضخمه لصد الجماعات المسلحة التابعة لخورشيد هركي.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/88386" target="_blank">📅 00:46 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88385">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21ef949d38.mp4?token=XRJKRKmdr4CrJylqDKkfPwVwPiQXkpygabeIFsMxFGWI6Hvtge4rbXFzTcviZfw1D7eg299REmVD_hT37SYpTR7poB-d-XOn1s6nMTaaUilNcal0_z1lZq5hKr_xRj-nhxrH16SLZobgEP622dooD9INyssafz_0CwjLIWp10ZLCjtj33UsTKV9dJEt4vH0u0JgcuDIe_IwNsqFtHU7hMR1hcewdGUA6DzzIAM5Adz-IX9PuN8Tg_tixzqvRrWDUyn-sjV6aU324h3IEO-OHAOs1g-cYYcwJqf4QxY3yZJcWKMl4HWegIaL1pBje0lqT7FoZxhN512ZjikuGX9vefA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21ef949d38.mp4?token=XRJKRKmdr4CrJylqDKkfPwVwPiQXkpygabeIFsMxFGWI6Hvtge4rbXFzTcviZfw1D7eg299REmVD_hT37SYpTR7poB-d-XOn1s6nMTaaUilNcal0_z1lZq5hKr_xRj-nhxrH16SLZobgEP622dooD9INyssafz_0CwjLIWp10ZLCjtj33UsTKV9dJEt4vH0u0JgcuDIe_IwNsqFtHU7hMR1hcewdGUA6DzzIAM5Adz-IX9PuN8Tg_tixzqvRrWDUyn-sjV6aU324h3IEO-OHAOs1g-cYYcwJqf4QxY3yZJcWKMl4HWegIaL1pBje0lqT7FoZxhN512ZjikuGX9vefA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشتباكات عنيفة تدور بين الهركية والبيشمركة</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/88385" target="_blank">📅 00:45 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88384">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇮🇶
تحشيدات عسكرية ضخمه تابعة للبيشمركة تتجه لقضاء خبات لمواجهة الهركية.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/88384" target="_blank">📅 00:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88383">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba261dcac7.mp4?token=jpYxly32kENQIucgu3iL2m4awkrFhyooF3cNshcxrtlBPWcu-VOg6PNg-Dz2hEvQInULeO52Q7wqkQzi_J2xODVBMxNL8W-D1sd01YIH1lkni0KIWOVbZdr2MGESsytTr8oXXhExvrKnmTf5fK0xYLWKNWxKdztXFqwHXDDxsZWdWc8_iCzmqAqFQBvidgHwK6haUmDOnCOdkUNWvJ4Zn5zj8aNu_7THnsFgFogd0DQHbKUOOsiI-bvEbqo12jco0JwBUT-CtnT8vwordk2TUezinRA8aR1fX8CwE_VBschEx1vp_6GagaTK7mKzIjklBQ-J_E3WIRhcOD9Dk7R2cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba261dcac7.mp4?token=jpYxly32kENQIucgu3iL2m4awkrFhyooF3cNshcxrtlBPWcu-VOg6PNg-Dz2hEvQInULeO52Q7wqkQzi_J2xODVBMxNL8W-D1sd01YIH1lkni0KIWOVbZdr2MGESsytTr8oXXhExvrKnmTf5fK0xYLWKNWxKdztXFqwHXDDxsZWdWc8_iCzmqAqFQBvidgHwK6haUmDOnCOdkUNWvJ4Zn5zj8aNu_7THnsFgFogd0DQHbKUOOsiI-bvEbqo12jco0JwBUT-CtnT8vwordk2TUezinRA8aR1fX8CwE_VBschEx1vp_6GagaTK7mKzIjklBQ-J_E3WIRhcOD9Dk7R2cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
البيشمركة ترسل تعزيزات عسكرية ضخمه لصد الجماعات المسلحة التابعة لخورشيد هركي.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/88383" target="_blank">📅 00:43 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88382">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/083ed6f065.mp4?token=eCdpdWVnYnssOCuuXwXIU2qs6-nQeomufFxpfvnzjkJaedF43WNr20avuXQ09U_690u3-Vru0ZnEE_dO_butsEd8NwT5x95zoAIEhsd5I5JiR9U8DGR_Pe1K9WhHev3VkbH6ess-PGCTAbpE2Migx0WLc7OY5jrLWuhijwHikZeGH-FxCeyt8nE0kx2NUS5IzMQgvP89xj4gS9mDaN8JNdxYCFkp3px4gxJ0_uKnWpk2r1jSszBjraq-jEnie7YQtbtp4VGbsedohx49LRWh3BJ5lnKguEUp5XCX6FYTtWCMlyqGbwDx0sX7OxvgVQ4zalE-4IOHKqh-trXuHjt8vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/083ed6f065.mp4?token=eCdpdWVnYnssOCuuXwXIU2qs6-nQeomufFxpfvnzjkJaedF43WNr20avuXQ09U_690u3-Vru0ZnEE_dO_butsEd8NwT5x95zoAIEhsd5I5JiR9U8DGR_Pe1K9WhHev3VkbH6ess-PGCTAbpE2Migx0WLc7OY5jrLWuhijwHikZeGH-FxCeyt8nE0kx2NUS5IzMQgvP89xj4gS9mDaN8JNdxYCFkp3px4gxJ0_uKnWpk2r1jSszBjraq-jEnie7YQtbtp4VGbsedohx49LRWh3BJ5lnKguEUp5XCX6FYTtWCMlyqGbwDx0sX7OxvgVQ4zalE-4IOHKqh-trXuHjt8vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
الجماعات المسلحة تحتشد لمواجهات اكثر عنفا مع البيشمركة بعد انتهاء مهلة اطلاق سراح زعيمهم خورشيد هركي.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/88382" target="_blank">📅 00:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88381">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇮🇶
الجماعات المسلحة تحتشد لمواجهات اكثر عنفا مع البيشمركة بعد انتهاء مهلة اطلاق سراح زعيمهم خورشيد هركي.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/88381" target="_blank">📅 00:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88380">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a3a009d53.mp4?token=msZL6XuIX_PmczzFoY6PAzQ6vsCG0PIj7ElAtbSePhyulExHeED99SDCiwcc4zGeBzAxyoEY5RwqX-nejHVDlCeMyfGFfK391GH9EhDjZrsTcWv0bpSl0BGiuFEqS8LjOksI2Gk63Xbdz292-EraiTX6R7ftSiVzdoCV4FXH-24AEOAKMElhosIg9m_kPNpoLrS5TT7ILrJX929tXRCta-sqpRtKRSRzPj4upU1oSB31oAjVmo-5EdKg5OfVG7lahMiIDBN0OuLpLoprIlwHsO-Mua1riLzqYOm2ZjBRJdwf80LComeRl-I8f54-kgAYyjN4qP427nNAhXVmqaZrYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a3a009d53.mp4?token=msZL6XuIX_PmczzFoY6PAzQ6vsCG0PIj7ElAtbSePhyulExHeED99SDCiwcc4zGeBzAxyoEY5RwqX-nejHVDlCeMyfGFfK391GH9EhDjZrsTcWv0bpSl0BGiuFEqS8LjOksI2Gk63Xbdz292-EraiTX6R7ftSiVzdoCV4FXH-24AEOAKMElhosIg9m_kPNpoLrS5TT7ILrJX929tXRCta-sqpRtKRSRzPj4upU1oSB31oAjVmo-5EdKg5OfVG7lahMiIDBN0OuLpLoprIlwHsO-Mua1riLzqYOm2ZjBRJdwf80LComeRl-I8f54-kgAYyjN4qP427nNAhXVmqaZrYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
الجماعات المسلحة تحتشد لمواجهات اكثر عنفا مع البيشمركة بعد انتهاء مهلة اطلاق سراح زعيمهم خورشيد هركي.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/88380" target="_blank">📅 00:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88377">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46e7020797.mp4?token=adFziu-ciuV-E46x_-7xp12DatzW5ap1Ek3ME4IUWLqdaEeEVTzpPPj6BesuVpJg9Jif5tugO_RAs46me4DjLN2WklIhR-bsByeIsZcHNIivojahXyicGuUzQduyvM9s-OACFtp5tm0ZPEkEAzDkEysHm5QYV7O2RRUeP1MRtAND8yHbgnWWpFpEn6xCyKUn3JnaHh23q_N5Wov92Kp5zMoiFkZgCoaY6Vdn8zZma7yPw8mAoCHOpo4RxqXHC1WdSx6-P4BNt1LgDnzjIt3FegoFnLDYGmkfkuZ1FSR8vnLkkHSyyioWDOp1m0WG_l2ZUSwU7ASDfYdjvuOvUDctvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46e7020797.mp4?token=adFziu-ciuV-E46x_-7xp12DatzW5ap1Ek3ME4IUWLqdaEeEVTzpPPj6BesuVpJg9Jif5tugO_RAs46me4DjLN2WklIhR-bsByeIsZcHNIivojahXyicGuUzQduyvM9s-OACFtp5tm0ZPEkEAzDkEysHm5QYV7O2RRUeP1MRtAND8yHbgnWWpFpEn6xCyKUn3JnaHh23q_N5Wov92Kp5zMoiFkZgCoaY6Vdn8zZma7yPw8mAoCHOpo4RxqXHC1WdSx6-P4BNt1LgDnzjIt3FegoFnLDYGmkfkuZ1FSR8vnLkkHSyyioWDOp1m0WG_l2ZUSwU7ASDfYdjvuOvUDctvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اطلاق نار كثيف في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/88377" target="_blank">📅 00:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88376">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇹🇷
🇮🇱
🇸🇾
اجتماع وزير الخارجية السوري مع مدير "الموساد" الإسرائيلي لخص إلى تشكيل لجنة أمنية سورية تركية إسرائيلية لمعالجة المشاكل وتفادي أي صدام.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/88376" target="_blank">📅 00:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88375">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇦🇪
الإعلام الأوروبي:
حذّر مسؤولون إماراتيون من أن "نتيجة سلبية" بشأن التحقيق الجاري مع نادي مانشستر سيتي لكرة القدم المملوك(منصور ال نهيان) بتهمة انتهاك القواعد المالية للدوري الإنجليزي الممتاز "قد تضر بالعلاقات المحسّنة مع المملكة المتحدة.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/88375" target="_blank">📅 23:35 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88374">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e86b62545.mp4?token=D2dzMkd9GYKtUlUu7__r1tGiFdpK3i9nQgV63ucUAcHID__o-TVpik5QJ69eBo15hJ0JmmXmhIdOU2barK8rodZCTnvbMjqIhT6IwFRxyexKq7e-tSB5L4CIVOqA0K8q2w0MBNoOo9Qb8c1Pe3APeWsY-nR6ETa_NrST9MBjq0tHHOrzM-zkEvVF0peX7WkCDbhKLp8S_HUezWUYQENUp-D5uyVspbJBMWZYYlIliGNeEqJHlDqHthdox_2AidY3VocBc5v_8LY4Eq66-xMVK8uZYp8LK0OA5dOUSx1HJleHZVWoiCr3kePiH4GetbVb4I94jatFa7jQCrR8uCdaWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e86b62545.mp4?token=D2dzMkd9GYKtUlUu7__r1tGiFdpK3i9nQgV63ucUAcHID__o-TVpik5QJ69eBo15hJ0JmmXmhIdOU2barK8rodZCTnvbMjqIhT6IwFRxyexKq7e-tSB5L4CIVOqA0K8q2w0MBNoOo9Qb8c1Pe3APeWsY-nR6ETa_NrST9MBjq0tHHOrzM-zkEvVF0peX7WkCDbhKLp8S_HUezWUYQENUp-D5uyVspbJBMWZYYlIliGNeEqJHlDqHthdox_2AidY3VocBc5v_8LY4Eq66-xMVK8uZYp8LK0OA5dOUSx1HJleHZVWoiCr3kePiH4GetbVb4I94jatFa7jQCrR8uCdaWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
تسريب غاز سام في حقل خباز النفطي بئر رقم 46 في محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/88374" target="_blank">📅 23:23 · 01 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

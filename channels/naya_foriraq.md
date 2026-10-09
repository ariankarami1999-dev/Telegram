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
<img src="https://cdn4.telesco.pe/file/jqvikChziGgJF6MY_8xrfTdZWR78TfJ0GHJJzzSievrrH-2gF5pi9fvZiQK33FHU5woUv_goWzVOoEyPL7qaK8YvyuJHwu6doO_qbh5NsPppMbzf_pJRHYUJbJIGu4sJGipqzqs5PJms5TzKMIMynza3ILIPgVoT8WFHRpTXJBbYsh1MJ145Y8QUGm1GysarTQFiD0ATWE4TJnLaG5t221ySSDLKqgyrz0sInzfqSvCyswFN65UAJKQZjXnNXRCcDltCI-iUAzGJC7U_EaxV9L67QtjXFVbpu0TLDFKClF9ma6zcu7VW_LR0Kn_-i-x0HHZ7vRAeaC6onbVwyOGj7Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 264K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 18:54:21</div>
<hr>

<div class="tg-post" id="msg-93099">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇺🇸
الولايات المتحدة تفرض عقوبات على المحكمة الجنائية الدولية.</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/naya_foriraq/93099" target="_blank">📅 18:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93098">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcd2029e25.mp4?token=dYzW1pAH_N95eOpy7r6twzcMESS3LQtgUlMEuEyeU45KOkmIyswd_Gh7-fxjN1fr2UQYjjrX4mht7aegChsSyKhXKzilzJOyaUUcvrwAFdg8tTunciDLLHzQpka4Xf3XjkbSRT194eMnEIMgK2BweJGfYBeNLPskPDlogMEpJDg-xQ2uBX8a6f1vIuEdIvQU2CrpyLgKH2aV76AF9aLSQNKmHkkJy_FXt7I2CnhRPI88usWquq0ZG5-o7wnxd5WkhmvxpGDcCfpfZp9RTXIKVimtbKrmlinVQ5pwW7r7UBnkVOjWTwWx89B2k-lZgm6a25vo-FfFSsLzyRuFTHf0H155k3rosWCPDgU9pVfhDRbiaffMaQ-AUgcSD-axWQr2q86LAxW_AOU9dSJy4pYLcYbEITcuDkrQVc0PtSm1SDPvcfjXc88px0ADPEnvsczDuhlkpZo1emUKd4rNfVUlnr1YN1bdEXL7qhAo2jdy7t9kMQCAnqendvxPpJ7AfeR30_Wl-j90NI-ZaDH8qj0hqM0_XiKOZ5ZGFHEuhDrxhZYmSuzOjSS8h4AFnnB4To9gjIM7jG-nQstpIHogMMutvZb2Vs95Z76h6yZtL4QIsrJH00VZzw2qC2mdLXI1flyHDgk8R7zO8poGiGqtOUvmBUzpYxHL8wEfGSwnxvuoOIc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcd2029e25.mp4?token=dYzW1pAH_N95eOpy7r6twzcMESS3LQtgUlMEuEyeU45KOkmIyswd_Gh7-fxjN1fr2UQYjjrX4mht7aegChsSyKhXKzilzJOyaUUcvrwAFdg8tTunciDLLHzQpka4Xf3XjkbSRT194eMnEIMgK2BweJGfYBeNLPskPDlogMEpJDg-xQ2uBX8a6f1vIuEdIvQU2CrpyLgKH2aV76AF9aLSQNKmHkkJy_FXt7I2CnhRPI88usWquq0ZG5-o7wnxd5WkhmvxpGDcCfpfZp9RTXIKVimtbKrmlinVQ5pwW7r7UBnkVOjWTwWx89B2k-lZgm6a25vo-FfFSsLzyRuFTHf0H155k3rosWCPDgU9pVfhDRbiaffMaQ-AUgcSD-axWQr2q86LAxW_AOU9dSJy4pYLcYbEITcuDkrQVc0PtSm1SDPvcfjXc88px0ADPEnvsczDuhlkpZo1emUKd4rNfVUlnr1YN1bdEXL7qhAo2jdy7t9kMQCAnqendvxPpJ7AfeR30_Wl-j90NI-ZaDH8qj0hqM0_XiKOZ5ZGFHEuhDrxhZYmSuzOjSS8h4AFnnB4To9gjIM7jG-nQstpIHogMMutvZb2Vs95Z76h6yZtL4QIsrJH00VZzw2qC2mdLXI1flyHDgk8R7zO8poGiGqtOUvmBUzpYxHL8wEfGSwnxvuoOIc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية في مضيق باب المندب بعد الف اعلان سعودي حول السيطرة على المضيق</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/naya_foriraq/93098" target="_blank">📅 18:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93097">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e52c72fd4d.mp4?token=J-P8MpwnCK9hA_w1c1RzCOyx74EqpsuWcs87nn3BVtqfdslHWyMn8MqqrIehmR1NwyHimTY0ZKfi64yc2_XUIDWpB1S8iawcHktRpr8eq5fJxa59I9Oo_T3cb6wS1Cbe7RYpslLRG8oWPnS1BKskK2l6bWNevQpHwXKCrG5UC8OoamrdUvim-N6mbZLO65eAfA9e3FWi7sqxFnap-iJOaaBzlphWllQbS3YeCfJD-lU14eqoxCTfbDnaCFWvtmpqSNkybP-UnRBY5qPJI5ifkvrP9qXjoAcbkmk41g_2WiM2MTVxZyWU695g-su_QW5eolY2oCbAA9fwCsCQrf73FjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e52c72fd4d.mp4?token=J-P8MpwnCK9hA_w1c1RzCOyx74EqpsuWcs87nn3BVtqfdslHWyMn8MqqrIehmR1NwyHimTY0ZKfi64yc2_XUIDWpB1S8iawcHktRpr8eq5fJxa59I9Oo_T3cb6wS1Cbe7RYpslLRG8oWPnS1BKskK2l6bWNevQpHwXKCrG5UC8OoamrdUvim-N6mbZLO65eAfA9e3FWi7sqxFnap-iJOaaBzlphWllQbS3YeCfJD-lU14eqoxCTfbDnaCFWvtmpqSNkybP-UnRBY5qPJI5ifkvrP9qXjoAcbkmk41g_2WiM2MTVxZyWU695g-su_QW5eolY2oCbAA9fwCsCQrf73FjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اندلاع اشتباكات عنيفة في شوارع الحسكة بين عصابات الجولاني وميليشيات قسد</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/naya_foriraq/93097" target="_blank">📅 18:14 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93096">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bbc462dbd.mp4?token=q_rqUA3o0-IgcXZYPQApFadv3fLWQVj9mPM--JQkp3q2tBrTQX0AqhdeXCk5J7P36HP6F9D4s7tO83SVzVCB9oRBihNk3tylOe3gkSoyNwRAlvFg_WOiB0a9beY8mT7FLdqUTR5Avws8LCmgElXldd3yimwWEIshn9IT5wSY_o7mtG6oJmyp9DlBz3L_RRALMYnaurjlBDrbVps6IHkX31iMpYRJ6rA7yU0xmW5WhjR0Ubc_yL2dTxdkuoVG5WOXaXKVHRMYun0XpD_gIrjB82b5i_eRGDkQ6rQjH5Rys5aeD8GKHrZpJd6wCpOyR5ri7_h1jXgcvzDZUJoSIYyYO5GuaU2gr03T6bTEQgkyG1lHcuhzrjNtutE9uwsgJegD3vP8E23LPhjnqVoZeQRiusYFMZrdHbsv01HF9XkLxRs1K2ybl7lHIpQJrxz7dAzi1UDjkJYrg1SvQB-pnCLDYjq7R4_FAxvm7gr8dCu-yUD48wzFJYGgzcWHj2TbMy-LGhmGVp-P-lgc3G_ZTW4Dl9C53vL9yvL886GPF5-ptE57dEPcdfeVYGRfPofD-8zMlHIvMqdyDggsix76z6OJvmClmwqAQe7ItKUM4-uq9D3RaoryrpnydCGyixIfecYAeq28ly7aKqxUJNgeufM98rVLv4XHm4MrsNuL8QzgHec" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bbc462dbd.mp4?token=q_rqUA3o0-IgcXZYPQApFadv3fLWQVj9mPM--JQkp3q2tBrTQX0AqhdeXCk5J7P36HP6F9D4s7tO83SVzVCB9oRBihNk3tylOe3gkSoyNwRAlvFg_WOiB0a9beY8mT7FLdqUTR5Avws8LCmgElXldd3yimwWEIshn9IT5wSY_o7mtG6oJmyp9DlBz3L_RRALMYnaurjlBDrbVps6IHkX31iMpYRJ6rA7yU0xmW5WhjR0Ubc_yL2dTxdkuoVG5WOXaXKVHRMYun0XpD_gIrjB82b5i_eRGDkQ6rQjH5Rys5aeD8GKHrZpJd6wCpOyR5ri7_h1jXgcvzDZUJoSIYyYO5GuaU2gr03T6bTEQgkyG1lHcuhzrjNtutE9uwsgJegD3vP8E23LPhjnqVoZeQRiusYFMZrdHbsv01HF9XkLxRs1K2ybl7lHIpQJrxz7dAzi1UDjkJYrg1SvQB-pnCLDYjq7R4_FAxvm7gr8dCu-yUD48wzFJYGgzcWHj2TbMy-LGhmGVp-P-lgc3G_ZTW4Dl9C53vL9yvL886GPF5-ptE57dEPcdfeVYGRfPofD-8zMlHIvMqdyDggsix76z6OJvmClmwqAQe7ItKUM4-uq9D3RaoryrpnydCGyixIfecYAeq28ly7aKqxUJNgeufM98rVLv4XHm4MrsNuL8QzgHec" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشتباكات بين عصابات الجولاني وميليشيات قسد في محافظة الحسكة السورية</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/naya_foriraq/93096" target="_blank">📅 18:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93095">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇺🇸
الولايات المتحدة تفرض عقوبات على المحكمة الجنائية الدولية.</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/naya_foriraq/93095" target="_blank">📅 18:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93094">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية:
تمكنت قواتنا المسلحة بفضل الله وعونه وتأييده _وللمرة الثانية خلال ساعات_ من التصدي وطرد التحشيدات التابعة للعدو السعودي التى حاولت التقدم من جهة لحج باتجاه باب المندب ولم تحرز أي تقدم بفضل الله، وتم استهدافها بعدد كبير من الصواريخ الباليستية و الإسناد المدفعي وبالأسلحة الثقيلة وتدمير أكثر من 22 مدرعة ومصرع وإصابة العشرات بينهم عدد من القادة
ووصول أكثر من 30 سيارة إسعاف إلى عدن تنقل القتلى والجرحى من تحشيدات العدو السعودي.</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/naya_foriraq/93094" target="_blank">📅 18:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93093">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">استهداف تجمعات الجيش السعودي في مطار عدن</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/naya_foriraq/93093" target="_blank">📅 17:57 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93092">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f7828e24c.mp4?token=cbSB7heTuIpbV6qd_TdIuQ33jbVq_Z4YyNNeos33vHWqoMfMlTD6sm3q9uWzeCorF40DhW2NQVKwU9nsIP5JH_4b9A06lNsIj8xPWQ8ENKUcPv_u43yykGGMOdb9hcBVARNP9qfSD3CHDcOEgZ1srt5YpfGzEYoWiY-w1qVpukeaIA8Sdl9qcT_cg3tsyfpdKSJJGQAN4dRoZKH1MJPmOzwz62vC90A2ReCymnsGj3fAVtl8enWd5aVYMc1bT7mZ4MsTV7RQSFbk7OWgjD5eBwXFr8UxU-S-_DKg02EwjkHlK7Y9mwElgDtQH1XmWRm5qUecZWz3lIh2fPsvr4UxXn5-9GaX7EsFdSykQucAdObp2SAtbfBfDYEZGCAFFyhb8BcNq96TI2Z17iKweibr_9XLjJkp8oFCo0RJu8FYew5k6EPiXGl7wC4z6rqx66DoiJva_wfMDY-mnwkQt86Aa0rsXOHmE5drpHW7QBqJRw4HLpRt0n9XjGqDzITVBRTq51DVFrievklsyKQjuaeCAqzC9MBJfWSK3XCI7aBzfsVqG4Ak9IdvPo7BakZ2QG_yE2R0d5vPiVTY9qjXg-iIr8zjIPPC42s01OTvviJTxw9b1mwZw95vB7YK_bVB-moCYEi1ZOc7-TsxFv6bHvlzpowSWJaGjEYdKojsiK3Llm4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f7828e24c.mp4?token=cbSB7heTuIpbV6qd_TdIuQ33jbVq_Z4YyNNeos33vHWqoMfMlTD6sm3q9uWzeCorF40DhW2NQVKwU9nsIP5JH_4b9A06lNsIj8xPWQ8ENKUcPv_u43yykGGMOdb9hcBVARNP9qfSD3CHDcOEgZ1srt5YpfGzEYoWiY-w1qVpukeaIA8Sdl9qcT_cg3tsyfpdKSJJGQAN4dRoZKH1MJPmOzwz62vC90A2ReCymnsGj3fAVtl8enWd5aVYMc1bT7mZ4MsTV7RQSFbk7OWgjD5eBwXFr8UxU-S-_DKg02EwjkHlK7Y9mwElgDtQH1XmWRm5qUecZWz3lIh2fPsvr4UxXn5-9GaX7EsFdSykQucAdObp2SAtbfBfDYEZGCAFFyhb8BcNq96TI2Z17iKweibr_9XLjJkp8oFCo0RJu8FYew5k6EPiXGl7wC4z6rqx66DoiJva_wfMDY-mnwkQt86Aa0rsXOHmE5drpHW7QBqJRw4HLpRt0n9XjGqDzITVBRTq51DVFrievklsyKQjuaeCAqzC9MBJfWSK3XCI7aBzfsVqG4Ak9IdvPo7BakZ2QG_yE2R0d5vPiVTY9qjXg-iIr8zjIPPC42s01OTvviJTxw9b1mwZw95vB7YK_bVB-moCYEi1ZOc7-TsxFv6bHvlzpowSWJaGjEYdKojsiK3Llm4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇾🇪
شعار الصرخة يهز جبهة الاقروض مع تصاعد حدة الاشتباكات بين القوات المسلحة اليمنية ومرتزقة السعودية.</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/naya_foriraq/93092" target="_blank">📅 17:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93091">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">القوات المسلحة اليمنية تدك مطار عدن</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/naya_foriraq/93091" target="_blank">📅 17:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93090">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">القوات المسلحة اليمنية تدك مطار عدن</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/naya_foriraq/93090" target="_blank">📅 17:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93089">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7c3880c04.mp4?token=BHPhS-cnG38rkIpfsauv1CcJik1F3ee2-Yw2iSYf25i4fbxO9uPdG07w-38GbKLZVh5SjXn8ozIrxa1s6I5wcbk7pVlo30xueeXGciy1SAHMT4_k8C_Uw2zkK4ynPfJReGta5qv_jxjVpC1P9eF7M7uYgxH4t3R4VlxLWmzEhNiuoCOBQy-O1olJy6pVLXDFO9IuDcU4BYzZ6eNGpBVSqJfsf3DGkV3g3MjvscAOgqRMRwWeEdjALM56kJSFcHXJaYMxTRDak4RnjBMtqUUfzPblkmZsI_HcyOZTNLinWv5o-SyAnKn2cGH42aX4gJ4108XK8_qc6x-yW3GC059sGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7c3880c04.mp4?token=BHPhS-cnG38rkIpfsauv1CcJik1F3ee2-Yw2iSYf25i4fbxO9uPdG07w-38GbKLZVh5SjXn8ozIrxa1s6I5wcbk7pVlo30xueeXGciy1SAHMT4_k8C_Uw2zkK4ynPfJReGta5qv_jxjVpC1P9eF7M7uYgxH4t3R4VlxLWmzEhNiuoCOBQy-O1olJy6pVLXDFO9IuDcU4BYzZ6eNGpBVSqJfsf3DGkV3g3MjvscAOgqRMRwWeEdjALM56kJSFcHXJaYMxTRDak4RnjBMtqUUfzPblkmZsI_HcyOZTNLinWv5o-SyAnKn2cGH42aX4gJ4108XK8_qc6x-yW3GC059sGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇾🇪
شعار الصرخة يهز جبهة الاقروض مع تصاعد حدة الاشتباكات بين القوات المسلحة اليمنية ومرتزقة السعودية.</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/naya_foriraq/93089" target="_blank">📅 17:53 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93088">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3629a87b.mp4?token=h4M7Cg3tCQEb-3nxu4-ePdgB6v0prw3ZZve26cSwofC3ACI5dodd4GYEj2hK07nBtg13w9m_OnoXDLlymMfZzyV8BtNoCSy3M-aoHQH-yz-2IukYuW2iiGqEL99gFM0-3O7qY5-2BgBaPnKvrKJ-KQMt5tlaAyYCV3o7-GN02gyOcTHIngwyNb-50Bljq6yrJo0RZpWMZysf3ST68cO0biREsGc0Ouvd2qs2OazQOT12mPKFAdXY16jovW0zV62uRms2u9OcUbJnX_lAuXHpDvqMAXeXvvMvsP9Eq9lOhK65hE8r0NpIi9G6Odf9L9BWCngs2i972SxnIhrqENw7Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3629a87b.mp4?token=h4M7Cg3tCQEb-3nxu4-ePdgB6v0prw3ZZve26cSwofC3ACI5dodd4GYEj2hK07nBtg13w9m_OnoXDLlymMfZzyV8BtNoCSy3M-aoHQH-yz-2IukYuW2iiGqEL99gFM0-3O7qY5-2BgBaPnKvrKJ-KQMt5tlaAyYCV3o7-GN02gyOcTHIngwyNb-50Bljq6yrJo0RZpWMZysf3ST68cO0biREsGc0Ouvd2qs2OazQOT12mPKFAdXY16jovW0zV62uRms2u9OcUbJnX_lAuXHpDvqMAXeXvvMvsP9Eq9lOhK65hE8r0NpIi9G6Odf9L9BWCngs2i972SxnIhrqENw7Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاعد اعمدة الدخان من محافظة السليمانية في شمال العراق لاسباب غير معروفة</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/naya_foriraq/93088" target="_blank">📅 17:49 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93087">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4386405697.mp4?token=SmIyA7jkXGz6rJMrEFh51kvABjt1wJ5GQFyYB1dESEOPJWgQL_pXTMg6YvLC0gtaiphtlXKF9zpIPoKQcvO6qdVpqJySmEkv3QEnxjOyjEVkOLQDY7LBTHJbUAJkOd0KmLph4Xo1U45n9Ua48K40dMx8ehQs6Gmt3n2IE7_6-RB75onVLCTEo9Sa_bjXaAbfcZvTFexJBQJKQ4pvYi8cY0JpHh04t7kKFREC1zQGxzD7xICdXFbRGBfC6Yei6zPooBViCOWrSJbyumGr2eobZ_vCgram5klRdaU2iIO9rTvRK_XIZqMJEspeYRYwtYrbld8vP4Z-MzrlVb8p9-ScHCJS9EwsNcUlJ_vkapetXKLlI6xUyYI9kMyHCmGMCF2YeCQAb_q9ZGhuCgeNhqyg4NFNbBLyPHNL8pGxj3u20YUBiBCpJt2jchhBwEC76_qnDe1wr3Hp3iqeZ4CqbxEv9iTCjHexDHEDY5BIW9OdUqvORoV4A-FG38txOt_hOWLfdjLI6YeQ_0kCF0SDRMmhaDa8k_JOHnv5hHcX414DVZ9s2krRRWun2xlswiWVrDWgd4lbJUMryE-GWOZ3f6haGkTwy4-VxbL2KPrmeFzKDHTeFIpms80ZlHvggbRlzjv-hqhtU8liYDyOcFESI3RCrR5CC8U9g8vyY5BNODx8Cck" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4386405697.mp4?token=SmIyA7jkXGz6rJMrEFh51kvABjt1wJ5GQFyYB1dESEOPJWgQL_pXTMg6YvLC0gtaiphtlXKF9zpIPoKQcvO6qdVpqJySmEkv3QEnxjOyjEVkOLQDY7LBTHJbUAJkOd0KmLph4Xo1U45n9Ua48K40dMx8ehQs6Gmt3n2IE7_6-RB75onVLCTEo9Sa_bjXaAbfcZvTFexJBQJKQ4pvYi8cY0JpHh04t7kKFREC1zQGxzD7xICdXFbRGBfC6Yei6zPooBViCOWrSJbyumGr2eobZ_vCgram5klRdaU2iIO9rTvRK_XIZqMJEspeYRYwtYrbld8vP4Z-MzrlVb8p9-ScHCJS9EwsNcUlJ_vkapetXKLlI6xUyYI9kMyHCmGMCF2YeCQAb_q9ZGhuCgeNhqyg4NFNbBLyPHNL8pGxj3u20YUBiBCpJt2jchhBwEC76_qnDe1wr3Hp3iqeZ4CqbxEv9iTCjHexDHEDY5BIW9OdUqvORoV4A-FG38txOt_hOWLfdjLI6YeQ_0kCF0SDRMmhaDa8k_JOHnv5hHcX414DVZ9s2krRRWun2xlswiWVrDWgd4lbJUMryE-GWOZ3f6haGkTwy4-VxbL2KPrmeFzKDHTeFIpms80ZlHvggbRlzjv-hqhtU8liYDyOcFESI3RCrR5CC8U9g8vyY5BNODx8Cck" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من العدوان السعودي على صنعاء</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/naya_foriraq/93087" target="_blank">📅 17:29 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93086">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9ad45a45d.mp4?token=uLoo-YieStt9aUha3MxX7DCvWfpjXGNToyDwsJYKRFjiuiJ77N1WzJq3Tx8gPTzS6w-pJ6RU2nXe5cTvzDNeAkcbrIylngf-TXjchJCXDr_-WGXwLolg3AmHhP8ZCbPoSaX7QF09sIwLSbfwNAnM9qcBLQhXTsCAuL6pjwphPl6mAsgprENz71fmwar9PeTNRoX7YVSFyHju1rTm3YVYqEXp4RxRIB3isv95HsEoDyjsOdkTsguDuFBbFRYJUMAP2RWvFI96aOefI3GpjKMQJrM16kU91zgmgzu0Tis83NcXnqwlOZqVaMPzPPx1_W_vKwNjKU5Md1wWr13y7sWDBDqKrgnY9E_IQtOFc8WPuarZf2GsWPWjWV3EnVzkrly4zwIjx39jp-lE33gj9mLXdIvx39NXeZSo534P42yCtmTBIqwg2ssPXU9_k7rIgTzrLcgFjlGCeAvCY20Da1xpuJ_G4DQesGFWQSkvhhXI-bEP72vnxUBHeWyNopUO3a2u-lK7bVNTmvP9XRJ5PJCHRIruZ_Rc3RvNO8LCXDtOs-1yjDWyRoubvPOGckrr6E2qCm6L6ewF87DPLfI31Y1w2nS4cEN1wxyF6cBINitDrK7ahfhmH0NGh1B2r7zsFJl1322VVz5-ikPaDcL4Abj_Bgb495_P8V8IQlmP1pd34Fs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9ad45a45d.mp4?token=uLoo-YieStt9aUha3MxX7DCvWfpjXGNToyDwsJYKRFjiuiJ77N1WzJq3Tx8gPTzS6w-pJ6RU2nXe5cTvzDNeAkcbrIylngf-TXjchJCXDr_-WGXwLolg3AmHhP8ZCbPoSaX7QF09sIwLSbfwNAnM9qcBLQhXTsCAuL6pjwphPl6mAsgprENz71fmwar9PeTNRoX7YVSFyHju1rTm3YVYqEXp4RxRIB3isv95HsEoDyjsOdkTsguDuFBbFRYJUMAP2RWvFI96aOefI3GpjKMQJrM16kU91zgmgzu0Tis83NcXnqwlOZqVaMPzPPx1_W_vKwNjKU5Md1wWr13y7sWDBDqKrgnY9E_IQtOFc8WPuarZf2GsWPWjWV3EnVzkrly4zwIjx39jp-lE33gj9mLXdIvx39NXeZSo534P42yCtmTBIqwg2ssPXU9_k7rIgTzrLcgFjlGCeAvCY20Da1xpuJ_G4DQesGFWQSkvhhXI-bEP72vnxUBHeWyNopUO3a2u-lK7bVNTmvP9XRJ5PJCHRIruZ_Rc3RvNO8LCXDtOs-1yjDWyRoubvPOGckrr6E2qCm6L6ewF87DPLfI31Y1w2nS4cEN1wxyF6cBINitDrK7ahfhmH0NGh1B2r7zsFJl1322VVz5-ikPaDcL4Abj_Bgb495_P8V8IQlmP1pd34Fs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من العدوان السعودي على صنعاء</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/naya_foriraq/93086" target="_blank">📅 17:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93085">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LR-a-7uuE74Pq_iXAHcg0rjhOvUEr99W5j7eGyBHDqRkVkUf9YQOUHXopNq989c3BECRCJO_LfyVUJ2N3_6eNnq_O6gJOpSlmC-4y-cPW-vkDjVDiSQSU5FtokCR-QuuAExm9BkK1imGe2B5-cwDMmR9BMl_hLvNw4yk0ab72rIiu3aDqD_zmenoIWcwW8SYCAKdousBOzT27Td-M4seEVbpGc_kgjHQxOp8qnxWvYW0_b6fk3hsn5-mTmPlS4ErwFoDkly4vVpzeXvSr5iiMwflSbTWiGf-csW4LD_CWNA_6sItu7Jyqr81J8Fsf_t9feACZGluaS-X2sFkE8YiLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">القيادة البحرية للحرس الثوري: من الآن فصاعدًا، لن يقتصر التعامل مع السفن المخالفة على مضيق هرمز، وسيتم ملاحقة أي سفينة تمر عبر ممر غير مصرح به في جميع أنحاء المنطقة، وستكون عقوبتها نهائية.</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/naya_foriraq/93085" target="_blank">📅 17:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93083">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eBECvXht8NxTWOhKngMqYQGK-v-T0qPmO7Mw4GjR9pN-iDsnQ-qv746hQA4JZMJ1062nWvEhduqIyIns__26OwJXSx3tVjLWZpJjF89ghNIQ6C4slKy8-CUNKrJtXV2F0UOSIghLVwbEQtvg9v56xJTJj65iAQ-W7QLlSFUdsh2vQGIQtglMGtUiQDxv6zG101L8W3ZcbVr__oC3O_c2Uts4ZuUrzZ4TNaGaHjUSrScgjlxBTeHsQlDcj2085tllgC77q9i0M0My4dm9uhgrjlLgaoVOhoR05RifJXnSOurDcm9LTH4xcamXk8qvT47jh3UTux2ShQ5v1favkpm5jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ndGZ1zLNUeqAbei47qdeMNxVwsLfr6TxCsLvZS9IfD2BZWJ4HuJCjNI_swOv0M5dWrfBx3keDMhwExgFaC8A_hSvrP6LLfBkdjdUHy4DSYMYKrV9EImSdJ3gPVxZhXfvVTTNUg87oG0lm51QOmYQTh4dg616yWh8xn46h2kGHUScZ-_E7MdwPje_ctpkTsPu-F6S9mDjQyADhQn0OA0uGUu30AlrItMkRm1nCAoxx4kRycEinX-cmASqpDS0jUzNRFHasp480Hg5HtnFDIUBDCr_0b3Ie82YkC_-u-e3uH_FY6vK0cQJ5X70CD6GrBL7Bji2we8PD2k-B8fGo0sizg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من العدوان السعودي على صنعاء</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/naya_foriraq/93083" target="_blank">📅 17:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93082">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de14d93788.mp4?token=TJoRR2DhNfSWWJNPMxkFnWcCcXlechbLfNKm3cLM2aV-0Y_DH1IodIBqz9YqA5k-q9tx3zWgLD7CRM0Zx5GPaIULX8snw2Wi5hEyXD7x1JZnu_QdhxFNFuLz2fujY5zuGN4g7aSV6fi3GbbJMcdzlzvWoXzxljH3nASj2p2S6-FxQJmc43rQLoyIUIWKR0cCCqz4PQ3GyJXAEsHWzHzOU37FVWx6MU3QKLqE4mIsdVxgsotBmO0rs2byNspKD3ipQWS8r9UQjbJFP4uVscmLBLHOuCasuisv9rscWMrDXd2VP6Yqj3fgqMWdSB5JEDNq9SlxWB04rhccbE1E-1aeGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de14d93788.mp4?token=TJoRR2DhNfSWWJNPMxkFnWcCcXlechbLfNKm3cLM2aV-0Y_DH1IodIBqz9YqA5k-q9tx3zWgLD7CRM0Zx5GPaIULX8snw2Wi5hEyXD7x1JZnu_QdhxFNFuLz2fujY5zuGN4g7aSV6fi3GbbJMcdzlzvWoXzxljH3nASj2p2S6-FxQJmc43rQLoyIUIWKR0cCCqz4PQ3GyJXAEsHWzHzOU37FVWx6MU3QKLqE4mIsdVxgsotBmO0rs2byNspKD3ipQWS8r9UQjbJFP4uVscmLBLHOuCasuisv9rscWMrDXd2VP6Yqj3fgqMWdSB5JEDNq9SlxWB04rhccbE1E-1aeGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماع دوي انفجار في صنعاء وسط انباء عن عدوان سعودي اجرامي</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/naya_foriraq/93082" target="_blank">📅 17:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93081">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سماع دوي انفجار في صنعاء وسط انباء عن عدوان سعودي اجرامي</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/naya_foriraq/93081" target="_blank">📅 17:14 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93080">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇱
بلدية كريات شمونة:
سيشنّ الجيش الإسرائيلي خلال الساعات المقبلة سلسلة غارات على الأراضي اللبنانية، وستُسمع أصوات انفجارات في المنطقة.</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/naya_foriraq/93080" target="_blank">📅 17:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93079">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇮🇶
عناصر من التيار المدخلي تقوم بكسر أقفال "جامع أبي بكر" في منطقة النساف ضمن محافظة الأنبار غربي العراق بعد إغلاقه من قبل الأهالي احتجاجاً على ما صدر منه من خطاب تكفيري.</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/naya_foriraq/93079" target="_blank">📅 17:08 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93077">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56c2f4e39e.mp4?token=iGgWiSLXjC-r7EBuDPWo9FgQ-ze540ZYNA5QdH_X8Be8Vt2qvgVwA4Os4D7m2pNyY9eqHSo2Ba4R4_ttWZCHe2B0shyWwsZCRCutNCnaBne05EhxELd6mzz4NcbtA68Ggigm2kdxPt15jWsOgUhbR27Qu9T2fNdMaK8uP9u222_Ga1da5hte2uwIf1yH-o0vrDaHnLZQW2orZlde5oClZkBSIsfxfex_zUIeXRoskH2B5AelDUO4CV-zNfslvnVL9zCwKu0SYH1eZ5rXPh22VzJgdyVmpvg9AIHlqtbTFHAonsVM0utwBFwpQpqD6qS-f6JbSIgJeSK1pgU8V0sVTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56c2f4e39e.mp4?token=iGgWiSLXjC-r7EBuDPWo9FgQ-ze540ZYNA5QdH_X8Be8Vt2qvgVwA4Os4D7m2pNyY9eqHSo2Ba4R4_ttWZCHe2B0shyWwsZCRCutNCnaBne05EhxELd6mzz4NcbtA68Ggigm2kdxPt15jWsOgUhbR27Qu9T2fNdMaK8uP9u222_Ga1da5hte2uwIf1yH-o0vrDaHnLZQW2orZlde5oClZkBSIsfxfex_zUIeXRoskH2B5AelDUO4CV-zNfslvnVL9zCwKu0SYH1eZ5rXPh22VzJgdyVmpvg9AIHlqtbTFHAonsVM0utwBFwpQpqD6qS-f6JbSIgJeSK1pgU8V0sVTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
الاعلام العبري:
محاولة استهداف سيارة في بلدة حوش السيد علي قضاء الهرمل على الحدود اللبنانية السورية.</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/naya_foriraq/93077" target="_blank">📅 16:53 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93076">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇷
انفجرت عبوة ناسفة على جانب الطريق في طريق سيارة تابعة للشرطة في منطقة "تشمه زيارت" في زاهدان بالجمهورية الاسلامية اصابة عدد من الشرطة كحصيلة اولية.</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/naya_foriraq/93076" target="_blank">📅 16:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93075">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QoVsjvhaEN9xV6lv-6bEYKe4u_H3lhpbIWNm9WrIKFemPd2YvEOlod2TSscw5ynC0pQF1Fogw0QFztwesC9-ywz_nNlvVot8VhpZyE0ssO5d6F865pEZSB5_IoBA1nL8sW8aAFwyyDfKoVuQJjxlmuJcYtnaxBVM0Nhr365oeaz-s9vTAbhOlRWyhTvUKxlOCpH2R7KU_CviRnTDkfAEhlVcpWPZBsqtAyvIq2XpmHQD6GtchyOBPMQVCyT6xSr64pH2D69Z-q4g-mv4LChqDD3R4H_0Lw0vM32BHxJ8yv3Pxz0MkRfr8-feVzUy5V8mo2lNojnyG5MpRcxHFawFGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
مشاركة حشود غفيرة إمتثالاً لتوجيهات السيد عبدالملك الحوثي ودعماً للقضية الفلسطينية والقوات المسلحة اليمنية في مواجهة العدو السعودي بمحافظة صعدة.</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/naya_foriraq/93075" target="_blank">📅 16:41 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93074">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_wNv0kyAFm0rIF3oU7XcFAsBDaxHdNpdCDl4rQM5mEYNZBwmBQ4VqDRsk3X5INztKBQNIbkz-9Wh7d2dkVTuvlwvHNQ5Rh4DhOeIPZF0Fu7QMq4cXLipTBLiWjBuyEAnRiIbwT4MhmwmpFarsTq7IwJaiyQ9LfBbLnot7F60QOGvdUSHT_tTmsl0Hld2MS4pF_fXLnSAcBrd02Sr_SvH3PIOhax854S8cUzp4nSdrO_Gen0F8_RYxD_0uPikMB2-T-jhjpvySyrrTg08FbDF-US9-eapMKwck0KsWh4eurCoJbCG81agWUMn1faK3KViE-1DrqW52lN5BzIBpxYHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضربة تطال سفينة قرب سواحل الإمارات</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/naya_foriraq/93074" target="_blank">📅 16:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93073">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
سيتم السماح للرحلات الإنسانية من وإلى مطار الرياض لجميع الرحلات الحاصلة على تصريح من مركز تنسيق العمليات الإنسانية في العاصمة صنعاء.</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/naya_foriraq/93073" target="_blank">📅 16:22 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93072">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‏قوات المرتزقة تعلن مقتل قائد قوات الطوارئ في أمن الضالع قائد اللواء 16 عمالقة خلال المواجهات مع انصار الله</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/naya_foriraq/93072" target="_blank">📅 16:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93071">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0a1a81fbc.mp4?token=MmPwehdHX4KuRY28BhpZmTzV-jJjwXClJWcuH8OpwvvaByF4mLH6xCeJdEoTYnG7R7o-l5YQN4UpPUX4MdhlTampCG1lSWNTOy4nwR_BfyvU9mFZeKksiG9rGaX7ErG44ESNA8Mg63mvvIUR1Q0eYYPIso3uMT8oX3l7CO9Bt0YOKijiFu0IktXVvNN41iQqVO2adZo5YACUqau3UGMvRvJdS3DDhYCcsgdfZHY0cZsfvpeEc6JK4oynhc9XSdRI0HYO6DQ89Wk7RC_CGVCtlex5pICzxW66aCcpl-jfOPQnwJMR6FuMdzyyqgCW_LJBnNXYgHz-a2aFX-fjmpSuQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0a1a81fbc.mp4?token=MmPwehdHX4KuRY28BhpZmTzV-jJjwXClJWcuH8OpwvvaByF4mLH6xCeJdEoTYnG7R7o-l5YQN4UpPUX4MdhlTampCG1lSWNTOy4nwR_BfyvU9mFZeKksiG9rGaX7ErG44ESNA8Mg63mvvIUR1Q0eYYPIso3uMT8oX3l7CO9Bt0YOKijiFu0IktXVvNN41iQqVO2adZo5YACUqau3UGMvRvJdS3DDhYCcsgdfZHY0cZsfvpeEc6JK4oynhc9XSdRI0HYO6DQ89Wk7RC_CGVCtlex5pICzxW66aCcpl-jfOPQnwJMR6FuMdzyyqgCW_LJBnNXYgHz-a2aFX-fjmpSuQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز اربيل</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/naya_foriraq/93071" target="_blank">📅 16:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93070">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">انفجارات تهز اربيل</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/naya_foriraq/93070" target="_blank">📅 16:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93069">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇾🇪
🇾🇪
وزارة الخارجية اليمنية في صنعاء:
بسط السيادة الوطنية على الأراضي اليمنية كافة حق مشروع كفلته الأعراف والقوانين والمواثيق</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/93069" target="_blank">📅 16:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93068">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ليست مشاهد من فيلم الرسالة او حرب البسوس في الجاهلية.. مشاهد مباشرة الان من محافظة الحسكة السورية.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/93068" target="_blank">📅 15:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93067">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e4c462e20.mp4?token=u4pqJF0s4hd3UlvYuOeahDsXMVec9nfbyJ7rRUBipBHZUG5UX_5jLmcWMYjWkpL_jXCaPFk5E0uy0hzk8QXEnvaG6uSC5Mrlzpz6xwgVitAcMzLjQiUgBjtkZ3IGmfSqkJdIakcHnjHDIFVFtoTR3LQuhf8_Dfqv3-Nnw07Q9adZ5mcJcsmbWYMtKUS4xVLX63awW9aiDwEy-NieNQwtEokMsB7evXazRmAa5WNBilyE9Wudtz5qUNyML5zMCmp7wvzTdVgD30Ym9nKiygbW7Sb6H3Dh7eZpmheBmhMxtx-zGZs6Jyd3_IfKArPJiWChzyQRHL6F3ruuMjtHTxrV5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e4c462e20.mp4?token=u4pqJF0s4hd3UlvYuOeahDsXMVec9nfbyJ7rRUBipBHZUG5UX_5jLmcWMYjWkpL_jXCaPFk5E0uy0hzk8QXEnvaG6uSC5Mrlzpz6xwgVitAcMzLjQiUgBjtkZ3IGmfSqkJdIakcHnjHDIFVFtoTR3LQuhf8_Dfqv3-Nnw07Q9adZ5mcJcsmbWYMtKUS4xVLX63awW9aiDwEy-NieNQwtEokMsB7evXazRmAa5WNBilyE9Wudtz5qUNyML5zMCmp7wvzTdVgD30Ym9nKiygbW7Sb6H3Dh7eZpmheBmhMxtx-zGZs6Jyd3_IfKArPJiWChzyQRHL6F3ruuMjtHTxrV5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ليست مشاهد من فيلم الرسالة او حرب البسوس في الجاهلية.. مشاهد مباشرة الان من محافظة الحسكة السورية.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/93067" target="_blank">📅 15:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93066">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">وكالة سلامة الطيران الأوروبية:
نوصي بعدم الطيران بأجزاء من المجال الجوي السعودي المحددة ضمن منطقة معلومات الطيران الخاصة بجدة إضافة الى منطقة أخرى في شمال غرب السعودية.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/93066" target="_blank">📅 14:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93065">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">وزير الطاقة الإيطالي:
لن أحضر اجتماع وزراء الطاقة المزمع عقده في الرياض الأسبوع المقبل، وسأشارك عبر الفيديوكونفراس.
الحصار بالحصار</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/93065" target="_blank">📅 14:18 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93064">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">"يا عاصب الراس وينك"..
مرتزقة السعودية يقومون بتشغيل قصائد داعشية ارهابية خلال اشتباكاتهم مع بواسل القوات المسلحة اليمنية!!</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/93064" target="_blank">📅 14:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93063">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اضطراب في المجال الجوي فوق الرياض</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/93063" target="_blank">📅 13:41 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93062">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اضطراب في المجال الجوي فوق الرياض</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/93062" target="_blank">📅 13:41 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93061">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">عدوان سعودي على العاصمة صنعاء</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/93061" target="_blank">📅 13:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93060">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇾🇪
🇸🇦
🇵🇰
اليمن يفرض قاعدة الحصار بالحصار..
باكستان تعلق رحلاتها الجوية من وإلى السعودية.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/93060" target="_blank">📅 13:15 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93059">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xyux4B-HCizQubDu983zBpv18ztP6dVl5MbOaWqpLWI2vejGnQc-ASqeTNI71JXN8uqMRJ8gcJTnTd_ygEYW3GO_1FtzBA2rSazA71Au0P73K1c1VIy_1Tbkgz28VL6oCz8mZBSJMSJ1zZrz5MOJWcylpP0pWvgrk43pNN_LmQefflPwo0Jg7JCTUwLktaLEnSAUZB25AIYavsUHgdj70yAQYIAUXiiATnVLgoZjDnYg6_j57NHL5ULGf14oMLsVB8TYxI_gM9oLx1RDpgoPC1wHLHswPYrcAchDWw1IJ6cfRnJw0giHqA3BtzWiiqbm-eVn-bMxV0XMUSBQ9tTgQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
إنفجارات تهز العاصمة السعودية الرياض.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/93059" target="_blank">📅 13:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93058">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇸🇦
إنفجارات تهز العاصمة السعودية الرياض.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/93058" target="_blank">📅 13:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93057">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇺🇸
السفارة الأمريكية في الأردن:  الأمريكيون الحاليون في الشرق الأوسط يجب أن يكونوا على استعداد للهجرة بسبب البيئة الأمنية المعقدة. يجب أن يكونوا على دراية بإنقاذات الطيران، وإغلاقات الأراضي الجوية، وتعطلات السفر.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/93057" target="_blank">📅 12:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93056">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇺🇸
السفارة الأمريكية في الأردن:
الأمريكيون الحاليون في الشرق الأوسط يجب أن يكونوا على استعداد للهجرة بسبب البيئة الأمنية المعقدة. يجب أن يكونوا على دراية بإنقاذات الطيران، وإغلاقات الأراضي الجوية، وتعطلات السفر.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/93056" target="_blank">📅 12:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93055">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇾🇪
🇸🇦
مصدر عسكري يمني:
انكسار هجوم لتحشيدات العدو السعودي جنوبي باب المندب قادمة من لحج وسقوط عشرات القتلى والجرحى وإحراق وتعطيل عدد من الآليات.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/93055" target="_blank">📅 12:37 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93054">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36234c6463.mp4?token=Gokknoee4QU40VVcSu1pPcMowHZdCaVJfZ6ZNPmbAolyyps4EHnCW4Pte-1NRY4al1mgx8wvnzIaODF1ovniudzQlMjICuu0SSnHEKoCOsIjQpdJuINnFPzqWGHZaKkDxJdqmErAdGMpl2ehCkYYUHFPlXnHXVsqFM95quI2cQINRNQzV3dwLaNc3ucQI9P-s258UtM9Gl6UWwFBfWD3TDRfsKSyW7lLX-FVkAKEOZylmf8vBIZ0wSOpcYbDO8k39ZM2-l-AIbFQsJ6Au9acuWHc2cc5x7m19NQmJOZCtPlCRpsV2YTtPdVGfd3AF8rp0YC2omoXpwSrCrgkJnyRJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36234c6463.mp4?token=Gokknoee4QU40VVcSu1pPcMowHZdCaVJfZ6ZNPmbAolyyps4EHnCW4Pte-1NRY4al1mgx8wvnzIaODF1ovniudzQlMjICuu0SSnHEKoCOsIjQpdJuINnFPzqWGHZaKkDxJdqmErAdGMpl2ehCkYYUHFPlXnHXVsqFM95quI2cQINRNQzV3dwLaNc3ucQI9P-s258UtM9Gl6UWwFBfWD3TDRfsKSyW7lLX-FVkAKEOZylmf8vBIZ0wSOpcYbDO8k39ZM2-l-AIbFQsJ6Au9acuWHc2cc5x7m19NQmJOZCtPlCRpsV2YTtPdVGfd3AF8rp0YC2omoXpwSrCrgkJnyRJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
منح جائزة نوبل للسلام لعام 2026 إلى "نافي بيلاي" مفوضة الأمم المتحدة لحقوق الإنسان.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/93054" target="_blank">📅 12:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93053">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69a4d2a50f.mp4?token=Bx5ZNfhLATJAfxopcHHwjvPvPKax7vOYD_-Y8tEMzM8Uq571TFWBrIvPXQoGrYKb646yqAp9jKbRxywcokRX2oQ1A4Ite053pnAPsum-PrW1SYcFm1iiDDiCRxZgmEIDiAi_yHktWLHCU1PvtJC4KXApZfms8Z65VWNBuorCe62R2kEbkdth3F0726oh9KnYiWMJdJ7ZmkYjOOcnoy3qtwpWSPuMKZCKJVwx_z9zodZd-KwW5TFtRJbPNmL_MzfFMaPSr2p4oNdygXnN09ivItDp9b9Q6iZhiRxY1zoBDRWbzt7Tk42FHuJ8kjZj6iBIlxomYBemFXSmxpELZ-WHlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69a4d2a50f.mp4?token=Bx5ZNfhLATJAfxopcHHwjvPvPKax7vOYD_-Y8tEMzM8Uq571TFWBrIvPXQoGrYKb646yqAp9jKbRxywcokRX2oQ1A4Ite053pnAPsum-PrW1SYcFm1iiDDiCRxZgmEIDiAi_yHktWLHCU1PvtJC4KXApZfms8Z65VWNBuorCe62R2kEbkdth3F0726oh9KnYiWMJdJ7ZmkYjOOcnoy3qtwpWSPuMKZCKJVwx_z9zodZd-KwW5TFtRJbPNmL_MzfFMaPSr2p4oNdygXnN09ivItDp9b9Q6iZhiRxY1zoBDRWbzt7Tk42FHuJ8kjZj6iBIlxomYBemFXSmxpELZ-WHlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
منح جائزة نوبل للسلام لعام 2026 إلى "نافي بيلاي" مفوضة الأمم المتحدة لحقوق الإنسان.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/93053" target="_blank">📅 12:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93052">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇺🇸
‏
مسؤول عسكري أميركي:
القوات الأميركية تلقّت أوامر بالاستنفار يوم الأحد الماضي.
‏تقديم اقتراحات لترمب لضرب قدرات إيران العسكرية على طول الساحل بعمق 50 إلى 80 كلم.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/93052" target="_blank">📅 12:07 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93050">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇾🇪
مشاركة حشود غفيرة إمتثالاً لتوجيهات السيد عبدالملك الحوثي ودعماً للقضية الفلسطينية والقوات المسلحة اليمنية في مواجهة العدو السعودي بمحافظة صعدة.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/93050" target="_blank">📅 11:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93049">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇸🇦
هيئة الطيران السعودي:
تعرض مطار الملك خالد الدولي لهجومين في يوم الخميس، أدى إلى مقتل 3 سعوديين وإصابة عدد من المواطنين والمقيمين من جنسيات مختلفة تراوحت إصاباتهم من الطفيفة إلى البليغة. الهجوم الأول طال مرافق المطار، فيما استهدف الهجوم الثاني طائرة تابعة للخطوط السعودية.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/93049" target="_blank">📅 11:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93048">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇺🇸
رويترز:
ساعدت الحرب، التي بدأت في فبراير عندما شنت الولايات المتحدة وإسرائيل ضربات على إيران، في خفض معدلات الموافقة المحلية لترامب إلى الانخفاض وتثقل كاهل زملائه الجمهوريين وهم يسعون إلى الحفاظ على أغلبيتهم التشريعية الضيقة في انتخابات نوفمبر.
حوالي 60٪ من الأمريكيين - بما في ذلك واحد من كل أربعة جمهوريين - لا يوافقون على كيفية تعامل ترامب مع الوضع في إيران. دفع الصراع أسعار البنزين إلى الارتفاع بشكل حاد في وقت يقول فيه الناخبون إن قلقهم الرئيسي هو تكلفة المعيشة.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/93048" target="_blank">📅 10:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93047">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇺🇸
البنتاغون : سيتم بث إعدام مطلق النار في فورت هود رمياً بالرصاص في الولايات المتحدة على الهواء مباشرة</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/93047" target="_blank">📅 00:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93046">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a053f827f4.mp4?token=VoVCfkNzY81RrpaejV3h1-qTHZVZNdxcFYgJXa7XC54o8NLkmjMhowmY89u5AU50xDkXtwpDpKQGL5UPzqkoQF5iYc3BxqWGcFw8vo2f9Y-2tiwYyoic8wOBEiVJ2kc5C7dRwNTzr7_xetXoza_9-NfN12YFoR-kCOLjgBGdFw89nodcS3BG2hvCkOV5CbZU-R2QEqIuOB4N0JplbhpzFtBN2hfXDiPuPZbiH-C6-AUrR6w2JullwT8UMopLvEQaYNUxLB_lYedXrtgrSlBl5gp0yP8KtXfMs-zJBJtph_NqsGuqzdqB-d6acIt3hNM054hzr5Jio0nIN_xdCQWtWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a053f827f4.mp4?token=VoVCfkNzY81RrpaejV3h1-qTHZVZNdxcFYgJXa7XC54o8NLkmjMhowmY89u5AU50xDkXtwpDpKQGL5UPzqkoQF5iYc3BxqWGcFw8vo2f9Y-2tiwYyoic8wOBEiVJ2kc5C7dRwNTzr7_xetXoza_9-NfN12YFoR-kCOLjgBGdFw89nodcS3BG2hvCkOV5CbZU-R2QEqIuOB4N0JplbhpzFtBN2hfXDiPuPZbiH-C6-AUrR6w2JullwT8UMopLvEQaYNUxLB_lYedXrtgrSlBl5gp0yP8KtXfMs-zJBJtph_NqsGuqzdqB-d6acIt3hNM054hzr5Jio0nIN_xdCQWtWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مشاهد حصرية لنايا... لانطلاق الدفاعات الجوية السعودية من وسط مطار الملك خالد الدولي بعد استهدافه بصواريخ اليمنية.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/93046" target="_blank">📅 00:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93045">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b786078ca8.mp4?token=sC0jojLC5cttBVawG-Dia9ZPnwnYeKnRYsk-Oo8oVZv4xE8dC6dc20hmSDlKqTU8q19JicNqQvhMy0G08uIziElTAagywqS1Z0Rv5tKZxw4AMfY_WcTWrSss1hv4b651xzXgZx-Q4MkhyGhi1HJzHMqqzvTNCTgmmmbS3d0B1vN1_QGnxs4ozslIxtHsJCSpbLeLD8Kz2KsosJPsLhTr15G6M1F22pmtesQBn3OO_AU9ic8w5pRX7_yOUIvWzg1ibsfVneF7-Vl9raiJADq-i1dZXRCS2wdz78R4OvmnOeyw0pGNwNgUJfGjE4jFK2KMlSwwTAjv2VdGSEtF5DhM8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b786078ca8.mp4?token=sC0jojLC5cttBVawG-Dia9ZPnwnYeKnRYsk-Oo8oVZv4xE8dC6dc20hmSDlKqTU8q19JicNqQvhMy0G08uIziElTAagywqS1Z0Rv5tKZxw4AMfY_WcTWrSss1hv4b651xzXgZx-Q4MkhyGhi1HJzHMqqzvTNCTgmmmbS3d0B1vN1_QGnxs4ozslIxtHsJCSpbLeLD8Kz2KsosJPsLhTr15G6M1F22pmtesQBn3OO_AU9ic8w5pRX7_yOUIvWzg1ibsfVneF7-Vl9raiJADq-i1dZXRCS2wdz78R4OvmnOeyw0pGNwNgUJfGjE4jFK2KMlSwwTAjv2VdGSEtF5DhM8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظة الهجوم اليمني على مطار الرياض الدولي</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/93045" target="_blank">📅 00:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93044">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي
: وزارة الدفاع الأمريكية تضع خططًا جديدة لضربة محتملة ضد إيران في الوقت الذي يتردد فيه ترامب.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/93044" target="_blank">📅 00:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93043">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇫🇷
🇸🇦
رئيس الأركان الفرنسي:
لا نزال ندرس مع السعودية خيارات تتضمن وسائل عسكرية للمساعدة بحماية ميناء ينبع النفطي.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/93043" target="_blank">📅 00:01 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93042">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/93042" target="_blank">📅 00:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93041">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-KR2vy542XkGq8hkL3mL9OLdOOBlONFnkIdZ-14xp8jw2E2REf8gjgq2gzaJvaGhgFshaTKUWZcY3dVEfMOOsRQ8MkvEdke61jh5bgsUd8gzmUQtq2K_KX_8pZFqWA9AVEUbZFuOHEM-Ap4Si93uCBrFoLWeDwd4Dy8YMeyUnLhGB_AwPEKB7hu-RB66HL4hAnbIxOMAtyRKbZYSyhhtGsc4rIzblU1RylfXnCujTIXk6KB1SDnUmasTRyZqffIO32wPjJnPWbHh6rpv2JcBgpWmTMdTOLfPZq9PJH22YKUZ8ydYlo7zv3a94OfBkEs2NPZ7Shg2TK1GkPxi2mPNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🇺🇸
🇮🇱
🇸🇦
🔻
أصدرت السفارة الأمريكية في القدس تنبيهاً أمنياً تحث فيه الأمريكيين في جميع أنحاء الشرق الأوسط على توخي الحذر الشديد، محذرةً من احتمال حدوث اضطرابات في الرحلات الجوية وتصاعد سريع في الأعمال العدائية بين السعودية " والحوثيين " ..</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/93041" target="_blank">📅 23:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93040">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8Qk-a_vldigB1ZpKt5Ea1lCFL0VLPuAbQSyz_-skGM_iBtHM875LMcyptshS8jM4gnDtaetIW9oda-AHPYqGaAhkFuZ9P6A_76QVCcNIN05Y8HPqrRkfC-j2Fh5FJqVaExxm50b6dOL4L5hppInrQiFdhmNHrLoR0PE9WIitGCLkepROVp3x5I4vhGlbX7av30hT_aQDOXajYn8j0tD-q3owpKYzrgF5ZgivDb61tpOjm89izQIrsxOmDf3NtQRKbnFGSlIf33rKw77TlzQUh4VqYy3RGyvffHOjS6jCRIckumeEH9Tlz2TOAIG6AnSv-VaTHD7y6OYYVmlzpmGuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
متداول
وثيقة تتضمن شمول رئيس هيئة الاستثمار العراقي بقيد جنائي ! الأمر الذي يطرح تسأل عن كيفية الموافقة عليه بمنصبه الحالي !</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/93040" target="_blank">📅 23:47 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93039">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWsMoga7GES3DCFYHv8ZcsN8Er-u5Ov31HJPAoGy35R6eMtX50szGNe13IK9-MFwoRGCgUBvkQBoapZEqoX5nSAVCR-zei1Ls05iApP-anghS2CKN1uKu_NXesz8bRQV6rEdGiQ5gVcEb4Gip5J9sipgmh3dFJOkSICBEcJ101Tc68_TJ296Id0LBlJ0zlYBIL7ICtItcF2WJwkBGDd_UTOVIGPugQc5tF16df-E4SCHlr9bbV7l3WCbChfexVxnfWpa--PBDk_oJ7rIgViNzybBS3xzJQoBy0HJXaKG4LiP775LLgcqmDMZp0lkQg-AhW7J33BnuCtqHwz_E7ce4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصوات انفجارات في صنعاء</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/93039" target="_blank">📅 23:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93038">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اصوات انفجارات في صنعاء</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/93038" target="_blank">📅 23:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93037">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AxzKardN_-PJUFcMmOC_LJ2PIMrHGHPIgBkpAH4yXJiGYyNEoVW9KC7haLhscYnVOjWUOdJbbibRIWCl3Hb-_NIPMSoGivSN4rTdpcfkFoDz6ngsK57FrvAZjd6u-ogU_Blo2W2hYLhduiIZNaPjh6xAximz3FIuLXtd2qAjb2OjgB40Rr9suSaSAoOaCwD_W2SUMoKkKOWq_pcRty87ak2F7vDt5wjFxu5wH3rxFGTzPGCAOZvYxdoO3m4h5DyCeSbcMezACMpvQFaMo0HQT0_aPX1DJcTnO22sz6mK2MSmspvEr2gnnDaK9epDUsbfy4z9Ok8Lolj-pbKk0XJBnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇶
تحذير أمني جديد من السفارة الأمريكية في بغداد للمواطنين الأمريكيين في العراق</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/93037" target="_blank">📅 23:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93036">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L926QE9lYRT0yT2PDz9P8qbMSUWSpvgDstyLWXM_4sT4Gydt22kChtfGmCWiwVuMFER6Jl9pnmWHc_LhIaluTusOfY5OKlaLxH-1EDS5Plge2733t8ITIcaBCsL1YMCqNWNbs8mvVeUbk0uwvru35AMjielKmJ3jZYUhDwmRpv3atdPyTjJ25JK9_mJ26AKfGWUhp82SBZ89sS7cyXCrdjbkqh5LRz6x0_N7VeGTxpGRdHooz4473wEM_dvMeqFmj9w9q44fRX8dmn2O7etwNi-7bR-6XmO0xZI8AhEAoZLNJSTqfVaspDV1egW4zbCjF-Dfn1qsN9iC1QkidRaJvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
اندلاع نزاع عشائري في محافظة ميسان جنوبي العراق مقتل طفل واحد كحصيلة اولية.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/93036" target="_blank">📅 23:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93035">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇺🇸
🇮🇱
السفارة الأمريكية في القدس تحذر المواطنين الأمريكيين الموجودين في إسرائيل:
يجب على المواطنين الأمريكيين الاستعداد لاحتمالية إلغاء الرحلات الجوية.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/93035" target="_blank">📅 23:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93034">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa770901e6.mp4?token=u3L2A1mWfChxsg3IUwT5bnwNVaPFZBeOlz96BSBJXif4L7Y79aFq2tzOAU745iKGVz5szyQllJ75-oYz2HJcDFZdxsesKrOYfChVg2g59NwrinTwG2KMSyNutunkfor8bwLmGmP29b5C0jM1fvOqFAnBd-N5UhofSX6SM6qTymz421cgtI3mqwyAVj0LVQWBvHuDD6tZOKTe9UgDhfVbG_JmM_6cvQPO1B4MSQt9uGatOekOY9BSiO5Rqe1w5X6Y6XkV7_Vn_fvXY2u2-n2GOBr47NVvDzma9_FumThqwep02Sq413TveUlNmSCAXMcgMqIb7D3XmRPVjGJRbEac3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa770901e6.mp4?token=u3L2A1mWfChxsg3IUwT5bnwNVaPFZBeOlz96BSBJXif4L7Y79aFq2tzOAU745iKGVz5szyQllJ75-oYz2HJcDFZdxsesKrOYfChVg2g59NwrinTwG2KMSyNutunkfor8bwLmGmP29b5C0jM1fvOqFAnBd-N5UhofSX6SM6qTymz421cgtI3mqwyAVj0LVQWBvHuDD6tZOKTe9UgDhfVbG_JmM_6cvQPO1B4MSQt9uGatOekOY9BSiO5Rqe1w5X6Y6XkV7_Vn_fvXY2u2-n2GOBr47NVvDzma9_FumThqwep02Sq413TveUlNmSCAXMcgMqIb7D3XmRPVjGJRbEac3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
توثيق قريب ومباشر للحظة استهداف احد مقرات الاحزاب المعارضة الايرانية في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/93034" target="_blank">📅 23:13 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93032">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c0ef9968e.mp4?token=ZzlEeayY7y9loR8WG0PiwN9Vp3N4f0YBnVgtjt2BdrR2c4Fby1E_-ok57K8tkkaJmy9n-dZalhqiYM5pYqpYQD3QC0dB7a5QBmmDErHY7m-IBOrMV_TJPM-YlaCcIOaA_kJUigIC5mN8-9j3OJv6nKbEx1X4wwO9Tdwg1Pl2M3WOpGoMH1LYe3M6HA8NDiFRLLQ97JhrgFDlvqd-HIwbep2oqtM4JNKiqiaBLHPCOmHOhqRGOUutFn5ShrRDm_2sVcgejD4xdgzKp1JTsFyRWJEKJK5UnxFD0Ej1ibHVWrdXRxi_G-URVL9ZPI7qxQ1YBenzl8DWHZD3TcYigkfJAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c0ef9968e.mp4?token=ZzlEeayY7y9loR8WG0PiwN9Vp3N4f0YBnVgtjt2BdrR2c4Fby1E_-ok57K8tkkaJmy9n-dZalhqiYM5pYqpYQD3QC0dB7a5QBmmDErHY7m-IBOrMV_TJPM-YlaCcIOaA_kJUigIC5mN8-9j3OJv6nKbEx1X4wwO9Tdwg1Pl2M3WOpGoMH1LYe3M6HA8NDiFRLLQ97JhrgFDlvqd-HIwbep2oqtM4JNKiqiaBLHPCOmHOhqRGOUutFn5ShrRDm_2sVcgejD4xdgzKp1JTsFyRWJEKJK5UnxFD0Ej1ibHVWrdXRxi_G-URVL9ZPI7qxQ1YBenzl8DWHZD3TcYigkfJAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من مقرات الاحزاب المعارضة في اربيل</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/93032" target="_blank">📅 23:11 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93031">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/039ff7ebef.mp4?token=nPuq2aWZD-lccpSZ3v9DrKOiN3acpL21GBdPd9MNMlc5oc4G-CM7vvF_lmXAdum6-i5rrnxjaAw05zj7oa8zmBmnSvt20OJR9iNr4ktWuciWUwqYHBEdAvc14qtFbHUlx1BR0gq-JF1pyHZ06zbl4HzZ8DU1HCk2_tR76PFHYRzbg2NbSQzHJYTllaJcTr6VLmBw61alh0cZ0lNBBSJSwo8AGpfiRJ8jt2aGcfiVa7l-B7nEYXqF8-WaYRrkDsUnBap7K7SzAqU8lkzpFLvTeGBNp-9arBYgynEpB3qbtF4lHMeqfAhKjQ_7LYB9QD41ZXW6ME1x_nT0untP-_PY3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/039ff7ebef.mp4?token=nPuq2aWZD-lccpSZ3v9DrKOiN3acpL21GBdPd9MNMlc5oc4G-CM7vvF_lmXAdum6-i5rrnxjaAw05zj7oa8zmBmnSvt20OJR9iNr4ktWuciWUwqYHBEdAvc14qtFbHUlx1BR0gq-JF1pyHZ06zbl4HzZ8DU1HCk2_tR76PFHYRzbg2NbSQzHJYTllaJcTr6VLmBw61alh0cZ0lNBBSJSwo8AGpfiRJ8jt2aGcfiVa7l-B7nEYXqF8-WaYRrkDsUnBap7K7SzAqU8lkzpFLvTeGBNp-9arBYgynEpB3qbtF4lHMeqfAhKjQ_7LYB9QD41ZXW6ME1x_nT0untP-_PY3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مشاهد قريبة للحظات الاولى لسقوط المباشر على احد مقرات الاحزاب الايرانية المعارضة في اربيل.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/93031" target="_blank">📅 23:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93030">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ace48d1baf.mp4?token=KRGD3qA1c-zeC4BaZXTR3cgFNH0-J6nsvcsKO91cTBSKgcydrbOjVhM5K7SYpHbKWlghbfPz04wC4rN41zsWSNe3FP9Q7kn6tJID8L1kY7EJOqA9GKSqFWW9HTEId94AWy8axfbVod884_ZjNt9Xyvoapm-5Vd8AZcnosTcGb69EPkIy32shtiCF3eh6fG5CR9wlU2qH5W0lr_vFCvFyURQnrDWBqzlL32ClqhqGPrs7qmXlwCN49zxrEejT7FTsv6wuZZy6ZnjP1hwfWzDeIVrMpu-YqITpBwAH9sJUwarE3zksHcaTpbSMbLy9Ed_SZB4lTs5Ui1IQPIQifuAxvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ace48d1baf.mp4?token=KRGD3qA1c-zeC4BaZXTR3cgFNH0-J6nsvcsKO91cTBSKgcydrbOjVhM5K7SYpHbKWlghbfPz04wC4rN41zsWSNe3FP9Q7kn6tJID8L1kY7EJOqA9GKSqFWW9HTEId94AWy8axfbVod884_ZjNt9Xyvoapm-5Vd8AZcnosTcGb69EPkIy32shtiCF3eh6fG5CR9wlU2qH5W0lr_vFCvFyURQnrDWBqzlL32ClqhqGPrs7qmXlwCN49zxrEejT7FTsv6wuZZy6ZnjP1hwfWzDeIVrMpu-YqITpBwAH9sJUwarE3zksHcaTpbSMbLy9Ed_SZB4lTs5Ui1IQPIQifuAxvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مشاهد من محاولات اسقاط الطارئات المسيرة المتجهة الى مقرات الاحزاب الايرانية في محافظة اربيل قبل ان تسقط على اهدافها بشكل مباشر.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/93030" target="_blank">📅 23:04 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93029">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bf39202dd.mp4?token=D6JTJ1LlW3kBl_44S6ZLIRkLGvJHorhe4nQvp2EsoDj4duzIaNWen7s8Gco9qSnnqnGcP7yrvMfwK4l3bPvc7UuvjI03-L03DRheg1OZpELk0I4ljpq4vhzhSqjR34ebpPVqoJfXSOLbiQP2PZyS-kV3N9F-hTamXqCU17qSJCKA6256YaZVNlQA4UzK9_CHJyPieAbc2lUub9eimss51ljr2uSsbc7fEDHQPnt8Xq-Ue8wuSs1NzF3CdR3_1jysqNS-nsgDrEKLtrjN1tqlD8375jTXVQutzzFWPIllIulD8uCqd3zdMjlym_Yhs9YbS_Yfr24kNPxrFB3ImVg9Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bf39202dd.mp4?token=D6JTJ1LlW3kBl_44S6ZLIRkLGvJHorhe4nQvp2EsoDj4duzIaNWen7s8Gco9qSnnqnGcP7yrvMfwK4l3bPvc7UuvjI03-L03DRheg1OZpELk0I4ljpq4vhzhSqjR34ebpPVqoJfXSOLbiQP2PZyS-kV3N9F-hTamXqCU17qSJCKA6256YaZVNlQA4UzK9_CHJyPieAbc2lUub9eimss51ljr2uSsbc7fEDHQPnt8Xq-Ue8wuSs1NzF3CdR3_1jysqNS-nsgDrEKLtrjN1tqlD8375jTXVQutzzFWPIllIulD8uCqd3zdMjlym_Yhs9YbS_Yfr24kNPxrFB3ImVg9Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرائق واسعة تطال مقرات المعارضة في اربيل.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/93029" target="_blank">📅 23:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93028">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db89739427.mp4?token=FTbPF2cu-rO_SehknHI0do-Kw38n6zTObHbO22dqyF27kBNNMRLdgG9kGWtqfAyYnUF0paEfPAZ1G7u1RKO05lwcdqx6ZS9Vc1A-Ugt22Wk33M9dYyIaN7yN_4DY4DXD_eP4095Q-Dd37Rv7CteEq2-DWL3BtSmDSCAITduryY-zKU-41S8LhGQJQ2wNh9xjb_pHMvqe9J6PWRPexPTeZ_ybNT_68EwS3imQhQoHTL4e0UAHydNZ_qSt1jkG5osc7Xkdl_RNgGHkLsMZ2IuR5SbRlCqPAiONZs8hpMtKnQhQ0CiSU6y_cR-3a4flkN8j-j_qYE5fzvW9_O_QtcqYyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db89739427.mp4?token=FTbPF2cu-rO_SehknHI0do-Kw38n6zTObHbO22dqyF27kBNNMRLdgG9kGWtqfAyYnUF0paEfPAZ1G7u1RKO05lwcdqx6ZS9Vc1A-Ugt22Wk33M9dYyIaN7yN_4DY4DXD_eP4095Q-Dd37Rv7CteEq2-DWL3BtSmDSCAITduryY-zKU-41S8LhGQJQ2wNh9xjb_pHMvqe9J6PWRPexPTeZ_ybNT_68EwS3imQhQoHTL4e0UAHydNZ_qSt1jkG5osc7Xkdl_RNgGHkLsMZ2IuR5SbRlCqPAiONZs8hpMtKnQhQ0CiSU6y_cR-3a4flkN8j-j_qYE5fzvW9_O_QtcqYyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مشاهد اخرى للحظات الاستهداف الت طالت مقرات الاحزاب الايراني المعارضة في اربيل.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/93028" target="_blank">📅 23:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93027">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f064a85ad2.mp4?token=nR-VxQ6fgZuKVluvIP7p_W9iYtZZ62bTyFMJPupA92Ln3CqEMVPGDHPMV1djj5Ai2ZBLxJBvntk4Bid6am5q4OHdS46_J-Bakj4cWPNayT16NMImCNdmrxTH6YIUinh0bzAa6GFKD14EpuTwTQH5uJlwq-4j1WHDlODtg5c2TrwVFVZat418IBGN3AQn45xbu4dHYtJzJCfi80IRfEVvslnASdpUqCqGIC7srr_IvHFslsxzz84PhjD2TevS9tr7LU3ykBbT5UDgB-sMWoL9wMSPQaEbvsyImqdemvzNuSJjAlMuItxJogVxx6EXmRN8G9s-jG_ciajNxil74leEBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f064a85ad2.mp4?token=nR-VxQ6fgZuKVluvIP7p_W9iYtZZ62bTyFMJPupA92Ln3CqEMVPGDHPMV1djj5Ai2ZBLxJBvntk4Bid6am5q4OHdS46_J-Bakj4cWPNayT16NMImCNdmrxTH6YIUinh0bzAa6GFKD14EpuTwTQH5uJlwq-4j1WHDlODtg5c2TrwVFVZat418IBGN3AQn45xbu4dHYtJzJCfi80IRfEVvslnASdpUqCqGIC7srr_IvHFslsxzz84PhjD2TevS9tr7LU3ykBbT5UDgB-sMWoL9wMSPQaEbvsyImqdemvzNuSJjAlMuItxJogVxx6EXmRN8G9s-jG_ciajNxil74leEBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
استهداف مباشر لمقرات الاحزاب المعارضة في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/93027" target="_blank">📅 23:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93026">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30d8437636.mp4?token=STyJLIA0rKtk-5a33lyIIT84FNg5st_t48trhNY32JL2yJSxY5wbrNlcxaVAsv93D1JSKqRV5p1kTdzyCxORDmORoPGRnLsTr1YWX2Wtq-NCiNrfcFVIaaJ7koihr4eeLklhGVdQOu8tbRveGzNOnzFVD1qQql2bbZW6XqRqv7AMi2hmkVEoTZwXu_tA5NEJuVwheQb0zkPsI3KwIksOwe4lGE0XfefbGPOprP-HHhg0oott0ArW54UbElkJkVPMQRyPkm8izaLv_Tzf0AffzmYigDlNpnktK8iwVmtroIgzyxhURd1MTXvld5Q21UPITYDwjxxfRYuwfzoskjCQmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30d8437636.mp4?token=STyJLIA0rKtk-5a33lyIIT84FNg5st_t48trhNY32JL2yJSxY5wbrNlcxaVAsv93D1JSKqRV5p1kTdzyCxORDmORoPGRnLsTr1YWX2Wtq-NCiNrfcFVIaaJ7koihr4eeLklhGVdQOu8tbRveGzNOnzFVD1qQql2bbZW6XqRqv7AMi2hmkVEoTZwXu_tA5NEJuVwheQb0zkPsI3KwIksOwe4lGE0XfefbGPOprP-HHhg0oott0ArW54UbElkJkVPMQRyPkm8izaLv_Tzf0AffzmYigDlNpnktK8iwVmtroIgzyxhURd1MTXvld5Q21UPITYDwjxxfRYuwfzoskjCQmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
لحظة استهداف احد مقرات الاحزاب المعارضة في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/93026" target="_blank">📅 22:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93025">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9dbe316ea.mp4?token=eHuDyaslbRIGaF0Po-frDYWqcyggnE-qWXxGB3jjlRhgpgmiSyUY2PBTzhiENBsRtzn34oIl8rODJuiOodfb6h8EO3pezqJUZf9f4rjtCMVRUYD9cZFN5K2GuqWgEsWcrqFo36FDCfO5SEODXUHmph56IPLzhJxsmIcSD1scB1iu8adfoYb3F0IOCWk_zDzv6zGp2aEw-cLOVTiorTu6ElWh32ADiEdZXR3AbTo7kPwGJYLGBc_eWFnDDq6Zb9s81nLg_2VcvqYe5LUGjdwwyWRRC_EURuP_nenO_v44HG1wCL72OYJzF3FJr2JfwTA8Q_MS1miFKCYaqauatWP9bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9dbe316ea.mp4?token=eHuDyaslbRIGaF0Po-frDYWqcyggnE-qWXxGB3jjlRhgpgmiSyUY2PBTzhiENBsRtzn34oIl8rODJuiOodfb6h8EO3pezqJUZf9f4rjtCMVRUYD9cZFN5K2GuqWgEsWcrqFo36FDCfO5SEODXUHmph56IPLzhJxsmIcSD1scB1iu8adfoYb3F0IOCWk_zDzv6zGp2aEw-cLOVTiorTu6ElWh32ADiEdZXR3AbTo7kPwGJYLGBc_eWFnDDq6Zb9s81nLg_2VcvqYe5LUGjdwwyWRRC_EURuP_nenO_v44HG1wCL72OYJzF3FJr2JfwTA8Q_MS1miFKCYaqauatWP9bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انفجارات عنيفة في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/93025" target="_blank">📅 22:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93024">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/391a0aa41d.mp4?token=HdD5waSLC6A0CSADxecFhQAt7kaeh8LjqncIlCP2kUECSDDLj7WYYA1gYNz23pCkmelXCOh60e3MKrfrdRZiqi_DLZpAHrJtr4RDVTHOpOnCC7UFgpeqHz4lqpKFVdR_9O-4uZLCYLZvViRX8EOHjY5204KYo6boJRNw0aPV2glkz_725tp2ltd_VwUmvIUzZe0BT6SMf4c-BW-SCJ3sSS8rbqcv1-e6yW2rupHDYNM9rHFf1FpMLcxy_cNVVZi_rUFS5gcguOR9cdIdlJn_925qAtbPFJfFSokS1S_ieOy7clQ3VHVS7oNQehLzNoAjKQZIzDs4F_gPai4jQXE7yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/391a0aa41d.mp4?token=HdD5waSLC6A0CSADxecFhQAt7kaeh8LjqncIlCP2kUECSDDLj7WYYA1gYNz23pCkmelXCOh60e3MKrfrdRZiqi_DLZpAHrJtr4RDVTHOpOnCC7UFgpeqHz4lqpKFVdR_9O-4uZLCYLZvViRX8EOHjY5204KYo6boJRNw0aPV2glkz_725tp2ltd_VwUmvIUzZe0BT6SMf4c-BW-SCJ3sSS8rbqcv1-e6yW2rupHDYNM9rHFf1FpMLcxy_cNVVZi_rUFS5gcguOR9cdIdlJn_925qAtbPFJfFSokS1S_ieOy7clQ3VHVS7oNQehLzNoAjKQZIzDs4F_gPai4jQXE7yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انفجارات عنيفة في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/93024" target="_blank">📅 22:55 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93023">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">الله اكبر
🇾🇪
اليمن تفرض حصار جوي على السعودية</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/93023" target="_blank">📅 22:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93022">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">السفارة الكندية في الرياض
: نحذر من احتمال فرض قيود على المجال الجوي واضطراب الرحلات الجوية في السعودية.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/93022" target="_blank">📅 22:39 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93021">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇬🇧
🇸🇦
بريطانيا تنصح الآن بعدم سفر أي شخص إلى الرياض، في المملكة العربية السعودية.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/93021" target="_blank">📅 22:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93020">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇮🇶
حدث هام بعد قليل يخص الملف العراقي ..</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/93020" target="_blank">📅 22:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93019">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8NP5y4K3c-yWRgcVYNtOU4tGsnFc3LJweVDBGHm-t3ZAdGxL_JAqz2gQ-Wr6zOEQYxtPDH8wMm6x8qubEcnsXdWh1xmtNMP23evKZouaJ5oDJhv8DSG3tODmH7eDBSafRCbRjARgsT4-k8IKZL3kACTgG0uKcb7Loy2BrdO_L9IHdzFxrM8K6XqVpyybc32qZPWHCM_KkKuqVyiWoSFLk9h-cSV3p9YONATQor5Y9L7mk2nRFoGjEsAmPfY31ECPnyt1p3Ig-sp3MBTkHaukrrWfsey6dUNabKMr9fDIUmybwESqq34w3SMQ-Ho8b_6KMdsUT2SRuhgBLsdumnAzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الرصد اليومي لطلعات العدو الجوية التي يخرق بها السيادة العراقية.
يستمر العدو الأمريكي في انتهاكه الصارخ لسيادتنا الجوية، انطلاقا من قواعدهم في الأردن.
- طيران حربي نوع (F-35) عدد 1.
- طائرة تزود بالوقود (KC-135) عدد 2 .
- طائرات مسيّرة (MQ9) عدد 4 .
طائرة مسيّرة (MQ1) عدد 1.
طوال ساعات يوم الاربعاء 7-10-2026 .</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/93019" target="_blank">📅 21:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93018">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WceYn54n7FbBtpCCZIVNCHdEupLmVu74XP83Bd2gRnXXAWnAtPGRgioDPn2PXsMO6Hzq4LfG7mq-aeAjxAv5Zt60QyXIdk3GQ7XQNIFbbC1TrbmqMXaDR8k8bD2MJ_7MMqGAnqPrlSpm1-YiEFRKYuOW1tZJMQsTiEgCM3-68DarV9YsunSDjOAgybvXFuaDjPklFRvA5C61M6oGaFew30Qm91ppr3pvVUX3K-9D1-KItEKvIvCQGfSvrE0I0l-jODzQsAWdYR3gp5mRYshMzV6B8WTWAmZLUGFG90Gaju968UjxZO1ZiooIWw5ueCa0_HJf9w8ZbiyaIl4L0WMWSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
🇮🇶
🔻
الحشد الشعبي يمثل العراق في موسكو
حضور د مهند العقابي مع وزير الاتصالات ورئيس خلية الاعلام الأمني في مؤتمر الإعلام والذكاء الصناعي بمشاركة ٧٠ دولة حول العالم</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/93018" target="_blank">📅 21:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93017">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKMLh5eeulAVGOBizmHKsBQRDjEyt0G__AUPocbjSpUv55Qu8j8X8XqBLjDQTeXqIvtcgBspuKdc0r9NLtiClxQh3E9dVB3IdogH7YALTzfGLvvw0frNSU7jYetW_om_UyH3dD_GOTULUlX4vEUZJwPrykjuw0lGWIXofe816DB15HUu559kDO0tB3sgolnM2dFmQY0uo0FSsZ2RvwfqsFWhW_GItsGmORqb_6K8CufWjivF0V2AOP2iPORmBFN3Juf1-UJGjACg6Yd2i3ilKRQfEPr-hT_iNxDJ4fDoySjNahyxFF4nPytEjwzbYSvDdB1lutbv9IItVK3IzbFCPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
احد الجنود الصهاينة الذي قتل في جنوب لبنان اثر حادث عملياتي حسب وصفهم.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/93017" target="_blank">📅 21:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93016">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇷🇺
🇮🇷
بوتين
:  طلب من بزشكيان نقل أفضل التمنيات إلى المرشد الأعلى لإيران مجتبى خامنئي، روسيا مستعدة لفعل كل شيء لمساعدة إيران في تسوية الوضع الذي نشأ في الشرق الأوسط.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/93016" target="_blank">📅 21:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93015">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇮🇶
ازدياد حدة التظاهرات في محافظة البصرة بعد القرار الأخير برفع سعر الصرف.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/93015" target="_blank">📅 21:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93014">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇮🇶
مشاهد لطرد التحشيدات التابعة للعدو السعودي من مديرية الشمايتين بمحافظة تعز - 8 أكتوبر 2026م
.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/93014" target="_blank">📅 21:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93013">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇮🇶
🔻
كتائب سيد الشهداء تحسم الجدل
لا تسليم للسلاح إلا بعدما يكون العراق سيد نفسه .
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/93013" target="_blank">📅 21:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93012">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 59 غارةً جويةً وصاروخاً استهدف بها العاصمة صنعاء ومحافظات الجوف وتعز ومأرب وحجة وصعدة والحديدة ولحج وريمة وإب والبيضاء من خلال طائرات "F-15" و "تايفون" أقلعت من قاعدتي خميس مشيط والطائف والعدوان الصاروخي من نجران وخلفت شهداء وجرحى بينهم نساء وأطفال.
ليبلغ إجمالي غارات العدوان السعودي منذ بدء التصعيد على بلدِنا العزيز 1857 غارةً جويةً وصاروخاً.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/93012" target="_blank">📅 21:18 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93011">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇮🇶
رئيس مجلس النواب العراقي: قرار تغيير سعر الصرف لا رجعة عنه.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/93011" target="_blank">📅 21:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93010">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇶
رئيس مجلس الوزراء العراقي أمام مجلس النواب:  كانت أمامنا ثلاثة خيارات الأول الذهاب إلى الادّخار الإجباري وترك الموظف يعيش بالوعود والثاني توزيع الرواتب كل 45 يوماً والثالث الذهاب إلى الاقتراض وإغراق البلد بالديون وهو مثقل بها أصلاً، تسلّمتُ المهمة واقتصادنا…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/93010" target="_blank">📅 21:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93009">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇮🇶
مجموعة من النواب يعلنون استضافة رئيس الوزراء ووزير المالية ومحافظ البنك المركزي لمناقشة تداعيات قرار تغيير سعر الصرف.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/93009" target="_blank">📅 21:05 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93008">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇷
قائد الثورة الإسلامية سماحة السيد مجتبى الخامنئي:
إن تركيز العدو الأمريكي الصهيوني المجرم وإصراره على ضرب مختلف مستويات الفرج، من أعلى المستويات إلى أدنى مستوياته، كشف عن أهمية هذه المؤسسة أكثر من أي وقت مضى. ومع ذلك، فإن هذا الجهد اليائس والهجمات الخبيثة على أركان النظام والأمن الاجتماعي، والتي لا مثيل لها في التاريخ، لم تثنِ قوات الفرج الباسلة عن أداء مهمتها قيد أنملة، بل واصلت، حتى في الشوارع والسيارات، أداء الدور والواجبات نفسها التي كانت تؤديها في مواقعها ومقراتها.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/93008" target="_blank">📅 20:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93007">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlovO9uenAWHE1U0HE4agnyUSlkyPM_nVyPsbIh3MsRubo0piAKIKJKJIgx6gqkX0_3vESz1L42wr4XVKlzcKwqQfIJQxN9sJH24_SDhFDosYkZ2eSAVtk5IDsEd8LHONFMMKaK3g2xBe_TlPYcnFqd2zXbkoICZ-C-ktaC9DBrtBjlORSuausF0qKzJZpQDPzTrBFHoR_IJJm-89ZSBNAgp9JoiQsVC8kdpTLuo1GbhpVXrVrjN15kyZmD9ZPUjPHe3HEK2gfgkAQiKni8CCdVvT-953_n7Oe9w4cHiWJBeec9mUVjsODqqGKzanLFw5YJpNWAQPsQyNwmyUpyriQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔻
الشيخ اكرم الكعبي:
ندعو الإخوة في مجلس النواب والحكومة العراقية إلى النظر لهذه الاعتبارات، وتقديم أولوية مراعاة معيشة المواطن والعمل على خطط شفافة لإعادة الاستقرار في السوق بعيداً عن المهاترات السياسية.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/93007" target="_blank">📅 20:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93006">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feec5483db.mp4?token=eyy2kmKZCDM-GjIQrfeahbSFnY7S-fPMJ42Ky5TaEiB_BendRygSs6Nzx10YKDRVxzHhhiOwI-A0DFmTUbdNdZDZ6bi2c_fF7fQAWbhmPfYJvMUOkTWJ3NNnjP5IVLUxnBBUUQL5mAltHJn3Rfy6c5V8pxXI_9Cw6zel7dm-VFU2WrFu5B_igTYZKryp4FEmyBRPaVpGMfTIXKmXCu2F8D_CbGVigp3-6WfS25Fw5pdG9I-GWvRNKfCLbr_5IjHHEKLfepkNpwChto4Rb_hWyKMGmXKFpYrsPvvg1Hzcedo6SAUo77vvnwElWzGeQCngEmIQ0qM9IIG9L7UXpreMmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feec5483db.mp4?token=eyy2kmKZCDM-GjIQrfeahbSFnY7S-fPMJ42Ky5TaEiB_BendRygSs6Nzx10YKDRVxzHhhiOwI-A0DFmTUbdNdZDZ6bi2c_fF7fQAWbhmPfYJvMUOkTWJ3NNnjP5IVLUxnBBUUQL5mAltHJn3Rfy6c5V8pxXI_9Cw6zel7dm-VFU2WrFu5B_igTYZKryp4FEmyBRPaVpGMfTIXKmXCu2F8D_CbGVigp3-6WfS25Fw5pdG9I-GWvRNKfCLbr_5IjHHEKLfepkNpwChto4Rb_hWyKMGmXKFpYrsPvvg1Hzcedo6SAUo77vvnwElWzGeQCngEmIQ0qM9IIG9L7UXpreMmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
ازدياد حدة التظاهرات في محافظة البصرة بعد القرار الأخير برفع سعر الصرف.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/93006" target="_blank">📅 20:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93005">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e97ff80a1b.mp4?token=pd-3GETEktg2jSxtrKFTNkbjM470yhnYmDtRebs3QM7akt5a6TKNbJ8JIHj8JwAlVf7yewALlRlZSJJrPg6S_oTRCAAS5cQGZl7mZ7vTyIV9D_husFkPDxLYp7kNOeVvhv63P-X3ErkmqdnbYjXq4IG2mMeIBhPAtOdDPMG08PzQP8wZOGesFVKEBuBEN46moSZMMcz0J5YhoCv6JA7YKMWw1yDq6J0UCDe6YL0YEh761BeyvVMe0zWBQCONLKeXHhYQL005Txk_aT8juv5g5lXXscnkkKjuLpLvxSfyOWoSU3FlxlI8Mr-Qu4D6iR6ZmpQyutmB4J_zTXoi0u7bYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e97ff80a1b.mp4?token=pd-3GETEktg2jSxtrKFTNkbjM470yhnYmDtRebs3QM7akt5a6TKNbJ8JIHj8JwAlVf7yewALlRlZSJJrPg6S_oTRCAAS5cQGZl7mZ7vTyIV9D_husFkPDxLYp7kNOeVvhv63P-X3ErkmqdnbYjXq4IG2mMeIBhPAtOdDPMG08PzQP8wZOGesFVKEBuBEN46moSZMMcz0J5YhoCv6JA7YKMWw1yDq6J0UCDe6YL0YEh761BeyvVMe0zWBQCONLKeXHhYQL005Txk_aT8juv5g5lXXscnkkKjuLpLvxSfyOWoSU3FlxlI8Mr-Qu4D6iR6ZmpQyutmB4J_zTXoi0u7bYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
مقيمة في السعودية تشتكي وتناشد بفتح المطارات السعودية بعد اغلاقها بسبب هجمات قوات المسلحة اليمنية ليتسنى لها العودة إلى بلدها بعد بقائها في السعودية لعدة أسابيع.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/93005" target="_blank">📅 20:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93002">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xvyd1LOq3Wr1n1qmfCK4tRNQAV1hpaGpfadfi-A_3NpVJaay_ZskD8_wBnaOSlW9IDwKwTnhjILpsI5Tbcyvi6JDc1nOtSksNqbB0IvcIiC37NaYh21gxP-Sbx9jS2AdYKiM342kd05TZa7TPqd5jxdHX-S6svH1FZRr5hpi1GGRNIeMoMgIMPdiAckBWzMzFzKJQuaj1pIF__I0cfoir0bY3_wrOky7CAQGtvEevVm9gU76W1Jj---4iVFPLKA5TvaTyPk8e_oM4CNzIQSTna9PxwxMnIl5xdrZoNIm-pjBFSlQ2VIfOt6zqjU--C5WT-CyWCbbBN_qmnm69oNOaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rH9mAKSnnCHxFpvrdLeKCCUXaQyG4mPh9m3myWFRQd0grFTV1zON2Dx53JleeVstPEDVoLhVsZM1bKFWNabqdX_VWlQKYmIFUKdHd4RvpHWxFObPoihDmD1LH1arKkF2qa7S_oP-krhZ6k_PiQDmQo3T6tNPLhGsicjZFJ_jmfB8BkV_5KADHj8fbAq4V2ntMqOKYJEBhpig659s3irC33xFGBT7i5vkEEbQPCJ_00OflQD1K6qWBEEwplk6cu3OToeJfSvDsDy3lBfusMJu058Xs_Srn44QWqdMhpwgYsx7lavWys9KoUNK6xKp_eUULIC5GzTvYyNjcQO6yPnFMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qOwlnbBG1LX6DNTRRiQ65ZguKvshHWEpH8XC9tBiQ1VjDD_p2fEquseuOqRb88pIji2dAlmLDraYDSnDiht8vq6a5j-h6hCZ0utsBjFIbKcCYXM9QViWoVWpoQKqlJT2IFtrs9QJXke5CJLl652lkZvIkQ7tQHzNpgx1QixO-XhcrKOldDoGnwkbo7JmgumKzqO5j00ap6BF7BUJT8gNE2guwF5TRjy911uQUfcBj50Pc2ZBtGp4tmpWEkr2ylp8xkncFh1wB59nFirwMF_K9oSq1M0tmUS4H0PEt4yR9VXEO5iEg5U-KdkUDY2l5JvwO5a4cSF5kWDlw-bhQQMsWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
مجموعة من النواب يعلنون استضافة رئيس الوزراء ووزير المالية ومحافظ البنك المركزي لمناقشة تداعيات قرار تغيير سعر الصرف.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/93002" target="_blank">📅 20:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93001">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/731963d562.mp4?token=u4_Iy5kl1jW5Fc-5AlcWv-BoUcVVsEtHE6RHgVS5lMIWqg_IGO5gyWOXz4aX7mm6P1F1Pc8W1oKjewHll0QgzgMIwjF3gklLVoYjaTdZ5Y_Ii2tGuG-CfJ-DOvQn9Kpew1DqhSEB1cPreeBdCymdoVUdAi94VbRi5HVSbgyOsW9UKBmQaxQX5_CAdtQuXD9gdGSAGOOQeIDDRPPAltEj27AkL4GwAvSc4ZS4EjAKV_YKWFKITokwEV78I-gMGYQzI7N904nT2iDJBu7-xobeU-IbjiExlSg4OMC6cmHygtZ3m6fk5apyWUtlA1lHbCH2ZdTAMtTbmf8lR8FY-uVsjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/731963d562.mp4?token=u4_Iy5kl1jW5Fc-5AlcWv-BoUcVVsEtHE6RHgVS5lMIWqg_IGO5gyWOXz4aX7mm6P1F1Pc8W1oKjewHll0QgzgMIwjF3gklLVoYjaTdZ5Y_Ii2tGuG-CfJ-DOvQn9Kpew1DqhSEB1cPreeBdCymdoVUdAi94VbRi5HVSbgyOsW9UKBmQaxQX5_CAdtQuXD9gdGSAGOOQeIDDRPPAltEj27AkL4GwAvSc4ZS4EjAKV_YKWFKITokwEV78I-gMGYQzI7N904nT2iDJBu7-xobeU-IbjiExlSg4OMC6cmHygtZ3m6fk5apyWUtlA1lHbCH2ZdTAMtTbmf8lR8FY-uVsjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مجموعة من النواب يعلنون استضافة رئيس الوزراء ووزير المالية ومحافظ البنك المركزي لمناقشة تداعيات قرار تغيير سعر الصرف.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/93001" target="_blank">📅 20:11 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93000">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇺🇸
🇸🇦
البعثة الأمريكية في السعودية تصدر تحذير امني لبعثتها خوفا من الهجمات اليمنية.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/93000" target="_blank">📅 20:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92999">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRhLFL2XyHsfDiCS8QPAhVbBompDZEu_lIpWUvO8O4hys4vBzlWJoTw5PKyae668pv0yCFTx92Fznk6I6BrkfhZPkrbGg7mv0UV-rrISmHfE5qClEzSeTS4AEs1gvfcMT9eLMYe7IR0A5SLEbFkc4mSWWi-cSXaqEsyqbOYfO6k76WgSShkcqwmx-pMrYVMuh11KeXag3uyQibLcT9UZlZyWb9GU4Z45tAvTNlGDZEeWAzv2atdi3IHSRfGuhaCku9ubHTeZjC31CodMLPhxvLBq6zDNRnScjZkM4a81BEOYoWeT8S6VGp_VA8pGjzQ88gMgfTvX3CXvEXrb2E66Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔻
المعاون العسكري لحركة النجباء الحاج عبد القادر الكربلائي:
فيا أنصار الله ورسوله والإسلام، إننا معكم ولن نتخلى عنكم.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/92999" target="_blank">📅 20:05 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92998">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqvMFLaXrXrIpPCK_NG2VcEasASuzPutGjX0p8HxVMfhMrgNkWIWaBnw59lNLOidAqDg5B3X4c0mzFLmeEogyurkE-H7qzjg-jhQI0TAx61UvvanJquIgv9QvRK_P2HoxsoMEJN5PxvgLT2PHVE2Z7vLZVdEh_9CBxd5VJ2j1HJ7kwud6paqy2Hlouu987wC0S3NhmCTFOfiAVVF7bXnnNUgxawcVT2JFg6sRwf2BQm_a5ITMQ6I-O-HXfQUWMYAVbWfXLvhX-Hy9SPH7EDQmUEhgBQEiEr1K3tt6vMYnO7dnu4sVwaMxlJ69fzldAQrCSalxyX0dKkYY6JT-R_ksQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب: لن نشن هجومًا على إيران في أي وقت قبل الانتخابات النصفية، نحن نجري محادثات مثمرة مع إيران.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/92998" target="_blank">📅 19:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92997">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZkc0YYEzN5N7ak400nlzHIkcNlAdSMTq7SZDj9PTpwWEk_cul6EKeCI9kUPlqDQdsfpmIzYmQlVcGSQrD23M-ZZI-xEQG4sjTaLeOaP4xRFDo4G8nzM9JsO5GxYxJDrFegSYfKUse8F693Sfy0kvAwPkEXmnuUTDZkeTBHyAphmhW4RTHnuYe4WSz_PFSH6JCU2lgpgZxCJ6WAjwzVWCDpxIsupXm2jLp9Ffnl0rZ6vqIX7K2I7wMSF7f2xLE5qSADvvtJkH_GGNn1QmMCp_gwK4rsVYD1cQRpZzaOQw8wZ3vFVJmBK7ZSdhotV6_Zj2lZh_q6ZwPh5AC7p-xKNaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
: لن نشن هجومًا على إيران في أي وقت قبل الانتخابات النصفية، نحن نجري محادثات مثمرة مع إيران.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/92997" target="_blank">📅 19:48 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92996">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">تدمير طائرة في مطار الرياض الدولي</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/92996" target="_blank">📅 19:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92995">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇶
‏
مستشار الأمن القومي العراقي:
العراق رفض طلبا من سوريا لإعادة آلاف الأشخاص المشتبه في انتمائهم إلى داعش، اجتماع عُقد مؤخرا بين سوريا والعراق وأميركا لبحث مصير سجناء داعش، العراق أعاد إلى سوريا نحو 50 محتجزا سوريا ثبت أنهم ليسوا أعضاء في داعش.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/92995" target="_blank">📅 19:38 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92994">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sv7iCY6xEnQJuqRNKDMQJbnKuEE7TQTsYE5kP3IOEeLpCMeunpxEV48a8kBjYXDHJ6S3XCD3cLQGezBynujM6TRkh73I40K0Ikl2xQBZEQlHmNZpJG6tGu5ss_ctTaGUAAkUHOa2OfMk1KuGjXJNy9nX7x2KMQaM7Lf8am3VEg4t8IqxeB9Gf2MbeWWXiNXP2Z3iSkpzr5AvU-_5Oj8jQTmtEy2eT1sMibDzkSGz4_4Ha_6qsD4lDUXPQOA-Rg6_djqjvlu7h6s6yGbaHSxjxtSgr399bg67JHaRSlgoMpxsMd-0LuEVysRJqJm5F0VcphUAkRlBTE8Y8shenN4DyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظة الهجوم اليمني على مطار الرياض الدولي</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/92994" target="_blank">📅 19:23 · 16 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
